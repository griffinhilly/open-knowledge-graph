---
id: alternating-machines-hierarchy
title: Alternating Turing Machines and the Polynomial Hierarchy
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: nondeterministic-turing-machines
  type: hard
- id: pspace-completeness
  type: soft
builds-toward:
- counting-complexity-sharp-p
tags:
- alternating-machines
- polynomial-hierarchy
- alternation
stage: advanced
status: draft
---

# Alternating Turing Machines and the Polynomial Hierarchy

## Core Idea
Alternating Turing machines extend nondeterminism by allowing both existential (there exists a successor state) and universal (all successor states lead to acceptance) choices. The complexity classes defined by alternating machines form the polynomial hierarchy: Σₖ correspond to k-quantifier alternations starting with existential. Alternation captures the power of interactive reasoning between a prover and verifier.

## How It's Best Learned
Simulate alternating machines on simple problems (e.g., game trees with alternating turns). See how existential and universal states correspond to ∃ and ∀ quantifiers in logic.
