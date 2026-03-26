---
id: rules-of-logical-inference
title: Rules of Logical Inference
domain: mathematics
course: methods-of-proof
prerequisites:
- id: conditional-implication-statements
  type: hard
- id: tautologies-and-contradictions-classification
  type: soft
builds-toward:
- modus-ponens-and-modus-tollens
- proving-by-direct-method
tags:
- logic
- inference
- deduction
- validity
stage: formal-systems
status: validated
---

# Rules of Logical Inference

## Core Idea
Rules of inference are patterns of reasoning that guarantee a true conclusion when applied to true premises. They preserve truth: if the premises are true, the conclusion must be true. These rules form the foundation of valid deductive proof.

## How It's Best Learned
Learn a few key rules deeply (modus ponens, modus tollens, hypothetical syllogism) rather than trying to memorize many. Understand why each rule works using truth tables or logical intuition.

## Common Misconceptions
- Confusing valid reasoning with true conclusions (validity requires true premises).
- Applying rules backwards (e.g., affirming the consequent).
- Assuming common-sense reasoning is logically valid.

## Questions

```yaml
- question: "A network engineer observes: 'If the server is overloaded (P), then response times increase (Q).' They see that response times have increased (Q is true). What can they definitively conclude?"
  type: multiple-choice
  options:
    - "The server is overloaded — Q being true confirms P"
    - "Nothing definitive — Q being true does not guarantee P is true"
    - "The server is not overloaded — increased response times rule out overload"
    - "P → Q is no longer a reliable rule, since Q occurred without confirmed P"
  answer: 1
  explanation: "Inferring P from Q and P→Q is the fallacy of affirming the consequent. Many things could cause increased response times (a DDoS attack, a memory leak, heavy legitimate traffic) — the conditional P→Q does not say Q can only happen if P happens. The only valid inference from Q and P→Q is that you cannot yet conclude ¬P. Contrast with modus tollens: if you observe ¬Q (normal response times), then you CAN conclude ¬P (server is not overloaded)."

- question: "Which of the following inference patterns is logically valid?"
  type: multiple-choice
  options:
    - "From P→Q and Q→R, conclude P→R (hypothetical syllogism)"
    - "From P→Q and Q, conclude P (affirming the consequent)"
    - "From P→Q and ¬P, conclude ¬Q (denying the antecedent)"
    - "From P∨Q and P, conclude ¬Q (disjunctive elimination)"
  answer: 0
  explanation: "Hypothetical syllogism (option A) is valid: if P implies Q and Q implies R, then P implies R by transitivity of implication. This is the chain rule of logic and underlies multi-step proofs. Options B and C are both classic invalid forms — common fallacies. Option D is wrong because P∨Q being true with P true tells you nothing about Q; Q could also be true."

- question: "A valid argument with true premises must have a true conclusion."
  type: true-false
  answer: true
  explanation: "This is the definition of validity combined with the truth of premises — it describes a *sound* argument. Validity guarantees that IF the premises are true, THEN the conclusion is true. When the premises are additionally stipulated to be true, the conclusion is forced to be true. This is precisely why valid inference rules are so powerful in mathematics: the axioms are taken as true, so valid deductions from them produce true theorems."

- question: "An argument is valid if and mainly if its conclusion is true."
  type: true-false
  answer: false
  explanation: "Validity is a structural property of the argument form, completely independent of whether the conclusion is actually true. 'All fish can fly; salmon are fish; therefore salmon can fly' is a valid argument (the conclusion follows necessarily from the premises) even though the conclusion is false (because a premise is false). Conversely, a conclusion can be true while the argument that reaches it is invalid. Validity concerns the logical relationship between premises and conclusion, not the truth values of either."

- question: "What is the difference between a valid argument and a sound argument? Give an example of a valid but unsound argument."
  type: short-answer
  answer: "A valid argument has a form that guarantees the conclusion is true whenever all premises are true — the conclusion follows necessarily from the premises. A sound argument is valid AND has true premises. A valid but unsound argument: 'All mammals can breathe underwater; dolphins are mammals; therefore dolphins can breathe underwater.' The form (all A are B; x is A; therefore x is B) is valid, but the first premise is false, making the argument unsound even though the conclusion happens to be true."
  explanation: "The distinction matters for proof-checking: you must verify both that your logical steps are valid (the structure is correct) and that your starting assumptions are true (the premises hold). In mathematics, axioms supply the true premises; logic rules supply validity. An error in either dimension produces a flawed proof — but they are distinct types of error."
```

## Explainer

A **rule of inference** is a template for constructing valid arguments. You know from your study of conditional statements that "P → Q" means "if P then Q," and you know what it means for a statement to be a tautology — true under every truth assignment. Rules of inference are exactly those argument forms whose logical structure guarantees truth-preservation: whenever the premises are true, the conclusion must be true. That guarantee is what makes a proof valid, as opposed to merely persuasive.

The most important rule is **modus ponens**: from P and P → Q, conclude Q. In natural language: "It is raining" and "If it rains, the ground gets wet" together imply "The ground gets wet." Verify this with a truth table — the only row where both premises are true forces Q to be true. **Modus tollens** runs the same conditional in reverse: from ¬Q and P → Q, conclude ¬P. If the ground is dry, and rain would wet it, then it hasn't rained. Notice what is not valid: from Q and P → Q, you cannot conclude P. That error is called **affirming the consequent** — it is the classic confusion between "if P then Q" and "if Q then P."

**Hypothetical syllogism** chains conditionals: from P → Q and Q → R, conclude P → R. This is transitivity of implication, and it is what allows multi-step proofs — each step passes the truth forward until you reach the desired conclusion. **Disjunctive syllogism** handles or-statements: from P ∨ Q and ¬P, conclude Q. If at least one of P, Q is true and P is false, Q must be true. This is the logical engine behind proof by cases and proof by elimination.

The overarching principle is **validity vs. truth**. An argument is valid if the conclusion follows necessarily from the premises — regardless of whether the premises are actually true. "All fish can fly; salmon are fish; therefore salmon can fly" is valid (the structure is correct) but unsound (a premise is false). In mathematics, where the axioms are stipulated to be true, validity and soundness coincide — but the distinction reminds you to check both the logical structure of your proof and the truth of your starting assumptions. Rules of inference give you the structural half; your domain knowledge gives you the truth half.
