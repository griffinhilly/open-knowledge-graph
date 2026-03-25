---
id: pspace-and-complexity-hierarchy
title: The Complexity Class Hierarchy
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: space-complexity-classes-formal
  type: hard
- id: cantor-diagonalization
  type: soft
- id: big-o-notation
  type: soft
- id: algorithm-complexity
  type: soft
- id: co-np
  type: soft
tags:
- complexity
- hierarchy
- PSPACE
- complexity-classes
- diagonalization
stage: advanced
status: validated
---
# The Complexity Class Hierarchy

## Core Idea
The major complexity classes form a hierarchy: L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE ⊆ EXPTIME. The time hierarchy theorem, proved by diagonalization, guarantees that strictly more time yields strictly more computational power: DTIME(n) ⊊ DTIME(n²). Similarly, the space hierarchy theorem shows DSPACE(log n) ⊊ DSPACE(n). It is proven that P ⊊ EXPTIME, so the hierarchy is strict overall, but the intermediate separations — P vs. NP, NP vs. PSPACE — remain open. The polynomial hierarchy extends NP with alternating quantifiers, analogous to the arithmetical hierarchy.

## How It's Best Learned
Study the hierarchy theorem proofs as applications of diagonalization — the same technique used for the halting problem. Then map out which containments are proven strict and which remain open, building an accurate picture of current knowledge.

## Common Misconceptions
- The complexity class hierarchy is not fully proven strict at every level; P ≠ NP and NP ≠ PSPACE are both unresolved.
- If P = NP were proven, the entire polynomial hierarchy would collapse to P, dramatically simplifying our picture of computational complexity.

## Questions

```yaml
- question: "Which containment in the standard complexity hierarchy is *proven to be strict* (not merely conjectured)?"
  type: multiple-choice
  options:
    - "P ⊊ NP — determinism is strictly weaker than nondeterminism in polynomial time"
    - "NP ⊊ PSPACE — polynomial time is strictly weaker than polynomial space"
    - "P ⊊ EXPTIME — polynomial time is strictly weaker than exponential time"
    - "PSPACE ⊊ EXPTIME — polynomial space is strictly weaker than exponential time"
  answer: 2
  explanation: "P ⊊ EXPTIME is proven strictly by the time hierarchy theorem via diagonalization: given exponentially more time, you can solve problems no polynomial-time machine can solve. P ≠ NP is the most famous open problem in computer science — unresolved. NP ⊊ PSPACE and PSPACE ⊊ EXPTIME are also not proven as strict containments at the intermediate level. The key insight is that we know the hierarchy is strict *overall* (P ⊊ EXPTIME) but the intermediate separations remain open."

- question: "A researcher proves P = NP. Which consequence follows for the polynomial hierarchy (PH)?"
  type: multiple-choice
  options:
    - "Only NP-complete problems become efficiently solvable; higher levels of PH are unaffected"
    - "The polynomial hierarchy collapses entirely to P — every level of PH becomes equivalent to P"
    - "PSPACE collapses to P as well, since PSPACE ⊆ EXP and EXP would now equal P"
    - "The result affects NP and co-NP only, leaving Σ₂ and higher intact"
  answer: 1
  explanation: "If P = NP, then since Σ₁ = NP = P, and Σ₂ = NP^NP = P^P = P, and by induction every level of PH collapses to P. This structural consequence is one reason researchers expect P ≠ NP: the polynomial hierarchy appears to be genuinely infinite with strictly more power at each level, and a P = NP proof would wipe out this entire structure. This argument is suggestive, not a proof of P ≠ NP."

- question: "It has been proven that P ≠ NP, establishing that nondeterminism provides a strict computational advantage over determinism in polynomial time."
  type: true-false
  answer: false
  explanation: "P ≠ NP is one of the most famous open problems in mathematics and computer science — it has NOT been proven. It is widely believed to be true (most complexity theorists expect P ≠ NP), but no proof exists. What IS proven is that P ⊊ EXPTIME (strict), so the hierarchy is not entirely flat. Confusing 'widely believed' with 'proven' is a common misconception in this area."

- question: "PSPACE contains NP as a subset: any problem solvable by a nondeterministic polynomial-time algorithm can also be solved using only polynomial space."
  type: true-false
  answer: true
  explanation: "This containment NP ⊆ PSPACE is proven. A nondeterministic polynomial-time algorithm can be simulated in polynomial space: enumerate and verify each nondeterministic branch one at a time, reusing space between branches. Since space can be reused across time steps but time cannot be reused across space, polynomial space is at least as powerful as nondeterministic polynomial time. Whether PSPACE = NP is a separate (and open) question."

- question: "The time hierarchy theorem proves P ⊊ EXPTIME using diagonalization. Explain why the same diagonalization argument does not directly prove P ≠ NP."
  type: short-answer
  answer: "The time hierarchy theorem works by constructing a machine D that runs in time T(n), simulates every polynomial-time machine, and deliberately differs from each one. For the P ⊊ EXPTIME proof, D has exponential time to simulate all polynomial-time machines — enough time to complete the simulation and flip the answer. The argument breaks for P vs. NP because NP uses nondeterminism. To diagonalize against all polynomial nondeterministic machines, D would need to simulate them deterministically — but that simulation requires potentially exponential time, blowing past D's polynomial budget. The argument 'runs out of time' before it can construct the separating language within P."
  explanation: "This is the technical barrier known as 'relativization' — naive diagonalization fails to separate P from NP because the simulation of NP machines does not fit in polynomial deterministic time. Proving P ≠ NP requires techniques that go beyond diagonalization, which is part of what makes it so difficult."
```

