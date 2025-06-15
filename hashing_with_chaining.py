# MSCS 532 Assignment 3
# Hashing with Chaining Algorithm

import random

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
    
if __name__ == "__main__":
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

