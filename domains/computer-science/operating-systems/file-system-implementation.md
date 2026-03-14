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
