import pytest
import requests
import json


def test_print():
    print('test complete!!!!')


def test_add():
    a = 5
    b = 1+a
    assert a+1 == b

def test_print_2():
    print('test 2 complete!!!!!!')


def test_requests_module():
    url = 'https://www.google.com/'
    Headers = {'content-type': 'application/json'}
    response = requests.get(url=url, headers=Headers, verify={})
    print(response)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
