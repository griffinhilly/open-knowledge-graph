---
id: program-synthesis
title: Program Synthesis
domain: computer-science
course: formal-methods
prerequisites:
- id: propositional-logic-introduction
  type: hard
- id: type-systems-overview
  type: soft
- id: model-checking-intro
  type: soft
builds-toward: []
tags:
- synthesis
- sketching
- cegis
- sygus
- oracle-guided
- specification
stage: expert
status: validated
---
# Program Synthesis

## Core Idea
Program synthesis automatically generates a program that meets a given specification. The specification can take many forms: logical formulas, input-output examples, natural language, or a reference implementation. The synthesis engine searches the space of possible programs for one that satisfies all constraints. Key approaches include enumerative search (try programs in order of size), constraint-based synthesis (encode the problem as a SAT/SMT query), and counterexample-guided inductive synthesis (CEGIS), which iterates between proposing candidate programs and checking them against the specification. Program synthesis inverts the verification problem: instead of checking whether a given program meets a spec, it finds a program that does.

## Questions

```yaml
- question: "How does counterexample-guided inductive synthesis (CEGIS) differ from exhaustive enumerative search?"
  type: multiple-choice
  options:
    - "CEGIS only works for hardware, while enumerative search works for software"
    - "CEGIS iterates between a synthesizer that proposes candidates from a finite set of examples and a verifier that checks candidates against the full specification, using counterexamples from failed checks to refine future proposals. Enumerative search tries all programs of increasing size and checks each against the full specification directly"
    - "CEGIS is less precise than enumerative search"
    - "Enumerative search uses machine learning while CEGIS uses logic"
  answer: 1
  explanation: "CEGIS has two phases per iteration: the synthesizer finds a program consistent with the current set of examples (a smaller, easier problem than meeting the full spec), and the verifier checks the candidate against the complete specification. If the candidate fails, the verifier produces a counterexample that is added to the example set, and the synthesizer tries again. This is typically much faster than enumerating all programs because the synthesizer solves a smaller problem (satisfy known examples) and the verifier prunes the search space with targeted counterexamples."

- question: "Program synthesis from input-output examples alone risks overfitting — producing a program that works on the given examples but fails on unseen inputs."
  type: true-false
  answer: true
  explanation: "With only examples as specification, there are infinitely many programs consistent with any finite set of examples (e.g., a lookup table that returns the right output for each example and garbage otherwise). Synthesis tools mitigate this by searching for the simplest program (Occam's razor via bounded search) or by combining examples with additional constraints (types, templates, or partial logical specs). CEGIS addresses this by using a verifier with access to the full specification to check proposed solutions against all inputs, not just the examples."

- question: "Explain how program synthesis relates to program verification, and why synthesis is sometimes described as 'the inverse of verification.'"
  type: short-answer
  answer: "Verification asks: given a program P and specification S, does P satisfy S? Synthesis asks: given a specification S, find a program P that satisfies S. Synthesis inverts the relationship — the program is the unknown. Many synthesis techniques use verification as a subroutine: CEGIS proposes a candidate program and then VERIFIES it against the specification. If verification fails (counterexample), the synthesis loop refines its search. The two problems are deeply connected — advances in verification (SMT solving, model checking) directly enable more powerful synthesis."
  explanation: "This connection is why formal methods expertise is prerequisite to understanding synthesis. The specification languages (temporal logic, pre/postconditions, types with refinements) come from verification. The checking algorithms (SMT solving, model checking) come from verification. Synthesis adds the search component: how to efficiently explore the space of programs to find one that passes verification. The SyGuS (Syntax-Guided Synthesis) framework formalizes this by combining a logical specification with a syntactic grammar constraining the search space."
```

## Explainer

**Program synthesis** is the automated construction of programs from specifications. Where verification asks "does this program meet this spec?", synthesis asks "find me a program that meets this spec." The specification constrains the desired behavior — it might be a logical formula (for all inputs x, output f(x) satisfies P(x, f(x))), a set of input-output examples ({(1,1), (2,4), (3,9)} suggesting squaring), a reference implementation to optimize, or even a natural language description. The synthesis engine's job is to search the space of possible programs and find one that satisfies all constraints.

The challenge is that the space of programs is astronomically large and mostly filled with incorrect candidates. **Enumerative search** tries programs in order of increasing size, checking each against the specification. This is complete (it will eventually find a solution if one exists) but slow. **Constraint-based synthesis** encodes the search as a SAT or SMT problem: represent the unknown program symbolically, express the specification as constraints, and let a solver find a satisfying assignment. This can be very effective for small programs but the encoding size grows with program complexity.

**CEGIS** (Counterexample-Guided Inductive Synthesis), introduced by Solar-Lezama, combines the best of both approaches. It maintains a set of concrete input-output examples and iterates two phases. The **synthesis phase** finds a program consistent with the current examples — a smaller, easier problem than meeting the full specification. The **verification phase** checks the candidate against the complete specification using a verification tool (SMT solver, model checker). If the candidate passes, synthesis succeeds. If it fails, the verifier produces a **counterexample** — a specific input where the candidate misbehaves — which is added to the example set, and the cycle repeats. Each counterexample prunes a large swath of the search space, making convergence fast in practice.

The **SyGuS** (Syntax-Guided Synthesis) framework standardizes the synthesis problem. A SyGuS instance consists of a **background theory** (defining the semantics of operations), a **syntactic grammar** (defining the space of candidate programs), and a **semantic specification** (defining the desired behavior). The grammar is crucial: by restricting the search space to programs constructable from specific operators and patterns, it makes synthesis tractable. SyGuS competitions benchmark synthesis tools on standard problems, driving advances in the field.

Practical applications include **programming by example** (Excel's FlashFill, which synthesizes string transformations from examples), **superoptimization** (finding the shortest instruction sequence equivalent to a given program fragment), **protocol synthesis** (generating distributed protocols from high-level specifications), and **program repair** (synthesizing patches that fix bugs while preserving correct behavior). The connection to **machine learning** is growing: neural-guided synthesis uses learned models to prioritize which programs to try, combining the generalization of ML with the correctness guarantees of formal verification.
