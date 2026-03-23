---
id: planetary-thermal-modeling
title: Parameterized Thermal Models of Planetary Interiors
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: planetary-interior-dynamics
  type: hard
- id: heat-flow-conduction-steady-state
  type: hard
- id: heat-transfer-conduction
  type: soft
- id: partial-differential-equations-intro
  type: soft
builds-toward:
- crustal-heat-flow-and-geotherms
- thermal-evolution-terrestrial-planets
tags:
- thermal-structure
- heat-flow
- cooling
- interior-modeling
stage: expert
status: draft
---

# Parameterized Thermal Models of Planetary Interiors

## Core Idea
One-dimensional parameterized models of planetary thermal structure balance heat diffusion in the crust and mantle against radiogenic heating and surface cooling. These models predict planetary thermal evolution over billions of years, constraining crustal thickness, mantle temperature, core cooling rates, and the potential for volcanism and tectonics.

## Questions

```yaml
- question: "In a parameterized thermal model, a planet's mantle becomes hotter due to an initial abundance of radioactive elements. What happens to the cooling rate?"
  type: multiple-choice
  options:
    - "Cooling slows — hotter materials have higher thermal conductivity, retaining heat"
    - "Cooling accelerates — a hotter mantle drives more vigorous convection, increasing heat transport"
    - "Cooling rate is unchanged — it depends only on surface temperature, not interior temperature"
    - "The planet heats up further in a runaway feedback loop"
  answer: 1
  explanation: "The Nusselt-Rayleigh parameterization captures a key negative feedback: a hotter mantle has lower viscosity, which increases the Rayleigh number (convective vigor), which increases the Nusselt number (ratio of actual to conductive heat transport). More vigorous convection transports heat more efficiently to the surface, where it is radiated to space — cooling the mantle faster. This self-regulating feedback prevents runaway heating and governs the long-term thermal evolution. A planet with more radiogenic heating initially cools faster, not slower, because the thermal feedback is stronger."

- question: "Two planets are identical except that Planet A is larger. All else equal, which is more likely to retain active plate tectonics after 4 billion years?"
  type: multiple-choice
  options:
    - "Planet B (smaller) — less mass means faster cooling, maintaining vigorous convection"
    - "Planet A (larger) — more radioactive elements in a larger volume means more sustained heating"
    - "They cool at identical rates because surface-area-to-volume ratio doesn't affect thermal models"
    - "Planet B — smaller planets have thinner lithospheres that are easier to subduct"
  answer: 1
  explanation: "A larger planet has more radioactive elements (total inventory scales with volume), sustaining internal heating for longer. More critically, a larger planet has a lower surface-area-to-volume ratio, meaning heat escapes more slowly relative to the volume that must cool. Both effects keep the mantle hotter and convection more vigorous for longer, maintaining the conditions for plate tectonics. Mars (smaller than Earth) is thought to have lost plate tectonics early partly for this reason. Planet size is a primary predictor of thermal longevity."

- question: "In planetary thermal models, a hotter mantle loses heat more slowly because high-temperature materials conduct heat less efficiently."
  type: true-false
  answer: false
  explanation: "The opposite is true for the convective component, which dominates heat transport in planetary mantles. A hotter mantle has lower viscosity, which increases the Rayleigh number and drives more vigorous convection. The Nusselt number increases with Rayleigh number, meaning total heat transport (dominated by convection) increases with mantle temperature. The negative feedback between temperature and cooling rate is what stabilizes planetary thermal evolution. Conduction alone (which does not strongly depend on temperature) is only dominant in the rigid lithosphere."

- question: "Parameterized thermal models predict that as a planet cools over billions of years, its lithosphere tends to thicken."
  type: true-false
  answer: true
  explanation: "The lithosphere is the rigid outer shell where conduction dominates over convection. As the mantle cools, viscosity increases and the temperature at which material transitions from ductile (convecting) to rigid (conductive) deepens. This progressive thickening has major geological consequences: it suppresses volcanic activity, can shut down plate tectonics (transition to stagnant-lid regime), and reduces the likelihood of generating a magnetic dynamo. Mars is the archetypal example — its early lithosphere thickened rapidly, freezing the planet into a single-plate state."

- question: "Explain the negative feedback loop that regulates planetary cooling in parameterized thermal models, and why it matters for long-term thermal evolution."
  type: short-answer
  answer: "A hotter mantle has lower viscosity, increasing the Rayleigh number (ratio of convective to diffusive heat transport). A higher Rayleigh number increases the Nusselt number via the power-law parameterization, meaning the mantle convects more vigorously and transports heat to the surface more efficiently. Faster heat loss cools the mantle, raising viscosity and reducing the Rayleigh number — a classic negative feedback. This self-regulation prevents runaway heating and stabilizes the cooling trajectory, but it also means a planet cannot indefinitely maintain vigorous convection: as it cools, convection weakens, the lithosphere thickens, and geological activity fades."
  explanation: "This feedback loop is encoded in the coupled ODEs — one for mantle temperature, one for core temperature — that parameterized models solve forward in time. The power-law Nusselt-Rayleigh relationship is the key parameterization that replaces the full 3D convection calculation with a tractable 1D description. Its accuracy is validated by comparing model predictions (volcanism timing, lithospheric thickness, magnetic field lifetime) against observational constraints from crater counts and remote sensing."
```

