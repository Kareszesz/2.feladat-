import string
import random

fajl = input("Add meg hogy melyik fájlt szeretnéd beolvasni (pl: ki.txt): ")
with open(fajl, "r", encoding="utf-8") as f:
    lines = f.readlines()


def main():

            num = []
            words = []

            for line in lines:
                parts = line.strip().split(";")
                
                if not any(char.isdigit() for char in parts):
                    words.extend(parts)
                else:
                    num.extend(parts)

            while True:
                if not words:
                    print(f"Csak számok vannk a txt-ben! \n     -A számaid: {num}!")     
                    szamok()
                    uj_elem_csak_num()
                    break
                elif not num:
                    print(f"Csak szók vannk a txt-ben! \n     -A szavaid: {words}!")
                    szavak()
                    uj_elem_csak_words()
                    print()
                    break
                else:
                    print(f"""\n     A txt fáljban számok és szavak is vannak!
                -A számaid: {num}
                -A szavaid: {words}""")
                    tovabb = input("""
                -Ha megakarod szakítani a programot 0-át írj!   
                -Ha folytatni szeretnéd 1-est írj!\n                     Írd ide: """)
                    if tovabb == "0":
                        print("Megszakítás...")
                        break
                    elif tovabb == "1":
                        sza_v_szo = input("""Szeretnél a számokkal és szavakkal is dolgozni?
                -Ha igen 1-est írj!
                -Ha nem 2-est írj!\n             Írd ide: """)
                        if sza_v_szo == "1":
                            szamok()
                            szavak()
                            uj_elem()
                            break
                        elif sza_v_szo == "2":
                            melyik = input("""Melyikkel szeretnél?
                -Ha a számokkal 1-est írj!
                -Ha a szavakkal 2-est írj!\n             Írd ide: """)
                            if melyik == "1":
                                szamok()
                                uj_elem_csak_num()
                                break
                            elif melyik == "2":
                                szavak()
                                uj_elem_csak_words()
                                break
                            else:
                                print("Nem értelmezhető! Válasz a két opció közül!")
                        else:
                            print("Nem értelmezhető! Válasz a két opció közül!")
                    else:
                        print("Nem értelmezhető! Válasz a két opció közül!")

def szamok():

    num = []
    words = []

    for line in lines:
        parts = line.strip().split(";")
        
        if not any(char.isdigit() for char in parts):
            words.extend(parts)
        else:
            num.extend(parts)

    num = list(map(int, num))

            
    while True:
        rendezes = input("""\n Milyen rendezéssel szeretnéd a számokat? 
                        -Ha egyszerű cserés rendezéssel 1-est írj
                        -Ha merge rendezéssel 2-est írj!\n        Írd ide: """)
        if rendezes == "1":
            novcsok = input("Növekvő vagy csökkenő sorrendben szeretnéd? (n/c)\n             Írd ide: ")
            if novcsok == "c":
                print(f"Csökkenő csere rendezést választottál: {csere_rendezes(num, novekvo=False)}")
                break
            elif novcsok == "n":
                print(f"Növekvő csere rendezést választottál: {csere_rendezes(num, novekvo=True)}")
                break
            else:
                print("Nem értelmezhető, próbáld újra!")
        elif rendezes == "2":
            novcsok = input("Növekvő vagy csökkenő sorrendben szeretnéd? (n/c)\n             Írd ide: ")
            if novcsok == "c":
                print(f"Csökkenő merge rendezést választottál: {merge_rendezes(num, novekvo=False)}")
                break
            elif novcsok == "n":
                print(f"Növekvő merge rendezést választottál: {merge_rendezes(num, novekvo=True)}")
                break
            else:
                print("Nem értelmezhető, próbáld újra!")
        else:
            print("Nem értelmezhető, próbáld újra!")


def szavak():

    num = []
    words = []

    for line in lines:
        parts = line.strip().split(";")
        
        if not any(char.isdigit() for char in parts):
            words.extend(parts)
        else:
            num.extend(parts)
    while True:
        rendezes = input("""\n Milyen rendezéssel szeretnéd a szavakat? 
                        -Ha egyszerű cserés rendezéssel 1-est írj
                        -Ha merge rendezéssel 2-est írj!\n        Írd ide: """)
        if rendezes == "1":
            novcsok = input("Növekvő vagy csökkenő sorrendben szeretnéd? (n/c)\n             Írd ide: ")
            if novcsok == "c":
                print(f"Csökkenő csere rendezést választottál: {csere_rendezes(words, novekvo=True)}")
                break
            elif novcsok == "n":
                print(f"Növekvő csere rendezést választottál: {csere_rendezes(words, novekvo=False)}")
                break
            else:
                print("Nem értelmezhető, próbáld újra!")
        elif rendezes == "2":
            novcsok = input("Növekvő vagy csökkenő sorrendben szeretnéd? (n/c)\n             Írd ide: ")
            if novcsok == "c":
                print(f"Csökkenő merge rendezést választottál: {merge_rendezes(words, novekvo=True)}")
                break
            elif novcsok == "n":
                print(f"Növekvő merge rendezést választottál: {merge_rendezes(words, novekvo=False)}")
                break
            else:
                print("Nem értelmezhető, próbáld újra!")
        else:
            print("Nem értelmezhető, próbáld újra!")        

