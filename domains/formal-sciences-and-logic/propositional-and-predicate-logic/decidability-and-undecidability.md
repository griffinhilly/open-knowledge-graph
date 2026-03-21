---
id: decidability-and-undecidability
title: Decidability and Undecidability
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: formal-arithmetic-and-expressibility
  type: hard
- id: cantor-diagonalization
  type: soft
builds-toward:
- godels-incompleteness-theorems
tags:
- decidability
- undecidability
- halting-problem-formal
- Church-Turing
- decision-procedure
stage: advanced
status: validated
---

# Decidability and Undecidability

## Core Idea
A theory is decidable if there is an algorithm that determines whether any given sentence is a theorem. Propositional logic is decidable (truth tables decide validity). First-order logic is semi-decidable — there is a procedure that halts on all valid sentences but may loop on invalid ones. The first-order theory of arithmetic (true arithmetic) is undecidable by Church's theorem, proved via reduction from the halting problem. Undecidability results are established using diagonalization arguments similar to Cantor's, demonstrating that no consistent recursive axiomatization can decide all arithmetic truths.

## How It's Best Learned
Study the decidability of propositional logic and contrast with the undecidability of FOL validity. Trace Church's reduction: show how a Turing machine computation can be expressed as an arithmetic sentence.

## Common Misconceptions
- Undecidable does not mean unprovable — many individual sentences in an undecidable theory are still provable.
- Semi-decidability (enumerability of theorems) is not the same as decidability.

## Questions

```yaml
- question: "A student concludes that because first-order arithmetic is undecidable, it is impossible to prove that '7 is prime' within arithmetic. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — undecidability means no individual arithmetic sentence can be proved"
    - "First-order arithmetic is actually decidable for simple sentences involving only bounded quantifiers"
    - "Undecidability means no uniform algorithm decides ALL sentences; individual sentences like '7 is prime' can still have proofs"
    - "The student confuses undecidability with inconsistency — undecidable theories prove both a sentence and its negation"
  answer: 2
  explanation: "This is the central misconception. Undecidability is a property of the collection of sentences — no single algorithm halts and correctly answers 'theorem or not?' for every input. But individual sentences can still have proofs found and verified: '7 is prime' has a straightforward formal proof, and Fermat's Last Theorem has a 200-page proof. Undecidability says we cannot automate the separation of all theorems from all non-theorems — not that no particular sentence is provable."

- question: "Which statement correctly distinguishes a decidable theory from a semi-decidable one?"
  type: multiple-choice
  options:
    - "A decidable theory has finitely many theorems; a semi-decidable theory has infinitely many"
    - "In a decidable theory, an algorithm always halts with yes or no for every sentence; in a semi-decidable theory, the algorithm halts on theorems but may loop indefinitely on non-theorems"
    - "Semi-decidability is a stronger property than decidability — semi-decidable theories have richer proof systems"
    - "Decidable and semi-decidable are synonyms — both refer to theories with enumerable theorem sets"
  answer: 1
  explanation: "The key asymmetry: a decision procedure must terminate on ALL inputs with a correct yes or no. A semi-decision procedure only guarantees termination on theorems — it enumerates valid sentences but may loop forever on non-theorems, never producing a 'no.' First-order logic is semi-decidable: proof search will eventually find a proof if one exists, but it may run forever if the sentence is invalid. Option C reverses the relationship: decidability is strictly stronger — every decidable theory is also semi-decidable, but not vice versa."

- question: "Propositional logic is decidable because truth tables provide a finite, always-terminating procedure to determine whether any propositional formula is a tautology."
  type: true-false
  answer: true
  explanation: "A propositional formula has finitely many propositional variables. The truth table for n variables has exactly 2ⁿ rows — a finite number. Evaluating all rows is a mechanical procedure that always terminates. If every row gives True, the formula is a tautology; otherwise it is not. This is the canonical example of a decidable logic: no open cases, no infinite searches, guaranteed termination with a correct yes-or-no answer for every input formula."

- question: "If a formal theory is undecidable, it must also be inconsistent — that is, it derives proofs of both a sentence and its negation."
  type: true-false
  answer: false
  explanation: "Undecidability and inconsistency are completely independent properties. An undecidable theory lacks a uniform algorithm for deciding all sentences; an inconsistent theory derives a contradiction (proves both φ and ¬φ). First-order arithmetic is undecidable (Church's theorem) but consistent — it does not prove contradictions. Conversely, an inconsistent theory trivially 'proves' every sentence, making it degenerate but not in a useful sense of 'decidable.' The two properties do not entail each other in either direction."

- question: "Explain what it means for a theory to be undecidable, without implying that nothing within the theory can be proved."
  type: short-answer
  answer: "A theory is undecidable if there exists no algorithm that, given any sentence of the theory as input, always halts and correctly outputs 'theorem' or 'not a theorem.' This is a claim about the non-existence of a uniform, general-purpose decision procedure for the entire collection of sentences — not a claim about any individual sentence. Many specific sentences in an undecidable theory are provable: a proof can be found, checked, and verified. Undecidability means we cannot write a program that reliably handles all sentences; it says nothing about whether particular proofs exist."
  explanation: "A useful analogy: 'no algorithm detects all malware' (undecidable) does not mean 'no malware can ever be identified.' Specific programs are identified all the time; the undecidability is about the impossibility of a general, always-correct solution for the universal case. Similarly, arithmetic truths are proved constantly — the infinitude of primes, Fermat's Last Theorem — but no algorithm correctly decides all of them. The undecidability result (via reduction from the halting problem) says the collection of arithmetic truths cannot be algorithmically separated from arithmetic falsehoods, even though any particular truth can be singled out and proved."
```

