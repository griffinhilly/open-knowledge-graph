---
id: floyd-hoare-verification
title: Floyd-Hoare Verification
domain: computer-science
course: formal-methods
prerequisites:
- id: hoare-logic
  type: hard
- id: weakest-precondition
  type: hard
builds-toward:
- invariant-generation
- symbolic-execution
tags:
- verification-conditions
- program-proof
- floyd
- annotation
stage: expert
status: validated
---
# Floyd-Hoare Verification

## Core Idea
Floyd-Hoare verification is the practical methodology of proving program correctness by annotating code with logical assertions at every control point — preconditions, postconditions, and loop invariants — then generating and discharging verification conditions (VCs) that confirm each annotation is consistent with its neighbors. Robert Floyd's original method attached assertions to flowchart edges; Hoare formalized it for structured programs. Modern tools automate VC generation via weakest precondition computation and offload proof obligations to SMT solvers, making the approach scalable to real software.

## Questions

```yaml
- question: "What is a verification condition in the context of Floyd-Hoare verification?"
  type: multiple-choice
  options:
    - "A runtime check inserted into the program to detect violations"
    - "A logical formula derived from program annotations that, if valid, guarantees the program meets its specification"
    - "A type-checking constraint that ensures the program compiles"
    - "A test case that exercises a particular code path"
  answer: 1
  explanation: "Verification conditions are purely logical — they are formulas generated from the program's annotations (preconditions, postconditions, loop invariants) and the program's semantics. If every VC is valid (true in all states), the program is guaranteed correct with respect to its specification. VCs are checked statically by theorem provers or SMT solvers, not at runtime."

- question: "In Floyd-Hoare verification, the human must supply loop invariants because verification condition generation cannot automatically discover them."
  type: true-false
  answer: true
  explanation: "VC generation is mechanical: given annotations at every loop head and function boundary, the tool computes weakest preconditions backward and checks that each annotation implies what the next one requires. But finding the right loop invariant — an assertion strong enough to prove the postcondition yet weak enough to be preserved by every iteration — is undecidable in general and must be supplied by the programmer or inferred by heuristic tools."

- question: "A Floyd-Hoare proof of a 50-line function with 3 loops has all its verification conditions discharged by an SMT solver. What has been proven, and what has NOT been proven?"
  type: short-answer
  answer: "What is proven: the function meets its specification (postcondition follows from precondition) assuming the annotations are correct and the language semantics model is faithful. What is NOT proven: termination (unless separately argued with ranking functions), absence of undefined behavior outside the modeled semantics (e.g., stack overflow), or that the specification itself captures the intended behavior."
  explanation: "Floyd-Hoare verification is relative verification — it proves the program correct relative to its specification and its semantic model. If the specification is wrong (says the wrong thing about what the function should do) or the semantic model omits important behavior (like integer overflow in C), the proof does not catch those errors. This is why formal methods practitioners emphasize getting the specification right as the hardest and most valuable part of the process."
```

## Explainer

Floyd-Hoare verification combines the theoretical machinery of Hoare logic and weakest preconditions into a practical workflow for proving programs correct. The idea is straightforward: annotate the program with logical assertions at strategic points, then mechanically verify that the assertions are mutually consistent. If they are, the program provably satisfies its specification.

The process begins with the programmer providing three kinds of annotations. **Function contracts** specify preconditions and postconditions for each procedure. **Loop invariants** describe what holds at the beginning of each loop iteration. **Intermediate assertions** (optional) can help guide the proof at complex points. Given these annotations, the verification tool generates **verification conditions** — logical formulas whose validity implies the program's correctness. For straight-line code between two annotations, the tool computes the weakest precondition of the later annotation backward through the statements and checks that the earlier annotation implies it.

The key insight is that annotations at loop heads and function boundaries **cut** the program into acyclic fragments. Each fragment is a straight-line or branching sequence of statements bookended by human-supplied assertions. Within each fragment, weakest precondition computation is entirely mechanical. The resulting VCs are first-order logic formulas (often in the theory of arithmetic, arrays, or bitvectors) that can be discharged by SMT solvers like Z3, CVC5, or Alt-Ergo. When a VC fails, the tool reports a counterexample — a concrete state showing how the annotation can be violated — guiding the programmer to fix the invariant or the code.

Modern verification systems like **Dafny**, **SPARK/Ada**, **Frama-C/WP**, and **Why3** implement this workflow end-to-end. The programmer writes code with annotations in a specification language, the tool generates VCs automatically, and backend SMT solvers discharge them. The human effort concentrates on writing correct specifications and discovering loop invariants — the genuinely creative parts. Everything else is automated. This division of labor has made Floyd-Hoare verification practical for safety-critical software in aerospace, automotive, and security-sensitive domains.

It is important to understand the limits of what a successful verification proves. The proof is **relative**: it shows the program meets its specification, assuming the semantic model accurately captures the programming language's behavior. If the specification is incomplete (says nothing about a particular error case) or the model is unfaithful (ignores machine-level overflow), bugs can survive verification. Getting the specification right — ensuring it captures what you actually want the program to do — is widely considered the most valuable and most difficult part of formal verification, often revealing design errors before a single line of proof is attempted.
