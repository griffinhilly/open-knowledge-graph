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
