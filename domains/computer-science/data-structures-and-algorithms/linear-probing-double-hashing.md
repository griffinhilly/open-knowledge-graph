---
id: linear-probing-double-hashing
title: 'Open Addressing: Linear Probing and Double Hashing'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: hash-function-design
  type: hard
- id: hash-tables
  type: hard
tags:
- open-addressing
- hash-tables
- collision-resolution
- linear-probing
- double-hashing
stage: formal-systems
status: draft
---

# Open Addressing: Linear Probing and Double Hashing

## Core Idea
Open addressing resolves collisions by storing all keys in the table itself, probing for empty slots when collisions occur. Linear probing checks consecutive slots (h, h+1, h+2, ...), while double hashing uses a second hash function h(k, i) = (h1(k) + i*h2(k)) mod m to avoid clustering. Both achieve O(1) amortized lookup with load factor below 0.5–0.75.

## How It's Best Learned
Trace insertion and lookup with primary clustering visible in linear probing. Implement both methods and measure performance. Understand load factor and table resizing triggers. See how double hashing mitigates primary clustering better than linear probing.

## Common Misconceptions
- Open addressing is always faster than chaining (depends on load factor, cache locality, and implementation). - Linear probing is simpler and better than double hashing (double hashing avoids primary clustering).
