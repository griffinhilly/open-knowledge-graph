---
id: stress-intensity-factor-and-fracture
title: Stress Intensity Factor and Fracture Mechanics
domain: engineering
course: materials-science
prerequisites:
- id: stress-concentration-and-singularities
  type: hard
- id: brittle-vs-ductile-fracture
  type: soft
- id: fracture-mechanics-analysis
  type: soft
- id: fracture-mechanics-concepts
  type: soft
builds-toward:
- fracture-mechanics
- fatigue-crack-propagation-and-growth
tags:
- stress-intensity-factor
- fracture-toughness
- crack-mechanics
stage: formal-systems
status: validated
---
# Stress Intensity Factor and Fracture Mechanics

## Core Idea
The stress intensity factor K quantifies the magnitude of the singular stress field at a crack tip and determines crack stability. Fracture toughness KIC is the critical stress intensity at which a crack grows instably; when K < KIC, cracks remain stable. The J-integral provides an energy-based alternative applicable to elastic-plastic situations.

## Questions

```yaml
- question: "A crack in a structural component has a half-length of 4 mm and the applied stress intensity factor K equals 0.8 K_IC. The crack then grows so its half-length becomes 16 mm, while the applied stress remains the same. Is the component now safe?"
  type: multiple-choice
  options:
    - "Yes — the crack is still below the critical length, so K < K_IC."
    - "No — quadrupling the crack half-length doubles K (since K ∝ √a), so K is now 1.6 K_IC and the crack propagates unstably."
    - "No — quadrupling the crack half-length quadruples K, so K is now 3.2 K_IC."
    - "Yes — K_IC is a material constant and does not change with crack size, so the same margin remains."
  answer: 1
  explanation: "K = Yσ√(πa), so K scales with √a. When a increases by a factor of 4 (from 4 mm to 16 mm), K increases by √4 = 2. The initial K was 0.8 K_IC, so the new K is 1.6 K_IC — above the critical threshold. This square-root dependence is the non-obvious core result: a crack four times longer is only twice as severe in terms of K, not four times."

- question: "What does the fracture toughness K_IC represent in practice?"
  type: multiple-choice
  options:
    - "The maximum stress a material can sustain before any crack nucleates."
    - "The stress concentration factor at the crack tip for Mode I loading."
    - "A material property giving the critical stress intensity at which a crack propagates unstably under Mode I loading."
    - "The energy required to create a unit area of new crack surface, equivalent to surface energy."
  answer: 2
  explanation: "K_IC is a material constant — like yield strength — measured experimentally using standardized specimens. It is not a stress, not a stress concentration factor, and not a surface energy directly (though it relates to Griffith energy via K_IC² = G_IC·E for plane stress). The design criterion is K < K_IC for safe operation. When K reaches K_IC, the crack grows unstably and fracture occurs."

- question: "A structure can remain safe in service even if it contains cracks, as long as the stress intensity factor K at the largest expected crack remains below K_IC."
  type: true-false
  answer: true
  explanation: "This is the foundation of damage-tolerant design. LEFM provides a critical crack size a_c = (K_IC / Yσ)² / π — the largest crack that can exist without catastrophic failure at the operating stress. Inspection intervals are set to ensure no crack grows beyond a_c between checks. The assumption is not zero defects, but bounded defects with known K."

- question: "Doubling the crack area in a uniformly loaded plate doubles the stress intensity factor K."
  type: true-false
  answer: false
  explanation: "Crack area scales as a² (for a penny-shaped crack) or as a·thickness (for a through-crack in a plate). For a through-crack of half-length a, doubling the crack area means a → √2·a (not 2a). Since K ∝ √a, this gives K → (√2)^(1/2) · K_original = 2^(1/4) · K ≈ 1.19 K_original. Even if we interpret 'doubling area' as doubling a (quadrupling the area), K only doubles — not quadruples. The nonlinear √a relationship is the key insight."

- question: "Why does LEFM use the stress intensity factor K to characterize crack severity rather than computing the actual stress at the crack tip?"
  type: short-answer
  answer: "Classical elasticity theory predicts that stress approaches infinity at the crack tip (a true mathematical singularity for a zero-radius notch). Computing a meaningful stress value there is impossible. K instead characterizes the amplitude of this singular stress field — how fast stresses rise as you approach the tip. The stress field takes the form σ ∝ K/√(2πr); K sets the scale. Two cracks with the same K have identical stress fields in the surrounding region, regardless of how they got there, so K fully determines fracture behavior. This allows a finite, measurable quantity to govern a physically infinite stress."
  explanation: "The singularity is not a flaw in the theory — it is the key feature. LEFM exploits the fact that the singular field is completely characterized by a single parameter K. This makes it possible to tabulate K_IC as a material constant and to use K = Yσ√(πa) as a design tool, without needing to resolve the actual stress distribution at the nanometer-scale crack tip."
```

## Explainer

From your prerequisite on stress concentrations, you know that geometric discontinuities amplify local stress: a circular hole in a plate triples the nominal stress at its edge. A crack is the most severe stress concentrator possible — it has an essentially zero-radius tip, and classical elasticity theory predicts that stress at the crack tip approaches infinity. This singularity is not a physical failure of the theory; it is a signal that something important is happening in that region. Linear elastic fracture mechanics (LEFM) exploits this singularity as a tool: rather than trying to compute a meaningful stress value at the infinitely sharp tip, it characterizes the *strength* of the singularity.

The mathematical result from elasticity theory is that the stress components near a crack tip scale as σ ∝ K / √(2πr), where r is distance from the crack tip. The **stress intensity factor** K sets the amplitude of this singular field — it describes how severe the stress concentration is, not at the tip itself, but in the surrounding region that controls crack behavior. K depends on three things: the applied stress σ, the crack half-length a, and a dimensionless geometry factor Y that accounts for crack location, plate width, and loading configuration: K = Yσ√(πa). Doubling the applied stress doubles K. Quadrupling the crack area doubles K (because K scales with √a). This square-root dependence on crack size is a fundamental, non-obvious result: a crack that is four times longer is only twice as dangerous in terms of K.

**Fracture toughness** K_IC (read "K-one-C") is a material property: the critical value of K at which a crack propagates unstably. The subscript I denotes Mode I loading (crack-opening mode, the most common). K_IC is measured experimentally using standardized specimens and represents the material's inherent resistance to crack growth. It is a genuine material constant in the same sense as yield strength — independent of specimen geometry (within size requirements) and directly tabulated. The design rule is simple: the structure is safe as long as the actual K, calculated from the applied load and crack size, remains below K_IC. Rearranging K = Yσ√(πa) = K_IC gives you the critical crack size a_c = (K_IC / Yσ)² / π — the largest crack that can exist without catastrophic failure at stress σ. This is the foundation of damage-tolerant design: you do not assume a flawless structure; you assume cracks exist and size the design to tolerate the largest crack that inspection could miss.

The **J-integral** extends fracture mechanics to situations where significant plastic deformation occurs at the crack tip, invalidating the purely elastic LEFM analysis. J is an energy quantity — a path-independent line integral around the crack tip that equals the rate of change of potential energy with crack area. In the linear elastic limit, J = K²/E, so K and J are equivalent for brittle materials. For ductile metals with large plastic zones, J-based criteria (using J_IC as the material toughness) provide a valid fracture assessment where LEFM would be non-conservative. J_IC values are higher than K_IC-based predictions would suggest, reflecting the extra energy absorbed by plastic deformation — which is precisely why ductile materials are tougher than brittle ones.
