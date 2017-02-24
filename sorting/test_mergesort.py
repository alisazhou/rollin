from sorting import mergesort


def test_sort_empty_list():
    result = mergesort([])
    assert result == []


def test_sort_list_in_random_order(random_unsorted, random_sorted):
    result = mergesort(random_unsorted)
    assert result == random_sorted


def test_sort_list_of_repeated_number(repeated_number):
    result = mergesort(repeated_number)
    assert result == repeated_number


def test_sort_list_in_descending_order(descending_unordered, descending_ordered):
    result = mergesort(descending_unordered)
    assert result == descending_ordered
