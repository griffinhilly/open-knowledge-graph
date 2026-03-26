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
stage: formal-systems
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

## Questions

```yaml
- question: "CO₂ is a linear, centrosymmetric molecule. A chemist collects both its IR and Raman spectra and finds that certain vibrational modes appear in the IR spectrum but are completely absent in the Raman spectrum, while other modes appear in Raman but not IR. Which principle best explains this complementary exclusivity?"
  type: multiple-choice
  options:
    - "The harmonic oscillator selection rule Δv = ±1 applies differently to IR and Raman techniques"
    - "For molecules with a center of symmetry, the rule of mutual exclusion states that no vibrational mode can be simultaneously IR-active and Raman-active"
    - "CO₂ has no permanent dipole, so all of its transitions are forbidden in all spectroscopic techniques"
    - "The Raman selection rule requires ΔJ = 0, while IR requires ΔJ = ±1, producing the apparent exclusion"
  answer: 1
  explanation: "The rule of mutual exclusion applies specifically to molecules with a center of inversion symmetry. IR activity requires a change in dipole moment during the vibration; Raman activity requires a change in polarizability. For centrosymmetric molecules (like CO₂, N₂, or benzene), these two symmetry requirements are mutually exclusive — a vibration that changes the dipole must break the inversion symmetry, while a vibration that preserves inversion symmetry can change polarizability but not dipole. This complementarity is a direct consequence of group theory and is one of the most useful diagnostic tools for determining molecular symmetry from spectroscopic data."

- question: "A spectroscopist observes a weak but clearly measurable absorption in a UV-Vis spectrum at a wavelength that electronic selection rules predict should be 'forbidden.' Which explanation is most physically accurate?"
  type: multiple-choice
  options:
    - "The selection rules were incorrectly derived and do not apply to molecules with more than two atoms"
    - "The transition occurs via a weaker mechanism — such as magnetic dipole coupling, electric quadrupole interaction, or vibronic coupling — that is not zero even when the electric dipole transition moment vanishes"
    - "The observation must be an experimental artifact; by definition, forbidden transitions cannot produce observable absorptions"
    - "The molecule must have undergone an irreversible chemical transformation that changed its electronic selection rules"
  answer: 1
  explanation: "'Forbidden' in spectroscopy means the electric dipole transition moment integral is zero — not that the transition is absolutely impossible. Weaker coupling mechanisms (magnetic dipole, electric quadrupole) can still mediate the transition, producing absorptions that are 100–10,000 times weaker than allowed transitions but measurable with modern instruments. Vibronic coupling — where molecular vibrations distort the symmetry and partially 'borrow' intensity from nearby allowed transitions — is especially important in electronic spectroscopy. The red color of rubies and phosphorescence in many organic compounds both arise from formally forbidden transitions."

- question: "A homonuclear diatomic molecule such as N₂ produces no absorption in the infrared region for its fundamental stretching vibration, because the vibration causes no change in the electric dipole moment."
  type: true-false
  answer: true
  explanation: "The electric dipole selection rule for IR activity requires that the vibration produce a changing dipole moment — the transition dipole integral ⟨ψ_f|μ̂|ψ_i⟩ must be nonzero. For homonuclear diatomics like N₂ or O₂, the molecule is perfectly symmetric: as the bond stretches and compresses, both atoms contribute equally to the electron distribution, and the dipole moment remains zero throughout. Because Δμ = 0 for the entire vibration, the IR selection rule is never satisfied, and no IR absorption occurs. This is why N₂ and O₂ — the main components of air — are transparent in the IR, while CO₂ and H₂O (with nonzero dipoles or asymmetric modes) are potent greenhouse gases."

- question: "The selection rule Δv = ±2 for the quantum harmonic oscillator is forbidden under the electric dipole mechanism, so first overtone absorptions are mostly absent from vibrational spectra."
  type: true-false
  answer: false
  explanation: "'Forbidden' does not mean 'absent' — it means the electric dipole transition moment for Δv = ±2 is zero under the idealized harmonic oscillator model. Real bonds are anharmonic: the potential energy is not a perfect parabola, and anharmonicity mixes wavefunctions of different v, making the Δv = ±2 transition moment nonzero (though small). Overtone bands (Δv = 2, 3, …) are routinely observed in IR spectra — they are 10–100 times weaker than the fundamental, but measurable. Near-infrared spectroscopy specifically exploits these overtone and combination bands for analytical purposes."

- question: "What physical quantity determines whether a spectroscopic transition is 'allowed' or 'forbidden,' and why can forbidden transitions still produce observable (if weak) spectral features?"
  type: short-answer
  answer: "The transition dipole moment integral ⟨ψ_f|μ̂|ψ_i⟩ determines allowedness: if this integral is nonzero, the electric dipole mechanism efficiently couples the radiation field to the transition and the absorption is 'allowed.' If the integral is zero (usually by symmetry), the electric dipole mechanism cannot operate and the transition is 'forbidden.' Forbidden transitions can still occur via weaker coupling mechanisms — magnetic dipole or electric quadrupole interactions, or vibronic coupling where molecular vibrations break the symmetry. These produce absorptions that are orders of magnitude weaker but not zero."
  explanation: "Understanding selection rules as threshold conditions (nonzero vs. zero integral) rather than absolute prohibitions is the key conceptual shift. The strength of an absorption depends on the square of the transition moment; electric dipole transitions are the strongest because the dipole moment operator couples most efficiently to electromagnetic radiation. When that mechanism is blocked by symmetry, weaker mechanisms take over, giving rise to the vast range of absorption intensities seen in real spectra."
```

