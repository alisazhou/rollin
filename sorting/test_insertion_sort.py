from sorting import insertion_sort


def test_sort_empty_list():
    result = insertion_sort([])
    assert result == []


def test_sort_list_in_random_order(random_unsorted):
    result = insertion_sort(random_unsorted)
    assert result == sorted(random_unsorted)


def test_sort_list_of_repeated_number(repeated_number):
    result = insertion_sort(repeated_number)
    assert result == sorted(repeated_number)


def test_sort_list_in_descending_order(descending_unordered):
    result = insertion_sort(descending_unordered)
    assert result == sorted(descending_unordered)