## Explainer

You already understand P and NP as the heart of the complexity landscape — P is what deterministic polynomial time can decide, NP is what nondeterminism adds. But these two classes sit inside a much richer landscape. Think of computational resources — time and space — as two different currencies. Using more of one can sometimes substitute for the other, and the **complexity hierarchy** maps out exactly which tradeoffs are possible and which boundaries are real.

**PSPACE** is the class of problems solvable with polynomial *space*, regardless of how long computation takes. Because space can be reused across time steps, PSPACE is potentially much larger than NP: a problem might require exponential time but only polynomial space to solve, since you can reuse the same memory cells for many different subcomputations. The canonical PSPACE-complete problem is TQBF (totally quantified Boolean formulas), which asks whether a formula with alternating universal and existential quantifiers is true — the same structure as adversarial games. This connects PSPACE to problems like determining the winner of a board game under optimal play.

Above PSPACE sits **EXPTIME** — problems solvable in exponential time — and we *do* know that P ⊊ EXPTIME is a strict containment. The proof uses **diagonalization**, the same technique you saw with Cantor and the halting problem. The time hierarchy theorem shows that given strictly more time, you can solve strictly more problems: DTIME(n^k) ⊊ DTIME(n^(k+1)) for all k. The argument constructs a language by diagonalizing against all machines running in time T(n), building a problem that deliberately answers differently from every such machine. Similarly, the space hierarchy theorem shows DSPACE(log n) ⊊ DSPACE(n).

The **polynomial hierarchy** (PH) extends NP with alternating quantifiers: Σ₁ = NP, Π₁ = co-NP, Σ₂ = NP^NP (NP with an NP oracle), and so on. This mirrors the arithmetical hierarchy you may know from logic. A key structural fact: if P = NP, then PH collapses to P — every level becomes equivalent. This is a reason (not a proof!) that P ≠ NP is expected: the polynomial hierarchy seems to be genuinely infinite. The current picture is: we know P ⊊ EXPTIME strictly, we know P ⊆ NP ⊆ PSPACE ⊆ EXPTIME, but the intermediate separations — P vs. NP, NP vs. PSPACE — remain among the deepest open problems in mathematics.
