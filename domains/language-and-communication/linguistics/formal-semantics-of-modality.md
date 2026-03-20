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

## Explainer

From your study of semantic types and composition, you know that meaning is built up systematically from the meanings of parts — that expressions denote objects, properties, or truth values, and that composition rules determine how those denotations combine. Modality extends this framework into a new dimension: instead of asking what is true in the actual world, you ask what is true across a **space of possible worlds**. This is the core innovation of possible-worlds semantics, and it gives formal linguists a powerful tool for analyzing sentences like "It might rain" or "You must submit the form."

The fundamental definitions are these: a proposition is **necessarily true** if it is true in *every* world accessible from the current one, and **possibly true** if it is true in *some* accessible world. Think of the current world as a point, and accessibility as a relation that reaches out to other points — other ways things could be or could have been. The sentence "It is possible that unicorns exist" is true just in case there is at least one accessible world where unicorns exist. "It is necessarily true that 2+2=4" is true because in every mathematically coherent world accessible from ours, that arithmetic fact holds. The **accessibility relation** is the mechanism that makes this framework flexible: by changing which worlds count as accessible, you can model different kinds of modality.

This is where the system gets its real power. Different modal flavors — **epistemic** (what's possible given what we know), **deontic** (what's obligatory or permitted given rules), **circumstantial** (what's possible given physical circumstances), **bouletic** (what's possible given desires) — all use the same possible-worlds machinery, but with different accessibility relations. "You must leave" in a deontic reading accesses worlds consistent with the relevant rules or norms; in an epistemic reading, it accesses worlds consistent with the speaker's evidence. The word *must* is the same; the accessibility relation shifts. Formally, if *R* is the accessibility relation and *w* is the evaluation world, then □φ (necessarily φ) is true at *w* iff φ is true at all worlds *v* such that *wRv*, and ◇φ (possibly φ) is true at *w* iff φ is true at some such *v*.

Your prerequisite in modal semantics introduced the intuitions behind necessity and possibility. The formal semantics machinery makes those intuitions precise enough to run compositional analyses — the same kind you already know from semantic types. A modal operator like *must* or *might* is a quantifier over worlds: *must* is a universal quantifier (∀w: accessible(w) → φ(w)), and *might* is an existential quantifier (∃w: accessible(w) ∧ φ(w)). This connects modality directly to quantifier semantics, which means the tools you've already built — type theory, functional application, lambda abstraction — apply directly. The remaining challenge is specifying the accessibility relation correctly for each modal context, which is what different modal systems (K, S4, S5, etc.) are doing when they impose constraints on that relation.
