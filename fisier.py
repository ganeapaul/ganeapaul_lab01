from pathlib import Path

def citire_fisier():
    nume_fisier = input("Introdu numele fisierului: ").strip()

    cale_fisier = Path(__file__).resolve().parent / nume_fisier

    try:
        with open(cale_fisier, "r", encoding="utf-8") as f:
            continut = f.read()

        sir = list(map(float, continut.split()))

        print("Numerele citite din fisier:")
        print(sir)

    except FileNotFoundError:
        print("Eroare: Fisierul nu exista!")

    except ValueError:
        print("Eroare: Fisierul contine valori invalide.")