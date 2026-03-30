---
id: interactive-theorem-proving
title: Interactive Theorem Proving
domain: computer-science
course: formal-methods
prerequisites:
- id: predicate-logic
  type: hard
- id: type-systems-type-checking
  type: soft
- id: curry-howard-correspondence
  type: soft
builds-toward:
- dependent-type-theory
tags:
- proof-assistant
- coq
- isabelle
- lean
- agda
- machine-checked-proof
stage: expert
status: validated
---
# Interactive Theorem Proving

## Core Idea
Interactive theorem proving uses software tools (proof assistants) in which humans construct formal proofs with machine verification of every step. The user states a theorem in a formal logic, then builds the proof interactively — applying tactics, introducing lemmas, and guiding the proof search — while the proof assistant checks that each step is logically valid. The result is a machine-checked proof: a certificate that the theorem follows from the axioms with absolute certainty. Major proof assistants include Coq (based on the Calculus of Inductive Constructions), Isabelle/HOL (based on higher-order logic), Lean (dependent type theory with strong automation), and Agda (dependently-typed programming language doubling as a proof assistant).

## Questions

```yaml
- question: "What distinguishes a machine-checked proof in Coq from an informal mathematical proof?"
  type: multiple-choice
  options:
    - "Machine-checked proofs are shorter and easier to read"
    - "Every logical step is verified by a small trusted kernel, making the proof's correctness independent of the user's reasoning ability. Informal proofs rely on the reader's judgment to assess whether each step is valid"
    - "Machine-checked proofs can prove statements that informal proofs cannot"
    - "Machine-checked proofs are generated automatically without human input"
  answer: 1
  explanation: "The key property is the trusted kernel: the proof assistant has a small core type-checker (a few thousand lines) that validates every proof step. The user can make mistakes, use dubious heuristics, or employ powerful automation — but the kernel will only accept the proof if every step is logically justified. This gives much stronger assurance than informal proofs, where a single oversight in a complex argument can invalidate the entire proof. The tradeoff is the effort to formalize: machine-checked proofs are typically 5-20x longer than informal ones."

- question: "The CompCert verified C compiler guarantees that the compiled machine code has the same observable behavior as the source C program. This was proven using which proof assistant?"
  type: multiple-choice
  options:
    - "Lean"
    - "Coq"
    - "Isabelle/HOL"
    - "Agda"
  answer: 1
  explanation: "CompCert, developed by Xavier Leroy, is a C compiler where every optimization pass is formally verified in Coq to preserve program semantics. The machine-checked proof guarantees that any behavior of the compiled code is a valid behavior of the source program — miscompilation bugs are impossible (within the modeled subset of C). This is a landmark achievement in formal methods: a production-quality compiler with end-to-end correctness guarantees."

- question: "Why do proof assistants use a small trusted kernel rather than trusting the entire tool, and what is the practical implication of this design?"
  type: short-answer
  answer: "The kernel is the only code that needs to be correct for the proofs to be valid. A small kernel (typically a few thousand lines) can be audited, tested, and formally analyzed. The rest of the proof assistant — tactics, automation, user interface, libraries — can be arbitrarily complex because anything they produce is re-checked by the kernel. If a tactic generates a wrong proof step, the kernel rejects it. This design, called the 'de Bruijn criterion,' minimizes the trusted computing base."
  explanation: "This is analogous to the principle of least privilege in security. By concentrating trust in a small, well-understood component, the overall system achieves high assurance despite its complexity. Coq's kernel is about 10,000 lines of OCaml. All of Coq's sophisticated tactic language, automation, and standard library depend on this kernel for soundness. If the kernel has no bugs (and it has been very thoroughly tested), then every proof Coq accepts is valid."

- question: "Interactive theorem proving cannot be fully automated for interesting theorems because the underlying logic is undecidable."
  type: true-false
  answer: true
  explanation: "Proof assistants typically use logics (higher-order logic, dependent type theory) in which validity is undecidable — there is no algorithm that can determine whether an arbitrary statement is provable. This is why the process is 'interactive': the human provides the creative insights (proof strategy, key lemmas, case splits) and the machine verifies each step. Automation (SAT/SMT solvers, decision procedures, proof search tactics) handles routine obligations, but non-trivial theorems require human guidance. The division of labor — human creativity, machine rigor — is the essence of interactive theorem proving."
```

## Explainer

An informal mathematical proof convinces a human reader that a theorem is true. But human readers make mistakes — they may accept a flawed argument because it "looks right" or skip a tedious case analysis. **Interactive theorem proving** raises the bar: the proof must convince a computer, which checks every logical step mechanically against a fixed set of axioms and inference rules. The result is a **machine-checked proof** — a formal object that can be independently verified by anyone who trusts the proof assistant's kernel (typically a few thousand lines of code).

The workflow is fundamentally interactive. The user states a theorem in the proof assistant's formal language, producing a **goal** — a statement to be proved. The user then applies **tactics** (proof commands) that transform the goal into simpler subgoals. A tactic might split a conjunction into two subgoals, apply an induction principle, rewrite using a known equality, or invoke an automated decision procedure. Each tactic application is checked by the kernel: it must produce valid proof steps or be rejected. The process continues until all subgoals are discharged. The resulting proof term is a complete formal derivation, independent of the tactic scripts that generated it.

The major proof assistants differ in their foundational logics. **Coq** uses the Calculus of Inductive Constructions (CIC), a dependent type theory where propositions are types and proofs are programs — a direct implementation of the Curry-Howard correspondence. **Isabelle/HOL** uses classical higher-order logic, which is more familiar to working mathematicians and supports automation well (the Sledgehammer tactic calls external SMT solvers). **Lean** uses a dependent type theory similar to Coq's but emphasizes usability, metaprogramming, and strong automation; it has attracted significant mathematical formalization effort (Mathlib). **Agda** is a dependently-typed programming language where proofs are written as programs, emphasizing direct term construction over tactic-based proof.

The practical impact of interactive theorem proving has grown dramatically. **CompCert** (a verified C compiler in Coq) guarantees that compiled code faithfully reflects source semantics. **seL4** (a verified microkernel in Isabelle/HOL) guarantees functional correctness and security properties of an operating system kernel. **The Feit-Thompson Theorem** and the **Kepler Conjecture** (Flyspeck project) have been formally verified, demonstrating that proof assistants can handle deep mathematics. The **Four Color Theorem** was verified in Coq, resolving concerns about the computer-assisted portions of the original proof.

The main barrier to broader adoption is the effort required to formalize proofs. Machine-checked proofs are typically 5-20 times longer than their informal counterparts because every implicit step, every appeal to "obviously," every routine calculation must be made explicit. This overhead is decreasing as automation improves — modern proof assistants can discharge many routine obligations automatically using SMT integration, rewriting engines, and proof search. The emerging pattern is **human-guided, machine-verified** development: the human provides the high-level proof strategy and key insights, automation handles the mechanical details, and the kernel guarantees correctness of the final result.