def csere_rendezes(lista, novekvo=True):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if novekvo:
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                if lista[j] < lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def merge_rendezes(lista, novekvo=True):
    if len(lista) > 1:
        mid = len(lista) // 2
        L = lista[:mid]
        R = lista[mid:]

        merge_rendezes(L, novekvo)
        merge_rendezes(R, novekvo)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if (L[i] < R[j] and novekvo) or (L[i] > R[j] and not novekvo):
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
    return lista

def uj_elem():    
    num = []
    words = []

    for line in lines:
        parts = line.strip().split(";")
        
        if not any(char.isdigit() for char in parts):
            words.extend(parts)
        else:
            num.extend(parts)


    while True:
        uj_elem = input("\nSzeretnél új elemet hozzáadni a rendezett listához? (i/n)\n             Írd ide: ")
        if uj_elem == "i":
            novcsok = input("Növekvő vagy csökkenő sorrendben szeretnéd? (n/c)\n             Írd ide: ")
            szam_v_szo = input("Add meg az új elemet (szám vagy szöveg): ")
            
            if not any(char.isdigit() for char in szam_v_szo):
                words.append(szam_v_szo)
            else:
                num.append(szam_v_szo)

            if novcsok == "c":
                num = list(map(int, num))
                rendezett_szamok = merge_rendezes(num, novekvo=False)
                rendezett_szavak = merge_rendezes(words, novekvo=True)
                vegleges_lista = rendezett_szavak + list(map(str, rendezett_szamok))
                print(f"Csökkenő sorrendben rendezett lista: {vegleges_lista}")
            elif novcsok == "n":
                num = list(map(int, num))
                rendezett_szamok = merge_rendezes(num, novekvo=True)
                rendezett_szavak = merge_rendezes(words, novekvo=False)
                vegleges_lista = rendezett_szavak + list(map(str, rendezett_szamok))
                print(f"Növekvő sorrendben rendezett lista: {vegleges_lista}")
            else:
                print("Nem értelmezhető, próbáld újra!")
            break
        elif uj_elem == "n":
            print("Megszakítás...")
            break
        else:
            print("Nem értelmezhető, próbáld újra!")  

def uj_elem_csak_num():    
    num = []
    words = []

    for line in lines:
        parts = line.strip().split(";")
        
        if not any(char.isdigit() for char in parts):
            words.extend(parts)
        else:
            num.extend(parts)


    while True:
        uj_elem = input("\nSzeretnél új elemet hozzáadni a rendezett listához? (i/n)\n             Írd ide: ")
        if uj_elem == "i":
            novcsok = input("Növekvő vagy csökkenő sorrendben szeretnéd? (n/c)\n             Írd ide: ")
            szam_v_szo = input("Add meg az új elemet (szám vagy szöveg): ")
            
            if not any(char.isdigit() for char in szam_v_szo):
                words.append(szam_v_szo)
            else:
                num.append(szam_v_szo)

            if novcsok == "c":
                num = list(map(int, num))
                rendezett_szamok = merge_rendezes(num, novekvo=False)
                vegleges_lista = words + list(map(str, rendezett_szamok))
                print(f"Csökkenő sorrendben rendezett lista: {vegleges_lista}")
            elif novcsok == "n":
                num = list(map(int, num))
                rendezett_szamok = merge_rendezes(num, novekvo=True)
                vegleges_lista = words + list(map(str, rendezett_szamok))
                print(f"Növekvő sorrendben rendezett lista: {vegleges_lista}")
            else:
                print("Nem értelmezhető, próbáld újra!")
            break
        elif uj_elem == "n":
            print("Megszakítás...")
            break
        else:
            print("Nem értelmezhető, próbáld újra!")  

def uj_elem_csak_words():    
    num = []
    words = []

    for line in lines:
        parts = line.strip().split(";")
        
        if not any(char.isdigit() for char in parts):
            words.extend(parts)
        else:
            num.extend(parts)


    while True:
        uj_elem = input("\nSzeretnél új elemet hozzáadni a rendezett listához? (i/n)\n             Írd ide: ")
        if uj_elem == "i":
            novcsok = input("Növekvő vagy csökkenő sorrendben szeretnéd? (n/c)\n             Írd ide: ")
            szam_v_szo = input("Add meg az új elemet (szám vagy szöveg): ")
            
            if not any(char.isdigit() for char in szam_v_szo):
                words.append(szam_v_szo)
            else:
                num.append(szam_v_szo)

            if novcsok == "c":
                rendezett_szavak = merge_rendezes(words, novekvo=True)
                vegleges_lista = rendezett_szavak + num
                print(f"Csökkenő sorrendben rendezett lista: {vegleges_lista}")
            elif novcsok == "n":
                rendezett_szavak = merge_rendezes(words, novekvo=False)
                vegleges_lista = rendezett_szavak + num
                print(f"Növekvő sorrendben rendezett lista: {vegleges_lista}")
            else:
                print("Nem értelmezhető, próbáld újra!")
            break
        elif uj_elem == "n":
            print("Megszakítás...")
            break
        else:
            print("Nem értelmezhető, próbáld újra!")  

main()          

