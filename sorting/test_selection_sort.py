from sorting import selection_sort


def test_random_order(random_unsorted, random_sorted):
    result = selection_sort(random_unsorted)
    assert result == random_sorted
