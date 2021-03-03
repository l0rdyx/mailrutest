import pytest


def test_tuple1():
    assert (1, 0) == (1, 0)


def test_tuple2():
    try:
        assert (1, 0)[2]
    except IndexError:
        pass


def test_tuple3():
    assert tuple([1, 0, 3]) == (1, 0, 3)


def test_float1():
    assert 1 - 0.01 == 0.99

def test_float2():
    assert 0.01**2 == 0.01 * 0.01


testdata = [5, 20, 50000, -5, -20, -5000]

@pytest.mark.parametrize("n", testdata)
def test_float3(n):
    try:
        assert 5.5** (n)
    except (OverflowError, AssertionError) as e:
        pass