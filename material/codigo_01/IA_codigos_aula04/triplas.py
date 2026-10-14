triplas = [
    ("curitiba", "capital_de", "parana"),
    ("parana", "pertence_a", "brasil"),
    ("brasil", "idioma", "portugues"),
    ("curitiba", "fundada_em", 1693),
]

def consulta(s=None, p=None, o=None):
    return [t for t in triplas
            if (s is None or t[0] == s)
            and (p is None or t[1] == p)
            and (o is None or t[2] == o)]

print(consulta(s="curitiba"))
print(consulta(p="pertence_a"))
estado = consulta(s="curitiba", p="capital_de")[0][2]
print(consulta(s=estado, p="pertence_a")[0][2])
