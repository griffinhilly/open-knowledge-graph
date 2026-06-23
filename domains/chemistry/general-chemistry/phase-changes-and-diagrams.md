---
id: phase-changes-and-diagrams
title: Phase Changes and Diagrams
domain: chemistry
course: general-chemistry
prerequisites:
- id: thermochemistry-enthalpy
  type: hard
- id: intermolecular-forces
  type: hard
- id: states-of-matter-properties-and-transitions
  type: soft
builds-toward:
- vapor-pressure-raoults-law
tags:
- melting
- boiling
- sublimation
- phase-diagram
- triple-point
- critical-point
- heat-of-fusion
- heat-of-vaporization
stage: formal-systems
status: validated
---
# Phase Changes and Diagrams

## Core Idea
Matter transitions between solid, liquid, and gas phases when energy is added or removed. Melting (solid→liquid), vaporization (liquid→gas), and sublimation (solid→gas) are endothermic; their reverses are exothermic. During a phase transition, temperature remains constant as added energy breaks intermolecular forces rather than increasing kinetic energy. Phase diagrams plot pressure vs temperature and show which phase is stable under given conditions. The triple point is the unique P-T condition where all three phases coexist in equilibrium. The critical point marks the end of the liquid-gas boundary — above it, a supercritical fluid exists with properties of both phases.

## How It's Best Learned
Trace heating curves (temperature vs heat added) to see how temperature plateaus during phase transitions. Read phase diagrams by identifying regions, boundaries, and special points. Compare phase diagrams of water (negative solid-liquid slope) and CO₂ (positive slope) to understand how pressure affects melting.

## Common Misconceptions
- Boiling point is not a fixed property of a substance — it depends on external pressure. Water boils below 100°C at high altitude because atmospheric pressure is lower.
- During a phase transition, added heat does not raise temperature. Students often expect temperature to rise continuously; the plateaus on heating curves reflect energy going into overcoming intermolecular forces.

## Questions

```yaml
- question: "A pot of water is heated steadily at sea level. The temperature reaches 100°C and then stops rising for several minutes despite continued heating. Which explanation is correct?"
  type: multiple-choice
  options:
    - "The stove cannot deliver enough energy to raise water above 100°C"
    - "Added energy is increasing the kinetic energy of water molecules uniformly"
    - "Added energy is being used to overcome intermolecular attractions during vaporization, not to increase kinetic energy"
    - "Water reaches maximum molecular speed at 100°C and cannot absorb more energy"
  answer: 2
  explanation: "During a phase transition, added energy breaks intermolecular forces (here, hydrogen bonds) rather than increasing molecular kinetic energy — and temperature is a measure of kinetic energy. Until all the liquid has vaporized, all added energy goes into the heat of vaporization (40.7 kJ/mol for water), and the temperature stays constant. Students who expect continuous temperature rise have conflated 'adding heat' with 'raising temperature' — the two are not equivalent during phase transitions."

- question: "A mountaineer at high altitude (atmospheric pressure ~0.5 atm) wants to boil water for sterilization. Compared to sea level, the water will:"
  type: multiple-choice
  options:
    - "Boil at exactly 100°C because that is water's fixed boiling point"
    - "Boil at a higher temperature because reduced pressure means more energy is needed"
    - "Boil at a lower temperature because reduced pressure lowers the liquid-gas phase boundary"
    - "Not boil because pressure below 1 atm prevents vaporization"
  answer: 2
  explanation: "Boiling point is the temperature at which vapor pressure equals external pressure — not a fixed property of water. At lower atmospheric pressure, vapor pressure equals external pressure at a lower temperature. On the phase diagram, moving to a lower pressure crosses the liquid-gas boundary at a lower temperature. Water boils at roughly 80°C at high altitude — a practical concern since this temperature may be insufficient for some sterilization purposes."

- question: "During a phase transition such as melting, adding heat to the system causes the temperature to rise continuously."
  type: true-false
  answer: false
  explanation: "Temperature remains constant throughout a phase transition because all added energy is consumed breaking intermolecular forces (heat of fusion, heat of vaporization) rather than increasing molecular kinetic energy. Temperature only resumes rising once the phase transition is complete. Heating curves display this as a flat plateau — the distinctive signature of a phase change occurring at constant temperature."

- question: "Water's phase diagram has an unusual negative slope on its solid-liquid boundary, meaning that applying pressure to ice at 0°C can cause it to melt."
  type: true-false
  answer: true
  explanation: "Ice is less dense than liquid water — an unusual property. At a phase boundary, pressure favors the denser phase. Since liquid water is denser than ice, increasing pressure shifts the equilibrium toward liquid — hence the negative slope of the solid-liquid line in water's phase diagram. For nearly all other substances, the solid is denser and the slope is positive. This anomaly is why ice floats and why lakes freeze from the top down, enabling aquatic life to survive under ice."

- question: "Why does temperature remain constant during a phase transition even when heat is continuously added to the system?"
  type: short-answer
  answer: "Temperature is a measure of the average kinetic energy of molecules. During a phase transition, added energy is not increasing kinetic energy — it is being used to overcome the intermolecular forces holding molecules in their current arrangement (breaking crystal lattice bonds during melting, completely separating molecules during vaporization). Until all molecules have completed the transition, energy input goes into molecular separation, not molecular speed. Only after the transition is complete does further heat input raise the temperature again."
  explanation: "The key is distinguishing between thermal energy (total) and temperature (kinetic component only). A phase transition converts heat into potential energy stored in the separated molecular arrangement. This is why ΔH_vap for water (40.7 kJ/mol) is much larger than ΔH_fus (6.01 kJ/mol) — complete molecular separation requires far more energy than merely disrupting the lattice, and all of it goes into the transition at constant temperature."
```