## Explainer

From your work with the harmonic oscillator and rigid rotor models, you know that molecules have discrete energy levels for vibration and rotation. Spectroscopy probes transitions between these levels — but not all transitions are physically possible. **Selection rules** are the quantum mechanical constraints that determine which transitions can actually absorb or emit a photon.

The fundamental criterion is the **transition dipole moment integral**: ⟨ψ_f|μ̂|ψ_i⟩, where ψ_i and ψ_f are the initial and final state wavefunctions, and μ̂ is the dipole moment operator. If this integral evaluates to zero, the transition is "forbidden" — meaning the electromagnetic field cannot couple the two states efficiently. If it is nonzero, the transition is "allowed" and will produce an observable spectral line. You can often determine whether the integral vanishes without computing it explicitly by using symmetry arguments: the product of the symmetries of ψ_i, μ̂, and ψ_f must contain the totally symmetric representation for the integral to be nonzero.

For the quantum harmonic oscillator, evaluating this integral with the known wavefunctions (Hermite polynomials times Gaussians) yields the electric dipole selection rule **Δv = ±1** — only transitions between adjacent vibrational levels are allowed. This is why IR spectra are dominated by fundamental absorptions rather than overtones. For the rigid rotor, the selection rule is **ΔJ = ±1**, which produces the evenly spaced lines of a pure rotational (microwave) spectrum. Crucially, both of these rules also require the molecule to have a permanent or changing dipole moment: homonuclear diatomics like N₂ and O₂ have no permanent dipole and no dipole change during symmetric vibration, so they are invisible to IR and microwave spectroscopy.

This is where the distinction between spectroscopic techniques becomes important. **Raman spectroscopy** operates through a different mechanism — it depends on changes in polarizability rather than the dipole moment. The Raman selection rule for vibrations is Δv = ±1 (same as IR), but the symmetry requirement differs: vibrations that are IR-inactive can be Raman-active, and vice versa. For molecules with a center of symmetry, this complementarity is exact — the **rule of mutual exclusion** states that no vibration can be both IR-active and Raman-active. Electronic transitions add spin selection rules (ΔS = 0, meaning no change in spin multiplicity) and orbital symmetry rules (Laporte rule: parity must change in centrosymmetric molecules).

Finally, "forbidden" does not mean "impossible." Forbidden transitions are merely very weak — they violate electric dipole selection rules but can still occur through weaker mechanisms like **magnetic dipole** or **electric quadrupole** interactions, or through symmetry-breaking effects like vibronic coupling (where molecular vibrations distort the symmetry enough to partially allow an otherwise forbidden electronic transition). The characteristic red color of rubies and the phosphorescence of many materials both arise from formally forbidden transitions that are weakly allowed through these secondary mechanisms.
