"""
Dust Detector — поиск пылевых UTXO на заданном Bitcoin-адресе.
"""

import requests
import argparse

DUST_THRESHOLD = 546  # сатоши

def fetch_utxos(address):
    url = f"https://api.blockchair.com/bitcoin/dashboards/address/{address}"
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("❌ Ошибка запроса к Blockchair API.")
    utxos = r.json()["data"][address]["utxo"]
    return utxos

def detect_dust(utxos):
    dust = [u for u in utxos if u["value"] <= DUST_THRESHOLD]
    print(f"🔍 Найдено {len(dust)} пылевых UTXO (≤ {DUST_THRESHOLD} сатоши):")
    for u in dust:
        print(f"  - {u['transaction_hash']}:{u['index']} — {u['value']} сатоши")

    print(f"
📦 Всего UTXO на адресе: {len(utxos)}")
    print(f"💸 Общая сумма пыли: {sum(u['value'] for u in dust)} сатоши")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dust Detector — поиск пылевых UTXO.")
    parser.add_argument("address", help="Bitcoin-адрес для анализа")
    args = parser.parse_args()

    utxos = fetch_utxos(args.address)
    detect_dust(utxos)
