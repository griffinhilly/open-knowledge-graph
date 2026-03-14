---
id: hash-table-collision-resolution-chaining
title: 'Hash Tables: Collision Resolution by Chaining'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: hash-function-design-universal
  type: hard
- id: hash-tables
  type: soft
tags:
- hash-table
- chaining
- collision
stage: formal-systems
status: draft
---

# Hash Tables: Collision Resolution by Chaining

## Core Idea
Chaining stores colliding keys in a linked list at each bucket. Search/insert/delete is O(1 + α) expected, where α = n/m is the load factor. High α increases average chain length; rehashing when α > threshold maintains performance.
