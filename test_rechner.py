import pytest
from rechner import addiere, subtrahiere, multipliziere, dividiere


def test_addiere():
    assert addiere(2, 3) == 5
    assert addiere(0, 0) == 0
    assert addiere(-1, 1) == 0


def test_subtrahiere():
    assert subtrahiere(5, 2) == 3
    assert subtrahiere(10, 10) == 0
    assert subtrahiere(0, 5) == -5


def test_multipliziere():
    assert multipliziere(4, 3) == 12
    assert multipliziere(0, 100) == 0
    assert multipliziere(-2, 3) == -6


def test_dividiere():
    assert dividiere(10, 2) == 5
    assert dividiere(9, 3) == 3
    assert dividiere(7, 2) == 3.5


def test_dividiere_durch_null():
    with pytest.raises(ValueError):
        dividiere(10, 0)