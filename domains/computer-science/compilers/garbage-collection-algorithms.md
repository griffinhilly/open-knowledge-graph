---
id: garbage-collection-algorithms
title: Garbage Collection Algorithms
domain: computer-science
course: compilers
prerequisites:
- id: runtime-function-calls
  type: hard
- id: memory-management-basics
  type: hard
builds-toward:
- jit-compilation
tags:
- garbage-collection
- memory-management
- runtime-system
stage: advanced
status: draft
---

# Garbage Collection Algorithms

## Core Idea
Garbage collection automatically reclaims memory of unreachable objects, freeing programmers from manual deallocation. Reachability is determined from root references (stack, globals). Common algorithms include mark-and-sweep (mark reachable objects, sweep unreachable), generational (younger objects collected more often), and copying (move live objects to a new space). GC adds overhead but prevents memory leaks.

## Questions

```yaml
- question: "A program creates thousands of short-lived temporary string objects during text processing, discarding most of them within milliseconds. Which garbage collection strategy is best suited to this workload, and why?"
  type: multiple-choice
  options:
    - "Mark-and-sweep, because it handles variable-sized objects cleanly by freeing each one individually."
    - "Generational collection, because most strings will be collected cheaply in frequent nursery passes without ever reaching the older generation."
    - "Reference counting, because each string is freed immediately when its reference count drops to zero."
    - "Mark-and-compact, because the many small freed objects would otherwise cause severe heap fragmentation."
  answer: 1
  explanation: "Generational collection is designed precisely for this pattern. The generational hypothesis states that most objects die young — short-lived temporaries like these strings almost never survive a nursery collection. The nursery is small and collected frequently using copying collection, so the per-collection cost is proportional to the few survivors, not the many dead objects. Reference counting (option C) is superficially appealing but cannot reclaim cycles and incurs per-assignment overhead; it also misses the deeper efficiency gain from batching collections."

- question: "Object A holds a reference to object B, and object B holds a reference back to A. No other live variables reference either A or B. Under which memory management approach will A and B be reclaimed without programmer intervention?"
  type: multiple-choice
  options:
    - "Reference counting, because each object's count drops to zero when the other is freed first."
    - "Reference counting, but only if a separate cycle-detection pass is added."
    - "Any tracing garbage collector (mark-and-sweep, copying, generational), because reachability from roots determines garbage regardless of internal reference cycles."
    - "No automatic strategy can reclaim them; the programmer must break the cycle manually."
  answer: 2
  explanation: "Reference counting fails on cycles: A's count is 1 (B points to it) and B's count is 1 (A points to it), so neither ever reaches zero, and both leak. Tracing collectors (mark-and-sweep, copying, generational) start from the root set — stack variables, globals, registers — and mark everything reachable by following pointer chains. Since no root reaches A or B, neither gets marked and both are collected. Reachability-from-roots is a global property that correctly identifies cyclic garbage; reference counting tracks only local pointer counts."

- question: "Copying collection is inefficient when most objects are short-lived, because it must copy all those short-lived objects before reclaiming their space."
  type: true-false
  answer: false
  explanation: "This is the key misconception. Copying collection only copies LIVE (reachable) objects from fromspace to tospace — dead objects are simply abandoned and their space reclaimed by swapping the roles of the two halves. If most objects are short-lived (the generational hypothesis), very few survive, and copying cost is proportional to survivors, not to all objects. A collection that sees 10,000 allocations but only 100 survivors copies only 100 objects. This is exactly why copying collection is the preferred algorithm for the nursery in generational systems."

- question: "In generational garbage collection, write barriers are needed to track old-to-young references so that nursery collections can find all roots without scanning the entire old generation."
  type: true-false
  answer: true
  explanation: "The nursery root set must include not only stack and global variables but also any pointers from old-generation objects into the nursery — otherwise a live young object pointed to only from old memory would appear unreachable and be incorrectly collected. Since scanning the entire old generation on every nursery collection would defeat its purpose, the runtime uses write barriers: small pieces of code executed on every pointer store that record when an old object is updated to point to a young one. These recorded pointers form a remembered set, which supplements the normal root set for nursery collections."

- question: "Explain why copying collection's cost is proportional to what survives rather than to what dies, and why this makes it efficient for short-lived objects."
  type: short-answer
  answer: "Copying collection works by evacuating all live objects from fromspace into a fresh tospace and then treating all remaining fromspace memory as free. Dead objects are never touched — the algorithm simply abandons them by swapping the roles of the two halves. Therefore, the work done is exactly proportional to the number (and size) of live objects copied. If most objects die before collection, few survive, and the collection is cheap regardless of how many short-lived objects were allocated. This is the opposite of mark-and-sweep, which must traverse and reclaim each dead object explicitly."
  explanation: "The key insight is that copying collection ignores garbage rather than reclaiming it item by item. The 'cost of garbage' is zero — garbage is simply left behind in fromspace. The cost is entirely in evacuating survivors. This creates a counter-intuitive result: allocating many objects that almost immediately die is cheap for a copying collector, because it pays work only for the few that live. This property directly motivates generational collection, which concentrates copying collection in the nursery where the survivor ratio is lowest."
```

## Explainer

From your study of memory management and runtime systems, you know that dynamically allocated objects live on the heap and that someone must decide when to free them. Manual memory management (as in C) puts this burden on the programmer, leading to use-after-free bugs and memory leaks. **Garbage collection** automates this decision using a simple principle: an object is garbage if no chain of references from any live variable (the **root set**) can reach it. The root set includes local variables on the call stack, global variables, and CPU registers — anything the running program can directly access. If no path of pointers leads from any root to an object, the program cannot possibly use that object again, so its memory can be safely reclaimed.

The most intuitive GC algorithm is **mark-and-sweep**. In the mark phase, the collector starts from every root and follows all pointer chains, marking each reachable object. In the sweep phase, it scans the entire heap and frees every unmarked object. This is conceptually simple — it is just a graph traversal from the root set — but it has two costs: it must pause the program during collection (a "stop-the-world" pause), and it leaves the heap fragmented because freed objects leave gaps of various sizes. **Mark-and-compact** extends this by sliding surviving objects together after sweeping, eliminating fragmentation but adding the cost of updating all pointers to moved objects.

**Copying collection** takes a different approach: divide the heap into two equal halves (fromspace and tospace). Allocate objects in fromspace until it fills up, then copy all reachable objects into tospace, compacting them in the process, and swap the roles of the two spaces. Allocation becomes trivially fast — just increment a pointer — and fragmentation is eliminated. The trade-off is that half the heap is always wasted as reserve space. Copying collection shines when most objects are short-lived, because copying only live objects means the cost is proportional to what survives, not what dies.

This observation — that most objects die young — motivates **generational collection**, the strategy used by nearly every modern runtime (JVM, .NET, V8, Python's CPython). The heap is divided into generations: a small nursery for new objects and one or more older generations. The nursery is collected frequently and cheaply (using copying collection), and only objects that survive several nursery collections are promoted to the older generation, which is collected less often. Since most objects are allocated and discarded quickly (temporary strings, loop variables, intermediate results), generational GC concentrates effort where it pays off most. The key engineering challenge is tracking pointers from old objects to young objects (via write barriers), so that nursery collections do not need to scan the entire old generation to find roots.
