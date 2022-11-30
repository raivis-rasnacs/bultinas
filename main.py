skaits = 6
virkne_str = "><<><>"

for pozicija in range(0, skaits):
    virkne = list(virkne_str)
    gajieni = 0
    if virkne[pozicija] == "<":
        virziens = -1
    elif virkne[pozicija] == ">":
        virziens = 1

    pozicija += virziens
    while pozicija in range(0, skaits):
        
        if virkne[pozicija] == ">" and virziens == 1:
            virkne[pozicija] = "<"
            virziens = -1
            gajieni += 1
        elif virkne[pozicija] == "<" and virziens == -1:
            virkne[pozicija] = ">"
            virziens = 1
            gajieni += 1
        
        pozicija += virziens

    print(gajieni + 1)