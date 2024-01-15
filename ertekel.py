print("\t\n I/A,B: ")

het_napja = input("\t Hét napjai: ")
ora_neve = input("\t Óra neve: ")
ertekeles = int(input("Kérem, adja meg az értékelést [0,5] intervallumban: "))


if ertekeles < 0:
    print("Az értékelés nem lehet negatív")
elif ertekeles > 5:
    print("5 pont feletti értékelés nem elfogadható")
else:
    print("Köszönjük az értékelést!")

