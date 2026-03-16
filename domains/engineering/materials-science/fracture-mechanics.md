---
id: fracture-mechanics
title: 'Fracture Mechanics: Brittle and Ductile Failure'
domain: engineering
course: materials-science
prerequisites:
- id: stress-strain-behavior
  type: hard
- id: mechanical-testing-methods
  type: soft
- id: stress-intensity-factor
  type: soft
- id: partial-derivatives
  type: soft
builds-toward:
- fatigue-in-materials
- fracture-toughness-and-design
tags:
- fracture
- stress-concentration
- KIC
- griffith
- brittle
- ductile
stage: formal-systems
status: validated
---

# Fracture Mechanics: Brittle and Ductile Failure

## Core Idea
Fracture is the separation of a material under stress. Brittle fracture occurs with little plastic deformation, often by rapid crack propagation along cleavage planes; ductile fracture is preceded by significant plastic deformation and void coalescence. Griffith's theory explains why cracks propagate: a crack spreads when the energy released by crack extension exceeds the energy required to create new surfaces. The fracture toughness KIc quantifies a material's resistance to crack propagation in plane-strain conditions and is the critical design parameter for components containing flaws.

## How It's Best Learned
Apply the fracture mechanics equation K = Yσ√(πa) to calculate critical crack size for a given applied stress, or critical stress for a given crack size. Compare KIc values for glass, steel, and aluminum to understand the range of fracture toughness in engineering materials.

## Common Misconceptions
- A stronger material is not necessarily tougher; high-strength steels often have lower fracture toughness than lower-strength variants.
- Stress concentrations at notches and holes do not cause higher average stress — they cause local stress amplification that can exceed the fracture stress.

## Explainer

From your stress-strain curve, you know that a material fractures when stress reaches a critical value. But experience — and engineering history — shows that structures fail at stresses far below the material's nominal tensile strength. Bridges collapse, pressure vessels burst, and aircraft fuselages crack at loads their designers considered safe. **Fracture mechanics** exists to explain why, by accounting for the presence of cracks and flaws that the simple stress-strain picture ignores.

**Griffith's energy balance** is the foundational insight. When a crack of half-length a extends by a small amount, the elastic strain energy stored in the surrounding material is released. That released energy either goes into creating new crack surfaces (which cost energy proportional to surface energy γ) or drives further crack growth. Griffith showed that a crack extends spontaneously when the energy release rate G equals the energy required to create the new surfaces. For brittle materials in plane stress, this gives a critical stress σ_c = √(2Eγ/πa) — the longer the crack, the lower the stress needed to propagate it. This explains why a small scratch on glass can cause it to shatter at a stress far below the theoretical crystal strength.

Modern fracture mechanics reformulates Griffith's idea in terms of the **stress intensity factor** K, which characterizes the magnitude of the stress field at the crack tip: K = Yσ√(πa), where Y is a dimensionless geometry factor, σ is the applied stress, and a is the crack half-length. This K tells you how strongly the crack tip is being "loaded." Fracture occurs when K reaches the material's **fracture toughness** K_Ic — a measured material property that represents the critical stress intensity for plane-strain crack propagation. The equation K = Yσ√(πa) is the central tool of damage-tolerant design: given a maximum expected crack size (from inspection), you can calculate the maximum safe operating stress; or given an applied stress, you can calculate the maximum tolerable crack size before the part must be retired.

**Brittle** and **ductile** fracture are distinguished by how much plastic deformation precedes failure. In brittle materials (ceramics, glass, some high-strength steels at low temperature), the crack propagates with almost no plastic zone at the tip — the fracture surface is flat and faceted, reflecting cleavage along crystal planes. In ductile materials, the plastic zone at the crack tip is large — the material yields, voids nucleate around inclusions, and the voids coalesce into a crack that advances by tearing rather than cleavage. The fracture surface looks dimpled and rough. Higher toughness K_Ic generally correlates with larger plastic zones (more energy absorbed before fracture), which is why ductile materials are tougher. Critically, high-strength alloys typically have smaller plastic zones (their yield strength is high, limiting plasticity), which is why increasing strength through cold work or precipitation hardening often *reduces* toughness — the tradeoff between strength and toughness is real and governs most structural material selection decisions.
