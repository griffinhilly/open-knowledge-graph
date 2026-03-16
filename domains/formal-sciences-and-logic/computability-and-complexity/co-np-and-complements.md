---
id: co-np-and-complements
title: Co-NP and Complementary Complexity Classes
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-and-polynomial-time
  type: hard
builds-toward:
- inapproximability-pcp
tags:
- complexity-classes
- complements
- decision-problems
stage: advanced
status: draft
---

# Co-NP and Complementary Complexity Classes

## Core Idea
Co-NP is the class of problems whose complement lies in NP: a language is in co-NP if its negation is in NP. While NP captures problems with efficiently verifiable 'yes' certificates, co-NP captures problems with efficiently verifiable 'no' certificates. Whether P = NP = co-NP remains a central unsolved question.

## How It's Best Learned
Start with examples of NP problems (satisfiability, clique existence) and their co-NP complements (unsatisfiability, clique non-existence). Note that co-NP is the class where 'no' instances have short proofs, not 'yes' instances.

## Common Misconceptions
- Assuming P = NP would automatically imply P = co-NP (only true if NP = co-NP).
- Confusing the complement of a problem with logical negation of a formula.

## Explainer

You already know that NP captures problems where "yes" answers are easy to verify: given a satisfying assignment for a Boolean formula, you can check it in polynomial time. The key move in understanding co-NP is to ask the symmetric question — what about "no" answers? The **complement** of a language L is the set of all strings not in L, written L̄. If L = SAT (satisfiable formulas), then L̄ = UNSAT (unsatisfiable formulas). Co-NP is precisely the class of languages whose complements are in NP.

Concretely: UNSAT is in co-NP because, to verify that a formula is *not* satisfiable, you don't have a short certificate — but to verify that a formula *is* satisfiable (its complement), you do. Equivalently, a language is in co-NP if "no" instances have polynomial-size certificates that can be checked in polynomial time. For UNSAT, a "no" certificate would be a proof that no assignment works — and we currently know no such short certificate exists in general. For problems like PRIMES (is n prime?), both the problem and its complement have short certificates, so PRIMES ∈ NP ∩ co-NP.

The relationship between NP and co-NP is one of the deepest open questions in complexity theory. We strongly suspect NP ≠ co-NP, because if NP = co-NP, then every NP-complete problem would also have short "no" certificates. Yet SAT having short "no" certificates seems implausible: how could you concisely prove that a formula with millions of possible assignments has no solution? Formally, NP = co-NP if and only if some (equivalently, every) NP-complete problem is also in co-NP.

Note a critical subtlety: if P = NP, then P = NP = co-NP, because P is closed under complementation. But the converse does not hold — NP = co-NP does not imply P = NP. The inclusions are P ⊆ NP ∩ co-NP ⊆ NP ∪ co-NP, and collapsing NP = co-NP is a weaker statement than collapsing P = NP. The co-NP class also starts its own hierarchy: co-NP-complete problems (like UNSAT) are the hardest problems in co-NP, and any NP-hard problem's complement is co-NP-hard.
