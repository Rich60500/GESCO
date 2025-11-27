"""
Script de test pour diagnostiquer l'API Sonepar - V2
Test avec différents formats de clé API
"""
import requests
import json

# Configuration - TESTS MULTIPLES
CUSTOMER_CODE = "4146EB1"
ORG_ID = "5QD"
BASE_URL = "https://apitst.sonepar.fr/api"

# Différents formats de clé à tester
API_KEYS_TO_TEST = [
    "95791076",
    "95791076-DENIS EURL-5QD",
    "95791076-DENIS-EURL-5QD",
]

print("=" * 60)
print("TEST API SONEPAR - Diagnostic V2")
print("Test de différents formats de clé API")
print("=" * 60)
print(f"\nConfiguration:")
print(f"  Base URL: {BASE_URL}")
print(f"  Customer Code: {CUSTOMER_CODE}")
print(f"  Org ID: {ORG_ID}")
print("\n" + "=" * 60)

for idx, api_key in enumerate(API_KEYS_TO_TEST, 1):
    print(f"\n[TEST {idx}] Tentative avec clé: '{api_key}'")
    print("-" * 60)

    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "customerCode": CUSTOMER_CODE,
        "orgId": ORG_ID,
        "Accept": "application/json"
    }

    try:
        # Test sur /products/v1/brands
        response = requests.get(
            f"{BASE_URL}/products/v1/brands",
            headers=headers,
            timeout=10
        )

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"✓✓✓ SUCCÈS !!! ✓✓✓")
            print(f"La bonne clé API est: '{api_key}'")
            data = response.json()
            print(f"Nombre de marques: {len(data.get('brands', []))}")
            if data.get('brands'):
                print(f"Exemples de marques:")
                for brand in data['brands'][:5]:
                    print(f"  - {brand}")
            break
        else:
            print(f"✗ ÉCHEC - {response.status_code}")
            print(f"Message: {response.text[:200]}")

    except Exception as e:
        print(f"✗ ERREUR: {e}")

print("\n" + "=" * 60)
print("FIN DES TESTS")
print("=" * 60)
