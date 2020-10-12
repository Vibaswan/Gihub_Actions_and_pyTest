import pytest


def test_print():
    print('test complete!!!!')


def test_add():
    a = 5
    b = 1+a
    assert a+1 == b


def test_print_2():
    print('test 2 complete!!!!!!')


if __name__ == '__main__':
    pytest.main(['-s', __file__])
