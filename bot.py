# bot.py - Kakaroto Albatross v3.0 (MAINNET - 24/7)
import time
import os
from hyperliquid.exchange import Exchange
from hyperliquid.utils import constants

# === CHAVES VIA ENV (RENDER) ===
ACCOUNT_ADDRESS = os.environ.get("ACCOUNT_ADDRESS")
SECRET_KEY = os.environ.get("SECRET_KEY")

if not ACCOUNT_ADDRESS or not SECRET_KEY:
    print("ERRO: CHAVES NÃO CONFIGURADAS")
    exit(1)

# === CONEXÃO ===
exchange = Exchange(0x22a436a08974e5ff08806c15939408f00063741a, 0xa5251a7cf438bf0226ee37243607952dd36efc312b6bbd59559d7ad0c2c9ffd1, base_url=constants.MAINNET_API_URL)

# === LOOP 24/7 ===
print("KAKAROTO ALBATROZ v3.0 INICIADO (MAINNET)")
while True:
    try:
        print("Bot rodando... Preço BTC:", exchange.info.all_mids().get("BTC"))
        time.sleep(30)
    except Exception as e:
        print("Erro:", e)
        time.sleep(60)
