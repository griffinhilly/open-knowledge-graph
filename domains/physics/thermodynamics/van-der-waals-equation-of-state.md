---
id: van-der-waals-equation-of-state
title: The van der Waals Equation of State
domain: physics
course: thermodynamics
prerequisites:
- id: real-gas-deviations
  type: hard
- id: virial-equation-and-intermolecular-forces
  type: soft
builds-toward:
- compressibility-factor-z
- critical-point-phenomena
tags:
- equations-of-state
- intermolecular-forces
- phase-transitions
stage: formal-systems
status: validated
---
# The van der Waals Equation of State

## Core Idea
The van der Waals equation (P + a(n/V)²)(V - nb) = nRT accounts for intermolecular attractions (a term) and molecular size (b term), providing better accuracy than the ideal gas law for real gases. The constants a and b are substance-specific, with a reflecting the strength of intermolecular forces and b representing the excluded volume per mole. The van der Waals equation predicts a critical point and qualitatively explains phase transitions, making it a useful model for intermediate pressures and temperatures.

## How It's Best Learned
Expand the van der Waals equation and recover the ideal gas law as a → 0, b → 0. Find the critical point by setting (∂P/∂V)_T = 0 and (∂²P/∂V²)_T = 0.

## Common Misconceptions
- Thinking the van der Waals equation predicts liquefaction exactly (it is qualitatively correct but quantitatively rough).
- Confusing the parameters a and b with measurable quantities (they are fitted constants).
- Assuming the van der Waals equation applies equally well at all pressures.

## Questions

```yaml
- question: "In the van der Waals equation (P + a(n/V)²)(V − nb) = nRT, why is the measured pressure P lower than what the ideal gas law predicts at the same temperature and volume?"
  type: multiple-choice
  options:
    - "The b term reduces the effective volume, which in turn reduces the pressure"
    - "The a term accounts for intermolecular attractions that pull molecules away from the container wall before they can strike it, reducing impact force"
    - "Both terms reduce pressure equally at high densities"
    - "Pressure is not lower in real gases — van der Waals only corrects for volume effects"
  answer: 1
  explanation: "The a correction addresses intermolecular attraction. Molecules in the bulk of the gas are pulled equally in all directions, so attractions cancel. But molecules near the wall have fewer neighbors on the outward side and are pulled back toward the bulk. This reduces their impact force on the wall — the measured pressure is lower than ideal. The equation compensates by adding a(n/V)² to P, restoring the pressure the gas would have without attractions. The b term corrects for excluded volume (reducing free volume), not for reduced wall pressure."

- question: "Gas A has a large van der Waals a constant; Gas B has a large van der Waals b constant. What does each constant tell you about the respective gas?"
  type: multiple-choice
  options:
    - "Gas A has large molecules; Gas B has strong intermolecular attractions"
    - "Gas A has strong intermolecular attractive forces; Gas B has large molecules that exclude significant volume"
    - "Gas A is easier to compress; Gas B has a lower boiling point"
    - "Both a and b measure deviation from ideality — just at different temperatures"
  answer: 1
  explanation: "The a constant reflects the strength of intermolecular attractive forces — large a means molecules attract each other strongly, pulling them back from the walls and causing the gas to deviate significantly from ideal behavior (especially at lower temperatures). The b constant reflects molecular size — large b means molecules themselves occupy a significant fraction of the container volume, so free volume is much less than total volume. These are physically distinct corrections: a is about forces between molecules, b is about the space they take up."

- question: "Setting a = 0 and b = 0 in the van der Waals equation exactly recovers the ideal gas law PV = nRT."
  type: true-false
  answer: true
  explanation: "Substituting a = 0 and b = 0 into (P + a(n/V)²)(V − nb) = nRT gives (P + 0)(V − 0) = nRT, which is exactly PV = nRT. This is a crucial consistency check: the van der Waals equation is not a replacement for the ideal gas law but a correction that reduces to it when molecular attractions and molecular volume are negligible — physically, at very low pressure or very high temperature where molecules are far apart."

- question: "The van der Waals equation gives quantitatively accurate predictions of gas behavior across all pressures and temperatures, including near phase transitions."
  type: true-false
  answer: false
  explanation: "The van der Waals equation is qualitatively excellent — it correctly predicts deviations from ideality, the existence of a critical point, and qualitatively explains phase transitions. But it is quantitatively rough, especially near phase transitions. It predicts an unphysical 'van der Waals loop' (a region where ∂P/∂V > 0) in the two-phase region, and predicted liquid volumes are systematically too large. For precision engineering calculations, more elaborate equations of state are required. Van der Waals is a teaching model that gives correct physical intuition, not an engineering tool."

- question: "Describe the physical meaning of the van der Waals b correction. Why does its effect become significant at high pressure but negligible at low pressure?"
  type: short-answer
  answer: "The b correction accounts for the finite volume of the gas molecules themselves. In the ideal gas law, V is the total container volume, as if molecules were point particles. Real molecules occupy space, so the volume available for molecular motion is V − nb, where b is the excluded volume per mole. At low pressure, molecules are widely separated and nb is a tiny fraction of total V — the correction is negligible. At high pressure, molecules are crowded together and nb becomes an appreciable fraction of V, meaning the ideal gas law significantly overestimates the free space available."
  explanation: "The analogy: in a nearly empty stadium, the space taken up by each seat is irrelevant — there's effectively infinite room. Pack the stadium to capacity and the seat volume becomes crucial. Similarly, excluded volume matters only when the gas is compressed to high density. This is why real gases at low pressure (widely separated molecules) behave nearly ideally, and deviation grows with pressure."
```

