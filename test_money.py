"""
Tests of the Money class using pytest.
These tests only test the student's code, not methods given
in the starter code.

Some tests are marked with @pytest.mark.skip since they test
methods that aren't in Money yet. When you write __add__ and
__gt__ in money, comment out the @pytest.mark.skip annotations.
"""
import pytest
import sys
sys.path.append("..")
from money import Money


def test_init():
    """Test the constructor."""
    print("TEST: init")
    m = Money(10.5)  # use default currency
    assert m.value == 10.5
    assert m.currency == "Baht"
    # Money can have 0 value.  Useful for accounting or sales application.
    m = Money(0, "USD")
    assert m.value == 0
    assert m.currency == "USD"


def test_eq():
    """Money objects are equal if and only if the value and currency are same."""
    m1 = Money(3, "Baht")
    m2 = Money(3, "Baht")
    assert m1 == m2
    # value is not the same
    m2 = Money(3.001, "Baht")
    assert not m1 == m2
    # currency is spelled differently (not same)
    m2 = Money(3, "Bath")
    assert not m1 == m2
    # Currency should be case-insensitive.
    m3 = Money(3, "BAHT")
    assert m1 == m3, "equal should treat uppercase/lowercase letters as same"
    # eq should not change the arguments
    assert m1.value == 3 and m1.currency == "Baht", "should not modify args"
    assert m2.value == 3 and m2.currency == "Bath", "should not modify args"
    # trivial case
    assert m1 == m1


def test_eq_other_type():
    """Cannot compare Money and non-Money."""
    m1 = Money(10, "Baht")
    assert not m1 == "10 Baht"
    assert not m1 == 10


#@pytest.mark.skip("skip this test until you write __add__")
def test_add():
    """Add money objects with the same currency."""
    m1 = Money(3, "Baht")
    m2 = Money(8, "Baht")
    m  = m1 + m2
    assert m.value == 11
    assert m.currency == "Baht"
    assert m1.value == 3, "Add should not modify the arguments"
    assert m2.value == 8, "Add should not modify the arguments"
    """It is OK to add zero-valued money."""
    m0 = Money(0, "Baht")
    m = m0 + m2
    assert m.value == m2.value
    assert m.currency == "Baht"  


#@pytest.mark.skip("skip this test until your write __add__")
def test_add_different_currency_or_type():
    """Add money with different currency should raise a ValueError."""
    m1 = Money(3, "Baht")
    m2 = Money(5, "Bird")
    # Adding different currencies should raise ValueError
    with pytest.raises(ValueError):
        m = m1 + m2
    # Cannot add Money and non-Money. Should raise TypeError.
    with pytest.raises(TypeError):
        m = m1 + 5

# Rename these as non-tests since they were given in starter code

def dont_test_properties():
    """Money should have r/o properties for currency and value."""
    m = Money(5.0, "RMB")
    # another instance, to verify the attributes are not shared
    m2 = Money(99.99, "Ruple")
    assert m.value == 5.0
    assert m.currency == "RMB"
    assert m2.value == 99.99
    assert m2.currency == 'Ruple'
    # Properties are read-only. Assignment should raise AttributeError.
    with pytest.raises(AttributeError):
        m.value = 10.0
    with pytest.raises(AttributeError):
        m.currency = "Ringgit"


def dont_test_str():
    """String form should show value of money as an int if there is
    no fractional value, or print with 2 decimal digits otherwise.
    """
    m = Money(12.0, "BTC")
    assert str(m) == "12 BTC"
    m = Money(0.12345, "Dogecoin")
    assert str(m) == "0.12 Dogecoin"
