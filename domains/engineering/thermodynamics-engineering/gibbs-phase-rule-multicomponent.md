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

## Questions

```yaml
- question: "A binary mixture (C=2) exists in vapor-liquid equilibrium (P=2 phases). You fix both temperature and pressure. According to the Gibbs phase rule, what remains free?"
  type: multiple-choice
  options:
    - "Nothing — fixing T and P completely determines all compositions in both phases"
    - "One composition variable — but fixing one composition immediately sets all others by the phase rule and equilibrium conditions"
    - "Two composition variables — both vapor and liquid compositions can independently vary"
    - "The number of phases — you can still add a third phase at fixed T and P"
  answer: 1
  explanation: "For a binary two-phase system: F = C − P + 2 = 2 − 2 + 2 = 2. With two degrees of freedom and T and P already fixed, exactly one more variable can vary — but here's the subtlety: while composition is 'free' in the sense of one degree of freedom, fixing the composition of one phase immediately determines the composition of the other through the equilibrium condition (equal chemical potentials). So F=2 means T, P, and compositions are not all independently choosable, but two of them can vary simultaneously while two-phase equilibrium is maintained. Option A is the common misconception: fixing T and P does NOT fully determine compositions in a binary two-phase system — that would require F=0, which needs three phases (C=2, P=4 is impossible by the rule)."

- question: "Ethanol and water form an azeotrope at approximately 95.6% ethanol by mass. A distillation column is being used to purify an 80% ethanol solution. What is the maximum purity achievable by simple distillation?"
  type: multiple-choice
  options:
    - "100% ethanol, since distillation always enriches the more volatile component"
    - "95.6% ethanol — the azeotropic composition, beyond which the vapor and liquid have identical compositions and no further separation occurs"
    - "80% ethanol — the starting composition; distillation cannot enrich below the azeotrope point"
    - "The maximum depends only on the number of theoretical stages in the column, with no absolute thermodynamic limit"
  answer: 1
  explanation: "An azeotrope is a special composition where the vapor and liquid in equilibrium have exactly the same composition. At this point, the phase envelope pinches to a single point on the T-xy diagram, and the relative volatility becomes 1. Distillation separates components by exploiting the difference in vapor and liquid compositions — when these are equal, there is nothing to separate. Simple distillation starting at 80% can concentrate ethanol up to 95.6% but cannot cross the azeotrope. To exceed 95.6% purity requires breaking the azeotrope with a third component (extractive distillation), pressure-swing distillation (azeotrope composition shifts with pressure), or a membrane."

- question: "For a binary mixture (C=2) in two-phase equilibrium, fixing temperature completely determines the pressure and the compositions of both phases."
  type: true-false
  answer: false
  explanation: "F = C − P + 2 = 2 − 2 + 2 = 2 for a binary two-phase system. Fixing temperature uses one degree of freedom, leaving one more — pressure can still vary independently. Unlike a pure substance (C=1, P=2, F=1) where fixing T on the vapor-pressure curve automatically sets P, a binary system has an extra degree of freedom from its composition. The two-phase region in binary systems is a surface in T-P-composition space, not a curve. You must fix both T and P to constrain the compositions of both phases (and even then, fixing one composition determines the other through phase equilibrium, not independently)."

- question: "Adding a third phase to a binary system (C=2, increasing P from 2 to 3) reduces the degrees of freedom from 2 to 1."
  type: true-false
  answer: true
  explanation: "Applying the Gibbs phase rule: with C=2 components and P=3 phases coexisting, F = 2 − 3 + 2 = 1. This means only one variable (either T or P, but not both) can be independently varied while maintaining three-phase equilibrium. The three-phase line (or 'eutectic line' in a solid-liquid-vapor context) is exactly this: a line in T-P space (F=1) rather than an area (F=2) or a point (F=0). Adding phases reduces freedom because each additional equilibrium condition (equal chemical potentials between phases) removes a degree of freedom from the system."

- question: "What does a 'degree of freedom' mean in the context of the Gibbs phase rule, and why does adding a phase reduce the number of degrees of freedom rather than increase it?"
  type: short-answer
  answer: "A degree of freedom is an intensive variable (temperature, pressure, or composition) that can be independently varied without changing the number of phases in equilibrium. The Gibbs phase rule F = C − P + 2 counts these. Adding a phase reduces degrees of freedom because each additional phase introduces new equilibrium constraints: for two phases to coexist, the chemical potential of every component must be equal in both phases. Adding a third phase adds C more equality constraints (one per component, equal in the third phase), each of which eliminates one degree of freedom. The system becomes more constrained — fewer variables can be freely adjusted while all the equilibrium conditions remain satisfied simultaneously. A triple point (pure substance, three phases) has F=0 precisely because all three equilibrium constraints (solid-liquid, liquid-vapor, solid-vapor) are active simultaneously, leaving no freedom to vary T or P."
  explanation: "A useful analogy: degrees of freedom in a mechanical system count how many ways it can move. Adding a rigid joint removes a degree of freedom by imposing a constraint. In thermodynamics, adding a coexisting phase imposes equilibrium constraints that have the same effect."
```

