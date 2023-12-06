"""
Sorting Algorithms
Shams Alkhalidy
"""

import random
import time
from typing import TypeVar, List, Callable, Dict, Tuple
from dataclasses import dataclass

T = TypeVar("T")  # represents generic type


# do_comparison is an optional helper function but HIGHLY recommended!!!
def do_comparison(first: T, second: T, comparator: Callable[[T, T], bool], descending: bool) -> bool:
    """
    Compare two elements 'first' and 'second' using the provided 'comparator' function to determine their ordering.
    :param first : The first element of type 'T' to be compared.
    :param second : The second element of type 'T' to be compared.
    :param comparator: A callable function that takes two elements of type 'T'
            and returns a boolean value indicating their ordering. If 'comparator(a, b)' returns True,
            it implies that 'a' should come before 'b' in a sorted list.
    :param descending : A boolean flag that determines the sorting order. If True, the comparison
            will be done in descending order; otherwise, it will be done in ascending order.
    :return bool: True if 'first' should come before 'second' based on the 'comparator' and 'descending' flag,
        otherwise, False.
    """
    # if descending:
    #     return first > second  # 2, 1 True
    # else:
    #     return first < second  # 1 , 2 : True
    if descending:
        return comparator(second, first)  # second > first
    else:
        return comparator(first , second) # first < second

def selection_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Given a list of values, sort that list in-place using the selection sort algorithm and the provided comparator,
    and perform the sort in descending order if descending is True.
    :param data: List of items to be sorted
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be
                        treated as less than the second argument.
    :param descending: Perform the sort in descending order when this is True. Defaults to False.
    :return: None
    Time Complexity: O(n^2)
    Aux.Space Complexity: O(1)
    """
    # look for min value, then swap it
    if not descending:
        for i in range(len(data)-1):
            smallest_index = i
            for j in range(i+1, len(data)):
                # if first index isnt < second,, meaning second is smaller, making second index smallest index
                if not do_comparison(data[smallest_index], data[j], comparator, False):
                # if comparator(data[j] , data[smallest_index]):
                # if data[j] < data[smallest_index]:  # j should be < i , 3,7
                    smallest_index = j
            data[i], data[smallest_index] = data[smallest_index], data[i]
    elif descending:
        for i in range(len(data)-1):
            biggest_index = i
            for j in range(i+1, len(data)):
                # if first index isn't greater than second, make biggest_index the second index
                if not do_comparison(data[biggest_index], data[j], comparator, True):
                    biggest_index = j
            data[i], data[biggest_index] = data[biggest_index], data[i]



def bubble_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                descending: bool = False) -> None:
    """
    Given a list of values, sort that list in-place using the bubble sort algorithm and the provided comparator, and
    perform the sort in descending order if descending is True.
    :param data: List of items to be sorted
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be treated as less than the second argument.
    :param descending: Perform the sort in descending order when this is True. Defaults to False.
    :return: None
    Time Complexity: O(n^2)
    Aux.Space Complexity: O(1)
    """
    if not descending:
        for i in range(len(data)-1):
            for j in range(0, len(data)-i-1):
                if not do_comparison(data[j], data[j+1], comparator, False):  # if first isnt less than second, swap
                    data[j], data[j+1] = data[j+1], data[j]
    elif descending:
        for i in range(len(data)-1):
            for j in range(0, len(data)-i-1):
                if not do_comparison(data[j], data[j+1], comparator, True):  # if first isnt greater than second, swap
                    data[j], data[j+1] = data[j+1], data[j]

def insertion_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    Given a list of values, sort that list in-place using the insertion sort algorithm and the provided comparator, and perform the sort in descending order if descending is True.
    :param data: List of items to be sorted
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be treated as less than the second argument.
    :param descending: Perform the sort in descending order when this is True. Defaults to False.
    :returns None:
    Time Complexity: O(n^2), faster for smaller inputs
    Aux.Space Complexity: O(1)
    """
    if len(data) <= 1:
        return  # No sorting needed for lists of length 1 or less
    if not descending:
        for i in range(1, len(data)):  # start at the second index/ unsorted list. 2,4
            key = data[i]
            j = i-1  # Initialize a variable 'j' to the current index 'i'.
            # repeatedly compare and swap elements elements
            while j >= 0 and not do_comparison(data[j], key, comparator, False):
                # insert the element at i if the element at the current index 'i' is smaller than the one before it.[j]
                data[j+1] = data[j]     # shift data[j] to next index
                j = j-1
            data[j+1] = key         # insert key into data[j] index
    elif descending:
        for i in range(1, len(data)):
            key = data[i]
            j = i-1
            while j >= 0 and not do_comparison(data[j], key, comparator, True):
                data[j+1] = data[j]
                j = j-1
            data[j+1] = key

