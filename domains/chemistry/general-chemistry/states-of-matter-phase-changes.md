---
id: states-of-matter-phase-changes
title: 'States of Matter and Phase Changes: Melting, Boiling, and Sublimation'
domain: chemistry
course: general-chemistry
prerequisites:
- id: intermolecular-forces
  type: hard
- id: boiling-and-condensation
  type: soft
- id: energy-in-phase-changes
  type: soft
- id: melting-and-freezing
  type: soft
- id: solids-liquids-gases
  type: soft
builds-toward:
- gas-laws-ideal-gas
- thermochemistry-heat-and-energy
tags:
- states of matter
- phase changes
- melting point
- boiling point
stage: formal-systems
status: validated
---

# States of Matter and Phase Changes: Melting, Boiling, and Sublimation

## Core Idea
Matter exists as solid (fixed shape), liquid (fixed volume), or gas (expands to fill container). Phase changes occur when temperature or pressure changes provide enough energy to overcome intermolecular forces. Melting (solid→liquid), boiling (liquid→gas), and sublimation (solid→gas) are endothermic; reverse processes are exothermic. Heat of fusion and vaporization quantify energy needed.

## Questions

```yaml
- question: "You are heating ice at a constant rate. When the temperature reaches 0°C, it stays constant for several minutes even though you continue adding heat. What explains this?"
  type: multiple-choice
  options:
    - "The heat source loses efficiency as it warms the surrounding environment, reducing effective heat transfer"
    - "Ice requires extra energy to increase its temperature once partial melting has begun"
    - "The added energy is consumed breaking intermolecular attractions in the crystal lattice rather than increasing molecular kinetic energy"
    - "The thermometer reads incorrectly near the freezing point due to the latent heat effect"
  answer: 2
  explanation: "During a phase change, added energy goes entirely into breaking intermolecular bonds (overcoming the crystal lattice in this case), not into increasing the speed of molecules. Since temperature measures average kinetic energy, and kinetic energy isn't increasing, temperature stays constant. This energy is the heat of fusion (ΔH_fus). Only once all the solid has melted — all lattice bonds broken — does further heating increase molecular speed and temperature again."

- question: "Ethanol (which forms hydrogen bonds) boils at 78°C, while propane (similar molar mass, only London dispersion forces) boils at −42°C. What is the correct explanation for this 120°C difference in boiling point?"
  type: multiple-choice
  options:
    - "Propane molecules move faster at any given temperature because they are slightly lighter"
    - "Ethanol's stronger intermolecular forces require more kinetic energy to overcome before molecules can escape the liquid phase"
    - "Propane's smaller molecular volume allows molecules to escape the liquid surface more easily"
    - "Hydrogen bonds in ethanol prevent sublimation, forcing the substance to pass through the liquid phase and raising its boiling point"
  answer: 1
  explanation: "Boiling occurs when molecules gain enough kinetic energy to escape the collective pull of intermolecular forces. Ethanol's hydrogen bonds are much stronger than propane's London dispersion forces, requiring a higher temperature (more kinetic energy) before enough molecules can escape to maintain a vapor phase at atmospheric pressure. This relationship is the predictive core of this topic: stronger intermolecular forces → higher boiling point. Molecular weight differences are a factor but secondary to force strength here."

- question: "The heat of vaporization for a substance is always larger than its heat of fusion because converting liquid to gas requires completely overcoming intermolecular forces, while melting only partially disrupts them."
  type: true-false
  answer: true
  explanation: "In the solid-to-liquid transition, molecules break free of fixed lattice positions but remain within the collective pull of nearby molecules — they can still slide past each other but don't escape entirely. In the liquid-to-gas transition, molecules must overcome all remaining intermolecular attractions to fly freely. Because complete escape requires breaking more interactions than partial disordering, ΔH_vap is always substantially larger than ΔH_fus. For water, ΔH_vap ≈ 40.7 kJ/mol vs. ΔH_fus ≈ 6.0 kJ/mol — nearly a 7-fold difference."

- question: "During sublimation, a solid converts directly to gas without passing through the liquid phase, which means it bypasses the energy cost of overcoming intermolecular forces."
  type: true-false
  answer: false
  explanation: "Sublimation requires overcoming intermolecular forces just as thoroughly as boiling — in fact, solid molecules must escape from a more tightly ordered lattice directly into the gas phase. The total enthalpy of sublimation approximately equals ΔH_fus + ΔH_vap because all intermolecular interactions must be broken. Sublimation occurs not because less energy is needed, but because surface molecules gain sufficient energy to escape without the intermediate liquid state being thermodynamically stable under those conditions of temperature and pressure."

- question: "Why does temperature remain constant during a phase change even when heat is continuously being added to the system?"
  type: short-answer
  answer: "Temperature measures the average kinetic energy of molecules. During a phase change, added energy is used entirely to break intermolecular bonds (e.g., overcoming lattice attractions during melting, or breaking all remaining intermolecular attractions during boiling) rather than increasing molecular speed. Since kinetic energy isn't increasing, temperature doesn't increase. Only once the phase transition is complete — all the bonds that needed to be broken have been broken — does further energy input increase molecular kinetic energy and raise the temperature again."
  explanation: "This is why phase transitions appear as flat plateaus on heating curves. The energy going in during the plateau is the latent heat (heat of fusion or vaporization). It's 'hidden' in the sense that it doesn't register as a temperature change. This also explains why steam burns are more severe than boiling water burns at the same temperature: steam releases both sensible heat (cooling to 100°C) and the full heat of condensation as it returns to liquid."
```

