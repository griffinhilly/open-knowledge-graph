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

## Explainer

From your understanding of virtual memory, you know that a process's address space is a collection of virtual pages mapped to physical frames through page tables. Normally, these pages back anonymous memory — stack, heap, and data segments that exist only in RAM (and swap). **Memory-mapped files** extend this mechanism: instead of mapping a virtual page to anonymous memory, the OS maps it to a specific region of a file on disk. When the process reads from or writes to that address range, it is transparently reading from or writing to the file.

The mechanics work through the same page fault machinery you already know. When a process calls `mmap()` to map a file, the kernel sets up page table entries for the requested address range but does not immediately load any data. When the process first accesses an address in the mapped region, a page fault occurs. The kernel's fault handler recognizes that this page is backed by a file, reads the corresponding file data into a physical frame (via the **page cache**), and updates the page table. Subsequent accesses to that page hit memory directly with no system call overhead. The kernel flushes modified pages back to disk lazily or when explicitly requested via `msync()`.

This approach has two major advantages over traditional `read()`/`write()` system calls. First, it eliminates a copy: with `read()`, the kernel reads file data into a kernel buffer and then copies it into the user's buffer — two copies total. With memory mapping, the process accesses the page cache directly, achieving **zero-copy** I/O. For large files or random-access patterns (like databases scanning an index), this difference is substantial. Second, memory-mapped files enable **shared memory between processes**. If two processes map the same file with `MAP_SHARED`, they share the same physical pages. A write by one process is visible to the other without any explicit IPC mechanism — the page cache serves as the shared medium. This is how many databases and high-performance servers share data across worker processes.

The tradeoffs are worth understanding. Memory-mapped I/O is not always faster than `read()`/`write()` — for sequential reads of small files, the system call overhead is negligible and the simpler interface may be preferable. Mapped regions consume virtual address space, which matters on 32-bit systems. Error handling is also less intuitive: a disk error during a memory access triggers a `SIGBUS` signal rather than returning an error code, which is harder to handle gracefully. And because the kernel controls when dirty pages are flushed, data can be lost if the system crashes before a writeback. Despite these caveats, memory-mapped files are a foundational technique — they underpin dynamic library loading (shared libraries are memory-mapped into process address spaces), executable loading, and the internals of many database engines.
