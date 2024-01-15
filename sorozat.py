import random

print("\t\n II/A, B, C: ")
global szam_lista 
szam_lista = []
index = 0

while index < 8:
    vszam = random.randint(-100,859)
    szam_lista.append(vszam)
    index += 1


index = 0
while index < len(szam_lista):
    if index < 8:
        print(f"\t {szam_lista[index]}", end=", ")
    else:
        print(f"{szam_lista[index]}", end=" ")
    
    index += 1




def tizzel_oszthatoak_szama():
    szamlalo = 0
    for i in szam_lista:
        if i % 10 == 0:
            szamlalo += 1
    return szamlalo


def konzol_kiir():
    eredmeny = tizzel_oszthatoak_szama()
    print(f"10-zel oszthatóak száma {eredmeny}.")

def fajlba_ir():
    szam=tizzel_oszthatoak_szama()
    f = open('vegeredmeny.txt', 'w')
    f.write(f"\t A tizzel osztahtoak szama {szam}.")
    f.close()





