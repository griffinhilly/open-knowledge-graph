---
id: memory-mapped-files-io
title: Memory-Mapped Files and I/O
domain: computer-science
course: operating-systems
prerequisites:
- id: virtual-memory-management
  type: hard
- id: file-system-implementation
  type: soft
builds-toward:
- io-buffering-and-kernel-buffers
tags:
- memory
- files
- io
stage: formal-systems
status: draft
---

# Memory-Mapped Files and I/O

## Core Idea
Memory-mapped files allow a file to be accessed as a region of memory, enabling efficient large-file operations and inter-process data sharing. Reads and writes to the mapped region are transparently managed by the kernel, with the page cache handling I/O. This provides an alternative to explicit read()/write() calls and enables zero-copy data transfer between processes.

## Questions

```yaml
- question: "A process calls mmap() to map a large file and then reads the first byte of the mapped region for the first time. What happens?"
  type: multiple-choice
  options:
    - "The kernel immediately reads the entire file into physical memory before returning from mmap()"
    - "A page fault occurs, the kernel reads the corresponding file page into a physical frame, updates the page table, and returns control to the process"
    - "The operating system copies the data into a user-space buffer, just like read() would"
    - "Nothing happens until the process calls msync() to load the data"
  answer: 1
  explanation: "mmap() sets up page table entries for the address range but loads nothing. The first access triggers a page fault — the CPU sees a valid but not-yet-present mapping. The kernel's fault handler recognizes the backing file, reads the relevant page from disk into the page cache (a physical frame), updates the page table to point to it, and resumes the process transparently. This lazy loading is what makes memory-mapped I/O efficient: pages are only fetched when accessed, not pre-loaded speculatively."

- question: "Two processes memory-map the same file with MAP_SHARED. Process A writes to the mapped region. When does Process B see the change?"
  type: multiple-choice
  options:
    - "Never — each process gets its own private copy of the file data when it calls mmap()"
    - "Only after Process A calls msync() and Process B calls munmap() and remaps the file"
    - "Immediately, because both processes share the same physical pages in the page cache"
    - "After the kernel's writeback daemon flushes the changes to disk and Process B re-reads from disk"
  answer: 2
  explanation: "MAP_SHARED means both processes map to the same physical pages in the page cache. A write by Process A modifies those pages directly, and since Process B's virtual addresses map to the same physical frames, it sees the change immediately — no IPC mechanism, no disk roundtrip, no explicit synchronization needed. This shared-page-cache mechanism is why memory-mapped files are used for high-performance inter-process communication in databases and servers."

- question: "Memory-mapped file I/O can achieve zero-copy reads because the process accesses file data directly in the page cache, avoiding an extra copy into a separate user-space buffer."
  type: true-false
  answer: true
  explanation: "With the traditional read() system call, the kernel reads file data from disk into a kernel buffer, then copies it into the user-space buffer provided by the application — two copies total. With mmap(), the process's virtual page is mapped directly to the physical frame in the page cache. The process reads from that frame without any intermediate copy. For large files or databases performing random index lookups, eliminating this extra copy produces a measurable performance improvement."

- question: "Memory-mapped I/O is always faster than read()/write() and should be preferred for all file access patterns."
  type: true-false
  answer: false
  explanation: "For sequential reads of small files, read()/write() can be faster or comparable — the system call overhead is negligible, and the kernel may apply read-ahead buffering more aggressively. Memory mapping also consumes virtual address space, complicates error handling (disk errors arrive as SIGBUS signals instead of error codes), and provides weaker durability guarantees (dirty pages may not be flushed before a crash without explicit msync()). mmap is best suited for large files, random access patterns, or shared-memory IPC — not universally superior."

- question: "Explain how the kernel handles a page fault when a process accesses an address in a memory-mapped file region that hasn't been loaded yet, and why this mechanism is preferable to loading the entire file up front."
  type: short-answer
  answer: "When a process accesses an unmapped address in the mmap'd region, the CPU raises a page fault. The kernel's fault handler checks the page table entry, recognizes it is backed by a file (not anonymous memory), reads the corresponding file block into a page cache frame, updates the page table to map the virtual page to that frame, and resumes the faulting instruction. Loading on demand is preferable because large files are rarely accessed in their entirety; only fetching pages that are actually touched avoids loading gigabytes into RAM for a query that touches a few blocks."
  explanation: "The lazy-loading behavior also enables efficient random access: processes can 'open' a multi-gigabyte file via mmap and access any offset directly without first seeking and reading sequentially. The kernel manages the working set automatically — frequently accessed pages stay in the page cache; rarely accessed ones are evicted. This is exactly why database engines use mmap for index structures: they can navigate a large B-tree by following pointers, and the OS transparently loads only the pages traversed."
```

## Explainer

From your understanding of virtual memory, you know that a process's address space is a collection of virtual pages mapped to physical frames through page tables. Normally, these pages back anonymous memory — stack, heap, and data segments that exist only in RAM (and swap). **Memory-mapped files** extend this mechanism: instead of mapping a virtual page to anonymous memory, the OS maps it to a specific region of a file on disk. When the process reads from or writes to that address range, it is transparently reading from or writing to the file.

The mechanics work through the same page fault machinery you already know. When a process calls `mmap()` to map a file, the kernel sets up page table entries for the requested address range but does not immediately load any data. When the process first accesses an address in the mapped region, a page fault occurs. The kernel's fault handler recognizes that this page is backed by a file, reads the corresponding file data into a physical frame (via the **page cache**), and updates the page table. Subsequent accesses to that page hit memory directly with no system call overhead. The kernel flushes modified pages back to disk lazily or when explicitly requested via `msync()`.

This approach has two major advantages over traditional `read()`/`write()` system calls. First, it eliminates a copy: with `read()`, the kernel reads file data into a kernel buffer and then copies it into the user's buffer — two copies total. With memory mapping, the process accesses the page cache directly, achieving **zero-copy** I/O. For large files or random-access patterns (like databases scanning an index), this difference is substantial. Second, memory-mapped files enable **shared memory between processes**. If two processes map the same file with `MAP_SHARED`, they share the same physical pages. A write by one process is visible to the other without any explicit IPC mechanism — the page cache serves as the shared medium. This is how many databases and high-performance servers share data across worker processes.

The tradeoffs are worth understanding. Memory-mapped I/O is not always faster than `read()`/`write()` — for sequential reads of small files, the system call overhead is negligible and the simpler interface may be preferable. Mapped regions consume virtual address space, which matters on 32-bit systems. Error handling is also less intuitive: a disk error during a memory access triggers a `SIGBUS` signal rather than returning an error code, which is harder to handle gracefully. And because the kernel controls when dirty pages are flushed, data can be lost if the system crashes before a writeback. Despite these caveats, memory-mapped files are a foundational technique — they underpin dynamic library loading (shared libraries are memory-mapped into process address spaces), executable loading, and the internals of many database engines.
