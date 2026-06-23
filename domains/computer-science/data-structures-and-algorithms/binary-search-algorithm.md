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
- id: array-representation-operations-efficiency
  type: hard
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

## Questions

```yaml
- question: "You run binary search on an array that you believe is sorted, but it was accidentally left unsorted. The target value is present. What will happen?"
  type: multiple-choice
  options:
    - "Binary search will still find the target — it checks all elements eventually"
    - "Binary search will return an error because it detects the unsorted order"
    - "Binary search may fail to find the target and return 'not found' even though it is present"
    - "Binary search will find the target but will be slower than linear search"
  answer: 2
  explanation: "Binary search relies on a critical guarantee: if the target is less than the middle element, it cannot be in the right half. This inference is only valid if the array is sorted. On an unsorted array, the target could be anywhere — including in the half that binary search has just eliminated. The algorithm may confidently discard the half containing the target and return 'not found' even when the target is present. This is not a performance issue but a correctness issue: binary search on unsorted data produces wrong answers, not just slow ones. Always verify that the input is sorted before applying binary search."

- question: "Why does binary search achieve O(log n) time complexity?"
  type: multiple-choice
  options:
    - "Because it uses two pointers that move toward each other, halving the work at each step"
    - "Because each comparison eliminates half the remaining candidates, reducing n elements to 1 in at most log₂(n) comparisons"
    - "Because the midpoint calculation takes O(log n) time on modern hardware"
    - "Because it only checks elements at positions that are powers of 2"
  answer: 1
  explanation: "After k comparisons, the search space has been halved k times, leaving n/2^k elements. The algorithm terminates when this reaches 1 (or 0 if the element is absent), so we solve n/2^k = 1 to get k = log₂(n). For n = 1,000,000, that is about 20 comparisons. Linear search, by contrast, may check all n elements. The log comes directly from the repeated halving — which is only possible because sortedness lets you definitively eliminate entire halves. The two-pointer movement in option A is a correct description of *how* binary search works, but the O(log n) complexity comes from the *halving*, not from the pointers per se."

- question: "Binary search can be applied to any problem where a monotonic predicate divides the search space into 'yes' and 'no' regions, not just to sorted arrays."
  type: true-false
  answer: true
  explanation: "The sorted array is just one instance of a general principle: binary search applies wherever there is a monotonic predicate — a yes/no question where all 'yes' answers come before all 'no' answers (or vice versa) across the search space. For example, 'does k workers suffice to handle this load?' may be monotonic: once k is large enough (yes), all larger values also suffice. The smallest satisfying k can be binary searched. 'What is the smallest radius that contains all points?' — similarly monotonic. This generalization, called binary search on the answer, is one of the most powerful algorithmic techniques and appears in competitive programming and system design alike."

- question: "Binary search can be applied to any array, sorted or not, as long as you know the target value you're looking for."
  type: true-false
  answer: false
  explanation: "Sorting is not a convenience — it is a correctness requirement. Binary search's logic depends entirely on the inference: 'if target < a[mid], the target cannot be in a[mid+1..high].' This inference is only valid when the array is sorted. On an unsorted array, the target could be anywhere, and eliminating half the array based on a midpoint comparison is incorrect. The algorithm will produce wrong answers on unsorted input — not slower correct answers. If you need to search an unsorted collection, you must either sort it first (then binary search works in O(n log n) + O(log n)) or use linear search in O(n)."

- question: "What property of a sorted array allows binary search to eliminate half the candidates with a single comparison, and why does the same principle not apply to an unsorted array?"
  type: short-answer
  answer: "In a sorted array, the ordering guarantee means that all elements to the left of any position are smaller and all elements to the right are larger. When we compare the target to the middle element, this guarantee lets us draw an absolute conclusion: if the target is smaller, it cannot exist anywhere in the right half (since every element there is larger than the middle). We have eliminated half the candidates with a single comparison and zero further inspection. In an unsorted array, no such guarantee exists: the target could be anywhere regardless of how it compares to the middle element, so we can eliminate nothing and must check everything."
  explanation: "The key concept is information content of a comparison. In a sorted array, a single comparison carries log₂(n) bits of information — it tells you which half to search. In an unsorted array, a comparison tells you only whether the middle element matches or not — no information about the other n−1 elements. The entire efficiency of binary search is derived from this information amplification, which exists only when the array is sorted."
```

## Explainer

You already know arrays as contiguous blocks of elements accessible by index, and you have some sense of what O(n) versus O(log n) means from complexity analysis. Binary search connects these ideas: it exploits the structure of a sorted array to avoid looking at most of the elements. Imagine searching for a word in a physical dictionary. You would not start at page one and read every entry — you would open to the middle, see whether your word comes before or after that page, and immediately discard half the book. Binary search does exactly this, and the reason it works is that sortedness guarantees: if the target is less than the middle element, it cannot exist anywhere in the right half.

The algorithm maintains two pointers, **low** and **high**, that define the current search space. Initially, low is 0 and high is n-1 (the full array). At each step, compute the **midpoint**: mid = low + (high - low) / 2. Compare the target to the element at mid. If they match, you are done. If the target is smaller, set high = mid - 1 to search the left half. If the target is larger, set low = mid + 1 to search the right half. The search space halves with every comparison, so after k comparisons you have narrowed n elements down to n/2^k. When this reaches 1, you have either found the target or determined it is absent. Solving n/2^k = 1 gives k = log₂(n) — this is why binary search is O(log n). For a million elements, that is roughly 20 comparisons instead of a million.

The most treacherous aspect of binary search is getting the boundary conditions right. Should the loop condition be `while (low <= high)` or `while (low < high)`? Should you set `high = mid` or `high = mid - 1`? These choices are interdependent, and mixing conventions causes either missed elements or infinite loops. The safest approach is to use the inclusive convention: low and high both point to valid, unsearched positions, the loop runs while `low <= high`, and updates are `low = mid + 1` and `high = mid - 1`. Trace through a two-element array by hand to verify your implementation handles the edge case — this is where bugs hide.

Binary search generalizes far beyond finding exact matches in arrays. Any situation where you can define a **monotonic predicate** — a yes/no question where all the "yes" answers come after all the "no" answers (or vice versa) — can be binary searched. For example, "what is the smallest number of servers needed to handle this load?" can be binary searched if you can test whether k servers suffice for any given k. This generalization, often called **binary search on the answer**, is one of the most powerful algorithmic techniques you will encounter, and it rests on the same core insight: sortedness (or monotonicity) lets you eliminate half the candidates with a single test.
