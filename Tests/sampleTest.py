import pytest


def print_test():
    print('test complete!!!!')


def add_test():
    a = 5
    b = 1+a
    assert a+1 == b


def print_test_2():
    print('test 2 complete!!!!!!')


if __name__ == '__main__':
    pytest.main(['-s', __file__])
