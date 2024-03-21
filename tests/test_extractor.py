import pytest

from ojd_daps_company_descriptions import extract_company_descriptions

example_text_1 = "Would you like to join a major manufacturing company?"
example_text_2 = "This is just a random sentence"

def test_extract_company_descriptions():
    result_1 = extract_company_descriptions(example_text_1)
    result_2 = extract_company_descriptions(example_text_2)
    assert result_1[0]["score"] > 0.5
    assert result_2[0]["score"] < 0.5