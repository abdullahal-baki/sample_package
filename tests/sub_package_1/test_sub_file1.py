from sample_package.sub_package_1.sub_file1 import sample_function2


def test_sample_function2():
    """
    Test the sample_function2 function.
    """
    result = sample_function2('arif', 34)
    assert result == 'Hello arif, your age 34'
    