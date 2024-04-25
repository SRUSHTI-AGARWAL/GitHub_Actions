# writing tests here

def add(a, b):
    return a+b


# performs Unit testing 

def test_add():
    assert add(1,2) == 4
    assert add(1,-1) == 0


