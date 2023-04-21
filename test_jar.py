from jar import Jar
def test_init():
    try:
        Jar(-5)
        assert False, "Expected ValueError"
    except ValueError:
        pass
    try:
        Jar(3.5)
        assert False, "Expected ValueError"
    except ValueError:
        pass
    assert Jar().capacity == 12
    assert Jar(10).capacity == 10

def test_str():
    assert str(Jar(3)) == "🍪🍪🍪"
    assert str(Jar()) == ""

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    try:
        jar.deposit(-2)
        assert False, "Expected ValueError"
    except ValueError:
        pass
    try:
        jar.deposit(5)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_withdraw():
    jar = Jar(8)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    try:
        jar.withdraw(-1)
        assert False, "Expected ValueError"
    except ValueError:
        pass
    try:
        jar.withdraw(4)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_capacity():
    jar = Jar(7)
    assert jar.capacity == 7

def test_size():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

