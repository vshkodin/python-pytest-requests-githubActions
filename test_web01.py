import requests


def test_web():
    r = requests.get('https://vshkodin.com/')
    assert 200 == r.status_code
