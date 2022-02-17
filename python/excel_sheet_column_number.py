
def titleToNumber(columnTitle: str) -> int:
    output = 0

    for n, c in enumerate(columnTitle[::-1]):
        output += (ord(c) - 64) * (26 ** n)

    return output