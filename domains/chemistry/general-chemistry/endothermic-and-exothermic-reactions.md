---
id: endothermic-and-exothermic-reactions
title: Endothermic and Exothermic Reactions
domain: chemistry
course: general-chemistry
prerequisites:
- id: thermochemistry-enthalpy
  type: hard
- id: heat-capacity-calorimetry
  type: hard
- id: burning-and-combustion-basics
  type: soft
- id: endothermic-exothermic-intro
  type: soft
builds-toward:
- bond-energy-and-enthaly
tags:
- exothermic
- endothermic
- enthalpy change
stage: formal-systems
status: validated
---

# Endothermic and Exothermic Reactions

## Core Idea
Exothermic reactions release heat (ΔH < 0); endothermic reactions absorb heat (ΔH > 0). The sign and magnitude of ΔH determine heat flow between system and surroundings.

## Questions

```yaml
- question: "A reaction has ΔH = –890 kJ/mol. A student says 'This must be endothermic because the surroundings gained 890 kJ of heat.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — a positive heat gain by surroundings means the reaction is endothermic"
    - "ΔH is defined from the system's perspective; ΔH = –890 kJ/mol means the system lost 890 kJ, making this exothermic"
    - "ΔH cannot be negative if heat is being released"
    - "The student is correct; exothermic reactions always have ΔH > 0"
  answer: 1
  explanation: "ΔH is defined from the system's perspective. A negative ΔH means the system's enthalpy decreased — it lost energy to the surroundings. The surroundings gaining heat is exactly what defines an exothermic reaction. The student reversed the logic: because the surroundings gained heat, the system's ΔH is negative, not positive. Combustion of methane (ΔH ≈ –890 kJ/mol) is the classic exothermic example."

- question: "You place an ammonium nitrate cold pack on an injury. The pack gets cold. What can you correctly conclude about the dissolution reaction occurring inside?"
  type: multiple-choice
  options:
    - "ΔH < 0; the reaction is exothermic because energy is being released to cool the pack"
    - "ΔH > 0; the reaction is endothermic because the system is absorbing heat from the surroundings"
    - "ΔH = 0; the temperature change is due to physical mixing, not a chemical process"
    - "ΔH < 0; the cold pack absorbs heat into the surroundings"
  answer: 1
  explanation: "When the pack feels cold, the reaction inside is pulling heat from your hand (the surroundings) into the system. The system's enthalpy is increasing — ΔH > 0, an endothermic process. Dissolving ammonium nitrate requires more energy to break its crystal lattice than is released by hydrating the ions, so the net process absorbs thermal energy from the environment."

- question: "For an exothermic reaction, the energy stored in the chemical bonds of the products is greater than in the reactants."
  type: true-false
  answer: false
  explanation: "The opposite is true. In an exothermic reaction, the products sit at lower enthalpy than the reactants. The bonds in the products are collectively stronger (more stable, lower energy) than in the reactants, so forming them releases energy. The 'extra' energy flows to the surroundings as heat. An energy diagram shows products below reactants for exothermic reactions — the vertical gap equals |ΔH|."

- question: "An endothermic reaction typically feels cold to the touch."
  type: true-false
  answer: false
  explanation: "Not necessarily. Whether a reaction feels cold depends on the rate of heat exchange relative to ambient conditions. Photosynthesis is endothermic but occurs at ambient temperatures without any noticeable cooling sensation. A ΔH > 0 means the system absorbs heat from the surroundings, but this absorption may be too slow, too small, or too well-insulated to produce a perceptible cold sensation."

- question: "Why is ΔH negative for exothermic reactions even though heat is flowing into the surroundings?"
  type: short-answer
  answer: "ΔH is defined from the system's perspective. A negative ΔH means the system lost enthalpy — its products are at a lower energy state than its reactants. The energy that left the system entered the surroundings as heat. Because energy departed the system, the system's change in energy is recorded as negative."
  explanation: "The sign convention is a persistent stumbling block. Many students expect that a 'hot' or 'energetic' reaction should have a positive ΔH, but the convention tracks the system's energy balance. Just as a bank withdrawal is negative on your account statement even though someone else is receiving that money, a reaction that releases heat records that energy loss as a negative ΔH."
```

## Explainer

From your study of thermochemistry and enthalpy, you know that enthalpy (H) is a state function measuring the heat content of a system at constant pressure, and from calorimetry you know how to measure the heat exchanged during a reaction. The classification of reactions as **exothermic** or **endothermic** applies these ideas to a simple but powerful question: does energy flow out of the reacting system into the surroundings, or into the system from the surroundings?

In an **exothermic reaction**, the products have lower enthalpy than the reactants — the system has released energy, typically as heat. The enthalpy change ΔH is negative because the final state is lower in energy than the initial state. You can feel this directly: the reaction vessel gets warm. Combustion is the classic example — burning methane (CH₄ + 2O₂ → CO₂ + 2H₂O) releases 890 kJ per mole because the bonds in CO₂ and H₂O are collectively stronger (lower energy) than the bonds in CH₄ and O₂. The excess energy escapes as heat. Neutralization reactions (mixing a strong acid with a strong base) are also exothermic: the formation of water from H⁺ and OH⁻ releases about 56 kJ/mol.

In an **endothermic reaction**, the products have higher enthalpy than the reactants — the system has absorbed energy from its surroundings. ΔH is positive, and the reaction vessel feels cold. Dissolving ammonium nitrate (NH₄NO₃) in water is a familiar example — this is the chemistry behind instant cold packs. The energy required to break apart the crystal lattice exceeds the energy released when ions are hydrated, so the net process absorbs heat. Photosynthesis is another endothermic process: plants use sunlight to drive the conversion of CO₂ and H₂O into glucose and O₂, storing the sun's energy in chemical bonds.

The sign convention is critical and often trips students up: ΔH is defined from the system's perspective. When the system *loses* heat (exothermic), ΔH is negative — even though the surroundings are gaining that heat. Think of it as the system's energy account balance: a withdrawal (energy leaving) is negative, a deposit (energy entering) is positive. An energy diagram makes this visual — exothermic reactions show products sitting below reactants on the enthalpy axis, with the vertical gap equal to |ΔH|. Endothermic reactions show products above reactants. This framework connects directly to your upcoming work with bond energies and Hess's Law, where you will calculate ΔH by tracking the energy cost of breaking bonds versus the energy released in forming new ones.
