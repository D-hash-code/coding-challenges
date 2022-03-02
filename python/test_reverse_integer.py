from python.reverse_integer import reverse


def test_reverse():
    IN_OUT = [(0, 0), (234, 432), (-232456, -654232)]
    for i, o in IN_OUT:
        func_out = reverse(i)
        assert o == func_out
