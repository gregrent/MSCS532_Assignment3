# MSCS 532 Assignment 3
# Randomized Quicksort Algorithm

import random

def randomized_quicksort(arr):
    def quicksort(low, high):
        if low < high:
            pivot_index = randomized_partition(low, high)
            quicksort(low, pivot_index - 1)
            quicksort(pivot_index + 1, high)

    def randomized_partition(low, high):
        # Choose a random pivot index and swap it with the last element
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        return partition(low, high)

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if arr:  # Only sort if the array is non-empty
        quicksort(0, len(arr) - 1)

# Example usage
if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [3, 1, 2],
        [5, 5, 5, 5],
        [1, 2, 3, 4, 5],
        [9, 7, 5, 3, 1],
        [10, -1, 2, 5, 0, 6, 4]
    ]

    for case in test_cases:
        arr = case[:]
        print(f"Original: {arr}")
        randomized_quicksort(arr)
        print(f"Sorted:   {arr}\n")
