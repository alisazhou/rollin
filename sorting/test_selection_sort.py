from sorting import selection_sort


def test_sort_list_in_random_order(random_unsorted, random_sorted):
    result = selection_sort(random_unsorted)
    assert result == random_sorted


def test_sort_list_of_repeated_number(repeated_number):
    orig_list = repeated_number[:]
    result = selection_sort(repeated_number)
    assert result == orig_list


def test_sort_list_in_descending_order(descending_unordered, descending_ordered):
    result = selection_sort(descending_unordered)
    assert result == descending_ordered
