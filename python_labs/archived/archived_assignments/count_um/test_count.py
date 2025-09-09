import pytest
from count import count

# Test straightforward cases
def test_simple():
    assert count("I um have some kind of um, issue with saying um too many times.") == 3
    assert count("Um um um um") == 4
    assert count("Ummmmm umm um um umm") == 5

# Test strings that contain words wherein "um" is a sub-string but shouldn't be counted
def test_words_containing_pattern():
    assert count("Umbrellas are, um, not related to um...umbillical cords at all.") == 2
    assert count("Summary") == 0
    assert count("Um, I'm trying to summarize the album, but ummm, I keep getting distracted by the drummer's rhythm and the humming.") == 2
    assert count("The aluminum umbrella was damaged, but ummmm, I think it's still usable for humid summer days.") == 1
    assert count("Ummm, I'm not sure how to circumvent this problem without a triumphant comeback or um... maybe some humble assumptions.") == 2
    assert count("The curriculum seems challenging, but um... the numbers in the plumbing column don't add up to the maximum allowed.") == 1

# Validate that empty input works as expected
def test_empty_input():
    assert count("") == 0
