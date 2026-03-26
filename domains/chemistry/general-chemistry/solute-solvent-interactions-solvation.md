---
id: solute-solvent-interactions-solvation
title: Solvation and Hydration Processes
domain: chemistry
course: general-chemistry
prerequisites:
- id: intermolecular-forces
  type: hard
- id: ionic-bonding
  type: soft
builds-toward:
- dissolution-equilibrium-and-saturation
- solution-thermodynamics
tags:
- solvation
- hydration
- dissolution
- solubility
stage: formal-systems
status: validated
---

# Solvation and Hydration Processes

## Core Idea
Dissolution occurs when solute-solvent interactions overcome solute-solute and solvent-solvent interactions. Solvation (or hydration in water) is the process where solvent molecules surround and stabilize dissolved ions or molecules. Polar solvents excel at dissolving ionic compounds; nonpolar solvents dissolve nonpolar solutes (like dissolves like).

## Questions

```yaml
- question: "Oil and water are famously immiscible. Which explanation best captures why, in terms of intermolecular forces?"
  type: multiple-choice
  options:
    - "Oil molecules are too large to fit between water molecules"
    - "Water molecules form strong hydrogen bonds with each other; accommodating nonpolar oil would cost more energy than nonpolar oil-water interactions can provide"
    - "Oil and water have different densities, so they naturally separate by gravity"
    - "Oil molecules carry a net negative charge that repels water's partial charges"
  answer: 1
  explanation: "Dissolution is an energy competition. Water's hydrogen-bonding network is highly stabilized. To dissolve oil, you'd have to disrupt that network and get back enough energy from oil-water interactions to compensate — but nonpolar oil can only offer weak London dispersion forces to water, nowhere near enough. The density/gravity explanation (C) describes the result, not the cause: even if you force them to mix, they separate because the thermodynamics are unfavorable."

- question: "When NaCl dissolves in water, each Na⁺ ion ends up surrounded by a hydration shell. How are water molecules oriented in that shell?"
  type: multiple-choice
  options:
    - "Randomly — the orientation depends on local turbulence"
    - "With hydrogen atoms pointing toward Na⁺, forming hydrogen bonds with it"
    - "With oxygen atoms (partially negative) pointing toward Na⁺, forming ion-dipole interactions"
    - "With oxygen atoms pointing away from Na⁺ to minimize repulsion"
  answer: 2
  explanation: "Na⁺ is a positive ion. Water's oxygen atom carries a partial negative charge (δ−), so it orients toward the cation to form an attractive ion-dipole interaction. The hydrogen atoms (δ+) orient toward anions like Cl⁻. This directional arrangement — not random orientation — is precisely what solvation means: a structured stabilizing shell formed by favorable electrostatic alignment."

- question: "Dissolution is generally exothermic — it releases heat as solute-solvent interactions form."
  type: true-false
  answer: false
  explanation: "Many substances dissolve endothermically (absorbing heat). Ammonium nitrate dissolving in water is a classic example — the pack gets cold. Dissolution is thermodynamically favorable when the overall free energy decreases, which requires considering both enthalpy (energy of breaking and forming interactions) and entropy (increase in disorder). Endothermic dissolution can proceed spontaneously when the entropy gain is large enough. The energy gained from solute-solvent interactions need not exceed the energy required to separate solute and solvent particles."

- question: "Grease dissolves in mineral spirits (a nonpolar solvent) but not in water because grease molecules can only form London dispersion interactions."
  type: true-false
  answer: true
  explanation: "Grease is a nonpolar substance and can only participate in London dispersion forces — it has no permanent dipoles, no -OH groups, no charged regions. Mineral spirits is also nonpolar, so grease-mineral spirits dispersion interactions are comparable in energy to the grease-grease and mineral spirits-mineral spirits interactions being broken, making dissolution energetically favorable. Water, by contrast, is held together by strong hydrogen bonds; disrupting that network to accommodate nonpolar grease would cost far more energy than weak grease-water dispersion forces can recover."

- question: "Explain why ethanol (which has an -OH group) is miscible with water in all proportions, while hexane (a nonpolar hydrocarbon) separates from water immediately."
  type: short-answer
  answer: "Ethanol's -OH group can form hydrogen bonds with water molecules, providing strong solute-solvent interactions. The energy gained from these ethanol-water hydrogen bonds is sufficient to compensate for disrupting the water-water and ethanol-ethanol hydrogen bonds being broken. Hexane is nonpolar and can only offer London dispersion forces to water. These are far too weak to compensate for disrupting water's strong hydrogen-bonding network, so the energy balance strongly disfavors dissolution. This is the 'like dissolves like' principle in operation: matching interaction types makes dissolution thermodynamically favorable."
```

## Explainer

From your study of intermolecular forces, you know that molecules attract each other through dipole-dipole interactions, hydrogen bonds, and London dispersion forces. Dissolution is fundamentally a competition among three sets of these forces. To dissolve a solute, you must first pull solute particles apart from each other (breaking solute-solute interactions), then push solvent molecules aside to make room (breaking solvent-solvent interactions), and finally form new attractive contacts between solute and solvent (creating solute-solvent interactions). Dissolution is favorable when the energy gained from new solute-solvent interactions roughly compensates for the energy spent breaking the other two.

**Solvation** is the name for the process where solvent molecules arrange themselves around each dissolved particle, forming a stabilizing shell. When the solvent is water, this process is called **hydration**. Picture dropping a crystal of NaCl into water: at the crystal surface, the partially negative oxygen atoms of water molecules orient toward Na⁺ ions, while the partially positive hydrogen atoms point toward Cl⁻ ions. These ion-dipole interactions are strong enough to overcome the ionic lattice energy holding the crystal together. Each ion ends up surrounded by a structured cage of water molecules — its **hydration shell** — which stabilizes the ion in solution and prevents it from recombining with its counterion.

The "like dissolves like" rule is a practical shortcut that follows directly from this energy analysis. Polar solvents like water form strong dipole-dipole and hydrogen-bonding interactions among themselves. To dissolve in water, a solute must offer comparably strong interactions — ionic compounds and polar molecules qualify, but nonpolar molecules like oil cannot form strong enough interactions with water to compensate for disrupting water's hydrogen-bonding network. Conversely, nonpolar solvents like hexane interact through weak London dispersion forces. Nonpolar solutes dissolve easily because the solute-solvent dispersion forces are similar in strength to the solute-solute and solvent-solvent forces being broken.

Understanding solvation at this level explains many everyday observations. Sugar dissolves in water because its many -OH groups form hydrogen bonds with water. Grease does not dissolve in water but dissolves readily in mineral spirits because both are nonpolar. Soap works by having a polar head that interacts with water and a nonpolar tail that interacts with grease — bridging the two incompatible worlds. The energetics of solvation also set the stage for understanding saturation limits, colligative properties, and the thermodynamics of solutions that you will encounter next.
