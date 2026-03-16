---
id: array-subscript-optimization
title: Array Subscript Optimization
domain: computer-science
course: compilers
prerequisites:
- id: loop-detection-analysis
  type: hard
- id: data-dependence-analysis
  type: hard
builds-toward:
- instruction-selection-techniques
tags:
- optimization
- loops
- memory
stage: advanced
status: draft
---

# Array Subscript Optimization

## Core Idea
Array subscript expressions often involve expensive multiplication and addition operations in loops. Strength reduction optimizes subscripts by detecting linear patterns (common in loops) and substituting cheaper operations. This optimization is particularly important for dense linear algebra code.

## How It's Best Learned
Implement strength reduction for induction variables in loops. Manually optimize nested loop array accesses.

## Explainer

Consider a simple loop that processes each element of an array: `for (i = 0; i < n; i++) a[i] = 0;`. The expression `a[i]` looks innocent, but the compiler must translate it into an address calculation: `base_address + i * element_size`. That multiplication executes on every iteration, even though the address advances by a fixed stride each time. From your study of loop detection and data dependence analysis, you know how to identify loop structure and track how variables change across iterations. **Array subscript optimization** exploits that regularity to eliminate redundant address arithmetic.

The central technique is **strength reduction** applied to **induction variables**. An induction variable is one that changes by a constant amount on each loop iteration — the classic loop counter `i` is the simplest example. The array address `base + i * element_size` is a **derived induction variable**: it is a linear function of `i`. Strength reduction replaces the multiplication with an addition by introducing a new pointer variable initialized to `base` before the loop, then incremented by `element_size` on each iteration. The expensive `multiply + add` per iteration becomes a single `add`. On most hardware, addition is significantly cheaper than multiplication, and the savings compound across millions of iterations in tight loops.

For nested loops, the optimization becomes more powerful and more intricate. Consider `a[i][j]` in a doubly-nested loop. The unoptimized address is `base + i * row_size + j * element_size` — two multiplications per inner iteration. The compiler can reduce the outer multiplication by maintaining a row pointer that advances by `row_size` in the outer loop, and reduce the inner multiplication by incrementing a column pointer by `element_size` in the inner loop. Data dependence analysis confirms these transformations are safe: the new pointer-based access pattern reaches exactly the same memory locations in the same order, so no dependencies are violated.

The compiler must also handle cases where subscript expressions are more complex — `a[2*i + 1]` or `a[i*n + j]` — by recognizing the linear pattern and reducing it to an initial value plus a constant stride. When the subscript is not a linear function of loop variables (e.g., `a[b[i]]` with indirect indexing), strength reduction does not apply. This optimization is particularly impactful in dense linear algebra — matrix multiplication, convolution, stencil computations — where the innermost loops are dominated by regular array access patterns and even small per-iteration savings translate to large absolute speedups.
