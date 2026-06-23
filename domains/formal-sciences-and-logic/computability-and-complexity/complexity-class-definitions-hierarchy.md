---
id: complexity-class-definitions-hierarchy
title: Complexity Classes and the Complexity Hierarchy
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: time-complexity-classes-formal
  type: hard
- id: space-complexity-classes-formal
  type: hard
- id: algorithm-analysis-big-o
  type: soft
- id: algorithm-complexity
  type: hard
- id: co-np-and-complements
  type: soft
- id: randomized-complexity-rp-coerp
  type: soft
- id: computability-complexity-overview
  type: soft
builds-toward:
- p-versus-np
- polynomial-hierarchy
tags:
- complexity-classes
- hierarchy-theorem
- p-np-pspace
stage: advanced
status: validated
---
# Complexity Classes and the Complexity Hierarchy

## Core Idea
Complexity classes like P, NP, PSPACE, and EXPTIME group problems by the computational resources (time or space) required to solve them. The Hierarchy Theorem shows that these classes are strictly nested (e.g., P ⊆ NP ⊆ PSPACE ⊆ EXPTIME), with some containments proven and others (like P vs. NP) remaining famously open.

## How It's Best Learned
Study the hierarchy theorem proofs to understand how resource bounds create proper inclusions. Visualize complexity classes as concentric circles to internalize nestings.

## Common Misconceptions
- Confusing 'properly contained' with 'strictly separated by a provable gap.' Hierarchy theorems use resource separation, not problem difficulty.
- Assuming all inclusions are proven. P ⊆ NP is known; P = NP is open.

## Questions

```yaml
- question: "A student argues: 'The Time Hierarchy Theorem proves P ≠ NP, because it shows that giving a machine more time strictly increases what it can compute.' What is the flaw in this reasoning?"
  type: multiple-choice
  options:
    - "The Hierarchy Theorem does not show that more time helps — it proves time and space are equivalent"
    - "The Hierarchy Theorem proves proper nesting only when the time bound grows super-polynomially, but P and NP differ by at most a polynomial factor — a gap the diagonal argument cannot exploit"
    - "P and NP are not separated because the theorem only applies to space complexity, not time complexity"
    - "The reasoning is correct; the Hierarchy Theorem does prove P ≠ NP, though the formal proof has not been accepted"
  answer: 1
  explanation: "The Time Hierarchy Theorem proves DTIME(f(n)) ⊊ DTIME(g(n)) when g grows sufficiently faster than f — specifically, when the ratio g/f grows without bound. This gives P ⊊ EXPTIME (exponential is super-polynomially larger than polynomial). But P vs NP asks whether polynomial solvability equals polynomial verifiability — both sides of the question are polynomial classes. The diagonalizing machine constructed in the hierarchy proof must itself run in polynomial time, placing it inside P and defeating the construction. Known barriers (relativization, natural proofs, algebrization) formally explain why standard diagonal arguments cannot resolve P vs NP."

- question: "A new problem Q is discovered that can be solved using at most O(n³) space but has no known algorithm faster than exponential time. What can be correctly concluded?"
  type: multiple-choice
  options:
    - "Q is in P, because polynomial space implies polynomial time — the inclusions run in that direction"
    - "Q is in PSPACE and therefore also in EXPTIME; whether Q is also in P or NP is unknown"
    - "Q is in EXPTIME and therefore cannot be in PSPACE, since PSPACE and EXPTIME are disjoint"
    - "Q is NP-complete by definition, since it has no known polynomial-time solution"
  answer: 1
  explanation: "The inclusions go: P ⊆ NP ⊆ PSPACE ⊆ EXPTIME. A problem solvable in polynomial space is automatically in PSPACE, and since PSPACE ⊆ EXPTIME, it is also in EXPTIME — consistent with having no known polynomial-time algorithm. Whether Q is also in P or NP is a separate question. NP-completeness is a specific property (every NP problem reduces to Q in polynomial time) that must be proven, not inferred from the absence of a fast algorithm. PSPACE and EXPTIME are not disjoint; PSPACE is a subset of EXPTIME."

- question: "The fact that P ⊆ NP is a proven theorem, but whether this inclusion is proper (P ⊊ NP, meaning there are problems in NP not in P) remains one of the most famous unsolved problems in mathematics."
  type: true-false
  answer: true
  explanation: "P ⊆ NP is trivial: any problem solvable in polynomial time can certainly be verified in polynomial time (just solve it and check). But whether NP contains problems that are genuinely harder to solve than to verify — i.e., whether P ⊊ NP — is the P vs NP question, one of the Millennium Prize Problems. The Hierarchy Theorem gives us P ⊊ EXPTIME, but the gap between P and NP is only polynomial, placing it outside the theorem's reach."

- question: "The Time Hierarchy Theorem proves P ≠ NP by showing there exist problems solvable in O(n²) time that can seldom be solved in O(n) time."
  type: true-false
  answer: false
  explanation: "The Time Hierarchy Theorem does show DTIME(n) ⊊ DTIME(n²) — a proper nesting within polynomial classes. But this proves only that linear and quadratic time are different, not that P ≠ NP. P vs NP is about whether *polynomial* time (all polynomials together) is different from *nondeterministic polynomial* verifiability. Both classes contain all polynomial-time computations, so showing linear ≠ quadratic within P says nothing about the P/NP boundary. The theorem's most significant separation is P ⊊ EXPTIME, not anything about NP."

- question: "What does the Time Hierarchy Theorem actually prove, and why is it insufficient to resolve P vs. NP?"
  type: short-answer
  answer: "The Time Hierarchy Theorem proves that DTIME(f(n)) is properly contained in DTIME(g(n)) when g grows sufficiently faster than f — for example, DTIME(n) ⊊ DTIME(n²) and, more significantly, P ⊊ EXPTIME. The proof is a diagonal argument: construct a machine M that on input ⟨T⟩ simulates machine T on ⟨T⟩ for the allowed time, then outputs the opposite. M is guaranteed to differ from every machine running within the tighter time bound, so it computes something genuinely new. This fails for P vs NP because any machine M that runs in polynomial time is itself inside P — making it a member of the class it was supposed to separate from NP. The diagonal construction collapses. Known barriers (relativization, natural proofs, algebrization) formalize exactly why every standard proof technique hits this wall for P vs NP."
  explanation: "Understanding why the theorem fails to resolve P vs NP is as important as understanding what it proves. It highlights that the P vs NP question has a fundamentally different structure — the two classes are separated by only a polynomial factor in resource, not a super-polynomial one, and that polynomial gap is exactly what makes the question hard."
```

