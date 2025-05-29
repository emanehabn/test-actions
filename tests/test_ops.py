from src.math_ops import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(-2, -3) == -5
    assert add(-2, 3) == 1
    assert add(2, -3) == -1


def test_sub():
    assert sub(1, 1) == 0
    assert sub(-1, 1) == -2
    assert sub(1, -1) == 2
    assert sub(-1, -1) == 0