## Explainer

From your study of heat conduction and planetary interior dynamics, you know that planets are essentially cooling engines: they start hot (from accretional energy and radioactive decay) and lose heat to space through their surfaces. The question that **parameterized thermal models** answer is: how fast does a planet cool, and what does its internal temperature profile look like at any point in its history? These models reduce the full three-dimensional convection problem to a tractable one-dimensional description by using scaling relationships that relate heat flux to temperature difference across each layer.

The basic structure divides a terrestrial planet into concentric shells — an iron core, a convecting silicate mantle, and a rigid lithospheric lid. In each shell, the model tracks the energy balance: heat produced by radioactive decay of uranium, thorium, and potassium (which decreases exponentially over time as isotopes decay) minus heat transported outward. Your prerequisite knowledge of steady-state heat conduction gives you the conductive piece — heat flows through the rigid lithosphere according to Fourier's law, proportional to the temperature gradient and thermal conductivity. But the mantle is not rigid; it convects. The key parameterization relates the **Nusselt number** (ratio of total heat transport to purely conductive transport) to the **Rayleigh number** (which measures convective vigor) through a power law. This single relationship captures the essential physics: a hotter mantle convects more vigorously, transporting heat more efficiently, which acts as a negative feedback that regulates cooling.

Solving the coupled ordinary differential equations (one for mantle temperature, one for core temperature) forward in time reveals how a planet evolves thermally. Early in its history, radiogenic heating is intense and the mantle is hot, driving vigorous convection and active volcanism. As radioactive elements decay and the planet cools, convection slows, the lithosphere thickens, and volcanic activity wanes. The model predicts critical transitions: when does the core cool enough to begin solidifying an inner core (which can power a magnetic dynamo)? When does the lithosphere become so thick that plate tectonics stalls, transitioning the planet to a stagnant-lid regime? Mars, for example, is thought to have lost its plate tectonics early and shifted to a single-plate mode, which thermal models can reproduce by tracking mantle viscosity as it increases with cooling.

These models are powerful precisely because they are simple enough to explore parameter space — varying planet size, composition, initial temperature, and radioactive element abundance — while capturing the first-order thermal behavior. Comparing model predictions to observational constraints (surface heat flow measurements, lithospheric thickness estimates, volcanic history from crater counts) tests our understanding of planetary interiors. The thermal state controls nearly everything geologically important: whether a planet has active volcanism, a magnetic field, plate tectonics, or the geological recycling needed to maintain a habitable surface environment.
