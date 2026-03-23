---
id: second-and-third-isomorphism-theorems
title: Second and Third Isomorphism Theorems
domain: mathematics
course: abstract-algebra
prerequisites:
- id: first-isomorphism-theorem-for-groups
  type: hard
tags:
- isomorphism-theorems
- subgroups
- structure
stage: advanced
status: validated
---

# Second and Third Isomorphism Theorems

## Core Idea
The second theorem: (S ∨ N)/N ≅ S/(S ∩ N) for S ≤ G and N ◁ G. The third: (G/M)/(N/M) ≅ G/N for M ⊆ N both normal. These theorems relate subgroup and quotient structures through isomorphisms.

## Questions

```yaml
- question: "Let G = ℤ₁₂, S = ⟨4⟩ = {0, 4, 8}, and N = ⟨6⟩ = {0, 6}. A student claims that (SN)/N must be isomorphic to S because 'S appears inside SN.' What does the Second Isomorphism Theorem actually say, and when would the student's conclusion fail in a different example?"
  type: multiple-choice
  options:
    - "(SN)/N ≅ S always, which confirms the student's claim for the right reason"
    - "(SN)/N ≅ S/(S ∩ N) — in this case S ∩ N = {0} so the conclusion holds, but the reason is wrong; when S ∩ N is non-trivial, (SN)/N is strictly smaller than S"
    - "(SN)/N ≅ N/(S ∩ N) — the theorem reverses the roles of S and N"
    - "The theorem doesn't apply here because S is not normal in G"
  answer: 1
  explanation: "The Second Isomorphism Theorem says (SN)/N ≅ S/(S ∩ N). Here S ∩ N = {0}, so S/(S ∩ N) ≅ S, making the student's conclusion accidentally correct. But the reason is wrong: N 'absorbs' the part of S overlapping with it, and the quotient reflects only the part of S outside N. If S ∩ N were non-trivial — say, a subgroup of order 2 — then (SN)/N would be strictly smaller than S."

- question: "The Third Isomorphism Theorem states that (G/M)/(N/M) ≅ G/N when M ⊆ N are both normal in G. Which of the following best captures the intuition behind this theorem?"
  type: multiple-choice
  options:
    - "Quotienting twice by different subgroups always produces a trivial group"
    - "The order of quotienting does not matter — G/N and N/M are interchangeable in any product"
    - "Quotienting first by M and then by N/M is equivalent to quotienting by N directly — a 'cancellation' analogous to fraction reduction"
    - "The theorem shows that every quotient group can be decomposed into exactly two smaller quotient groups"
  answer: 2
  explanation: "The Third Isomorphism Theorem is often called 'cancellation of quotients': (G/M)/(N/M) behaves like G/N because the M's cancel. The ℤ example makes this concrete: (ℤ/6ℤ)/(2ℤ/6ℤ) ≅ ℤ/2ℤ, just as (1/6)/(1/3) = 1/2. The key is not that order doesn't matter (it does) but that the nested two-step quotient reduces to the simpler direct quotient G/N."

- question: "The proof of the Second Isomorphism Theorem works by defining a homomorphism φ: S → (SN)/N and applying the First Isomorphism Theorem — the kernel turns out to be S ∩ N."
  type: true-false
  answer: true
  explanation: "This is the standard proof: define φ(s) = sN. This is a homomorphism (composition of inclusion S ↪ SN and natural projection SN → (SN)/N). Its kernel is {s ∈ S : sN = N} = {s ∈ S : s ∈ N} = S ∩ N. Its image is all of (SN)/N. The First Isomorphism Theorem then gives S/(S ∩ N) ≅ (SN)/N. The entire argument is an application of the first theorem in the right context — once you see the right homomorphism."

- question: "The Second and Third Isomorphism Theorems are independent results that require entirely different proof techniques from each other and from the First Isomorphism Theorem."
  type: true-false
  answer: false
  explanation: "Both theorems are consequences of the First Isomorphism Theorem — they are the same tool applied in two different contexts. The key skill in both proofs is identifying the right homomorphism and computing its kernel; once the homomorphism is found, the First Isomorphism Theorem does all the work. Understanding them as 'First Isomorphism Theorem in disguise' is what allows fluent application rather than memorizing each as a separate result."

- question: "Explain in your own words why the Third Isomorphism Theorem can be thought of as 'cancellation of quotients,' and give a concrete numerical example."
  type: short-answer
  answer: "When M ⊆ N are both normal in G, the theorem says (G/M)/(N/M) ≅ G/N. Quotienting G by M gives G/M; within G/M, the image of N is N/M; quotienting again by N/M is equivalent to having quotiented G by N in one step — the M's cancel. Numerically: G = ℤ, M = 6ℤ, N = 2ℤ. Then G/M = ℤ₆, N/M = {0̄, 2̄, 4̄} ≅ ℤ₃ inside ℤ₆, and (ℤ₆)/(ℤ₃) ≅ ℤ₂. But G/N = ℤ/2ℤ = ℤ₂ directly. The two-step and one-step quotients produce isomorphic groups."
  explanation: "The fraction analogy is (G/M) ÷ (N/M) = G/N, just as (1/6) ÷ (1/3) = 1/2. The theorem confirms that two successive quotients, when properly nested, reduce to a single quotient — providing a canonical simplification for working with complex subgroup lattices in deeper group theory."
```

