from digits import validate

def test_validate_valid():
    assert validate("192.168.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("10.20.30.40") == True

def test_validate_invalid():
    assert validate("192.168.0") == False
    assert validate("192.168.0.275") == False
    assert validate("192.168.0.") == False
    assert validate("192.168..1") == False
    assert validate("192.168.0.-1") == False
    assert validate("192.168.0.256") == False
    assert validate("") == False
