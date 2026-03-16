---
id: gibbs-phase-rule-multicomponent
title: Gibbs Phase Rule and Phase Equilibrium
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: pure-substance-phase-diagrams
  type: hard
- id: partial-molar-properties-solutions
  type: hard
builds-toward:
- two-phase-homogeneous-flow-equilibrium
tags:
- phase-rule
- degrees-of-freedom
- multicomponent
- phase-envelope
stage: advanced
status: draft
---

# Gibbs Phase Rule and Phase Equilibrium

## Core Idea
The Gibbs phase rule F = C - P + 2 predicts the degrees of freedom in a system with C components and P phases. For a binary mixture with two phases, one composition can vary freely at fixed T and P. Phase diagrams visualize this: critical points, azeotropes, and phase envelopes dictate separation and equilibrium behavior in distillation and extraction.

## Explainer

From your study of pure-substance phase diagrams, you know that a single-component system (C = 1) can exist as solid, liquid, or vapor. Along the vapor-pressure curve (two phases coexisting), you lose one degree of freedom: fix T and P is determined, or vice versa. At the triple point (three phases), neither T nor P can vary — there are zero degrees of freedom. The **Gibbs phase rule** F = C − P + 2 is the formula that predicts this pattern for any number of components and phases. For a pure substance (C = 1) with two phases (P = 2): F = 1 − 2 + 2 = 1. One variable (say, temperature) can vary freely while the two-phase equilibrium is maintained.

For a **binary mixture** (C = 2) with two coexisting phases, F = 2 − 2 + 2 = 2. You can independently vary both T and P while maintaining vapor-liquid equilibrium. This means the two-phase region is a surface in T-P-composition space, not a curve. Fix T and P and you still have freedom to vary composition — but the compositions of the two phases are set by equilibrium, not freely choosable. This is why vapor-liquid equilibrium in binary systems is presented as a pair of curves (the **bubble-point line** and the **dew-point line**) on a pressure-composition or temperature-composition diagram rather than a single line.

The **bubble-point** is the pressure (or temperature) at which the first bubble of vapor forms as a liquid mixture is depressurized (or heated). The **dew-point** is the pressure at which the first drop of liquid forms as a vapor is compressed. Between these lines lies the two-phase region, often called the **phase envelope**. The key observation from your partial molar properties background is that the vapor and liquid compositions inside this envelope are generally different — this composition split is the thermodynamic basis for distillation. Heating a binary liquid at constant pressure, the vapor that first forms is richer in the more volatile component, and the liquid becomes progressively depleted of it.

An **azeotrope** occurs at a special composition where the vapor and liquid have exactly the same composition — the phase envelope pinches to a point on the T-xy or P-xy diagram. At an azeotrope, F = 2 − 2 + 2 = 2, but the equality of compositions eliminates the useful separation: distillation cannot cross an azeotrope. Ethanol-water is the classic example: the azeotrope at ~95.6% ethanol by mass sets an absolute limit on simple distillation purity. Removing the azeotrope requires a different solvent, pressure-swing distillation, or membrane separation.

With three components (C = 3) and two phases, F = 3 − 2 + 2 = 3, meaning T, P, and one composition variable can all be set independently while the two-phase region persists — giving rise to the triangular ternary phase diagrams used in liquid-liquid extraction design. Adding a third phase (P = 3, C = 3): F = 3 − 3 + 2 = 2. The phase rule's power is that it tells you immediately whether an equilibrium state is unique, part of a family, or impossible without doing any calculation. Before you set up any phase-equilibrium problem, state C and P, apply the rule, and verify that you have exactly F independent constraints — no more, no less.