## Explainer

You already know how to measure time and space complexity: a problem's time complexity is roughly how many steps the best algorithm takes as input grows, expressed in big-O notation, and you've studied formal resource bounds like DTIME(f(n)) and DSPACE(f(n)). **Complexity classes** are simply the collections of all decision problems solvable within some bound. **P** is the class of problems solvable in polynomial time — O(n^k) for some fixed k. **NP** is the class solvable in polynomial time on a nondeterministic Turing machine, equivalently, the class of problems whose solutions can be *verified* in polynomial time. Sorting is in P; given a proposed Hamiltonian cycle, you can check it in polynomial time, so the Hamiltonian cycle problem is in NP.

The hierarchy of classes P ⊆ NP ⊆ PSPACE ⊆ EXPTIME is an inclusion chain organized by resource. **PSPACE** groups problems solvable using polynomial *space* (but possibly exponential time), while **EXPTIME** groups those solvable in at most exponential time. The key insight is that using more resources can only help: a problem solvable in polynomial time is certainly solvable in polynomial space, because space can be reused across steps. This gives you the chain of inclusions for free — every problem in the smaller class is automatically a member of every larger class.

The **Time Hierarchy Theorem** and **Space Hierarchy Theorem** prove that the inclusions are *proper* when you jump by a sufficient factor. The Time Hierarchy Theorem says DTIME(n) ⊊ DTIME(n²) — there are problems solvable in quadratic time that cannot be solved in linear time. The proof is a diagonal argument in the tradition of Cantor and Turing: construct a machine that reads the description of other machines and deliberately differs from each in finite time, guaranteeing it computes a function none of them can. This gives you the guaranteed proper nesting: P ⊊ EXPTIME and PSPACE ⊊ EXPSPACE are both proven. The hierarchy theorems do *not*, however, resolve P vs. NP — diagonalization cannot separate classes that differ only by a polynomial factor without additional structure.

The famous open question — whether **P = NP** — asks if polynomial verifiability implies polynomial solvability. The question is hard precisely because every technique that would separate them (diagonalization, circuit lower bounds, natural proofs) has hit known barriers. What we *do* know is that if P ≠ NP, the class NP splits further: there are problems in NP that are neither in P nor NP-complete, a fact established by Ladner's theorem. The complexity hierarchy is thus not just a tower of inclusions but a landscape of problems clustered by difficulty, with P and EXPTIME as the two proven landmarks and NP as the central mystery between them.
