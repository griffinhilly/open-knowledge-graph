---
id: finite-sets-and-finiteness-definition
title: Defining Finite Sets Rigorously
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: set-membership-and-notation
  type: hard
- id: injections-surjections-and-inverse-functions
  type: hard
- id: counting-principles
  type: soft
- id: mathematical-induction
  type: soft
builds-toward:
- recursion-on-finite-structures
- countable-sets-and-enumeration
- natural-numbers-as-iterative-construction
tags:
- finiteness
- cardinality
- characterization
stage: formal-systems
status: draft
---

# Defining Finite Sets Rigorously

## Core Idea
A set S is finite if there exists a bijection between S and {1, 2, ..., n} for some natural number n, or S is empty. Equivalently, S is finite if and only if there is no injection from S into any proper subset of S. This purely set-theoretic definition of finiteness works without relying on prior notion of 'natural number'.
