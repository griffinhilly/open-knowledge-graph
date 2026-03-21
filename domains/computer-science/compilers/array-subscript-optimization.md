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

## Questions

```yaml
- question: "A compiler applies strength reduction to the loop `for (i=0; i<n; i++) a[i] = 0;`. Which transformation best describes what happens to the address calculation `base + i * element_size`?"
  type: multiple-choice
  options:
    - "The multiplication is replaced by a left shift, because element_size is always a power of two"
    - "A pointer `p` is initialized to `base` before the loop and incremented by `element_size` each iteration, replacing the multiply-add with a single add"
    - "The loop is unrolled so the multiplication only executes every other iteration"
    - "The subscript is cached and reused, so the multiplication executes once regardless of loop length"
  answer: 1
  explanation: "Strength reduction for a derived induction variable replaces the per-iteration `multiply + add` with a single `add`. A pointer is initialized to `base` before the loop and advanced by `element_size` on each iteration — producing the same address sequence with no multiplication. Option A (shift) is a narrower optimization that only works for power-of-two element sizes and is a separate transformation. Option D describes constant folding, not strength reduction for a loop-varying expression."

- question: "A student claims that array subscript optimization changes which memory locations are accessed in order to improve performance. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — the optimizer reorders memory accesses to improve cache behavior"
    - "Yes — the optimizer skips redundant accesses identified by data dependence analysis"
    - "No — strength reduction produces the same address sequence using cheaper arithmetic operations"
    - "No — the optimizer replaces array accesses with register variables, eliminating memory access entirely"
  answer: 2
  explanation: "Strength reduction is purely an arithmetic optimization: it computes the same addresses using additions instead of multiplications. The memory access pattern — which locations are touched, in what order — is unchanged. This is confirmed by data dependence analysis, which verifies that the new pointer-based access visits the same locations in the same order, preserving all dependencies. Option A (cache reordering) describes loop interchange or tiling, which are separate transformations."

- question: "Strength reduction can be applied to `a[b[i]]` when `b[i]` is known to be monotonically increasing."
  type: true-false
  answer: false
  explanation: "Strength reduction requires a *linear* function of the loop induction variable: the address must advance by a constant stride each iteration. `a[b[i]]` uses indirect indexing — the subscript depends on the contents of `b`, which are generally not known at compile time and not necessarily a constant stride. Strength reduction does not apply here, even if `b[i]` happens to be monotone at runtime."

- question: "In a doubly-nested loop accessing `a[i][j]`, strength reduction can eliminate both the outer and inner multiplications by maintaining a separate pointer for each loop level."
  type: true-false
  answer: true
  explanation: "For `a[i][j]`, the unoptimized address involves `base + i * row_size + j * element_size` — two multiplications. The outer multiplication (involving `i`) can be reduced by a row pointer updated in the outer loop; the inner multiplication (involving `j`) can be reduced by a column pointer updated in the inner loop. Both are linear functions of their respective loop variables, so both qualify for strength reduction independently. This compounds the savings in nested-loop linear algebra code."

- question: "Why is array subscript optimization especially important for dense linear algebra code rather than for code with irregular access patterns?"
  type: short-answer
  answer: "Dense linear algebra (matrix multiply, convolution, stencils) has inner loops that execute millions of times with regular, strided array access. Each iteration has a constant address stride, so the subscript forms a derived induction variable — exactly the pattern that makes strength reduction applicable and impactful. Irregular access patterns (e.g., sparse matrices, hash tables) involve non-linear or data-dependent subscripts where no constant stride exists, so strength reduction cannot apply."
  explanation: "The optimization's benefit scales with loop trip count: replacing a multiply with an add saves a small constant per iteration, but in a loop running 10⁸ times that constant dominates total execution time. Dense linear algebra is the prototypical case because it combines high trip counts with perfectly regular stride patterns. Irregular patterns break the linear induction variable assumption, so the compiler cannot safely substitute an increment for the general address calculation."
```

## Explainer

Consider a simple loop that processes each element of an array: `for (i = 0; i < n; i++) a[i] = 0;`. The expression `a[i]` looks innocent, but the compiler must translate it into an address calculation: `base_address + i * element_size`. That multiplication executes on every iteration, even though the address advances by a fixed stride each time. From your study of loop detection and data dependence analysis, you know how to identify loop structure and track how variables change across iterations. **Array subscript optimization** exploits that regularity to eliminate redundant address arithmetic.

The central technique is **strength reduction** applied to **induction variables**. An induction variable is one that changes by a constant amount on each loop iteration — the classic loop counter `i` is the simplest example. The array address `base + i * element_size` is a **derived induction variable**: it is a linear function of `i`. Strength reduction replaces the multiplication with an addition by introducing a new pointer variable initialized to `base` before the loop, then incremented by `element_size` on each iteration. The expensive `multiply + add` per iteration becomes a single `add`. On most hardware, addition is significantly cheaper than multiplication, and the savings compound across millions of iterations in tight loops.

For nested loops, the optimization becomes more powerful and more intricate. Consider `a[i][j]` in a doubly-nested loop. The unoptimized address is `base + i * row_size + j * element_size` — two multiplications per inner iteration. The compiler can reduce the outer multiplication by maintaining a row pointer that advances by `row_size` in the outer loop, and reduce the inner multiplication by incrementing a column pointer by `element_size` in the inner loop. Data dependence analysis confirms these transformations are safe: the new pointer-based access pattern reaches exactly the same memory locations in the same order, so no dependencies are violated.

The compiler must also handle cases where subscript expressions are more complex — `a[2*i + 1]` or `a[i*n + j]` — by recognizing the linear pattern and reducing it to an initial value plus a constant stride. When the subscript is not a linear function of loop variables (e.g., `a[b[i]]` with indirect indexing), strength reduction does not apply. This optimization is particularly impactful in dense linear algebra — matrix multiplication, convolution, stencil computations — where the innermost loops are dominated by regular array access patterns and even small per-iteration savings translate to large absolute speedups.
