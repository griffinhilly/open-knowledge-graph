---
id: hamilton-jacobi-theory
title: Hamilton-Jacobi Theory and Action-Angle Variables
domain: physics
course: classical-mechanics
prerequisites:
- id: canonical-transformations
  type: hard
- id: hamiltonian-mechanics-intro
  type: hard
- id: hamilton-jacobi-equations
  type: soft
- id: simple-harmonic-motion
  type: soft
builds-toward:
- kam-theorem
- hamiltonian-chaos
- wkb-quantization-rule
tags:
- hamiltonian
- action
- action-angle-variables
- adiabatic-invariants
stage: advanced
status: validated
---

# Hamilton-Jacobi Theory and Action-Angle Variables

## Core Idea
Hamilton-Jacobi theory looks for a canonical transformation that makes the new Hamiltonian zero, so that all new variables are constant. The generating function S(q, t) that does this obeys the Hamilton-Jacobi equation H(q, ∂S/∂q, t) + ∂S/∂t = 0, and along the true path S equals the action ∫L dt. For bounded periodic motion, the action variable J = ∮p dq and its conjugate angle give the frequency of the motion directly, as ν = ∂H/∂J. The action variable is also an adiabatic invariant and was the basis of the old quantum rule ∮p dq = nh.

## How It's Best Learned
Solve the free particle and the harmonic oscillator with the Hamilton-Jacobi equation first; separation of variables does all the work. Next compute J for the oscillator as the area of its phase-space ellipse and read off the frequency. Then discuss a pendulum whose string is slowly shortened, showing that E/ν stays constant while E changes. End by connecting S to the phase of a quantum wavefunction.

## Common Misconceptions
- The Hamilton-Jacobi equation is just a longer route to the same answers. (It gives frequencies without solving the motion, identifies adiabatic invariants, and links classical mechanics to wave optics and quantum mechanics.)
- The action variable J has units of energy. (J = ∮p dq has units of momentum times length, the same as energy times time and as Planck's constant.)
- Every mechanical system has action-angle variables. (They exist for integrable systems with bounded motion; chaotic systems do not have a global set of them.)

## Questions

```yaml
- question: "For a harmonic oscillator, the action variable is J = ∮p dq = 2πE/ω. What frequency ν does ∂H/∂J give?"
  type: multiple-choice
  options: ["ν = ω", "ν = ω/2π", "ν = 2πω", "ν = E/J"]
  answer: 1
  explanation: "Solving for the energy gives H = Jω/2π. Then ν = ∂H/∂J = ω/2π, the oscillation frequency in cycles per unit time."
- question: "Evaluated along the actual path of a system, Hamilton's principal function S changes at the rate dS/dt = L, so S equals the action integral of the Lagrangian."
  type: true-false
  answer: true
  explanation: "dS/dt = Σ(∂S/∂q)q̇ + ∂S/∂t = Σpq̇ − H = L along the true motion. Up to a constant, S is the action."
- question: "The string of a swinging pendulum is shortened very slowly. Which quantity stays approximately constant?"
  type: multiple-choice
  options: ["The energy E", "The frequency ν", "The ratio E/ν, which equals the action J", "The amplitude of the swing"]
  answer: 2
  explanation: "For slow changes the action variable is an adiabatic invariant. For small oscillations J = E/ν, so E rises in step with ν as the string shortens."
- question: "Apply the old quantum rule ∮p dq = nh to the harmonic oscillator. What energies does it give, and how do they differ from the quantum result?"
  type: short-answer
  answer: "E = nhν = nħω. The full quantum result is (n + ½)ħω, so the old rule misses the zero-point energy ½ħω."
  explanation: "Setting J = 2πE/ω equal to nh gives E = nhω/2π = nħω. The WKB method corrects this by adding a half-integer term from the turning points."
```

## Explainer
Canonical transformations let us trade one set of phase-space variables for another. Hamilton-Jacobi theory asks for the most extreme trade: choose a generating function S(q, P, t) so that the new Hamiltonian K is zero. Then every new coordinate and momentum is constant, and the motion follows from inverting the transformation. Using K = H + ∂S/∂t and p = ∂S/∂q, the condition K = 0 becomes the Hamilton-Jacobi equation,

H(q, ∂S/∂q, t) + ∂S/∂t = 0.

This is one first-order partial differential equation in place of 2n ordinary ones. For a free particle, H = p²/2m, try S = αq − (α²/2m)t. It satisfies the equation, and setting ∂S/∂α equal to a constant β gives q = β + (α/m)t, uniform motion as expected.

When H does not depend on time, write S = W(q) − Et. Then W obeys H(q, ∂W/∂q) = E. Systems that separate in some coordinate system, such as the Kepler problem in spherical coordinates, split into one ordinary equation per coordinate. This is how many classic problems are solved in full.

For bounded periodic motion, a special choice of new momentum is the action variable J = ∮p dq, the area enclosed by the orbit in phase space. Its conjugate coordinate w is called the angle variable. The Hamiltonian depends on J alone, so w increases at the steady rate ν = ∂H/∂J. For the oscillator, the phase-space orbit is an ellipse with semi-axes √(2mE) and √(2E/mω²). Its area is J = 2πE/ω, so H = Jω/2π and ν = ω/2π. The frequency appears without solving any equation of motion.

The action variable has two further uses. First, it is an adiabatic invariant. If a parameter such as the length of a pendulum changes slowly compared with one period, J stays nearly constant even though E and ν both change. Second, it shaped early quantum theory. Bohr and Sommerfeld postulated ∮p dq = nh, which reproduces the Bohr energy levels of hydrogen. A modern view comes from the WKB approximation, where a wavefunction behaves like exp(iS/ħ). In that picture S is the phase of a matter wave, and the Hamilton-Jacobi equation is the short-wavelength limit of the Schrödinger equation, just as ray optics is the short-wavelength limit of wave optics.
