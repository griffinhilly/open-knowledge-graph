---
id: selection-rules-spectroscopy
title: Quantum Mechanical Selection Rules
domain: chemistry
course: physical-chemistry
prerequisites:
- id: harmonic-oscillator-molecular-vibrations
  type: hard
- id: rigid-rotor-model
  type: hard
- id: hydrogen-atom-wavefunctions
  type: soft
builds-toward:
- rotational-spectroscopy
- vibrational-spectroscopy-theory
- electronic-spectroscopy-theory
- raman-spectroscopy-theory
tags:
- selection-rules
- transition-dipole
- spectroscopy
- forbidden
- allowed
stage: advanced
status: draft
---

# Quantum Mechanical Selection Rules

## Core Idea
Selection rules determine which spectroscopic transitions are allowed or forbidden by quantum mechanics. A transition between states is allowed only if the transition dipole moment integral ⟨ψ_f|μ̂|ψ_i⟩ is nonzero; when this integral vanishes by symmetry or orthogonality, the transition is forbidden. For the harmonic oscillator, the electric dipole selection rule is Δv = ±1; for the rigid rotor, ΔJ = ±1 (with permanent dipole required). Electronic transitions obey spin selection rules (ΔS = 0) and orbital symmetry rules. Forbidden transitions can still occur weakly via magnetic dipole, quadrupole, or vibronic coupling mechanisms.

## How It's Best Learned
Evaluate the transition dipole integral explicitly for the lowest QHO levels to see why Δv = ±2 vanishes. Then use group theory (symmetry arguments) to evaluate integrals by inspection for polyatomic molecules.

## Common Misconceptions
- Treating 'forbidden' as 'impossible' — forbidden transitions are merely very weak, not absent.
- Thinking selection rules are universal; each type of spectroscopy (IR, Raman, microwave, UV-Vis) has its own set of rules.
