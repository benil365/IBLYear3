from um import count
def test_count_no_um():
    assert count("hello world") == 0
    assert count("this sentence has no ums") == 0


def test_count_one_um():
    assert count("um") == 1
    assert count("the ums are here") == 1


def test_count_multiple_ums():
    assert count("um um um") == 3
    assert count("UM um um UM UM") == 4
