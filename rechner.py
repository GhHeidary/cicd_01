# ============================================
# rechner.py - Einfache Rechen-Funktionen
# ============================================

def addiere(a, b):
    """Addiert zwei Zahlen."""
    return a + b


def subtrahiere(a, b):
    """Subtrahiert b von a."""
    return a - b


def multipliziere(a, b):
    """Multipliziert zwei Zahlen."""
    return a * b


def dividiere(a, b):
    """Dividiert a durch b."""
    if b == 0:
        raise ValueError("Division durch Null nicht erlaubt!")
    return a / b
def potenz(a, b):
    """ Berechnet a hoch b"""
    return a ** b

if __name__ == "__main__":
    print(f"2 + 3 = {addiere(2, 3)}")
    print(f"5 - 2 = {subtrahiere(5, 2)}")
    print(f"4 * 3 = {multipliziere(4, 3)}")
    print(f"10 / 2 = {dividiere(10, 2)}")