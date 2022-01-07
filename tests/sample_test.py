import pytest
import requests
import json


def test_print():
    print('test complete!!!!')


@pytest.mark.onlyRun
def test_add():
    a = 5
    b = 1+a
    assert a+1 == b


@pytest.mark.onlyRun
def test_print_2():
    print('test 2 complete!!!!!!')


def test_docker_server():
    url = 'https://www.google.com/'
    Headers = {'content-type': 'application/json'}
    response = requests.get(url=url, headers=Headers, verify={})
    print(response.json())


if __name__ == '__main__':
    pytest.main(['-s', __file__])
