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
stage: formal-systems
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

## Explainer

The key to understanding both fission and fusion is the **binding energy curve**: a plot of binding energy per nucleon versus mass number A. Starting from hydrogen (A=1) and climbing the curve, binding energy per nucleon rises steeply — helium-4 is unusually tightly bound — then continues rising more gently to a peak around iron (A≈56). Beyond iron, the curve slopes gently downward to the heavy elements like uranium (A≈235). This curve encodes a universal rule: any nuclear reaction that moves nuclei toward iron releases energy; any reaction that moves them away from iron costs energy. Fission splits heavy nuclei (moving left toward iron), and fusion combines light nuclei (moving right toward iron). Both are exothermic for the right starting materials precisely because iron sits at the energy minimum.

The **mass defect** is the mechanism by which this energy is released. You know from E = mc² that mass and energy are interconvertible. When you measure the mass of a helium-4 nucleus, it is less than the combined mass of two protons and two neutrons assembled separately. The missing mass — the mass defect Δm — has been converted to the binding energy that holds the nucleus together. In a fission or fusion reaction, the products have higher binding energy per nucleon than the reactants, so the products are lighter than the reactants by Δm. This Δm is released as kinetic energy of the products, gamma rays, and neutrons. Even Δm of order 10⁻²⁸ kg produces ~200 MeV via E = Δmc² — about 50 million times more energy per atom than a typical chemical reaction.

**Fission** requires that a heavy nucleus be hit by a neutron and become unstable enough to split. Uranium-235 absorbs a neutron to form U-236, which splits into two medium-mass fragments and 2–3 fast neutrons. Those neutrons can each trigger further fissions — a **chain reaction**. Whether the chain reaction grows (supercritical), stays steady (critical), or dies out (subcritical) depends on whether, on average, more than one, exactly one, or fewer than one neutron from each fission triggers another fission. A nuclear reactor maintains criticality by using control rods to absorb surplus neutrons; a bomb allows supercritical exponential growth, which is why the distinction between reactor and weapon is fundamental, not incidental.

**Fusion** combines light nuclei — most practically, deuterium (H-2) and tritium (H-3) — but requires them to get close enough for the strong force to dominate over the Coulomb repulsion between like-charged nuclei. Classically, room-temperature nuclei would need to collide head-on with enormous kinetic energy. In the sun's core, thermal energy at ~15 million K and **quantum tunneling** (your soft prerequisite) together make fusion possible: protons tunnel through the Coulomb barrier even at energies below the classical threshold. On Earth, achieving the plasma temperatures (>100 million K) and confinement times needed for sustained fusion is the central challenge of fusion energy research. The DT reaction (D + T → He-4 + n + 17.6 MeV) is the easiest to ignite, and the n carries most of the energy, which must then be captured as heat to drive a turbine — still the same old steam cycle, just with a nuclear heat source.
