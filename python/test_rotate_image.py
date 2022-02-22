from python.rotate_image import rotate


def test_rotate():
    IN_OUT = [
        ([[1,2,3],[4,5,6],[7,8,9]],
         [[7,4,1],[8,5,2],[9,6,3]])
    ]
    for i, o in IN_OUT:
        func_out = rotate(i)
        assert o == func_out
