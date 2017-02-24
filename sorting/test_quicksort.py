from sorting import quicksort


def test_sort_empty_list():
    result = quicksort([])
    assert result == []


def test_sort_list_in_random_order(random_unsorted, random_sorted):
    result = quicksort(random_unsorted)
    assert result == quicksort(random_sorted)


def test_sort_list_of_repeated_number(repeated_number):
    result = quicksort(repeated_number)
    assert result == repeated_number


def test_sort_list_in_descending_order(descending_unordered, descending_ordered):
    result = quicksort(descending_unordered)
    assert result == descending_ordered
