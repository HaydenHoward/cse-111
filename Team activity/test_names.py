from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('larry', 'wheels') == 'wheels; larry'
    assert make_full_name('Hayden','Howard') == 'Howard; Hayden'
    assert make_full_name('Clay', 'Wood-gate') == "Wood-gate; Clay"

def test_extract_family_name():
    assert extract_family_name("Howard; Hayden") == "Howard"
    assert extract_family_name("wheels; larry") == "wheels"
    assert extract_family_name("Wood-gate; Clay") == "Wood-gate"

def test_extract_given_name():
    assert extract_given_name('wheels; larry') == 'larry'
    assert extract_given_name('Howard; Hayden') == "Hayden"
    assert extract_given_name("Wood-gate; Clay-ton") == "Clay-ton"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])