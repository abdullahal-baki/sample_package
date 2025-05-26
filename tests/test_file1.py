from sample_package.file1 import sample_function


def test_sample_function():
    """Test the sample_function from file1."""
    result = sample_function("John", 30)
    expected = "Hello, John. You are 30 years old."
    assert result == expected, f"Expected '{expected}', but got '{result}'"