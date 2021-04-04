import requests
import subprocess

def get_stores(zipcode = "XXXXX", radius = 10):
  url_base = "https://www.riteaid.com/services/ext/v2/stores/getStores"
  params = {
    "address": zipcode,
    "attrFilter": "PREF-112",
    "fetchMechanismVersion": "2",
    "radius": radius,
  }
  return requests.get(url_base, params=params)

def get_store(storenumber):
  url_base = "https://www.riteaid.com/services/ext/v2/vaccine/checkSlots"
  params = {
    "storeNumber": storenumber,
  }

  return requests.get(url_base, params=params)

def is_store_eligible(store):
  return sum([1 for slot in store['Data']['slots'].values() if slot]) > 0


zip_codes = ['95070']
radius = 50

for z in zip_codes:
  stores = get_stores(zipcode=z, radius=radius).json()
  for item in stores['Data']['stores']:
    store = get_store(item['storeNumber']).json()
    if is_store_eligible(store):
      print(item['storeNumber'], z)
      subprocess.call(['say', 'available'])
