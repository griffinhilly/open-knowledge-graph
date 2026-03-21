---
id: stress-intensity-factor
title: Stress Intensity Factor
domain: engineering
course: materials-science
prerequisites:
  - id: stress-strain-behavior
    type: hard
builds-toward:
  - fracture-mechanics
  - fatigue-in-materials
tags: [stress-intensity-factor, fracture-mechanics, LEFM, crack-propagation, fracture-toughness]
stage: formal-systems
status: validated
---

# Stress Intensity Factor

## Core Idea
The stress intensity factor K quantifies the magnitude of the stress field near the tip of a crack in a material under load, and is the central parameter in linear elastic fracture mechanics (LEFM). It is defined as K = Yσ√(πa), where σ is the applied stress, a is the crack length, and Y is a dimensionless geometry factor that depends on crack shape and specimen configuration. Three fracture modes describe how loads open or shear a crack: Mode I (opening/tensile — by far the most common and dangerous), Mode II (in-plane shear), and Mode III (out-of-plane shear/tearing). Each mode has its own stress intensity factor (K_I, K_II, K_III). Fracture occurs when K reaches the critical stress intensity factor K_c (also called fracture toughness), a material property measured in units of MPa√m. Materials with high K_c (like steel) resist crack propagation; those with low K_c (like glass) fracture catastrophically.

## How It's Best Learned
Start with the physical intuition: stress concentrates at crack tips, and sharper/longer cracks create more intense stress fields. Show how K captures this with a single number. Work through K = Yσ√(πa) with concrete examples — calculate K for a center crack in a plate and compare to the material's K_c to predict whether it will fracture. Introduce the three modes with diagrams showing the direction of loading relative to the crack plane. Compare K_c values across material classes (ceramics, metals, polymers) to build intuition about brittleness vs. toughness. Connect to real engineering failures where cracks propagated because K exceeded K_c.

## Common Misconceptions
- Confusing stress intensity factor K with stress concentration factor K_t — K_t is a dimensionless ratio from elasticity theory, while K has units of MPa√m and predicts fracture.
- Thinking a material fails when stress exceeds yield strength everywhere — with a crack present, local failure occurs when K reaches K_c even if the average stress is well below yield.
- Assuming longer cracks are always more dangerous at the same load — K depends on both crack length and geometry factor Y, which varies with configuration.
- Believing K_c is a fixed universal constant for a material — it varies with thickness (plane stress vs. plane strain), temperature, and loading rate.

## Questions

```yaml
- question: "A steel component has a crack of length 4 mm and is operating such that K_I = 0.8 K_c. The crack grows to 16 mm while the applied stress and geometry factor Y remain unchanged. What is the approximate new value of K_I?"
  type: multiple-choice
  options:
    - "K_I = 0.8 K_c — applied stress hasn't changed, so K_I doesn't change"
    - "K_I = 3.2 K_c — crack length quadrupled, so K_I quadruples"
    - "K_I = 1.6 K_c — K_I scales as √a, so it doubles when crack length quadruples; fracture occurs"
    - "K_I = 1.13 K_c — K_I scales as the fourth root of crack length"
  answer: 2
  explanation: "K_I = Yσ√(πa), so K_I scales as √a. When crack length goes from 4 mm to 16 mm (a factor of 4), K_I increases by √4 = 2. The new K_I = 2 × 0.8 K_c = 1.6 K_c, which exceeds K_c — the component fractures. This square-root dependence is the key: cracks grow more dangerous faster than linearly. The common wrong answer (tripling or quadrupling) treats K as linearly proportional to crack length, which is incorrect."

- question: "How does the stress intensity factor K differ fundamentally from the stress concentration factor K_t?"
  type: multiple-choice
  options:
    - "K applies only to Mode I loading; K_t applies to all three fracture modes"
    - "K has units of MPa√m and predicts fracture by comparison to K_c; K_t is dimensionless and describes local stress amplification from elasticity theory without predicting fracture"
    - "K_t is the material property; K is the applied quantity — they are two halves of the same fracture criterion"
    - "K measures crack tip displacement; K_t measures the stress ratio between tip and nominal stress"
  answer: 1
  explanation: "These two quantities are frequently confused because both involve 'K' and both relate to stress near a notch or crack. K_t (stress concentration factor) is a dimensionless ratio from linear elasticity — it tells you how much higher the local stress is than the nominal stress, but makes no fracture prediction. K (stress intensity factor) has dimensions of MPa√m and is compared to K_c to predict whether fracture will occur. A material without a crack can have a high K_t at a notch and still not fracture; a cracked material fails when K_I = K_c."

- question: "According to K = Yσ√(πa), doubling the applied stress increases K by the same multiplicative factor as doubling the crack length."
  type: true-false
  answer: false
  explanation: "Doubling the applied stress σ doubles K (linear relationship). Doubling the crack length a increases K by √2 ≈ 1.41 (square-root relationship). These are different factors. A doubling of stress is more dangerous per unit change than a doubling of crack length. This distinction matters for damage tolerance design: you can sometimes reduce stress levels more easily than eliminating cracks, and the calculations must respect the correct scaling."

- question: "A component can fracture even when the average applied stress is well below the material's yield strength, if a crack is present and K_I reaches K_c."
  type: true-false
  answer: true
  explanation: "This is the central insight of fracture mechanics. The stress field near a crack tip is singular — it rises steeply regardless of the average stress — and the material fails when this local intensity (K_I) reaches the material's fracture toughness (K_c). An aircraft component with a small crack can fail at loads that would be safe for an uncracked specimen. This is why damage-tolerance design evaluates components based on their crack state, not just their nominal stress levels."

- question: "Explain why detecting a crack at 1 mm is disproportionately more valuable than detecting a crack at 16 mm, even if both are below the critical size at current stress levels."
  type: short-answer
  answer: "Because K_I scales as √a, the stress intensity at a 16 mm crack is √(16/1) = 4 times that at a 1 mm crack under the same stress and geometry. A crack that is 'safe' at 1 mm may reach K_c after modest growth. More importantly, the rate of danger accumulation is front-loaded: going from 1 mm to 4 mm quadruples crack length but only doubles K; going from 4 mm to 16 mm does the same multiplication. Each size doubling adds less marginal danger, but small cracks that are missed grow into the dangerous range through normal operation. Early detection gives the most intervention time before K_I approaches K_c."
  explanation: "The square-root scaling means that the marginal increase in K per unit of crack growth decreases as the crack gets longer. But the absolute level of K is still much lower at small sizes. Detecting at 1 mm and arresting growth or reducing stress gives a much larger safety margin than detecting at 16 mm when the component may already be near fracture. This is the quantitative basis for inspection interval design in damage-tolerant structures."
```

