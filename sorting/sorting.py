"""
Hand-rolling classic sorting algos (all return sorted in ascending order).
    - selection sort
"""


def selection_sort(unsorted_list):
    """
    In each iteration, pop the smallest, add it to the end of sorted array.
    """
    in_order = []
    while unsorted_list:
        smallest = unsorted_list[0]
        for i in unsorted_list:
            if i < smallest:
                smallest = i
        unsorted_list.remove(smallest)
        in_order.append(smallest)
    return in_order
