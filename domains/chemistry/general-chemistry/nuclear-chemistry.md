---
id: nuclear-chemistry
title: Nuclear Chemistry
domain: chemistry
course: general-chemistry
prerequisites:
- id: atomic-structure-basics
  type: hard
- id: half-life-decay-law
  type: soft
- id: nuclear-structure
  type: soft
- id: radioactive-decay
  type: soft
- id: mass-energy-equivalence
  type: soft
- id: isotopes-and-nuclear-composition
  type: soft
tags:
- radioactivity
- alpha-decay
- beta-decay
- gamma-radiation
- nuclear-stability
- binding-energy
- fission
- fusion
- radiometric-dating
stage: formal-systems
status: validated
---

# Nuclear Chemistry

## Core Idea
Nuclear chemistry involves reactions that change the nucleus itself, unlike ordinary chemical reactions which involve only valence electrons. Radioactive decay occurs when an unstable nucleus emits radiation to reach greater stability: alpha decay (loss of ⁴₂He nucleus), beta decay (neutron converts to proton with electron emission), or gamma emission (release of high-energy photons following other decay). Nuclear binding energy — the energy required to disassemble a nucleus into its constituent nucleons — determines stability and is the basis for fission (splitting heavy nuclei) and fusion (combining light nuclei) as immense energy sources.

## How It's Best Learned
Practice writing and balancing nuclear equations by conserving mass number (superscript) and atomic number (subscript) on both sides. Calculate decay quantities using first-order kinetics and half-life. Compare binding energy per nucleon across the periodic table to understand why iron-56 is the most stable nucleus and why both fission of uranium and fusion of hydrogen release energy.

## Common Misconceptions
- Nuclear reactions are not accelerated chemical reactions — they involve the strong nuclear force and can transmute elements entirely, something chemical reactions cannot do.
- Radioactive half-life is the time for half the atoms in a sample to decay, not the time until the sample is safe or inert — samples technically never reach zero radioactivity, though they approach negligible levels after many half-lives.

## Questions

```yaml
- question: "Radium-226 undergoes alpha decay. Its mass number is 226 and atomic number is 88. What are the mass number and atomic number of the daughter nucleus?"
  type: multiple-choice
  options: ["Mass 226, atomic 86", "Mass 222, atomic 86", "Mass 222, atomic 84", "Mass 224, atomic 87"]
  answer: 1
  explanation: "Alpha decay emits a ⁴₂He nucleus, so the mass number decreases by 4 (226 - 4 = 222) and the atomic number decreases by 2 (88 - 2 = 86). The daughter is radon-222. Balancing nuclear equations requires conserving both mass number (superscripts) and atomic number (subscripts) on both sides."

- question: "After exactly three half-lives, a radioactive sample has decayed to zero — it is largely gone."
  type: true-false
  answer: false
  explanation: "Half-life describes exponential decay: after one half-life, 50% remains; after two, 25%; after three, 12.5%. The amount approaches zero asymptotically but never actually reaches it mathematically. Practically, samples become negligible after many half-lives, but there is no point at which the last atom decays predictably. The misconception arises from treating half-life like a countdown timer rather than a statistical rate."

- question: "Why do both nuclear fission of uranium-235 and nuclear fusion of hydrogen release energy, even though fission splits nuclei apart and fusion joins them together?"
  type: short-answer
  answer: "Both processes move nuclei toward the peak of the binding energy per nucleon curve, near iron-56. Heavy nuclei like uranium have lower binding energy per nucleon than mid-weight nuclei, so splitting them releases energy. Light nuclei like hydrogen have lower binding energy per nucleon than helium, so fusing them also releases energy."
  explanation: "Binding energy per nucleon peaks around iron-56 and decreases in both directions. Any nuclear reaction that moves a nucleus closer to iron-56 releases energy (the mass difference is converted via E=mc²). Uranium-235 is heavier than iron, so fission moves the products toward the peak. Hydrogen is lighter than iron, so fusion of hydrogen to helium also moves toward the peak. Both reactions liberate the binding energy difference as kinetic energy and radiation."
```

## Explainer

When you study chemical reactions, the nucleus stays entirely untouched — electrons are shuffled between atoms, but protons and neutrons never change. Nuclear chemistry is fundamentally different: it involves reactions that transform the nucleus itself, transmuting one element into another and releasing energies that dwarf anything in ordinary chemistry. To understand why, you need to think about what holds the nucleus together in the first place.

Protons are all positively charged and packed into an incredibly small space, so the electromagnetic repulsion between them is enormous. What overcomes this repulsion is the **strong nuclear force** — a short-range force that acts between nucleons (protons and neutrons) and is far stronger than electromagnetism at the scale of the nucleus. The **binding energy** of a nucleus is the energy you would need to supply to completely disassemble it into separate protons and neutrons. Equivalently, it is the energy released when those nucleons come together. A useful benchmark is **binding energy per nucleon** — this peaks around iron-56, which is why iron is the most stable nucleus. Nuclei lighter than iron can release energy by fusing; nuclei heavier than iron can release energy by splitting.

**Radioactive decay** occurs when a nucleus is unstable — typically because the neutron-to-proton ratio is too high or too low, or because the nucleus is simply too large for the strong force to hold together across its full diameter. Three common decay modes: **alpha decay** ejects a helium-4 nucleus (⁴₂He), reducing both mass number and atomic number by losing two protons and two neutrons; **beta decay** (β⁻) converts a neutron into a proton while emitting an electron and an antineutrino, increasing atomic number by one; **gamma emission** releases a high-energy photon after another decay event, allowing the nucleus to shed excess energy without changing its particle composition. To balance nuclear equations, conserve both mass number (total nucleons, superscript) and atomic number (proton count, subscript) on both sides.

Radioactive decay is described by first-order kinetics: the decay rate at any moment is proportional to how many radioactive atoms remain. The **half-life** (t₁/₂) is the time for half of any sample to decay. After one half-life, 50% remains; after two, 25%; after three, 12.5% — and so on, exponentially. The sample asymptotically approaches zero but never reaches it. This matters practically: a substance is not "safe" after one half-life, and the concept of "when will it be gone?" is mathematically meaningless. Instead, we ask how many half-lives are needed for the activity to fall below some threshold relevant to biology or regulation.

**Fission** (splitting heavy nuclei like uranium-235 by neutron bombardment) and **fusion** (joining light nuclei like deuterium and tritium) are both routes toward greater binding energy per nucleon — toward the iron-56 peak. The mass difference between reactants and products is converted into energy by Einstein's E = mc². Because c² is enormous (~9 × 10¹⁶ m²/s²), even tiny mass differences yield vast energies. Fusion reactions, which power the sun, produce far more energy per unit mass than fission, but sustaining the temperatures and pressures needed for fusion on Earth remains an active engineering challenge.
