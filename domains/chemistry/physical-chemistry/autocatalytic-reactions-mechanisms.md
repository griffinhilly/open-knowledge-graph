---
id: autocatalytic-reactions-mechanisms
title: Autocatalytic Reactions and Nonlinear Kinetics
domain: chemistry
course: physical-chemistry
prerequisites:
- id: reaction-mechanisms-elementary-steps
  type: hard
- id: michaelis-menten-enzyme-kinetics
  type: soft
tags:
- autocatalysis
- nonlinear
- kinetics
- oscillation
stage: advanced
status: draft
---

# Autocatalytic Reactions and Nonlinear Kinetics

## Core Idea
Autocatalytic reactions are accelerated by their own products, creating sigmoidal rate curves and often complex dynamics. Classic examples include the BZ reaction and the iodine-clock reaction. Autocatalysis can produce oscillations, traveling waves, and chaos—nonlinear phenomena absent in simple reactions. These reactions are important in oscillatory biochemical cycles, combustion, and understanding complex chemical behavior.

## Explainer

In the reaction mechanisms you have studied so far, the rate depends on reactant concentrations — as reactants are consumed, the reaction slows down. **Autocatalytic reactions** break this pattern: a product of the reaction accelerates its own formation, so the rate increases as the reaction proceeds. The simplest example is A + B → 2B, where species B catalyzes its own production. Initially, when B concentration is low, the reaction is slow. As B accumulates, the rate accelerates. Eventually, reactant A is depleted and the rate drops again. This produces the characteristic **sigmoidal (S-shaped) concentration curve** — slow start, rapid acceleration, then leveling off — fundamentally different from the exponential decay of simple first-order kinetics.

The mathematical reason autocatalysis produces such different behavior is that the rate law contains a product of reactant and product concentrations: rate = k[A][B]. This makes the differential equation **nonlinear** — the rate depends on the very quantity being produced. In enzyme kinetics (your prerequisite), you encountered nonlinearity in the Michaelis-Menten equation, but autocatalysis adds a qualitatively new feature: positive feedback. The system amplifies small perturbations rather than damping them, which is why autocatalytic systems can exhibit behaviors impossible in linear kinetics.

When autocatalytic steps are embedded in reaction networks with competing pathways and feedback loops, the system can produce **chemical oscillations** — concentrations that rise and fall periodically rather than approaching equilibrium monotonically. The **Belousov-Zhabotinsky (BZ) reaction** is the iconic example: a cerium-catalyzed bromate-malonate system in which the solution visibly oscillates between yellow and colorless (or produces striking spiral waves in a thin layer). The mechanism involves autocatalytic production of bromous acid (HBrO₂) coupled with a delayed inhibitory pathway, creating the conditions for sustained oscillation.

These phenomena — oscillation, bistability, traveling waves, and even deterministic chaos — emerge from the interplay of autocatalysis, inhibition, and time delays. They are not exotic curiosities: autocatalysis is central to combustion ignition (radical chain branching), biological pattern formation (morphogen gradients), and the origin-of-life problem (self-replicating molecular systems). The key insight is that once a reaction can accelerate itself, the simple picture of monotonic approach to equilibrium breaks down, and the tools of nonlinear dynamics become necessary to understand the system's behavior.
