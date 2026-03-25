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
- id: stopping-potential-kinetic-energy
  type: soft
tags:
- atomic-physics
- energy-levels
- experimental-verification
stage: advanced
status: validated
---
# Franck-Hertz Experiment: Verification of Discrete Energy Levels

## Core Idea
In the Franck-Hertz experiment, electrons collide with atoms and can transfer energy. Below a threshold voltage, collisions are elastic. Once the collision energy exceeds the energy gap to the first excited state (~4.9 V for mercury), inelastic collisions occur: the electron loses energy in discrete quanta, and the atom is excited. This produces a sharp discontinuity in the current-voltage curve, directly confirming quantized energy levels.

## How It's Best Learned
Plot current vs. voltage data from a Franck-Hertz tube, identifying the characteristic dips where inelastic collisions dominate. Calculate the excitation energy from the voltage at the first dip. Observe the repetition of dips at multiples of the first excitation voltage.

## Common Misconceptions
Atoms can only absorb specific energies (the energy gaps between levels). Below-threshold collisions are elastic and don't excite the atom. The current drops where inelastic collisions dominate because fewer electrons have sufficient energy to reach the anode.

## Questions

```yaml
- question: "In the Franck-Hertz experiment with mercury vapor, why does the measured current drop sharply near 4.9 V and then rise again before dropping again near 9.8 V?"
  type: multiple-choice
  options:
    - "At 4.9 V, electrons reach a resonant frequency that causes interference, temporarily reducing current"
    - "At 4.9 V, electrons gain enough energy to excite mercury's first energy level; they lose that energy inelastically and arrive at the anode with too little energy to overcome the retarding voltage"
    - "At 4.9 V, the electric field is too strong and deflects electrons sideways before they reach the detector"
    - "Mercury atoms absorb electrons completely at 4.9 V, reducing the number of free electrons until the voltage increases"
  answer: 1
  explanation: "Below 4.9 eV, electron-mercury collisions are elastic — the electron bounces with negligible energy loss (mercury is ~500× heavier). At 4.9 eV, inelastic collisions begin: an electron transfers exactly 4.9 eV to excite mercury from its ground state to its first excited level, dropping to near-zero kinetic energy. This near-stopped electron cannot overcome the small retarding voltage and is not collected — current falls. At slightly higher voltage, the inelastic collision happens earlier in the electron's path, leaving time to reaccelerate; current rises. At 9.8 V, electrons can lose 4.9 eV twice — current dips again. The pattern repeats at every multiple of 4.9 V."

- question: "An electron enters the mercury vapor with 5.5 eV of kinetic energy and collides inelastically with a mercury atom whose first excited state is 4.9 eV above ground. What is the electron's kinetic energy immediately after the collision?"
  type: multiple-choice
  options:
    - "0 eV — the atom absorbs all available kinetic energy"
    - "0.6 eV — the atom takes exactly 4.9 eV; the electron keeps the remainder"
    - "5.5 eV — the collision is elastic because 5.5 eV exceeds the threshold"
    - "4.9 eV — the electron transfers only a fraction of its energy matching the energy gap"
  answer: 1
  explanation: "In an inelastic collision, the atom absorbs exactly the energy it needs to transition to an excited state — no more, no less. The mercury atom takes 4.9 eV (the energy gap to the first excited state), and the electron retains the excess: 5.5 − 4.9 = 0.6 eV. The atom cannot accept an arbitrary amount; it requires precisely 4.9 eV. An electron with 4.85 eV cannot excite the atom at all (collision is elastic); one with 5.5 eV can, transferring exactly 4.9 eV. This quantized all-or-nothing behavior is the direct experimental signature of discrete energy levels."

- question: "In the Franck-Hertz experiment, a mercury atom can absorb any fraction of an electron's kinetic energy as long as the total energy transferred is less than the ionization energy."
  type: true-false
  answer: false
  explanation: "This is the key misconception the experiment refutes. Atoms do not absorb arbitrary amounts of energy — they can only accept energies corresponding to specific transitions between their discrete energy levels. Below the threshold for the first excited state (4.9 eV for mercury), all collisions are elastic regardless of the electron's energy. The atom is not a continuous energy absorber; it is a quantum system with fixed allowed states. The sharpness of the current drop at 4.9 V is direct evidence that the energy transfer is quantized, not continuous."

- question: "The current in a Franck-Hertz tube dips at regular voltage intervals (4.9 V, 9.8 V, 13.7 V...) because each successive dip corresponds to electrons undergoing one additional inelastic collision on their path to the anode."
  type: true-false
  answer: true
  explanation: "At 4.9 V, electrons accumulate enough energy over their entire accelerating path to undergo one inelastic collision, ending up near-stopped. At 9.8 V, electrons can undergo one collision, reaccelerate, undergo a second collision (losing another 4.9 eV), and again arrive at the anode with insufficient energy. At 13.7 V, three sequential inelastic collisions are possible. Each dip marks a voltage at which a whole additional excitation event fits into the electron's path. The integer multiples directly count the number of excitation events — a macroscopic electrical observation that tracks discrete quantum events one by one."

- question: "Why was the Franck-Hertz experiment considered particularly decisive evidence for quantized atomic energy levels, beyond what spectroscopy had already shown?"
  type: short-answer
  answer: "Spectroscopy had already established that atoms emit and absorb light at discrete wavelengths, but this could theoretically be explained by classical resonance phenomena in some models. The Franck-Hertz experiment confirmed discrete energy levels through a completely different, purely mechanical and electrical method: no light, no prisms, no spectral lines — just a voltage source and a current meter. When the same energy gaps appeared in electron-collision data as in optical spectra, it became very difficult to maintain that the discreteness was an artifact of how atoms interact with light. The experiment showed that atoms can only gain or lose energy in fixed quanta regardless of the mechanism of energy transfer, making discrete energy levels a feature of atomic structure itself, not just of optical transitions."
  explanation: "This independence from optics was the experiment's key contribution. Franck and Hertz received the 1925 Nobel Prize specifically because their work provided direct, non-spectroscopic confirmation that energy quantization was intrinsic to atoms — not a property of light-matter interaction alone. The purely electrical measurement cut off a classical escape route and forced the quantum interpretation."
```

