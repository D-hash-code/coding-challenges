from python.integer_to_roman import intToRoman


def test_intToRoman():
    IN_OUT = [(1, "I"), (19, "XIX"), (1299, "MCCXCIX")]
    for i, o in IN_OUT:
        func_out = intToRoman(i)
        assert o == func_out
