---
id: binary-search-algorithm
title: Binary Search
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: time-space-complexity
  type: soft
- id: recursion-basics
  type: soft
- id: logarithms-intro
  type: soft
builds-toward:
- binary-search-trees
- divide-and-conquer-strategy
tags:
- searching
- binary-search
- divide-and-conquer
- sorted-arrays
stage: formal-systems
status: validated
---

# Binary Search

## Core Idea
Binary search finds a target value in a sorted array by repeatedly halving the search space. At each step, the algorithm compares the target to the middle element and eliminates half of the remaining candidates. This achieves O(log n) time complexity, a dramatic improvement over O(n) linear search for large datasets. Binary search requires that the input array be sorted, and the key insight is that sortedness allows drawing definitive conclusions about entire halves of the array.

## How It's Best Learned
Implement both iterative and recursive versions. Practice on concrete sorted arrays and trace through the index arithmetic step by step. Pay careful attention to off-by-one errors in the loop bounds (< vs <=, mid+1 vs mid).

## Common Misconceptions
- Binary search only works on sorted data; applying it to unsorted arrays yields incorrect results.
- Off-by-one errors in the index update are the most common source of bugs and can cause infinite loops.
- The iterative version avoids stack overflow risks for very large inputs compared to the recursive version.

## Explainer

You already know arrays as contiguous blocks of elements accessible by index, and you have some sense of what O(n) versus O(log n) means from complexity analysis. Binary search connects these ideas: it exploits the structure of a sorted array to avoid looking at most of the elements. Imagine searching for a word in a physical dictionary. You would not start at page one and read every entry — you would open to the middle, see whether your word comes before or after that page, and immediately discard half the book. Binary search does exactly this, and the reason it works is that sortedness guarantees: if the target is less than the middle element, it cannot exist anywhere in the right half.

The algorithm maintains two pointers, **low** and **high**, that define the current search space. Initially, low is 0 and high is n-1 (the full array). At each step, compute the **midpoint**: mid = low + (high - low) / 2. Compare the target to the element at mid. If they match, you are done. If the target is smaller, set high = mid - 1 to search the left half. If the target is larger, set low = mid + 1 to search the right half. The search space halves with every comparison, so after k comparisons you have narrowed n elements down to n/2^k. When this reaches 1, you have either found the target or determined it is absent. Solving n/2^k = 1 gives k = log₂(n) — this is why binary search is O(log n). For a million elements, that is roughly 20 comparisons instead of a million.

The most treacherous aspect of binary search is getting the boundary conditions right. Should the loop condition be `while (low <= high)` or `while (low < high)`? Should you set `high = mid` or `high = mid - 1`? These choices are interdependent, and mixing conventions causes either missed elements or infinite loops. The safest approach is to use the inclusive convention: low and high both point to valid, unsearched positions, the loop runs while `low <= high`, and updates are `low = mid + 1` and `high = mid - 1`. Trace through a two-element array by hand to verify your implementation handles the edge case — this is where bugs hide.

Binary search generalizes far beyond finding exact matches in arrays. Any situation where you can define a **monotonic predicate** — a yes/no question where all the "yes" answers come after all the "no" answers (or vice versa) — can be binary searched. For example, "what is the smallest number of servers needed to handle this load?" can be binary searched if you can test whether k servers suffice for any given k. This generalization, often called **binary search on the answer**, is one of the most powerful algorithmic techniques you will encounter, and it rests on the same core insight: sortedness (or monotonicity) lets you eliminate half the candidates with a single test.
