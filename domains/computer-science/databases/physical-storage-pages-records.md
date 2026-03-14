---
id: physical-storage-pages-records
title: 'Physical Storage: Pages, Records, and Heap Files'
domain: computer-science
course: databases
prerequisites:
- id: database-systems-introduction
  type: hard
builds-toward:
- buffer-pool-cache-management
- index-types-btree-hash-bitmap
tags:
- physical-storage
- pages
- heap-files
- record-layout
stage: formal-systems
status: draft
---

# Physical Storage: Pages, Records, and Heap Files

## Core Idea
Databases organize data into fixed-size pages (typically 4-8KB) as the unit of disk I/O. Pages contain records (rows) with headers tracking metadata. Heap files store records in arbitrary order, requiring full table scans. Record formats include a fixed portion (known-size columns) and variable portion (VARCHAR, BLOB). Slot arrays within pages track record locations. Understanding page organization predicts I/O costs accurately.
