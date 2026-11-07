---
id: latimer-and-frost-diagrams
title: Latimer and Frost Diagrams
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: electrochemical-cells
  type: hard
- id: free-energy-change-spontaneity-work
  type: hard
- id: oxidation-numbers
  type: soft
- id: half-reactions-and-balancing
  type: soft
- id: electrochemistry-nernst-equation
  type: soft
builds-toward:
- corrosion-chemistry-and-protection
tags:
- redox
- Latimer diagram
- Frost diagram
- disproportionation
- comproportionation
- standard potentials
stage: advanced
status: validated
---

# Latimer and Frost Diagrams

## Core Idea
Latimer and Frost diagrams summarize the standard reduction potentials of every oxidation state of one element. A Latimer diagram lists the species in order of oxidation state with the potential of each step written over the arrow. A Frost diagram plots each state's volt-equivalent (N × E°, relative to the element) against oxidation number N, so the lowest point is the most stable state and points above the line joining their neighbors tend to disproportionate. Both diagrams let you judge redox stability at a glance without writing out each half-reaction.

## How It's Best Learned
Start with a short Latimer diagram such as copper in acid and practise two skills: combining non-adjacent potentials through ΔG° = −nFE°, and spotting disproportionation. Then convert the same data into a Frost diagram by hand, plotting N × E° against N. Read slopes as potentials and compare the shape with the Latimer numbers until the two views feel like the same information.

## Common Misconceptions
- Potentials for a multi-step change can be added like enthalpies. (Free energies add, but potentials do not; the combined E° is the electron-weighted average (n₁E₁ + n₂E₂)/(n₁ + n₂).)
- A species with a high oxidation state is always unstable. (Stability depends on its position relative to neighbors on the Frost diagram, and on pH; MnO₄⁻ is kinetically persistent in water even though it is a strong oxidant.)
- A Frost diagram drawn for acid solution also holds in base. (Potentials of couples involving H⁺ or OH⁻ change with pH, so separate diagrams are drawn for pH 0 and pH 14.)

## Questions

```yaml
- question: "In acid solution the Latimer diagram for copper is Cu²⁺ → Cu⁺ (+0.15 V) → Cu (+0.52 V). What happens to Cu⁺ in water under standard conditions?"
  type: multiple-choice
  options: ["It is stable because both potentials are positive", "It disproportionates into Cu²⁺ and Cu", "It is oxidized by water to Cu²⁺ only", "It comproportionates with Cu²⁺"]
  answer: 1
  explanation: "A species disproportionates when the potential on its right is more positive than the potential on its left. Here 0.52 V > 0.15 V, so 2Cu⁺ → Cu²⁺ + Cu has E° = 0.52 − 0.15 = +0.37 V and is spontaneous."
- question: "The standard potential for Fe³⁺ → Fe can be found by adding the potentials for Fe³⁺ → Fe²⁺ and Fe²⁺ → Fe."
  type: true-false
  answer: false
  explanation: "Potentials are intensive and do not add. You add the free energies (−nFE°) and divide by the total number of electrons. Adding the potentials directly gives the wrong answer."
- question: "Given Fe³⁺/Fe²⁺ = +0.77 V and Fe²⁺/Fe = −0.44 V, calculate E° for Fe³⁺ + 3e⁻ → Fe."
  type: short-answer
  answer: "About −0.04 V"
  explanation: "E° = (1 × 0.77 + 2 × (−0.44)) / 3 = (0.77 − 0.88) / 3 ≈ −0.04 V. The electron counts weight each step because ΔG° = −nFE° is the additive quantity."
- question: "On a Frost diagram, a species whose point lies above the straight line joining its two neighboring oxidation states is expected to:"
  type: multiple-choice
  options: ["Be the most stable state of the element", "Disproportionate into those neighbors", "Form by comproportionation of those neighbors", "Be unaffected by pH"]
  answer: 1
  explanation: "If a point lies above the line, the average free energy of the two neighbors is lower than that of the species itself, so splitting into the neighbors is favored. A point below the line means the neighbors would comproportionate to form it."
```

## Explainer

Many elements, especially transition metals and the heavier p-block elements, have several oxidation states. Tables of standard potentials list them couple by couple, which makes it hard to see the whole picture. Latimer and Frost diagrams organize the same data by element.

A Latimer diagram writes the species from highest oxidation state on the left to lowest on the right, with the standard reduction potential of each step above the arrow. For copper in acid it reads Cu²⁺ (+0.15 V) Cu⁺ (+0.52 V) Cu. Two rules make this useful. First, to find the potential for a non-adjacent couple, convert each step to free energy with ΔG° = −nFE°, add the free energies, and divide by −F times the total electrons. For Fe³⁺ to Fe, (1 × 0.77 + 2 × (−0.44))/3 gives about −0.04 V. Second, a species is unstable to disproportionation when the potential to its right is more positive than the potential to its left. Cu⁺ fits this rule, which is why simple Cu⁺ salts are unstable in water and give Cu²⁺ and copper metal.

A Frost diagram turns the list into a picture. For each species, multiply its oxidation number N by the standard potential for reducing it all the way to the element. This product, N × E°, is the volt-equivalent, and it equals ΔG°/F for forming that species from the element. Plot it against N with the element at the origin. Because the vertical axis tracks free energy, the lowest point is the most thermodynamically stable state. The slope of a line between any two points equals the standard potential of that couple. A steep line from a low state up to a high state means the higher state is a strong oxidizing agent.

The geometry also shows stability toward splitting. If a point sits above the line joining its neighbors, it can lower the total free energy by disproportionating. If it sits below, the neighbors will comproportionate to form it. In the manganese diagram for acid solution, Mn²⁺ is the lowest point, and MnO₄²⁻ lies above the line between MnO₄⁻ and MnO₂, so manganate(VI) disproportionates in acid.

Two cautions apply. These diagrams describe thermodynamics only; a favored reaction may still be slow. They are also specific to pH, because many couples involve H⁺ or OH⁻. Pourbaix diagrams extend the same idea by plotting stability across both potential and pH.
