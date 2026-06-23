---
id: propositional-logic-introduction
title: Introduction to Propositional Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: set-fundamentals
  type: soft
- id: boolean-algebra
  type: soft
- id: if-then-statements
  type: soft
- id: true-and-false-statements
  type: hard
- id: variables-in-logic
  type: soft
builds-toward:
- propositional-connectives
- truth-assignments-and-valuations
- logical-implication-entailment
tags:
- foundations
- propositional-logic
- introduction
stage: formal-systems
status: validated
---

# Introduction to Propositional Logic

## Core Idea
Propositional logic studies the structure of logical arguments using propositions and logical connectives. A proposition is a statement that is either true or false. The goal is to develop a formal system for reasoning about propositions without considering their content—only their truth values and how they combine.

## How It's Best Learned
Start by examining simple propositions and how they combine with connectives. Work through natural language arguments and formalize them into propositional notation.

## Common Misconceptions
Confusing natural language 'and' with logical AND (natural 'and' often carries temporal meaning). Thinking the truth value depends on real-world facts rather than component truth values.

## Questions

```yaml
- question: "Which of the following is a proposition in the logical sense?"
  type: multiple-choice
  options:
    - "Close the door!"
    - "Is it raining?"
    - "Either the light is on or the light is off."
    - "This sentence is false."
  answer: 2
  explanation: "A proposition must be a declarative statement with a definite truth value. Commands (option A) and questions (option B) are not truth-apt. 'Either the light is on or the light is off' is a tautology — true by the law of excluded middle — making it a valid proposition. The paradoxical sentence in option D is self-referential in a way that produces no stable truth value, disqualifying it as a well-formed proposition in classical propositional logic."

- question: "In propositional logic, the truth value of a compound statement like 'P AND Q' depends on understanding what P and Q actually mean in the real world."
  type: true-false
  answer: false
  explanation: "This is the central feature — and the power — of propositional logic: truth values are determined entirely by the truth values of the component propositions, not by their content or meaning. If P is true and Q is false, then 'P AND Q' is false regardless of whether P means 'It is raining' or 'The Pythagorean theorem holds'. Logic is formal, not semantic."

- question: "What distinguishes a proposition from a sentence, and why does this distinction matter for building a formal logical system?"
  type: short-answer
  answer: "A sentence is a grammatical unit of language; a proposition is the abstract content of a declarative sentence that has a definite truth value. The distinction matters because the same proposition can be expressed by different sentences (in different languages or phrasings), and the same sentence can fail to express a proposition (if it is a question, command, or paradox). Formal logic operates on propositions — truth-bearing objects — not on sentences, which allows the system to be language-independent and unambiguous."
  explanation: "This abstraction is what makes propositional logic a 'formal' system: by stripping away linguistic content and working only with truth values, we can prove things about the structure of valid arguments that hold universally, regardless of subject matter. The sentence/proposition distinction is the first step in that formalization."
```

## Explainer

Propositional logic is the simplest formal system for reasoning rigorously about truth. Its core move is to abstract away the content of statements entirely and work only with their truth values. You begin with propositions — declarative statements that are either true or false, like "It is raining" or "5 is prime" — and combine them using logical connectives: AND, OR, NOT, and IF...THEN. The resulting compound statements have truth values determined purely by the truth values of their components, following fixed rules regardless of what the propositions are actually about.

If you have studied set theory, you already have useful intuition here. Propositions are like sets of possible worlds — the set of situations in which the proposition is true. Logical AND corresponds to intersection: "P AND Q" is true in worlds where both P and Q hold. Logical OR corresponds to union: "P OR Q" is true in any world where at least one holds. NOT corresponds to complement. The parallel is not accidental — Boolean algebra, set theory, and propositional logic are deeply related formal structures.

The most important thing to internalize early is that logical connectives are not the same as their natural language counterparts. In English, "I ate dinner and went to bed" implies a temporal sequence. In logic, "P AND Q" says nothing about order — it is simply true when both P and Q are true simultaneously. Similarly, logical OR is inclusive: "P OR Q" is true even when both are true, which differs from how "or" often functions in everyday speech ("coffee or tea?" typically means one, not both). The formal system forces you to be precise in ways natural language does not require.

A proposition must have a definite truth value. This excludes questions, commands, and self-referential statements like "This sentence is false." The last case — called the Liar Paradox — reveals a genuine limitation of classical logic: assigning either truth value leads to contradiction. Classical propositional logic avoids this by requiring propositions to be truth-apt, stable, and non-self-referential. The study of what to do about paradoxes has driven important research in logic, but propositional logic sidesteps them cleanly by simply not admitting such sentences as propositions.

With these foundations — propositions, connectives, and truth values — you can build truth tables that exhaustively show the behavior of any compound statement, prove that arguments are valid or invalid, and identify tautologies (statements true in all cases) and contradictions (statements false in all cases). This is the beginning of formal reasoning, and every more advanced logical system you encounter — predicate logic, modal logic, type theory — builds directly on this foundation.
