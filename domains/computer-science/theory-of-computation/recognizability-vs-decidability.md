---
id: recognizability-vs-decidability
title: Recognizability vs. Decidability
domain: computer-science
course: theory-of-computation
prerequisites:
- id: halting-problem
  type: hard
builds-toward:
- undecidable-problems
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

## Questions

```yaml
- question: "Suppose language L is Turing-recognizable and its complement L̄ is also Turing-recognizable. What can you conclude?"
  type: multiple-choice
  options:
    - "L is in RE but may or may not be decidable — more information is needed"
    - "L is decidable, because you can run both recognizers in parallel and always get an answer"
    - "L̄ is decidable, but L itself might not be"
    - "Nothing — recognizability of both L and L̄ has no implications for decidability"
  answer: 1
  explanation: "This is the key theorem: L is decidable if and only if both L and L̄ are Turing-recognizable. The proof is constructive: run the recognizer for L and the recognizer for L̄ in parallel on any input. Since every input is either in L or in L̄, one of the two recognizers must eventually accept. Whichever accepts first gives you a definitive yes-or-no answer — and crucially, this parallel simulation always halts. You never loop forever."

- question: "A Turing machine M is given as input along with a string w. You simulate M on w and the simulation runs for 10,000 steps without halting. What can you correctly conclude about HALT_TM?"
  type: multiple-choice
  options:
    - "M does not halt on w — this is evidence that the complement of HALT_TM is recognizable"
    - "You cannot conclude that M will never halt — the recognizer for HALT_TM can loop forever on non-halting inputs, which is why HALT_TM is not decidable"
    - "M eventually halts — 10,000 steps is enough to confirm this"
    - "HALT_TM is co-RE because you can detect non-halting after a finite number of steps"
  answer: 1
  explanation: "This is the core asymmetry of HALT_TM. You can recognize it: if M halts, your simulation eventually terminates and you output 'yes.' But if M loops forever, your simulation loops forever too — you can never output 'no.' No matter how many steps you observe without halting, you cannot rule out that M halts on step 10,001. This is exactly why HALT_TM's complement is not recognizable: confirming that a TM loops forever would require running it forever, which is not a finite computation."

- question: "Every decidable language is Turing-recognizable."
  type: true-false
  answer: true
  explanation: "This follows immediately from definitions. A decider always halts and correctly accepts strings in L and rejects strings not in L. This is strictly stronger than recognition, which only requires accepting strings in L (and allows looping on strings not in L). So any decider is also a recognizer — recognition is a weaker condition. The class of decidable languages is a proper subset of the Turing-recognizable (RE) languages."

- question: "If a language L is Turing-recognizable, then L is expected to be decidable — it just might take a very long time to compute the answer."
  type: true-false
  answer: false
  explanation: "This is the most common misconception in this area. Recognizability does not mean 'slow decidability' — these are categorically different. A recognizer for L can loop forever on inputs not in L; it never produces a 'no' answer for those inputs at all. A decider must halt on every input, including non-members. HALT_TM is the canonical counterexample: it is Turing-recognizable (simulate and wait for halting) but not decidable (there is no algorithm that always halts and correctly answers whether an arbitrary TM halts)."

- question: "Explain why the halting language HALT_TM being in RE but not in co-RE proves it is undecidable."
  type: short-answer
  answer: "A language is decidable if and only if it is in both RE and co-RE. HALT_TM is in RE because you can recognize it: simulate the TM and accept if it halts. But HALT_TM's complement — the set of (M, w) pairs where M does not halt on w — is not recognizable. No Turing machine can confirm that a TM loops forever in finite time. Since HALT_TM is not in co-RE, it is not in the intersection RE ∩ co-RE, and that intersection is exactly the decidable languages. Therefore HALT_TM is undecidable."
  explanation: "The key is that decidability requires being in both RE and co-RE simultaneously. If L is decidable, you can trivially recognize both L and its complement (just run the decider and flip the answer). Conversely, if both L and L̄ are recognizable, run them in parallel to decide. HALT_TM fails because its complement is not recognizable — there's an asymmetry between 'yes' instances (the TM halts, your simulator confirms it) and 'no' instances (the TM loops, your simulator loops with it). That asymmetry is why HALT_TM sits outside the decidable languages."
```

## Explainer

From studying the halting problem, you know that some problems cannot be decided by any Turing machine — there is no algorithm that always halts with the correct yes-or-no answer. But the halting problem is not completely beyond computation: a Turing machine can recognize it. Given a TM description and input, you can simulate the TM and say "yes" if it halts and accepts. The catch is that if the TM loops forever, your simulator loops forever too — it never outputs "no." This asymmetry between "yes" answers and "no" answers is the heart of the distinction between **recognizability** and **decidability**.

A language is **Turing-recognizable** (also called recursively enumerable, or RE) if some Turing machine accepts every string in the language — though it may loop forever on strings not in the language. A language is **decidable** (recursive) if some Turing machine correctly accepts every string in the language and correctly rejects every string not in it, always halting. Decidability is strictly stronger: every decidable language is recognizable, but not every recognizable language is decidable.

The crucial theorem connecting these concepts involves complements. A language L is decidable if and only if both L and its complement L̄ are Turing-recognizable. The intuition is elegant: if you have a recognizer for L and a recognizer for L̄, run them in parallel on any input. One of them must eventually accept (since the input is either in L or in L̄), and whichever accepts first tells you the answer. This parallel simulation always halts, giving you a decider. Conversely, if L is decidable, you can trivially recognize both L and L̄ by running the decider.

This theorem creates a clean landscape of language classes. **RE** contains all Turing-recognizable languages. **co-RE** contains all languages whose complements are recognizable. Their intersection — languages that are both RE and co-RE — is exactly the decidable languages. The halting language HALT_TM sits in RE but outside co-RE: you can recognize it (simulate and wait for halting) but cannot recognize its complement (there is no way to confirm that a TM will loop forever). This placement immediately proves HALT_TM is undecidable, since decidability requires membership in both classes. Whenever you encounter a new problem and want to classify it, the first questions to ask are: is it in RE? Is its complement in RE? The answers place it in this hierarchy and determine whether a decision algorithm can exist.
