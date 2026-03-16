---
id: escape-analysis
title: Escape Analysis for Allocation Optimization
domain: computer-science
course: compilers
prerequisites:
- id: dataflow-analysis
  type: hard
- id: control-flow-graphs
  type: hard
builds-toward:
- alias-analysis
tags:
- optimization
- memory
- allocation
stage: advanced
status: draft
---

# Escape Analysis for Allocation Optimization

## Core Idea
Escape analysis determines whether objects escape a function's scope. Objects that don't escape can be stack-allocated instead of heap-allocated, or scalarized (fields separated and stored directly), improving memory performance by reducing allocation and garbage collection pressure.

## Explainer

In managed languages like Java or Go, creating an object with `new Point(x, y)` typically allocates memory on the heap. Heap allocation requires asking the runtime allocator for space, and every heap object eventually needs to be found and reclaimed by the garbage collector. Both costs add up, especially in hot loops that create many short-lived objects. **Escape analysis** asks a simple question: does this object ever become visible outside the function that created it? If not, the compiler can use dramatically cheaper allocation strategies.

An object **escapes** a function if any of these occur: it is returned as the function's result, it is stored into a global variable or a field of an object that itself escapes, it is passed to another function that might store it, or a reference to it is published to another thread. Using your knowledge of control flow graphs and dataflow analysis, the compiler tracks all references to the object through assignments, function calls, and field stores. If no execution path leads to the object being reachable after the function returns, the object is **non-escaping**.

For a non-escaping object, the compiler has two powerful options. **Stack allocation** places the object in the function's stack frame instead of on the heap. Stack memory is essentially free to allocate (just a pointer bump) and free to reclaim (the stack frame is destroyed when the function returns). No garbage collector involvement is needed. Even better, **scalar replacement** (also called scalarization) eliminates the object entirely by replacing it with individual local variables for each field. A `Point(x, y)` becomes two separate variables that the register allocator can place directly in CPU registers. The object, its header, its indirection — all gone.

The impact can be substantial. A method that creates a temporary `Iterator` or `StringBuilder` on every call may look expensive, but if escape analysis proves the object stays local, the JIT compiler eliminates the allocation entirely. Java's HotSpot JVM and Go's compiler both perform escape analysis routinely. The analysis must be conservative: if it cannot *prove* an object stays local (for example, because it is passed to a virtual method whose implementation is unknown), it must assume the object escapes and heap-allocate it. This is why understanding what causes escape is practical knowledge — writing code that avoids unnecessary escape (not storing temporary objects into fields, not passing them through opaque interfaces) helps the compiler optimize more aggressively.
