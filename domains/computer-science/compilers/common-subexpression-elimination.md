---
id: common-subexpression-elimination
title: Common Subexpression Elimination (CSE)
domain: computer-science
course: compilers
prerequisites:
- id: dataflow-analysis
  type: hard
- id: reaching-definitions-analysis
  type: hard
tags:
- optimization
- cse
- expression-reuse
stage: advanced
status: validated
---

# Common Subexpression Elimination (CSE)

## Core Idea
Common subexpression elimination detects and removes redundant computations. If the same expression is computed multiple times with unchanged operands, compute it once and reuse the result. CSE requires tracking when expressions are available (all operands have definitions reaching the current point) and when they are not killed (operands not reassigned).

## Questions

```yaml
- question: "Two control flow paths converge at point P. On path A, the expression 'a + b' is computed and neither operand is modified before reaching P. On path B, 'a' is reassigned before P, and 'a + b' is not recomputed after the assignment. Can CSE safely reuse the result of 'a + b' at point P?"
  type: multiple-choice
  options:
    - "Yes — 'a + b' was computed on at least one incoming path, so it is available"
    - "No — available expressions analysis requires the expression to be computed on ALL incoming paths with operands unchanged since their last computation"
    - "Yes — the compiler can substitute the known new value of 'a' to compute a corrected result"
    - "It depends on which path the program takes at runtime, so the compiler must insert a runtime check"
  answer: 1
  explanation: "Available expressions analysis uses intersection at join points: an expression is available at P only if it is available on EVERY path reaching P. On path B, 'a' was reassigned after the last computation of 'a + b', so the stored result may not reflect the current value of 'a'. The compiler cannot know at compile time which path will execute, so it must conservatively declare 'a + b' unavailable. Using the path-A result when path B was taken would generate wrong code. This intersection semantics — not union — is what makes global CSE safe."

- question: "A compiler performs available expressions analysis at a join point where 'x * y' is available on one incoming control flow edge but not the other. What does the analysis conclude?"
  type: multiple-choice
  options:
    - "'x * y' is available — availability on any path is sufficient to justify reuse"
    - "'x * y' is not available — intersection requires availability on ALL paths before reuse is safe"
    - "'x * y' may be available depending on the loop iteration count"
    - "'x * y' is available only if 'x' and 'y' are loop-invariant variables"
  answer: 1
  explanation: "Intersection is the conservative, correct choice for available expressions. If 'x * y' is available on only one of two incoming edges, the compiler cannot guarantee that a stored result exists for both execution paths. Reusing a non-existent result on the other path would produce incorrect output. Option A (union) would be unsafe: it claims availability even when the result is absent on some paths. Safety requires that the expression is available on ALL paths, which intersection enforces — potentially missing some opportunities, but never generating incorrect code."

- question: "Local CSE and global CSE differ only in scale — both rely on the same underlying dataflow analysis, applied to a larger or smaller region of code."
  type: true-false
  answer: false
  explanation: "Local CSE requires NO dataflow analysis. A basic block is a straight-line sequence with no branches, so there is only one path through it. The compiler scans forward, maintains a table of previously computed expressions, and replaces duplicates — no join points, no gen/kill propagation needed. Global CSE, by contrast, must propagate availability information across basic block boundaries using a full forward dataflow analysis with gen sets, kill sets, and intersection at join points. The two methods differ fundamentally in technique, not just code region size."

- question: "The kill set for available expressions analysis at a statement that assigns to variable 'x' includes all expressions in the program that contain 'x' as an operand."
  type: true-false
  answer: true
  explanation: "When 'x' is assigned a new value, any previously computed expression containing 'x' may now be stale — the stored result no longer reflects what 'x + y' or 'x * z' would yield with the new value of 'x'. Therefore, all such expressions must be killed (removed from the available set) at that assignment. This is conservative but correct: even if the new value of 'x' happens to equal the old value, the compiler cannot generally know this and must invalidate all expressions using 'x' to preserve safety."

- question: "Why does global CSE use intersection (not union) at join points in the available expressions dataflow analysis? What would go wrong if union were used?"
  type: short-answer
  answer: "Intersection is required because CSE can only safely reuse a result that is guaranteed to exist no matter which path reached the current point. If union were used, the compiler would claim an expression is 'available' even when it was computed on only one of several paths — on the other paths, no stored result exists. When the program takes one of those paths, the compiler would try to reuse a nonexistent result, generating incorrect output. Intersection ensures the result was definitely computed on every possible execution path to this point, making reuse unconditionally safe."
  explanation: "This is the fundamental correctness constraint in dataflow analysis for optimization. Intersection gives a safe under-approximation: the compiler may miss some reuse opportunities (it's conservative), but it never reuses a result that might be stale or absent. Union is an over-approximation — it finds more 'available' expressions but is unsafe. The broader principle: optimizations must be conservative when in doubt; performance is sacrificed before correctness. Global CSE is typically combined with loop-invariant code motion to recover additional reuse opportunities that intersection alone might miss."
```

## Explainer

Consider this fragment of intermediate code: `t1 = a + b; t2 = a + b;`. If neither `a` nor `b` is modified between the two statements, then `t2` will always equal `t1`. Computing `a + b` a second time is pure waste — the compiler can replace the second computation with `t2 = t1`. This is the essence of **common subexpression elimination (CSE)**: find expressions that have already been computed with unchanged operands, and reuse the earlier result instead of recomputing.

The challenge is determining *when* an expression is safe to reuse. From your study of dataflow analysis and reaching definitions, you have the machinery to answer this. An expression `a + b` is **available** at a program point if every path from the start of the program to that point computes `a + b`, and neither `a` nor `b` is redefined after the most recent computation. If any path redefines an operand without recomputing the expression, the earlier value may be stale and cannot be reused. The compiler solves this with **available expressions analysis**, a forward dataflow problem: the gen set at each statement includes expressions it computes, the kill set includes all expressions containing variables it redefines, and the meet operation at join points takes the intersection (an expression is only available if it is available on *all* incoming paths).

There are two scopes of CSE. **Local CSE** operates within a single basic block — a straight-line sequence of instructions with no branches. This is simple because there is only one path, so you just scan forward, maintaining a table of computed expressions and replacing duplicates. **Global CSE** operates across an entire function's control flow graph, handling branches and loops. Global CSE requires the full available expressions dataflow analysis, which propagates information across basic block boundaries. The result is more powerful: it can catch redundancies across branches, in loop bodies, and between distant parts of the function.

CSE interacts productively with other optimizations. Copy propagation can expose new common subexpressions by replacing variable copies with their originals, making previously different-looking expressions identical. Constant folding can simplify operands, again revealing matches. In loops, CSE often works hand-in-hand with loop-invariant code motion: an expression computed inside a loop whose operands never change across iterations is both a common subexpression and loop-invariant, and can be hoisted out of the loop entirely. The compiler's optimization pipeline typically runs these passes in sequence, with each pass creating opportunities for the next.
