---
id: formal-semantics-of-modality
title: Formal Semantics of Modality and Possibility
domain: language-and-communication
course: linguistics
prerequisites:
- id: semantic-types-and-composition
  type: hard
- id: modal-semantics-necessity-possibility
  type: soft
tags:
- semantics
- modality
- possible-worlds
stage: advanced
status: draft
---

# Formal Semantics of Modality and Possibility

## Core Idea
Modal logic formalizes modality using possible worlds: a sentence is necessarily true if it holds in all accessible worlds, possibly true if it holds in some. Accessibility relations between worlds encode different modal systems (deontic, epistemic, etc.).

## Questions

```yaml
- question: "'You must leave now' can mean either 'It is obligatory that you leave' or 'I conclude from the evidence that you must be leaving.' How does possible-worlds semantics account for this ambiguity?"
  type: multiple-choice
  options:
    - "The sentence has two separate lexical entries for 'must' — one deontic, one epistemic — that happen to be phonologically identical"
    - "The ambiguity is pragmatic, not semantic — context determines which meaning applies without any formal difference"
    - "The same operator □ applies in both readings, but the accessibility relations differ: deontic accesses worlds consistent with norms/rules; epistemic accesses worlds consistent with the speaker's evidence"
    - "The deontic reading uses universal quantification over worlds while the epistemic reading uses existential quantification"
  answer: 2
  explanation: "This is the power of possible-worlds semantics: the formal operator □ (necessarily) is uniform across modal flavors. What changes between 'You must leave' (deontic) and 'You must be leaving' (epistemic) is the accessibility relation — which worlds count as relevant. For deontic modality, accessible worlds are those consistent with the relevant rules or norms; for epistemic modality, accessible worlds are those consistent with the speaker's knowledge or evidence. The word 'must' is identical; the relation determines the interpretation. This unification is what makes the framework powerful — one logical tool analyzes many natural language phenomena."

- question: "In possible-worlds semantics, what is the truth condition for 'It might rain tomorrow' (epistemic reading)?"
  type: multiple-choice
  options:
    - "'It rains tomorrow' is true in the actual world"
    - "'It rains tomorrow' is true in every world accessible from the current world given what the speaker knows"
    - "'It rains tomorrow' is true in at least one world accessible from the current world given what the speaker knows"
    - "'It rains tomorrow' is true in the majority of worlds accessible from the current world"
  answer: 2
  explanation: "◇φ (possibly φ) is true at world w iff there exists at least one world v such that wRv and φ is true at v. 'Might' is an existential quantifier over accessible worlds — it requires only one accessible world where it rains. This contrasts with □φ (necessarily φ / 'must'), which requires rain in *all* accessible worlds. The common error is thinking 'might' means something weaker than its formal definition — e.g., 'probably' or 'more likely than not.' Formally, 'might' asserts only that the complement of one accessible world is non-empty, which is a much weaker claim."

- question: "'It is necessarily true that 2+2=4' means the same thing as 'It is actually true that 2+2=4' — both are asserting truth in the world we inhabit."
  type: true-false
  answer: false
  explanation: "Necessary truth and actual truth are categorically different claims. 'It is actually true that 2+2=4' asserts truth at the evaluation world. 'It is necessarily true that 2+2=4' asserts truth at *all* worlds accessible from this one. A claim can be actually true without being necessarily true: 'It is actually true that the US has 50 states' holds in the actual world, but there are accessible worlds where different political history produced a different number. Conversely, necessary truths (logical and mathematical) hold across all mathematically coherent worlds. This distinction is fundamental to understanding why necessary truth is a stronger and categorically different claim than actual truth."

- question: "In formal modal semantics, the operators □ (necessarily) and ◇ (possibly) function as quantifiers over possible worlds — □ as universal quantification and ◇ as existential quantification over worlds accessible via the accessibility relation."
  type: true-false
  answer: true
  explanation: "This is the core formal insight: □φ is true at w iff φ is true at all v such that wRv (universal quantification over accessible worlds); ◇φ is true at w iff φ is true at some v such that wRv (existential quantification). This connects modality directly to standard quantifier semantics, meaning that the tools already in the formal semanticist's toolkit — type theory, lambda abstraction, functional application — apply to modal analysis. It also makes clear why 'must' and 'might' are duals: ◇φ ≡ ¬□¬φ, just as ∃x Px ≡ ¬∀x ¬Px."

- question: "Why does formal modal semantics need an accessibility relation, and how does varying it allow the same logical framework to analyze both epistemic and deontic modality?"
  type: short-answer
  answer: "The accessibility relation specifies which possible worlds are 'relevant' when evaluating a modal claim at a given world — which worlds the quantification ranges over. Without it, 'necessarily' would mean 'true in all possible worlds whatsoever,' which is too strong for most natural language uses of 'must' and 'might.' By varying the accessibility relation, the same formal operators model different modal flavors: for epistemic modality, accessible worlds are those consistent with the agent's knowledge or evidence; for deontic modality, accessible worlds are those consistent with the relevant norms or rules; for circumstantial modality, accessible worlds are those consistent with physical circumstances. The word 'must' is formally identical across all uses — what shifts is the set of worlds over which the universal quantifier ranges, determined by the accessibility relation."
  explanation: "This question targets the key architectural insight of possible-worlds semantics: a single formal apparatus with one variable parameter (the accessibility relation) can model the full diversity of modal meaning in natural language. Students often think different modal flavors require completely different theories; the elegance is that they require only different specifications of one relation."
```

