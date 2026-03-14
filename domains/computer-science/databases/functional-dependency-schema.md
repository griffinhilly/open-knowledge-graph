---
id: functional-dependency-schema
title: Functional Dependencies and Database Design
domain: computer-science
course: databases
prerequisites:
- id: relational-data-model
  type: hard
- id: primary-key-foreign-key-constraints
  type: soft
builds-toward:
- normalization-first-second-third
tags:
- functional dependency
- FD
- candidate key
- superkey
stage: formal-systems
status: draft
---

# Functional Dependencies and Database Design

## Core Idea
A functional dependency (FD) is a constraint stating that if two rows have the same value in attribute A, they must have the same value in attribute B (written A → B). Functional dependencies identify candidate keys and guide normalization. Understanding FDs is essential for eliminating data redundancy.

## How It's Best Learned
Identify functional dependencies in real-world scenarios, determine candidate keys from FD sets, and use FD analysis to guide schema design toward higher normal forms.
