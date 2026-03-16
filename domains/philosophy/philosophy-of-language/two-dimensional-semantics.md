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
- modal-status-identity-statements
- direct-reference-theory
tags:
- semantics
- modality
- two-dimensionalism
- meaning
stage: abstract-reasoning
status: draft
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

## Explainer

From your study of possible worlds semantics you know that the **intension** of an expression is a function from possible worlds to extensions — it specifies what the expression picks out in each way the world could be. Rigid designators, as Kripke showed, have the same extension in every possible world: "Aristotle" picks out Aristotle wherever he exists. This created a puzzle: if "Hesperus is Phosphorus" (both names refer to Venus) is necessarily true — true in every possible world — why was it an astronomical discovery? And if "Water is H₂O" is necessary, why did we have to do chemistry to find it out? **Two-dimensional semantics** is the framework designed to resolve this tension by distinguishing two separate dimensions along which meaning operates.

The first distinction, from David Kaplan's work on indexicals, is between **character** and **content**. The word "I" has a stable meaning in the language — it always refers to the speaker of the utterance — but its content (what it picks out) varies depending on who utters it. The character is the rule for determining the content from context; the content is what gets evaluated for truth across possible worlds. Two-dimensional semantics generalizes this: every expression can be evaluated (1) with respect to a possible world considered as **the actual world** (determining which object gets picked out), and (2) with respect to a possible world considered as a **world of evaluation** (asking whether the truth condition holds in that world). These two dimensions can come apart.

The framework gives us two intensions for any expression. The **primary intension** (or "1-intension") evaluates a term at a world considered as actual: it asks, if this world were actual, what would the term pick out? For "water," the primary intension picks out whatever the watery stuff in the actual world turns out to be. The **secondary intension** (or "2-intension") holds the actual reference fixed and evaluates across worlds: since water is H₂O, the secondary intension picks out H₂O in every possible world, making "Water is H₂O" necessary. The a posteriori character of the discovery is explained by the primary intension: there is an epistemically possible world in which the watery stuff turns out not to be H₂O (suppose we had discovered it was XYZ) — the primary intension is contingent even though the secondary intension is necessary. This is what it means for a truth to be **necessary a posteriori**: the secondary intension is invariant across worlds, but the primary intension leaves open what would have been discovered.

Two-dimensional semantics thus reconciles Kripke's modal insights with the classical concern for distinguishing epistemic and metaphysical modality. The **epistemic** dimension tracks what is conceivable or discoverable — what's possible "for all we knew a priori." The **metaphysical** dimension tracks what is genuinely possible in the world, given how things actually are. David Chalmers has extended this framework aggressively, arguing that the two dimensions correspond to a deep duality in the nature of mental content: phenomenal concepts (like your concept of the color red) may have primary intensions that diverge from their secondary intensions in ways that explain why physicalist identity claims always feel like discoveries rather than conceptual truths. Whether or not you accept the extensions, the core framework gives you a precise vocabulary for distinguishing the different ways an expression can "mean" something — and for tracking exactly where Kripke's rigid designation creates the appearance of a priori necessity it does not actually deliver.
