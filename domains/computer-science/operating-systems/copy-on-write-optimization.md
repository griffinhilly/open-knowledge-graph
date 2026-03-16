---
id: copy-on-write-optimization
title: Copy-on-Write Memory Optimization
domain: computer-science
course: operating-systems
prerequisites:
- id: demand-paging-and-page-faults
  type: hard
- id: process-creation-fork-exec
  type: soft
tags:
- optimization
- paging
- fork
stage: formal-systems
status: draft
---

# Copy-on-Write Memory Optimization

## Core Idea
Copy-on-write defers copying memory pages until a process modifies them, reducing overhead when child processes immediately exec(). When fork() creates a child, both parent and child share physical pages; modification triggers a page fault and copy. CoW is essential for efficient process creation in modern operating systems and reduces memory waste.

## Explainer

From your study of demand paging, you know that the OS can intercept memory accesses through page faults and respond by loading pages on demand rather than upfront. **Copy-on-write** (CoW) applies the same principle to a different problem: when fork() creates a child process, must the OS immediately duplicate every page of the parent's address space? The answer is no — and avoiding that copy makes process creation dramatically faster.

Consider what happens without CoW. A process with 500MB of memory calls fork(). The OS must allocate 500MB of new physical memory and copy every byte, even though the child process will likely call exec() within microseconds, replacing all that memory with a new program. This is an enormous waste of time and memory. With CoW, fork() does no copying at all. Instead, the OS points the child's page table entries at the same physical frames the parent uses and marks every shared page as **read-only** in both page tables. The two processes share all their memory, and neither knows it.

The deferred copy happens through the page fault mechanism you already understand. When either process — parent or child — tries to **write** to a shared page, the CPU triggers a page fault because the page is marked read-only. The OS page fault handler recognizes this as a CoW fault (not a genuine protection violation), allocates a new physical frame, copies the contents of the shared page into it, updates the writing process's page table to point to the new copy with write permissions, and resumes execution. The other process keeps the original page. From this point forward, the two processes have independent copies of that one page — but only that page. All unmodified pages remain shared.

This optimization is particularly powerful because of how fork() is typically used. The overwhelmingly common pattern is fork() followed immediately by exec(), which replaces the child's entire address space with a new program. With CoW, this pattern touches zero data pages — the child never writes to the parent's memory, so no copies ever occur. Even when fork() is used without exec(), most pages are read-only code and shared libraries that neither process will modify. In practice, CoW means a fork() that would have copied hundreds of megabytes instead copies only the page tables themselves — a few kilobytes — and defers the rest to the rare moments when it is actually needed.
