from sorting import mergesort


def test_sort_empty_list():
    result = mergesort([])
    assert result == []


def test_sort_list_in_random_order(random_unsorted):
    result = mergesort(random_unsorted)
    assert result == sorted(random_unsorted)


def test_sort_list_of_repeated_number(repeated_number):
    result = mergesort(repeated_number)
    assert result == sorted(repeated_number)


def test_sort_list_in_descending_order(descending_unordered):
    result = mergesort(descending_unordered)
    assert result == sorted(descending_unordered)
