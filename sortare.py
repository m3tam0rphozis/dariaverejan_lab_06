def insertion_sort(v):
    for i in range(1, len(v)):
        aux = v[i]
        j = i - 1
        while j >= 0 and v[j] > aux:
            v[j + 1] = v[j]
            j = j - 1
        v[j + 1] = aux
    return v


def merge_sort(v):
    if len(v) <= 1:
        return v

    mij = len(v) // 2
    st = merge_sort(v[:mij])
    dr = merge_sort(v[mij:])

    rez = []
    i = 0
    j = 0
    while i < len(st) and j < len(dr):
        if st[i] < dr[j]:
            rez.append(st[i])
            i = i + 1
        else:
            rez.append(dr[j])
            j = j + 1

    while i < len(st):
        rez.append(st[i])
        i = i + 1

    while j < len(dr):
        rez.append(dr[j])
        j = j + 1

    return rez


try:
    f = open("date.txt", "r")
    linii = f.readlines()
    f.close()

    if len(linii) < 2:
        print("Fisierul nu are destule linii.")
    else:
        linie1 = linii[0].strip()
        alg = linii[1].strip()

        if linie1 == "":
            print("Nu exista numere pe prima linie.")
        else:
            parti = linie1.split()
            numere = []
            date_ok = True

            for x in parti:
                try:
                    numere.append(int(x))
                except ValueError:
                    date_ok = False
                    break

            if not date_ok:
                print("Date invalide! Prima linie trebuie sa contina doar numere intregi.")
            elif alg != "Insertion" and alg != "Merge":
                print("Algoritm invalid! Alege Insertion sau Merge.")
            else:
                if alg == "Insertion":
                    rezultat = insertion_sort(numere)
                else:
                    rezultat = merge_sort(numere)

                sir_rezultat = ""
                for nr in rezultat:
                    sir_rezultat = sir_rezultat + str(nr) + " "
                sir_rezultat = sir_rezultat.strip()

                f = open("date.txt", "a")
                if not linii[-1].endswith("\n"):
                    f.write("\n")
                f.write(alg + ": " + sir_rezultat + "\n")
                f.close()

                print("Rezultatul a fost scris in date.txt:", alg + ": " + sir_rezultat)

except FileNotFoundError:
    print("Nu s-a gasit fisierul date.txt.")