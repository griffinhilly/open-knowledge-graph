---
id: partial-evaluation-specialization
title: Partial Evaluation and Program Specialization
domain: computer-science
course: compilers
prerequisites:
- id: intermediate-code-representation
  type: hard
- id: compiler-phases-and-organization
  type: hard
builds-toward:
- multi-stage-programming
tags:
- specialization
- optimization
- meta
stage: advanced
status: draft
---

# Partial Evaluation and Program Specialization

## Core Idea
Partial evaluation specializes a program by pre-computing it with known inputs, eliminating branches and loops whose conditions are statically determinable. The result is more efficient code tailored to those inputs, useful for generating fast versions of generic code.

## Explainer

Imagine a generic power function `pow(base, n)` that computes `base^n` using a loop. If the compiler knows at compile time that `n` is always 3, it can replace the entire loop with `base * base * base` — eliminating the loop control, the counter variable, and the branch. This is the essence of **partial evaluation**: given a program and some of its inputs, produce a specialized version of the program that "bakes in" those known values and only waits for the remaining unknown inputs.

From your understanding of intermediate representations and compiler phases, you can see where partial evaluation fits. The compiler already performs constant folding (replacing `3 + 4` with `7`) and dead code elimination (removing unreachable branches). Partial evaluation generalizes these ideas aggressively. Rather than simplifying individual expressions, it propagates known values through the entire program structure — unfolding function calls, resolving conditionals, and unrolling loops whose bounds are known. The result is a **residual program** that contains only the computations that genuinely depend on the unknown inputs.

A classic application is interpreter specialization. Suppose you have an interpreter for a small language and a specific program written in that language. The program text is a static input to the interpreter. Partially evaluating the interpreter with respect to that program produces a compiled version of the program — the interpreter's dispatch logic and parsing overhead are eliminated, leaving only the operations the program actually performs. This is known as the **first Futamura projection**, and it demonstrates that partial evaluation is powerful enough to derive compilers from interpreters automatically.

The challenge is controlling the specialization process. Aggressive unfolding can cause **code explosion** — a small generic function might produce an enormous specialized version if it is unfolded across many call sites with different static inputs. Practical partial evaluators use binding-time analysis to classify each variable and operation as either **static** (known at specialization time) or **dynamic** (only known at runtime), then specialize only the static parts. This analysis, performed as a preprocessing phase over the intermediate representation, ensures that specialization terminates and produces code of manageable size.
