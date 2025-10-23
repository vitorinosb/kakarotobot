# bot.py - Kakaroto Albatross v3.0 (MAINNET - FINAL)
import time
import os
from hyperliquid.exchange import Exchange
from hyperliquid.utils import constants

# === CHAVES ===
ACCOUNT_ADDRESS = os.environ.get("ACCOUNT_ADDRESS")
SECRET_KEY = os.environ.get("SECRET_KEY")

if not ACCOUNT_ADDRESS or not SECRET_KEY:
    print("ERRO: CHAVES NÃO CONFIGURADAS")
    exit(1)

# === CONEXÃO CORRETA ===
exchange = Exchange(
    address=ACCOUNT_ADDRESS,
    private_key=SECRET_KEY,
    base_url=constants.MAINNET_API_URL
)

print("KAKAROTO ALBATROZ v3.0 INICIADO (MAINNET)")

# === LOOP 24/7 ===
while True:
    try:
        price = exchange.info.all_mids().get("BTC")
        print(f"Bot rodando... Preço BTC: ${price}")
        time.sleep(30)
    except Exception as e:
        print("Erro:", e)
        time.sleep(60)
