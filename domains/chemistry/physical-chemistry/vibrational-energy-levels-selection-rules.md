---
id: vibrational-energy-levels-selection-rules
title: Vibrational Energy Levels and Selection Rules
domain: chemistry
course: physical-chemistry
prerequisites:
- id: harmonic-oscillator-molecular-vibrations
  type: hard
- id: vibrational-spectroscopy-theory
  type: hard
builds-toward:
- vibrational-frequency-force-constant
- infrared-spectroscopy-applications
tags:
- vibrational-spectroscopy
- selection-rules
- energy-levels
stage: advanced
status: draft
---

# Vibrational Energy Levels and Selection Rules

## Core Idea
Quantum vibrational states are quantized: E_v = ℏω(v + 1/2) where v = 0, 1, 2,... IR-active transitions require Δv = ±1 and a change in dipole moment along the vibration. Overtones (Δv = ±2, ±3,...) are typically forbidden or very weak. Hot bands from thermally populated excited states appear at lower frequency than fundamental transitions.

## How It's Best Learned
Measure IR spectrum of a diatomic or small polyatomic molecule; identify fundamental, overtone, and hot band transitions. Relate intensities to Franck-Condon factors and dipole moment derivatives.

## Questions

```yaml
- question: "A chemist records the IR spectrum of pure N₂ gas and observes no absorption in the fundamental stretching region. The most likely explanation is:"
  type: multiple-choice
  options:
    - "N₂ has no vibrational modes because the triple bond is too strong to vibrate"
    - "Stretching the N≡N bond does not change the molecular dipole moment, so the IR selection rule is violated"
    - "The N≡N stretching frequency falls outside the standard IR range"
    - "N₂ absorbs only in the microwave region due to its small moment of inertia"
  answer: 1
  explanation: "IR activity requires two conditions: Δv = ±1 AND a change in dipole moment during the vibration. N₂ is homonuclear — it has zero dipole moment by symmetry at any bond length. Stretching the bond doesn't change this, so the dipole-moment condition is never satisfied. N₂ does vibrate (it has zero-point energy and normal modes), but it cannot interact with infrared radiation regardless of frequency. This is why atmospheric N₂ doesn't absorb IR radiation despite being the dominant gas — it's IR-invisible."

- question: "For a harmonic oscillator, the energy spacing between vibrational levels v=1 and v=2 compared to the spacing between v=0 and v=1 is:"
  type: multiple-choice
  options:
    - "Larger, because higher vibrational states are more energetic"
    - "Smaller, because quantum numbers increase but the ladder slows"
    - "Identical — spacing is constant at ℏω regardless of quantum number"
    - "Temperature-dependent — spacing increases at higher temperatures"
  answer: 2
  explanation: "In the harmonic oscillator, E_v = ℏω(v + ½), so the spacing ΔE = ℏω is the same between every pair of adjacent levels. This uniform spacing is a defining property of the harmonic potential. Real molecules are anharmonic, which makes spacing decrease with increasing v — but the question specifies the harmonic oscillator model, where spacing is strictly constant. This constant spacing is also why the selection rule Δv = ±1 gives a single fundamental absorption: all allowed transitions occur at the same frequency ω."

- question: "A vibrational mode that obeys the Δv = ±1 selection rule will still not absorb infrared radiation if the vibration does not change the molecular dipole moment."
  type: true-false
  answer: true
  explanation: "True. IR absorption requires both conditions simultaneously: the quantum selection rule Δv = ±1 (from the transition dipole moment integral over wavefunctions) AND a nonzero dipole moment derivative with respect to the normal coordinate. The dipole condition is the physical requirement that the oscillating electric field of the photon can couple to an oscillating charge distribution in the molecule. A symmetric stretching mode in CO₂, for example, satisfies Δv = ±1 but is IR-inactive because it preserves the molecular symmetry and produces no net dipole change."

- question: "Hot bands in an IR spectrum appear at higher frequency than the fundamental transition because molecules in excited vibrational states vibrate faster."
  type: true-false
  answer: false
  explanation: "False. Hot bands appear at slightly lower frequency than the fundamental. They arise from transitions between thermally populated excited states (e.g., v=1 → v=2). In anharmonic potentials, the energy level spacing decreases with increasing v — the levels are closer together higher up. So the v=1→v=2 transition has a smaller ΔE than the v=0→v=1 fundamental, producing absorption at lower frequency. Their intensity increases with temperature as higher v states become more populated, making them a diagnostic for thermal vibrational excitation."

- question: "Explain why overtone transitions (Δv = ±2) appear in real molecular spectra even though they are forbidden for a harmonic oscillator."
  type: short-answer
  answer: "In a perfect harmonic oscillator the wavefunction integrals for Δv = ±2 vanish exactly, making overtones strictly forbidden. Real molecules have anharmonic potentials — the true potential energy curve deviates from a parabola. Anharmonicity mixes the pure harmonic wavefunctions, giving each vibrational state a small admixture of other quantum numbers. This mixing makes the transition dipole moment integral for Δv = ±2 (and ±3 etc.) small but nonzero, allowing weak overtone absorption at approximately twice the fundamental frequency."
  explanation: "The key point is that the harmonic oscillator selection rule is exact only for a perfectly parabolic potential. Any anharmonicity is a perturbation that relaxes the rule. Overtone intensities decrease rapidly with increasing Δv because the anharmonic mixing coefficients are small — the v=0→v=2 overtone is typically 10–100 times weaker than the fundamental, and v=0→v=3 weaker still."
```

