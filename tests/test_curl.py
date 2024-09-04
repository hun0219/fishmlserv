from fishmlserv.curl import get

def test_get():
    r = get(10,10)
    print(r)
    assert r == "빙어"

