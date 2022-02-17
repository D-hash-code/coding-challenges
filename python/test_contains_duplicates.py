from python.contains_duplicates import containsDuplicate


def test_contains_duplicates():
    IN_OUT = [([1, 2, 2, 3], True), ([1, 2, 3, 4, 5], False), ([1], False)]
    for i, o in IN_OUT:
        func_out = containsDuplicate(i)
        assert o == func_out
