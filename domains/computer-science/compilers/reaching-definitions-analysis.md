---
id: reaching-definitions-analysis
title: Reaching Definitions Analysis
domain: computer-science
course: compilers
prerequisites:
- id: dataflow-analysis
  type: hard
builds-toward:
- common-subexpression-elimination
- constant-propagation
tags:
- dataflow
- reaching-definitions
- optimization
stage: advanced
status: validated
---

# Reaching Definitions Analysis

## Core Idea
Reaching definitions analysis determines which variable assignments (definitions) can reach a given program point without being overwritten. A definition 'd' reaches point p if there exists a path from d's block to p where the variable is not reassigned. Results enable constant propagation, copy propagation, and other optimizations.

## Questions

```yaml
- question: "Block B1 assigns `x = 5` and block B2 assigns `x = 10`. Both B1 and B2 are predecessors of block B3, which contains the expression `y = x + 1`. Can constant propagation replace `x` with a constant value in B3?"
  type: multiple-choice
  options:
    - "Yes — x = 5 should be used because B1 is likely executed first"
    - "Yes — x = 10 should be used because it is the more recent assignment"
    - "No — both definitions reach B3, so the compiler cannot determine a unique constant value for x"
    - "No — reaching definitions cannot track variables across multiple blocks"
  answer: 2
  explanation: "Reaching definitions uses union at join points (it is a may-analysis): IN[B3] contains definitions from ALL predecessor blocks. Since both `x = 5` from B1 and `x = 10` from B2 reach B3, the compiler cannot assume x has a single constant value there — constant propagation requires exactly one reaching definition with a constant. Options A and B reflect the common mistake of assuming execution order determines which definition 'wins'; a dataflow analysis must conservatively account for all possible execution paths."

- question: "Why does reaching definitions analysis use union (not intersection) to combine facts from predecessor blocks at a join point?"
  type: multiple-choice
  options:
    - "Because it is a must-analysis: a definition must reach via all paths to be considered live"
    - "Because it is a may-analysis: a definition reaches a point if it arrives via at least one path"
    - "Because the kill sets require union to correctly remove overwritten definitions"
    - "Because intersection would make the analysis unsound, producing too few reaching definitions"
  answer: 1
  explanation: "Reaching definitions is a may-analysis — it tracks which definitions *might* reach a given point along some path. A definition is included in IN[B] if it can arrive via ANY predecessor path, hence union. Intersection would compute the must-analysis dual: definitions that reach via ALL paths. Using intersection for reaching definitions would cause unsoundness in the opposite direction — it would miss valid reaching definitions, incorrectly enabling optimizations like constant propagation when a definition only sometimes reaches a use."

- question: "If a variable x is assigned in every predecessor block of block B, then every one of those definitions appears in IN[B]."
  type: true-false
  answer: true
  explanation: "Because reaching definitions uses union at join points, IN[B] = union of OUT[pred] for all predecessors. If x is defined in every predecessor, each predecessor's OUT set includes that definition, and the union includes all of them. This is precisely why reaching definitions cannot enable constant propagation when multiple different definitions reach a point — all of them are tracked, even if the same variable is defined everywhere."

- question: "A basic block's kill set contains definitions that occur after that block in the control flow graph and that assign to the same variable."
  type: true-false
  answer: false
  explanation: "The kill set contains definitions that occur BEFORE the current block (anywhere else in the program) that assign to the same variable as a definition in this block. When a block defines x, it 'kills' (overwrites) any earlier reaching definition of x, because the old value of x can no longer reach points after this block unchanged. The kill set looks backward, not forward — it identifies what the current block's assignments destroy, not what later blocks might overwrite."

- question: "Explain why reaching definitions is classified as a 'may-analysis' and what practical consequence this has for how compilers use its results."
  type: short-answer
  answer: "Reaching definitions is a may-analysis because a definition is considered to reach a point if there EXISTS at least one control-flow path from the definition to that point without an intervening kill — not if all paths carry the definition. The practical consequence is conservatism: the analysis over-approximates, potentially reporting more definitions as reaching than actually execute at runtime. Compilers using the results for optimization (e.g., constant propagation) must treat a use as safe to optimize only if exactly one definition reaches it — any ambiguity blocks the optimization. May-analyses are sound for this use case because they never miss a real reaching definition."
  explanation: "The may/must distinction in dataflow analysis determines how join points combine information. May-analyses (union) are appropriate when any reachable path matters — for reaching definitions, a definition that can arrive on even one path must be considered because the compiler cannot rule out that path being taken at runtime. Must-analyses (intersection) would only retain definitions guaranteed to arrive regardless of which path executes, which is overly restrictive for most forward dataflow problems."
```

## Explainer

From your study of dataflow analysis, you know the general framework: define a set of facts, specify how those facts flow through basic blocks and across edges, and iterate to a fixed point. Reaching definitions is one of the most fundamental instantiations of this framework. The "fact" being tracked is simple: which assignments to variables are still "alive" — meaning they have not been overwritten — when execution reaches a particular point in the program.

Consider a straightforward example. If block B1 contains `x = 5` and block B2 contains `y = x + 1`, and there is a path from B1 to B2 where `x` is never reassigned, then the definition `x = 5` **reaches** the use of `x` in B2. But if there is another path through block B3 that also assigns `x = 10`, and both paths converge before B2, then two definitions of `x` reach B2: `x = 5` from B1 and `x = 10` from B3. The compiler cannot assume `x` is 5 at B2, which means constant propagation cannot replace `x` with `5` there.

The analysis works using **gen and kill sets** for each basic block. A block's **gen set** contains the definitions it creates — the assignments that originate in that block. Its **kill set** contains the definitions it destroys — any prior definition of the same variable, since the new assignment overwrites the old value. The dataflow equation for each block is: OUT[B] = gen[B] ∪ (IN[B] − kill[B]). The IN set for a block is the union of OUT sets from all its predecessors. Because definitions can reach a point along *any* path (not just all paths), this is a **may-analysis** using union at join points. The analysis initializes all sets to empty and iterates until no OUT set changes — the fixed point.

Reaching definitions directly enables several important optimizations. **Constant propagation** checks whether all reaching definitions of a variable assign the same constant — if so, the variable can be replaced with that constant. **Copy propagation** checks whether a variable's only reaching definition is a copy like `x = y`, and if `y` has not been redefined, replaces uses of `x` with `y`. **Dead code elimination** uses the inverse question: if a definition reaches no use at all, the assignment is dead and can be removed. Understanding reaching definitions gives you the foundation for reasoning about how information flows forward through a program, which is the basis for most compiler optimizations.
