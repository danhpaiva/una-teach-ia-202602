def agente_aspirador(percepcao):
    local, estado = percepcao
    if estado == "sujo":
        return "aspirar"
    if local == "A":
        return "ir_para_B"
    return "ir_para_A"

print(agente_aspirador(("A", "sujo")))
print(agente_aspirador(("A", "limpo")))
print(agente_aspirador(("B", "limpo")))
