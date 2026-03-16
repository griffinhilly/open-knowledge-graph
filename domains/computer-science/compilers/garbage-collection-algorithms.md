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

## Explainer

From your study of memory management and runtime systems, you know that dynamically allocated objects live on the heap and that someone must decide when to free them. Manual memory management (as in C) puts this burden on the programmer, leading to use-after-free bugs and memory leaks. **Garbage collection** automates this decision using a simple principle: an object is garbage if no chain of references from any live variable (the **root set**) can reach it. The root set includes local variables on the call stack, global variables, and CPU registers — anything the running program can directly access. If no path of pointers leads from any root to an object, the program cannot possibly use that object again, so its memory can be safely reclaimed.

The most intuitive GC algorithm is **mark-and-sweep**. In the mark phase, the collector starts from every root and follows all pointer chains, marking each reachable object. In the sweep phase, it scans the entire heap and frees every unmarked object. This is conceptually simple — it is just a graph traversal from the root set — but it has two costs: it must pause the program during collection (a "stop-the-world" pause), and it leaves the heap fragmented because freed objects leave gaps of various sizes. **Mark-and-compact** extends this by sliding surviving objects together after sweeping, eliminating fragmentation but adding the cost of updating all pointers to moved objects.

**Copying collection** takes a different approach: divide the heap into two equal halves (fromspace and tospace). Allocate objects in fromspace until it fills up, then copy all reachable objects into tospace, compacting them in the process, and swap the roles of the two spaces. Allocation becomes trivially fast — just increment a pointer — and fragmentation is eliminated. The trade-off is that half the heap is always wasted as reserve space. Copying collection shines when most objects are short-lived, because copying only live objects means the cost is proportional to what survives, not what dies.

This observation — that most objects die young — motivates **generational collection**, the strategy used by nearly every modern runtime (JVM, .NET, V8, Python's CPython). The heap is divided into generations: a small nursery for new objects and one or more older generations. The nursery is collected frequently and cheaply (using copying collection), and only objects that survive several nursery collections are promoted to the older generation, which is collected less often. Since most objects are allocated and discarded quickly (temporary strings, loop variables, intermediate results), generational GC concentrates effort where it pays off most. The key engineering challenge is tracking pointers from old objects to young objects (via write barriers), so that nursery collections do not need to scan the entire old generation to find roots.
