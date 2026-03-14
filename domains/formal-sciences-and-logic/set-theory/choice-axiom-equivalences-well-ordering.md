---
id: choice-axiom-equivalences-well-ordering
title: The Axiom of Choice and Its Equivalences
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: axiom-of-choice
  type: hard
- id: well-ordering-theorem
  type: hard
- id: ordinal-numbers-and-order
  type: soft
builds-toward:
- martins-axiom-introduction
tags:
- axiom-of-choice
- equivalences
- well-ordering
- zorn
stage: formal-systems
status: draft
---

# The Axiom of Choice and Its Equivalences

## Core Idea
The axiom of choice (AC) has many equivalent formulations: the well-ordering theorem (every set can be well-ordered), Zorn's lemma (maximal elements exist in certain posets), Zermelo's axiom (choice functions exist), and the multiplicative principle (products of nonempty sets are nonempty). Each formulation is intuitively different, yet logically equivalent over ZF. AC is independent of ZF and required for many results (e.g., Hahn-Banach, Tychonoff compactness).

## How It's Best Learned
Prove AC ↔ well-ordering theorem by constructing well-orderings from choice functions. Derive Zorn's lemma from AC via ordinals. Show consistency of each: any ZFC proof can be 'avoided' in ZF+¬AC (e.g., vector spaces need not have bases). Discuss constructive alternatives (DC, AD).

## Common Misconceptions
- Assuming AC is 'obvious' (it is not; it postulates global selection, which is nonconstructive).
- Confusing choice functions (AC) with the ability to choose finitely many items (need only finite axiom of choice).
