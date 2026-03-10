---
id: virtual-memory-basics
title: Virtual Memory and Paging
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-hierarchy-overview
  type: hard
- id: memory-organization
  type: hard
- id: cache-replacement-policies
  type: soft
tags:
- virtual-memory
- paging
- page-table
- TLB
- address-translation
stage: formal-systems
status: draft
---

# Virtual Memory and Paging

## Core Idea
Virtual memory gives each process the illusion of a private, contiguous address space larger than physical RAM. The virtual address space is divided into fixed-size pages; corresponding physical memory units are called frames. A page table maintained by the OS and hardware maps virtual page numbers to physical frame numbers. The Translation Lookaside Buffer (TLB) caches recent page table entries to speed up address translation. Pages not in physical memory are stored on disk and fetched on a page fault.

## How It's Best Learned
Trace the full address translation path: virtual address → TLB lookup or page table walk → physical address → cache lookup → memory. Simulate page replacement policies on a small address sequence. Understand the page fault handler's role in the OS.

## Common Misconceptions
- Virtual memory is not just using disk as RAM; it also provides memory isolation between processes and enables memory-mapped files.
- A TLB miss does not always cause a page fault; the page may already be in physical memory and the TLB simply needs to be refilled from the page table.
