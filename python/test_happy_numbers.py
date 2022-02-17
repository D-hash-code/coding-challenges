from python.happy_numbers import isHappy


def test_ishappy():
    IN_OUT = [(1, True), (19, True), (2, False)]
    for i, o in IN_OUT:
        func_out = isHappy(i)
        assert o == func_out
