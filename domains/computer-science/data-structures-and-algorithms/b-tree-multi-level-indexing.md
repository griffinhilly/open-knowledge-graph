---
id: b-tree-multi-level-indexing
title: 'B-Trees: Multi-Level Indexing and Database Applications'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-search-tree-search-insert-delete
  type: hard
builds-toward:
- database-schema-design
tags:
- b-tree
- indexing
- database
stage: formal-systems
status: draft
---

# B-Trees: Multi-Level Indexing and Database Applications

## Core Idea
B-trees generalize BSTs to allow multiple keys per node (order t). Searches, insertions, and deletions are O(log n) and optimized for disk I/O—fewer seeks per operation. They're the standard for database indexes and file systems.
