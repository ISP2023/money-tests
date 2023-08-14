"""Test of Banknote."""
import sys
sys.path.append("..")
from money import Banknote, Money

def test_banknote_is_money():
    """Banknote is a subclass of money has has money properties."""
    banknote = Banknote(200, "Eth")
    # another banknote to verify the attributes are not static
    banknote2 = Banknote(10, "USD")
    assert isinstance(banknote, Money)
    assert banknote.value == 200
    assert banknote._currency == "Eth"
    assert banknote2.value == 10
    assert banknote2._currency == "USD"

def test_serial_number():
    """Each banknote has a unique serial number, at least 1,000,000,000."""
    MIN_SERIAL_NUMBER = 1000000000
    note1 = Banknote(100, "USD")
    note2 = Banknote(50, "USD")
    note3 = Banknote(100, "Baht")
    assert note1._serial_number >= MIN_SERIAL_NUMBER
    assert note2._serial_number >= MIN_SERIAL_NUMBER
    assert note3._serial_number >= MIN_SERIAL_NUMBER
    assert note1._serial_number != note2._serial_number
    assert note1._serial_number != note3._serial_number
    assert note2._serial_number != note3._serial_number