## Explainer

From stress-strain behavior, you know that a material yields when stress exceeds the yield strength σ_y, and fractures when the applied energy exceeds its toughness. But these concepts assume a smooth, defect-free specimen. Real engineering components always contain imperfections: machining scratches, weld pores, inclusions, or surface nicks. The field of **linear elastic fracture mechanics (LEFM)** exists because a crack-tipped defect creates a local stress field that is far more severe than any average stress analysis can capture.

Here is the key insight: the stress field near a crack tip is singular — mathematically, it approaches infinity as you move toward the tip. In practice, some small plastic zone forms at the tip to relieve the singularity, but for most engineering metals and all ceramics, this zone is small enough to ignore. What LEFM recognizes is that even though the actual stress at the crack tip is not well-defined, the *intensity* of the entire surrounding stress field can be characterized by a single number. That number is the **stress intensity factor** K_I = Yσ√(πa), where σ is the remotely applied stress, a is the crack half-length, and Y is a geometry correction factor near 1 for a through crack in a wide plate.

The √(πa) dependence is the most important feature of this equation. It tells you that cracks become more dangerous faster than linearly with length — doubling crack length increases K by a factor of √2, not 2. This also means that detecting cracks early matters disproportionately: a crack of length 1 mm is four times less dangerous than a crack of length 16 mm at the same stress level. The geometry factor Y accounts for the specific configuration: a crack at an edge (Y ≈ 1.12) is about 12% more dangerous than a centered through-crack (Y ≈ 1.0) at the same nominal size and stress, because the free surface concentrates stress more efficiently. For complex geometries — holes, notches, curved surfaces — Y must be looked up in handbooks or computed by finite element analysis.

**Fracture toughness** K_c is the material's resistance to this singular field. It is a true material property, measurable by a standardized test (ASTM E399), with units of MPa√m. When K_I reaches K_c, the crack propagates catastrophically. To use this in design: calculate K_I from the applied stress and the largest crack you cannot detect or guarantee absence of; compare to K_c; design so K_I < K_c with an appropriate safety margin. This logic governs the entire damage-tolerance philosophy used in aircraft, pressure vessels, and nuclear reactors. A high K_c material (like 4340 steel at ~50 MPa√m) can tolerate substantial cracks before fracture; a low K_c material (like glass at ~0.7 MPa√m) fractures at microscopic flaws. The dramatic difference in toughness between these two materials — both of which have similar theoretical bond strengths — arises from the ability of metals to plastically deform at the crack tip and absorb energy, which is why ductility and toughness are related even though they are not the same thing.