## Explainer

A logic or formal theory is **decidable** if there is an effective procedure — an algorithm that always terminates — which, given any sentence φ in the language, determines whether φ is a theorem. Notice the word "always": the algorithm must halt with a correct yes-or-no answer for every input, not just the easy ones. Propositional logic meets this bar cleanly. Any propositional formula has finitely many propositional variables, and a truth table with 2ⁿ rows evaluates every possible truth assignment. If every row gives "true," the formula is a tautology. The procedure always terminates. Propositional logic is decidable.

First-order logic is harder. The **completeness theorem** tells you that every valid first-order sentence (true in all structures) is provable from the axioms. This gives you a semi-decision procedure: systematically enumerate all proofs in some proof system; if φ is valid, you will eventually find a proof and halt with "yes." But if φ is not valid — if it is false in some structure — the search may run forever. There is no complementary procedure that reliably terminates and says "no, φ is not valid." First-order logic is **semi-decidable**: you can enumerate the valid sentences, but you cannot decide validity in general.

The undecidability of first-order arithmetic (true arithmetic, the set of sentences true in ℕ) goes further: not even the valid sentences of arithmetic can be enumerated by any consistent recursive axiomatization. Church's theorem establishes this via a reduction from the halting problem — the very technique you studied in Cantor's diagonalization argument. The reduction works by encoding Turing machine computations as arithmetic sentences: a machine M halts on input w if and only if a specific arithmetic sentence is true. If arithmetic were decidable, the halting problem would be too, contradicting what you already know is impossible.

The crucial distinction is between **undecidable** and **unprovable**. A theory being undecidable means there is no uniform algorithm that decides all its sentences. But individual sentences within the theory are still provable one at a time: 2 + 2 = 4 has a proof; Fermat's Last Theorem has a proof. Undecidability says the *collection* of theorems cannot be separated from the collection of non-theorems by any algorithm — not that individual proofs cannot be found. This nuance is easy to miss, and keeping it sharp is essential for understanding Gödel's incompleteness theorems, which sit immediately ahead.
