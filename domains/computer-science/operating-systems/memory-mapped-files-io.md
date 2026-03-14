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
