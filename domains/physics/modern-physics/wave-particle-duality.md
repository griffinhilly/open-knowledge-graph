---
id: wave-particle-duality
title: Wave-Particle Duality
domain: physics
course: modern-physics
prerequisites:
- id: photon-model
  type: hard
- id: wave-properties-intro
  type: hard
- id: bohr-model
  type: soft
- id: compton-scattering
  type: soft
builds-toward:
- de-broglie-wavelength
- heisenberg-uncertainty-principle
- wavefunction-and-probability
tags:
- quantum
- duality
- complementarity
- double-slit
stage: advanced
status: validated
---
# Wave-Particle Duality

## Core Idea
Quantum objects exhibit both wave and particle properties depending on how they are observed — this is wave-particle duality. Photons interfere like waves in a double-slit experiment yet arrive at the detector as discrete clicks. Electrons show the same interference pattern when no attempt is made to determine which slit they passed through, but the interference vanishes when their path is measured. Bohr's complementarity principle states that wave and particle aspects are mutually exclusive experimental situations, not contradictory properties of a single object.

## How It's Best Learned
Build intuition by considering the double-slit experiment for photons, then electrons, then molecules. Focus on what changes when a 'which-path' detector is introduced and why the interference disappears.

## Common Misconceptions
- An electron literally splits and goes through both slits — the electron is a quantum system described by a wavefunction; it is not a split classical particle.
- Wave-particle duality is resolved by hidden variables — no local hidden variable theory can reproduce quantum predictions (Bell's theorem).
- Only subatomic particles show duality — interference has been demonstrated for molecules containing hundreds of atoms.

## Questions

```yaml
- question: "In a double-slit experiment, electrons are fired one at a time. After thousands of electrons have been detected, the pattern on the screen..."
  type: multiple-choice
  options: ["Shows two bright bands directly behind each slit, confirming particles traveled one path", "Shows an interference pattern with multiple bright and dark fringes", "Shows a single central bright band regardless of slit spacing", "Shows no pattern — each electron lands at a completely random location"]
  answer: 1
  explanation: "Even though each individual electron arrives as a localized click (particle behavior), the accumulated distribution over many electrons forms an interference pattern (wave behavior). This is only possible if each electron's wavefunction passes through both slits and interferes with itself. The pattern disappears if which-path detectors are added at the slits."

- question: "In the double-slit experiment, each electron literally splits into two halves — one half going through each slit — and then recombines at the detector."
  type: true-false
  answer: false
  explanation: "Electrons do not split. Each electron is detected as a single, whole, localized particle. What spreads through both slits is the electron's wavefunction — a probability amplitude, not a physical division of the electron's substance. The interference pattern reflects the wavefunction's behavior, but each detection event is one undivided electron."

- question: "If you place detectors at the slits to determine which slit each electron passes through, what happens to the interference pattern?"
  type: short-answer
  answer: "The interference pattern disappears, replaced by two plain bands corresponding to the two slits."
  explanation: "Measuring the electron's path collapses its wavefunction to a definite trajectory. Once the path is determined, the electron behaves like a classical particle passing through one slit, and there is nothing to interfere. This is Bohr's complementarity principle: wave behavior (interference) and particle behavior (definite path) are mutually exclusive — the experimental arrangement determines which aspect you observe."
```

## Explainer

By the early 20th century, two experimental results had shattered classical physics from opposite directions. The photoelectric effect (Einstein, 1905) showed that light — long established as a wave — delivers energy in discrete packets called photons, with each packet's energy proportional to frequency. Meanwhile, electron diffraction experiments showed that electrons — clearly particles with definite mass and charge — produce the same kind of interference fringes as X-ray waves passing through a crystal. The same kinds of entities were behaving as both waves and particles, depending on the experiment. This is wave-particle duality.

The double-slit experiment makes the paradox vivid. Fire electrons one at a time at a screen with two narrow slits: each electron produces a single localized click on the detector behind — unmistakably particle-like. Watch where those clicks accumulate over thousands of electrons, and an interference pattern builds up: alternating bright and dark bands that can only be explained if each electron's probability distribution was shaped by wave interference between paths through both slits. The electron does not split; its wavefunction — which encodes probabilities — spreads through both slits and interferes with itself. The detection event collapses that wavefunction to a point.

The deepest part of the story is what happens when you try to resolve the paradox by watching which slit each electron uses. Place a detector at the slits to record the path — and the interference pattern immediately vanishes, leaving only two plain bands. No disturbance to the electron is required; the mere fact of which-path information being available in the environment destroys the interference. Bohr called this complementarity: wave behavior and particle behavior are mutually exclusive aspects of the same system. The experimental arrangement determines which you observe. You cannot observe both simultaneously.

Wave-particle duality is sometimes misread as uncertainty about what the electron "really is." A more accurate framing is that quantum objects are neither classical waves nor classical particles — they are quantum systems described by wavefunctions. The wavefunction evolves according to a wave equation (which is why interference occurs) but yields definite, localized outcomes upon measurement (which is why detectors click at specific points). The apparent contradiction dissolves when you stop demanding that quantum objects conform to the categories of classical physics.

One important correction to the popular picture: duality is not limited to fundamental particles. Interference has been demonstrated for fullerene molecules (C₆₀, "buckyballs") and molecules containing hundreds of atoms. The reason we do not see interference for billiard balls or baseballs is not a sharp size boundary but a process called decoherence — rapid, unavoidable entanglement with the environment that destroys quantum coherence. Duality is universal in principle; decoherence is what hides it at everyday scales. Understanding duality is the prerequisite for the wavefunction interpretation, the uncertainty principle, and every subsequent concept in quantum mechanics.
