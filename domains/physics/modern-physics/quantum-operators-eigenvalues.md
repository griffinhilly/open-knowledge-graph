---
id: quantum-operators-eigenvalues
title: Quantum Operators and Eigenvalues
domain: physics
course: modern-physics
prerequisites:
- id: probability-amplitude-interpretation
  type: hard
builds-toward:
- classical-limit-correspondence
- uncertainty-relation-measurements
tags:
- quantum-mechanics
- operators
stage: advanced
status: draft
---

# Quantum Operators and Eigenvalues

## Core Idea
In quantum mechanics, physical observables (position, momentum, energy) are represented by Hermitian operators. When an operator Â acts on an eigenstate |ψ⟩, it returns the same state multiplied by a scalar eigenvalue: Â|ψ⟩ = a|ψ⟩. The eigenvalue is the unique result obtained when measuring the observable on that eigenstate; the set of all eigenvalues of an operator comprises the possible measurement outcomes.

## How It's Best Learned
Learn the position and momentum operators in 1D: x̂ and p̂ = −iℏ d/dx. Apply them to simple wavefunctions and eigenstates; compute expectation values for particles in boxes.

## Common Misconceptions
- Operators are not numbers; they are mathematical objects that transform states.
- Eigenvalues of Hermitian operators are always real, but eigenstates are generally complex.
- The eigenvalue equation Âψ = aψ holds only for eigenstates, not arbitrary states.
