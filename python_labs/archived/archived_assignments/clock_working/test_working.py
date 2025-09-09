import pytest
from working import convert

def test_standard_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"

def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_mixed_formats():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

def test_noon_and_midnight():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_edge_case_hours():
    assert convert("1:00 AM to 11:00 PM") == "01:00 to 23:00"
    assert convert("12:30 AM to 11:59 PM") == "00:30 to 23:59"

def test_invalid_time_format():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")  # Invalid minutes

def test_invalid_hour_values():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")  # Hour > 12 with AM/PM

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # Using hyphen instead of "to"
    
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")  # Missing AM/PM
    
    with pytest.raises(ValueError):
        convert("9:00 am to 5:00 pm")  # Lowercase am/pm

def test_garbage_input():
    with pytest.raises(ValueError):
        convert("cat")
    
    with pytest.raises(ValueError):
        convert("")