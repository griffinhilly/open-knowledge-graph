---
id: nuclear-fission-fusion
title: Nuclear Fission and Fusion
domain: physics
course: modern-physics
prerequisites:
- id: nuclear-structure
  type: hard
- id: mass-energy-equivalence
  type: hard
- id: quantum-tunneling
  type: soft
- id: half-life-decay-law
  type: soft
- id: radioactive-decay
  type: soft
tags:
- nuclear
- fission
- fusion
- chain-reaction
- energy
- sun
stage: advanced
status: validated
---
# Nuclear Fission and Fusion

## Core Idea
Fission is the splitting of a heavy nucleus (e.g., U-235) into lighter fragments, releasing energy because the products have higher binding energy per nucleon than the reactant. A single neutron-induced fission event releases ~200 MeV and 2–3 neutrons, enabling a chain reaction. Fusion is the combining of light nuclei (e.g., H-2 + H-3 → He-4 + n) to produce heavier products with even higher binding energy per nucleon; it powers stars and releases far more energy per kilogram than fission. Both processes are explained by the mass defect and E = Δmc².

## How It's Best Learned
Calculate the energy released in a D-T fusion reaction and a U-235 fission event from tabulated atomic masses. Compare to chemical energy release per kilogram. Discuss the conditions required — fission needs a critical mass and neutron moderation; fusion needs extreme temperature and pressure to overcome Coulomb repulsion.

## Common Misconceptions
- Fission and fusion both release energy for any nucleus — only fission of nuclei heavier than iron and fusion of nuclei lighter than iron release net energy; the reverse costs energy.
- Nuclear reactors and bombs work the same way — reactors control the chain reaction to maintain a steady rate; bombs allow supercritical exponential growth.

## Questions

```yaml
- question: "A student argues: 'Since fission (splitting) and fusion (combining) are physical opposites, they must have opposite energy behavior — one releases energy because the other absorbs it.' Why is this reasoning wrong?"
  type: multiple-choice
  options:
    - "The student is correct — fusion releases energy precisely because fission absorbs it for heavy nuclei"
    - "Both release energy because the binding energy curve has a peak at iron — fission moves heavy nuclei toward that peak (splitting them), and fusion moves light nuclei toward that peak (combining them)"
    - "Fission always releases energy for any nucleus, but fusion only releases energy for the very lightest nuclei like hydrogen"
    - "Both processes release energy because quantum tunneling effects always produce a net energy surplus regardless of mass number"
  answer: 1
  explanation: "The binding energy curve is the key. It peaks at iron (A ≈ 56). Nuclei on either side of iron can release energy by moving toward that peak: heavy nuclei (like uranium) release energy when split (fission moves them left toward iron), and light nuclei (like hydrogen isotopes) release energy when combined (fusion moves them right toward iron). The student's 'opposites' intuition misses this shared mechanism. Both are exothermic for the same underlying reason — both move toward the energy minimum at iron."

- question: "Why can iron not serve as fuel in either a fission reactor or a fusion reactor?"
  type: multiple-choice
  options:
    - "Iron has no free neutrons available to initiate a chain reaction"
    - "Iron is too abundant in nature to be economically refined as a nuclear fuel"
    - "Iron sits at the peak of the binding energy per nucleon curve, so any nuclear reaction involving iron — splitting it or fusing it — moves away from the peak and requires an energy input rather than releasing energy"
    - "Iron requires plasma temperatures above what is achievable in any known reactor design"
  answer: 2
  explanation: "The binding energy per nucleon curve peaks at iron-56. Energy is released only when a reaction moves nuclei toward this peak. For nuclei lighter than iron, fusion moves them toward the peak (energy release). For nuclei heavier than iron, fission moves them toward the peak (energy release). But iron is already at the peak — any reaction involving iron moves away from it, which requires energy input. This is why the sun will eventually 'die' when its core is iron: no further energy can be extracted from nuclear reactions at that point."

- question: "The energy released in nuclear fission comes from the mass defect — the products are slightly lighter than the reactants because some mass is converted to energy as the products achieve higher binding energy per nucleon."
  type: true-false
  answer: true
  explanation: "This correctly describes the mechanism via E = mc². When U-235 fissions into two medium-mass fragments, the products have higher binding energy per nucleon than the reactant. Higher binding energy means the nucleus is more tightly bound — and this tighter binding corresponds to a smaller total mass (the mass defect). The 'missing' mass Δm has been converted to kinetic energy of the fragments, gamma rays, and neutrons via E = Δmc². Even tiny Δm values produce enormous energy: about 200 MeV per fission event, roughly 50 million times the energy of a typical chemical bond."

- question: "Nuclear fusion releases less energy per reaction event than nuclear fission because fusion uses lighter, less massive nuclei as fuel."
  type: true-false
  answer: false
  explanation: "This confuses total mass with energy release efficiency. What matters is the mass defect per nucleon, not the total mass. The D-T fusion reaction (deuterium + tritium → helium-4 + neutron) releases about 17.6 MeV from just 5 nucleons — approximately 3.5 MeV per nucleon. Uranium-235 fission releases about 200 MeV from 236 nucleons — approximately 0.85 MeV per nucleon. So fusion releases more energy per unit mass (per kilogram of fuel), not less. This is why fusion is the energy source of stars and why fusion fuel would be far more energy-dense than fission fuel."

- question: "Why does the binding energy per nucleon curve explain why both fission AND fusion release net energy, despite the fact that one splits nuclei and the other combines them?"
  type: short-answer
  answer: "Because the binding energy curve peaks at iron — nuclei near iron are the most tightly bound and the most stable. Any nuclear reaction that moves nuclei toward this peak releases the energy difference as kinetic energy and radiation. Heavy nuclei like uranium sit to the right of the peak, so splitting them (fission) produces fragments closer to the peak. Light nuclei like hydrogen sit to the left of the peak, so combining them (fusion) produces a product closer to the peak. Both reactions are exothermic for the same reason: the products are more tightly bound than the reactants."
  explanation: "The binding energy curve is the master key to nuclear energy. Without it, fission and fusion seem paradoxical opposites. With it, both become special cases of the same rule: reactions that increase average binding energy per nucleon release energy. Iron is the turning point — below iron, fusion is exothermic and fission is endothermic; above iron, the reverse. This also explains why 'cold fusion' of iron would be nonsensical and why stellar nucleosynthesis stalls at iron."
```

