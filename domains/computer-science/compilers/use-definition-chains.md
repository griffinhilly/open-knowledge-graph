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

## Questions

```yaml
- question: "Variable x is assigned on line 5 (x = 10) and on line 8 (x = y + 2). An if-statement between lines 5 and 12 can route control through line 8 or bypass it. At line 12, the use of x is analyzed. What does its U-D chain contain?"
  type: multiple-choice
  options:
    - "Only line 8, since it is the most recent possible definition"
    - "Only line 5, since it is the first definition and line 8 does not always execute"
    - "Both line 5 and line 8, because both can reach line 12 along different control flow paths"
    - "Nothing, because U-D chains only apply to variables with a single unambiguous definition"
  answer: 2
  explanation: "U-D chains link a use to ALL definitions that could reach it along some execution path. Because the if-statement may bypass line 8, the definition from line 5 can still be live at line 12. If the path through line 8 is taken, that definition also reaches line 12. Both definitions appear in the U-D chain because both are in the reaching-definitions set at that point. The misconception that only the 'most recent' definition matters ignores how control flow analysis works — the compiler cannot assume which branch will be taken."

- question: "A compiler wants to apply constant propagation to replace a use of variable x with a literal. Using U-D chains, what condition must hold?"
  type: multiple-choice
  options:
    - "The variable x must not be redefined anywhere in the entire function"
    - "The U-D chain for that specific use must contain exactly one definition, and that definition must assign a constant value"
    - "All definitions of x in the program must assign the same constant value"
    - "The use must appear in the same basic block as the definition with no control flow in between"
  answer: 1
  explanation: "U-D chains make this check efficient: look up the chain for the specific use and count the definitions. If there is exactly one — say, x = 5 — the compiler can safely substitute the literal 5. If the chain contains two or more definitions, the value of x at that use point is ambiguous, and constant propagation is unsafe. This precision is what makes U-D chains valuable: without them, the compiler would need to re-solve reaching definitions each time it considers a substitution, querying a per-use structure is dramatically faster."

- question: "U-D chains allow a compiler to answer data-dependence queries with targeted lookups rather than re-solving reaching-definitions equations for every optimization pass."
  type: true-false
  answer: true
  explanation: "This is the fundamental value proposition of U-D chains. Reaching definitions analysis solves a system of dataflow equations across the control flow graph — an expensive operation. Without chains, every optimization (constant propagation, copy propagation, dead code elimination) would need to re-query this system for each use or definition it examines. U-D chains precompute the relationship once and organize it per-use, so subsequent analyses perform direct lookups. This is the 'sparse' analysis advantage: the compiler follows chains only to relevant definitions rather than examining all statements at all program points."

- question: "A use of a variable always has exactly one definition in its U-D chain, because programs must assign a variable before using it."
  type: true-false
  answer: false
  explanation: "This confuses program correctness requirements with data-flow analysis results. Even in a correct program where every use is preceded by at least one definition, control flow can create situations where multiple definitions reach the same use. An if-else that assigns x differently in each branch, followed by a use of x after the merge point, produces a U-D chain with two definitions — one from each branch. The use is unambiguously after a definition (so the program is correct), but the compiler cannot determine at compile time which definition's value will be used at runtime. Handling this multi-definition case correctly is exactly what U-D chains are designed to represent."

- question: "Why are U-D chains described as enabling 'sparse' analysis, and how do they improve on using reaching-definitions sets directly for each optimization query?"
  type: short-answer
  answer: "Reaching definitions computes, for each program point, a potentially large set of all live definitions. To answer 'which definitions reach this use?' using raw reaching-definitions sets, the compiler must look up the set at that point and filter for the specific variable — and do this for every use, every time. U-D chains preorganize this: for each use, the chain is already the filtered, variable-specific list of definitions that can reach it. Optimization passes follow chains directly to relevant definitions rather than scanning all statements at all points, which is the 'sparse' traversal. The result is a one-time construction cost in exchange for efficient repeated querying."
  explanation: "The analogy is building an index for a database: you pay upfront to organize information, then queries are fast. SSA form takes this further by making each variable have exactly one definition in the program, eliminating multi-definition chains entirely and enabling even more aggressive sparse analysis. U-D chains are the conceptual stepping stone: they show why per-use organization of data-flow information enables efficient analysis, which SSA then extends to its logical extreme."
```

## Explainer

From reaching definitions analysis, you know how to compute, for each point in a program, the set of definitions that could reach it along some execution path. **Use-definition chains** (U-D chains) take this information and organize it into a directly queryable structure: for each *use* of a variable, a U-D chain lists every *definition* of that variable that could flow to that use. The result is a sparse, per-variable view of data flow that makes many compiler analyses and transformations dramatically more efficient.

Consider a simple example. Suppose variable `x` is defined on line 3 (`x = 5`) and line 7 (`x = y + 1`), and used on line 10 (`z = x * 2`). If line 10 can be reached from both lines 3 and 7 — perhaps through different branches of an if-statement — then the U-D chain for the use of `x` at line 10 contains both definitions: {line 3, line 7}. If the code is restructured so that line 7 always executes before line 10 and kills the definition from line 3, then the U-D chain narrows to just {line 7}. This precision comes directly from solving the reaching definitions dataflow problem on the control flow graph.

The power of U-D chains lies in the questions they let you answer quickly. **Constant propagation** asks: does a variable have exactly one reaching definition, and is that definition a constant? If the U-D chain for a use contains a single definition `x = 5`, the compiler can replace the use with the literal `5`. **Dead code elimination** asks the reverse question using **definition-use chains** (D-U chains, the inverse structure): does a definition have zero uses? If nothing in any D-U chain references a definition, that definition is dead and can be removed. **Copy propagation** asks: is the single reaching definition a copy `x = y`? If so, replace uses of `x` with `y` directly.

Without U-D chains, answering these questions would require re-solving dataflow equations for each query. With them, the compiler precomputes the relationships once and then performs targeted lookups. This is especially important for **sparse analysis** — rather than examining every statement at every program point, the compiler follows chains only to relevant definitions and uses. The tradeoff is memory: storing explicit chains for every use and definition in a large program consumes space. More advanced representations like **static single assignment** (SSA) form build on the same intuition but encode the information even more compactly, making U-D chains a conceptual stepping stone toward modern compiler intermediate representations.
