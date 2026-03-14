---
id: sorting-linear-time-counting-radix
title: 'Linear-Time Sorting: Counting Sort and Radix Sort'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: sorting-comparison-based-lower-bounds
  type: hard
tags:
- sorting
- linear-time
- counting-radix
stage: formal-systems
status: draft
---

# Linear-Time Sorting: Counting Sort and Radix Sort

## Core Idea
Counting sort achieves O(n + k) time for keys in [0, k-1] by counting occurrences and rebuilding. Radix sort applies counting sort to each digit, sorting in O(d(n + b)) time for d digits and base b. Both break the comparison lower bound by exploiting key structure.
