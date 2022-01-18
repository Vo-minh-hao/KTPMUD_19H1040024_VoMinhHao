import pytest
def check_bcd_number(value):
    if value == "0000" or value == "00000000":
        return True

    if len(value) % 4 == 0:
        try:
            return bool(int(value, 2))
        except ValueError:
            return False
    else:
        return False

@pytest.mark.parametrize("value, result", [("0001", True), ("1234", False), ("12", False)])
def test_check_bcd_number(value, result):
    assert result == check_bcd_number(value)

