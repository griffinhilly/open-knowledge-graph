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

## Questions

```yaml
- question: "A program opens the file /home/user/notes.txt. How does the file system locate the data blocks for this file?"
  type: multiple-choice
  options:
    - "It searches all data blocks sequentially for the file's content, then follows a chain of pointers to remaining blocks"
    - "It looks up 'notes.txt' in a global file name table and retrieves the block address directly"
    - "It reads the root inode, resolves each path component to an inode number by scanning directory data blocks, and reaches the file's inode, which contains pointers to its data blocks"
    - "It reads the superblock, which contains a complete directory tree listing all files and their block addresses"
  answer: 2
  explanation: "Path resolution is an iterative process: the file system starts at the root inode, reads its data blocks (a directory table), finds 'home' and its inode number, reads that inode to find 'home's data blocks, finds 'user' and its inode, then finds 'notes.txt' and its inode — which finally contains the pointers to the file's data blocks. Option A describes a FAT-style linked-list layout, not inode-based file systems. Option B doesn't match any real file system design. The superblock (option D) stores global metadata like block size and counts, not the directory tree."

- question: "A large file requires more storage than the direct pointers in its inode can address. How does the inode handle this?"
  type: multiple-choice
  options:
    - "The file system creates a second inode for the overflow portion and links the two inodes together"
    - "The file is split into fixed-size segments, each with its own inode, presented as a single file by the OS"
    - "The inode uses single-, double-, and triple-indirect pointer blocks, each adding a level of indirection to reach additional data blocks"
    - "The file system allocates contiguous 'super-blocks' and updates the inode's single pointer to this range"
  answer: 2
  explanation: "An inode has a fixed number of direct pointer slots (typically 12–15). For larger files, it uses indirect pointers: a single-indirect pointer points to a block full of data block addresses; a double-indirect pointer points to a block of single-indirect pointers; a triple-indirect adds yet another level. This hierarchical structure lets a fixed-size inode address files from kilobytes to terabytes without splitting across multiple inodes. The key insight is that the indirection blocks are themselves just data blocks used as pointer tables."

- question: "In a Unix-style file system, a directory is a special kind of file whose data blocks contain a mapping from file names to inode numbers."
  type: true-false
  answer: true
  explanation: "This is one of the most important unifications in file system design: directories are ordinary files with a defined format. A directory's data blocks contain a list of (name, inode number) pairs — directory entries. Reading a directory means reading its data blocks and parsing the name-inode pairs to find a target entry. This design makes directories and regular files uniform at the storage level while allowing the OS to enforce directory-specific constraints."

- question: "The inode stores the file's name alongside its metadata so that the OS can look up any file directly by name."
  type: true-false
  answer: false
  explanation: "The inode does NOT store the file's name — names live in directory files, which map names to inode numbers. The inode stores only metadata (permissions, timestamps, owner, size) and block pointers. This separation is intentional: it enables hard links, where multiple directory entries in different directories can point to the same inode number. If names were stored in inodes, one file could not have multiple names. Name lookup requires reading directory data blocks, not just the inode."

- question: "Why does a file's inode not contain the file's name, and what design capability does this separation enable?"
  type: short-answer
  answer: "The inode stores metadata and block pointers but not the name because names live in directory files (as name-to-inode mappings). This separation enables hard links: multiple directory entries in the same or different directories can map different names to the same inode number, giving one file multiple valid names. The inode stores a reference count tracking how many directory entries point to it; blocks are only reclaimed when the count reaches zero. If names were stored in inodes, this many-names-to-one-file relationship would be impossible."
  explanation: "The separation also makes renaming cheap: you update a directory entry without touching the inode or moving data. Moving a file within the same file system is equally fast — remove one directory entry, add another, inode unchanged. This design separates naming (a social/user-space concept) from identity (a storage-level concept), giving Unix file systems both flexibility and efficiency."
```

## Explainer

A disk is fundamentally a flat array of blocks (typically 4 KB each), numbered from 0 to some maximum. Without a file system, you would need to remember that your essay starts at block 7,342 and spans 15 blocks, your spreadsheet lives at block 22,107, and so on. A **file system** imposes structure on this flat space, providing the abstractions you take for granted: named files, directories, permissions, and the ability to grow or shrink files without manually tracking blocks.

The key data structure in Unix-style file systems is the **inode** (index node). Each file or directory has exactly one inode, which stores all metadata — owner, group, permissions, timestamps, file size — and, crucially, pointers to the data blocks containing the file's content. For small files, the inode's direct pointers (typically 12-15 of them) point straight to data blocks. For larger files, the inode uses **indirect pointers**: a single-indirect pointer points to a block full of block pointers, a double-indirect pointer points to a block of single-indirect pointers, and a triple-indirect pointer adds yet another level. This hierarchical pointer structure allows a fixed-size inode to address files ranging from a few kilobytes to several terabytes.

A **directory** is itself a file whose data blocks contain a table mapping names to inode numbers. When you type `ls /home/user/report.txt`, the file system reads the root directory's inode, finds the data blocks listing its entries, locates "home" and its inode number, reads that inode to find its data blocks, locates "user," and so on until it resolves "report.txt" to an inode number. This is **path resolution**, and it explains why deeply nested paths are slightly slower to access — each component requires an inode lookup and a directory scan.

The file system also needs bookkeeping structures to manage free space. A **superblock** stores global metadata: total size, block size, number of inodes, pointers to free-space management structures. **Allocation bitmaps** — one for data blocks and one for inodes — use one bit per block or inode to track whether it is free or in use. Allocating a new block means scanning the bitmap for a 0 bit, setting it to 1, and returning that block number. This layout — superblock, inode table, bitmaps, data blocks — is replicated across **block groups** in modern file systems like ext4, so that related data (a file's inode and its data blocks) tends to be physically close on disk, reducing seek time and improving performance.
