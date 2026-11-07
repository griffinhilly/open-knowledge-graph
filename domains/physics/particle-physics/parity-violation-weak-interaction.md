---
id: parity-violation-weak-interaction
title: Parity Violation in the Weak Interaction
domain: physics
course: particle-physics
prerequisites:
- id: symmetries-conservation-laws-quantum
  type: hard
- id: beta-emission-weak-force
  type: hard
- id: spin-angular-momentum
  type: hard
- id: conservation-laws-particle-reactions
  type: soft
builds-toward:
- cp-violation
- electroweak-unification
tags:
- parity
- weak-interaction
- symmetry
- helicity
- wu-experiment
stage: advanced
status: validated
---

# Parity Violation in the Weak Interaction

## Core Idea
Parity is the operation of reflecting all spatial coordinates through the origin, which turns a process into its mirror image. Gravity, electromagnetism, and the strong interaction look the same in a mirror, but the weak interaction does not. In 1956 Tsung-Dao Lee and Chen-Ning Yang pointed out that parity conservation had never been tested in weak processes, and in 1957 Chien-Shiung Wu's cobalt-60 experiment showed that beta-decay electrons come out preferentially opposite to the nuclear spin. The weak interaction couples only to left-handed neutrinos and right-handed antineutrinos, so it violates parity as strongly as possible.

## How It's Best Learned
Start by sorting quantities into polar vectors, which flip under parity (position, momentum), and axial vectors, which do not (angular momentum, spin). Show that any observed correlation like ⟨J·p⟩ ≠ 0 is a sign of parity violation, because J·p changes sign in the mirror. Walk through the Wu experiment with a diagram of the experiment and its mirror image. Then connect to neutrino helicity and to the suppression of the decay π⁺ → e⁺ + νₑ.

## Common Misconceptions
- Parity violation means no mirror-image process can ever occur. (Only the weak interaction distinguishes left from right; the other forces are mirror-symmetric.)
- Spin reverses under a parity transformation, just like momentum. (Spin is an axial vector and is unchanged by parity, while momentum reverses; that difference is what makes J·p a test of parity.)
- Parity violation is a small correction to the weak interaction. (The violation is maximal; in the Standard Model only left-handed particles and right-handed antiparticles feel the charged weak force.)

## Questions

```yaml
- question: "In the Wu experiment with polarized cobalt-60 nuclei, what was observed?"
  type: multiple-choice
  options: ["Electrons were emitted equally in all directions", "Electrons were emitted preferentially opposite to the direction of the nuclear spin", "Electrons were emitted only along the nuclear spin", "No electrons were emitted at low temperature"]
  answer: 1
  explanation: "An asymmetry between the directions along and against the spin means the mirror-image experiment, in which that relation is reversed, would give a different result. Parity is not conserved."
- question: "Which quantity changes sign under a parity transformation and so can reveal parity violation if its average is nonzero?"
  type: multiple-choice
  options: ["The energy of a particle", "The spin of a particle", "The product of spin and momentum, σ·p", "The magnitude of momentum"]
  answer: 2
  explanation: "Momentum reverses under parity, while spin does not, so σ·p (helicity) changes sign. A nonzero average helicity cannot occur in a parity-symmetric world."
- question: "Under a parity transformation, the spin of a particle reverses direction."
  type: true-false
  answer: false
  explanation: "Spin, like orbital angular momentum r × p, is an axial vector. Both r and p reverse, so their cross product does not."
- question: "The pion decays to a muon and neutrino far more often than to an electron and neutrino, even though the electron channel releases more energy. Explain using helicity."
  type: short-answer
  answer: "The spin-0 pion must produce the charged lepton and neutrino with opposite momenta and opposite spins, which forces the charged antilepton into the 'wrong' helicity for the weak interaction. The amplitude for that helicity is proportional to the lepton's mass, so the very light positron is strongly suppressed."
  explanation: "The measured ratio of π⁺ → e⁺νₑ to π⁺ → μ⁺ν_μ is about 1.2 × 10⁻⁴, in agreement with this helicity suppression."
```

## Explainer
A parity transformation sends every position r to −r. Under it, momenta reverse, while angular momenta and spins, which are cross products of two reversing vectors, stay the same. For decades physicists assumed that the laws of nature were unchanged by this reflection, and the assumption holds for gravity, electromagnetism, and the strong force.

In the mid-1950s a puzzle arose. Two particles, called τ and θ, had the same mass and lifetime, yet one decayed into two pions and the other into three, final states of opposite parity. Either they were different particles that happened to match, or parity was not conserved in their decay. Lee and Yang reviewed the evidence in 1956 and found that parity conservation had been well tested in strong and electromagnetic processes but never in weak ones. They proposed experiments that could check it.

Chien-Shiung Wu led the first, working with physicists at the National Bureau of Standards. They cooled cobalt-60 to a small fraction of a kelvin and aligned the nuclear spins with a magnetic field. Cobalt-60 undergoes beta decay. If parity were conserved, electrons would be emitted equally along and against the spin direction, because the mirror image of the experiment reverses the electrons' momenta but not the spins. Instead, more electrons came out opposite to the spin. The results, published in early 1957 alongside a muon-decay experiment by Richard Garwin, Leon Lederman, and Marcel Weinrich, showed that the weak interaction distinguishes left from right. Lee and Yang received the Nobel Prize in Physics that same year.

The violation turned out to be maximal. In 1958 Maurice Goldhaber and colleagues measured the helicity of the neutrino and found it negative: neutrinos are left-handed. The charged weak interaction acts only on left-handed particles and right-handed antiparticles, a structure written into the V − A theory and later into the electroweak part of the Standard Model. One striking test is pion decay. The spin-0 pion decays far more often to a muon than to an electron, because helicity rules suppress the electron mode by a factor proportional to the square of the lepton mass.

The weak interaction also violates charge conjugation C, which swaps particles and antiparticles. For a few years the combination CP seemed exact, but in 1964 James Cronin and Val Fitch found a small CP violation in neutral kaon decays, the subject of the next stage in this story.
