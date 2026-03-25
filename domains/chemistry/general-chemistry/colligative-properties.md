---
id: colligative-properties
title: Colligative Properties
domain: chemistry
course: general-chemistry
prerequisites:
- id: solution-concentration
  type: hard
- id: intermolecular-forces
  type: soft
- id: colligative-properties-solutions
  type: soft
tags:
- boiling-point-elevation
- freezing-point-depression
- osmotic-pressure
- Raoults-law
- vant-Hoff-factor
stage: formal-systems
status: validated
---
# Colligative Properties

## Core Idea
Colligative properties depend only on the number of dissolved solute particles, not their chemical identity. Adding a nonvolatile solute lowers vapor pressure (Raoult's law), elevates boiling point (ΔTb = iKbm), depresses freezing point (ΔTf = iKfm), and creates osmotic pressure (π = iMRT). The van't Hoff factor i accounts for dissociation of electrolytes: NaCl gives i ≈ 2, AlCl₃ gives i ≈ 4. These effects are used to determine molar masses experimentally and explain biological phenomena like cell osmosis.

## How It's Best Learned
Practice calculating ΔTb and ΔTf for both electrolyte and nonelectrolyte solutes. Emphasize the van't Hoff factor: compare equal concentrations of glucose and NaCl. Connect osmotic pressure to real-world applications like IV drips, dialysis, and why salting roads melts ice.

## Common Misconceptions
- Colligative properties depend on particle count, not identity or mass — 1 mol of NaCl has roughly twice the colligative effect of 1 mol of sugar because NaCl dissociates into two ions.
- The van't Hoff factor for electrolytes is slightly less than the theoretical integer value because ion pairing reduces the effective particle count at typical concentrations.

## Questions

```yaml
- question: "Equal molar amounts (1 mol each) of glucose and NaCl are dissolved in separate 1 kg samples of water. Which solution will have the greater freezing point depression, and why?"
  type: multiple-choice
  options:
    - "The glucose solution, because glucose has a higher molar mass"
    - "They will be equal, because both solutions contain the same number of moles of solute"
    - "The NaCl solution, because NaCl dissociates into approximately two ions per formula unit, doubling the effective particle count"
    - "The NaCl solution, because ionic solutes always lower the freezing point more than molecular solutes regardless of concentration"
  answer: 2
  explanation: "Colligative properties depend on the number of dissolved particles, not the chemical identity or mass of the solute. NaCl dissociates into Na⁺ and Cl⁻ (i ≈ 2), effectively producing ~2 mol of particles per mol of NaCl dissolved. Glucose does not dissociate (i = 1). ΔTf = iKfm, so the NaCl solution has roughly twice the freezing point depression. Option D is wrong because it's particle count, not ionic character per se, that matters."

- question: "Two solutions at the same molality must have the same boiling point elevation if they are at the same temperature and pressure."
  type: true-false
  answer: false
  explanation: "Boiling point elevation depends on the total concentration of dissolved particles (ΔTb = iKbm), so the van't Hoff factor i matters. A 1.0 m NaCl solution (i ≈ 2) has roughly twice the boiling point elevation of a 1.0 m glucose solution (i = 1). Equal molality does not guarantee equal colligative effects unless the solutes have the same degree of dissociation."

- question: "Why does salting an icy road cause the ice to melt at temperatures below 0°C? Invoke the relevant colligative property in your answer."
  type: short-answer
  answer: "Salt (NaCl) dissolves in a thin film of liquid water on the ice surface and dissociates into Na⁺ and Cl⁻, increasing the total dissolved particle concentration. This lowers the freezing point of the solution below 0°C via freezing point depression (ΔTf = iKfm). As long as the ambient temperature is above the new (depressed) freezing point of the brine, the ice melts into liquid solution rather than remaining solid."
  explanation: "This question connects the abstract formula to a concrete physical process. The key insight is that adding dissolved particles disrupts the equilibrium between liquid and solid water — the solution's chemical potential is lower than that of pure ice at 0°C, so ice melts to reach a new equilibrium. This is the same thermodynamic logic behind all colligative properties."
```

## Explainer

You already know from studying solution concentration that molarity and molality describe how much solute is dissolved. Colligative properties extend that idea with a surprising twist: it does not matter *what* you dissolve, only *how many particles* you create. Drop a handful of sugar or a handful of salt into the same amount of water — the chemical identities are completely different, but the physical effects on the solvent (vapor pressure, boiling point, freezing point, osmotic pressure) depend only on the total particle count.

The anchor equation for two of the most useful colligative properties is ΔT = iKm, where ΔT is the change in boiling or freezing point, K is a solvent-specific constant (Kb for boiling, Kf for freezing), m is molality, and i is the van't Hoff factor. For non-electrolytes like glucose, i = 1 — one mole of molecules produces one mole of particles. For electrolytes, i equals the number of ions per formula unit: NaCl gives i ≈ 2, CaCl₂ gives i ≈ 3, AlCl₃ gives i ≈ 4. The "approximately" matters: at realistic concentrations, ion pairing slightly reduces the effective number of independent particles, so measured i values fall a bit short of the theoretical integers. This is a real-world correction, not a flaw in the theory.

Raoult's law connects colligative properties to vapor pressure: adding a nonvolatile solute lowers the vapor pressure of the solvent proportionally to the mole fraction of the solute. Intuitively, solute molecules occupy the surface, reducing the rate at which solvent molecules escape into the gas phase. A lower vapor pressure means the solvent needs to be heated to a higher temperature before its vapor pressure equals atmospheric pressure — hence boiling point elevation. Conversely, dissolved particles disrupt the lattice-forming ability of the solvent at its normal freezing point — hence freezing point depression. Both effects flow from the same underlying cause.

Osmotic pressure (π = iMRT) is the colligative property most relevant to biology. Water moves across a semipermeable membrane from regions of low solute concentration (high water activity) to high solute concentration (low water activity) — this is osmosis. The pressure required to stop this flow is the osmotic pressure. Red blood cells in a hypotonic solution (less solute than inside the cell) swell and can lyse; in a hypertonic solution, they shrink. IV fluids must be carefully formulated to be isotonic — matching the osmotic pressure of blood — for exactly this reason.

A practical application ties it together: measuring freezing point depression experimentally lets you determine the molar mass of an unknown solute. You measure ΔTf, you know Kf and the mass of solvent you used, and you solve for molality. From molality and the known mass of solute dissolved, you calculate the molar mass. This technique, called cryoscopy, was historically important in chemistry before modern mass spectrometry and remains a clean illustration of how a macroscopic measurement can reveal a molecular-scale property.
