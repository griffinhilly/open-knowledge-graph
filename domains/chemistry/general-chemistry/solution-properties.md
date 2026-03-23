---
id: solution-properties
title: 'Solutions and Solubility: Factors Affecting Dissolution'
domain: chemistry
course: general-chemistry
prerequisites:
- id: intermolecular-forces-overview
  type: hard
builds-toward:
- concentration-and-molarity
- colligative-properties-solutions
tags:
- solutions
- solubility
- solvents
- dissolution
- like dissolves like
stage: formal-systems
status: draft
---

# Solutions and Solubility: Factors Affecting Dissolution

## Core Idea
A solution is a homogeneous mixture where a solute dissolves in a solvent. Solubility depends on intermolecular forces ('like dissolves like'), temperature, and pressure. Polar solutes dissolve in polar solvents; nonpolar in nonpolar. Dissolution is an equilibrium process; a saturated solution contains the maximum dissolved solute at that temperature.

## Questions

```yaml
- question: "You want to dissolve a nonpolar organic compound in a solvent. Which solvent choice best applies the principle of 'like dissolves like'?"
  type: multiple-choice
  options:
    - "Water, because it is a universal solvent that dissolves most substances"
    - "Ethanol, because it is a liquid at room temperature and mixes with everything"
    - "Hexane, because its London dispersion forces match the nonpolar solute's intermolecular forces"
    - "Acetone, because it has a high boiling point that keeps the solute dissolved"
  answer: 2
  explanation: "'Like dissolves like' means the solute and solvent must have the same *type* of intermolecular forces. A nonpolar solute interacts via London dispersion forces, so a nonpolar solvent like hexane — which also relies on dispersion forces — provides the energetically favorable solute-solvent interactions needed for dissolution. Water is polar and forms strong hydrogen bonds; it would not accommodate nonpolar molecules because water molecules prefer each other. Ethanol has a polar hydroxyl group and does not universally dissolve nonpolar compounds. Boiling point is irrelevant to solubility."

- question: "A sealed bottle of soda is cold and fizzy. You warm it to room temperature and shake it. What happens to the dissolved CO₂, and why?"
  type: multiple-choice
  options:
    - "More CO₂ dissolves because warmer water has more kinetic energy to absorb gas molecules"
    - "The same amount of CO₂ stays dissolved because Henry's law only applies to very high pressures"
    - "CO₂ escapes from solution because gas solubility in liquids decreases as temperature rises"
    - "CO₂ stays dissolved until you open the bottle because temperature does not affect gas solubility"
  answer: 2
  explanation: "Gas solubility in liquids decreases with increasing temperature — the reverse of the trend for most solid solutes. As temperature rises, gas molecules gain enough kinetic energy to escape the solution more readily, shifting the dissolution equilibrium toward the gas phase. This is why a warm soda goes flat quickly and why boiling water degasses it. Opening the bottle releases the pressure, but warming already reduces solubility even while sealed."

- question: "A saturated solution cannot dissolve any additional solute under any circumstances."
  type: true-false
  answer: false
  explanation: "A saturated solution holds the maximum amount of solute *at that temperature and pressure*. Changing conditions — especially raising the temperature for most solid solutes — increases solubility, allowing more solute to dissolve. A supersaturated solution is even a case where more than the equilibrium amount is temporarily dissolved. 'Saturated' describes an equilibrium at specific conditions, not a permanent ceiling."

- question: "In a saturated solution, dissolution has stopped and the system is static — no solute is entering or leaving the solid."
  type: true-false
  answer: false
  explanation: "Saturation is a *dynamic* equilibrium, not a static one. Solute molecules continue to leave the solid surface and enter solution (dissolution), while dissolved molecules continue to return to the solid (recrystallization) at equal rates. The net concentration remains constant, but both processes proceed continuously. This is the same type of dynamic equilibrium seen in other reversible processes like vapor pressure equilibrium."

- question: "Why does oil not dissolve in water, even though both are liquids?"
  type: short-answer
  answer: "Oil molecules interact through weak London dispersion forces, while water molecules form strong hydrogen bonds with each other. For dissolution to occur, solute-solvent interactions must be comparable in strength to the solute-solute and solvent-solvent interactions they replace. Inserting nonpolar oil molecules into water would disrupt water's hydrogen-bond network without providing comparable compensating interactions, making dissolution energetically unfavorable. Water molecules effectively exclude the oil, which clusters together instead."
  explanation: "The 'like dissolves like' principle reflects an energy and intermolecular force argument, not just a polarity label. The key is whether the energy required to break existing solute-solute and solvent-solvent interactions is offset by the energy gained from new solute-solvent interactions. When the force types are mismatched (London dispersion vs. hydrogen bonding), they cannot compensate each other, and dissolution does not occur."
```

## Explainer

A **solution** forms when one substance (the **solute**) disperses uniformly throughout another (the **solvent**) at the molecular level. Unlike a suspension or colloid, you cannot see the individual solute particles — the mixture is homogeneous. The most familiar example is salt dissolving in water, but solutions also include gases dissolved in liquids (carbon dioxide in soda), liquids in liquids (ethanol in water), and even solids in solids (metal alloys like bronze).

The central principle governing solubility is **"like dissolves like,"** which builds directly on your understanding of intermolecular forces. When a solute's intermolecular forces are similar in type and strength to those of the solvent, the solute-solvent interactions can effectively replace the solute-solute and solvent-solvent interactions that must be broken during dissolution. Table salt (NaCl) dissolves readily in water because water's strong dipole can stabilize the separated Na⁺ and Cl⁻ ions through ion-dipole forces. Oil does not dissolve in water because oil molecules interact through weak London dispersion forces, and these cannot compete with the strong hydrogen bonds that water molecules form with each other — water molecules would rather stay bonded to each other than accommodate nonpolar intruders.

Dissolution is an **equilibrium process**. When you first add a solid solute to a solvent, molecules leave the solid surface and enter solution. As the concentration of dissolved solute increases, some dissolved molecules return to the solid. Eventually, the rate of dissolution equals the rate of recrystallization, and the solution is **saturated** — it holds the maximum amount of solute at that temperature. An **unsaturated** solution contains less than this maximum and can dissolve more. A **supersaturated** solution temporarily holds more dissolved solute than equilibrium allows, and a small disturbance (a seed crystal, a scratch on the glass) can trigger rapid crystallization.

Temperature and pressure also affect solubility in predictable ways. For most solid solutes in liquid solvents, solubility increases with temperature — the extra thermal energy helps overcome the lattice forces holding the solid together. For gases dissolved in liquids, the pattern reverses: solubility decreases with temperature (which is why a warm soda goes flat faster) and increases with pressure, as described by **Henry's law**. These relationships matter in contexts from cooking (why you degas water by boiling it) to deep-sea diving (why ascending too quickly causes nitrogen bubbles to form in the blood).
