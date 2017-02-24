"""
Hand-rolling classic sorting algos (all return sorted in ascending order).
    - selection sort
    - insertion sort
"""


def insertion_sort(unsorted_list):
    """
    For each unsorted elem, iterate through the sorted list, insert into the
    correct place.
    """
    if unsorted_list == []:
        return []
    in_order = [unsorted_list[0]]
    for num in unsorted_list[1:]:
        for i in range(len(in_order)):
            if num < in_order[i]:
                in_order.insert(i, num)
                break
            if i == len(in_order) - 1:
                # current number is greater than all nums in in_order
                in_order.append(num)
    return in_order


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
