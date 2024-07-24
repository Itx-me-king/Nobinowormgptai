# test_example.py

import pytest
from bot.py import process_data , handle_message # Import your functions here

def test_Process_data():
    # Arrange
    input_data = "Processed input"
    expected_output = "processed output"
    
    # Act
    result = Process_data(input_data)
    
    # Assert
    assert result == expected_output

def test_handle_function():
    # Arrange
    another_input = "message input"
    another_expected_output = "message output"
    
    # Act
    another_result = handle_message(another_input)
    
    # Assert
    assert another_result == Another_expected_output
