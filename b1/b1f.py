def berechne_fakultaet(n):
    """
    Berechnet die Fakultät einer Zahl.

    Parameters:
    n (int): Die Zahl, deren Fakultät berechnet werden soll.

    Returns:
    int: Die Fakultät von n.
    """
    def fakultaet_recursion(k):
        if k == 0 or k == 1:
            return 1
        else:
            return k * fakultaet_recursion(k - 1)

    return fakultaet_recursion(n)

def main():
    zahl = 5
    ergebnis = berechne_fakultaet(zahl)
    print(f'Die Fakultät von {zahl} ist {ergebnis}')

if __name__ == "__main__":
    main()
