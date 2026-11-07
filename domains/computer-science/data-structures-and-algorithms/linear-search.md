---
id: linear-search
title: Linear Search
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: for-loops
  type: hard
- id: comparison-operators
  type: hard
- id: big-o-complexity-analysis
  type: soft
builds-toward:
- binary-search-algorithm
tags:
- searching
- linear-search
- sequential-search
- algorithms
- arrays
- AP-CSA
stage: formal-systems
status: validated
---
# Linear Search

## Core Idea
Linear search (also called sequential search) finds a target value in a list by checking the elements one at a time, in order, until it finds a match or reaches the end. It returns the position of the first match, or a signal such as -1 when the target is absent. It works on any list, sorted or not. For a list of n elements it makes at most n comparisons, so its worst-case running time is O(n).

## How It's Best Learned
Act it out with a row of face-down cards: turn them over one by one and count the flips needed for different targets, including one that is missing. Then write the loop and trace it on a target at the front, in the middle, at the end, and absent. Count comparisons for each case before introducing big-O, and finally compare the counts with binary search on a sorted list of the same size.

## Common Misconceptions
- The search can return "not found" as soon as one element fails to match. (It may report "not found" only after checking every element; an `else: return -1` inside the loop is a classic bug.)
- Binary search is always the better choice. (Binary search needs sorted data; for unsorted data searched once, sorting first costs more than one linear pass, and for very small lists the difference is negligible.)
- Linear search always takes n steps. (It stops at the first match, so the best case is one comparison; n comparisons is the worst case.)

## Questions

```yaml
- question: "What is wrong with this Python function?\n\ndef find(items, target):\n    for i in range(len(items)):\n        if items[i] == target:\n            return i\n        else:\n            return -1"
  type: multiple-choice
  options:
    - "Nothing; it is a correct linear search"
    - "It checks only the first element, because both branches return during the first pass of the loop"
    - "It skips the first element"
    - "It returns the last match instead of the first"
  answer: 1
  explanation: "On the first iteration, either the if or the else returns, so the loop never reaches index 1. The return -1 belongs after the loop, so it runs only when every element has been checked without a match."

- question: "A linear search runs on an unsorted array of 1,000 distinct values. What is the largest number of element comparisons it can make?"
  type: multiple-choice
  options:
    - "10"
    - "500"
    - "1,000"
    - "1,000,000"
  answer: 2
  explanation: "In the worst case the target is in the last position or absent, so every one of the 1,000 elements is compared once. About 10 is the worst case for binary search on a sorted array of this size, and 500 is roughly the average for a target that is present."

- question: "Because binary search is O(log n) and linear search is O(n), it is always faster to sort an unsorted list and then binary search it than to run one linear search."
  type: true-false
  answer: false
  explanation: "A comparison sort takes O(n log n) time, which is more than the O(n) of a single linear search. Sorting pays off only when the same data will be searched many times."

- question: "A list contains the target value at indexes 3, 7 and 12. A standard linear search that returns as soon as it finds a match is run on it. Which index does it return, and why?"
  type: short-answer
  answer: "It returns 3, because it checks indexes in increasing order and stops at the first element that matches."
  explanation: "Linear search finds the first occurrence. To find all occurrences, the loop must keep going and collect every matching index instead of returning early."
```

## Explainer

Searching is one of the most common jobs a program does: find a name in a contact list, a product in an inventory, a word in a document. The simplest method is the one you would use with a messy stack of papers. Look at the first one. If it is not what you want, look at the next. Keep going until you find it or run out.

In code, linear search is a single loop:

```python
def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1
```

Notice where `return -1` sits. It is after the loop, not inside it. The function can say "not found" only after every element has been checked. Putting the "not found" return in an `else` branch inside the loop is one of the most common beginner bugs, because it makes the function give up after the first element.

How much work does it do? Count comparisons. If the target is first, one comparison. If it is last, or not present, every element is compared, so n comparisons for a list of n items. If the target is equally likely to be anywhere in the list, the average is about (n + 1) / 2. Computer scientists usually describe the worst case, so linear search is **O(n)**: doubling the list roughly doubles the worst-case time.

Linear search has real strengths. It works on unsorted data. It works on structures you can only walk through in order, such as linked lists or a file being read line by line. It is short and hard to get wrong once the return is placed correctly. It also adapts easily: you can search for the largest value, for the first item meeting a condition, or for every match by collecting indexes instead of returning early.

Its weakness appears with large data searched often. A million-element list can require a million comparisons per search. If the list is sorted, **binary search** can find any item in about 20 comparisons by repeatedly halving the range. Sorting has its own cost, so the right choice depends on how often you search. For one search of unsorted data, linear search is the better choice. For many searches of the same data, sorting once and then using binary search is usually worth it.
