---
id: truth-values-and-statements
title: Truth Values and Statements
domain: mathematics
course: methods-of-proof
prerequisites: []
builds-toward:
- logical-connectives-and-operators
- truth-tables-and-evaluation
- conditional-implication-statements
tags:
- logic
- statements
- foundations
stage: formal-systems
status: validated
---

# Truth Values and Statements

## Core Idea
A statement is a declarative sentence that is either true or false, but not both. In mathematics, we work with statements that can be analyzed for their truth value. Understanding what counts as a mathematical statement is foundational to all proof work.

## How It's Best Learned
Start with simple examples (e.g., '2 + 2 = 4' is true, '5 > 10' is false) and non-examples (e.g., 'What time is it?' is not a statement). Practice classifying sentences as statements or non-statements.

## Common Misconceptions
- Assuming questions or commands are statements.
- Thinking that statements must be true (false statements are still statements).
- Confusing the meaning of a statement with its truth value.

## Questions

```yaml
- question: "Which of the following is a mathematical statement?"
  type: multiple-choice
  options:
    - "Solve for x in the equation x + 5 = 12"
    - "Is 17 a prime number?"
    - "The square root of two is rational"
    - "x + 3 = 7"
  answer: 2
  explanation: "A statement is a declarative sentence that is either true or false. 'The square root of two is rational' is a statement — it is false. Option A is a command (no truth value). Option B is a question (no truth value). Option D is an open sentence (predicate) — it depends on x and has no truth value until x is specified or quantified. A common misconception is that option D is a statement because it 'looks mathematical,' but it is a predicate: it becomes true for x=4 and false for x=5."

- question: "A student argues that 'x > 0' becomes a statement when we substitute x = 3. The student is:"
  type: multiple-choice
  options:
    - "Wrong — open sentences can never become statements, even with substitution"
    - "Correct — substituting x = 3 gives '3 > 0', which is a true statement"
    - "Wrong — we must also know the domain before it has a truth value"
    - "Correct — any equation involving numbers automatically qualifies as a statement"
  answer: 1
  explanation: "Substituting a specific value for the variable converts a predicate into a statement. '3 > 0' is a genuine statement — it is true. The key distinction is between a predicate like 'x > 0' (truth depends on x, so no single truth value) and a statement like '3 > 0' (definite truth value regardless of context). Option A is wrong: substitution is precisely one of the two ways to produce a statement from a predicate. Option C is wrong for this example — once x is replaced by a specific number, no domain ambiguity remains."

- question: "A false sentence is not a mathematical statement — it must be true to count as a statement."
  type: true-false
  answer: false
  explanation: "This is one of the most common misconceptions about statements. A statement is defined by its *capacity* to have a truth value, not by the value itself. '5 > 10' is a perfectly good mathematical statement — it is simply false. '2 + 2 = 5' is a statement; it is false. The truth value of a statement can be true or false; what disqualifies a sentence from being a statement is being a question, command, or open sentence — not being false."

- question: "The sentence 'For all integers x, x + 3 = 7' is a statement."
  type: true-false
  answer: true
  explanation: "Binding the variable x with the universal quantifier 'for all integers x' converts the predicate 'x + 3 = 7' into a statement. The statement has a definite truth value: it is false (it fails for x = 1, 2, 3, and almost every other integer). The key is that the quantifier removes the dependence on a free variable — nothing is unspecified, so the sentence is either true or false. This is one of the two ways (the other being substitution) to turn a predicate into a statement."

- question: "Why is 'x + 3 = 7' not a statement on its own, but 'for all integers x, x + 3 = 7' is a statement? What changes?"
  type: short-answer
  answer: "The open sentence 'x + 3 = 7' contains a free variable x — its truth depends on what x is, so it has no single truth value and is therefore a predicate, not a statement. The universal quantifier 'for all integers x' binds the variable, removing the dependence on any particular value. The result has a definite truth value (false — since it fails for x = 1, among others), making it a genuine statement."
  explanation: "The distinction between predicates and statements is foundational to all of logic. Proofs consist of statements — sentences with definite truth values. A predicate like 'x + 3 = 7' is a function from values to truth values, not a truth value itself. Quantifiers (for all, there exists) convert predicates into statements by either ranging over all possible values or asserting the existence of one that satisfies the condition. Understanding this is the prerequisite for working with quantified logic, the main language of mathematical proof."
```

## Explainer

Mathematics runs on claims that are either true or false. Before you can reason about numbers, sets, functions, or proofs, you need a precise notion of what kinds of sentences can even have a truth value. A **statement** (also called a **proposition**) is a declarative sentence that is, in principle, either true or false — no other possibility exists. "Seven is prime" is a statement; it is true. "The square root of two is rational" is a statement; it is false. "What is the value of x?" is a question, not a statement — it cannot be true or false.

This binary structure — true or false, and nothing else — is called the **law of the excluded middle**, a foundational assumption of classical logic. It is what makes proof by contradiction possible: if you assume something is false and derive a contradiction, you conclude it must be true, because there is no third option. The assumption is not trivially obvious — constructive mathematicians sometimes question it for certain kinds of statements about infinite objects. But in standard mathematics, every well-formed statement has exactly one **truth value**.

Not every sentence in ordinary language qualifies. Commands ("Compute the integral") and questions ("Is 17 prime?") have no truth value. Open sentences like "x + 3 = 7" depend on the variable x — they become true or false only once x is specified or quantified. These are called **predicates**, and they become statements when the variable is either substituted with a specific value ("5 + 3 = 7" is false) or bound by a quantifier ("For all x, x + 3 = 7" is a statement — a false one). Recognizing this distinction between statements and predicates is the first step toward working with quantifiers, which will drive nearly all of proof logic.

Being careful about what counts as a statement pays off throughout all proof work. A proof is a sequence of statements, each either a hypothesis, a previously established fact, or a logical consequence of earlier lines — every line must be a genuine statement with a definite truth value. A false statement is still a statement; what matters is not truth but the capacity to be true or false. From these simple building blocks — declarative sentences with binary truth values — all of mathematical logic is constructed: connectives combine statements, quantifiers range predicates over domains, and proofs chain statements together in truth-preserving steps.
