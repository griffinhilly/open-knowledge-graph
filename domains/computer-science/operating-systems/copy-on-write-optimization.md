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
status: validated
---

# Copy-on-Write Memory Optimization

## Core Idea
Copy-on-write defers copying memory pages until a process modifies them, reducing overhead when child processes immediately exec(). When fork() creates a child, both parent and child share physical pages; modification triggers a page fault and copy. CoW is essential for efficient process creation in modern operating systems and reduces memory waste.

## Questions

```yaml
- question: "A process with 200MB of memory calls fork(), and the child immediately calls exec(). With copy-on-write enabled, approximately how much memory is actually copied during this sequence?"
  type: multiple-choice
  options:
    - "200MB — all of the parent's address space must be duplicated at fork() time"
    - "100MB — only writable pages are copied; code pages are shared"
    - "A few kilobytes — only the page tables are duplicated; data pages are never written before exec() replaces them"
    - "Nothing — exec() makes any memory copying completely unnecessary"
  answer: 2
  explanation: "With CoW, fork() copies only the page tables (a few kilobytes), not the data they point to. All physical pages are shared and marked read-only. The child then calls exec(), which replaces the entire address space before any write occurs — so no page faults are triggered and no data pages are ever copied. Option D is close but wrong: the page tables themselves do get copied. Option A describes behavior without CoW."

- question: "After fork() with copy-on-write, a page is marked read-only in both the parent and child page tables. The parent then writes to that page. What happens next?"
  type: multiple-choice
  options:
    - "The write is silently ignored to preserve the shared copy"
    - "A segmentation fault is raised because the page is read-only"
    - "The OS copies the page for the parent, updates the parent's page table to point to the new copy with write permission, and the child keeps the original"
    - "The OS copies the page for the child, and both parent and child receive new independent copies"
  answer: 2
  explanation: "The write triggers a page fault — but the OS recognizes it as a CoW fault, not a genuine protection violation. It allocates a new physical frame, copies the shared page's contents into it, updates the *writing* process's page table entry to point to the new copy with write permission, and resumes execution. The other process keeps the original page unchanged. Only the one page is copied, not the entire address space."

- question: "With copy-on-write, parent and child processes share physical memory pages until one of them reads those pages."
  type: true-false
  answer: false
  explanation: "Sharing continues through reads — reads are permitted on the shared read-only pages and generate no page fault. Sharing ends only when one process *writes* to a shared page, triggering the CoW page fault and copy. This is critical to why CoW is efficient: most pages in a fork()/exec() pattern are never written at all, so they are shared indefinitely and never copied."

- question: "Copy-on-write relies on the page fault mechanism to defer copying until a write actually occurs."
  type: true-false
  answer: true
  explanation: "CoW is implemented by marking shared pages read-only in both page tables. When a write occurs, the CPU cannot complete it — the page-protection hardware raises a fault. The OS fault handler intercepts this, recognizes the CoW flag on the page table entry, performs the copy, upgrades permissions, and resumes. Without page faults as the interception mechanism, the OS would have no way to lazily defer the copy."

- question: "Explain why copy-on-write makes fork() followed immediately by exec() nearly free in terms of memory copying."
  type: short-answer
  answer: "fork() with CoW duplicates only the page tables, not the physical pages. All pages are marked read-only and shared. exec() then replaces the child's entire address space with a new program before the child ever writes to any shared page. Since no write occurs, no CoW page fault fires, and no data pages are ever copied. The cost of the fork()/exec() sequence is proportional to page table size — a few kilobytes — not the process's data size."
  explanation: "The key insight is that CoW defers the cost to the moment it's actually needed. For the fork()/exec() pattern, that moment never arrives. Even when fork() is used without exec(), most pages (code segments, shared libraries, read-only data) are never written by either process, so they remain shared. In practice, only the small number of modified data pages ever incur the copy cost — typically a tiny fraction of total address space."
```

## Explainer

From your study of demand paging, you know that the OS can intercept memory accesses through page faults and respond by loading pages on demand rather than upfront. **Copy-on-write** (CoW) applies the same principle to a different problem: when fork() creates a child process, must the OS immediately duplicate every page of the parent's address space? The answer is no — and avoiding that copy makes process creation dramatically faster.

Consider what happens without CoW. A process with 500MB of memory calls fork(). The OS must allocate 500MB of new physical memory and copy every byte, even though the child process will likely call exec() within microseconds, replacing all that memory with a new program. This is an enormous waste of time and memory. With CoW, fork() does no copying at all. Instead, the OS points the child's page table entries at the same physical frames the parent uses and marks every shared page as **read-only** in both page tables. The two processes share all their memory, and neither knows it.

The deferred copy happens through the page fault mechanism you already understand. When either process — parent or child — tries to **write** to a shared page, the CPU triggers a page fault because the page is marked read-only. The OS page fault handler recognizes this as a CoW fault (not a genuine protection violation), allocates a new physical frame, copies the contents of the shared page into it, updates the writing process's page table to point to the new copy with write permissions, and resumes execution. The other process keeps the original page. From this point forward, the two processes have independent copies of that one page — but only that page. All unmodified pages remain shared.

This optimization is particularly powerful because of how fork() is typically used. The overwhelmingly common pattern is fork() followed immediately by exec(), which replaces the child's entire address space with a new program. With CoW, this pattern touches zero data pages — the child never writes to the parent's memory, so no copies ever occur. Even when fork() is used without exec(), most pages are read-only code and shared libraries that neither process will modify. In practice, CoW means a fork() that would have copied hundreds of megabytes instead copies only the page tables themselves — a few kilobytes — and defers the rest to the rare moments when it is actually needed.
