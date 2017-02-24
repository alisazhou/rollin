import pytest


@pytest.fixture
def random_unsorted():
    return [4, 5, 3, 8, 12, -3]

@pytest.fixture
def random_sorted():
    return [-3, 3, 4, 5, 8, 12]


@pytest.fixture
def repeated_number():
    return [1, 1, 1, 1, 1]


@pytest.fixture
def descending_unordered():
    return [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

@pytest.fixture
def descending_ordered():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
