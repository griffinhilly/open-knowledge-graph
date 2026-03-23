---
id: two-dimensional-semantics
title: Two-Dimensional Semantics
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: possible-worlds-semantics
  type: hard
- id: compositionality-principle
  type: soft
- id: modal-logic-intro
  type: soft
builds-toward:
  - direct-reference-theory
tags:
- semantics
- modality
- two-dimensionalism
- meaning
stage: formal-systems
status: validated
---
# Two-Dimensional Semantics

## Core Idea
Two-dimensional semantics analyzes meaning by separating intension (what varies across possible worlds) from extension (actual reference). This framework explains how identity statements can be necessary a posteriori (like "H2O is water") while remaining epistemically contingent. By treating both the way we determine reference and what is actually referred to, it reconciles insights from Kripke about necessity with classical semantics about meaning.

## How It's Best Learned
Start with simple examples of identity statements ("Water is H2O", "Hesperus is Phosphorus") and map out both how we discovered they were true and why they're necessary. Practice building models where extension diverges from intension, then study how Kaplan's framework handles characters versus contents.

## Common Misconceptions
- Thinking two-dimensionalism itself determines truth-values; it's a framework for tracking meaning distinctions.
- Confusing epistemic possibility (how things could be for all we knew) with metaphysical possibility.
- Assuming all necessary truths must be a priori; two-dimensionalism shows otherwise.

## Questions

```yaml
- question: "The statement 'Water is H₂O' is necessary a posteriori. In two-dimensional semantic terms, this means:"
  type: multiple-choice
  options:
    - "Its primary intension is necessary (the same across all worlds considered as actual) while its secondary intension is contingent"
    - "Its secondary intension is necessary (true in every world of evaluation), while its primary intension is contingent (could pick out something other than H₂O in an epistemically possible world)"
    - "Both its primary and secondary intensions are necessary, making it knowable a priori after all"
    - "The statement is actually contingent because we could have discovered water was XYZ"
  answer: 1
  explanation: "The secondary intension holds actual reference fixed: since water is in fact H₂O, in every possible world we evaluate, water (= H₂O) is H₂O — necessary. But the primary intension asks what 'water' would pick out if a given world were actual. In an epistemically possible world where the watery stuff turns out to be XYZ, the primary intension picks out XYZ — contingent. The a posteriori character comes from the primary dimension: we had to investigate the actual world to discover which watery substance we were referring to."

- question: "In Kaplan's framework, the 'character' of the indexical 'I' is best described as:"
  type: multiple-choice
  options:
    - "A rigid designator: it picks out the same individual in every possible world"
    - "A rule that takes a context of utterance and returns the speaker as the semantic content"
    - "The specific individual picked out, which varies depending on which world is being evaluated"
    - "An empty placeholder with no semantic value until a speaker fills it in"
  answer: 1
  explanation: "In Kaplan's two-level framework, character is a function from contexts to contents. The character of 'I' is the linguistic rule: 'refers to the speaker of this utterance.' This rule is stable across all contexts. But the content — the actual person picked out — varies with the context of utterance. Once content is fixed, it is then evaluated for truth across possible worlds. Two-dimensional semantics generalizes this character/content split to all expressions, not just indexicals."

- question: "Two-dimensional semantics implies that all necessary truths must be knowable a priori."
  type: true-false
  answer: false
  explanation: "The whole point of two-dimensional semantics is to explain necessary a posteriori truths — statements that are metaphysically necessary (true in all worlds at the secondary intension level) yet not knowable without empirical investigation (contingent at the primary intension level). 'Water is H₂O' and 'Hesperus is Phosphorus' are paradigm cases. Two-dimensionalism separates metaphysical modality (which intension is necessary) from epistemic modality (which intension is knowable a priori), showing they can come apart."

- question: "The primary intension of 'water' picks out H₂O in every epistemically possible world considered as actual."
  type: true-false
  answer: false
  explanation: "The primary intension of 'water' picks out whatever the watery stuff turns out to be in whichever world is considered actual. It is a description-like function: 'the watery substance in the actual world.' In an epistemically possible world where the watery stuff is XYZ rather than H₂O, the primary intension picks out XYZ. This is precisely how two-dimensionalism explains why 'Water is H₂O' was a discovery: the primary intension is contingent, leaving open which substance is water until investigation determines it."

- question: "Explain in your own words why 'Water is H₂O' counts as necessary but not a priori in two-dimensional semantics."
  type: short-answer
  answer: "It is necessary because the secondary intension holds actual reference fixed: since water in our world is H₂O, across every possible world of evaluation, the thing that is actually water (H₂O) is H₂O — true everywhere. It is not a priori because the primary intension is contingent: there are epistemically possible worlds where the watery stuff is XYZ, and we cannot rule this out from the armchair. We had to do chemistry to discover which world we inhabit. The two dimensions come apart: secondary-intension necessity coexists with primary-intension contingency, producing a truth that is both metaphysically necessary and discovered empirically."
  explanation: "This is the two-dimensionalist resolution of Kripke's puzzle about necessary a posteriori truths. The apparent paradox disappears once you distinguish the dimension along which reference is fixed (the primary intension, tracking epistemic possibilities) from the dimension along which truth is evaluated (the secondary intension, tracking metaphysical possibilities)."
```

