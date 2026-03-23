---
id: basic-block-analysis
title: Basic Block Analysis
domain: computer-science
course: compilers
prerequisites:
- id: quadruple-intermediate-representation
  type: hard
- id: control-flow-graphs
  type: hard
builds-toward:
- data-dependence-analysis
tags:
- analysis
- basic-blocks
- optimization
stage: advanced
status: validated
---

# Basic Block Analysis

## Core Idea
A basic block is a maximal sequence of instructions with no jumps except at the end and no jump targets except at the beginning. Identifying basic blocks is the first step toward understanding program structure for optimization. Basic blocks form nodes of a control-flow graph.

## How It's Best Learned
Build a basic block graph from 3AC code and study how it represents program structure. Implement a basic block builder and test on loop-heavy code.

## Common Misconceptions
Exception handlers complicate basic block analysis (they do; must decide how to handle them). All instructions within a block can be reordered (only if they have no dependencies).

## Questions

```yaml
- question: "A three-address code sequence contains a conditional branch to label L7, followed by another instruction. According to basic block analysis, which of the following is correct?"
  type: multiple-choice
  options:
    - "Only the instruction at L7 starts a new basic block; the instruction after the branch stays in the current block"
    - "The conditional branch itself becomes its own single-instruction basic block"
    - "Both the instruction at L7 and the instruction immediately following the branch are leaders that start new basic blocks"
    - "The branch ends the current block; no new block begins until the next unconditional jump"
  answer: 2
  explanation: "A branch creates two potential successors: the branch target (L7) and the fall-through (the instruction immediately after). Both are leaders because: L7 is a jump target, and the instruction after the branch immediately follows a branch instruction. These are two of the three leader conditions. The current block ends at the branch (its last instruction). This ensures every basic block has exactly one entry point and exits only at its final instruction — the defining property of a basic block."

- question: "A compiler wants to propagate constants across an entire function (not just within single blocks). What infrastructure is required beyond basic block identification?"
  type: multiple-choice
  options:
    - "No additional infrastructure — constant propagation is purely local and works block-by-block"
    - "A control-flow graph built from the basic blocks, then a dataflow analysis (reaching definitions) across block boundaries"
    - "Splitting basic blocks into smaller single-instruction units so constants propagate more easily"
    - "Exception handler elimination, since exception targets are the only obstacle to global propagation"
  answer: 1
  explanation: "Local constant folding works within a single basic block. But to propagate a constant computed in block A into block B (which follows A), the compiler needs to know which blocks can reach which — that is, it needs the control-flow graph. Then it runs a dataflow analysis (like reaching definitions) that tracks what values are guaranteed to be constant at each point across the CFG. This is the distinction between local optimizations (within a block) and global optimizations (across the CFG). Basic block identification is the prerequisite for building the CFG."

- question: "Any two instructions within the same basic block can be freely reordered, since a basic block guarantees sequential execution with no branches."
  type: true-false
  answer: false
  explanation: "Sequential control flow guarantees that all instructions in a basic block execute in order when any of them executes — but it does NOT mean they can be arbitrarily reordered. Reordering is only safe when there are no data dependencies: if instruction B reads a value written by instruction A, B must come after A regardless of the block structure. A basic block eliminates control-flow hazards but not data-dependence hazards. Local optimization within a block still requires dependence analysis before reordering instructions."

- question: "A basic block has exactly one entry point (its first instruction) and all control flow exits through its last instruction, with no jumps into or out of the middle of the block."
  type: true-false
  answer: true
  explanation: "This single-entry, single-exit property is the defining characteristic of a basic block and the reason it is so useful for optimization. It means that if the first instruction of a block executes, every instruction in the block executes. This guarantee allows local optimizations (common subexpression elimination, constant folding) to reason about a block's contents as a straight-line sequence without worrying about control flow. The CFG edges then capture how blocks relate to each other."

- question: "What is a 'leader' in basic block analysis, and what three conditions make an instruction a leader? Why does identifying leaders fully determine the basic block partition?"
  type: short-answer
  answer: "A leader is an instruction that begins a new basic block. The three conditions are: (1) the first instruction in the program is always a leader; (2) any instruction that is the target of a branch or jump is a leader; (3) any instruction that immediately follows a branch or jump is a leader. Once all leaders are identified, each basic block consists of a leader plus all subsequent instructions up to (but not including) the next leader. This completely partitions the instruction sequence into non-overlapping basic blocks with no ambiguity."
  explanation: "The leader-based algorithm is elegant because it requires only a single pass to identify leaders and a second pass to assign instructions to blocks. Every instruction belongs to exactly one basic block: the one begun by the most recent leader at or before it. The algorithm handles all control flow structures — conditionals, loops, switches — uniformly, because they all ultimately reduce to branch instructions whose targets and fall-throughs are leaders."
```

## Explainer

You already know that compilers translate source code into intermediate representations like three-address code (quadruples). But a flat list of instructions is hard to reason about for optimization — you need structure. A **basic block** is a maximal straight-line sequence of instructions where control flow enters only at the first instruction and exits only at the last. There are no jumps into the middle and no jumps out of the middle. If any instruction in the block executes, they all execute, in order.

The algorithm to identify basic blocks is straightforward. First, identify **leaders** — instructions that begin a new block. An instruction is a leader if it is the first instruction in the program, it is the target of any branch or jump, or it immediately follows a branch or jump. Each leader starts a new basic block that extends to (but does not include) the next leader. Applied to your intermediate representation, this partitioning transforms a flat instruction list into a structured collection of blocks, each with a single entry point and a single exit point.

Once you have basic blocks, you connect them to form the **control-flow graph** (CFG) you studied as a prerequisite. Each block becomes a node. An edge from block A to block B means that after A's last instruction executes, control might flow to B — either through a fall-through (sequential execution) or an explicit branch. The CFG is the foundational data structure for nearly every compiler optimization and analysis: liveness analysis, reaching definitions, dominance, and loop detection all operate on the CFG rather than on raw instruction lists.

Within a single basic block, optimization is relatively simple because execution is guaranteed to be sequential. **Local optimizations** like common subexpression elimination, constant folding, and dead code elimination can be applied within a block by analyzing instruction dependencies without worrying about control flow. The real power comes when you combine basic block structure with the CFG to perform **global optimizations** — analyses that reason across block boundaries about how data flows through the entire function. Basic block identification is therefore the essential first step: it decomposes the complexity of a whole program into manageable pieces that can be analyzed both individually and in relation to each other.
