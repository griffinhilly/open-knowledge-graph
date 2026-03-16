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
status: draft
---

# Reaching Definitions Analysis

## Core Idea
Reaching definitions analysis determines which variable assignments (definitions) can reach a given program point without being overwritten. A definition 'd' reaches point p if there exists a path from d's block to p where the variable is not reassigned. Results enable constant propagation, copy propagation, and other optimizations.

## Explainer

From your study of dataflow analysis, you know the general framework: define a set of facts, specify how those facts flow through basic blocks and across edges, and iterate to a fixed point. Reaching definitions is one of the most fundamental instantiations of this framework. The "fact" being tracked is simple: which assignments to variables are still "alive" — meaning they have not been overwritten — when execution reaches a particular point in the program.

Consider a straightforward example. If block B1 contains `x = 5` and block B2 contains `y = x + 1`, and there is a path from B1 to B2 where `x` is never reassigned, then the definition `x = 5` **reaches** the use of `x` in B2. But if there is another path through block B3 that also assigns `x = 10`, and both paths converge before B2, then two definitions of `x` reach B2: `x = 5` from B1 and `x = 10` from B3. The compiler cannot assume `x` is 5 at B2, which means constant propagation cannot replace `x` with `5` there.

The analysis works using **gen and kill sets** for each basic block. A block's **gen set** contains the definitions it creates — the assignments that originate in that block. Its **kill set** contains the definitions it destroys — any prior definition of the same variable, since the new assignment overwrites the old value. The dataflow equation for each block is: OUT[B] = gen[B] ∪ (IN[B] − kill[B]). The IN set for a block is the union of OUT sets from all its predecessors. Because definitions can reach a point along *any* path (not just all paths), this is a **may-analysis** using union at join points. The analysis initializes all sets to empty and iterates until no OUT set changes — the fixed point.

Reaching definitions directly enables several important optimizations. **Constant propagation** checks whether all reaching definitions of a variable assign the same constant — if so, the variable can be replaced with that constant. **Copy propagation** checks whether a variable's only reaching definition is a copy like `x = y`, and if `y` has not been redefined, replaces uses of `x` with `y`. **Dead code elimination** uses the inverse question: if a definition reaches no use at all, the assignment is dead and can be removed. Understanding reaching definitions gives you the foundation for reasoning about how information flows forward through a program, which is the basis for most compiler optimizations.