## Explainer

From your study of possible worlds semantics you know that the **intension** of an expression is a function from possible worlds to extensions — it specifies what the expression picks out in each way the world could be. Rigid designators, as Kripke showed, have the same extension in every possible world: "Aristotle" picks out Aristotle wherever he exists. This created a puzzle: if "Hesperus is Phosphorus" (both names refer to Venus) is necessarily true — true in every possible world — why was it an astronomical discovery? And if "Water is H₂O" is necessary, why did we have to do chemistry to find it out? **Two-dimensional semantics** is the framework designed to resolve this tension by distinguishing two separate dimensions along which meaning operates.

The first distinction, from David Kaplan's work on indexicals, is between **character** and **content**. The word "I" has a stable meaning in the language — it always refers to the speaker of the utterance — but its content (what it picks out) varies depending on who utters it. The character is the rule for determining the content from context; the content is what gets evaluated for truth across possible worlds. Two-dimensional semantics generalizes this: every expression can be evaluated (1) with respect to a possible world considered as **the actual world** (determining which object gets picked out), and (2) with respect to a possible world considered as a **world of evaluation** (asking whether the truth condition holds in that world). These two dimensions can come apart.

The framework gives us two intensions for any expression. The **primary intension** (or "1-intension") evaluates a term at a world considered as actual: it asks, if this world were actual, what would the term pick out? For "water," the primary intension picks out whatever the watery stuff in the actual world turns out to be. The **secondary intension** (or "2-intension") holds the actual reference fixed and evaluates across worlds: since water is H₂O, the secondary intension picks out H₂O in every possible world, making "Water is H₂O" necessary. The a posteriori character of the discovery is explained by the primary intension: there is an epistemically possible world in which the watery stuff turns out not to be H₂O (suppose we had discovered it was XYZ) — the primary intension is contingent even though the secondary intension is necessary. This is what it means for a truth to be **necessary a posteriori**: the secondary intension is invariant across worlds, but the primary intension leaves open what would have been discovered.

Two-dimensional semantics thus reconciles Kripke's modal insights with the classical concern for distinguishing epistemic and metaphysical modality. The **epistemic** dimension tracks what is conceivable or discoverable — what's possible "for all we knew a priori." The **metaphysical** dimension tracks what is genuinely possible in the world, given how things actually are. David Chalmers has extended this framework aggressively, arguing that the two dimensions correspond to a deep duality in the nature of mental content: phenomenal concepts (like your concept of the color red) may have primary intensions that diverge from their secondary intensions in ways that explain why physicalist identity claims always feel like discoveries rather than conceptual truths. Whether or not you accept the extensions, the core framework gives you a precise vocabulary for distinguishing the different ways an expression can "mean" something — and for tracking exactly where Kripke's rigid designation creates the appearance of a priori necessity it does not actually deliver.
