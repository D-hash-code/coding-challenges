from python.nim_game import canWinNim


def test_canWinNim():
    IN_OUT = [(1, True), (4, False), (2, True)]
    for i, o in IN_OUT:
        func_out = canWinNim(i)
        assert o == func_out
