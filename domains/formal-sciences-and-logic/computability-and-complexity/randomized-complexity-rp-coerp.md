---
id: randomized-complexity-rp-coerp
title: 'Randomized Complexity: RP, co-RP, and ZPP'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: bpp-randomized-complexity
  type: hard
- id: probabilistic-computation
  type: hard
tags:
- randomization
- complexity-classes
- error-bounds
stage: advanced
status: draft
---

# Randomized Complexity: RP, co-RP, and ZPP

## Core Idea
RP (randomized polynomial time) contains problems solvable in randomized polynomial time with bounded false-positive error. co-RP has bounded false-negative error. ZPP (zero-error probabilistic polynomial time) = RP ∩ co-RP contains problems with randomized algorithms guaranteeing correct answers with expected polynomial runtime. These classes capture how randomization enables efficient computation with controlled error.

## Explainer

You already know BPP — the class of problems solvable in randomized polynomial time with two-sided bounded error. A BPP algorithm may be wrong on YES instances (false negatives) or NO instances (false positives), but the probability of error is at most 1/3 in either case, and you can reduce the error arbitrarily by repeating and taking the majority vote. RP, co-RP, and ZPP explore a finer question: what if we are willing to tolerate one direction of error but not the other?

**RP (Randomized Polynomial time)** requires that if the answer is NO, the algorithm always says NO — no false positives. But if the answer is YES, the algorithm says YES with probability at least 1/2 and may incorrectly say NO. This **one-sided error** is valuable because we can run the algorithm many times: if it says YES even once, the answer is definitely YES. If it always says NO after k runs, the probability we are wrong drops to (1/2)^k. The classic example is polynomial identity testing via the Schwartz-Zippel lemma: to test if a polynomial is identically zero, evaluate it at a random point; a nonzero polynomial will be caught with high probability, but a zero polynomial is always correctly identified.

**co-RP** is the complement class: if the answer is YES, the algorithm always says YES, but on NO instances it may falsely say YES with probability at most 1/2. Think of it as RP "flipped." A co-RP algorithm is useful when false negatives are acceptable but false positives are not — if it says NO, the answer is definitely NO. **ZPP** (Zero-error Probabilistic Polynomial time) is defined as RP ∩ co-RP: a problem is in ZPP if it has both an RP algorithm and a co-RP algorithm. This means there is a randomized algorithm that is always correct but may "give up" (output "I don't know") with some probability less than 1/2 — and equivalently, a Las Vegas algorithm that always gives the correct answer in expected polynomial time. ZPP captures truly zero-error randomized efficiency.

The relationship to BPP is an important open question. We know ZPP ⊆ RP ⊆ BPP and ZPP ⊆ co-RP ⊆ BPP. Whether any of these containments are strict is unknown — it is possible that P = BPP, which would collapse the whole hierarchy. The deeper lesson is that the structure of randomized complexity is about the asymmetry of error: which mistakes you can live with shapes which problems become tractable and by how much. One-sided error is strictly more useful than two-sided when you need certainty on one type of answer.