## Explainer

From the Bohr model and hydrogen energy levels, you have a theoretical framework: electrons occupy discrete shells with specific energies, and transitions between levels involve photons with precisely quantized energies matching the energy gaps. This framework was built from spectroscopic data — the observation that atoms emit and absorb light only at specific wavelengths. The **Franck-Hertz experiment** (1914) provided something more direct: a purely mechanical, electrical demonstration that atomic energy levels are discrete, with no reference to light at all.

The experimental setup is deceptively simple. Electrons are emitted from a heated cathode, accelerated through mercury vapor by a voltage V, and collected at an anode (with a small retarding voltage opposing final collection). As V increases from zero, you might expect current to rise monotonically — more voltage, more electron energy, more electrons reaching the detector. Instead, the current-voltage curve shows a series of sharp *dips* at regular intervals of about 4.9 V. This periodic structure is the direct signature of a discrete energy level.

The mechanism operates through two kinds of collisions. For most of their journey, electrons undergo **elastic collisions** with mercury atoms: the electron bounces without transferring meaningful energy (the mercury atom is ~500 times heavier, so the electron barely slows, just like a tennis ball bouncing off a bowling ball). Electrons accumulate kinetic energy as they're accelerated. But once an electron's kinetic energy reaches exactly 4.9 eV — the energy separation between mercury's ground state and its first excited state — it can undergo an **inelastic collision**: it transfers exactly 4.9 eV to the mercury atom, dropping to near-zero kinetic energy itself. This nearly stopped electron cannot overcome the retarding voltage and reach the anode — current drops sharply. At slightly higher accelerating voltage, electrons reach the excitation threshold earlier in their path, then have room to reaccelerate and arrive at the anode — current rises again. At 9.8 V, an electron can undergo two sequential inelastic collisions, losing 4.9 eV each time, and current dips again. The dips at 4.9 V, 9.8 V, 13.7 V... directly count 1, 2, 3 excitation events per electron.

The crucial insight is the *sharpness* of the threshold. An electron with 4.85 eV cannot excite mercury's first state (which requires 4.9 eV); the collision is elastic. An electron with 4.95 eV can transfer exactly 4.9 eV and loses the remainder as kinetic energy. Atoms cannot accept arbitrary fractions of the excitation energy — they require the exact quantum. This all-or-nothing behavior is direct experimental evidence that atomic energy levels are discrete, not continuous. The Franck-Hertz experiment was decisive precisely because it bypassed optics entirely: no spectral lines, no prisms, no photographic plates — just a simple electrical measurement that forced the same conclusion as the entire history of atomic spectroscopy.
