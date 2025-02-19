import pytest
import os

def demo_function():
    """
    This function returns a dictionary.
    Modify it to test with an empty or non-empty dictionary.
    """
    return {"key": "value"}  # Change to {} for an empty dictionary


def test_demo_function():
    """
    Test to check if demo_function returns a non-empty dictionary.
    """
    result = demo_function()
    assert isinstance(result, dict), "Function should return a dictionary"
    assert result, "The dictionary should not be empty"

    # Get API key from environment
    api_key = os.environ["OPENAI_API_KEY"]
    assert api_key, "OPENAI_API_KEY is not set"


if __name__ == "__main__":
    pytest.main()