## Explainer

From thermochemistry, you know that enthalpy changes track heat flow, and from intermolecular forces, you know that molecules attract each other through dipole-dipole interactions, hydrogen bonds, and London dispersion forces. Phase changes are what happen when thermal energy either overwhelms these intermolecular attractions or loses the battle against them. Melting, boiling, and sublimation are endothermic because energy must be absorbed to pull molecules apart; freezing, condensation, and deposition are exothermic because energy is released as molecules settle into closer, more ordered arrangements.

The **heating curve** makes the energy story visible. When you heat ice from −20°C, the temperature rises steadily as the added energy increases molecular kinetic energy (the sloped portions). But at 0°C something striking happens: the temperature stops rising even though you're still adding heat. All the incoming energy goes into breaking the hydrogen bonds that hold the ice lattice together — this is the **heat of fusion** (ΔH_fus = 6.01 kJ/mol for water). Only after all the ice has melted does the temperature resume climbing. The same plateau occurs at 100°C during vaporization, except the **heat of vaporization** (ΔH_vap = 40.7 kJ/mol) is much larger because vaporization requires completely separating molecules from each other, not just disrupting a lattice. This is why it takes far more energy to boil water away than to melt ice — and why steam burns are so much worse than hot water burns, as the condensing steam releases all that stored energy onto your skin.

A **phase diagram** maps which phase is thermodynamically stable at each combination of pressure and temperature. The boundaries between regions are lines where two phases coexist in equilibrium — the solid-liquid boundary, the liquid-gas boundary, and the solid-gas boundary. The **triple point** is the unique temperature and pressure where all three phase boundaries meet and all three phases coexist simultaneously (for water: 0.01°C, 0.006 atm). The **critical point** marks the end of the liquid-gas boundary — above this temperature and pressure, the distinction between liquid and gas disappears, and a **supercritical fluid** exists with properties of both phases (supercritical CO₂ is used as a solvent in decaffeination).

Water's phase diagram has a famous anomaly: its solid-liquid boundary slopes to the left (negative slope), meaning that increasing pressure at constant temperature can melt ice. This happens because ice is less dense than liquid water — pressure favors the denser phase. For nearly every other substance, the solid-liquid line slopes to the right (positive slope) because the solid is denser. This quirk of water is why ice floats, why lakes freeze from the top down, and why ice skating works — pressure under the blade slightly lowers the melting point, though the effect is much smaller than commonly claimed. Reading a phase diagram is a matter of placing your finger at a P-T coordinate and seeing which region you're in, then tracing how phase changes occur as you move along a path of changing temperature or pressure.
