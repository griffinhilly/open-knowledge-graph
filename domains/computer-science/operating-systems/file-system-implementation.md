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

## Questions

```yaml
- question: "You create two hard links — 'report.pdf' and 'final.pdf' — pointing to the same file. You then delete 'report.pdf.' What happens to the file data?"
  type: multiple-choice
  options:
    - "The file data is immediately deleted when the first link is removed"
    - "The file data is preserved because 'final.pdf' has its own independent copy of the data"
    - "The file data is preserved because 'final.pdf' still references the same inode, and the inode's link count is now 1"
    - "The file data becomes inaccessible but remains on disk until the next garbage collection cycle"
  answer: 2
  explanation: "Hard links work because filenames and file data are separate. Both 'report.pdf' and 'final.pdf' are directory entries pointing to the same inode. The inode maintains a link count. Deleting 'report.pdf' decrements the link count to 1 — the inode and data blocks are only freed when the link count reaches 0. 'final.pdf' still points to the same inode, so the data is fully intact and accessible. This is only possible because the inode stores everything EXCEPT the filename."

- question: "Which file allocation method best supports efficient random access to an arbitrary byte within a large file?"
  type: multiple-choice
  options:
    - "Linked allocation — each block can be placed anywhere, reducing seek time"
    - "Contiguous allocation — the block containing any byte can be computed directly from the byte offset"
    - "FAT (File Allocation Table) — the allocation table is cached in memory, making traversal fast"
    - "Linked allocation with doubly-linked pointers — backward traversal halves average seek time"
  answer: 1
  explanation: "Contiguous allocation allows direct computation: byte N is at disk block (start_block + N/block_size). No traversal is needed — it's O(1). Linked allocation and FAT require traversing a chain from the beginning to reach block k, taking O(k) time. Indexed allocation (inodes) is also efficient for random access (follow one or two levels of indirect pointers), but contiguous allocation is the simplest and fastest. Linked allocation's advantage is dynamic growth and no external fragmentation, not random access speed."

- question: "In a Unix file system, the inode stores the file's permissions, owner, timestamps, size, and pointers to data blocks — but NOT the filename."
  type: true-false
  answer: true
  explanation: "The separation of filenames from inodes is a fundamental Unix design decision. Filenames live in directory entries, which are themselves files mapping names to inode numbers. This separation is what makes hard links possible: multiple directory entries in different locations can all point to the same inode, sharing a single file's data. If the filename were stored in the inode, a file could only have one name."

- question: "A disk showing file system fragmentation — where file blocks are scattered non-contiguously — means the storage device is nearly full."
  type: true-false
  answer: false
  explanation: "Fragmentation and fullness are independent. A disk with 90% free space can be heavily fragmented if files have been created and deleted repeatedly, leaving scattered free blocks too small for new files. Conversely, a nearly full disk might have its remaining files stored contiguously. Fragmentation is a problem of free-space distribution and allocation method, not of total available space."

- question: "Explain why hard links are possible in Unix file systems. What does their existence reveal about the relationship between filenames and file data?"
  type: short-answer
  answer: "Hard links are possible because filenames and file data are stored separately. File data is managed by an inode (index node), which contains metadata and pointers to data blocks. Filenames exist only in directory entries, which map a name string to an inode number. Multiple directory entries can reference the same inode number — these are hard links. This reveals that a 'file name' is not an intrinsic property of the data; it's just a label in a directory that happens to point to an inode."
  explanation: "The inode-directory separation is one of the most elegant design decisions in Unix. It means 'a file' is really the inode, not the name. Any number of names can refer to the same inode. The inode is only reclaimed when its link count drops to zero (all names removed) AND no process has it open. This design also explains why moving a file within the same file system is fast — it just updates directory entries, not data blocks."
```

## Explainer

From file system concepts, you know that files are named collections of data and that directories organize them into hierarchies. But the file system must solve a concrete engineering problem: a file is a logical sequence of bytes, while a disk is a flat array of fixed-size blocks (typically 4KB). **File system implementation** is the layer that maps between these two views — deciding which disk blocks belong to which file and how to find them efficiently.

The simplest approach is **contiguous allocation**: store each file in a consecutive run of disk blocks. File "report.pdf" might occupy blocks 100–124. This is fast for sequential reads (the disk head never moves) and trivially supports random access (byte offset N is at block start + N/block_size). But it has a fatal flaw: external fragmentation. As files are created and deleted, the disk becomes a patchwork of free and occupied regions, and eventually there is no contiguous gap large enough for a new file even though plenty of total space exists. This is the same fragmentation problem you may recognize from memory management.

**Linked allocation** solves fragmentation by letting each file scatter its blocks anywhere on disk. Each block contains a pointer to the next block in the file, forming a linked list. Files can grow dynamically and never suffer external fragmentation. The cost is terrible random access — to read the 1000th block, you must follow 999 pointers sequentially. **FAT** (File Allocation Table) is a practical refinement: instead of embedding pointers in data blocks, it stores all the next-block pointers in a separate table in a known disk location. This lets the OS traverse the chain in memory rather than on disk, but computing a file's size still requires walking the entire chain.

**Indexed allocation** — the approach used by Unix/Linux file systems — gives each file an **inode** (index node) that contains an array of pointers to the file's data blocks. For small files, a dozen or so **direct pointers** in the inode point straight to data blocks. For larger files, one pointer leads to a **singly indirect block** — a block full of pointers to data blocks. For very large files, **doubly** and **triply indirect blocks** add further levels of indirection. This structure supports both fast random access (compute which pointer level to traverse) and efficient growth (allocate new blocks and add pointers). Critically, the inode stores all metadata — permissions, timestamps, owner, size — but *not* the filename. Filenames live in directory entries, which are themselves just files mapping names to inode numbers. This separation is why hard links work: multiple directory entries can point to the same inode, sharing a single underlying file.
