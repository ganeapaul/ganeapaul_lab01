
def citire_fisier():
    nume_fisier = input("Introdu numele fisierului: ")

    try:
        with open(nume_fisier, "r", encoding="utf-8") as f:
            continut = f.read()

        sir = list(map(float, continut.split()))

        print("Numerele citite din fisier:")
        print(sir)

    except FileNotFoundError:
        print("Eroare: Fisierul nu exista!")

    except ValueError:
        print("Eroare: Fisierul contine valori invalide.")