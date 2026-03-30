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
stage: expert
status: validated
---

# Partial Evaluation and Program Specialization

## Core Idea
Partial evaluation specializes a program by pre-computing it with known inputs, eliminating branches and loops whose conditions are statically determinable. The result is more efficient code tailored to those inputs, useful for generating fast versions of generic code.

## Questions

```yaml
- question: "A partial evaluator is given an interpreter for a small language and a specific program written in that language. The program text is treated as a static (known) input. What does the output of the partial evaluator represent?"
  type: multiple-choice
  options:
    - "An optimized version of the interpreter with dead code eliminated"
    - "A compiled version of the specific program — the interpreter's dispatch logic has been specialized away"
    - "A new interpreter that runs the same program faster by caching results"
    - "A proof that the interpreter correctly implements the language semantics"
  answer: 1
  explanation: "This is the first Futamura projection: partially evaluating an interpreter with respect to a specific program produces a compiled version of that program. The interpreter's parsing overhead, dispatch tables, and runtime branching — all of which are driven by the program text, a static input — are eliminated during specialization. What remains is only the sequence of operations the specific program actually performs, with no interpreter overhead. This shows that partial evaluation is powerful enough to derive compilers from interpreters automatically, without writing a compiler by hand."

- question: "A partial evaluator is applied to a generic image-processing function with a static kernel size of 3×3. Instead of a compact specialized function, the output is thousands of lines of unrolled code. What phenomenon explains this?"
  type: multiple-choice
  options:
    - "The partial evaluator made a logic error and must be rerun"
    - "Code explosion — aggressive unfolding of a small static input produced an oversized residual program"
    - "The function contained dynamic inputs that were incorrectly treated as static"
    - "Binding-time analysis failed to classify any variables, so all code was duplicated"
  answer: 1
  explanation: "Code explosion occurs when partial evaluation aggressively unfolds loops and function calls driven by static inputs, producing a residual program much larger than the original. Even a small kernel size can cause substantial unrolling if the specialization recursively inlines multiple levels of function calls. This is why binding-time analysis is essential: it identifies which computations are static and limits specialization to avoid producing unmanageably large code. Without this analysis, partial evaluation can make programs larger and slower."

- question: "Partial evaluation generalizes constant folding and dead code elimination by propagating known values through the entire program structure, including across function call boundaries."
  type: true-false
  answer: true
  explanation: "Constant folding replaces expressions like '3 + 4' with '7' locally. Partial evaluation extends this by following known values into function bodies, unrolling loops whose bounds are statically known, resolving conditionals whose conditions are static, and inlining calls where the arguments are known. This is a global, whole-program transformation, not a local peephole optimization. The result — the residual program — contains only computations that genuinely depend on the unknown inputs."

- question: "Partial evaluation typically produces a smaller, faster program than the original, making it a universally applicable optimization."
  type: true-false
  answer: false
  explanation: "Partial evaluation can cause code explosion — producing residual programs much larger than the original. If a generic function is specialized for multiple different static inputs, the result is many large specialized copies, potentially worse in code size and instruction-cache performance than the generic original. This is why practical partial evaluators use binding-time analysis to limit specialization, and why partial evaluation is most valuable in specific scenarios (interpreter specialization, tight inner loops with known parameters) rather than as a blanket optimization."

- question: "Explain what binding-time analysis does in partial evaluation and why it is necessary."
  type: short-answer
  answer: "Binding-time analysis is a preprocessing phase that classifies every variable and expression in the program as either static (its value is known at specialization time) or dynamic (its value is only known at runtime). The partial evaluator then specializes only the static portions, leaving dynamic computations in the residual program. Without this analysis, the evaluator might attempt to specialize dynamic computations, causing infinite loops or code explosion."
  explanation: "Without binding-time analysis, partial evaluation lacks a stopping criterion. It might try to evaluate a dynamic expression by unfolding it indefinitely, looping forever, or might aggressively inline every function call, producing enormous residual code. The static/dynamic classification is a conservative approximation: anything that might be dynamic is marked dynamic. The analysis ensures specialization terminates and produces a residual program of manageable size. It also guides the programmer in annotating which inputs should be considered static, enabling targeted specialization."
```

## Explainer

Imagine a generic power function `pow(base, n)` that computes `base^n` using a loop. If the compiler knows at compile time that `n` is always 3, it can replace the entire loop with `base * base * base` — eliminating the loop control, the counter variable, and the branch. This is the essence of **partial evaluation**: given a program and some of its inputs, produce a specialized version of the program that "bakes in" those known values and only waits for the remaining unknown inputs.

From your understanding of intermediate representations and compiler phases, you can see where partial evaluation fits. The compiler already performs constant folding (replacing `3 + 4` with `7`) and dead code elimination (removing unreachable branches). Partial evaluation generalizes these ideas aggressively. Rather than simplifying individual expressions, it propagates known values through the entire program structure — unfolding function calls, resolving conditionals, and unrolling loops whose bounds are known. The result is a **residual program** that contains only the computations that genuinely depend on the unknown inputs.

A classic application is interpreter specialization. Suppose you have an interpreter for a small language and a specific program written in that language. The program text is a static input to the interpreter. Partially evaluating the interpreter with respect to that program produces a compiled version of the program — the interpreter's dispatch logic and parsing overhead are eliminated, leaving only the operations the program actually performs. This is known as the **first Futamura projection**, and it demonstrates that partial evaluation is powerful enough to derive compilers from interpreters automatically.

The challenge is controlling the specialization process. Aggressive unfolding can cause **code explosion** — a small generic function might produce an enormous specialized version if it is unfolded across many call sites with different static inputs. Practical partial evaluators use binding-time analysis to classify each variable and operation as either **static** (known at specialization time) or **dynamic** (only known at runtime), then specialize only the static parts. This analysis, performed as a preprocessing phase over the intermediate representation, ensures that specialization terminates and produces code of manageable size.
