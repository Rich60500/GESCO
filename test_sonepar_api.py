"""
Script de test pour diagnostiquer l'API Sonepar
"""
import requests
import json

# Configuration
API_KEY = "95791076"
CUSTOMER_CODE = "4146EB1"
ORG_ID = "5QD"
BASE_URL = "https://apitst.sonepar.fr/api"

print("=" * 60)
print("TEST API SONEPAR - Diagnostic")
print("=" * 60)
print(f"\nConfiguration:")
print(f"  Base URL: {BASE_URL}")
print(f"  API Key: {API_KEY}")
print(f"  Customer Code: {CUSTOMER_CODE}")
print(f"  Org ID: {ORG_ID}")
print("\n" + "=" * 60)

# Test 1: GET /products/v1/brands (sans auth user/pass)
print("\n[TEST 1] GET /products/v1/brands (sans user/pass)")
print("-" * 60)

headers_brands = {
    "Ocp-Apim-Subscription-Key": API_KEY,
    "customerCode": CUSTOMER_CODE,
    "orgId": ORG_ID,
    "Accept": "application/json"
}

try:
    response = requests.get(
        f"{BASE_URL}/products/v1/brands",
        headers=headers_brands,
        timeout=10
    )

    print(f"Status Code: {response.status_code}")
    print(f"Headers envoyés: {json.dumps(headers_brands, indent=2)}")

    if response.status_code == 200:
        print(f"✓ SUCCÈS !")
        data = response.json()
        print(f"Nombre de marques: {len(data.get('brands', []))}")
        if data.get('brands'):
            print(f"Première marque: {data['brands'][0]}")
    else:
        print(f"✗ ÉCHEC")
        print(f"Réponse: {response.text[:500]}")

except Exception as e:
    print(f"✗ ERREUR: {e}")

# Test 2: GET /products/v1/catalogs (sans auth user/pass)
print("\n\n[TEST 2] GET /products/v1/catalogs?page=1&responseType=json (sans user/pass)")
print("-" * 60)

headers_catalog = {
    "Ocp-Apim-Subscription-Key": API_KEY,
    "customerCode": CUSTOMER_CODE,
    "orgId": ORG_ID,
    "Accept": "application/json"
}

try:
    response = requests.get(
        f"{BASE_URL}/products/v1/catalogs",
        headers=headers_catalog,
        params={
            'page': 1,
            'responseType': 'json'
        },
        timeout=10
    )

    print(f"Status Code: {response.status_code}")
    print(f"Headers envoyés: {json.dumps(headers_catalog, indent=2)}")

    if response.status_code == 200:
        print(f"✓ SUCCÈS !")
        data = response.json()
        print(f"Nombre de produits: {len(data.get('products', []))}")
        if data.get('products'):
            print(f"Premier produit: {json.dumps(data['products'][0], indent=2)[:500]}")
    else:
        print(f"✗ ÉCHEC")
        print(f"Réponse: {response.text[:500]}")

except Exception as e:
    print(f"✗ ERREUR: {e}")

# Test 3: Vérifier la structure complète de la réponse d'erreur si 404
print("\n\n[TEST 3] Détails de la dernière erreur")
print("-" * 60)
if response.status_code != 200:
    print(f"Status: {response.status_code}")
    print(f"Reason: {response.reason}")
    print(f"URL complète: {response.url}")
    print(f"Headers de réponse:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")
    print(f"\nCorps de la réponse:")
    print(response.text)

print("\n" + "=" * 60)
print("FIN DES TESTS")
print("=" * 60)
