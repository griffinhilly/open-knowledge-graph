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

## Questions

```yaml
- question: "A table has 500,000 rows, each 200 bytes. Pages are 8KB. A query needs exactly one row. How many pages must the database read in the worst case (assuming a heap file with no index)?"
  type: multiple-choice
  options:
    - "1 page — the database reads only the page containing the needed row"
    - "500 pages — one page per thousand rows"
    - "Approximately 12,500 pages — the entire heap file must be scanned"
    - "200 pages — one page per byte in the row"
  answer: 2
  explanation: "A heap file stores records in no particular order, so without an index the database has no way to know which page holds the target row — it must read every page until it finds the row (or confirms it is absent). Pages hold 8192 / 200 ≈ 40 rows each, so 500,000 rows ÷ 40 rows/page = 12,500 pages. Even for a single-row query, the database may read all 12,500 pages. This is the cost that indexes are designed to eliminate — but understanding the baseline page-scan cost explains why indexes matter."

- question: "When a record is moved within a page during compaction, the database must update every external reference (such as index entries) pointing to that record's location."
  type: multiple-choice
  options:
    - "True — every reference stores the physical byte offset, so any move requires updating all references"
    - "False — the slot array provides indirection so only the slot pointer needs updating, not external references"
    - "True — slot arrays only help within a page, not for cross-page references"
    - "False — records can never be moved once written; compaction is not possible"
  answer: 1
  explanation: "The slot array is specifically designed to handle this. External references (such as index entries) point to a record ID that includes the page number and slot number — not the raw byte offset within the page. When a record moves during compaction, only its slot entry (byte offset within the page) is updated. All external references continue to point to the same slot, which now reflects the new position. This indirection is the reason slot arrays exist: they decouple external references from the physical layout within a page."

- question: "The database reads a minimum of one full page from disk even if the query only needs a single column from a single row."
  type: true-false
  answer: true
  explanation: "The page is the atomic unit of disk I/O — disks are optimized for reading fixed-size sequential blocks, not random byte access. When the database needs any data from a page, the entire page is transferred into the buffer pool. There is no mechanism to read 'just the column you need' from disk at a sub-page granularity. This is why column-oriented storage (a more advanced topic) offers I/O advantages for analytical queries that read few columns from many rows — it physically groups column data so that reading a column requires fewer pages."

- question: "Variable-length columns (VARCHAR, TEXT) are stored at the beginning of a record so the database can quickly locate them."
  type: true-false
  answer: false
  explanation: "It is the opposite: fixed-length columns are stored first (in a fixed-length portion), precisely because their byte offsets are arithmetically predictable — to reach the 3rd fixed-length column, you add up the sizes of the first two. Variable-length columns follow in a separate portion, with offset pointers indicating where each one starts and ends. This layout lets the database jump directly to any fixed column without parsing variable-length data, which would require scanning from the beginning of the record each time."

- question: "Why is the page the fundamental unit of disk I/O in a database system, and what consequence does this have for query performance?"
  type: short-answer
  answer: "Disk hardware is designed for sequential block access, not random byte access. Reading a single byte requires the same mechanical seek and rotational latency as reading a full 4KB or 8KB block, so the database always reads in page-sized units to amortize that fixed cost. The consequence is that I/O cost is measured in pages, not rows. A query that touches one row on each of 10,000 pages costs as much as reading 10,000 complete pages, even if only tiny fractions of those pages are needed. This makes the number of pages accessed — not the number of rows — the primary predictor of query cost, and it explains why index structures (which reduce page accesses) and physical data layout (which clusters related rows on the same page) are the main levers of database performance optimization."
  explanation: "Understanding page-level I/O is the foundation for reasoning about any database optimization. When evaluating whether an index helps, you ask: does it reduce the number of pages read? When evaluating whether to cluster a table by a key, you ask: does it ensure that rows likely to be queried together live on the same pages? Every higher-level optimization technique (indexes, buffer pools, partitioning) ultimately works by reducing page-level I/O."
```

## Explainer

When you interact with a database through SQL, you think in terms of tables, rows, and columns. But the database engine must eventually read and write actual bytes on a physical disk, and understanding how it organizes those bytes explains why some queries are fast and others are slow. The fundamental unit of disk I/O is the **page** — a fixed-size block, typically 4KB or 8KB. Every time the database needs data, it reads at least one full page from disk into memory, even if it only needs a single row. This is because disks are optimized for sequential block reads, not random byte access.

Within each page, the database stores **records** (rows). A page has a header containing metadata — how many records it holds, how much free space remains, and a **slot array** that acts like a table of contents. Each slot points to the byte offset where a record begins within the page. This indirection is important: if a record is moved within the page (say, during compaction), only its slot pointer needs updating, not every external reference to that record. Think of it like a library where each shelf has a directory card — you look up the card to find where the book actually sits.

Records themselves have structure. Columns with fixed-size types (INTEGER, CHAR(10)) occupy a predictable number of bytes and are stored in a **fixed-length portion** at the front of the record. Variable-length columns (VARCHAR, TEXT, BLOB) go in a **variable-length portion**, with offset pointers indicating where each variable field starts and ends. This split lets the database quickly jump to any fixed column by arithmetic alone, while still accommodating arbitrarily sized text or binary data.

A **heap file** is the simplest way to organize pages: new records are appended wherever there is space, with no particular ordering. This means finding a specific record requires scanning every page in the file — a **full table scan**. For a table with 1 million rows at 100 bytes per row and 8KB pages, that is roughly 12,500 pages the database must read. This cost is predictable and calculable, which is exactly the point: understanding page-level organization lets you reason concretely about I/O costs. When you later learn about indexes and buffer pools, you will see how they reduce the number of pages that must be read — but the page remains the atomic unit of all that optimization.