## Explainer

From the harmonic oscillator model, you know that a vibrating diatomic molecule behaves approximately like a mass on a spring, with the potential energy rising parabolically as the bond stretches or compresses. Quantum mechanics tells us that such a system cannot vibrate with arbitrary energy — its energy is **quantized** into discrete levels given by E_v = ℏω(v + ½), where v is the vibrational quantum number (0, 1, 2, ...) and ω is the angular frequency determined by the bond's force constant and the reduced mass. The ½ in the formula means that even at v = 0, the molecule has **zero-point energy** — it never stops vibrating entirely, a direct consequence of the Heisenberg uncertainty principle.

The spacing between adjacent vibrational levels is uniform in the harmonic approximation: ΔE = ℏω regardless of which level you start from. This sets the stage for the **selection rule** Δv = ±1, which says that in a harmonic oscillator, only transitions between neighboring levels are allowed. The physical basis is that the transition dipole moment integral vanishes for Δv ≠ ±1 when the potential is exactly parabolic. The transition from v = 0 to v = 1 is the **fundamental**, and it dominates the IR spectrum.

But there is a second requirement: the vibration must cause a **change in dipole moment**. This is why homonuclear diatomics like N₂ and O₂ are IR-invisible — stretching the bond does not change the dipole moment (which is zero by symmetry at all bond lengths). Heteronuclear diatomics like HCl are IR-active because stretching the bond changes the charge separation. For polyatomic molecules, each normal mode is independently IR-active or inactive depending on whether that particular vibration modulates the molecular dipole.

Real molecules are not perfect harmonic oscillators. The true potential is **anharmonic** — it flattens out as the bond stretches toward dissociation and steepens at very short distances. Anharmonicity has two consequences: it makes the energy levels progressively closer together at higher v, and it relaxes the Δv = ±1 selection rule, allowing weak **overtone** transitions (Δv = ±2, ±3). Overtones appear in the spectrum at roughly twice, three times, etc., the fundamental frequency, but with rapidly decreasing intensity. **Hot bands** arise from transitions originating in thermally populated excited states (e.g., v = 1 → v = 2). Because anharmonicity compresses the spacing, hot bands appear at slightly lower frequency than the fundamental. Their intensity increases with temperature as more molecules occupy higher vibrational states, providing a direct spectroscopic thermometer for molecular vibration.
