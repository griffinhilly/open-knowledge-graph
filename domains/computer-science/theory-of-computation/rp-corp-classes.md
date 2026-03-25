---
id: rp-corp-classes
title: RP and coRP Complexity Classes
domain: computer-science
course: theory-of-computation
prerequisites:
- id: probabilistic-turing-machines
  type: hard
- id: exptime-expspace-classes
  type: soft
- id: bpp-complexity-class
  type: soft
builds-toward:
- bpp-complexity-class
tags:
- complexity-classes
- one-sided-error
stage: advanced
status: validated
---
# RP and coRP Complexity Classes

## Core Idea
RP (randomized polynomial time) allows one-sided error: if x ∈ L, accept with probability ≥ 1/2; if x ∉ L, always reject (no false negatives, possibly false positives). coRP is the complement. Both are contained in BPP. RP is the probabilistic analog of NP; coRP to coNP. These classes model practical algorithms where false answers only occur in one direction and are amplifiable via repetition. RP and coRP provide finer granularity than BPP for understanding randomized algorithm error structures.

## Questions

```yaml
- question: "The Miller-Rabin primality test has the property: if it declares a number composite, it is definitely composite; if it declares a number prime, there is a small chance it is actually composite. Which complexity class does this algorithm belong to?"
  type: multiple-choice
  options:
    - "RP — the algorithm allows false positives (claiming prime when composite) but never false negatives"
    - "coRP — the algorithm has no false negatives (composite → always says composite) but allows false positives"
    - "BPP — the algorithm has two-sided error with error probability below 1/2"
    - "P — primality testing is known to run in deterministic polynomial time"
  answer: 1
  explanation: "The Miller-Rabin test is a coRP algorithm. coRP requires: if the true answer is 'yes' (the number is prime), always output 'yes' — no false negatives. But if the true answer is 'no' (the number is composite), you might incorrectly output 'yes' — false positives allowed. Miller-Rabin satisfies exactly this: it never calls a composite number prime (no false negatives), but it might rarely call a composite number prime (false positives possible). This makes it coRP, not RP (which is the mirror: no false positives, possible false negatives)."

- question: "An RP algorithm runs on input x and outputs 'yes'. What can you conclude with certainty?"
  type: multiple-choice
  options:
    - "x is definitely in the language — RP never produces false positives"
    - "x is probably in the language — there is at most a 1/2 chance of a false positive"
    - "Nothing conclusive — RP allows both false positives and false negatives"
    - "x might not be in the language — you should run the algorithm again to confirm"
  answer: 0
  explanation: "RP has one-sided error: if x ∉ L (x is not in the language), the algorithm always rejects — never producing a false positive. Therefore, if the algorithm says 'yes,' x must be in the language. This is the key practical value of RP: a 'yes' answer is unconditionally trustworthy, while a 'no' might be a false negative (the algorithm might have missed a real 'yes' with probability ≤ 1/2). This asymmetry — trust the positive but not the negative — is precisely what distinguishes RP from BPP, where neither answer can be trusted unconditionally."

- question: "Running an RP algorithm k times and accepting if any single run returns 'yes' reduces the probability of a false negative to at most (1/2)^k."
  type: true-false
  answer: true
  explanation: "This amplification works because RP has one-sided error: the only errors are false negatives (rejecting a true 'yes' instance). For a true 'yes' instance, each run independently accepts with probability ≥ 1/2, so the probability of k consecutive rejections is at most (1/2)^k. After 100 runs, this is less than 10^-30 — effectively zero. And false positives never occur, so accepting as soon as any run says 'yes' is always correct. This amplification argument doesn't work for BPP's two-sided error without more care."

- question: "RP and coRP are the same complexity class, since both allow one-sided error and both are contained in BPP."
  type: true-false
  answer: false
  explanation: "RP and coRP are defined as complements, not equals. RP allows false negatives (might miss true 'yes' instances) but never false positives. coRP allows false positives (might incorrectly accept 'no' instances) but never false negatives. A language is in RP if there is an algorithm with no false positives; the same language is in coRP if there is an algorithm with no false negatives — these are different properties. It is not known whether RP = coRP. Their intersection RP ∩ coRP is particularly useful: an algorithm in this intersection would have no error at all in at least one direction for each answer."

- question: "Explain why one-sided error in RP is more practically useful than two-sided error in BPP, even though BPP contains RP."
  type: short-answer
  answer: "With RP, a 'yes' answer is unconditionally correct — you never need to worry that an acceptance was a false positive. This lets you trust positive results immediately without repetition. With BPP's two-sided error, neither answer can be trusted unconditionally without running the algorithm multiple times to amplify confidence. In settings where you need an unconditionally reliable positive answer (e.g., confirming a witness, verifying a solution), RP gives you this for free; BPP requires extra repetition and probabilistic confidence intervals."
  explanation: "The practical asymmetry matters in many real applications. If you're testing whether a number is prime, an unconditional 'yes' is more useful than 'probably yes with error < 2^-100' — the former admits no doubt. RP algorithms also compose more naturally with other deterministic checks: if an RP algorithm says 'yes' and a subsequent deterministic verifier confirms it, you know the answer is correct without tracking error probabilities. BPP requires careful error bookkeeping throughout. This is why RP/coRP algorithms are often described as 'more trustworthy' despite having higher error probability than amplified BPP."
```

## Explainer

From your work with probabilistic Turing machines, you know that randomness can be a computational resource — a machine that flips coins during its execution can sometimes solve problems more efficiently than a deterministic one. **RP** and **coRP** capture a particularly clean and useful form of randomized computation: algorithms that can only make mistakes in one direction.

An **RP** (Randomized Polynomial time) algorithm has this guarantee: if the true answer is "no," the algorithm always says "no" — it never produces a false positive. But if the true answer is "yes," the algorithm might incorrectly say "no" with probability up to 1/2. Think of it like a metal detector that never beeps for non-metal objects but might miss some metal ones. The key insight is that this one-sided error is easily fixable by repetition: run the algorithm k times, and if it ever says "yes," accept. The probability of missing a true "yes" k times in a row is at most (1/2)^k, which shrinks exponentially. After 100 repetitions, the failure probability is less than 10^-30.

**coRP** is the mirror image: if the true answer is "yes," the algorithm always says "yes" (no false negatives), but it might incorrectly say "yes" when the answer is really "no" (false positives allowed). The classic example is the Miller-Rabin primality test, which sits in coRP: if it declares a number composite, it is certainly composite, but if it declares a number prime, there is a small chance of error. Again, repetition drives the error probability to negligible levels.

Both RP and coRP sit inside **BPP** (bounded-error probabilistic polynomial time), which allows two-sided error. The containment chain is P ⊆ RP ⊆ BPP and P ⊆ coRP ⊆ BPP. It is widely conjectured that P = BPP — that randomness does not actually help for decision problems — which would collapse RP and coRP into P as well. But proving this remains open. In practice, RP and coRP algorithms are valued precisely because their one-sided error makes them trustworthy in one direction without any repetition at all: when an RP algorithm says "yes," you can believe it unconditionally.
