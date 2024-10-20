import random
import string



def elso():
    print("1. opció:")
    minimum1 = int(input("\nAdd meg a szám minimum határát: "))
    maximum1 = int(input("Add meg a szám maximum határát: "))
    darabszam1 = int(input("Add meg hány számot generáljon a gép! "))

    veletlen_szam = [random.randint(minimum1, maximum1) for i in range(darabszam1)]

    print("\nGenerált véletlen számok:", veletlen_szam)
    
    with open("ki.txt", "a", encoding="utf-8") as f:
        f.write(";".join(map(str, veletlen_szam)) + "\n")

   

def masodik():
    print("2. opció:")
    
    darabszam2 = int(input("\nAdd meg számmal, hogy hány darab szöveget generáljon a gép!: "))
    
    veletlen_szoveg = []
    for i in range(darabszam2):
        hosszusag = random.randint(1, 20)
        szoveg = ''.join(random.choices(string.ascii_letters, k=hosszusag)) 
        veletlen_szoveg.append(szoveg)
    
    print(f"\nA véletlen szövegek: {veletlen_szoveg}")

    with open("ki.txt", "a", encoding="utf-8") as f:
        f.write(";".join(map(str, veletlen_szoveg)) + "\n")
       
def harmadik():
    print("3. opció: (Ez a program soronként ellenőrzi a txt tartalmát!)")
    
    minimum2 = int(input("\nAdd meg a szám minimum határát: "))
    maximum2 = int(input("Add meg a szám maximum határát:  "))
    darabszam3 = int(input("Add meg hány számot kell ellenőrizni!: "))

    with open("ki.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    eredmenyek = []

    counter = 0

    for line in lines:
        try:
            szamok = list(map(int, line.split(";")))
            for szam in szamok:
                if szam == " ":
                    counter += 1
        except ValueError:
            eredmenyek.append(f"A {counter + 1}. sor nem tartalmaz számokat.")
            counter += 1
            continue 

        hibas_szamok = [szam for szam in szamok if szam < minimum2 or szam > maximum2]
        if hibas_szamok:
            eredmenyek.append(f"A {counter + 1}. sorban az alábbi számok nem felelnek meg a megadott határoknak: {hibas_szamok}")
            counter += 1
        else:
            eredmenyek.append(f"Minden szám megfelel az összes megadott határnak a {counter + 1}. sorban!")
            counter += 1

    for eredmeny in eredmenyek:
        print(eredmeny)


def negyedik():
    print("4. opció: (Ez a program soronként ellenőrzi a txt tartalmát!).")

    darabszam4 = int(input("Add meg hány elemnek kell lennie egy sorban!: "))

    with open("ki.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for sor_szam, line in enumerate(lines, 1):
        betuk = list(map(str, line.split(";")))
        nem_szamos_elemek = 0

        for betu in betuk:
            if not any(char.isdigit() for char in betu):
                nem_szamos_elemek += 1

        print(f"{sor_szam}. sor: {nem_szamos_elemek} darab elem tartalmaz szót:")

        if nem_szamos_elemek == 0:
            print("    - A sorban nincsenek szavak!")
            continue
        elif len(betuk) != darabszam4:
            print(f"    - Nem felel meg a feltételeknek, mert {len(betuk)} elem van, de {darabszam4} kellett volna!")
        else:
            print("    - A sor elemeinek száma helyes!")



def main():
    while True:
        valasztas = input("""\nÍrj be 0-4 között egy számot, ha: 
        - 0-át írsz: megszakítod a programot!
        - 1-et írsz: számokat tudsz lekérni!
        - 2-őt írsz: szavakat tudsz lekérni!
        - 3-at írsz: a számokat ellenőrzöd!
        - 4-et írsz: a szavakat ellenőrzöd! \n              Írd ide: """)

        if valasztas == '1':
            elso()
        elif valasztas == '2':
            masodik()
        elif valasztas == '3':
            harmadik()
        elif valasztas == '4':
            negyedik()
        elif valasztas == '0':
            print("Megszakítás...")
            break
        else:
            print("Érvénytelen választási opció, próbáld újra!")

main()
