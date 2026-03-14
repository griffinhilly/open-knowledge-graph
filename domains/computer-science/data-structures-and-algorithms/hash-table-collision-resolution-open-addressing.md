---
id: hash-table-collision-resolution-open-addressing
title: 'Hash Tables: Collision Resolution by Open Addressing'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: hash-function-design-universal
  type: hard
- id: hash-tables
  type: soft
tags:
- hash-table
- open-addressing
- collision
stage: formal-systems
status: draft
---

# Hash Tables: Collision Resolution by Open Addressing

## Core Idea
Open addressing probes for an empty slot when collision occurs. Linear probing (i+1, i+2, ...) is simple but suffers clustering. Quadratic probing (i+1², i+2², ...) and double hashing (second hash function) reduce clustering. Load factor α must stay low (< 0.5–0.75).
