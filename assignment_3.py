# MSCS 532 Assignment 3
# Hashing with Chaining Algorithm and Randomized Quicksort Algorithm

import random

# ---------- Universal Hash Table with Chaining ----------
class UniversalHashTable:
    def __init__(self, size=101):
        self.size = size  # Number of buckets (should be a prime)
        self.p = 109345121  # A large prime number > size
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
        self.table = [[] for _ in range(size)]  # Chaining: each bucket is a list

    def _hash(self, key):
        # Convert the key to an integer hash code
        key_hash = hash(key)
        # Universal hash function: ((a * key_hash + b) mod p) mod m
        return ((self.a * key_hash + self.b) % self.p) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Add new key-value pair

    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None  # Key not found

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False  # Key not found

    def __repr__(self):
        return str(self.table)

# ---------- Randomized Quicksort ----------
def randomized_quicksort(arr):
    def quicksort(low, high):
        if low < high:
            pivot_index = randomized_partition(low, high)
            quicksort(low, pivot_index - 1)
            quicksort(pivot_index + 1, high)

    def randomized_partition(low, high):
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

    if arr:
        quicksort(0, len(arr) - 1)

# ---------- Main Program ----------
if __name__ == "__main__":
    print("=== Hash Table Demo ===")
    ht = UniversalHashTable(size=17)

    # Insert some key-value pairs
    ht.insert("apple", 5)
    ht.insert("banana", 3)
    ht.insert("orange", 8)

    print("Search apple:", ht.search("apple"))
    print("Search grape:", ht.search("grape"))

    ht.insert("apple", 10)
    print("Updated apple:", ht.search("apple"))

    ht.delete("banana")
    print("After deleting banana:", ht.search("banana"))

    print("\nFull Table:\n", ht)

    print("\n=== Randomized Quicksort Demo ===")
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