## Explainer

From your study of intermolecular forces, you know that molecules attract each other through dipole-dipole interactions, hydrogen bonds, and London dispersion forces. The state of matter a substance adopts is fundamentally a contest between these attractive forces pulling molecules together and **kinetic energy** (thermal motion) trying to fling them apart. In a solid, intermolecular forces win decisively — molecules vibrate in fixed positions within an ordered lattice. In a liquid, kinetic energy is high enough that molecules slide past each other but not high enough to escape the collective pull entirely. In a gas, kinetic energy overwhelms the attractions and molecules fly freely, filling whatever container they occupy.

A **phase change** happens at the tipping point where the balance shifts. When you heat ice, you add kinetic energy. At 0°C, the molecules have enough energy to break free of the rigid crystal lattice — this is **melting**. Crucially, temperature stays constant during a phase change even though you keep adding heat. That energy is not increasing molecular speed; it is being consumed entirely by breaking intermolecular attractions. The energy required to melt one mole of a substance is its **heat of fusion** (ΔH_fus). Continue heating the liquid water to 100°C, and molecules gain enough energy to escape the liquid surface entirely — **boiling**. The **heat of vaporization** (ΔH_vap) is always much larger than the heat of fusion because going from liquid to gas requires completely overcoming intermolecular forces, whereas melting only loosens the structure partially.

**Sublimation** — a solid converting directly to gas, as dry ice does — occurs when surface molecules gain enough energy to escape the lattice entirely without passing through the liquid phase. This happens when vapor pressure at the solid's surface exceeds atmospheric conditions that would otherwise stabilize a liquid. The reverse processes — freezing, condensation, and deposition — are **exothermic** because forming intermolecular attractions releases energy. Every phase change is thus a story told in the language of intermolecular forces: stronger forces mean higher melting and boiling points, larger heats of fusion and vaporization, and a greater reluctance to enter the gas phase.

The practical consequence is predictive power. If you know a substance has strong hydrogen bonding (like water), you can predict it will have an unusually high boiling point relative to its molecular weight. If a substance has only weak London dispersion forces (like methane), it will be a gas at room temperature. Phase diagrams, which you will encounter later, map out these relationships across all combinations of temperature and pressure, but the underlying logic is always the same: intermolecular forces versus kinetic energy.
