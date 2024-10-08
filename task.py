import timeit
import random


# Generate a list of numbers from 1 to n
def generate_unique_numbers(n):
    numbers = list(range(1, n + 1))
    random.shuffle(numbers)
    return numbers


# Timsort using the sorted() function (returns a new sorted list)
def timsort_sorted(array):
    return sorted(array)


# Timsort using the sort() method (sorts the list in place)
def timsort_sort(array):
    array.sort()
    return array


# Insertion sort algorithm
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


# Merge sort algorithm
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


# Merge helper function for merge sort
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Function to measure sorting execution times
def sorting_measurement(size):
    print(f"Number of items to measure: '{size}'")

    # Measure execution time for Timsort (sorted)
    execution_time = timeit.timeit(lambda: timsort_sorted(generate_unique_numbers(size)), number=1)
    print(f"Execution time for 'Timsort (sorted)': {execution_time} seconds")

    # Measure execution time for Timsort (sort)
    execution_time = timeit.timeit(lambda: timsort_sort(generate_unique_numbers(size)), number=1)
    print(f"Execution time for 'Timsort (sort)': {execution_time} seconds")

    # Measure execution time for merge sort
    execution_time = timeit.timeit(lambda: merge_sort(generate_unique_numbers(size)), number=1)
    print(f"Execution time for 'Merge sort': {execution_time} seconds")

    # Measure execution time for insertion sort
    execution_time = timeit.timeit(lambda: insertion_sort(generate_unique_numbers(size)), number=1)
    print(f"Execution time for 'Insertion sort': {execution_time} seconds")


# Measure for different list sizes
sorting_measurement(1000)
sorting_measurement(10000)
sorting_measurement(100000)
sorting_measurement(1000000)
