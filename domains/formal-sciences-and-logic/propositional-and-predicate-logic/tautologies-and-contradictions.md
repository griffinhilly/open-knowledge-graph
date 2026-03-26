---
id: tautologies-and-contradictions
title: Tautologies, Contradictions, and Satisfiability
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-semantics
  type: hard
- id: logical-equivalences
  type: soft
- id: truth-tables
  type: soft
builds-toward:
- normal-forms-cnf-dnf
- propositional-soundness-completeness
tags:
- tautology
- contradiction
- satisfiability
- validity
stage: formal-systems
status: validated
---

# Tautologies, Contradictions, and Satisfiability

## Core Idea
A tautology is a formula true under every possible valuation (e.g., p ∨ ¬p); a contradiction is false under every valuation (e.g., p ∧ ¬p); a contingency is neither. A formula is satisfiable if at least one valuation makes it true. These classifications partition the space of propositional formulas and are central to logic — proof systems aim to derive exactly the tautologies. The semantic notion of validity (⊨ φ) is the target that syntactic proof systems strive to match.

## How It's Best Learned
Classify a variety of formulas before and after applying De Morgan's laws. Practice converting the question 'is φ a tautology?' to 'is ¬φ a contradiction?' and verify the equivalence.

## Common Misconceptions
- A tautology is not just 'always probably true' — it must hold for literally every truth assignment.
- Satisfiable does not mean true; it means true in at least one scenario.

## Questions

```yaml
- question: "Which statement correctly describes the relationship between tautologies and satisfiability?"
  type: multiple-choice
  options:
    - "Every tautology is satisfiable, but not every satisfiable formula is a tautology"
    - "A tautology and a satisfiable formula are the same thing"
    - "A tautology is not satisfiable because its truth value doesn't depend on any specific assignment"
    - "Every satisfiable formula must be a tautology, since satisfiability requires truth in all cases"
  answer: 0
  explanation: "A tautology is true under every truth assignment — which means it is certainly true under at least one, so it qualifies as satisfiable. But satisfiable only requires truth under at least one assignment. Contingencies (like p → q) are satisfiable but not tautologies, since they are false under some assignments. The relationship is: tautologies ⊂ satisfiable formulas. Contradictions are the only formulas that are unsatisfiable."

- question: "A student claims: 'The formula (p → q) → p is a tautology because it seems obviously reasonable — if p implies q, then p is true.' This claim is:"
  type: multiple-choice
  options:
    - "Correct — the formula holds under every truth assignment"
    - "Incorrect — this is a contingency; when p is false, (p → q) is vacuously true, making (p → q) → p false"
    - "Incorrect — this formula is actually a contradiction"
    - "Correct only when p and q are propositional constants rather than variables"
  answer: 1
  explanation: "This is the classic trap of reasoning from intuition rather than checking all truth assignments. When p = false: (false → q) is true (vacuous implication), so (p → q) → p becomes true → false, which is false. The formula fails on this assignment, making it a contingency, not a tautology. This is why tautology-checking requires systematic verification of all 2ⁿ assignments, not just the plausible-seeming ones."

- question: "If a formula φ is a tautology, then its negation ¬φ must be unsatisfiable."
  type: true-false
  answer: true
  explanation: "This equivalence is fundamental: φ is a tautology (true under every assignment) if and only if ¬φ is false under every assignment (a contradiction), which is exactly what unsatisfiable means. This transformation is practically powerful for proof systems and automated reasoning: checking whether φ is a tautology can be converted into checking whether ¬φ is satisfiable, and vice versa. SAT solvers exploit this duality extensively."

- question: "A satisfiable formula is one that is true under most possible truth assignments."
  type: true-false
  answer: false
  explanation: "False. 'Satisfiable' means true under at least one truth assignment — not all of them. A formula that is true under all assignments is a tautology, which is a strictly stronger condition. Satisfiable formulas include tautologies (all assignments work), contingencies (some work, some don't), but not contradictions (no assignment works). Confusing 'satisfiable' with 'always true' is a common error that conflates two very different concepts."

- question: "What is the practical value of being able to convert the question 'Is φ a tautology?' into 'Is ¬φ satisfiable?' Why might this conversion matter for automated reasoning?"
  type: short-answer
  answer: "Tautology-checking and satisfiability-checking are in principle equivalent problems (one converts to the other by negation), but automated systems — especially SAT solvers — are specialized for satisfiability. By converting a tautology check into an unsatisfiability check on the negation, you can apply highly optimized SAT-solving algorithms to what was originally a validity question. This matters for proof systems, circuit verification, and formal methods, where the question 'is this formula always true?' is central but satisfiability tools are more computationally mature."
  explanation: "The tautology-contradiction-satisfiability triangle is not just a classification system — it is an operational toolkit. Every proof system targets exactly the tautologies. Every SAT solver operates on the satisfiability question. The equivalence between them means progress in one domain directly benefits the other. This is why the relationship is taught not as mere definitional housekeeping but as a conceptually powerful transformation."
```

## Explainer

You know from propositional semantics that a formula's truth value depends on a **truth assignment** — a function mapping each propositional variable to true or false. A formula with n distinct variables has 2ⁿ possible truth assignments. The central classifications of propositional logic ask: what does a formula's truth value look like *across all* those assignments?

A **tautology** (also called a validity) is true under every possible truth assignment — not some, not most, but all of them. The classic example is p ∨ ¬p ("law of excluded middle"): no matter what truth value p takes, one of p and ¬p is true, so the disjunction is always true. A **contradiction** (also called an unsatisfiable formula) is false under every assignment. The example p ∧ ¬p assigns p a value, then requires it to be both true and false simultaneously — impossible. A **contingency** falls in between: true under some assignments, false under others. The formula p → q is contingent: it fails only when p is true and q is false.

The third classification, **satisfiability**, cuts differently: a formula is satisfiable if at least one truth assignment makes it true. Every tautology is satisfiable (all assignments work); every contradiction is unsatisfiable (no assignment works); contingencies are satisfiable but not tautologies. Satisfiability is the focus of SAT solvers and computational complexity — it is the question "can this formula ever be true?" rather than "is this formula always true?"

The most useful transformation here is one you can derive from the logical equivalences you know: φ is a tautology if and only if ¬φ is a contradiction if and only if ¬φ is unsatisfiable. This equivalence is practically powerful because it lets you convert a tautology-checking question into a satisfiability-checking question (and vice versa), which matters for proof systems and automated reasoning. In a proof system, the goal is to derive exactly the tautologies — the formulas whose negations are unsatisfiable, i.e., the ones no consistent assignment can falsify. The semantic target of proof theory is tautology; satisfiability is the complementary concept used to detect when a formula can coherently be false.
