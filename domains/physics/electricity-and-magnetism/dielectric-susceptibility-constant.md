---
id: dielectric-susceptibility-constant
title: Dielectric Susceptibility and Permittivity
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: dielectric-materials-polarization
  type: hard
builds-toward:
- energy-density-electric-field
tags:
- susceptibility
- permittivity
- relative
stage: formal-systems
status: validated
---

# Dielectric Susceptibility and Permittivity

## Core Idea
Polarization is P = ε₀χₑE, where χₑ is electric susceptibility. The relative permittivity εᵣ = 1 + χₑ gives total field E = E₀/εᵣ inside dielectric. Capacitance with dielectric: C = εᵣε₀A/d.

## How It's Best Learned
Compare capacitance with and without dielectric. Measure field reduction and relate to susceptibility values in reference tables.

## Questions

```yaml
- question: "A parallel-plate capacitor is fully charged to voltage V₀ (storing charge Q₀), then disconnected from the battery. A dielectric with εᵣ = 4 is inserted between the plates. What happens?"
  type: multiple-choice
  options:
    - "Voltage stays at V₀, charge increases to 4Q₀ — the dielectric draws in more charge from the surroundings."
    - "Voltage drops to V₀/4, charge stays at Q₀ — the dielectric reduces the electric field, lowering the voltage."
    - "Both voltage and charge stay the same — the dielectric has no effect on an isolated capacitor."
    - "Voltage increases to 4V₀, charge increases to 4Q₀ — more dielectric means more energy stored."
  answer: 1
  explanation: "When disconnected from the battery, charge Q is fixed (nowhere for it to go). Inserting the dielectric reduces the internal electric field by εᵣ = 4. Since V = Ed, voltage drops to V₀/4. Capacitance C = Q/V therefore increases to 4C₀. Option A describes what happens when the battery stays connected: then the battery supplies extra charge to maintain V₀, and Q increases. The key distinction is whether voltage or charge is held constant — battery connected holds V fixed, battery disconnected holds Q fixed."

- question: "Water has a dielectric constant εᵣ ≈ 80. What does this mean for the electric field inside liquid water compared to the same field configuration in vacuum?"
  type: multiple-choice
  options:
    - "The field inside water is 80 times stronger — water's polar molecules amplify the applied field."
    - "The field inside water is reduced to about 1/80 of the vacuum value — polarized water dipoles create a large opposing field."
    - "Water blocks electric fields entirely, so the internal field is zero."
    - "The field is unchanged; εᵣ only affects capacitance, not field strength inside the material."
  answer: 1
  explanation: "The dielectric constant εᵣ = 1 + χₑ quantifies how much the material's polarization reduces the internal field. Water's enormous susceptibility (χₑ ≈ 79) means its dipoles align strongly with the applied field, producing a bound-charge field that nearly cancels the applied field. The net internal field is E₀/εᵣ ≈ E₀/80. This field reduction is why water dissolves ionic compounds so effectively: the electrostatic attraction between Na⁺ and Cl⁻ is weakened 80-fold in water, allowing thermal energy to keep them separated."

- question: "Inserting a dielectric into a capacitor increases its capacitance because the polarized dielectric creates an opposing electric field, allowing more charge to be stored at the same voltage."
  type: true-false
  answer: true
  explanation: "When a dielectric fills a capacitor, its dipoles align with the applied field and create bound surface charges that oppose the free charges on the plates, reducing the net internal field. For a capacitor connected to a battery (fixed voltage), the battery supplies additional charge to restore E = V/d, so Q increases. Since C = Q/V and Q has grown at the same V, capacitance rises: C = εᵣC₀. The mechanism is the opposing bound-charge field — the dielectric screens the plate charges, making room for more charge at the same voltage."

- question: "The electric field inside a dielectric material is stronger than in vacuum because the aligned dipoles add their own field to the external applied field."
  type: true-false
  answer: false
  explanation: "The opposite is true. When dipoles align with the applied field, their negative ends face the positive plate and positive ends face the negative plate — producing bound surface charges that oppose the applied field and reduce the net internal field to E₀/εᵣ ≤ E₀. The dipoles screen the field, they do not amplify it. (Ferroelectric materials can have spontaneous polarization, but even there the standard dielectric analysis shows field reduction due to bound charges, not enhancement.)"

- question: "Explain why a material with high electric susceptibility (like water, χₑ ≈ 79) produces an internal electric field only about 1/80th as strong as the same field would be in vacuum."
  type: short-answer
  answer: "A high-susceptibility material polarizes strongly: its molecular dipoles align efficiently with the applied field, producing large bound surface charges on the dielectric faces. These bound charges generate their own electric field directed opposite to the applied field. The net internal field is the applied field minus the opposing bound-charge field. For water (εᵣ ≈ 80), the opposition is nearly complete: E_internal = E₀/εᵣ ≈ E₀/80. The susceptibility χₑ quantifies the strength of this polarization response, and εᵣ = 1 + χₑ directly gives the field reduction factor."
  explanation: "This is why the relative permittivity appears in the denominator: vacuum has χₑ = 0 and εᵣ = 1 (no polarization, no reduction). As susceptibility grows, bound surface charges grow proportionally, and the internal field shrinks by 1/εᵣ. Water's extreme case (εᵣ ≈ 80) makes it one of the strongest dielectrics at room temperature, which is chemically fundamental: the 80-fold field reduction means electrostatic forces between dissolved ions are 80 times weaker than in vacuum, making ionic dissolution thermodynamically favorable."
```

## Explainer

When you studied dielectric polarization, you learned that an electric field applied to an insulating material causes microscopic dipoles — either permanent molecular dipoles that align, or induced charge displacements — to line up with the field. The result is a net bound surface charge on the dielectric that partially cancels the free charges on the capacitor plates. **Electric susceptibility** χₑ (chi-sub-e) is the number that quantifies how strongly a material polarizes: the polarization field P is related to the applied field E by P = ε₀χₑE. A large χₑ means the material polarizes easily and creates a large opposing field; a small χₑ means the material barely responds.

The connection to the total field inside the material is direct. The bound surface charge creates a field that opposes the applied field, reducing the net field inside the dielectric. Accounting for both the free charge field and the opposing bound charge field gives a total field E = E₀/(1 + χₑ). The combination (1 + χₑ) appears so frequently that we give it a name: the **relative permittivity** εᵣ = 1 + χₑ, sometimes called the **dielectric constant**. Vacuum has χₑ = 0 and εᵣ = 1. Water has χₑ ≈ 79 and εᵣ ≈ 80, meaning water's dipoles polarize so strongly that the field inside water is reduced to about 1/80 of its free-space value — which is why water is such an effective solvent for ionic compounds.

The practical payoff for capacitors is immediate. A parallel-plate capacitor with no dielectric has C₀ = ε₀A/d. Insert a dielectric filling the gap and the field inside drops by a factor of εᵣ, which means the voltage V = Ed drops by the same factor for the same stored charge Q. Since C = Q/V, the capacitance increases to C = εᵣε₀A/d = εᵣC₀. The dielectric effectively allows more charge to be stored at the same voltage — it multiplies the capacitance by the dielectric constant. This is precisely why real capacitors are packed with ceramic, polymer, or electrolytic dielectric materials: a few grams of high-εᵣ material can replace what would otherwise require a much larger physical structure, and the field energy stored in the electric field U = ½CV² scales up accordingly.
