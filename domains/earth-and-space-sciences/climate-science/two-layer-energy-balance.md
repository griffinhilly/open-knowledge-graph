---
id: two-layer-energy-balance
title: Two-Layer Energy Balance Model
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: energy-balance-models
  type: hard
- id: radiative-convective-equilibrium
  type: hard
- id: surface-energy-balance
  type: soft
builds-toward:
- general-circulation-models
- climate-models-and-projections
tags:
- energy-balance
- modeling
- climate-response
- temperature-structure
stage: advanced
status: draft
---

# Two-Layer Energy Balance Model

## Core Idea
A two-layer model divides the climate system into a surface and an atmosphere, each with a temperature. This simplified model captures the essential physics that atmospheric back-radiation increases surface temperature while maintaining radiative balance to space. Despite its simplicity, it reproduces key climate sensitivities and feedback mechanisms, making it useful for understanding how atmospheric properties control surface warming.

## Explainer

From your work with energy balance models, you understand that Earth's temperature adjusts until incoming solar radiation equals outgoing longwave radiation. The simplest version — a single-layer model — treats the entire planet as one object with one temperature and gets surprisingly close to reality, but it cannot explain why Earth's surface is warmer than the single-layer prediction. The **two-layer energy balance model** solves this by splitting the system into two interacting components: a surface layer and an atmospheric layer, each with its own temperature and energy budget.

The key insight is that the atmosphere is partly transparent to incoming shortwave solar radiation but partly opaque to outgoing longwave (infrared) radiation emitted by the surface. In the model, the surface absorbs solar energy and radiates infrared upward. The atmospheric layer absorbs some fraction of that outgoing infrared — determined by its **emissivity**, which depends on greenhouse gas concentration — and then radiates energy both upward to space and back downward toward the surface. This **back-radiation** is the mechanism behind the greenhouse effect. The surface receives energy from two sources: the sun and the atmosphere above it. Because it receives more total energy than in the single-layer case, it must warm to a higher equilibrium temperature to radiate enough energy to balance its budget.

Writing out the energy balance equations for each layer makes the physics concrete. The atmosphere must be in radiative equilibrium: the infrared it absorbs from below must equal the total infrared it emits (upward plus downward). The surface must also balance: absorbed solar radiation plus atmospheric back-radiation must equal the surface's upward infrared emission. Solving these two coupled equations simultaneously yields both temperatures. When atmospheric emissivity is zero (no greenhouse gases), the model collapses back to the simple one-layer case. As emissivity increases toward one, the surface temperature rises — quantifying how greenhouse gas concentration controls warming.

Despite having only two layers and no convection, winds, or ocean currents, this model captures the essential **climate sensitivity** concept: how much surface temperature changes per unit change in atmospheric properties. You can perturb the model — increase emissivity to simulate adding CO₂ — and calculate the resulting surface warming. This is the conceptual foundation for understanding climate feedbacks in more complex general circulation models. The two-layer model also reveals why the stratosphere cools when the troposphere warms under increased greenhouse forcing: the atmospheric layer must still radiate enough energy to space, but with more back-radiation going downward, the upper layer's temperature adjusts differently than the surface. This counterintuitive result, confirmed by observations, emerges naturally from the two-layer framework.
