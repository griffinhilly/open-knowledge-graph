---
id: kinetic-molecular-theory-overview
title: Kinetic Molecular Theory of Gases
domain: chemistry
course: general-chemistry
prerequisites:
- id: gas-laws
  type: hard
- id: states-of-matter-properties-and-transitions
  type: hard
builds-toward:
- gas-pressure-from-kinetic-theory
- heat-capacity-calorimetry
tags:
- kinetic-theory
- gases
- molecular-motion
- pressure
stage: formal-systems
status: draft
---

# Kinetic Molecular Theory of Gases

## Core Idea
Kinetic molecular theory explains gas behavior at the molecular level: gas molecules are in random, continuous motion, collisions between molecules are elastic, and average kinetic energy is proportional to absolute temperature. This microscopic view connects observable properties like pressure and temperature to molecular motion.

## How It's Best Learned
Visualize gas molecules in constant motion and connect pressure (force from collisions) to molecular speed and density. Derive gas law relationships from KMT assumptions.

## Questions

```yaml
- question: "A sealed container of gas is heated from 200 K to 400 K. By what factor does the average kinetic energy of the gas molecules change?"
  type: multiple-choice
  options:
    - "It doubles, because average kinetic energy is directly proportional to absolute temperature"
    - "It increases by √2, because molecular speed is proportional to √T and kinetic energy scales with speed"
    - "It quadruples, because both molecular speed and mass increase with temperature"
    - "It stays the same, because the molecules are confined and cannot do work on their surroundings"
  answer: 0
  explanation: "From KE_avg = (3/2)kT, doubling T (200 K → 400 K) directly doubles the average kinetic energy. Option B reflects the classic confusion: the rms speed is proportional to √T, but kinetic energy is ½mv² ∝ v² ∝ T — the T not √T relationship. Students who know 'speed increases with temperature' without knowing the exact scaling often select the wrong factor. Average speed ≠ average kinetic energy."

- question: "A container at room temperature holds a mixture of hydrogen gas (H₂, molar mass 2 g/mol) and oxygen gas (O₂, molar mass 32 g/mol). What can you conclude about their average kinetic energies and average speeds?"
  type: multiple-choice
  options:
    - "Both gases have the same average kinetic energy and the same average speed"
    - "H₂ molecules have lower kinetic energy and higher speed than O₂ molecules"
    - "Both gases have the same average kinetic energy, but H₂ molecules move faster"
    - "O₂ molecules have higher average kinetic energy because they are heavier"
  answer: 2
  explanation: "By KMT, at the same temperature all gases have the same average kinetic energy: KE_avg = (3/2)kT regardless of mass. But since KE = ½mv², equal KE with lower mass requires higher speed. H₂ is 16× lighter than O₂, so its rms speed is √16 = 4 times greater. Option D is the most tempting misconception — students associate mass with energy in everyday experience, but in KMT it is temperature (not mass) that sets the kinetic energy."

- question: "At the same temperature, hydrogen molecules move faster on average than oxygen molecules because hydrogen has lower molecular mass."
  type: true-false
  answer: true
  explanation: "From KE = ½mv², equal average kinetic energy at equal temperature means v ∝ 1/√m. Lighter molecules must move faster to have the same kinetic energy. This directly explains Graham's law of effusion: lighter gases escape through small openings faster because their molecules are individually moving faster at the same temperature."

- question: "Temperature causes molecules to move faster; it is a separate property of matter that drives molecular motion as an external force."
  type: true-false
  answer: false
  explanation: "This reverses the conceptual relationship. Temperature IS average molecular kinetic energy — KE_avg = (3/2)kT defines temperature in terms of motion. There is no separate 'temperature substance' that pushes molecules around. Saying 'temperature causes molecular motion' is like saying 'bank balance causes money to exist.' Higher temperature means the molecules are already moving faster; the temperature measurement quantifies that motion rather than being a cause external to it."

- question: "How does kinetic molecular theory explain why pressure doubles when you halve the volume of a gas at constant temperature (Boyle's law)?"
  type: short-answer
  answer: "Pressure results from molecular collisions with container walls. Halving the volume at constant temperature has two compounding effects: (1) the same number of molecules must hit half as much wall area, and (2) molecules travel shorter distances between walls and therefore collide with the walls roughly twice as frequently. Both effects double the collision rate per unit area, doubling the pressure. The molecules' average speed has not changed (temperature is constant), but each unit of wall area receives twice as many impacts per second."
  explanation: "This is the molecular explanation that makes Boyle's law intuitive rather than just empirical. The pressure increase is not because molecules hit harder — it is because they hit more often. This also explains why the ideal gas law PV = nRT is linear in both P and V: both effects scale linearly with compression."
```

## Explainer

The gas laws you have already learned — Boyle's law, Charles's law, Avogadro's law, and the ideal gas law — describe *what* gases do: pressure drops when volume increases, volume rises with temperature, and so on. **Kinetic molecular theory (KMT)** explains *why* gases behave this way by modeling them at the molecular level. The theory rests on a set of assumptions: gas particles are in constant, random, straight-line motion; they are so small relative to the distances between them that their individual volumes are negligible; they exert no attractive or repulsive forces on one another except during collisions; and those collisions are perfectly **elastic**, meaning no kinetic energy is lost — it is simply transferred between particles.

From these assumptions, pressure emerges naturally. When a gas molecule strikes a container wall, it exerts a tiny force on that wall. **Pressure** is the cumulative effect of billions of these molecular impacts per second on every square centimeter of surface. Now Boyle's law makes intuitive sense: if you halve the volume, the same number of molecules hits half the wall area, and they hit it twice as often because they have less distance to travel between bounces — so pressure doubles. Charles's law follows too: heating a gas increases the average speed of its molecules, so they strike the walls harder and more frequently, requiring a volume increase to keep pressure constant.

The deepest insight of KMT is the relationship between temperature and molecular motion. The **average kinetic energy** of gas molecules is directly proportional to absolute temperature: KE_avg = (3/2)kT, where k is Boltzmann's constant and T is temperature in Kelvin. This means temperature *is* molecular motion — it is not some separate property that happens to correlate with speed. At absolute zero (0 K), molecular motion would theoretically cease. This relationship also explains why lighter molecules move faster than heavier ones at the same temperature: since KE = ½mv², a smaller mass requires a higher velocity to have the same kinetic energy. Hydrogen molecules at room temperature zip around at roughly 1,900 m/s, while heavier oxygen molecules travel at about 480 m/s.

KMT also clarifies when the ideal gas law breaks down. The assumptions of negligible molecular volume and no intermolecular forces work well at high temperatures and low pressures, where molecules are far apart and moving fast. But at high pressures (molecules squeezed close together, so their volumes matter) or low temperatures (molecules moving slowly enough for attractive forces to pull them together), real gases deviate from ideal behavior. Recognizing these limits prepares you for more advanced models like the van der Waals equation that correct for these effects.
