---
id: energy-balance-models
title: Energy Balance Models of Climate
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: radiative-transfer-atmospheric
  type: hard
- id: solar-radiation-and-earth-energy-balance
  type: hard
- id: first-law-of-thermodynamics
  type: soft
- id: radiation-heat-transfer-stefan-boltzmann
  type: soft
- id: fundamental-theorem-of-calculus-part-1
  type: soft
builds-toward:
- radiative-forcing-definition
- climate-sensitivity-radiative-feedbacks
- general-circulation-models
tags:
- model
- energy
- balance
- temperature
- feedback
stage: advanced
status: validated
---

# Energy Balance Models of Climate

## Core Idea
Energy balance models (EBMs) represent Earth's climate by balancing incoming solar radiation with outgoing thermal radiation, allowing computation of equilibrium temperature. The simplest zero-dimensional model treats Earth as a single box with uniform temperature; more sophisticated 1D and 2D versions include latitudinal or spatial variation. EBMs reveal how changes in atmospheric composition, albedo, and solar output alter global mean temperature and are computationally efficient for exploring climate feedback mechanisms.

## How It's Best Learned
Begin by deriving the zero-dimensional model with no feedbacks and calculate equilibrium temperature. Then add latitudinal structure and feedbacks (albedo, water vapor) incrementally, observing how model complexity and realism increase.

## Common Misconceptions
Energy balance does not mean temperatures are static; it means energy input equals energy output at equilibrium. Also, EBMs are illustrative tools, not predictions; they show principle but neglect spatial heterogeneity and transient dynamics.

## Questions

```yaml
- question: "In a zero-dimensional energy balance model, if Earth's surface albedo increases (e.g., due to expanding ice cover), what happens to the equilibrium temperature?"
  type: multiple-choice
  options: ["It increases, because ice reflects energy back into the atmosphere and warms it", "It decreases, because more incoming solar radiation is reflected away and less energy is absorbed", "It stays the same, because the model enforces energy balance by definition", "It increases, because outgoing longwave radiation decreases proportionally"]
  answer: 1
  explanation: "Higher albedo means a greater fraction of incoming solar radiation is reflected rather than absorbed. With less energy input, the equilibrium temperature must decrease for outgoing infrared radiation (which scales as T⁴) to balance the reduced absorbed solar flux. This is the physical basis of the ice-albedo feedback: more ice → higher albedo → lower equilibrium temperature → more ice."

- question: "In an energy balance model, achieving 'equilibrium' means Earth's surface temperature is perfectly constant and does not fluctuate over time."
  type: true-false
  answer: false
  explanation: "Equilibrium in an EBM means the long-term average energy input equals the long-term average energy output — not that temperature is instantaneously static. Real climate exhibits year-to-year variability, seasonal cycles, and transient fluctuations even around an equilibrium state. EBMs describe the mean state toward which climate tends, not a moment-by-moment balance."

- question: "In the zero-dimensional EBM, why is the incoming solar flux divided by 4 when computing Earth's equilibrium temperature?"
  type: short-answer
  answer: "Earth intercepts solar radiation as a disk of area πR², but radiates infrared energy from its entire spherical surface of area 4πR². Dividing by 4 spreads the intercepted solar energy over the full surface, giving the effective solar input per unit area as S/4."
  explanation: "The solar constant S (watts per square meter) is measured at Earth's orbital distance facing the Sun. To find the energy absorbed per unit of Earth's surface, you must account for the geometry: only the cross-section (πR²) faces the Sun, but the whole sphere (4πR²) radiates. The ratio 4πR²/πR² = 4 is where the factor comes from. Without this, you would compute an equilibrium temperature much too high."
```

## Explainer

You already know from studying radiative transfer and Earth's energy balance that the planet absorbs solar radiation and emits infrared radiation, and that these two fluxes must balance on long timescales or the climate would warm or cool indefinitely. Energy balance models (EBMs) take this principle and turn it into a quantitative tool: they write down an equation for energy input and output, set them equal, and solve for the temperature that makes them balance.

The simplest version is the zero-dimensional (0D) EBM, which treats the entire Earth as a single point with one uniform temperature T. The energy absorbed by Earth per unit surface area is S(1−α)/4, where S ≈ 1361 W/m² is the solar constant, α is Earth's albedo (fraction of sunlight reflected), and the factor of 4 accounts for the geometry of a sphere intercepting sunlight as a disk. The energy emitted back to space is σT⁴ (Stefan-Boltzmann law), where ε is an emissivity factor accounting for the greenhouse effect. Setting these equal and solving for T gives an equilibrium temperature — the temperature at which the planet neither gains nor loses net energy.

What makes this model powerful despite its simplicity is that it reveals how equilibrium temperature depends on key parameters. If albedo α increases (more reflective surface — e.g., more ice), the absorbed solar flux decreases and T must fall to maintain balance. If the effective emissivity ε decreases (stronger greenhouse effect), outgoing radiation is reduced and T must rise to compensate. These sensitivities are the mathematical basis for climate feedbacks: mechanisms that change α or ε in response to temperature change, either amplifying (positive feedback) or damping (negative feedback) the initial perturbation.

Higher-dimensional EBMs add spatial structure. A one-dimensional EBM resolves latitude, allowing each latitude band to have its own temperature and albedo, with heat transported between bands by the atmosphere and ocean. This captures the ice-albedo feedback more realistically — high-latitude cooling leads to ice expansion, increasing albedo there — and reproduces the observed pattern of greater warming at the poles. These latitudinal models were historically important for predicting that polar regions warm faster than the tropics under increased CO₂.

It is critical to understand what EBMs are and are not. They are conceptual and diagnostic tools that isolate specific mechanisms — energy balance, albedo, greenhouse forcing — in a transparent way. They are not forecasting tools: they neglect clouds, ocean circulation, regional geography, and the time-dependent response of the climate system. When you move on to general circulation models (GCMs), you will see how these neglected processes are added back in at the cost of vastly greater computational complexity. The EBM is where intuition is built before that complexity is confronted.

