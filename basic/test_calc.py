from calc import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    assert square(1.5) == 2.25

def test_positive():
    assert square(5) == 25

def test_negative():
    assert square(-4) == 16

def test_zero():
    assert square(0) == 0   

if __name__ == "__main__":
    main()