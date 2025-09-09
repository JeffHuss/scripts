from twttr import shorten
import pytest

def test_default():
    assert shorten() == "smthng"

def test_phrases():
    assert shorten("Jeff") == "Jff"
    assert shorten("apple") == "ppl"
    assert shorten("peanut butter") == "pnt bttr"
    assert shorten("twitter") == "twttr"
    assert shorten("cat") == "ct"
    assert shorten("12345") == "12345"

if __name__ == "__main__":
    main()