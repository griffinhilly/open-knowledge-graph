---
id: joint-inversion-gravity-seismics
title: Joint Inversion of Gravity and Seismic Data
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: gravity-surveys-and-data-inversion
  type: hard
- id: seismic-tomography-velocity-imaging
  type: hard
tags:
- inversion
- gravity
- seismic
- joint-inversion
stage: expert
status: draft
---

# Joint Inversion of Gravity and Seismic Data

## Core Idea
Gravity and seismic data constrain different physical properties (density and seismic velocity) and can be combined in joint inversions to construct more robust models of subsurface structure. Gravity adds depth sensitivity beyond seismic surveys and provides independent constraints on density; seismics provides detailed velocity structure. Joint inversion reduces model ambiguity and improves interpretability.

## Questions

```yaml
- question: "A geophysicist inverts gravity data alone to determine the depth of a sedimentary basin and obtains multiple equally valid depth models. What is the fundamental reason for this non-uniqueness?"
  type: multiple-choice
  options:
    - "The gravity survey used too few stations to adequately cover the basin area"
    - "Many different subsurface density distributions can produce identical surface gravity fields — the inverse problem is inherently ill-posed from gravity data alone"
    - "Gravity measurements are not sufficiently precise to distinguish between different basin depths"
    - "Gravity inversion only works when the basin is flat; irregular basement topography always causes non-uniqueness"
  answer: 1
  explanation: "This is a fundamental mathematical property of potential field inversion, not a data-quality problem. The surface gravity field is the integral of the 3D density distribution — many different distributions can produce the same integral. Infinite thin-sheet models, finite thick-body models, and everything in between can match the same gravity data. Options 0 and 2 attribute the problem to insufficient data when the issue is inherent ill-posedness: even perfect, infinitely dense gravity measurements cannot uniquely resolve the 3D density structure."

- question: "In a petrophysically coupled joint inversion, the velocity-density relationship breaks down in a gas-saturated reservoir. What is the likely consequence?"
  type: multiple-choice
  options:
    - "The inversion fails completely and cannot produce any model in the gas zone"
    - "The inversion may produce erroneously low density estimates in the gas zone, because gas lowers velocity without proportionally reducing density"
    - "Structural coupling would exhibit the same failure, since it also depends on the velocity-density relationship"
    - "Gas saturation increases both velocity and density proportionally, so the standard relationship still holds in this case"
  answer: 1
  explanation: "Gas dramatically reduces seismic velocity by lowering the bulk modulus of the rock, while having relatively little effect on density. If the inversion enforces a standard empirical relationship (like Gardner's relation) that predicts density from velocity, it will infer anomalously low density from the anomalously low velocity — mischaracterizing the reservoir. This is a known limitation of petrophysically coupled inversion. Structural coupling (option 2) is unaffected because it makes no assumption about the velocity-density relationship; it only requires structural boundaries to coincide in both models."

- question: "Joint inversion reduces model non-uniqueness by requiring the subsurface model to simultaneously satisfy two datasets that each respond to different physical properties."
  type: true-false
  answer: true
  explanation: "This is the core principle. Gravity constrains density distributions; seismics constrains velocity distributions. Each imposes independent constraints on different regions of model space. The intersection of models acceptable to both datasets is much smaller than the set acceptable to either alone. Even without a known empirical relationship between velocity and density, the simultaneous requirement to satisfy independent observations substantially shrinks the space of permissible models — which is the practical goal of joint inversion."

- question: "Structural (cross-gradient) coupling in joint inversion enforces that seismic velocity and density must have the same numerical values at each point in the model."
  type: true-false
  answer: false
  explanation: "Structural coupling requires that the spatial gradients of velocity and density are parallel — meaning structural boundaries and discontinuities appear in the same locations in both models. It says nothing about the absolute values or ratios of the two properties. A granite body might appear as a high-velocity, high-density anomaly, or as a moderate-velocity, very-high-density anomaly — either is acceptable as long as the boundary between granite and surrounding rock appears at the same position in both models. This flexibility is structural coupling's key advantage over petrophysical coupling."

- question: "Explain why joint inversion of gravity and seismic data produces more tightly constrained models than either dataset inverted separately, even when no empirical velocity-density relationship is assumed."
  type: short-answer
  answer: "Each dataset independently constrains a different physical property of the same subsurface volume. Gravity restricts which density distributions are compatible with the observed surface gravity field. Seismic data restricts which velocity distributions are compatible with observed travel times. Any acceptable joint model must simultaneously satisfy both constraint sets. Even without knowing how velocity and density relate numerically, requiring that a single physical volume explains both datasets eliminates the large space of density models that fit gravity alone but are inconsistent with the seismic velocity structure, and vice versa. Structural coupling adds the further requirement that anomalies and boundaries coincide spatially in both property fields, further eliminating physically implausible models."
  explanation: "The key insight is that two independent observational constraints, even qualitative ones, multiplicatively reduce the acceptable model space. If 1,000 density models fit the gravity data and 1,000 velocity models fit the seismic data, only a small subset of each set is mutually consistent — and that intersection is the result of joint inversion. The more independent the two datasets' sensitivities, the greater the reduction in non-uniqueness."
```

## Explainer

From your work with gravity data inversion, you know that gravity measurements constrain density structure but suffer from severe non-uniqueness — many different subsurface density distributions can produce the same surface gravity field. From seismic tomography, you know that travel-time data constrain velocity structure with good spatial resolution but can have limited sensitivity to certain rock properties. **Joint inversion** combines these two complementary datasets into a single inversion framework, producing a model that must simultaneously satisfy both gravity and seismic observations. The result is more tightly constrained than either method alone could achieve.

The physical basis for joint inversion is the empirical relationship between seismic velocity and density. In most crustal rocks, velocity and density covary — denser rocks generally have higher seismic velocities. This correlation has been quantified through relationships like **Nafe-Drake** curves (for marine sediments), **Birch's law** (for crystalline rocks), and **Gardner's relation** (ρ ≈ aV^0.25 for sedimentary rocks). These empirical links mean that a velocity model and a density model of the same region should be mutually consistent. Joint inversion enforces this consistency by coupling the two parameter fields through a shared constraint — either a direct petrophysical relationship or a structural similarity requirement.

There are two main approaches to joint inversion. In **petrophysically coupled** inversion, the velocity-density relationship is built directly into the forward model: when the algorithm adjusts velocity in a cell, the density changes accordingly (or vice versa). This is powerful when the empirical relationship is well established, but it can fail in unusual lithologies where the standard relationships break down (e.g., gas-saturated sediments have low velocity but moderate density). In **structurally coupled** (or cross-gradient) inversion, the algorithm does not enforce a specific velocity-density relationship but instead requires that the spatial gradients of the two property fields are parallel — meaning structural boundaries appear in the same locations in both models. This is more flexible and makes fewer petrophysical assumptions, but it provides weaker coupling.

The practical benefit is a dramatic reduction in model ambiguity. Consider mapping a sedimentary basin: gravity alone might suggest either a deep basin with moderate density contrast or a shallow basin with strong contrast. Seismic refraction data resolve the basin geometry (depth to basement) but may poorly constrain absolute densities. Jointly inverting both datasets yields a model where the basin geometry is fixed by the seismics and the density distribution is consistent with the gravity — a result neither method could produce independently. Joint inversion is now standard practice in crustal-scale studies, resource exploration, and tectonic research, and the framework extends naturally to include additional datasets like magnetotelluric conductivity or magnetic susceptibility, further narrowing the space of permissible models.
