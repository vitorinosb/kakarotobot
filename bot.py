# bot.py - KAKAROTO ALBATROZ v3.0 (MAINNET - SDK OFICIAL)
import time
import os
from hyperliquid import Exchange
from hyperliquid.utils import constants

# === API KEY + SECRET (DO PAINEL DA HYPERLIQUID) ===
API_KEY = "0x22a436a08974e5ff08806c15939408f00063741a"
API_SECRET = "0xa5251a7cf438bf0226ee37243607952dd36efc312b6bbd59559d7ad0c2c9ffd1"

# === VALIDAÇÃO ===
if not API_KEY.startswith("0x") or not API_SECRET.startswith("0x"):
    print("ERRO: API_KEY ou API_SECRET inválidos")
    exit(1)

# === CONEXÃO COM SDK OFICIAL ===
try:
    exchange = Exchange(
        api_key=API_KEY,
        secret=API_SECRET,
        base_url=constants.MAINNET_API_URL
    )
    print("CONEXÃO ESTABELECIDA COM HYPERLIQUID MAINNET (SDK OFICIAL)")
except Exception as e:
    print(f"ERRO NA CONEXÃO: {e}")
    exit(1)

print("KAKAROTO ALBATROZ v3.0 INICIADO (MAINNET)")

# === LOOP 24/7 ===
while True:
    try:
        mids = exchange.get_mid_prices()
        btc_price = mids.get("BTC")
        if btc_price:
            print(f"Bot rodando... Preço BTC: ${float(btc_price):,.2f}")
        else:
            print("Bot rodando... (sem preço BTC)")
        time.sleep(30)
    except Exception as e:
        print(f"ERRO NO LOOP: {e}")
        time.sleep(60)
