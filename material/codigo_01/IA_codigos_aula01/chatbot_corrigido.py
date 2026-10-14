# Gabarito dos exercicios 1 e 2: nova regra ("obrigado") e correcao do bug
# ("boa noite" contem "oi"): compara palavras inteiras com split().
REGRAS = {
    "oi": "Olá! Como posso ajudar?",
    "preço": "Nossos planos começam em R$ 29.",
    "horário": "Atendemos de segunda a sexta, 8h às 18h.",
    "obrigado": "Por nada!",
    "tchau": "Até logo!",
}

def responder(texto):
    palavras = texto.lower().split()
    for palavra, resposta in REGRAS.items():
        if palavra in palavras:
            return resposta
    return "Não entendi."

while True:
    entrada = input("Você: ")
    resposta = responder(entrada)
    print("Bot:", resposta)
    if resposta == "Até logo!":
        break
