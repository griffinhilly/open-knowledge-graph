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
status: validated
---

# Quantum Mechanical Selection Rules

## Core Idea
Selection rules determine which spectroscopic transitions are allowed or forbidden by quantum mechanics. A transition between states is allowed only if the transition dipole moment integral ⟨ψ_f|μ̂|ψ_i⟩ is nonzero; when this integral vanishes by symmetry or orthogonality, the transition is forbidden. For the harmonic oscillator, the electric dipole selection rule is Δv = ±1; for the rigid rotor, ΔJ = ±1 (with permanent dipole required). Electronic transitions obey spin selection rules (ΔS = 0) and orbital symmetry rules. Forbidden transitions can still occur weakly via magnetic dipole, quadrupole, or vibronic coupling mechanisms.

## How It's Best Learned
Evaluate the transition dipole integral explicitly for the lowest QHO levels to see why Δv = ±2 vanishes. Then use group theory (symmetry arguments) to evaluate integrals by inspection for polyatomic molecules.

## Common Misconceptions
- Treating 'forbidden' as 'impossible' — forbidden transitions are merely very weak, not absent.
- Thinking selection rules are universal; each type of spectroscopy (IR, Raman, microwave, UV-Vis) has its own set of rules.

## Explainer

From your work with the harmonic oscillator and rigid rotor models, you know that molecules have discrete energy levels for vibration and rotation. Spectroscopy probes transitions between these levels — but not all transitions are physically possible. **Selection rules** are the quantum mechanical constraints that determine which transitions can actually absorb or emit a photon.

The fundamental criterion is the **transition dipole moment integral**: ⟨ψ_f|μ̂|ψ_i⟩, where ψ_i and ψ_f are the initial and final state wavefunctions, and μ̂ is the dipole moment operator. If this integral evaluates to zero, the transition is "forbidden" — meaning the electromagnetic field cannot couple the two states efficiently. If it is nonzero, the transition is "allowed" and will produce an observable spectral line. You can often determine whether the integral vanishes without computing it explicitly by using symmetry arguments: the product of the symmetries of ψ_i, μ̂, and ψ_f must contain the totally symmetric representation for the integral to be nonzero.

For the quantum harmonic oscillator, evaluating this integral with the known wavefunctions (Hermite polynomials times Gaussians) yields the electric dipole selection rule **Δv = ±1** — only transitions between adjacent vibrational levels are allowed. This is why IR spectra are dominated by fundamental absorptions rather than overtones. For the rigid rotor, the selection rule is **ΔJ = ±1**, which produces the evenly spaced lines of a pure rotational (microwave) spectrum. Crucially, both of these rules also require the molecule to have a permanent or changing dipole moment: homonuclear diatomics like N₂ and O₂ have no permanent dipole and no dipole change during symmetric vibration, so they are invisible to IR and microwave spectroscopy.

This is where the distinction between spectroscopic techniques becomes important. **Raman spectroscopy** operates through a different mechanism — it depends on changes in polarizability rather than the dipole moment. The Raman selection rule for vibrations is Δv = ±1 (same as IR), but the symmetry requirement differs: vibrations that are IR-inactive can be Raman-active, and vice versa. For molecules with a center of symmetry, this complementarity is exact — the **rule of mutual exclusion** states that no vibration can be both IR-active and Raman-active. Electronic transitions add spin selection rules (ΔS = 0, meaning no change in spin multiplicity) and orbital symmetry rules (Laporte rule: parity must change in centrosymmetric molecules).

Finally, "forbidden" does not mean "impossible." Forbidden transitions are merely very weak — they violate electric dipole selection rules but can still occur through weaker mechanisms like **magnetic dipole** or **electric quadrupole** interactions, or through symmetry-breaking effects like vibronic coupling (where molecular vibrations distort the symmetry enough to partially allow an otherwise forbidden electronic transition). The characteristic red color of rubies and the phosphorescence of many materials both arise from formally forbidden transitions that are weakly allowed through these secondary mechanisms.
