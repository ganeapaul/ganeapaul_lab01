
def citire_tastatura():
    # Citirea unui sir de numere
    sir = list(map(float, input(
        "Introdu numerele separate prin spatii: "
    ).split()))

    print("Sirul introdus:", sir)

    linii = int(input("Numarul de linii: "))
    coloane = int(input("Numarul de coloane: "))

    matrice = []

    for i in range(linii):
        while True:
            try:
                rand = list(map(float, input(
                    f"Introdu {coloane} numere pentru linia {i + 1}: "
                ).split()))

                if len(rand) == coloane:
                    break

                print(f"Introdu exact {coloane} numere.")
            except ValueError:
                print("Introdu doar numere valide.")

        matrice.append(rand)

    print("\nMatricea introdusa:")
    for rand in matrice:
        print(" ".join(f"{numar:g}" for numar in rand))


if __name__ == "__main__":
    citire_tastatura()
