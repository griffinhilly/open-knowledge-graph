---
id: index-types-btree-hash-bitmap
title: 'Index Types: B-Trees, Hash Indexes, and Bitmap Indexes'
domain: computer-science
course: databases
prerequisites:
- id: b-trees
  type: hard
- id: hash-indexes
  type: hard
- id: indexing-concepts
  type: hard
builds-toward:
- physical-storage-pages-records
- index-design-selection
tags:
- index-types
- B-tree
- hash
- bitmap
- tradeoffs
stage: formal-systems
status: draft
---

# Index Types: B-Trees, Hash Indexes, and Bitmap Indexes

## Core Idea
B-tree indexes provide sorted access supporting range queries through multi-level balanced tree structures; hash indexes use hash functions for fast exact-match lookups but don't support range queries; bitmap indexes use bit arrays for low-cardinality columns, excelling in data warehouse environments. Each type has different I/O characteristics, space requirements, and INSERT/UPDATE/DELETE costs.
