---
id: modal-semantics-possible-worlds
title: Modal Semantics and Possible Worlds
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: possible-worlds-semantics
  type: hard
- id: modal-logic-intro
  type: hard
builds-toward:
- temporal-semantics-and-tense
- counterfactual-conditionals
tags:
- modality
- possible-worlds
- necessity
- semantics
stage: advanced
status: draft
---

# Modal Semantics and Possible Worlds

## Core Idea
Modal sentences involving necessity and possibility are analyzed using possible worlds: a sentence is necessarily true iff true at all possible worlds; possibly true iff true at some accessible world. This extends truth-conditional semantics to modal discourse by adding a dimension of possible alternatives.

## How It's Best Learned
Understand accessibility relations and how different modal logics (K, S4, S5) correspond to different properties of accessibility. Work through simple modal sentences and their truth conditions across worlds.

## Explainer

Modal language — "necessarily," "possibly," "could have been," "must" — is pervasive but semantically opaque without a framework. What does it even mean to say something is necessary? From your study of possible worlds semantics and modal logic, you know the fundamental setup: a **possible world** is a complete way reality could be or could have been. The actual world is one possible world — the way things are. Other worlds are the ways things might have been. Modal semantics cashes out necessity and possibility as quantification over these worlds.

The core semantic clauses are elegant. A sentence is **necessarily true** if and only if it is true at every possible world accessible from the world of evaluation. It is **possibly true** if and only if it is true at some accessible world. The notion of an **accessibility relation** is what differentiates modal logics. If every world accesses every other, we get S5 — the logic typically used for metaphysical modality, where what's necessarily true is so in all worlds without restriction. If accessibility is reflexive but not symmetric (every world accesses itself, but not necessarily every other), we get different systems. Your modal logic background lets you see that formal axioms correspond to properties of accessibility: the T axiom ("if necessarily p, then p") corresponds to reflexivity — every world accesses itself, so what's necessary in this world is true here.

The philosophical significance goes beyond formal elegance. Possible worlds semantics gives a uniform account of **de dicto** and **de re** modality — the difference between necessity attributed to a proposition versus necessity attributed to an object's property. "Necessarily, the number of planets is greater than seven" (de dicto) is false: in some worlds, there are fewer planets. "Eight necessarily has the property of being greater than seven" (de re) is true: in every world, eight exceeds seven. The analysis uses **rigid designators** — terms like numerals and proper names that pick out the same object in every world — versus non-rigid descriptions like "the number of planets." Kripke's insight was that names are rigid while descriptions often are not, which explains why "Aristotle was necessarily Aristotle" is true but "Aristotle was necessarily the teacher of Alexander" is not.

The framework extends naturally to **counterfactual conditionals**: "if it had rained, the match would have been canceled" is true at a world w if and only if the closest worlds to w where it rained are worlds where the match was canceled. "Closest" is measured by a similarity ordering — Lewis's account uses exactly this structure. Possible worlds semantics thus serves triple duty: it formalizes modal logic, provides truth conditions for modal language in natural language, and underpins the semantics of counterfactuals. Understanding the unifying role of this framework — how a single ontological apparatus addresses questions from logic, language, and metaphysics simultaneously — is what makes it central to contemporary analytic philosophy.

