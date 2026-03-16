---
id: file-system-implementation
title: File System Implementation
domain: computer-science
course: operating-systems
prerequisites:
- id: file-system-concepts
  type: hard
- id: paging
  type: soft
- id: directory-structures
  type: soft
tags:
- inode
- allocation-methods
- contiguous-allocation
- linked-allocation
- indexed-allocation
- FAT
stage: formal-systems
status: validated
---
# File System Implementation

## Core Idea
A file system must decide how to allocate disk blocks to files and how to track that allocation. Three classic methods exist: contiguous allocation (fast sequential access, but suffers external fragmentation and requires knowing file size upfront), linked allocation (each block contains a pointer to the next, allowing dynamic growth but slow random access — FAT is this on-disk), and indexed allocation (one index block holds all data block pointers, supporting efficient random access — the Unix inode is this structure). The inode stores all file metadata plus an array of direct block pointers and indirect block pointers for large files. The file system also maintains a free-space bitmap or free list tracking which disk blocks are available.

## How It's Best Learned
Draw an inode for a 50KB file on a system with 4KB blocks: how many direct, singly indirect, and doubly indirect pointers are needed? Then explain why FAT requires a full table scan to compute file size.

## Common Misconceptions
- The inode does not contain the filename; filenames live in directory entries.
- File system fragmentation on disk (blocks non-contiguous) does not mean the file system is full.

## Explainer

From file system concepts, you know that files are named collections of data and that directories organize them into hierarchies. But the file system must solve a concrete engineering problem: a file is a logical sequence of bytes, while a disk is a flat array of fixed-size blocks (typically 4KB). **File system implementation** is the layer that maps between these two views — deciding which disk blocks belong to which file and how to find them efficiently.

The simplest approach is **contiguous allocation**: store each file in a consecutive run of disk blocks. File "report.pdf" might occupy blocks 100–124. This is fast for sequential reads (the disk head never moves) and trivially supports random access (byte offset N is at block start + N/block_size). But it has a fatal flaw: external fragmentation. As files are created and deleted, the disk becomes a patchwork of free and occupied regions, and eventually there is no contiguous gap large enough for a new file even though plenty of total space exists. This is the same fragmentation problem you may recognize from memory management.

**Linked allocation** solves fragmentation by letting each file scatter its blocks anywhere on disk. Each block contains a pointer to the next block in the file, forming a linked list. Files can grow dynamically and never suffer external fragmentation. The cost is terrible random access — to read the 1000th block, you must follow 999 pointers sequentially. **FAT** (File Allocation Table) is a practical refinement: instead of embedding pointers in data blocks, it stores all the next-block pointers in a separate table in a known disk location. This lets the OS traverse the chain in memory rather than on disk, but computing a file's size still requires walking the entire chain.

**Indexed allocation** — the approach used by Unix/Linux file systems — gives each file an **inode** (index node) that contains an array of pointers to the file's data blocks. For small files, a dozen or so **direct pointers** in the inode point straight to data blocks. For larger files, one pointer leads to a **singly indirect block** — a block full of pointers to data blocks. For very large files, **doubly** and **triply indirect blocks** add further levels of indirection. This structure supports both fast random access (compute which pointer level to traverse) and efficient growth (allocate new blocks and add pointers). Critically, the inode stores all metadata — permissions, timestamps, owner, size — but *not* the filename. Filenames live in directory entries, which are themselves just files mapping names to inode numbers. This separation is why hard links work: multiple directory entries can point to the same inode, sharing a single underlying file.
