"""
Hand-rolling classic sorting algos (all return sorted in ascending order).
    - selection sort
    - insertion sort
    - mergesort
    - quicksort
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


def mergesort(unsorted_list):
    """
    Recursively divides list into two halves, calls itself for each half, and
    then merges the two sorted halves.
    """
    n = len(unsorted_list)
    if n <= 1:
        return unsorted_list

    mid_pt = n // 2
    unsorted_left = unsorted_list[:mid_pt]
    unsorted_right = unsorted_list[mid_pt:]

    sorted_left = mergesort(unsorted_left)
    sorted_right = mergesort(unsorted_right)
    sorted_list = merge(sorted_left, sorted_right)
    return sorted_list


def merge(sorted_l, sorted_r):
    merged_list = []
    ind_l, ind_r = 0, 0
    len_l, len_r = len(sorted_l), len(sorted_r)
    while ind_l < len_l and ind_r < len_r:
        elem_l = sorted_l[ind_l]
        elem_r = sorted_r[ind_r]
        if elem_l <= elem_r:
            merged_list.append(elem_l)
            ind_l += 1
        else:
            merged_list.append(elem_r)
            ind_r += 1
    if ind_l < len_l:
        # all elems of sorted_r have been merged
        merged_list += sorted_l[ind_l:]
    elif ind_r < len_r:
        # all elems of sorted_l have been merged
        merged_list += sorted_r[ind_r:]
    return merged_list


def selection_sort(unsorted_list):
    """
    In each iteration, pop the smallest, add it to the end of sorted array.
    """
    in_order = []
    unsorted_list_copy = unsorted_list[:]
    while unsorted_list_copy:
        smallest = unsorted_list_copy[0]
        for i in unsorted_list_copy:
            if i < smallest:
                smallest = i
        unsorted_list_copy.remove(smallest)
        in_order.append(smallest)
    return in_order


def quicksort(unsorted_list):
    """
    Pick first elem as pivot, partition list into less-than and greater-than
    pivot, so that at end of iteration, pivot ends up in correct place. Recurse
    on the two partitions.
    """
    if len(unsorted_list) <= 1:
        return unsorted_list

    pivot = unsorted_list[0]
    less_unsorted, greater_unsorted = [], []
    for num in unsorted_list[1:]:
        if num < pivot:
            less_unsorted.append(num)
        else:
            greater_unsorted.append(num)
    less_sorted = quicksort(less_unsorted)
    greater_sorted = quicksort(greater_unsorted)
    sorted_list = less_sorted + [pivot] + greater_sorted
    return sorted_list
