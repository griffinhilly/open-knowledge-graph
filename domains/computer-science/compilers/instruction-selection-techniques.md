---
id: instruction-selection-techniques
title: Instruction Selection Techniques
domain: computer-science
course: compilers
prerequisites:
- id: code-generation
  type: hard
- id: procedure-inlining-optimization
  type: soft
- id: array-subscript-optimization
  type: soft
builds-toward:
- graph-coloring-register-allocation
- code-emission-target-generation
tags:
- code-generation
- backend
- instruction-selection
stage: advanced
status: draft
---

# Instruction Selection Techniques

## Core Idea
Instruction selection translates intermediate code into target machine instructions. One IR operation may correspond to many possible machine instructions, each with different costs and constraints. Pattern matching or dynamic programming finds good instruction sequences.

## How It's Best Learned
Implement pattern-based instruction selection for a real ISA subset. Write patterns as tree rules and test on realistic code.

## Explainer

After the compiler's front end and middle end have parsed, type-checked, and optimized the program, the code generation phase must translate the compiler's intermediate representation into actual machine instructions. You already know from studying code generation that this involves mapping IR operations to target architecture instructions. But this mapping is not one-to-one: a single IR operation like "add a variable to a constant" might be implementable by several different machine instructions, each with different costs, register constraints, and addressing modes. **Instruction selection** is the process of choosing which machine instructions to emit, and choosing well can significantly affect the speed and size of the generated code.

The simplest approach is **macro expansion**: each IR instruction maps to a fixed template of machine instructions. An IR add becomes a machine ADD, an IR load becomes a machine LOAD, and so on. This is easy to implement but produces poor code because it cannot exploit complex instructions that combine multiple operations. For example, many architectures have a "load-and-add" instruction that loads a value from memory and adds it to a register in one step. Macro expansion would emit a separate load followed by a separate add, missing the opportunity to use the combined instruction that is faster and more compact.

**Tree pattern matching** is the standard technique for better instruction selection. The compiler represents each IR expression as a tree — an addition node with two children, one of which might be a memory load. Machine instructions are described as **tree patterns**: each pattern covers a subtree of the IR and specifies the machine instruction that implements it. A pattern for "load-and-add" covers a tree with an add node whose right child is a load node. The instruction selector finds a set of non-overlapping patterns that **tiles** the entire IR tree with minimum total cost. This is essentially a covering problem: which combination of patterns covers every node in the tree at the lowest cost?

For tree-shaped IR, **dynamic programming** solves this optimally. The algorithm works bottom-up: at each node, it considers every pattern whose root matches that node, computes the cost as the pattern's own cost plus the optimal costs of the subtrees not covered by the pattern, and selects the minimum. This produces an optimal tiling in linear time with respect to the tree size. When the IR is a **DAG** (directed acyclic graph) rather than a tree — because common subexpressions share nodes — the problem becomes NP-hard in general, but heuristics like decomposing the DAG into trees or using greedy selection work well in practice. The quality of instruction selection depends heavily on having a comprehensive set of patterns that exploit the target architecture's instruction set, which is why compiler backends for complex architectures like x86 contain thousands of selection rules.
