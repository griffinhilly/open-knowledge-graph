---
id: hash-tables
title: Hash Tables
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: time-space-complexity
  type: hard
builds-toward:
- tries
- memoization-and-tabulation
tags:
- hash-table
- hashing
- collision
- dictionary
- key-value
stage: formal-systems
status: draft
---

# Hash Tables

## Core Idea
A hash table stores key-value pairs and supports O(1) average-case insertion, deletion, and lookup. A hash function maps keys to array indices; since the key domain is typically larger than the table size, collisions (two keys mapping to the same index) are inevitable. Common collision resolution strategies are chaining (each slot holds a linked list) and open addressing (probe for the next open slot). A good hash function distributes keys uniformly; poor hash functions lead to many collisions and degrade performance to O(n).

## How It's Best Learned
Implement a simple hash table with chaining from scratch. Experiment with different hash functions and load factors to observe their effect on collision rates. Then examine how Python's dict handles resizing.

## Common Misconceptions
- O(1) average case assumes a good hash function and a low load factor; worst case is O(n) with many collisions.
- Hash tables do not preserve insertion order in most implementations (Python 3.7+ dicts are an exception).
- Hash tables and hash sets are distinct: a set stores only keys; a map stores key-value pairs.
