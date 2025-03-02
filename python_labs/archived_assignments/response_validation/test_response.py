import pytest
from response import validate

# Tests for valid email formats
def test_valid_emails():
    assert validate("simple@example.com") == "Valid"
    assert validate("very.common@example.com") == "Valid"
    assert validate("disposable.style.email.with+symbol@example.com") == "Valid"
    assert validate("other.email-with-hyphen@example.com") == "Valid"
    assert validate("fully-qualified-domain@example.com") == "Valid"
    assert validate("user.name+tag+sorting@example.com") == "Valid"
    assert validate("x@example.com") == "Valid"
    assert validate("example-indeed@strange-example.com") == "Valid"
    assert validate("example@s.example") == "Valid"

# Tests for invalid email formats
def test_invalid_emails():
    assert validate("Abc.example.com") == "Invalid"
    assert validate("A@b@c@example.com") == "Invalid"
    assert validate('a"b(c)d,e:f;g<h>i[j\\k]l@example.com') == "Invalid"
    assert validate('i_like_underscore@but_its_not_allowed_in_this_part.example.com') == "Invalid"
    assert validate('@example.com') == "Invalid"
    assert validate('user@') == "Invalid"
    assert validate("cat") == "Invalid"