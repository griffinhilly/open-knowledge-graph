---
id: electron-diffraction-matter
title: Electron Diffraction and Matter Wave Interference
domain: physics
course: modern-physics
prerequisites:
- id: matter-wave-de-broglie-momentum
  type: hard
- id: davisson-germer-crystal-diffraction
  type: hard
builds-toward:
- wavefunction-probability-density
tags:
- quantum
- diffraction
- matter-waves
stage: advanced
status: draft
---

# Electron Diffraction and Matter Wave Interference

## Core Idea
Electrons diffract through crystal lattices or slits, producing interference patterns identical to those of light, with spacing inversely proportional to electron momentum. Double-slit experiments with electrons demonstrate that individual electrons do not take definite paths but exist in superposition. This confirms that matter possesses genuine wave properties that affect its propagation.

## Questions

```yaml
- question: "Electrons are fired through a double slit one at a time, with a gap between electrons so large that only one electron is in the apparatus at any moment. After many electrons, an interference pattern builds up on the detector. What is the correct interpretation?"
  type: multiple-choice
  options:
    - "The electrons interact with each other in the detector over time, collectively building the pattern"
    - "Each individual electron interferes with itself — it exists in superposition of passing through both slits, and the two amplitudes interfere before the electron is detected"
    - "The electrons are traveling in packets, each packet passing through both slits like a water wave"
    - "The pattern is produced by the electric field of the electron gun, not by the electrons themselves"
  answer: 1
  explanation: "This is the crucial conceptual point. With only one electron in the apparatus at a time, there is no possible interaction between electrons during flight. Yet the interference pattern still builds up, identical to what you get with many simultaneous electrons. The interference must therefore be a property of each individual electron — it does not take a definite path through one slit but exists in quantum superposition of both paths simultaneously. The two superposed amplitudes interfere, producing peaks and troughs in the probability of landing at each location. Each electron lands at a single point (particle-like detection), but the probability distribution follows wave interference."

- question: "A physicist sets up a detector at the slits of a double-slit experiment to record which slit each electron passes through. What happens to the interference pattern?"
  type: multiple-choice
  options:
    - "The interference pattern becomes sharper because the electron's path is now precisely known"
    - "The interference pattern disappears — measuring which path the electron took collapses the superposition, forcing the electron to have taken a definite path"
    - "The interference pattern shifts to a different location on the detector but does not disappear"
    - "Nothing changes — the interference pattern is a property of the apparatus geometry, not the electron's quantum state"
  answer: 1
  explanation: "This is one of the most important results in quantum mechanics. The interference pattern exists because the electron is in superposition — it 'goes through both slits' simultaneously, and the two amplitudes interfere. When a which-path detector is placed at the slits, it becomes possible in principle to know which path was taken. This collapses the superposition: the electron is now definitely in one slit or the other, and there are no two amplitudes to interfere. The single-slit pattern (broad, no interference) replaces the two-slit interference pattern. The act of gaining which-path information, regardless of how it is obtained, destroys the interference."

- question: "When electrons are sent through a double slit one at a time, they still produce an interference pattern after many electrons accumulate, demonstrating that matter wave interference is a property of each individual electron."
  type: true-false
  answer: true
  explanation: "The single-electron double-slit experiment is one of the most direct demonstrations of quantum superposition. Each electron arrives as a point on the detector (particle-like behavior at detection), but its probability of landing at any given point follows wave interference (wave-like behavior during propagation). Since electrons are sent one at a time, the pattern cannot result from electrons interacting with each other. The interference is a single-particle quantum effect — each electron propagates as a superposition of wave amplitudes through both slits simultaneously."

- question: "Electron diffraction patterns arise from collective interactions among many electrons — similar to how water waves from two sources interfere — so they would not appear if electrons were sent one at a time."
  type: true-false
  answer: false
  explanation: "Single-electron experiments directly disprove this. The interference pattern appears even when electrons are sent so slowly that only one is in the apparatus at any time, ruling out any interaction between electrons. Unlike water waves (which are collective disturbances in a medium), electron matter waves describe the quantum state of an individual particle. The wave amplitude is not spread across many electrons — it describes the probability amplitude for a single electron. This is what makes quantum interference conceptually radical: it is interference without any medium, and without multiple sources."

- question: "Explain why placing a detector at the slits to determine which path an electron took destroys the interference pattern. What does this reveal about the nature of quantum superposition?"
  type: short-answer
  answer: "The interference pattern exists because the electron is in a superposition of two states: passing through slit 1 and passing through slit 2. These two amplitudes propagate to the detector screen and add coherently — at some points they reinforce (bright fringes), at others they cancel (dark fringes). Placing a which-path detector at the slits entangles the electron's state with the detector — the electron's path becomes correlated with the detector's reading, making the two paths distinguishable in principle. Once the paths are distinguishable, the superposition is effectively collapsed: the electron is forced into a definite state (slit 1 or slit 2), and there is no second amplitude to interfere with the first. This reveals that superposition is not just ignorance about which path was taken — it is a physical state in which both amplitudes are genuinely present and contributing. Knowledge of the path destroys the superposition, not because knowledge is metaphysically special, but because gaining that knowledge requires a physical interaction that collapses the quantum state."
  explanation: "This experiment is why physicists say measurement affects the system being measured in quantum mechanics. The which-path detector is not just passively observing — it is interacting with the electron in a way that establishes a definite path. The loss of interference is direct physical evidence that superposition is real and that collapse occurs when superposed states become distinguishable."
```

