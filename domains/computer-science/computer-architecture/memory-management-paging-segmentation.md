---
id: memory-management-paging-segmentation
title: 'Memory Management: Paging and Segmentation'
domain: computer-science
course: computer-architecture
prerequisites:
- id: virtual-memory-basics
  type: hard
- id: memory-array-organization
  type: soft
builds-toward:
- cache-design-principles
- io-architecture-system-integration
tags:
- memory
- paging
- segmentation
- virtual
stage: formal-systems
status: draft
---

# Memory Management: Paging and Segmentation

## Core Idea
Paging divides virtual address space into fixed-size pages mapped to physical frames via a page table; segmentation divides address space into variable-size logical segments. Both separate logical and physical memory, enabling isolation and larger address spaces.

## Explainer

From your study of virtual memory, you know the core motivation: programs should behave as if they have a large, private, contiguous address space, even though physical RAM is limited and shared. The question is how the hardware and operating system collaborate to translate virtual addresses into physical ones. **Paging** and **segmentation** are the two fundamental schemes for this translation, and understanding their tradeoffs explains why modern systems overwhelmingly use paging.

**Paging** divides the virtual address space into fixed-size blocks called **pages** (typically 4 KB) and physical memory into identically sized blocks called **frames**. A **page table** maps each virtual page number to a physical frame number. When the CPU generates a virtual address, the hardware splits it into a page number (upper bits) and an offset within the page (lower bits), looks up the page number in the page table to find the corresponding frame, and concatenates the frame number with the offset to produce the physical address. Because pages and frames are the same fixed size, any page can go into any available frame — there is no external fragmentation. The tradeoff is **internal fragmentation**: the last page of a process may not be fully used, wasting up to one page minus one byte.

**Segmentation** takes a different approach. Instead of uniform blocks, it divides the address space into variable-size **segments** that correspond to logical units of the program — code, stack, heap, data. Each segment has a base address and a length stored in a **segment table**. The hardware checks that the offset within a segment does not exceed its length (providing bounds checking), then adds the offset to the base address. Segmentation maps naturally onto how programmers think about programs, and it provides fine-grained protection — you can mark the code segment as read-only and executable while the data segment is read-write. However, because segments vary in size, allocating and deallocating them creates **external fragmentation**: free memory becomes scattered into small unusable gaps.

Modern architectures like x86-64 effectively use **paging as the primary mechanism** and have largely flattened segmentation into a compatibility feature. The reason is practical: fixed-size pages make allocation simple and predictable, multi-level page tables (and hardware TLBs that cache recent translations) make lookups fast, and the operating system can swap individual pages to disk without worrying about fitting variable-size chunks. Some historical systems combined both — segmented paging, where each segment is itself paged — to get the logical structure of segmentation with the allocation simplicity of paging. Understanding both schemes clarifies why paging won: the engineering cost of managing variable-size memory blocks at hardware speed is simply too high compared to the elegance of uniform pages.
