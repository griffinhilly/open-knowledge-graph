---
id: adjoint-functor-theorem
title: The General Adjoint Functor Theorem
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: adjoint-functors
  type: hard
- id: limits-and-colimits
  type: hard
builds-toward:
- kan-extensions
- topos-theory-intro
tags:
- adjoint
- theorem
- representability
- preservation
- completeness
stage: advanced
status: draft
---

# The General Adjoint Functor Theorem

## Core Idea
The General Adjoint Functor Theorem states that a functor G: D → C has a left adjoint if and only if G preserves limits and satisfies the solution set condition (roughly: the class of solutions to a lifting problem forms a set). This theorem transforms adjoint existence into verifiable structural properties. It provides a systematic approach to constructing adjoints and is central to existence proofs in algebra and topology.

## How It's Best Learned
Study the proof using the solution set condition and verify its application to familiar functors (forgetful functors, localization). Explore what happens when hypotheses fail and how the theorem guides explicit adjoint construction.

## Common Misconceptions
The solution set condition is subtle and may be difficult to verify directly; sufficient conditions are often used in practice. Adjoint existence is guaranteed but may not yield explicit descriptions of the adjoint. The theorem applies to left adjoints; right adjoints require dual conditions.
