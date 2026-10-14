frame_carro = {"rodas": 4, "motor": "combustao",
               "portas": 4}
meu_carro = {"herda": frame_carro, "cor": "azul",
             "motor": "eletrico"}

def slot(frame, nome):
    while frame is not None:
        if nome in frame:
            return frame[nome]
        frame = frame.get("herda")
    return None

print(slot(meu_carro, "cor"))
print(slot(meu_carro, "motor"))
print(slot(meu_carro, "rodas"))
print(slot(meu_carro, "teto"))
