rede = {
    "animal":  {"tem": "pele"},
    "ave":     {"e_um": "animal", "voa": True, "tem": "penas"},
    "canario": {"e_um": "ave", "cor": "amarelo"},
    "pinguim": {"e_um": "ave", "voa": False},
}

def propriedade(no, prop):
    while no is not None:
        if prop in rede[no]:
            return rede[no][prop]
        no = rede[no].get("e_um")
    return None

print(propriedade("canario", "voa"))
print(propriedade("pinguim", "voa"))
print(propriedade("canario", "tem"))
print(propriedade("pinguim", "cor"))
