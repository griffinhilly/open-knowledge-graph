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

## Explainer

When you interact with a database through SQL, you think in terms of tables, rows, and columns. But the database engine must eventually read and write actual bytes on a physical disk, and understanding how it organizes those bytes explains why some queries are fast and others are slow. The fundamental unit of disk I/O is the **page** — a fixed-size block, typically 4KB or 8KB. Every time the database needs data, it reads at least one full page from disk into memory, even if it only needs a single row. This is because disks are optimized for sequential block reads, not random byte access.

Within each page, the database stores **records** (rows). A page has a header containing metadata — how many records it holds, how much free space remains, and a **slot array** that acts like a table of contents. Each slot points to the byte offset where a record begins within the page. This indirection is important: if a record is moved within the page (say, during compaction), only its slot pointer needs updating, not every external reference to that record. Think of it like a library where each shelf has a directory card — you look up the card to find where the book actually sits.

Records themselves have structure. Columns with fixed-size types (INTEGER, CHAR(10)) occupy a predictable number of bytes and are stored in a **fixed-length portion** at the front of the record. Variable-length columns (VARCHAR, TEXT, BLOB) go in a **variable-length portion**, with offset pointers indicating where each variable field starts and ends. This split lets the database quickly jump to any fixed column by arithmetic alone, while still accommodating arbitrarily sized text or binary data.

A **heap file** is the simplest way to organize pages: new records are appended wherever there is space, with no particular ordering. This means finding a specific record requires scanning every page in the file — a **full table scan**. For a table with 1 million rows at 100 bytes per row and 8KB pages, that is roughly 12,500 pages the database must read. This cost is predictable and calculable, which is exactly the point: understanding page-level organization lets you reason concretely about I/O costs. When you later learn about indexes and buffer pools, you will see how they reduce the number of pages that must be read — but the page remains the atomic unit of all that optimization.
