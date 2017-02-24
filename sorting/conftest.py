import pytest


@pytest.fixture
def random_unsorted():
    return [4, 5, 3, 8, 12, -3]

@pytest.fixture
def random_sorted():
    return [-3, 3, 4, 5, 8, 12]
