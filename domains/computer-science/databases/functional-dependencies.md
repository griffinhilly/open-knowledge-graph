---
id: functional-dependencies
title: Functional Dependencies
domain: computer-science
course: databases
prerequisites:
- id: relational-model-basics
  type: hard
- id: primary-and-foreign-keys
  type: hard
- id: binary-relations
  type: soft
- id: logical-equivalence
  type: soft
- id: relations-properties-and-types
  type: soft
builds-toward:
- database-normalization-1nf-2nf
- database-normalization-3nf-bcnf
tags:
- functional dependencies
- keys
- candidate keys
- Armstrong's axioms
- normalization theory
stage: formal-systems
status: validated
---

# Functional Dependencies

## Core Idea
A functional dependency X → Y means the value of attribute set X uniquely determines the value of Y: any two tuples agreeing on X must agree on Y. Functional dependencies formalize the concept of a key — K is a superkey if K determines all attributes, and a candidate key if no proper subset of K also determines all attributes. Armstrong's axioms (reflexivity, augmentation, transitivity) form a sound and complete inference system for deriving all logical consequences of a given set of FDs.

## How It's Best Learned
Given a sample table with data anomalies (insertion, update, deletion), identify the functional dependencies that caused them. Practice computing attribute closures under a set of FDs to find all candidate keys.

## Common Misconceptions
- A functional dependency is a data constraint, not a causal relationship — it must hold for all possible instances, not just the current data.
- The left-hand side of an FD can be a set of multiple attributes.
- Having two tuples that happen to agree on X and Y in the current data does not prove X → Y — the FD must hold for all future data too.
