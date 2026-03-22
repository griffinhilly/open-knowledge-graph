---
id: io-buffering-and-kernel-buffers
title: I/O Buffering and Kernel Buffer Caches
domain: computer-science
course: operating-systems
prerequisites:
- id: io-systems-overview
  type: hard
- id: cache-design-principles
  type: soft
tags:
- io
- buffering
- cache
stage: formal-systems
status: draft
---

# I/O Buffering and Kernel Buffer Caches

## Core Idea
The kernel maintains buffer caches between processes and storage devices to reduce I/O latency and optimize bandwidth utilization. Write-back caching defers writes to disk; read caching avoids repeated disk accesses for the same data. Buffer cache management, including dirty buffer flushing and page replacement policies, is critical to both performance and data durability guarantees.

## Questions

```yaml
- question: "A process calls write() to save a file and the call returns successfully. Two seconds later, the system crashes unexpectedly. Will the data be on disk when the system restarts?"
  type: multiple-choice
  options:
    - "Yes — write() returning means the data was committed to disk"
    - "No — with write-back caching, write() only puts data in the kernel buffer cache; it is lost if the buffer was never flushed to disk"
    - "Yes — the kernel always flushes dirty buffers before returning from write()"
    - "No — write() never guarantees durability regardless of caching policy"
  answer: 1
  explanation: "This is the key durability trap of write-back caching. write() returning successfully means the kernel accepted the data into its buffer cache and marked the buffer dirty. The actual disk write happens later, asynchronously, by background flush threads. If the system crashes before the flush, the data in dirty buffers is gone. To guarantee durability, an application must call fsync() after writing, which forces the kernel to flush dirty buffers to disk before returning."

- question: "What does it mean for a kernel buffer to be 'dirty'?"
  type: multiple-choice
  options:
    - "The buffer contains data that has been corrupted or is no longer valid"
    - "The buffer holds data that has been written by a process but not yet flushed to the underlying storage device"
    - "The buffer was recently evicted and its data is now only on disk, not in memory"
    - "The buffer is currently being read from disk into the cache"
  answer: 1
  explanation: "A dirty buffer is one whose in-memory contents have been modified (written to) but whose counterpart on disk has not yet been updated to match. The kernel marks buffers dirty on write-back to track which blocks need to be flushed to disk. Clean buffers, by contrast, exactly mirror what is on disk and can be evicted without any disk write. This dirty/clean distinction is the core bookkeeping mechanism of write-back caching."

- question: "If a file's blocks are in the kernel buffer cache, a process's read() call for that file will not generate any disk I/O."
  type: true-false
  answer: true
  explanation: "This is exactly the purpose of the buffer cache. On a cache hit, the kernel copies the requested data from main memory (the cache) to the process's address space — no disk access occurs. This is why programs that repeatedly read the same files (config files, shared libraries) do not produce repeated disk I/O. The first read (a cache miss) fetches from disk; all subsequent reads hit the cache and are served at memory speed."

- question: "Write-back caching provides stronger data durability guarantees than write-through caching because the kernel takes responsibility for managing the writes."
  type: true-false
  answer: false
  explanation: "Write-back offers worse durability than write-through, not better. Write-through writes data to both cache and disk immediately — every write blocks until the disk confirms, so if the system crashes, no acknowledged write is lost. Write-back defers disk writes, so data in dirty buffers can be lost on a crash. Write-back is dramatically faster (the application isn't waiting for disk), but that performance comes at the cost of a durability window. Databases use fsync() precisely to close this window for critical commits."

- question: "Why do database systems typically call fsync() after committing a transaction, even though it significantly slows write throughput?"
  type: short-answer
  answer: "fsync() forces the kernel to flush all dirty buffers for the file to disk before returning, guaranteeing the data survives a subsequent crash. Without it, a committed transaction might exist only in the kernel buffer cache and be lost if the system crashes before the background flush thread runs."
  explanation: "Databases must guarantee durability — the 'D' in ACID. A transaction marked committed must survive crashes. With write-back caching, write() returning just means data reached the kernel cache; it could still be lost. fsync() closes this gap by synchronously flushing dirty buffers. The throughput cost is real, which is why databases batch multiple transactions and call fsync() once per batch (group commit), rather than once per transaction."
```

## Explainer

You know from I/O systems that storage devices are dramatically slower than the CPU and main memory — a disk read takes milliseconds while a memory access takes nanoseconds, a gap of roughly six orders of magnitude. From cache design principles, you know the strategy: put a faster, smaller storage layer in front of a slower, larger one and exploit temporal and spatial locality. The kernel's **buffer cache** (also called the page cache in modern Linux) applies this exact strategy to disk I/O, sitting in main memory between user processes and the storage device.

When a process calls `read()`, the kernel first checks whether the requested disk blocks are already in the buffer cache. If they are (a cache hit), the data is copied from memory to the process — no disk access needed. If not (a cache miss), the kernel reads the block from disk into the buffer cache, then copies it to the process. Subsequent reads of the same block by any process hit the cache. The kernel also performs **read-ahead**: when it detects sequential access patterns, it prefetches upcoming blocks into the cache before they are requested, turning what would be many small random reads into efficient sequential I/O.

Writing has two strategies with very different trade-offs. **Write-through** writes data to both the cache and the disk immediately — safe but slow, since every write blocks until the disk confirms. **Write-back** (the default in most operating systems) writes only to the cache and marks the buffer as **dirty**, deferring the actual disk write to a later time. This is dramatically faster for the application — `write()` returns almost immediately — but creates a durability risk: if the system crashes before dirty buffers are flushed to disk, that data is lost. The kernel mitigates this by periodically flushing dirty buffers (Linux's `pdflush`/`writeback` threads run every few seconds) and by honoring explicit `fsync()` calls from applications that need durability guarantees, such as databases.

Managing the buffer cache means deciding which blocks to keep and which to evict when memory is full. The kernel uses page replacement policies (like LRU approximations) to evict the least-recently-used cached blocks, making room for new ones. This is the same fundamental trade-off you studied in cache design: cache size versus hit rate, write-back versus write-through, and eviction policy. The buffer cache is why a program that reads the same configuration file a hundred times does not generate a hundred disk reads, and why a burst of small writes to a log file does not produce a burst of disk I/O — the kernel absorbs the writes into memory and flushes them efficiently in larger batches.
