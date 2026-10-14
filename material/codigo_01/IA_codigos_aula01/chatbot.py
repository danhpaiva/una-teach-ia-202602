REGRAS = {
    "oi": "Olá! Como posso ajudar?",
    "preço": "Nossos planos começam em R$ 29.",
    "horário": "Atendemos de segunda a sexta, 8h às 18h.",
    "tchau": "Até logo!",
}

def responder(texto):
    texto = texto.lower()
    for palavra, resposta in REGRAS.items():
        if palavra in texto:
            return resposta
    return "Não entendi. Pode reformular?"

while True:
    entrada = input("Você: ")
    resposta = responder(entrada)
    print("Bot:", resposta)
    if resposta == "Até logo!":
        break
