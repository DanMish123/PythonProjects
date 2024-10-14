ovire = [(1, 3, 3), (2, 4, 3), (4, 6, 5),
         (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8)]

def najdaljsaPot(ovire):
    vrsticaStolpec = []
    for x in range(1, 11):
        seznamY = []
        for x1, x2, y in ovire:
            if x1 <= x <= x2:
                seznamY.append(y)
        if not seznamY:
            return False
        else:
            vrsticaStolpec.append((x,min(seznamY)))
    return vrsticaStolpec

ovire2 = najdaljsaPot(ovire)
if ovire2:
    najdaljsaY = 0
    najdaljsaX = None
    for x,y in ovire2:
        if y > najdaljsaY:
            najdaljsaY = y
            najdaljsaX = x
    print(najdaljsaX, ',', najdaljsaY)
else:
    print("Zmaga!")
