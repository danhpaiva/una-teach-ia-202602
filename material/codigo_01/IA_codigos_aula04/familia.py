pai = {("joao", "maria"), ("joao", "pedro"),
       ("maria", "ana"), ("pedro", "lucas")}

def avos(pai):
    return {(x, z) for (x, y1) in pai
            for (y2, z) in pai if y1 == y2}

def irmaos(pai):
    return {(a, b) for (p1, a) in pai for (p2, b) in pai
            if p1 == p2 and a != b}

print(sorted(avos(pai)))
print(sorted(irmaos(pai)))
