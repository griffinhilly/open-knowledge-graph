---
id: hash-function-design-universal
title: Hash Function Design and Universal Hashing
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: algorithm-design-basics
  type: hard
builds-toward:
- hash-table-collision-resolution-chaining
- hash-table-collision-resolution-open-addressing
tags:
- hash-function
- hashing
- universal
stage: formal-systems
status: draft
---

# Hash Function Design and Universal Hashing

## Core Idea
Good hash functions distribute keys uniformly to minimize collisions. Division hashing (h(k) = k mod m), multiplication hashing, and universal hashing families (randomized) are common. Bad hashing leads to clustering and O(n) performance.
