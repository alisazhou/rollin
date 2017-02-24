from sorting import selection_sort


def test_sort_empty_list():
    result = selection_sort([])
    assert result == []


def test_sort_list_in_random_order(random_unsorted):
    result = selection_sort(random_unsorted)
    assert result == sorted(random_unsorted)


def test_sort_list_of_repeated_number(repeated_number):
    result = selection_sort(repeated_number)
    assert result == sorted(repeated_number)


def test_sort_list_in_descending_order(descending_unordered):
    result = selection_sort(descending_unordered)
    assert result == sorted(descending_unordered)
