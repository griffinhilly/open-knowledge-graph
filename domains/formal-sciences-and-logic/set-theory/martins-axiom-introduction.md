---
id: martins-axiom-introduction
title: Martin's Axiom and Extensions of ZFC
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: continuum-hypothesis
  type: hard
- id: forcing-intro
  type: soft
builds-toward:
- independence-results-set-theory
- consistency-strength-large-cardinals
tags:
- martins-axiom
- ma
- continuum
- extensions
stage: formal-systems
status: draft
---

# Martin's Axiom and Extensions of ZFC

## Core Idea
Martin's Axiom (MA) states that for any partial order P with the countable chain condition and any collection D of fewer than 𝔠 dense sets, there exists a filter meeting every set in D. MA is consistent with and independent of ZFC + ¬CH. It implies many consequences about the continuum (e.g., no gaps of size ω₁ can remain) and has applications throughout modern set theory.

## How It's Best Learned
Understand the countable chain condition: no antichain exceeds countable size. Apply MA to force dense sets in simple posets (e.g., Baire category). Show that MA implies the failure of certain cardinal inequalities and provides non-constructible sets beyond L.

## Common Misconceptions
- Assuming MA resolves CH (it does not; MA is independent of CH and ZFC).
- Confusing the partial order with the poset of dense sets; both concepts are essential.
