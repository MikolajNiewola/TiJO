from src.math_lib import max
from src.math_lib import is_perfect


def max_test_1():
    # Arrange
    numbers = None

    # Act
    result = max(numbers)

    # Assert
    assert result is None, "max(numbers) should return None"


def max_test_2():
    # Arrange
    numbers = []

    # Act
    result = max(numbers)

    # Assert
    assert result is None, "max(numbers) should return None"


def max_test_3():
    # Arrange
    numbers = [7]

    # Act
    result = max(numbers)

    # Assert
    assert result == 7, "max(numbers) should return 7"


def max_test_4():
    # Arrange
    numbers = [6, 7, 1, 2, 3, 8, 9, 4, 5]

    # Act
    result = max(numbers)

    # Assert
    assert result == 9, "max(numbers) should return 9"


def ip_test_1():
    # Arrange
    num = 6

    # Act
    result = is_perfect(num)

    # Assert
    assert result == True, "is_perfect(6) should return True"


def ip_test_2():
    # Arrange
    num = 2

    # Act
    result = is_perfect(num)

    # Assert
    assert result == False, "is_perfect(2) should return False"


def ip_test_3():
    # Arrange
    num = None

    # Act
    result = is_perfect(num)

    # Assert
    assert result is None, "is_perfect(None) should return None"


if __name__ == "__main__":
    max_test_1()
    max_test_2()
    max_test_3()
    max_test_4()
    ip_test_1()
    ip_test_2()
    ip_test_3()

