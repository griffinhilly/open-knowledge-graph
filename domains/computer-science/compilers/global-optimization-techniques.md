---
id: global-optimization-techniques
title: Global Optimization Techniques
domain: computer-science
course: compilers
prerequisites:
- id: use-definition-chains
  type: hard
- id: code-optimization
  type: hard
builds-toward:
- procedure-inlining-optimization
- array-subscript-optimization
tags:
- optimization
- global-opts
- dataflow
stage: advanced
status: draft
---

# Global Optimization Techniques

## Core Idea
Global optimizations operate across basic block boundaries using data-flow information. Common global optimizations include code hoisting, common subexpression elimination, and copy propagation. These optimizations are more powerful but more complex than local optimizations.

## How It's Best Learned
Implement global common subexpression elimination or code hoisting using reaching definitions and data-flow analysis.

## Questions

```yaml
- question: "In global common subexpression elimination, when can the compiler safely replace the second computation of `a + b` in block B3 with the value already computed in block B1?"
  type: multiple-choice
  options:
    - "Whenever B3 immediately follows B1 in the source code order"
    - "When neither `a` nor `b` is redefined on any path from B1 to B3"
    - "When `a` and `b` are both global variables visible across the entire function"
    - "When B1 dominates B3 in the control flow graph"
  answer: 1
  explanation: "The expression `a + b` is 'available' at B3 only if it has been computed and not subsequently invalidated on every path from B1 to B3. Domination alone (option D) is insufficient — `a` or `b` might be redefined on some path, making the earlier value stale. Global variables are not special in this context. Source code order (option A) is irrelevant since control flow may diverge. Available expressions analysis — a forward dataflow problem computing the intersection of available expressions along all paths — is what the compiler uses to establish this condition rigorously."

- question: "Which condition must hold for loop-invariant code motion to safely hoist a computation out of a loop?"
  type: multiple-choice
  options:
    - "The computation must appear in every basic block inside the loop body"
    - "The computation's operands must have the same reaching definitions at the hoist point as at the original location inside the loop"
    - "The loop must be guaranteed to execute at least once, so the hoisted computation always runs"
    - "The computation must involve only constants or variables that are never assigned inside the function"
  answer: 1
  explanation: "The safety check is that the operands have the same reaching definitions at the hoist point as at the original location — meaning no definition of those operands exists inside the loop that could change the result. This is precisely what use-definition chains provide. Option A is wrong: a computation only in some blocks can still be hoisted if the other conditions hold. Option C (guaranteed execution) is relevant for avoiding new side effects but is a separate concern from correctness of the value. Option D is overly restrictive — variables assigned outside the loop are perfectly safe."

- question: "Global dataflow analysis must use conservative 'meet-over-all-paths' reasoning, which for available expressions means computing the intersection (not union) of available expressions along all paths to a program point."
  type: true-false
  answer: true
  explanation: "For available expressions, an expression is safe to use only if it is available on every path reaching that point — the intersection. If it is available on some paths but not others, using the optimized value would produce wrong results when execution follows the path where it was not computed or was invalidated. This conservatism is what guarantees soundness: the optimization may miss some opportunities (expressions available on most but not all paths), but it will never produce incorrect code."

- question: "Copy propagation — replacing uses of `x` with `y` after the assignment `x = y` — is primarily valuable because it directly reduces the number of memory accesses in the final code."
  type: true-false
  answer: false
  explanation: "Copy propagation's primary value is enabling further optimizations, especially dead code elimination. After propagating all uses of `x` to `y`, the original assignment `x = y` may become dead (no remaining uses of `x`), and the compiler can remove it entirely. The direct benefit of one fewer variable reference is minor; the cascading benefit of enabling subsequent optimizations is the real gain. This is characteristic of global optimizations generally — they often create opportunities for each other."

- question: "Why must global dataflow analysis reason conservatively over all possible execution paths, rather than optimistically assuming the most common or most likely path?"
  type: short-answer
  answer: "Because the compiler must guarantee correctness for every possible execution, not just typical ones. If an expression is available on the frequent path but not on a rare path (e.g., a rarely-taken branch that redefines a variable), optimizing it would produce the wrong result whenever that rare path executes. Unlike a human programmer who might assume 'this branch almost never runs,' the compiler has no runtime information at compile time and must be safe for all inputs. Conservative reasoning — requiring a property to hold on every path — ensures that the optimization is never applied unsafely."
  explanation: "This is the fundamental tradeoff in static analysis: soundness (no incorrect transformations) at the cost of completeness (some safe transformations may be missed). Path-sensitive or speculative optimizations can recover some missed opportunities but at the cost of greater complexity and sometimes correctness guarantees."
```

## Explainer

From your study of code optimization, you know that local optimizations work within a single basic block — a straight-line sequence of instructions with one entry and one exit. These are safe and straightforward because control flow within a block is linear. But real programs branch, loop, and merge, meaning most optimization opportunities span multiple basic blocks. **Global optimization** extends optimization across an entire function's control flow graph, using the dataflow information from use-definition chains to determine what transformations are safe at each point in the program.

Consider **global common subexpression elimination** (GCSE). If the expression `a + b` is computed in block B1 and again in block B3, and neither `a` nor `b` is redefined on any path from B1 to B3, then the second computation is redundant. A local optimizer would miss this because the two computations are in different blocks. GCSE uses **available expressions analysis** — a forward dataflow problem that tracks which expressions have been computed and not subsequently invalidated at each program point. If `a + b` is available at the entry to B3, the compiler replaces the redundant computation with a reference to the previously computed value, saving an arithmetic operation on every execution of that path.

**Code hoisting** (also called loop-invariant code motion when applied to loops) moves computations to earlier points in the program where they dominate later uses. If a computation inside a loop produces the same result on every iteration because its operands are not modified within the loop, the compiler can hoist it above the loop header so it executes once instead of thousands of times. The safety check requires that the computation's operands have the same reaching definitions at the hoist point as they do at the original location — this is exactly the information that use-definition chains provide. **Copy propagation** is another global optimization: after an assignment `x = y`, every subsequent use of `x` (where no intervening redefinition of `x` or `y` occurs) can be replaced with `y`, potentially enabling further optimizations like dead code elimination when `x` is no longer used.

The challenge of global optimization is that safety requires conservative reasoning about all possible execution paths. If a value is available on one path to a block but not another, the compiler cannot assume it is available — it must account for the worst case. This is why dataflow analysis computes meet-over-all-paths solutions: the intersection (for available expressions) or union (for reaching definitions) of information along every path to a given point. The result is that global optimizations are always sound but sometimes miss opportunities that a more aggressive analysis (like path-sensitive or speculative optimization) could catch. Despite this conservatism, global optimizations typically yield significant performance improvements — often 10–30% — because redundant computations and loop-invariant operations are pervasive in real programs.
