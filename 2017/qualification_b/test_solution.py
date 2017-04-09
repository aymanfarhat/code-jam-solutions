from solution import is_tidy
from solution import last_tidy


def test_is_tidy():
    assert is_tidy(0)
    assert is_tidy(1)
    assert is_tidy(8)
    assert is_tidy(88)
    assert is_tidy(33)
    assert is_tidy(334)
    assert is_tidy(224488)
    assert not is_tidy(534)
    assert not is_tidy(999990)
    assert not is_tidy(495)
    assert not is_tidy(111111111111111109)


def test_last_tidy():
    assert last_tidy(132) == 129
    assert last_tidy(1000) == 999
    assert last_tidy(7) == 7
    #assert last_tidy(111111111111111110) == 99999999999999999
