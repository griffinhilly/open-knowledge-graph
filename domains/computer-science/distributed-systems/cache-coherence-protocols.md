---
id: cache-coherence-protocols
title: Cache Coherence Protocols and Memory Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
- id: synchronization-problem
  type: hard
tags:
- caching
- consistency
- coherence
stage: advanced
status: validated
---

# Cache Coherence Protocols and Memory Consistency

## Core Idea
Cache coherence protocols maintain consistency between multiple caches in a system. MESI (Modified, Exclusive, Shared, Invalid) is a common protocol that tracks cache line states and coordinates through snooping or directory-based schemes. Correct coherence is essential to prevent processes from seeing inconsistent data when multiple CPUs or nodes have copies of the same memory location.

## Questions

```yaml
- question: "Processor A and Processor B each hold a Shared copy of cache line X. Processor A writes a new value to X. What does the MESI protocol dictate?"
  type: multiple-choice
  options:
    - "Both processors update their copies simultaneously via a broadcast write"
    - "Processor A's copy transitions to Modified; an invalidation message causes Processor B's copy to transition to Invalid"
    - "Processor A writes through to main memory; Processor B's copy remains Shared but stale"
    - "The write is blocked until Processor B releases its Shared copy"
  answer: 1
  explanation: "Under MESI write-invalidate, when a processor writes to a Shared line, it first acquires exclusive ownership by sending an invalidation to all other caches holding the line. Processor B's copy transitions to Invalid (unusable), and Processor A's copy transitions to Modified (the only valid, changed copy, with main memory now stale). Processor B's next read will cause a cache miss and require fetching the updated value. Write-broadcast (option A) is an alternative coherence strategy but not what MESI uses."

- question: "Why do directory-based cache coherence protocols scale better than bus-snooping protocols for systems with many processors?"
  type: multiple-choice
  options:
    - "Directory protocols are simpler to implement because they eliminate the need for state tracking"
    - "Snooping requires every cache to monitor every bus transaction, causing bus bandwidth to become the bottleneck; directories send targeted messages only to caches holding the relevant line"
    - "Directory protocols allow caches to hold multiple Modified copies simultaneously"
    - "Snooping protocols cannot handle the Invalid state, which is required for correctness"
  answer: 1
  explanation: "The fundamental scalability problem with snooping is that every coherence transaction must be visible to every cache — the shared bus becomes a bandwidth bottleneck, and each cache must inspect every transaction even if it has no copy of that line. Directory protocols track which caches hold each memory block; when a write occurs, targeted invalidation messages go only to those specific caches. This reduces both bus traffic and per-cache processing, enabling scaling to hundreds of processors. The tradeoff is added latency for the directory lookup itself."

- question: "In the MESI protocol, a cache line in the Modified state has an up-to-date copy in main memory."
  type: true-false
  answer: false
  explanation: "Modified means the opposite: this cache holds the ONLY valid copy, and main memory is STALE. The cache has written to the line without immediately updating main memory (write-back caching). When another processor requests that line, the Modified cache must write its copy back to main memory (or directly supply the data to the requesting cache) before the state changes. This is why the Modified state is significant — it carries a dirty-bit obligation to eventually commit the change."

- question: "False sharing occurs when two processors each write to different variables that happen to reside on the same cache line, causing cache invalidations that are correct but unnecessarily frequent."
  type: true-false
  answer: true
  explanation: "False sharing is a real performance pathology. Two processors writing to independent variables X and Y experience cache invalidations as if they were writing to the same variable — because the coherence protocol operates at the granularity of cache lines, not individual bytes. Each write by Processor A invalidates Processor B's copy of the entire line (even though B's variable Y hasn't changed), forcing B to re-fetch the line on its next access. The data remains correct, but performance degrades dramatically. The fix is to pad variables so they occupy separate cache lines."

- question: "Explain why cache coherence protocols are necessary even when application code uses locks and synchronization primitives for mutual exclusion."
  type: short-answer
  answer: "Locks prevent concurrent access to shared data by ensuring only one thread holds the lock at a time — but they don't guarantee that a thread sees the most recent value of the data after acquiring the lock. Without cache coherence, a thread could acquire a lock and then read a stale value from its local cache that was updated by another processor while that processor held the lock. Coherence ensures that when a thread reads an address, it sees the most recent write by any processor, making the lock's critical section actually operate on current data. Synchronization and coherence are complementary: synchronization controls when threads can access shared data; coherence ensures the data they see is consistent."
  explanation: "This distinction between safety (locks) and visibility (coherence) is subtle but important. A lock without coherence is like a traffic light without mirrors — you know you have the right of way, but you can't see if something from a different direction is already in the intersection. Modern hardware provides coherence automatically, but in distributed systems (multi-machine), the programmer is responsible for both."
```

## Questions