def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    Given a list of values, sort that list using a hybrid sort with the merge sort and insertion sort algorithms and
    the provided comparator, and perform the sort in descending order if descending is True.
    The function should use insertion_sort to sort lists once their size is less than or equal to threshold, and
    otherwise perform a merge sort.
    :param data: List of items to be sorted
    :param threshold: Maximum size at which insertion sort will be used instead of merge sort.
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be treated as less than the second argument.
    :param descending: Perform the sort in descending order when this is True. Defaults to False.
    :return None:
    Time Complexity: O(n log(n)), Aux. Space Complexity: O(n)
    """
    if len(data) <= 1:
        return

    if len(data) <= threshold:
        insertion_sort(data, comparator=comparator, descending=descending)
    else:
        # Split the data into two halves, mergesorting/dividing until base case
        middle = len(data) // 2
        left_half = data[:middle]
        right_half = data[middle:]
        # Recursively sort the left and right halves
        hybrid_merge_sort(left_half, threshold=threshold, comparator=comparator, descending=descending)
        hybrid_merge_sort(right_half, threshold=threshold, comparator=comparator, descending=descending)

        # Track the length of lists being sorted by doing insertion sort if less than threshold
        if len(left_half) <= threshold:
            insertion_sort(left_half, comparator=comparator, descending=descending)
        if len(right_half) <= threshold:
            insertion_sort(right_half, comparator=comparator, descending=descending)

        # Merge the sorted left and right halves back into the original data, merge sorting happens here, if len > threshold
        merge(data, left_half, right_half, comparator=comparator, descending=descending)


def merge(data: List[T], left: List[T], right: List[T], *, comparator: Callable[[T, T], bool], descending: bool) -> None:
    """
    Merge two sorted lists 'left' and 'right' into the list 'data' using the provided comparator.
    :param data: The list to merge into
    :param left: The sorted left half of the data
    :param right: The sorted right half of the data
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be treated as less than the second argument.
    :param descending: Perform the merge in descending order if True
    :return None:
    """
    i = j = k = 0

    while i < len(left) and j < len(right):
        # if ascending
        if do_comparison(left[i], right[j], comparator, descending):
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1


def maximize_rewards(item_prices: List[int]) -> (List[Tuple[int, int]], int):
    """
    Split orders into pairs with consistent sums and compute the reward points
    :param item_prices: A list of integers representing the price of each food item.
    :return: A tuple containing a list of paired items and the total reward points.
    """
    # if list is empty or has one item
    if len(item_prices) <= 1:
        return ([], -1)

    # if list is odd
    if len(item_prices) % 2 != 0:
        return ([], -1)
    # if list is even
    hybrid_merge_sort(item_prices)  # sort the data

    pairs = []  # initialize the pairs list and reward
    reward = 0
    # initializing pointers, one starting from beginning and one from end
    left_pointer = 0
    right_pointer = len(item_prices)-1

    while left_pointer < right_pointer:
        # computing the sum for each pair
        pair_sum = item_prices[left_pointer] + item_prices[right_pointer]
        # Check if the current pair has the same sum as previous one, if not, return none
        if left_pointer > 0 and pair_sum != item_prices[left_pointer-1] + item_prices[right_pointer+1]:
            return ([], -1)

        # adding the pairs into the pair list
        pairs.append((item_prices[left_pointer], item_prices[right_pointer]))
        reward += item_prices[left_pointer] * item_prices[right_pointer]

        left_pointer += 1   # moving to next
        right_pointer -= 1  # moving back
    return pairs, reward


def quicksort(data) -> None:
    """
    Sorts a list in place using quicksort
    :param data: Data to sort
    """

    def quicksort_inner(first, last) -> None:
        """
        Sorts portion of list at indices in interval [first, last] using quicksort

        :param first: first index of portion of data to sort
        :param last: last index of portion of data to sort
        Like merge sort, quicksort is average case O(n log(n)), but its worst case performance is O(n^2).
        """
        # List must already be sorted in this case
        if first >= last:
            return

        left = first
        right = last

        # Need to start by getting median of 3 to use for pivot
        # We can do this by sorting the first, middle, and last elements
        midpoint = (right - left) // 2 + left
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]
        if data[left] > data[midpoint]:
            data[left], data[midpoint] = data[midpoint], data[left]
        if data[midpoint] > data[right]:
            data[midpoint], data[right] = data[right], data[midpoint]
        # data[midpoint] now contains the median of first, last, and middle elements
        pivot = data[midpoint]
        # First and last elements are already on right side of pivot since they are sorted
        left += 1
        right -= 1

        # Move pointers until they cross
        while left <= right:
            # Move left and right pointers until they cross or reach values which could be swapped
            # Anything < pivot must move to left side, anything > pivot must move to right side
            #
            # Not allowing one pointer to stop moving when it reached the pivot (data[left/right] == pivot)
            # could cause one pointer to move all the way to one side in the pathological case of the pivot being
            # the min or max element, leading to infinitely calling the inner function on the same indices without
            # ever swapping
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1

            # Swap, but only if pointers haven't crossed
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        quicksort_inner(first, left - 1)
        quicksort_inner(left, last)

    # Perform sort in the inner function
    quicksort_inner(0, len(data) - 1)