## Explainer

The key to understanding both fission and fusion is the **binding energy curve**: a plot of binding energy per nucleon versus mass number A. Starting from hydrogen (A=1) and climbing the curve, binding energy per nucleon rises steeply — helium-4 is unusually tightly bound — then continues rising more gently to a peak around iron (A≈56). Beyond iron, the curve slopes gently downward to the heavy elements like uranium (A≈235). This curve encodes a universal rule: any nuclear reaction that moves nuclei toward iron releases energy; any reaction that moves them away from iron costs energy. Fission splits heavy nuclei (moving left toward iron), and fusion combines light nuclei (moving right toward iron). Both are exothermic for the right starting materials precisely because iron sits at the energy minimum.

The **mass defect** is the mechanism by which this energy is released. You know from E = mc² that mass and energy are interconvertible. When you measure the mass of a helium-4 nucleus, it is less than the combined mass of two protons and two neutrons assembled separately. The missing mass — the mass defect Δm — has been converted to the binding energy that holds the nucleus together. In a fission or fusion reaction, the products have higher binding energy per nucleon than the reactants, so the products are lighter than the reactants by Δm. This Δm is released as kinetic energy of the products, gamma rays, and neutrons. Even Δm of order 10⁻²⁸ kg produces ~200 MeV via E = Δmc² — about 50 million times more energy per atom than a typical chemical reaction.

**Fission** requires that a heavy nucleus be hit by a neutron and become unstable enough to split. Uranium-235 absorbs a neutron to form U-236, which splits into two medium-mass fragments and 2–3 fast neutrons. Those neutrons can each trigger further fissions — a **chain reaction**. Whether the chain reaction grows (supercritical), stays steady (critical), or dies out (subcritical) depends on whether, on average, more than one, exactly one, or fewer than one neutron from each fission triggers another fission. A nuclear reactor maintains criticality by using control rods to absorb surplus neutrons; a bomb allows supercritical exponential growth, which is why the distinction between reactor and weapon is fundamental, not incidental.

**Fusion** combines light nuclei — most practically, deuterium (H-2) and tritium (H-3) — but requires them to get close enough for the strong force to dominate over the Coulomb repulsion between like-charged nuclei. Classically, room-temperature nuclei would need to collide head-on with enormous kinetic energy. In the sun's core, thermal energy at ~15 million K and **quantum tunneling** (your soft prerequisite) together make fusion possible: protons tunnel through the Coulomb barrier even at energies below the classical threshold. On Earth, achieving the plasma temperatures (>100 million K) and confinement times needed for sustained fusion is the central challenge of fusion energy research. The DT reaction (D + T → He-4 + n + 17.6 MeV) is the easiest to ignite, and the n carries most of the energy, which must then be captured as heat to drive a turbine — still the same old steam cycle, just with a nuclear heat source.
