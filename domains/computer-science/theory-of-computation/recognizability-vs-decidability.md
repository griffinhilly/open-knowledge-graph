---
id: recognizability-vs-decidability
title: Recognizability vs. Decidability
domain: computer-science
course: theory-of-computation
prerequisites:
- id: halting-problem
  type: hard
builds-toward:
- undecidability-reductions
tags:
- RE
- co-RE
- recognizable
- decidable
- complement
stage: advanced
status: validated
---

# Recognizability vs. Decidability

## Core Idea
A language is decidable if and only if both it and its complement are Turing-recognizable. This gives a useful test: if a language is recognizable but its complement is not, it cannot be decidable. The class of Turing-recognizable languages (RE) and the class of co-RE languages (complements of RE) overlap exactly at the decidable languages. HALT_TM is in RE but not co-RE (its complement is not recognizable), confirming its undecidability. Understanding this landscape is essential for classifying computational problems.

## Common Misconceptions
- Thinking every recognizable language is decidable — recognizability is strictly weaker.
- Confusing the complement of a language with the complement of a complexity class — co-RE is not the same as 'not RE'.

## Explainer

From studying the halting problem, you know that some problems cannot be decided by any Turing machine — there is no algorithm that always halts with the correct yes-or-no answer. But the halting problem is not completely beyond computation: a Turing machine can recognize it. Given a TM description and input, you can simulate the TM and say "yes" if it halts and accepts. The catch is that if the TM loops forever, your simulator loops forever too — it never outputs "no." This asymmetry between "yes" answers and "no" answers is the heart of the distinction between **recognizability** and **decidability**.

A language is **Turing-recognizable** (also called recursively enumerable, or RE) if some Turing machine accepts every string in the language — though it may loop forever on strings not in the language. A language is **decidable** (recursive) if some Turing machine correctly accepts every string in the language and correctly rejects every string not in it, always halting. Decidability is strictly stronger: every decidable language is recognizable, but not every recognizable language is decidable.

The crucial theorem connecting these concepts involves complements. A language L is decidable if and only if both L and its complement L̄ are Turing-recognizable. The intuition is elegant: if you have a recognizer for L and a recognizer for L̄, run them in parallel on any input. One of them must eventually accept (since the input is either in L or in L̄), and whichever accepts first tells you the answer. This parallel simulation always halts, giving you a decider. Conversely, if L is decidable, you can trivially recognize both L and L̄ by running the decider.

This theorem creates a clean landscape of language classes. **RE** contains all Turing-recognizable languages. **co-RE** contains all languages whose complements are recognizable. Their intersection — languages that are both RE and co-RE — is exactly the decidable languages. The halting language HALT_TM sits in RE but outside co-RE: you can recognize it (simulate and wait for halting) but cannot recognize its complement (there is no way to confirm that a TM will loop forever). This placement immediately proves HALT_TM is undecidable, since decidability requires membership in both classes. Whenever you encounter a new problem and want to classify it, the first questions to ask are: is it in RE? Is its complement in RE? The answers place it in this hierarchy and determine whether a decision algorithm can exist.