```yaml
- question: "Under the MESI protocol, Processor A writes a new value to a cache line currently in the Shared state (held by both A and B). What state does Processor B's copy transition to?"
  type: multiple-choice
  options:
    - "Shared — B's copy is automatically updated to the new value via broadcast"
    - "Invalid — B's copy is marked unusable; B must fetch the updated value from A or memory on next access"
    - "Modified — B holds the updated copy since A's write propagated to it"
    - "Exclusive — B becomes the sole holder once A finishes writing"
  answer: 1
  explanation: "MESI uses an invalidation protocol, not an update protocol. When A writes to a Shared line, it sends an *invalidation* message to all other caches holding that line — not the new value. B's copy transitions to Invalid. On B's next read, it must fetch the current value (which A holds in Modified state). The tempting wrong answer is A: a write-update protocol would broadcast the new value, but MESI invalidates instead, deferring the transfer until B actually needs the data."

- question: "Two threads each modify a different variable, X and Y, that happen to be allocated on the same 64-byte cache line. On a multi-core machine, this causes severe performance degradation. What is this phenomenon called, and why does it occur?"
  type: multiple-choice
  options:
    - "True sharing — X and Y are logically dependent, causing serialized access"
    - "False sharing — the coherence protocol treats the entire cache line as the unit of coherence, so writes to either variable invalidate the other processor's copy of the whole line"
    - "Cache thrashing — the cache is too small to hold both variables simultaneously"
    - "Directory overflow — the directory-based protocol cannot track two variables in the same entry"
  answer: 1
  explanation: "False sharing is the key pathology that demonstrates why coherence operates on cache lines (typically 64 bytes), not individual variables. Even though X and Y are logically independent and never accessed together, the protocol sees one cache line. Every time thread 1 writes X, it invalidates thread 2's cache line (which also contains Y), and vice versa. The result is constant cache misses despite no logical data sharing. The fix is to pad the data structures so X and Y reside on different cache lines."

- question: "Cache coherence and memory consistency are the same concept: both describe what value a processor reads from a shared memory location."
  type: true-false
  answer: false
  explanation: "These are distinct but complementary concepts. Cache *coherence* is a hardware-level guarantee about a *single memory location*: eventually, all processors agree on its current value (stale copies are invalidated). Memory *consistency* is a higher-level contract about *multiple memory locations*: it specifies what orderings of reads and writes across *different* locations are visible to programs. For example, sequential consistency says each processor sees all writes in a globally consistent order; relaxed models allow reordering for performance. Coherence is the mechanism; consistency is the programmer-facing specification."

- question: "In a directory-based coherence protocol, a processor that wants to write to a cache line must receive explicit permission from the directory, which then invalidates all other cached copies before granting the write."
  type: true-false
  answer: true
  explanation: "This is exactly how directory-based protocols work. Unlike snooping protocols (where every cache watches a shared bus), the directory maintains a table of which caches hold each line. When a processor requests write permission, the directory sends targeted invalidation messages to all sharers listed for that line, waits for acknowledgments, then grants exclusive write access. This avoids the broadcast overhead of snooping and scales to larger systems, but adds latency for the directory lookup and invalidation round-trip."

- question: "What is the difference between cache coherence and a memory consistency model, and why does a system need both?"
  type: short-answer
  answer: "Cache coherence ensures that all processors eventually agree on the value of a *single* memory location — stale copies are invalidated so no processor reads outdated data. A memory consistency model specifies the ordering guarantees for reads and writes across *multiple* locations as seen by concurrent threads (e.g., whether a write to X is visible before a subsequent write to Y). You need both: coherence prevents reading stale data for any one variable, while the consistency model tells programmers what ordering assumptions they can safely rely on when reasoning about concurrent programs. Without coherence, programs see phantom old values; without a consistency model, programs have no contract for when writes become visible."
  explanation: "The key insight is the different scopes: coherence is about agreement on one location over time; consistency is about ordering across multiple locations simultaneously. Many bugs in concurrent programs stem from confusing these two levels or assuming stronger guarantees (like sequential consistency) when the hardware provides a weaker model (like x86's TSO)."
```

## Explainer

From your work with consistency models and the synchronization problem, you know that when multiple processors or nodes share data, concurrent access without coordination leads to inconsistent views. **Cache coherence** is the specific instance of this problem that arises when multiple processors each maintain their own local cache of shared memory. If processor A writes a new value to address X in its cache, processor B's cache still holds the stale old value — and without a coherence protocol, B has no way of knowing its copy is outdated.

The **MESI protocol** solves this by assigning each cache line one of four states. **Modified** means this cache holds the only valid copy and it has been changed — main memory is stale. **Exclusive** means this cache holds the only copy and it matches main memory — no other cache has it. **Shared** means multiple caches hold this line and all copies match main memory. **Invalid** means this cache line is not usable — it has been invalidated because another processor modified the data. Every read and write triggers state transitions: when processor A writes to a Shared line, the protocol sends an invalidation message to all other caches holding that line, transitioning their copies to Invalid and A's copy to Modified.

There are two main coordination mechanisms. In **snooping protocols**, every cache watches (snoops on) a shared bus and reacts when it sees transactions involving addresses it holds. This works well for small numbers of processors sharing a bus, but does not scale — every cache must see every transaction. In **directory-based protocols**, a central directory tracks which caches hold copies of each memory block. When a write occurs, the directory sends targeted invalidation messages only to caches that actually hold the line, avoiding broadcast overhead. This scales to larger systems but adds latency for the directory lookup.

Understanding cache coherence bridges the gap between the abstract consistency models you have studied and the physical reality of how hardware enforces them. The consistency model tells you what ordering guarantees the system provides to programmers; the coherence protocol is the mechanism that delivers those guarantees at the hardware level. When coherence works correctly, programmers can reason about shared memory without thinking about caches at all. When it breaks down — or when the performance cost of maintaining coherence becomes the bottleneck — it explains phenomena like false sharing (two unrelated variables on the same cache line causing constant invalidations) and motivates the design of systems that minimize shared mutable state entirely.
