---
id: use-definition-chains
title: Use-Definition Chains
domain: computer-science
course: compilers
prerequisites:
- id: data-dependence-analysis
  type: hard
- id: reaching-definitions-analysis
  type: hard
builds-toward:
- global-optimization-techniques
tags:
- analysis
- use-def-chains
- optimization
stage: advanced
status: draft
---

# Use-Definition Chains

## Core Idea
A use-definition chain links each use of a variable to all definitions that could reach it. U-D chains enable efficient dependence queries for sparse analysis and targeted optimizations. Constructing U-D chains requires solving the reaching definitions problem.

## How It's Best Learned
Implement reaching definitions analysis and use it to construct U-D chains. Trace chains through programs with multiple definitions.

## Common Misconceptions
U-D chains are only useful for optimization (they enable many forms of analysis). All uses must have a unique definition (a use can have multiple definitions in control flow).

## Explainer

From reaching definitions analysis, you know how to compute, for each point in a program, the set of definitions that could reach it along some execution path. **Use-definition chains** (U-D chains) take this information and organize it into a directly queryable structure: for each *use* of a variable, a U-D chain lists every *definition* of that variable that could flow to that use. The result is a sparse, per-variable view of data flow that makes many compiler analyses and transformations dramatically more efficient.

Consider a simple example. Suppose variable `x` is defined on line 3 (`x = 5`) and line 7 (`x = y + 1`), and used on line 10 (`z = x * 2`). If line 10 can be reached from both lines 3 and 7 — perhaps through different branches of an if-statement — then the U-D chain for the use of `x` at line 10 contains both definitions: {line 3, line 7}. If the code is restructured so that line 7 always executes before line 10 and kills the definition from line 3, then the U-D chain narrows to just {line 7}. This precision comes directly from solving the reaching definitions dataflow problem on the control flow graph.

The power of U-D chains lies in the questions they let you answer quickly. **Constant propagation** asks: does a variable have exactly one reaching definition, and is that definition a constant? If the U-D chain for a use contains a single definition `x = 5`, the compiler can replace the use with the literal `5`. **Dead code elimination** asks the reverse question using **definition-use chains** (D-U chains, the inverse structure): does a definition have zero uses? If nothing in any D-U chain references a definition, that definition is dead and can be removed. **Copy propagation** asks: is the single reaching definition a copy `x = y`? If so, replace uses of `x` with `y` directly.

Without U-D chains, answering these questions would require re-solving dataflow equations for each query. With them, the compiler precomputes the relationships once and then performs targeted lookups. This is especially important for **sparse analysis** — rather than examining every statement at every program point, the compiler follows chains only to relevant definitions and uses. The tradeoff is memory: storing explicit chains for every use and definition in a large program consumes space. More advanced representations like **static single assignment** (SSA) form build on the same intuition but encode the information even more compactly, making U-D chains a conceptual stepping stone toward modern compiler intermediate representations.
