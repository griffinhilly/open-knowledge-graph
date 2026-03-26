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

## Questions

```yaml
- question: "An engineer selects steel for a pressure vessel that may contain small manufacturing flaws and will operate at low temperatures. Steel A has yield strength 800 MPa and KIc = 150 MPa√m. Steel B has yield strength 1400 MPa and KIc = 50 MPa√m. Which should she choose?"
  type: multiple-choice
  options:
    - "Steel B, because higher yield strength means the vessel can withstand higher operating pressures"
    - "Steel A, because higher fracture toughness means it can tolerate larger cracks before fracturing — critical when flaws are present"
    - "Steel B, because higher strength always means better resistance to all failure modes"
    - "Steel A, because lower strength means the material will deform plastically instead of fracturing"
  answer: 1
  explanation: "When cracks are present, fracture toughness KIc — not yield strength — governs failure. From K = Yσ√(πa), the critical crack size at a given stress scales as (KIc/σ)². Steel A's KIc is three times higher, meaning it tolerates dramatically larger cracks before fracture. Steel B's high yield strength is irrelevant if a crack reaches critical length first. Low temperatures exacerbate this: many high-strength steels undergo a ductile-to-brittle transition at low temperature, further reducing toughness. This is precisely the strength-toughness tradeoff at the heart of structural materials selection."

- question: "A glass panel is rated to withstand 50 MPa. A surface scratch doubles the effective crack length (a → 2a). According to Griffith's theory (σ_c = √(2Eγ/πa)), what happens to the critical fracture stress?"
  type: multiple-choice
  options:
    - "It doubles — longer cracks require more force to propagate"
    - "It remains the same — crack length does not affect fracture stress in brittle materials"
    - "It decreases by a factor of √2 — longer cracks require lower stress to propagate"
    - "It increases — longer cracks have more surface area to absorb energy"
  answer: 2
  explanation: "From σ_c = √(2Eγ/πa), critical stress is proportional to 1/√a. Doubling a gives σ_c(new) = √(2Eγ/π·2a) = σ_c / √2 ≈ 0.71 × σ_c. The critical stress *decreases* — longer cracks are more dangerous, not less. This explains why tiny scratches on glass can cause catastrophic failure at stresses far below the theoretical crystal strength: a crack tip concentrates stress locally, and longer cracks lower the globally applied stress needed to reach that critical local concentration."

- question: "A stronger material (higher yield strength) is typically more resistant to fracture than a weaker material."
  type: true-false
  answer: false
  explanation: "Strength and fracture toughness are distinct properties that often trade off against each other. High-strength alloys achieved through cold work, precipitation hardening, or other microstructural refinement have high yield strength but restricted plastic zone sizes at crack tips — less energy is absorbed before fracture, giving lower KIc. Many high-strength steels fail catastrophically at lower applied stresses than lower-strength variants when cracks are present. The strength-toughness tradeoff is one of the central constraints of structural materials selection."

- question: "According to Griffith's theory, the critical stress required to propagate a crack decreases as crack length increases — meaning longer pre-existing cracks make a material more vulnerable to fracture at lower applied stresses."
  type: true-false
  answer: true
  explanation: "From σ_c = √(2Eγ/πa), critical stress is inversely proportional to √a. A longer crack lowers the stress needed to release enough elastic strain energy to create new crack surfaces. This is the foundation of damage-tolerant design: given an operating stress level, the maximum allowable crack size before the part must be retired can be calculated from K = Yσ√(πa) = KIc. It also explains why crack inspection and early detection matter — cracks found early can be repaired before they grow to critical length."

- question: "Explain Griffith's energy balance: why does a crack propagate spontaneously once it reaches a critical length, rather than requiring continuously increasing applied stress?"
  type: short-answer
  answer: "Griffith's insight is that crack propagation is governed by energy balance. When a crack of half-length a extends slightly, elastic strain energy stored in the surrounding stressed material is released. This released energy must either create new crack surfaces (costing energy proportional to surface energy γ) or drive further crack growth. For small cracks, each small extension releases less energy than it costs to create new surfaces, so the crack is stable. But as crack length grows, the energy released by extension scales with crack area (∝ a²) while the surface creation cost scales linearly — so there is a critical length above which each small extension releases more energy than it costs. Beyond this length, crack growth becomes self-sustaining: energy surplus from each extension drives further extension without requiring additional applied stress, and the crack runs catastrophically."
  explanation: "This energy perspective explains something that the simple stress-strain picture cannot: why small flaws are far more dangerous than their size suggests, and why fracture is often sudden and complete rather than gradual. The crack doesn't need the applied stress to increase; it only needs to reach the length at which the energy balance tips. The equation σ_c = √(2Eγ/πa) is the direct result of setting the energy release rate equal to the surface energy cost."
```

## Explainer

From your stress-strain curve, you know that a material fractures when stress reaches a critical value. But experience — and engineering history — shows that structures fail at stresses far below the material's nominal tensile strength. Bridges collapse, pressure vessels burst, and aircraft fuselages crack at loads their designers considered safe. **Fracture mechanics** exists to explain why, by accounting for the presence of cracks and flaws that the simple stress-strain picture ignores.

**Griffith's energy balance** is the foundational insight. When a crack of half-length a extends by a small amount, the elastic strain energy stored in the surrounding material is released. That released energy either goes into creating new crack surfaces (which cost energy proportional to surface energy γ) or drives further crack growth. Griffith showed that a crack extends spontaneously when the energy release rate G equals the energy required to create the new surfaces. For brittle materials in plane stress, this gives a critical stress σ_c = √(2Eγ/πa) — the longer the crack, the lower the stress needed to propagate it. This explains why a small scratch on glass can cause it to shatter at a stress far below the theoretical crystal strength.

Modern fracture mechanics reformulates Griffith's idea in terms of the **stress intensity factor** K, which characterizes the magnitude of the stress field at the crack tip: K = Yσ√(πa), where Y is a dimensionless geometry factor, σ is the applied stress, and a is the crack half-length. This K tells you how strongly the crack tip is being "loaded." Fracture occurs when K reaches the material's **fracture toughness** K_Ic — a measured material property that represents the critical stress intensity for plane-strain crack propagation. The equation K = Yσ√(πa) is the central tool of damage-tolerant design: given a maximum expected crack size (from inspection), you can calculate the maximum safe operating stress; or given an applied stress, you can calculate the maximum tolerable crack size before the part must be retired.

**Brittle** and **ductile** fracture are distinguished by how much plastic deformation precedes failure. In brittle materials (ceramics, glass, some high-strength steels at low temperature), the crack propagates with almost no plastic zone at the tip — the fracture surface is flat and faceted, reflecting cleavage along crystal planes. In ductile materials, the plastic zone at the crack tip is large — the material yields, voids nucleate around inclusions, and the voids coalesce into a crack that advances by tearing rather than cleavage. The fracture surface looks dimpled and rough. Higher toughness K_Ic generally correlates with larger plastic zones (more energy absorbed before fracture), which is why ductile materials are tougher. Critically, high-strength alloys typically have smaller plastic zones (their yield strength is high, limiting plasticity), which is why increasing strength through cold work or precipitation hardening often *reduces* toughness — the tradeoff between strength and toughness is real and governs most structural material selection decisions.
