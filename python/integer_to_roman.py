def intToRoman(num: int) -> str:
    # breakdown the integer into units divisible by
    # 1s, 10s, 100s, 1000s

    # divide each group by its corresponding mag

    L = {
        "1":['I','V'],"10":['X','L'],
        "100":['C','D'], "1000":['M','']
    }

    def get_roms(mag,val):
        if mag < 1000:
            magAbove = str(mag*10)
        else:
            magAbove = "100"
        mag = str(mag)
        ones = [
            '', L[mag][0]*1,
            L[mag][0]*2,
            L[mag][0]*3,
            L[mag][0]+L[mag][1],
            L[mag][1],
            L[mag][1] + L[mag][0],
            L[mag][1] + L[mag][0]*2,
            L[mag][1] + L[mag][0]*3,
            L[mag][0] + L[magAbove][0]
        ]
        return ones[val]
    out = ""
    rem = num
    for i in [1000,100,10,1]:
        rem = num % i
        out += get_roms(i,num//i)

        num = rem

    return out
