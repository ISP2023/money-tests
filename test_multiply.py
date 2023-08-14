"""
Extra credit for writing multiply in Money to do Money * float
or float * Money.
"""
import pytest
import sys
sys.path.append("..")
from money import Money


def test_left_multiply():
    """Multiply money x float multiplies value."""
    m = Money(10.5, "USD")
    m1 = m * 2
    assert m1.value == 21
    assert m1.currency == "USD"
    # Does not change original money object
    assert m.value == 10.5
    assert m.currency == "USD"
    # Fractional multiply. Be careful of round-off errors.
    m = Money(20, "Baht")
    m2 = m * 0.25
    assert m2.value == 5
    assert m2.currency == "Baht"
    zero = m * 0.0
    assert zero.value == 0

def test_right_multiply():
    """Performing float x money invokes Money.__rmul__."""
    m = Money(10.5, "USD")
    m1 = 2 * m
    assert m1.value == 21
    assert m1.currency == "USD"
    # Does not change original money object
    assert m.value == 10.5
    assert m.currency == "USD"
    # Fractional multiply. Be careful of round-off errors.
    m = Money(40, "Baht")
    m2 = 0.25 * m
    assert m2.value == 10
    assert m2.currency == "Baht"
    zero = 0.0 * m
    assert zero.value == 0

# This test would pass for codes that *do not* implement __mul__,
# so don't test it.
def dont_test_raises_exception():
    """Cannot multiply money x money."""
    m1 = Money(5, "THB")
    m2 = Money(10, "THB")
    with pytest.raises(TypeError):
        product = m1 * m2
