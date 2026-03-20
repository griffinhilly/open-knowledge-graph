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

## Explainer

A logic or formal theory is **decidable** if there is an effective procedure — an algorithm that always terminates — which, given any sentence φ in the language, determines whether φ is a theorem. Notice the word "always": the algorithm must halt with a correct yes-or-no answer for every input, not just the easy ones. Propositional logic meets this bar cleanly. Any propositional formula has finitely many propositional variables, and a truth table with 2ⁿ rows evaluates every possible truth assignment. If every row gives "true," the formula is a tautology. The procedure always terminates. Propositional logic is decidable.

First-order logic is harder. The **completeness theorem** tells you that every valid first-order sentence (true in all structures) is provable from the axioms. This gives you a semi-decision procedure: systematically enumerate all proofs in some proof system; if φ is valid, you will eventually find a proof and halt with "yes." But if φ is not valid — if it is false in some structure — the search may run forever. There is no complementary procedure that reliably terminates and says "no, φ is not valid." First-order logic is **semi-decidable**: you can enumerate the valid sentences, but you cannot decide validity in general.

The undecidability of first-order arithmetic (true arithmetic, the set of sentences true in ℕ) goes further: not even the valid sentences of arithmetic can be enumerated by any consistent recursive axiomatization. Church's theorem establishes this via a reduction from the halting problem — the very technique you studied in Cantor's diagonalization argument. The reduction works by encoding Turing machine computations as arithmetic sentences: a machine M halts on input w if and only if a specific arithmetic sentence is true. If arithmetic were decidable, the halting problem would be too, contradicting what you already know is impossible.

The crucial distinction is between **undecidable** and **unprovable**. A theory being undecidable means there is no uniform algorithm that decides all its sentences. But individual sentences within the theory are still provable one at a time: 2 + 2 = 4 has a proof; Fermat's Last Theorem has a proof. Undecidability says the *collection* of theorems cannot be separated from the collection of non-theorems by any algorithm — not that individual proofs cannot be found. This nuance is easy to miss, and keeping it sharp is essential for understanding Gödel's incompleteness theorems, which sit immediately ahead.
