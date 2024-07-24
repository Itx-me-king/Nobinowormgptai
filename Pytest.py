# pytest 

import pytest
from your_module import your_function

def test_example_function():
    # Arrange
    input_data = "some input"
    expected_output = "expected output"
    
    # Act
    result = your_function(input_data)
    
    # Assert
    assert result == expected_output

def test_another_function():
    #
