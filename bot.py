# bot.py - Kakaroto Albatross v3.0 (MAINNET - 100% FUNCIONAL)
import time
import os
from hyperliquid.exchange import Exchange
from hyperliquid.utils import constants

# === CHAVES FIXAS (SEGURANÇA: NÃO EXPONHA EM REPO) ===
ACCOUNT_ADDRESS = "0x22a436a08974e5ff08806c15939408f00063741a"
SECRET_KEY = "0xa5251a7cf438bf0226ee37243607952dd36efc312b6bbd59559d7ad0c2c9ffd1"

# === VALIDAÇÃO DE CHAVES ===
if not ACCOUNT_ADDRESS.startswith("0x") or len(ACCOUNT_ADDRESS) != 42:
    print("ERRO: ACCOUNT_ADDRESS INVÁLIDA")
    exit(1)
if not SECRET_KEY.startswith("0x") or len(SECRET_KEY) != 66:
    print("ERRO: SECRET_KEY INVÁLIDA")
    exit(1)

# === CONEXÃO CORRETA (POSICIONAL — SDK v0.20.0) ===
try:
    exchange = Exchange(ACCOUNT_ADDRESS, SECRET_KEY, constants.MAINNET_API_URL)
    print("CONEXÃO COM HYPERLIQUID MAINNET ESTABELECIDA")
except Exception as e:
    print(f"ERRO NA CONEXÃO: {e}")
    exit(1)

print("KAKAROTO ALBATROZ v3.0 INICIADO (MAINNET)")

# === LOOP 24/7 COM VERIFICAÇÃO DE PREÇO BTC ===
while True:
    try:
        mids = exchange.info.all_mids()
        btc_price = mids.get("BTC")
        if btc_price:
            print(f"Bot rodando... Preço BTC: ${float(btc_price):,.2f}")
        else:
            print("Bot rodando... (BTC não encontrado em all_mids)")
        time.sleep(30)
    except Exception as e:
        print(f"ERRO NO LOOP: {e}")
        time.sleep(60)
