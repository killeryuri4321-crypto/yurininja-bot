
import requests
import time
import os
import random

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": mensagem
    })

sinais = [
    "🎯 BLAZE DOUBLE\nEntrada: 🔴 VERMELHO\nProteção: ⚪ BRANCO",
    "🎯 BLAZE DOUBLE\nEntrada: ⚫ PRETO\nProteção: ⚪ BRANCO",
    "🎯 BLAZE CRASH\nEntrar após 1.50x\nSaída em 2.00x",
]

while True:
    sinal = random.choice(sinais)
    enviar(sinal)
    time.sleep(1800)  # envia a cada 30 minutos