## Explainer

The Second and Third Isomorphism Theorems extend the First Isomorphism Theorem to more complex situations involving subgroups and nested quotients. Rather than being standalone results, both are consequences of the first theorem applied in a structured way. Understanding them means recognizing the First Isomorphism Theorem operating in disguise — the key is identifying the right homomorphism and computing its kernel.

The **Second Isomorphism Theorem** concerns a subgroup S ≤ G and a normal subgroup N ◁ G. The product SN = {sn : s ∈ S, n ∈ N} is a subgroup of G (guaranteed because N is normal), and the theorem states (SN)/N ≅ S/(S ∩ N). The proof uses the First Isomorphism Theorem: define φ: S → (SN)/N by φ(s) = sN. This is a homomorphism, and its kernel is exactly S ∩ N (the elements of S that land in N, hence map to the identity coset). The image is all of (SN)/N, so the First Isomorphism Theorem gives S/(S ∩ N) ≅ (SN)/N. The intuition: N "absorbs" the part of S that overlaps with it, and what remains of S in the quotient is S modulo that overlap. To see it numerically: in ℤ₁₂, take S = {0, 4, 8} and N = {0, 6}. Then S ∩ N = {0}, SN = {0, 4, 6, 8, 2, 10}, and the isomorphism says (SN)/N ≅ S/{0} ≅ S, both groups of order 3.

The **Third Isomorphism Theorem** handles nested normal subgroups: if M ◁ G and N ◁ G with M ⊆ N, then N/M is normal in G/M, and (G/M)/(N/M) ≅ G/N. The intuition is "cancellation of quotients" — quotienting by M and then by N/M is equivalent to quotienting by N in one step. Think of it as fraction cancellation: (G/M)/(N/M) behaves like G/N. A number-theoretic example: G = ℤ, M = 6ℤ, N = 2ℤ. Then G/M = ℤ₆, N/M = {0̄, 2̄, 4̄} ≅ ℤ₃ inside ℤ₆, and (ℤ₆)/(ℤ₃) ≅ ℤ₂ = G/N. The proof again invokes the First Isomorphism Theorem, this time for the natural projection G/M → G/N.

Both theorems are tools for translating between different descriptions of the same group-theoretic structure. When confronted with a complicated quotient or an intersection of subgroups, they provide canonical rewritings that simplify further analysis. They appear constantly in deeper group theory — the Jordan-Hölder theorem and Sylow theory both require comparing quotients at different levels of a group's subgroup lattice — and in the isomorphism theorems for rings and modules, where the same patterns recur.