## Explainer

From your study of semantic types and composition, you know that meaning is built up systematically from the meanings of parts — that expressions denote objects, properties, or truth values, and that composition rules determine how those denotations combine. Modality extends this framework into a new dimension: instead of asking what is true in the actual world, you ask what is true across a **space of possible worlds**. This is the core innovation of possible-worlds semantics, and it gives formal linguists a powerful tool for analyzing sentences like "It might rain" or "You must submit the form."

The fundamental definitions are these: a proposition is **necessarily true** if it is true in *every* world accessible from the current one, and **possibly true** if it is true in *some* accessible world. Think of the current world as a point, and accessibility as a relation that reaches out to other points — other ways things could be or could have been. The sentence "It is possible that unicorns exist" is true just in case there is at least one accessible world where unicorns exist. "It is necessarily true that 2+2=4" is true because in every mathematically coherent world accessible from ours, that arithmetic fact holds. The **accessibility relation** is the mechanism that makes this framework flexible: by changing which worlds count as accessible, you can model different kinds of modality.

This is where the system gets its real power. Different modal flavors — **epistemic** (what's possible given what we know), **deontic** (what's obligatory or permitted given rules), **circumstantial** (what's possible given physical circumstances), **bouletic** (what's possible given desires) — all use the same possible-worlds machinery, but with different accessibility relations. "You must leave" in a deontic reading accesses worlds consistent with the relevant rules or norms; in an epistemic reading, it accesses worlds consistent with the speaker's evidence. The word *must* is the same; the accessibility relation shifts. Formally, if *R* is the accessibility relation and *w* is the evaluation world, then □φ (necessarily φ) is true at *w* iff φ is true at all worlds *v* such that *wRv*, and ◇φ (possibly φ) is true at *w* iff φ is true at some such *v*.

Your prerequisite in modal semantics introduced the intuitions behind necessity and possibility. The formal semantics machinery makes those intuitions precise enough to run compositional analyses — the same kind you already know from semantic types. A modal operator like *must* or *might* is a quantifier over worlds: *must* is a universal quantifier (∀w: accessible(w) → φ(w)), and *might* is an existential quantifier (∃w: accessible(w) ∧ φ(w)). This connects modality directly to quantifier semantics, which means the tools you've already built — type theory, functional application, lambda abstraction — apply directly. The remaining challenge is specifying the accessibility relation correctly for each modal context, which is what different modal systems (K, S4, S5, etc.) are doing when they impose constraints on that relation.
