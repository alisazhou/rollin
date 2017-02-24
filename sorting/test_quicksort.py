from sorting import quicksort


def test_sort_empty_list():
    result = quicksort([])
    assert result == []


def test_sort_list_in_random_order(random_unsorted):
    result = quicksort(random_unsorted)
    assert result == sorted(random_unsorted)


def test_sort_list_of_repeated_number(repeated_number):
    result = quicksort(repeated_number)
    assert result == sorted(repeated_number)


def test_sort_list_in_descending_order(descending_unordered):
    result = quicksort(descending_unordered)
    assert result == sorted(descending_unordered)
