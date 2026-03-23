---
id: when-is-something-proven
title: When Is Something "Proven"?
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: direct-proof-introduction
    type: hard
  - id: proof-by-contradiction-introduction
    type: hard
  - id: proof-by-exhaustion-intro
    type: soft
  - id: mathematical-induction-introduction
    type: soft
  - id: conjectures-and-testing
    type: hard
builds-toward:
  - proof-structure-and-terminology
  - deductive-reasoning-and-formal-proofs
tags: [proof, certainty, mathematical-truth, standards-of-proof]
stage: abstract-reasoning
status: validated
---

# When Is Something "Proven"?

## Core Idea
A mathematical statement is proven when a logical argument demonstrates that the conclusion follows necessarily from accepted axioms, definitions, and previously proven results — with no gaps in reasoning. A proof is not a pile of evidence or a collection of examples; it is a deductive chain where each step is justified. Proof gives mathematical certainty, which is different from scientific confidence (strong evidence) or legal proof (beyond reasonable doubt). Understanding the standard of proof in mathematics helps you distinguish between "strongly supported" and "definitely true."

## How It's Best Learned
Compare standards of evidence across fields. In court: "beyond reasonable doubt." In science: "supported by reproducible evidence." In math: "follows necessarily from axioms." Show a conjecture with enormous evidence (Goldbach's) that remains unproven, alongside a simple theorem with a short proof. Discuss: why do mathematicians insist on this standard? Connect to the proof strategies already learned and show how each meets the standard of zero logical gaps.

## Common Misconceptions
- Equating evidence with proof. A million confirming examples are not a proof. This is the hardest idea for students coming from empirical disciplines.
- Thinking proofs are discovered by checking every case. Most proofs work for all cases simultaneously through abstraction, not by enumeration.
- Believing that once a statement is proven, it might later be disproven by new evidence. Mathematical proof is permanent — a correctly proven theorem stays true forever (barring errors in the proof itself).

## Questions

```yaml
- question: "Which of the following constitutes a mathematical proof that all multiples of 4 are even?"
  type: multiple-choice
  options:
    - "Checking that 4, 8, 12, 16, and 20 are all even"
    - "A survey showing 95% of mathematicians believe it"
    - "The argument: if n = 4k, then n = 2(2k), which is 2 times an integer, hence even"
    - "A computer program that checks the first million multiples of 4"
  answer: 2
  explanation: "Option C is a deductive proof: it starts from the definition (n = 4k), performs valid algebra (4k = 2·2k), and arrives at the conclusion by definition (2 times an integer is even). It covers all multiples of 4 at once, not just specific ones. Options A and D check examples, which is testing, not proving. Option B is an appeal to authority."

- question: "A mathematical theorem that was proven 200 years ago could be overturned by new evidence discovered today."
  type: true-false
  answer: false
  explanation: "Mathematical proof is deductive: if the axioms are accepted and the logical steps are valid, the conclusion follows necessarily and permanently. A proven theorem cannot be 'overturned by evidence' the way a scientific theory can be revised by new data. The only way a proven theorem fails is if an error is found in the proof itself — which is a correction, not new evidence."

- question: "Explain why Goldbach's Conjecture (every even number greater than 2 is the sum of two primes) is not considered proven, despite being verified for all even numbers up to 4 × 10¹⁸."
  type: short-answer
  answer: "Verification of specific cases, no matter how many, is not a proof. A proof must show the statement follows logically for ALL even numbers greater than 2 — infinitely many cases. The 4 × 10¹⁸ verified cases show the conjecture is very likely true, but it is possible (however unlikely) that some larger number is a counterexample. Only a deductive argument covering all cases would constitute proof."
  explanation: "This highlights the fundamental gap between evidence and proof in mathematics. Scientific disciplines accept strong evidence as provisional truth. Mathematics requires logical certainty. Goldbach's Conjecture is one of the oldest unsolved problems precisely because the gap between 'checked extremely many cases' and 'proven for all cases' is the hardest part of mathematics."
```

## Explainer

You have now seen four proof strategies: direct proof, contradiction, exhaustion, and induction. Each works differently, but they all meet the same standard: every step follows logically from previous steps, and the conclusion is an unavoidable consequence of the premises. When mathematicians say something is "proven," they mean this standard has been met — not that there is a lot of evidence for it, not that experts believe it, not that a computer checked many cases.

This standard is unique to mathematics. In a courtroom, the standard is "beyond reasonable doubt" — strong enough for practical purposes, but not logically airtight. In science, the standard is reproducible evidence and peer review — powerful, but always provisional, because tomorrow's experiment could overturn today's theory. In mathematics, once a theorem is proven, it stays proven forever. The Pythagorean theorem was proven over 2,000 years ago, and no discovery will ever invalidate it. The proof is a logical structure that stands independent of observation.

Why insist on such a high standard? Because mathematics deals with universal claims about infinite sets. "Every even number greater than 2 can be written as a sum of two primes" is a claim about infinitely many numbers. You cannot check them all. Goldbach's Conjecture has been verified computationally for every even number up to 4 × 10¹⁸ — an unimaginably large number of cases — and yet no mathematician considers it proven. The reason is not stubbornness; it is that the very next number could be a counterexample. In principle, there might be some enormous even number that defies the pattern. Only a proof can rule that out.

This creates a practical lesson for your own reasoning: always be clear about whether you have evidence or proof. When you check examples and see a pattern, you have evidence — a conjecture worth investigating. When you construct a deductive argument that covers all cases, you have a proof. The cycle of conjecture → testing → proof (or counterexample) is the engine of mathematical discovery, and understanding where you are in that cycle at any moment is one of the most important skills this course teaches.

There is also a humbling corollary. Kurt Godel proved in 1931 that any sufficiently powerful mathematical system contains true statements that cannot be proven within that system. This does not mean proof is unreliable — proven statements are certain. It means there are limits to what can be proven, which is itself a proven theorem. The study of what can and cannot be proven is one of the deepest branches of logic, and the reasoning skills you are building now are the foundation for eventually exploring it.
