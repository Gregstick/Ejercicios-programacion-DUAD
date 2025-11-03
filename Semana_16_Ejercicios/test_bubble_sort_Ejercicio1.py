import pytest
from Unit_testing_Ejercicio1 import bubble_sort

def test_small_list():
    # Arrange
    data = [3, 1, 2]
    expected = [1, 2, 3]

    # Act
    bubble_sort(data)

    # Assert
    assert data == expected

def test_large_list():
    # Arrange
    data = [3, -200, 1000, 50000, 5, 6, -8]
    expected = [-200, -8, 3, 5, 6, 1000, 50000]

    # Act
    bubble_sort(data)

    # Assert
    assert data == expected

def test_empty_list():
    # Arrange
    data = []
    expected = []

    # Act
    bubble_sort(data)

    # Assert
    assert data == expected

def test_invalid_input():
    # Arrange
    invalid_input = (1, 2, "text")

    # Act and Assert
    with pytest.raises(TypeError):
        bubble_sort(invalid_input)