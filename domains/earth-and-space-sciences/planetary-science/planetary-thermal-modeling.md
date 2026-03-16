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
stage: advanced
status: draft
---

# Parameterized Thermal Models of Planetary Interiors

## Core Idea
One-dimensional parameterized models of planetary thermal structure balance heat diffusion in the crust and mantle against radiogenic heating and surface cooling. These models predict planetary thermal evolution over billions of years, constraining crustal thickness, mantle temperature, core cooling rates, and the potential for volcanism and tectonics.

## Explainer

From your study of heat conduction and planetary interior dynamics, you know that planets are essentially cooling engines: they start hot (from accretional energy and radioactive decay) and lose heat to space through their surfaces. The question that **parameterized thermal models** answer is: how fast does a planet cool, and what does its internal temperature profile look like at any point in its history? These models reduce the full three-dimensional convection problem to a tractable one-dimensional description by using scaling relationships that relate heat flux to temperature difference across each layer.

The basic structure divides a terrestrial planet into concentric shells — an iron core, a convecting silicate mantle, and a rigid lithospheric lid. In each shell, the model tracks the energy balance: heat produced by radioactive decay of uranium, thorium, and potassium (which decreases exponentially over time as isotopes decay) minus heat transported outward. Your prerequisite knowledge of steady-state heat conduction gives you the conductive piece — heat flows through the rigid lithosphere according to Fourier's law, proportional to the temperature gradient and thermal conductivity. But the mantle is not rigid; it convects. The key parameterization relates the **Nusselt number** (ratio of total heat transport to purely conductive transport) to the **Rayleigh number** (which measures convective vigor) through a power law. This single relationship captures the essential physics: a hotter mantle convects more vigorously, transporting heat more efficiently, which acts as a negative feedback that regulates cooling.

Solving the coupled ordinary differential equations (one for mantle temperature, one for core temperature) forward in time reveals how a planet evolves thermally. Early in its history, radiogenic heating is intense and the mantle is hot, driving vigorous convection and active volcanism. As radioactive elements decay and the planet cools, convection slows, the lithosphere thickens, and volcanic activity wanes. The model predicts critical transitions: when does the core cool enough to begin solidifying an inner core (which can power a magnetic dynamo)? When does the lithosphere become so thick that plate tectonics stalls, transitioning the planet to a stagnant-lid regime? Mars, for example, is thought to have lost its plate tectonics early and shifted to a single-plate mode, which thermal models can reproduce by tracking mantle viscosity as it increases with cooling.

These models are powerful precisely because they are simple enough to explore parameter space — varying planet size, composition, initial temperature, and radioactive element abundance — while capturing the first-order thermal behavior. Comparing model predictions to observational constraints (surface heat flow measurements, lithospheric thickness estimates, volcanic history from crater counts) tests our understanding of planetary interiors. The thermal state controls nearly everything geologically important: whether a planet has active volcanism, a magnetic field, plate tectonics, or the geological recycling needed to maintain a habitable surface environment.
