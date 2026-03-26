---
id: tautologies-and-contradictions-methods-of-proof
title: Tautologies and Contradictions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: truth-tables
  type: hard
builds-toward:
- proof-by-contradiction
tags:
- tautology
- contradiction
- validity
stage: formal-systems
status: validated
---

# Tautologies and Contradictions

## Core Idea
A tautology is always true regardless of truth assignments; a contradiction is always false. Recognizing these is crucial: if assuming negation of a statement yields a contradiction, the statement must be true.

## How It's Best Learned
Compare tautologies (p ∨ ¬p) with contingencies (p ∧ ¬q) that can be either true or false.

## Common Misconceptions
- Treating a frequently-true statement as a tautology when it could be false in some cases.
- Confusing contradictions with statements that are merely false in specific cases.

## Questions

```yaml
- question: "In a proof by contradiction, you assume ¬Q and derive a contradiction. What exactly does deriving a contradiction establish?"
  type: multiple-choice
  options:
    - "That ¬Q is false in some cases, so Q is probably true"
    - "That the logical system itself contains an inconsistency"
    - "That ¬Q cannot possibly be true under any truth assignment, so Q must be true"
    - "That Q is a tautology — true under all interpretations of its component variables"
  answer: 2
  explanation: "A contradiction is false under every possible truth assignment — it cannot be true. If valid logical steps from assumption ¬Q lead to a contradiction, then ¬Q cannot be true in any world where logic holds. The inference is: if ¬Q were true, the contradiction would have to be true (since each step was valid); but the contradiction cannot be true; therefore ¬Q cannot be true. This is a deductive certainty, not a probabilistic claim. Option D is wrong: Q need not be a tautology — it just must be true in the specific context at hand."

- question: "Which of the following is a tautology?"
  type: multiple-choice
  options:
    - "p → q"
    - "p ∨ q"
    - "p → (q → p)"
    - "¬p → q"
  answer: 2
  explanation: "p → (q → p) is true under every truth assignment. If p is true, then q → p is true (p is the consequent and it's true), so the whole statement is true. If p is false, the antecedent of the outer conditional is false, making the whole statement true regardless of q. Options A and D are contingencies — false when antecedent is true and consequent false. Option B is false when both p and q are false. Only C is always true."

- question: "The statement 'The sun is either currently shining or it is not currently shining' is a tautology."
  type: true-false
  answer: true
  explanation: "This is an instance of p ∨ ¬p — the law of excluded middle — which is always true regardless of the actual weather. A tautology is true by its logical structure alone, not because of contingent facts. Whether it's sunny or cloudy today is irrelevant; the statement's truth is guaranteed by its form."

- question: "Any statement that has been observed to be true in nearly every case examined so far is a tautology."
  type: true-false
  answer: false
  explanation: "A tautology must be true under every logically possible truth assignment, not just every empirically observed case. 'All swans are white' was observed to be true in Europe for centuries — but it was a contingency, not a tautology, because non-white swans were possible (and turned out to exist). Tautologies are true by virtue of logical structure; a contingency can be consistently false under some assignment even if you've never witnessed that assignment."

- question: "Why does deriving a contradiction from an assumption prove that the assumption is false? What property of contradictions makes proof by contradiction work?"
  type: short-answer
  answer: "A contradiction is false under every possible truth assignment — there is no possible world where it is true. If valid logical steps from assumption A lead to a contradiction, then A cannot be true in any world where logic holds: if A were true, the contradiction would have to be true (each step was valid); but contradictions are impossible; therefore A is impossible. The contradiction functions as a logical impossibility — a destination that proves the journey to it was impossible."
  explanation: "This distinguishes proof by contradiction from merely finding a false or surprising conclusion. A surprising conclusion is still possible; a contradiction (R ∧ ¬R) violates the basic law of non-contradiction. Reaching it under valid inference condemns the premise that set you on that path — which is why the method is a deductive proof, not an argument by implausibility."
```

## Explainer

Every logical statement lives somewhere on a spectrum between always-true and always-false. From your truth table work, you know that a compound statement can be true under some truth assignments and false under others — these are called **contingencies** and they're the typical case. But at the extremes are two special cases: **tautologies** are true under every possible truth assignment, and **contradictions** are false under every possible truth assignment. These are not just statements that happen to be true or false — they're true or false as a matter of logical structure alone, independent of any facts about the world.

The canonical tautology is p ∨ ¬p: "p or not p." No matter whether p is true or false, exactly one of the disjuncts is true, so the whole statement is always true. It captures the law of excluded middle. The canonical contradiction is p ∧ ¬p: "p and not p." This is always false because no statement can simultaneously be true and false. Notice these two are negations of each other: ¬(p ∧ ¬p) ≡ p ∨ ¬p, and a tautology's negation is always a contradiction.

The proof-theoretic importance of contradictions is enormous. **Proof by contradiction** works as follows: to prove a statement Q is true, assume ¬Q and derive a contradiction — a statement of the form (R ∧ ¬R). Once you've derived a logical impossibility, the assumption ¬Q must be false, which means Q must be true. The classical example is the irrationality of √2: assume √2 = p/q in lowest terms, derive that both p and q must be even (contradicting "lowest terms"), and conclude the assumption was false. The power of this method depends entirely on understanding that a contradiction is not just a "false thing" but a statement that cannot possibly be true under any assignment — so reaching it proves the starting assumption was impossible.

Tautologies play a complementary role as rewriting tools. In formal logic and computer science, rules of inference are tautologies: modus ponens says that ((p → q) ∧ p) → q is always true. When you apply a proof rule, you're instantiating a tautology. Recognizing a tautology tells you that an argument form is universally valid — it works for any specific statements you plug in. Recognizing a contradiction tells you that a set of assumptions is inconsistent — they can never all be simultaneously true — which is why reaching one during a proof demolishes the premises that led there.
