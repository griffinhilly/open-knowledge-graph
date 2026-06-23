---
id: proving-by-contradiction
title: Proving by Contradiction
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proving-by-direct-method
  type: hard
- id: tautologies-and-contradictions-classification
  type: soft
- id: negating-quantifiers
  type: soft
- id: proof-by-contradiction-introduction
  type: hard
builds-toward:
- proving-by-cases
tags:
- proof
- contradiction
- reductio ad absurdum
- indirect
stage: formal-systems
status: validated
---

# Proving by Contradiction

## Core Idea
To prove P, assume ¬P and derive a contradiction. If ¬P leads to a contradiction (a statement that is always false), then ¬P must be false, so P must be true. Contradiction proofs are powerful for establishing results that are hard to derive directly.

## How It's Best Learned
Start with simple contradiction proofs (e.g., proving √2 is irrational). Identify the contradiction clearly and verify it is genuine.

## Common Misconceptions
- Confusing any false statement with a logical contradiction.
- Failing to clearly state what is assumed and what is derived.
- Using the conclusion indirectly in the proof.

## Questions

```yaml
- question: "A student assumes ¬P, works through several steps, and derives a statement that is clearly false given the other facts of the problem — but does not derive a statement of the form Q ∧ ¬Q. Has the student completed a valid proof by contradiction?"
  type: multiple-choice
  options:
    - "Yes — deriving any false statement from ¬P is sufficient to conclude ¬P is false"
    - "Yes — the contradiction is implicit; a false conclusion demonstrates that ¬P cannot hold"
    - "No — the proof is incomplete. A contradiction requires deriving Q ∧ ¬Q, a statement that is simultaneously true and false, not merely a false statement"
    - "No — but only if the false statement was derived using an error in reasoning"
  answer: 2
  explanation: "This is the most common error in contradiction proofs. A 'false given other facts' is not the same as a logical contradiction. A contradiction must be of the form Q ∧ ¬Q — the exact same proposition asserted both true and false within the proof. If the student merely derived something that conflicts with background knowledge, the proof structure is incomplete: it hasn't yet shown that assuming ¬P alone creates an internal impossibility."

- question: "For which of the following is proof by contradiction the most natural approach?"
  type: multiple-choice
  options:
    - "Proving that the sum of two even numbers is even"
    - "Proving that if n² is even then n is even"
    - "Proving that there are infinitely many prime numbers"
    - "Proving that (a+b)² = a² + 2ab + b²"
  answer: 2
  explanation: "Proving there are infinitely many primes is a classic non-constructive existence result — the direct approach (exhibiting infinitely many primes explicitly) is not feasible. Euclid's contradiction proof assumes there are finitely many primes, constructs their product plus one, and shows that number can't be divisible by any prime on the list — a contradiction. The sum of two evens (A) and algebraic identities (D) follow directly from definitions. That n² even implies n even (B) can be done by contrapositive. Contradiction is most powerful for negatives, irrationality claims, and non-constructive existence results."

- question: "In a valid proof by contradiction of proposition P, the contradiction must arise specifically from the assumption of ¬P — deriving any false or absurd-looking statement is not sufficient."
  type: true-false
  answer: true
  explanation: "The logical force of a contradiction proof comes from the assumption of ¬P causing the impossibility. If the contradiction arises from an unrelated error or from some other background assumption being wrong, it does not establish P. The structure requires: (assume ¬P) + (apply valid reasoning) + (other accepted truths) → Q ∧ ¬Q. The '¬P is the culprit' is what allows you to discharge the assumption and conclude P must hold."

- question: "Proof by contradiction and proof by contrapositive are the same technique: both assume the negation of something and derive a contradiction."
  type: true-false
  answer: false
  explanation: "These are distinct techniques. Proof by contrapositive proves 'P → Q' by directly proving '¬Q → ¬P' — a positive chain of reasoning from ¬Q to ¬P, with no contradiction involved. Proof by contradiction assumes ¬P (or assumes the entire proposition is false) and derives an explicit logical impossibility (Q ∧ ¬Q). Contrapositive is technically a direct proof of the contrapositive form; contradiction is an indirect proof that derives an impossibility. The structural difference matters when deciding which technique to use."

- question: "What distinguishes a genuine logical contradiction from merely deriving a statement that is false in context, and why does the distinction matter for the validity of a contradiction proof?"
  type: short-answer
  answer: "A genuine logical contradiction is a statement of the form Q ∧ ¬Q — the exact same proposition is simultaneously asserted true and false within the proof, regardless of any external context. A false-in-context statement is one that contradicts background knowledge or previous results, but is not self-negating. The distinction matters because the validity of reductio ad absurdum depends on the law of excluded middle: ¬P → (Q ∧ ¬Q) implies P, because Q ∧ ¬Q is an absolute impossibility. If instead ¬P merely implies something empirically false or contextually awkward, the logical engine fails — the impossibility might have another source, and we cannot conclude ¬P is the culprit."
  explanation: "Getting this distinction right is what separates a valid contradiction proof from a proof that only *looks* like one. Common error: a student derives '2 = 3' from ¬P and considers the proof complete, but '2 ≠ 3' is an external fact, not a logical negation of anything already in the proof. A cleaner contradiction would be: from ¬P, derive that some integer n is both even (2 | n) and odd (2 ∤ n). That is Q ∧ ¬Q, a self-contained logical impossibility."
```

## Explainer

You already know from direct proof that a mathematical argument establishes P by starting from known truths and reasoning forward to P. Proof by contradiction takes a different entry point: instead of trying to build a path to P, you ask what would happen if P were false. The logical engine is the **law of excluded middle** — every proposition is either true or false, with no middle ground. If assuming ¬P leads to a logical impossibility (a statement that cannot be true), then ¬P must be false, so P must be true. The formal name for this technique is **reductio ad absurdum** — "reduction to the absurd."

The structure of every contradiction proof follows the same template: (1) clearly state that you are assuming ¬P; (2) derive consequences from ¬P, combined with whatever other facts are available; (3) arrive at a statement of the form "Q and ¬Q" — a statement that is simultaneously asserted true and false. The contradiction is genuine only when Q and ¬Q are exact logical negations of each other. This is where most errors enter: a conclusion can be merely false (given our other assumptions) without being a literal logical contradiction of the form Q ∧ ¬Q. The contradiction must come from the assumption of ¬P itself.

The most famous example — proving √2 is irrational — illustrates why contradiction is sometimes the only viable method. To prove a negative ("√2 is *not* rational") directly would require examining every rational number, which is impossible. Instead, assume √2 = p/q in lowest terms. Squaring both sides gives 2q² = p², so p² is even, so p is even (write p = 2k). Then 2q² = 4k², so q² = 2k², so q is even. But then p and q share a factor of 2, contradicting the assumption that p/q was in lowest terms. The contradiction is concrete and specific — the same fraction cannot simultaneously be in lowest terms and have both numerator and denominator even.

From your study of negating quantifiers and tautologies, you know that negating a statement carefully is essential. When the proposition P has the form "for all x, Q(x)," the negation ¬P is "there exists x such that ¬Q(x)" — not just "Q(x) is false somewhere." Getting the negation precisely right before beginning the proof prevents the error of assuming something weaker than ¬P and then being surprised when the contradiction does not materialize. Contradiction is especially powerful when P is an existence statement, an irrationality claim, or a non-constructive assertion — cases where direct proof would require exhibiting or constructing something that may be hard to find.
