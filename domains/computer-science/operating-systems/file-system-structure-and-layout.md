---
id: file-system-structure-and-layout
title: File System Structure and Layout
domain: computer-science
course: operating-systems
prerequisites:
- id: disk-io-scheduling
  type: soft
- id: memory-management-paging
  type: soft
tags:
- file-systems
- storage
- data-structures
stage: formal-systems
status: draft
---

# File System Structure and Layout

## Core Idea
File systems organize disk storage into files and directories. An inode contains metadata (ownership, permissions, block pointers). Data blocks store file content; inodes are indexed in a table or B-tree. The OS maintains a directory structure (typically hierarchical) and allocation bitmaps to track free blocks. File system design balances performance, reliability, and recovery capability.

## Explainer

A disk is fundamentally a flat array of blocks (typically 4 KB each), numbered from 0 to some maximum. Without a file system, you would need to remember that your essay starts at block 7,342 and spans 15 blocks, your spreadsheet lives at block 22,107, and so on. A **file system** imposes structure on this flat space, providing the abstractions you take for granted: named files, directories, permissions, and the ability to grow or shrink files without manually tracking blocks.

The key data structure in Unix-style file systems is the **inode** (index node). Each file or directory has exactly one inode, which stores all metadata — owner, group, permissions, timestamps, file size — and, crucially, pointers to the data blocks containing the file's content. For small files, the inode's direct pointers (typically 12-15 of them) point straight to data blocks. For larger files, the inode uses **indirect pointers**: a single-indirect pointer points to a block full of block pointers, a double-indirect pointer points to a block of single-indirect pointers, and a triple-indirect pointer adds yet another level. This hierarchical pointer structure allows a fixed-size inode to address files ranging from a few kilobytes to several terabytes.

A **directory** is itself a file whose data blocks contain a table mapping names to inode numbers. When you type `ls /home/user/report.txt`, the file system reads the root directory's inode, finds the data blocks listing its entries, locates "home" and its inode number, reads that inode to find its data blocks, locates "user," and so on until it resolves "report.txt" to an inode number. This is **path resolution**, and it explains why deeply nested paths are slightly slower to access — each component requires an inode lookup and a directory scan.

The file system also needs bookkeeping structures to manage free space. A **superblock** stores global metadata: total size, block size, number of inodes, pointers to free-space management structures. **Allocation bitmaps** — one for data blocks and one for inodes — use one bit per block or inode to track whether it is free or in use. Allocating a new block means scanning the bitmap for a 0 bit, setting it to 1, and returning that block number. This layout — superblock, inode table, bitmaps, data blocks — is replicated across **block groups** in modern file systems like ext4, so that related data (a file's inode and its data blocks) tends to be physically close on disk, reducing seek time and improving performance.
