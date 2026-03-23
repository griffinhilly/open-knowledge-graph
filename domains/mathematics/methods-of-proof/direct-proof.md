---
id: direct-proof
title: Direct Proof
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proof-structure-and-terminology
  type: hard
builds-toward:
- proof-by-contrapositive
- mathematical-induction
tags:
- proof
- technique
- forward
stage: formal-systems
status: validated
---

# Direct Proof

## Core Idea
A direct proof assumes the hypothesis and uses valid logical steps to derive the conclusion. To prove p → q, assume p is true and show q must follow, establishing the implication.

## How It's Best Learned
Write the hypothesis as a given, list what follows step-by-step with justifications, and show how you reach the conclusion.

## Common Misconceptions
- Proving the converse (q → p) instead of the original statement (p → q).
- Assuming the conclusion is true at the start rather than deriving it.

## Questions

```yaml
- question: "You want to prove: 'If n is odd, then n² is odd.' A student writes: 'Assume n² is odd. Then n² = 2k+1 for some integer k...' and eventually concludes that n must be odd. What error has this student made?"
  type: multiple-choice
  options:
    - "They proved the converse (n² odd → n odd) instead of the original statement (n odd → n² odd)"
    - "They used algebraic manipulation incorrectly"
    - "They forgot to state that k is an integer"
    - "No error — they proved the original statement correctly"
  answer: 0
  explanation: "The student assumed n² is odd (the conclusion) and derived that n is odd (the hypothesis). This proves the converse, q → p, not the original implication p → q. These are different claims — the converse of a true statement is not automatically true. A direct proof of 'if n is odd, then n² is odd' must start by assuming n is odd and then deriving that n² is odd."

- question: "A student proves 'if n is even, then n² is divisible by 4.' Midway through, they write: 'Since n² is divisible by 4, we can write n² = 4m for some integer m, and therefore...' What is the fundamental flaw?"
  type: multiple-choice
  options:
    - "Writing n² = 4m is not a valid algebraic substitution"
    - "The theorem is false for some values of n"
    - "The student is assuming the conclusion before proving it, making the argument circular"
    - "They should have used proof by contradiction instead"
  answer: 2
  explanation: "A direct proof must derive the conclusion; it cannot assume it. Writing 'since n² is divisible by 4' as a step inside the proof that n² is divisible by 4 is circular reasoning — the thing being proved is smuggled in as a premise. The only thing you are allowed to assume at the start is the hypothesis (n is even). Every subsequent step must follow from previous ones."

- question: "In a valid direct proof of 'if P, then Q,' the only statement you are permitted to assume at the very start is P."
  type: true-false
  answer: true
  explanation: "This is the defining constraint of a direct proof. You assume the hypothesis P and nothing else. All other statements — intermediate conclusions, substitutions, applications of definitions — must be derived from P using logic, definitions, and previously established theorems. Assuming anything beyond P (especially Q itself) invalidates the proof."

- question: "Successfully proving 'if Q, then P' also proves 'if P, then Q.'"
  type: true-false
  answer: false
  explanation: "Proving 'if Q, then P' proves the converse of 'if P, then Q' — a completely different statement. An implication and its converse are logically independent: one can be true while the other is false. For example, 'if n is even, then n² is even' is true, but its converse 'if n² is even, then n is even' requires a separate proof. Proving the converse is one of the most common errors in beginning proof-writing."

- question: "Why does assuming the conclusion at the start of a direct proof invalidate the argument, even if every subsequent step is logically valid?"
  type: short-answer
  answer: "A proof is meant to establish that Q must follow from P alone. If you assume Q as a premise, you have added it to your starting assumptions — so your argument only shows that Q follows from {P, Q}, which is trivially true and tells you nothing. The whole point of the proof is to show Q is necessary given P. Assuming Q makes the argument circular: the conclusion depends on itself."
  explanation: "This is the distinction between a proof and a verification. A verification starts with Q and checks consistency; a proof starts only with P and derives Q. Any step that introduces Q as an assumption — even implicitly — collapses the proof into circular reasoning. The practical warning sign: if you find yourself writing the conclusion in the middle of the argument, check whether you are using it as a premise."
```

## Explainer

You have already learned, from proof-structure-terminology, that a mathematical proof is a sequence of logical steps leading from accepted premises to a conclusion. A **direct proof** is the most natural way to build that sequence: start with what you're given, apply valid reasoning rules, and walk forward until you arrive at what you want to show.

The structure is always the same. To prove "if P, then Q," you write: "Assume P." Then you deduce a sequence of intermediate statements, each following from previous ones by a logical rule, a definition, or a known theorem. The proof ends when you reach Q. Every step needs a justification — "by definition of X," "by hypothesis," "by Theorem 5," "by algebraic manipulation." The chain of justifications is what makes it a proof rather than an assertion.

Consider proving: "If n is an even integer, then n² is even." Assume n is even. By definition of evenness, n = 2k for some integer k. Then n² = (2k)² = 4k² = 2(2k²). Since 2k² is an integer, n² has the form 2m for an integer m, so n² is even. Done. Notice the structure: unpack definitions, do algebra, repack into the definition of what you need to prove. This is the standard pattern for direct proofs about algebraic or divisibility claims.

The most common errors are subtle flips of direction. Proving the **converse** (assuming Q and deriving P) does not prove the original statement — it proves a different claim. Assuming the **conclusion** at the start and working backward also fails: if you write "suppose n² is even" in the middle of a proof that n² is even, you have assumed what you are trying to show, which is circular. The key discipline is: the hypothesis P is the only thing you are allowed to assume at the start. Everything else must be derived. If you find yourself needing to assume Q to make the argument work, that is a warning sign to check whether you have inverted the implication.
