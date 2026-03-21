---
id: data-dependence-analysis
title: Data Dependence Analysis
domain: computer-science
course: compilers
prerequisites:
- id: basic-block-analysis
  type: hard
- id: dataflow-analysis
  type: hard
builds-toward:
- use-definition-chains
- loop-detection-analysis
tags:
- analysis
- data-flow
- dependencies
stage: advanced
status: draft
---

# Data Dependence Analysis

## Core Idea
Data dependence analysis determines which instructions depend on results from earlier instructions. Dependencies include true dependencies (a use depends on a write), anti-dependencies (a write depends on an earlier read), and output dependencies. Understanding dependencies is essential for safe code motion and parallelization.

## How It's Best Learned
Compute data dependence sets for small programs and draw dependence graphs. Understand how dependences limit parallelization.

## Common Misconceptions
All dependencies must be respected (anti and output dependencies can often be eliminated through renaming). Dependence analysis only matters for parallelization (it affects all optimizations that move code).

## Questions

```yaml
- question: "Consider this code fragment: (1) x = a + b; (2) y = x * 2; (3) x = c - d. What type of dependence exists between instruction (2) and instruction (3)?"
  type: multiple-choice
  options:
    - "True dependence: instruction (3) reads a value written by instruction (2)"
    - "Anti-dependence (write-after-read): instruction (2) reads x before instruction (3) writes x"
    - "Output dependence (write-after-write): both instructions write to the same variable"
    - "No dependence: instructions (2) and (3) use different variables"
  answer: 1
  explanation: "Instruction (2) reads x (written by instruction (1)), and instruction (3) later writes to x. This is an anti-dependence (write-after-read): if we reordered and put instruction (3) before instruction (2), then (2) would read the new value of x (c − d) instead of the intended value (a + b), producing a wrong result. Anti-dependencies arise from name reuse — x is being used for two different purposes. They can be eliminated by renaming: if instruction (3) wrote to a new variable x2 instead, the dependence disappears entirely."

- question: "A compiler wants to parallelize the loop: for (i=0; i<n; i++) { a[i] = a[i-1] + 1; }. Which statement is correct?"
  type: multiple-choice
  options:
    - "The loop can be fully parallelized because each iteration writes to a different array element"
    - "The loop has a loop-carried true dependence: iteration i reads a[i-1] which was written by iteration i-1"
    - "The loop has only an anti-dependence, which can be eliminated by renaming"
    - "The loop can be parallelized after applying register renaming to the array accesses"
  answer: 1
  explanation: "Each iteration i reads a[i-1], which was written by the previous iteration (i-1). This is a loop-carried *true dependence* (read-after-write across iterations): iteration i genuinely needs the result of iteration i-1 to compute its own value. Unlike name dependencies, this cannot be eliminated by renaming — the data flow is real. The iterations must execute sequentially in order. In contrast, a loop like `a[i] = b[i] + 1` has no loop-carried dependencies and can be parallelized freely."

- question: "Anti-dependencies (write-after-read) and output dependencies (write-after-write) can potentially be eliminated by renaming variables or registers, whereas true dependencies (read-after-write) cannot."
  type: true-false
  answer: true
  explanation: "Anti and output dependencies are 'name dependencies' — they arise because the same variable name or storage location is reused for different values, not because one instruction genuinely needs data produced by another. By introducing new names (SSA form in compilers, register renaming in hardware), each write targets a distinct location and the false dependence disappears. True dependencies cannot be eliminated by renaming because they represent actual data flow: instruction B genuinely requires the value computed by instruction A."

- question: "A true dependence between two instructions is a conservative approximation: the compiler may identify a true dependence even when the instructions could safely be reordered."
  type: true-false
  answer: false
  explanation: "True dependencies (read-after-write) represent genuine data flow constraints that cannot be removed. If instruction B reads a value that instruction A wrote, then A must complete before B reads — reordering would give B a wrong value. This is not a conservative approximation; it is an exact constraint. Conservative approximations arise in alias and pointer analysis, where the compiler may be uncertain whether two memory accesses refer to the same location. But a confirmed true dependence is a hard constraint, not an approximation."

- question: "Explain why anti-dependencies and output dependencies are called 'name dependencies,' and describe one technique compilers use to eliminate them."
  type: short-answer
  answer: "Anti-dependencies and output dependencies arise not from genuine data flow but from the reuse of a single variable name or storage location for different values. An anti-dependence occurs when one instruction reads a variable and a later instruction writes to it — the ordering constraint exists only because both instructions refer to the same name, not because the second instruction needs the first's result. An output dependence similarly arises when two instructions write to the same location. If each write were directed to a distinct location, both dependencies would vanish. Compilers eliminate name dependencies by transforming the program into Static Single Assignment (SSA) form, where each variable is defined exactly once — every write introduces a fresh name, so no two writes share a target."
  explanation: "This insight is also the basis of hardware register renaming, which allows out-of-order processors to exploit instruction-level parallelism by dynamically mapping architectural registers to a larger physical register file, eliminating false dependencies that would otherwise force sequential execution."
```

## Explainer

From basic block analysis and dataflow analysis, you know how to trace values through a program's control flow graph. Data dependence analysis takes this further by asking a precise question: for any two instructions, does the order in which they execute matter? If instruction B reads a value that instruction A writes, then A must execute before B — reordering them would give B the wrong value. This relationship is called a **true dependence** (also called a flow dependence or read-after-write), and it represents a genuine constraint that no optimization can eliminate. If you compute `x = a + b` on line 3 and use `y = x * 2` on line 7, the multiplication truly depends on the addition.

Two other kinds of dependence are less fundamental but equally important to get right. An **anti-dependence** (write-after-read) occurs when instruction A reads a variable and later instruction B writes to it — B must not execute before A finishes reading the old value. An **output dependence** (write-after-write) occurs when two instructions write to the same variable — their order determines which value persists. Unlike true dependences, anti and output dependences are **name dependences**: they arise not from genuine data flow but from the reuse of variable names or storage locations. If you renamed the variable so that each write targets a distinct location, these dependences vanish. This insight is the basis of register renaming in hardware and SSA form in compilers.

The practical output of dependence analysis is a **dependence graph**, where nodes are instructions and directed edges represent dependences. An edge from A to B labeled with the dependence type means "A must execute before B." Any valid reordering of instructions must respect every edge in this graph — it must be a topological order. Instructions with no path between them in the dependence graph are independent and can safely execute in parallel or be reordered freely. This directly enables optimizations like instruction scheduling (reorder instructions to fill pipeline stalls), loop parallelization (execute independent iterations simultaneously), and code motion (move an instruction out of a loop if no dependence prevents it).

For loops, dependence analysis becomes especially powerful and subtle. A **loop-carried dependence** exists when an instruction in iteration i depends on a result from iteration i−1 (or earlier). The classic example is `a[i] = a[i-1] + 1` — each iteration reads the value written by the previous one, creating a chain that prevents parallel execution. In contrast, `a[i] = b[i] + 1` has no loop-carried dependence, so all iterations can run in parallel. Determining whether array accesses in a loop create dependences requires solving systems of integer constraints (like the GCD test or the Banerjee test), connecting dependence analysis to the integer arithmetic you encountered in earlier compiler topics.
