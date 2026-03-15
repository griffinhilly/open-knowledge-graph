---
id: michaelis-menten-enzyme-kinetics
title: Michaelis-Menten Enzyme Kinetics
domain: biology
course: biochemistry
prerequisites:
- id: enzyme-kinetics
  type: hard
- id: enzyme-cofactors-and-coenzymes
  type: soft
- id: limit-definition-of-derivative
  type: soft
- id: equilibrium-expression-kc-kp-constants
  type: hard
- id: rate-law-determination
  type: hard
- id: differential-equations-intro
  type: soft
builds-toward:
- enzyme-inhibition-competitive
- allosteric-enzyme-regulation
tags:
- Michaelis-Menten
- Km
- Vmax
- enzyme kinetics
- steady-state
stage: advanced
status: draft
---

# Michaelis-Menten Enzyme Kinetics

## Core Idea
The Michaelis-Menten equation (v = Vmax × [S] / (Km + [S])) describes enzyme velocity as a function of substrate concentration under steady-state conditions, where the enzyme-substrate complex concentration remains constant. Km (Michaelis constant) reflects the substrate concentration at which the enzyme operates at half-maximal velocity and approximates substrate affinity when the dissociation rate dominates. Vmax is the maximum velocity achieved when all enzyme molecules are saturated with substrate.

## How It's Best Learned
Derive the Michaelis-Menten equation from first principles (rapid equilibrium assumption or steady-state approximation). Plot real enzyme data and extract Km and Vmax from a Lineweaver-Burk (double reciprocal) plot, which linearizes the hyperbolic kinetic curve.

## Common Misconceptions
- Confusing Km with binding affinity; Km includes both association and dissociation rates and is only true affinity under certain conditions.
- Assuming Vmax is achieved at high substrate concentrations for all enzymes; some enzymes show substrate inhibition.
- Treating Michaelis-Menten as universally applicable; allosteric and cooperative enzymes deviate significantly.
