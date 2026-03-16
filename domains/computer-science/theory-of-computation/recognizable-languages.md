---
id: recognizable-languages
title: Recognizable Languages and Turing Recognizability
domain: computer-science
course: theory-of-computation
prerequisites:
- id: decidable-languages
  type: hard
builds-toward:
- undecidable-problems
tags:
- recognizable
- semi-decidable
- turing-recognizable
stage: abstract-reasoning
status: draft
---

# Recognizable Languages and Turing Recognizability

## Core Idea
A language is recognizable (or recursively enumerable) if there exists a Turing machine that halts and accepts all strings in the language, but may loop indefinitely on strings outside the language. Not all recognizable languages are decidable; the halting problem is recognizable but not decidable.

## Explainer

You already understand decidable languages — those for which a Turing machine always halts and gives a definitive yes-or-no answer. **Recognizable languages** (also called **recursively enumerable** or **Turing-recognizable** languages) relax this guarantee in a specific way: a recognizer must still halt and accept every string that *is* in the language, but it is allowed to loop forever on strings that are *not* in the language. In other words, a recognizer can reliably say "yes" but might never get around to saying "no."

Think of it like a search process. Suppose you want to know whether a particular mathematical theorem has a proof. You could systematically enumerate all possible proofs, checking each one. If a proof exists, you will eventually find it and halt with "yes." But if no proof exists, you will search forever without ever being certain that you've exhausted all possibilities. This asymmetry — certainty of membership but not of non-membership — is exactly what separates recognizable from decidable. Every decidable language is recognizable (a decider is automatically a recognizer that just never loops), but not every recognizable language is decidable.

The canonical example is the **halting problem**: the language of all ⟨M, w⟩ pairs where Turing machine M halts on input w. You can recognize this language by simply simulating M on w — if M halts, you accept. But if M runs forever, your simulation also runs forever, and you never produce a "no" answer. This is why the halting problem is recognizable but not decidable: there is no machine that can always correctly determine in finite time whether an arbitrary computation will halt.

A useful theorem connects recognizability to decidability: a language is decidable if and only if both it and its complement are recognizable. If you have a recognizer for L and a recognizer for its complement L̄, you can run both in parallel — on any input, exactly one of them will eventually accept, giving you a definitive answer either way. This means that for undecidable but recognizable languages like the halting problem, the complement (the set of non-halting computations) is not even recognizable. There exist languages so far beyond computation that no Turing machine can even partially identify their members.
