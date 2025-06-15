# MSCS532_Assignment3

# 🔧 Hash Table with Chaining & 🌀 Randomized Quicksort

## 📦 Overview

This project includes two core data structure and algorithm implementations in Python:

1. **Hash Table using Chaining**  
   - Collision resolution via linked lists (chaining)
   - Universal hash function for better distribution
   - Supports insert, search, and delete operations efficiently

2. **Randomized Quicksort**  
   - Random pivot selection to avoid worst-case partitioning
   - Handles various input types: sorted, reverse-sorted, repeated elements
   - Compared against Deterministic Quicksort (using first element as pivot)

---

## 🚀 How to Run

### Requirements
- Python 3.6 or higher (no external libraries needed)

### Running the Randomized Quicksort Demo
python randomized_quicksort.py

### Running the Hash Table Demo
python hashing_with_chaining.py

---

## 📊 Theoretical Summary

Randomized Quicksort
- Average Case: 𝑂(n log n)
- Worst Case: 𝑂(n²) (rare due to random pivot selection)
- More robust than Deterministic Quicksort
- Performs better on sorted or duplicate-heavy inputs

Hash Table - Expected Time Complexity
- Insert/Search/Delete:
  𝑂(1 + α), where α = n / m (load factor)
- Performance degrades if α becomes large
- Use dynamic resizing and universal hashing to maintain constant-time operations


## 📈 Findings

Hash Table
- Performs efficiently under uniform hashing with low load factor
- Gracefully handles duplicates and deletions
- Without resizing, high load factors lead to degraded performance due to longer chains
- Universal hashing ensures better key distribution and reduces collision clustering

Randomized Quicksort
- Outperforms Deterministic Quicksort on sorted and reverse-sorted arrays
- Consistently maintains 𝑂(n log n) time on random and duplicate-filled inputs
- Deterministic Quicksort often hits 𝑂(n²) on already sorted data due to unbalanced partitions
- Random pivoting improves recursion balance and average-case reliability

