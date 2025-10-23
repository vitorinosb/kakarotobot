# bot.py - Kakaroto Albatross v3.0 (MAINNET - ORDEM CORRETA)
import time
import os
from hyperliquid.exchange import Exchange
from hyperliquid.utils import constants

# === CHAVES FIXAS (CORRETAS) ===
ACCOUNT_ADDRESS = "0x22a436a08974e5ff08806c15939408f00063741a"
SECRET_KEY = "0xa5251a7cf438bf0226ee37243607952dd36efc312b6bbd59559d7ad0c2c9ffd1"

# === VALIDAÇÃO ===
if not ACCOUNT_ADDRESS or not SECRET_KEY:
    print("ERRO: CHAVES NÃO CONFIGURADAS")
    exit(1)

# === CONEXÃO: ORDEM CORRETA (address, private_key, base_url) ===
try:
    exchange = Exchange(
        ACCOUNT_ADDRESS,      # ← 1º: endereço
        SECRET_KEY,           # ← 2º: chave privada
        constants.MAINNET_API_URL  # ← 3º: URL da API
    )
    print("CONEXÃO ESTABELECIDA COM HYPERLIQUID MAINNET")
except Exception as e:
    print(f"ERRO NA CONEXÃO: {e}")
    exit(1)

print("KAKAROTO ALBATROZ v3.0 INICIADO (MAINNET)")

# === LOOP 24/7 ===
while True:
    try:
        mids = exchange.info.all_mids()
        btc_price = mids.get("BTC")
        if btc_price:
            print(f"Bot rodando... Preço BTC: ${float(btc_price):,.2f}")
        else:
            print("Bot rodando... (sem preço BTC)")
        time.sleep(30)
    except Exception as e:
        print(f"ERRO NO LOOP: {e}")
        time.sleep(60)
