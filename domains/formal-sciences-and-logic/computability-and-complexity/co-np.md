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
stage: formal-systems
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

## Questions

```yaml
- question: "Consider the TAUTOLOGY problem: given a Boolean formula, is it true under every possible truth assignment? Which type of certificate does TAUTOLOGY have that is short and efficiently verifiable?"
  type: multiple-choice
  options:
    - "A 'yes' certificate — a single satisfying assignment that proves the formula is always true"
    - "A 'no' certificate — a single falsifying assignment that proves the formula is not always true"
    - "Both types — TAUTOLOGY has polynomial-time certificates for both yes and no answers"
    - "Neither — TAUTOLOGY requires checking exponentially many assignments in both directions"
  answer: 1
  explanation: "TAUTOLOGY is the co-NP-complete problem precisely because 'no' answers are easy to verify (one falsifying assignment suffices) while 'yes' answers apparently require checking all 2^n assignments. This is the defining asymmetry of co-NP: problems where 'no' has a short, efficiently verifiable certificate. A 'yes' certificate for TAUTOLOGY would need to certify that *no* falsifying assignment exists — which seems to require exhaustive search and is why TAUTOLOGY is not believed to be in NP (unless NP = co-NP)."

- question: "Which of the following correctly describes the relationship between P, NP, and co-NP?"
  type: multiple-choice
  options:
    - "co-NP is the set of all decision problems NOT in NP; P is in NP but not in co-NP"
    - "P is contained in both NP and co-NP; co-NP consists of problems whose complements are in NP"
    - "co-NP = NP by definition, since every problem in NP has a complement"
    - "co-NP problems are strictly harder than NP problems since they require verifying more assignments"
  answer: 1
  explanation: "P is closed under complement (if you can solve a problem in polynomial time, you can solve its complement in polynomial time too), so P ⊆ NP ∩ co-NP — both classes share all of P. co-NP is defined language-by-language: L ∈ co-NP iff the complement of L is in NP. It is NOT the complement of NP as a set; the complement of NP would exclude P, which is clearly wrong. Whether NP = co-NP is open. What we know is that P ⊆ NP ∩ co-NP, and likely NP ≠ co-NP, but we cannot prove it."

- question: "If P = NP, then it follows that NP = co-NP."
  type: true-false
  answer: true
  explanation: "P is closed under complement: if a problem is solvable in polynomial time, its complement is also solvable in polynomial time (just flip the accept/reject). If P = NP, then NP = P, and since P = co-P ⊆ co-NP, and also co-NP ⊆ NP (because NP = P = co-P and then by symmetry), we get NP = co-NP. More directly: if P = NP, every NP problem is solvable in polynomial time, so its complement is also solvable in polynomial time, putting the complement in P ⊆ NP. Hence every NP language has its complement in NP, meaning every NP language is in co-NP, so NP ⊆ co-NP, and symmetrically co-NP ⊆ NP."

- question: "co-NP is the set of decision problems that are not in NP."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about co-NP. co-NP is defined as the class of problems whose *complements* are in NP — it is NOT the complement of the set NP. In fact, P is contained in both NP and co-NP, so the two classes overlap substantially. Problems in P are in both NP and co-NP simultaneously. The 'co-' prefix refers to taking the complement of each *individual language*, not the complement of the entire complexity class."

- question: "Explain the asymmetry between SAT and TAUTOLOGY that makes SAT an NP-complete problem and TAUTOLOGY a co-NP-complete problem."
  type: short-answer
  answer: "SAT asks: does a given formula have *at least one* satisfying assignment? A 'yes' certificate is short and easy to verify — just provide one satisfying assignment and check it in polynomial time. But TAUTOLOGY asks: does a formula hold under *every* assignment? A 'no' certificate is short — one falsifying assignment suffices. The difficulty is asymmetric: SAT's 'yes' instances are easy to certify (one witness), and TAUTOLOGY's 'no' instances are easy to certify (one witness). SAT is in NP because yes-answers have short certificates; TAUTOLOGY is in co-NP because its no-answers have short certificates, which means SAT (= complement of TAUTOLOGY) is in NP."
  explanation: "The relationship is exact: TAUTOLOGY is the complement of SAT. Every formula either has a satisfying assignment (SAT = 'yes', TAUTOLOGY = 'no') or has none (SAT = 'no', TAUTOLOGY = 'yes'). NP is precisely the class where yes-answers have efficient certificates; co-NP is the class where no-answers have efficient certificates. Since SAT ∈ NP, the complement (TAUTOLOGY) is in co-NP by definition — and TAUTOLOGY is co-NP-complete because any co-NP problem reduces to it."
```

## Explainer

Start from what you already know about NP: a problem is in NP if "yes" answers have short, efficiently checkable **certificates**. For SAT, a satisfying assignment is the certificate — hand it to a verifier and it can confirm in polynomial time that the assignment makes the formula true. The difficulty is in *finding* such an assignment, not in checking it. NP is the class where yes-answers are easy to verify even if they are hard to find.

**co-NP** is the mirror image. A language L is in co-NP if and only if its complement — the language of all strings *not* in L — is in NP. Equivalently, co-NP is the class of problems where *"no" answers have short, efficiently checkable certificates*. The canonical example is TAUTOLOGY: given a propositional formula, is it true under every possible truth assignment? A "no" certificate for TAUTOLOGY is a single falsifying assignment — you can verify it in polynomial time by evaluating the formula. But a "yes" certificate would require confirming that *no* falsifying assignment exists, which seems to require checking all of them. This asymmetry between yes-certificates and no-certificates is exactly the content of the NP vs. co-NP distinction.

Note carefully what co-NP is *not*. It is not the complement of NP as a set of languages. Both NP and co-NP contain all of P — they overlap substantially. The complement of the set NP would exclude P, which is clearly wrong. Rather, co-NP is defined *language-by-language*: for each language L, L is in co-NP iff the complement language {x : x ∉ L} is in NP. So TAUTOLOGY is in co-NP because SAT (its complement) is in NP.

The deepest open question here is whether NP = co-NP. If they are equal, then every problem with efficiently verifiable yes-certificates also has efficiently verifiable no-certificates — a dramatic structural symmetry. We have strong intuition that NP ≠ co-NP (the asymmetry between SAT and TAUTOLOGY feels real), but we cannot prove it. We do know that if P = NP, then NP = co-NP, because P is closed under complement. The converse fails: NP = co-NP is consistent with P ≠ NP. This one-way implication means NP ≠ co-NP would immediately imply P ≠ NP, making NP vs. co-NP a potentially more approachable stepping stone in the P vs. NP program — though no one has cracked either.
