---
id: lever-rule
title: The Lever Rule and Phase Fraction Calculation
domain: engineering
course: materials-science
prerequisites:
- id: phase-diagrams-binary
  type: hard
- id: proportions
  type: soft
builds-toward:
- iron-carbon-phase-diagram
- heat-treatment-of-steels
tags:
- lever-rule
- phase-fraction
- composition
- two-phase
stage: formal-systems
status: validated
---

# The Lever Rule and Phase Fraction Calculation

## Core Idea
In a two-phase region of a binary phase diagram, the lever rule quantifies the relative amounts (mass fractions) of each phase present at a given overall composition and temperature. By reading the phase boundary compositions on either side of the overall composition and applying a simple inverse-proportion calculation — like a mechanical lever balanced at the overall composition — engineers can determine how much solid vs. liquid (or two distinct solid phases) is present. This calculation is fundamental to predicting microstructure after solidification or heat treatment.

## How It's Best Learned
Practice on the Pb-Sn eutectic diagram at several temperatures and overall compositions. Verify that the calculated fractions sum to 1 and that limiting cases (at a phase boundary) give 100% of one phase.

## Common Misconceptions
- The lever rule gives mass fractions of phases, not mole fractions of components — students frequently confuse these.
- The rule applies only inside two-phase regions; in single-phase regions the composition of the phase equals the overall composition.

## Questions

```yaml
- question: "A Pb-Sn alloy with overall composition C₀ = 60 wt% Sn sits in a two-phase (α + β) region at temperature T. The α-phase boundary is at Cα = 20 wt% Sn and the β-phase boundary is at Cβ = 80 wt% Sn. What is the mass fraction of the β phase?"
  type: multiple-choice
  options:
    - "33% — calculated as the distance from C₀ to Cβ divided by the total two-phase field width"
    - "67% — calculated as the distance from Cα to C₀ divided by the total two-phase field width"
    - "60% — equal to the overall alloy composition"
    - "40% — the remaining fraction after subtracting the alloy composition from 100%"
  answer: 1
  explanation: "f_β = (C₀ − Cα)/(Cβ − Cα) = (60 − 20)/(80 − 20) = 40/60 ≈ 67%. The β fraction equals the distance from the overall composition to the LEFT (α) boundary, divided by the total two-phase field width — the OPPOSITE side, not the β side. This inverse proportion is the most common error: students intuitively reach for the distance to the β boundary, but that gives f_α. The mechanical lever analogy clarifies it: the fraction of β is proportional to the arm length on the α side of the fulcrum (overall composition)."

- question: "As an alloy cools through a two-phase (solid + liquid) region from the liquidus toward the solidus on a binary phase diagram, what happens to the solid fraction?"
  type: multiple-choice
  options:
    - "It remains constant because the overall alloy composition does not change"
    - "It jumps discontinuously at the eutectic temperature from 0 to 1"
    - "It increases continuously as the lever rule shifts with each decrement in temperature"
    - "It decreases because cooling removes the thermal energy needed to maintain solidification"
  answer: 2
  explanation: "At the liquidus, the alloy is 100% liquid (f_solid = 0). At the solidus, it is 100% solid (f_solid = 1). Between these temperatures, the phase boundaries shift continuously with temperature, so applying the lever rule at each temperature shows the solid fraction increasing continuously. The overall composition is fixed (it is the composition of the alloy you started with), but the RELATIVE AMOUNTS of liquid and solid change at every temperature as solidification proceeds. This continuous change is the basis for Scheil solidification models."

- question: "The lever rule gives the composition of each phase in a two-phase region — for example, it tells you what percentage of Sn is dissolved in the α phase at a given temperature."
  type: true-false
  answer: false
  explanation: "False — this is a common and important confusion. The compositions of each phase are read directly from the phase boundaries on the phase diagram at the relevant temperature: Cα is where the left boundary intersects the temperature line, Cβ is where the right boundary does. These are given by the thermodynamics of the system. The lever rule then uses those fixed boundary compositions and the overall alloy composition to calculate how much of each phase is present. Composition of phases (from phase boundaries) and amount of phases (from lever rule) are two distinct pieces of information from two different readings of the diagram."

- question: "The lever rule applies only within a two-phase region of a binary phase diagram; in a single-phase region, all the material has the composition of the overall alloy."
  type: true-false
  answer: true
  explanation: "True. In a single-phase region, only one phase is present, so that phase's composition must equal the overall alloy composition by definition — there is no second phase with a different composition to lever between. The lever rule requires two coexisting phases with different compositions (the two endpoints of the lever arm) and an overall composition located between them. At a phase boundary, one phase fraction goes to zero and the other to 100%, giving the correct limiting behavior. Applying the lever rule in a single-phase region is physically meaningless."

- question: "Explain why the lever rule uses an inverse proportion — why is the mass fraction of the β phase calculated using the distance from the overall composition to the α boundary, rather than the distance to the β boundary?"
  type: short-answer
  answer: "The lever rule is derived from mass balance: the overall composition must equal the weighted average of the two phase compositions (C₀ = f_α · Cα + f_β · Cβ). For this equation to be satisfied, a composition C₀ that is close to Cβ must have a large f_β — so the 'weight' assigned to β must be large when C₀ is near Cβ. That weight (f_β) is measured by how far C₀ is from the α boundary, not the β boundary. The longer the arm on the α side of the fulcrum, the more β is needed to balance — just like a mechanical lever."
  explanation: "The limiting cases confirm the inverse logic: if C₀ = Cβ (at the β boundary), f_β = (Cβ − Cα)/(Cβ − Cα) = 1 — the alloy is 100% β, as it should be. If C₀ = Cα, f_β = 0 — all α. Students who mistakenly use the direct distance (C₀ to Cβ) would calculate f_β = 0 when C₀ = Cβ, which is physically wrong. The mass balance derivation makes the inverse proportion inevitable: the phase you have MORE of is the one whose boundary your overall composition is FARTHER from, not closer to."
```

