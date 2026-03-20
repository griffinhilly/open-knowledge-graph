---
id: co-np
title: co-NP
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-and-polynomial-time
  type: hard
builds-toward:
- bpp-randomized-complexity
- interactive-proofs
tags:
- complexity
- co-NP
- complexity-classes
stage: advanced
status: draft
---

# co-NP

## Core Idea
co-NP is the class of decision problems whose complements are in NP — equivalently, problems for which "no" answers have short, efficiently verifiable proofs (certificates). The canonical co-NP-complete problem is TAUTOLOGY: given a Boolean formula, is it true under every assignment? While NP captures problems with easily verified "yes" certificates, co-NP captures problems with easily verified "no" certificates. Whether NP equals co-NP is a major open question; if they differ, then no NP-complete problem is in co-NP and no co-NP-complete problem is in NP.

## How It's Best Learned
Start from a familiar NP problem (SAT) and construct its complement (UNSAT / TAUTOLOGY). Observe that verifying a "yes" instance of TAUTOLOGY seems to require checking all assignments, whereas verifying a "no" instance just requires one falsifying assignment. This asymmetry between "yes" and "no" certificates is the essence of NP vs co-NP.

## Common Misconceptions
- co-NP is NOT the complement of NP — it is the class of complements of NP languages. P is contained in both NP and co-NP, so these classes overlap significantly.
- If P = NP, then NP = co-NP, but NP = co-NP does not necessarily imply P = NP — the relationship is a one-way implication.

## Explainer

Start from what you already know about NP: a problem is in NP if "yes" answers have short, efficiently checkable **certificates**. For SAT, a satisfying assignment is the certificate — hand it to a verifier and it can confirm in polynomial time that the assignment makes the formula true. The difficulty is in *finding* such an assignment, not in checking it. NP is the class where yes-answers are easy to verify even if they are hard to find.

**co-NP** is the mirror image. A language L is in co-NP if and only if its complement — the language of all strings *not* in L — is in NP. Equivalently, co-NP is the class of problems where *"no" answers have short, efficiently checkable certificates*. The canonical example is TAUTOLOGY: given a propositional formula, is it true under every possible truth assignment? A "no" certificate for TAUTOLOGY is a single falsifying assignment — you can verify it in polynomial time by evaluating the formula. But a "yes" certificate would require confirming that *no* falsifying assignment exists, which seems to require checking all of them. This asymmetry between yes-certificates and no-certificates is exactly the content of the NP vs. co-NP distinction.

Note carefully what co-NP is *not*. It is not the complement of NP as a set of languages. Both NP and co-NP contain all of P — they overlap substantially. The complement of the set NP would exclude P, which is clearly wrong. Rather, co-NP is defined *language-by-language*: for each language L, L is in co-NP iff the complement language {x : x ∉ L} is in NP. So TAUTOLOGY is in co-NP because SAT (its complement) is in NP.

The deepest open question here is whether NP = co-NP. If they are equal, then every problem with efficiently verifiable yes-certificates also has efficiently verifiable no-certificates — a dramatic structural symmetry. We have strong intuition that NP ≠ co-NP (the asymmetry between SAT and TAUTOLOGY feels real), but we cannot prove it. We do know that if P = NP, then NP = co-NP, because P is closed under complement. The converse fails: NP = co-NP is consistent with P ≠ NP. This one-way implication means NP ≠ co-NP would immediately imply P ≠ NP, making NP vs. co-NP a potentially more approachable stepping stone in the P vs. NP program — though no one has cracked either.
