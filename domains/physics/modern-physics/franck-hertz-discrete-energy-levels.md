---
id: franck-hertz-discrete-energy-levels
title: 'Franck-Hertz Experiment: Verification of Discrete Energy Levels'
domain: physics
course: modern-physics
prerequisites:
- id: bohr-model
  type: hard
- id: hydrogen-energy-levels
  type: hard
tags:
- atomic-physics
- energy-levels
- experimental-verification
stage: advanced
status: draft
---

# Franck-Hertz Experiment: Verification of Discrete Energy Levels

## Core Idea
In the Franck-Hertz experiment, electrons collide with atoms and can transfer energy. Below a threshold voltage, collisions are elastic. Once the collision energy exceeds the energy gap to the first excited state (~4.9 V for mercury), inelastic collisions occur: the electron loses energy in discrete quanta, and the atom is excited. This produces a sharp discontinuity in the current-voltage curve, directly confirming quantized energy levels.

## How It's Best Learned
Plot current vs. voltage data from a Franck-Hertz tube, identifying the characteristic dips where inelastic collisions dominate. Calculate the excitation energy from the voltage at the first dip. Observe the repetition of dips at multiples of the first excitation voltage.

## Common Misconceptions
Atoms can only absorb specific energies (the energy gaps between levels). Below-threshold collisions are elastic and don't excite the atom. The current drops where inelastic collisions dominate because fewer electrons have sufficient energy to reach the anode.

## Explainer

From the Bohr model and hydrogen energy levels, you have a theoretical framework: electrons occupy discrete shells with specific energies, and transitions between levels involve photons with precisely quantized energies matching the energy gaps. This framework was built from spectroscopic data — the observation that atoms emit and absorb light only at specific wavelengths. The **Franck-Hertz experiment** (1914) provided something more direct: a purely mechanical, electrical demonstration that atomic energy levels are discrete, with no reference to light at all.

The experimental setup is deceptively simple. Electrons are emitted from a heated cathode, accelerated through mercury vapor by a voltage V, and collected at an anode (with a small retarding voltage opposing final collection). As V increases from zero, you might expect current to rise monotonically — more voltage, more electron energy, more electrons reaching the detector. Instead, the current-voltage curve shows a series of sharp *dips* at regular intervals of about 4.9 V. This periodic structure is the direct signature of a discrete energy level.

The mechanism operates through two kinds of collisions. For most of their journey, electrons undergo **elastic collisions** with mercury atoms: the electron bounces without transferring meaningful energy (the mercury atom is ~500 times heavier, so the electron barely slows, just like a tennis ball bouncing off a bowling ball). Electrons accumulate kinetic energy as they're accelerated. But once an electron's kinetic energy reaches exactly 4.9 eV — the energy separation between mercury's ground state and its first excited state — it can undergo an **inelastic collision**: it transfers exactly 4.9 eV to the mercury atom, dropping to near-zero kinetic energy itself. This nearly stopped electron cannot overcome the retarding voltage and reach the anode — current drops sharply. At slightly higher accelerating voltage, electrons reach the excitation threshold earlier in their path, then have room to reaccelerate and arrive at the anode — current rises again. At 9.8 V, an electron can undergo two sequential inelastic collisions, losing 4.9 eV each time, and current dips again. The dips at 4.9 V, 9.8 V, 13.7 V... directly count 1, 2, 3 excitation events per electron.

The crucial insight is the *sharpness* of the threshold. An electron with 4.85 eV cannot excite mercury's first state (which requires 4.9 eV); the collision is elastic. An electron with 4.95 eV can transfer exactly 4.9 eV and loses the remainder as kinetic energy. Atoms cannot accept arbitrary fractions of the excitation energy — they require the exact quantum. This all-or-nothing behavior is direct experimental evidence that atomic energy levels are discrete, not continuous. The Franck-Hertz experiment was decisive precisely because it bypassed optics entirely: no spectral lines, no prisms, no photographic plates — just a simple electrical measurement that forced the same conclusion as the entire history of atomic spectroscopy.
