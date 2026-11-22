def insertion_sort(lista):
    arr = lista[:]
    for i in range(1, len(arr)):
        cheie = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cheie:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cheie
    return arr


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mijloc = len(lista) // 2
    stanga = merge_sort(lista[:mijloc])
    dreapta = merge_sort(lista[mijloc:])

    rezultat = []
    i = j = 0
    while i < len(stanga) and j < len(dreapta):
        if stanga[i] <= dreapta[j]:
            rezultat.append(stanga[i])
            i += 1
        else:
            rezultat.append(dreapta[j])
            j += 1

    rezultat.extend(stanga[i:])
    rezultat.extend(dreapta[j:])
    return rezultat


def main():
    try:
        with open("date.txt", "r", encoding="utf-8") as f:
            continut = f.read()
            linii = [linie.strip() for linie in continut.splitlines() if linie.strip()]

        if len(linii) < 2:
            print("Eroare: Fisierul date.txt trebuie sa contina cel putin 2 linii (numerele si algoritmul).")
            return

        elemente_text = linii[0].split()
        if not elemente_text:
            print("Eroare: Prima linie nu contine numere.")
            return

        numere = []
        for elem in elemente_text:
            try:
                numere.append(int(elem))
            except ValueError:
                print(f"Eroare: '{elem}' nu este un numar intreg valid.")
                return

        algoritm = linii[1].strip()
        if algoritm == "Insertion":
            sortate = insertion_sort(numere)
        elif algoritm == "Merge":
            sortate = merge_sort(numere)
        else:
            print(f"Eroare: Algoritmul '{algoritm}' nu este suportat. Alege 'Insertion' sau 'Merge'.")
            return

        text_sortat = " ".join(str(x) for x in sortate)
        linie_rezultat = f"{algoritm}: {text_sortat}"

        with open("date.txt", "a", encoding="utf-8") as f:
            if not continut.endswith("\n"):
                f.write("\n")
            f.write(linie_rezultat + "\n")

        print(f"Succes! Rezultatul a fost adaugat in date.txt -> {linie_rezultat}")

    except FileNotFoundError:
        print("Eroare: Fisierul 'date.txt' nu a fost gasit.")


if __name__ == "__main__":
    main()