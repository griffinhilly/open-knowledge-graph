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
- register-allocation
- code-generation
tags:
- code-generation
- backend
- instruction-selection
stage: advanced
status: validated
---

# Instruction Selection Techniques

## Core Idea
Instruction selection translates intermediate code into target machine instructions. One IR operation may correspond to many possible machine instructions, each with different costs and constraints. Pattern matching or dynamic programming finds good instruction sequences.

## How It's Best Learned
Implement pattern-based instruction selection for a real ISA subset. Write patterns as tree rules and test on realistic code.

## Questions

```yaml
- question: "A compiler backend uses macro expansion: each IR operation maps directly to one fixed machine instruction. The target architecture has a single 'load-and-add' instruction that loads from memory and adds to a register in one cycle. What will the macro expansion backend do?"
  type: multiple-choice
  options:
    - "Automatically recognize the opportunity and emit the load-and-add instruction when the pattern appears"
    - "Emit a separate LOAD followed by a separate ADD, missing the opportunity to use the combined instruction"
    - "Produce the same output as tree pattern matching since the semantics are equivalent"
    - "Emit a load-and-add only if the IR was explicitly annotated to request it"
  answer: 1
  explanation: "Macro expansion maps each IR instruction to a fixed template in isolation, so it can't recognize patterns that span multiple IR nodes. The load-and-add instruction corresponds to a two-node subtree (add whose child is a load), but macro expansion sees only one IR node at a time. Tree pattern matching exists precisely to exploit these combined instructions by covering multi-node IR subtrees with single machine instructions."

- question: "Why does the optimal instruction selection problem become NP-hard in general when the IR is a DAG rather than a tree?"
  type: multiple-choice
  options:
    - "DAGs have exponentially more nodes than equivalent trees, making pattern enumeration infeasible"
    - "Common subexpressions share nodes that could be covered by multiple overlapping patterns; choosing the globally optimal assignment is computationally intractable in general"
    - "Dynamic programming cannot process directed graphs, eliminating the efficient algorithm available for trees"
    - "Machine instruction sets are too large for the DAG case to enumerate all possible coverings"
  answer: 1
  explanation: "In a tree, each node has exactly one parent, so pattern choices at each node interact only with their subtree. In a DAG, a shared node (common subexpression) can be reached from multiple places. A pattern covering that node affects the cost of covering every path through it. Optimizing these interdependent choices globally is NP-hard, unlike the tree case where dynamic programming produces an optimal linear-time solution."

- question: "Optimal tree-tiling instruction selection can be solved in linear time using dynamic programming, but the analogous problem for DAGs is NP-hard in general."
  type: true-false
  answer: true
  explanation: "For trees, dynamic programming works bottom-up: at each node, it considers all patterns whose root matches that node, computes the cost as the pattern's cost plus the optimal costs of the uncovered subtrees, and picks the minimum. This is O(n) in the tree size. For DAGs, shared nodes create interdependencies between covering decisions that the bottom-up algorithm can't handle optimally without exponential enumeration. Practical compilers handle this via heuristics like decomposing DAGs into trees."

- question: "The goal of instruction selection is to minimize the total number of machine instructions emitted, since fewer instructions usually means faster execution."
  type: true-false
  answer: false
  explanation: "The goal is to minimize total cost, not instruction count. Instructions have different costs—some take one cycle, others take many; some are compact, others occupy more code space. A single complex instruction (like load-and-add) can replace two simpler instructions and cost less in total even though it 'counts' as one. Equally, sometimes emitting slightly more instructions that use cheap, fast operations produces better code than fewer expensive ones. The tree-tiling algorithm minimizes cost based on a cost model assigned to each pattern."

- question: "What is 'tree tiling' in instruction selection, and why does it produce better code than simple macro expansion?"
  type: short-answer
  answer: "Tree tiling is the process of covering an IR expression tree with a set of non-overlapping pattern templates, where each pattern corresponds to one machine instruction that implements the semantics of a subtree. The algorithm finds the minimum-cost set of patterns that covers every node in the tree. It produces better code than macro expansion because it can use complex instructions that span multiple IR nodes—such as a single 'load-and-add' that implements a two-node add-over-load subtree—rather than emitting one instruction per IR node in isolation. Dynamic programming solves the optimal tiling for trees in linear time by computing, bottom-up at each node, the minimum-cost pattern assignment that covers the subtree rooted there."
  explanation: "The key insight is that the IR-to-machine mapping is not one-to-one: a single IR subtree can often be implemented by several different machine instruction sequences with different costs, and modern architectures have complex instructions specifically designed to exploit common patterns. Macro expansion ignores this by collapsing each IR node independently; tree tiling exploits it by considering the structure of the entire expression."
```

## Explainer

After the compiler's front end and middle end have parsed, type-checked, and optimized the program, the code generation phase must translate the compiler's intermediate representation into actual machine instructions. You already know from studying code generation that this involves mapping IR operations to target architecture instructions. But this mapping is not one-to-one: a single IR operation like "add a variable to a constant" might be implementable by several different machine instructions, each with different costs, register constraints, and addressing modes. **Instruction selection** is the process of choosing which machine instructions to emit, and choosing well can significantly affect the speed and size of the generated code.

The simplest approach is **macro expansion**: each IR instruction maps to a fixed template of machine instructions. An IR add becomes a machine ADD, an IR load becomes a machine LOAD, and so on. This is easy to implement but produces poor code because it cannot exploit complex instructions that combine multiple operations. For example, many architectures have a "load-and-add" instruction that loads a value from memory and adds it to a register in one step. Macro expansion would emit a separate load followed by a separate add, missing the opportunity to use the combined instruction that is faster and more compact.

**Tree pattern matching** is the standard technique for better instruction selection. The compiler represents each IR expression as a tree — an addition node with two children, one of which might be a memory load. Machine instructions are described as **tree patterns**: each pattern covers a subtree of the IR and specifies the machine instruction that implements it. A pattern for "load-and-add" covers a tree with an add node whose right child is a load node. The instruction selector finds a set of non-overlapping patterns that **tiles** the entire IR tree with minimum total cost. This is essentially a covering problem: which combination of patterns covers every node in the tree at the lowest cost?

For tree-shaped IR, **dynamic programming** solves this optimally. The algorithm works bottom-up: at each node, it considers every pattern whose root matches that node, computes the cost as the pattern's own cost plus the optimal costs of the subtrees not covered by the pattern, and selects the minimum. This produces an optimal tiling in linear time with respect to the tree size. When the IR is a **DAG** (directed acyclic graph) rather than a tree — because common subexpressions share nodes — the problem becomes NP-hard in general, but heuristics like decomposing the DAG into trees or using greedy selection work well in practice. The quality of instruction selection depends heavily on having a comprehensive set of patterns that exploit the target architecture's instruction set, which is why compiler backends for complex architectures like x86 contain thousands of selection rules.
