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
- id: co-np-and-complements
  type: soft
tags:
- randomization
- complexity-classes
- error-bounds
stage: advanced
status: validated
---
# Randomized Complexity: RP, co-RP, and ZPP

## Core Idea
RP (randomized polynomial time) contains problems solvable in randomized polynomial time with bounded false-positive error. co-RP has bounded false-negative error. ZPP (zero-error probabilistic polynomial time) = RP ∩ co-RP contains problems with randomized algorithms guaranteeing correct answers with expected polynomial runtime. These classes capture how randomization enables efficient computation with controlled error.

## Questions

```yaml
- question: "An RP algorithm is run 20 times on an input x, and all 20 runs output NO. What can we conclude?"
  type: multiple-choice
  options:
    - "The answer is definitely NO — RP algorithms are always correct on NO instances"
    - "The answer is probably NO, with error probability at most (1/2)^20, but we cannot be certain"
    - "The answer is definitely YES — if the algorithm said NO 20 times, it must have been on a YES instance and kept making mistakes"
    - "We cannot conclude anything, because RP algorithms have two-sided error like BPP"
  answer: 1
  explanation: "RP has ONE-SIDED error: on NO instances, the algorithm ALWAYS says NO (no false positives). So if the true answer is NO, every run correctly outputs NO. If the true answer is YES, each run says YES with probability ≥ 1/2 and NO with probability ≤ 1/2. After 20 independent NO outputs, the probability that the true answer is YES is at most (1/2)^20 ≈ 10^{-6}. We are extremely confident the answer is NO, but not with absolute certainty — the true answer could be YES and we just got unlucky 20 times. This is why we say 'with high probability' rather than 'certainly.'"

- question: "An RP algorithm for problem L is run on input x and outputs YES. What can we conclude?"
  type: multiple-choice
  options:
    - "The answer is probably YES, with error probability at most 1/2, but not definite"
    - "The answer is definitely YES — RP has no false positives, so a YES output is always correct"
    - "We need to run the algorithm more times to reduce the error probability below 1/2"
    - "The algorithm may have made an error; we should switch to a co-RP algorithm for confirmation"
  answer: 1
  explanation: "RP is defined so that NO instances always output NO (no false positives). Equivalently, a YES output is never wrong — if the algorithm says YES, the answer is definitely YES. The one-sided error is on YES instances: the algorithm might say NO when the answer is YES (a false negative), but never says YES when the answer is NO (no false positives). This asymmetry is the whole point: a single YES output from an RP algorithm is a definitive witness to membership, while repeated NO outputs give exponentially increasing confidence."

- question: "A problem in ZPP has a randomized algorithm that always outputs the correct answer, but may run for a very long time on some random coin sequences — ZPP does not require polynomial time on every execution, only in expectation."
  type: true-false
  answer: true
  explanation: "ZPP = RP ∩ co-RP, and can be characterized by Las Vegas algorithms: always correct, with expected polynomial running time. On some coin sequences, a ZPP algorithm may run for much longer than polynomial time; what is bounded is the EXPECTED runtime over the random choices. This contrasts with deterministic polynomial time (P), where every execution must halt in polynomial time, and with Monte Carlo algorithms (BPP/RP), which halt quickly but may be wrong."

- question: "The most efficient strategy to reduce the error probability of an RP algorithm is to run it multiple times and take the majority vote, just as with BPP algorithms."
  type: true-false
  answer: false
  explanation: "For RP, majority vote is both unnecessary and suboptimal. Because RP has no false positives, a single YES output is definitive — you do not need to confirm it with more runs. The right strategy for RP is: run k times, and if ANY run outputs YES, answer YES. If ALL runs output NO, answer NO. This achieves error probability (1/2)^k with k runs. Majority vote would be wasteful (it discards the definitive YES information) and would actually weaken the conclusion on some inputs. Majority vote is appropriate for BPP because two-sided error requires averaging out both types of mistakes."

- question: "Why is one-sided error more exploitable than two-sided error? Explain using the structure of RP algorithms."
  type: short-answer
  answer: "With one-sided error, one answer type is always reliable. In RP, NO outputs are always correct — there are no false positives. This means a single YES output is a conclusive proof of YES-membership. Repeated runs amplify confidence exponentially: if all k runs say NO, the probability of a missed YES is at most (1/2)^k, which shrinks exponentially fast. With two-sided error (BPP), neither YES nor NO is conclusive on any single run — you can only accumulate probabilistic evidence, requiring majority vote over many runs. One-sided error gives you a 'definitive witness' property that two-sided error lacks."
  explanation: "This structure explains why RP is the natural complexity class for many algebraic and combinatorial decision problems: often there is an efficient way to CHECK a certificate (if a polynomial is non-zero, a random evaluation witnesses it), but no efficient way to prove non-membership. Problems in RP tend to have efficient randomized witnesses for the YES case, which is exactly the one-sided-error structure. Co-RP has the same advantage for the NO case."
```

## Explainer

You already know BPP — the class of problems solvable in randomized polynomial time with two-sided bounded error. A BPP algorithm may be wrong on YES instances (false negatives) or NO instances (false positives), but the probability of error is at most 1/3 in either case, and you can reduce the error arbitrarily by repeating and taking the majority vote. RP, co-RP, and ZPP explore a finer question: what if we are willing to tolerate one direction of error but not the other?

**RP (Randomized Polynomial time)** requires that if the answer is NO, the algorithm always says NO — no false positives. But if the answer is YES, the algorithm says YES with probability at least 1/2 and may incorrectly say NO. This **one-sided error** is valuable because we can run the algorithm many times: if it says YES even once, the answer is definitely YES. If it always says NO after k runs, the probability we are wrong drops to (1/2)^k. The classic example is polynomial identity testing via the Schwartz-Zippel lemma: to test if a polynomial is identically zero, evaluate it at a random point; a nonzero polynomial will be caught with high probability, but a zero polynomial is always correctly identified.

**co-RP** is the complement class: if the answer is YES, the algorithm always says YES, but on NO instances it may falsely say YES with probability at most 1/2. Think of it as RP "flipped." A co-RP algorithm is useful when false negatives are acceptable but false positives are not — if it says NO, the answer is definitely NO. **ZPP** (Zero-error Probabilistic Polynomial time) is defined as RP ∩ co-RP: a problem is in ZPP if it has both an RP algorithm and a co-RP algorithm. This means there is a randomized algorithm that is always correct but may "give up" (output "I don't know") with some probability less than 1/2 — and equivalently, a Las Vegas algorithm that always gives the correct answer in expected polynomial time. ZPP captures truly zero-error randomized efficiency.

The relationship to BPP is an important open question. We know ZPP ⊆ RP ⊆ BPP and ZPP ⊆ co-RP ⊆ BPP. Whether any of these containments are strict is unknown — it is possible that P = BPP, which would collapse the whole hierarchy. The deeper lesson is that the structure of randomized complexity is about the asymmetry of error: which mistakes you can live with shapes which problems become tractable and by how much. One-sided error is strictly more useful than two-sided when you need certainty on one type of answer.