## Explainer

A binary phase diagram tells you which phases are stable at a given temperature and overall composition. From your study of phase diagrams, you know how to read the phase boundaries and identify whether you are in a single-phase region or a two-phase region. What the diagram does not directly tell you is *how much* of each phase is present. That is exactly what the **lever rule** provides: a quantitative statement about the relative amounts of two coexisting phases derived from mass balance.

The physical reasoning is straightforward. Suppose you have a binary alloy of overall composition C₀ that lies in a two-phase (α + β) region at some temperature. Reading the phase diagram at that temperature, you find that the α phase has composition Cα (the left boundary) and the β phase has composition Cβ (the right boundary). The overall composition must be a weighted average of the two phase compositions: C₀ = f_α · Cα + f_β · Cβ, where f_α and f_β are the mass fractions (and f_α + f_β = 1). Solving these two equations gives **f_β = (C₀ − Cα)/(Cβ − Cα)** and **f_α = (Cβ − C₀)/(Cβ − Cα)**. Notice that each fraction is the distance from the overall composition to the *opposite* boundary, divided by the total two-phase field width — exactly like balancing a mechanical lever, with the overall composition as the fulcrum.

The analogy is worth visualizing: draw the two-phase field as a horizontal bar at the relevant temperature, with Cα on the left and Cβ on the right. Place the fulcrum (overall composition C₀) somewhere in the middle. The fraction of β is the length of the left arm (C₀ − Cα) divided by the total bar length (Cβ − Cα); the fraction of α is the right arm (Cβ − C₀) divided by the same total. A composition close to Cβ produces mostly β; a composition close to Cα produces mostly α. At exactly a phase boundary, you get 100% of one phase, which is the correct limiting behavior.

In practice, the lever rule is applied at every temperature during solidification to track how much solid and liquid are present as an alloy cools through a two-phase region. At the liquidus, the alloy is 100% liquid; at the solidus, 100% solid. Between them, the solid fraction increases continuously, and the lever rule tells you the fraction at each temperature. This quantitative picture connects directly to **Scheil solidification** models and to predicting **segregation** — the degree to which the first solid to form differs in composition from the last, which sets the severity of compositional gradients in a cast part. The lever rule is the foundation for all such microstructural predictions from phase diagrams.
