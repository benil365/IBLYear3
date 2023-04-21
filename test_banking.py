
from bank import value


def test_value_hello():
    assert value('Hello, world!') == 0
    assert value('HELLO, WORLD!') == 0
    assert value('hello there') == 0
    assert value('heLLo') != 0


def test_value_h():
    assert value('Hi there') == 20
    assert value('hi, how are you?') == 20
    assert value('hola') == 20
    assert value('Ha!') != 20


def test_value_other():
    assert value('Good morning') == 100
    assert value('good night') == 100
    assert value('Guten Tag') == 100
    assert value('') == 100
