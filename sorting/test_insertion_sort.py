from sorting import insertion_sort


def test_sort_empty_list():
    result = insertion_sort([])
    assert result == []


def test_sort_list_in_random_order(random_unsorted, random_sorted):
    result = insertion_sort(random_unsorted)
    assert result == random_sorted


def test_sort_list_of_repeated_number(repeated_number):
    result = insertion_sort(repeated_number)
    assert result == repeated_number


def test_sort_list_in_descending_order(descending_unordered, descending_ordered):
    result = insertion_sort(descending_unordered)
    assert result == descending_ordered