## Explainer

From de Broglie's hypothesis — your prerequisite — you know that any particle with momentum p has an associated wavelength λ = h/p. From the Davisson-Germer experiment, you know that electrons scattered from a nickel crystal produced an interference pattern whose angular positions matched Bragg diffraction calculated using this de Broglie wavelength. That experiment confirmed that the hypothesis is not merely a mathematical curiosity but a physical reality: electrons genuinely behave as waves when they encounter structures whose spacing is comparable to their wavelength.

What makes electron diffraction conceptually deeper than confirming a formula is what it says about the nature of the electron's path. In the classic **double-slit experiment** performed with electrons, a beam of electrons is directed at a barrier with two narrow slits. If you block one slit, you get a single broad diffraction pattern on the detector. If you open both slits, you do not get the sum of two single-slit patterns — you get an interference pattern with alternating bright and dark fringes, just as with light. This already suggests wave behavior. But the truly startling version is when electrons are sent one at a time, so slowly that only one electron is in the apparatus at any moment. Each electron lands at a single point on the detector, as a particle would. But as millions of electrons accumulate, they build up the same interference pattern. No individual electron "knew" about the other electrons; yet the statistical distribution of landing positions displays wave interference.

The inescapable conclusion is that the interference is a property of each individual electron, not a collective effect. Each electron does not take a definite path through one slit or the other — it exists in a **superposition** of going through both slits, and the two amplitudes interfere. If you place a detector at the slits to determine which path the electron took, the interference pattern disappears. The act of measurement collapses the superposition and forces a definite path, eliminating the interference. This is not a technical limitation but a fundamental feature of quantum mechanics.

The connection between wavelength and momentum is quantitative and testable. Electrons accelerated through a potential difference V acquire kinetic energy eV = p²/2m, giving momentum p = √(2meV) and wavelength λ = h/√(2meV). At 100 V, λ ≈ 0.12 nm — comparable to atomic spacings, which is why crystal diffraction works so well. At higher energies (shorter wavelengths), electron diffraction becomes a precision tool for determining crystal structure and atomic spacing in materials science, just as X-ray crystallography does — but electrons interact far more strongly with matter, making them ideal for surface studies. The wave nature of matter is not an abstraction; it is the operating principle behind electron microscopes, electron crystallography, and quantum interference devices.
