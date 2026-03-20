---
id: phase-transitions
title: Phase Transitions
domain: physics
course: thermodynamics
prerequisites:
- id: temperature-and-thermal-equilibrium
  type: hard
- id: heat-and-internal-energy
  type: hard
builds-toward:
- latent-heat
- phase-diagrams
tags:
- phase-transition
- melting
- boiling
- condensation
- freezing
- solid-liquid-gas
stage: formal-systems
status: validated
---

# Phase Transitions

## Core Idea
A phase transition is a change in the physical state of matter (solid, liquid, gas, plasma) driven by changes in temperature or pressure. During a phase transition at constant pressure, temperature remains constant even as heat is added or removed — the energy goes into breaking or forming intermolecular bonds rather than changing kinetic energy. The transitions include melting/freezing (solid↔liquid), vaporization/condensation (liquid↔gas), and sublimation/deposition (solid↔gas).

## How It's Best Learned
Plot temperature versus time as ice is continuously heated through melting and boiling — the flat regions at 0°C and 100°C (for water at 1 atm) show that temperature is constant during transitions. Relate each plateau to latent heat.

## Common Misconceptions
- During boiling, adding more heat does not raise the temperature above 100°C (at 1 atm) until all the liquid is converted to vapor — the energy all goes into the phase change.
- Evaporation and boiling are different: evaporation occurs at any temperature from the surface; boiling occurs throughout the bulk at the boiling point.

## Questions

```yaml
- question: "A pot of water is boiling vigorously at 100°C. You turn up the burner to maximum. What happens to the water temperature?"
  type: multiple-choice
  options: ["It rises above 100°C immediately", "It stays at 100°C until all the water has evaporated", "It fluctuates between 95°C and 105°C", "It drops slightly due to increased evaporation cooling"]
  answer: 1
  explanation: "At 1 atm, water's boiling point is 100°C. During boiling, all added heat goes into the latent heat of vaporization — breaking the intermolecular bonds in the liquid — rather than raising the temperature. The water cannot rise above 100°C until the last drop of liquid has converted to steam. Turning up the burner only makes water boil faster, not hotter."

- question: "Evaporation and boiling are essentially the same process and occur under the same conditions."
  type: true-false
  answer: false
  explanation: "Evaporation occurs at any temperature from the liquid's surface, driven by the fastest-moving surface molecules escaping into the vapor phase. Boiling requires reaching the boiling point and occurs throughout the bulk liquid, forming bubbles that rise to the surface. A wet shirt dries by evaporation at room temperature — that is not boiling."

- question: "During melting, a solid absorbs heat but its temperature does not rise. Where does that energy go?"
  type: short-answer
  answer: "The energy goes into breaking the intermolecular bonds that hold molecules in the rigid lattice structure of the solid, converting it to the less-ordered liquid phase — not into increasing molecular kinetic energy."
  explanation: "Temperature is a measure of average kinetic energy. During a phase transition, the added heat (called latent heat) disrupts the ordered structure rather than speeding molecules up. Once the transition is complete, further heating resumes raising the temperature. This is why the temperature-vs-time graph is flat during melting and boiling."
```

## Explainer

You already know that heat is energy transferred due to a temperature difference, and that temperature measures the average kinetic energy of molecules. Phase transitions are the striking exception to the rule that "heating = temperature increase." When a substance changes phase — ice melting, water boiling — you can keep adding heat steadily and the temperature stays flat. This is one of the most counterintuitive results in introductory thermodynamics, and understanding *why* it happens is the core lesson of this topic.

The answer lies in what holds matter in each phase. In a solid, molecules are locked in a lattice by intermolecular bonds, vibrating in place. In a liquid, those bonds are weaker and molecules can flow past each other. In a gas, the molecules are essentially free. Moving from solid → liquid → gas requires *breaking* those bonds, which costs energy. When you heat ice to its melting point, the added energy goes entirely into disrupting the crystal lattice — not into making the molecules move faster. Since temperature measures kinetic energy (not bond energy), the temperature does not rise until all the solid is melted. This stored energy is called latent heat.

A useful mental model is the temperature-vs-time graph for water heated continuously from ice at -20°C to steam above 100°C. You see two flat regions: one at 0°C (melting) and one at 100°C (boiling). The slope of the rising regions tells you the heat capacity — how fast the temperature climbs per joule added. The flat regions tell you the latent heats. Water has unusually high latent heats compared to most substances, which is why steam burns are more severe than hot-water burns at the same temperature (steam releases extra energy as it condenses on your skin).

Evaporation is different from boiling and is a common source of confusion. Boiling happens throughout the bulk liquid once the boiling point is reached: bubbles of vapor form inside the liquid and rise to the surface. Evaporation happens only at the liquid's surface, at any temperature, because a few high-energy molecules always have enough energy to escape into the vapor phase even at room temperature. This is why puddles dry on a cool day and why sweat cools you — it is evaporation, not boiling. The boiling-vs-evaporation distinction will become important when you study vapor pressure and phase diagrams.
