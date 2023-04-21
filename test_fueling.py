from fueling import convert, gauge


def test_convert_integer():
    assert convert('5/8') == 62
    assert convert('3/4') == 75


def test_convert_rounding():
    assert convert('1/2') == 50
    assert convert('1/3') == 33
    assert convert('2/3') == 67


def test_convert_invalid_input():
    try:
        convert('1.5/2')
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"
    try:
        convert('2/1')
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"
    try:
        convert('1/0')
    except ZeroDivisionError:
        pass
    else:
        assert False, "Expected ZeroDivisionError"


def test_gauge_E():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(50) != 'E'


def test_gauge_Z():
    assert gauge(50) == '50%'
    assert gauge(99) != '99%'
    assert gauge(100) == '100%'


def test_gauge_F():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(101) != 'F'
