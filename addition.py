# app.py
# this is my first github action
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