## Explainer

From your study of pure-substance phase diagrams, you know that a single-component system (C = 1) can exist as solid, liquid, or vapor. Along the vapor-pressure curve (two phases coexisting), you lose one degree of freedom: fix T and P is determined, or vice versa. At the triple point (three phases), neither T nor P can vary — there are zero degrees of freedom. The **Gibbs phase rule** F = C − P + 2 is the formula that predicts this pattern for any number of components and phases. For a pure substance (C = 1) with two phases (P = 2): F = 1 − 2 + 2 = 1. One variable (say, temperature) can vary freely while the two-phase equilibrium is maintained.

For a **binary mixture** (C = 2) with two coexisting phases, F = 2 − 2 + 2 = 2. You can independently vary both T and P while maintaining vapor-liquid equilibrium. This means the two-phase region is a surface in T-P-composition space, not a curve. Fix T and P and you still have freedom to vary composition — but the compositions of the two phases are set by equilibrium, not freely choosable. This is why vapor-liquid equilibrium in binary systems is presented as a pair of curves (the **bubble-point line** and the **dew-point line**) on a pressure-composition or temperature-composition diagram rather than a single line.

The **bubble-point** is the pressure (or temperature) at which the first bubble of vapor forms as a liquid mixture is depressurized (or heated). The **dew-point** is the pressure at which the first drop of liquid forms as a vapor is compressed. Between these lines lies the two-phase region, often called the **phase envelope**. The key observation from your partial molar properties background is that the vapor and liquid compositions inside this envelope are generally different — this composition split is the thermodynamic basis for distillation. Heating a binary liquid at constant pressure, the vapor that first forms is richer in the more volatile component, and the liquid becomes progressively depleted of it.

An **azeotrope** occurs at a special composition where the vapor and liquid have exactly the same composition — the phase envelope pinches to a point on the T-xy or P-xy diagram. At an azeotrope, F = 2 − 2 + 2 = 2, but the equality of compositions eliminates the useful separation: distillation cannot cross an azeotrope. Ethanol-water is the classic example: the azeotrope at ~95.6% ethanol by mass sets an absolute limit on simple distillation purity. Removing the azeotrope requires a different solvent, pressure-swing distillation, or membrane separation.

With three components (C = 3) and two phases, F = 3 − 2 + 2 = 3, meaning T, P, and one composition variable can all be set independently while the two-phase region persists — giving rise to the triangular ternary phase diagrams used in liquid-liquid extraction design. Adding a third phase (P = 3, C = 3): F = 3 − 3 + 2 = 2. The phase rule's power is that it tells you immediately whether an equilibrium state is unique, part of a family, or impossible without doing any calculation. Before you set up any phase-equilibrium problem, state C and P, apply the rule, and verify that you have exactly F independent constraints — no more, no less.