## Explainer

You already know from your study of real gas deviations that the ideal gas law breaks down under high pressure and low temperature. The ideal gas model treats molecules as point particles with no volume and no attraction to each other. Both assumptions fail in reality — molecules occupy space and pull on each other. The van der Waals equation fixes both flaws with just two extra constants, giving a much more realistic picture of gas behavior.

The **b term** (the "excluded volume" correction) addresses molecular size. In the ideal gas law, volume V is the total container volume. But molecules themselves take up space, so the free volume available for motion is not V but V − nb, where n is the number of moles and b is the volume excluded per mole. Think of it like having a room full of people: the space each person can move around in is the room volume minus the space the other people occupy. Subtracting nb from V corrects for this overcrowding effect, which becomes significant only when molecules are packed tightly — that is, at high pressures.

The **a term** (the "intermolecular attraction" correction) addresses the pull between molecules. In the bulk of the gas, a molecule is surrounded equally on all sides, so the attractions cancel out. But molecules near the container wall have fewer neighbors on the outward side, so they are tugged backward by the bulk. This reduces the force with which they strike the wall, meaning the actual pressure is slightly lower than the ideal formula predicts. The correction adds a/V²ₘ (or a(n/V)² in the full equation) back onto the measured pressure to recover what the pressure would be without intermolecular attraction. Substances with strong intermolecular forces have large a values; noble gases have small a values.

Putting it together: (P + a(n/V)²)(V − nb) = nRT. Notice that if a → 0 and b → 0, this collapses exactly to the ideal gas law PV = nRT — a good sanity check that the correction is additive, not a replacement. The equation also predicts a **critical point**, the temperature and pressure above which a gas cannot be liquefied no matter how much pressure is applied. At the critical point, the van der Waals isotherm has both its first and second derivatives equal to zero with respect to volume — a mathematical condition that lets you derive the critical temperature, pressure, and volume in terms of a and b. This is a remarkable prediction from a two-parameter model.

The honest limitation: the van der Waals equation is qualitatively excellent but quantitatively rough, especially near phase transitions. It predicts the S-shaped "van der Waals loop" in the pressure-volume diagram that signals a phase transition, but real condensation is sharper and the predicted liquid volumes are too large. For engineering calculations requiring precision, more elaborate equations of state are used. But van der Waals gives you the right physical intuition — that real gases behave ideally when molecules are far apart, and deviate most when they are crowded or cold enough that attractions matter.
