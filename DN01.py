teza = int(input("Vnesi teza: "))
koraki = 1
kolicinaGoriva = 0

while teza > 0:
    teza2 = int(teza / 3 - 2)
    print(koraki,". ", teza, " / 3 - 2 = ", teza2)
    teza = teza2
    koraki+=1
    if teza2 > 0:
        kolicinaGoriva += teza2

print(koraki-1, kolicinaGoriva)