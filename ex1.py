import pytest
def check_bcd_number(value):
    try:
        int(value, 2)
        return True
    except ValueError:
        return False


print(check_bcd_number("11"))

@pytest.mark.parametrize("value, result", [("0001", True), ("1234", False), ("12", False)])
def test_check_bcd_number(value, result):
    assert result == check_bcd_number(value)

