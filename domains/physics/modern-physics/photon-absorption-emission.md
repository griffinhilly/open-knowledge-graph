---
id: photon-absorption-emission
title: Photon Absorption and Emission by Atoms
domain: physics
course: modern-physics
prerequisites:
- id: planck-einstein-relation
  type: hard
- id: hydrogen-quantum-energy-levels
  type: soft
builds-toward:
- line-spectra-discrete-frequencies
tags:
- atomic-physics
- spectroscopy
stage: formal-systems
status: validated
---

# Photon Absorption and Emission by Atoms

## Core Idea
An atom absorbs a photon if its energy matches the difference between two energy levels: hf = E_upper − E_lower. The electron is excited to the upper level; de-excitation emits an identical photon. For hydrogen, the Rydberg formula ν = R(1/n_lower² − 1/n_upper²) predicts all observed lines. Selection rules (Δℓ = ±1) govern which transitions are allowed, explaining why certain lines appear and others vanish.

## Questions

```yaml
- question: "A hydrogen atom in its ground state (n=1) is illuminated with photons of several different energies. Which photon will it absorb?"
  type: multiple-choice
  options:
    - "The photon with energy closest to any energy level, since partial absorption is possible"
    - "Only a photon whose energy exactly matches the gap between n=1 and an allowed upper level (e.g., 10.2 eV for the n=1→n=2 transition)"
    - "Any photon with energy greater than 13.6 eV, since that exceeds all bound-state energies"
    - "The highest-energy photon, since more energetic photons are more likely to interact with electrons"
  answer: 1
  explanation: "Energy conservation is exact — the photon's energy must precisely match an energy level gap (hf = E_upper − E_lower) for absorption to occur. There is no such thing as partial absorption of a photon. A photon with energy slightly above or below 10.2 eV will simply pass through without interacting. This selectivity is the direct cause of line spectra: atoms absorb and emit at specific discrete frequencies, not across a continuous range."

- question: "Which of the following hydrogen transitions is 'forbidden' by the electric dipole selection rule (Δℓ = ±1)?"
  type: multiple-choice
  options:
    - "1s → 2p  (Δℓ = +1)"
    - "2p → 1s  (Δℓ = −1)"
    - "1s → 2s  (Δℓ = 0)"
    - "3d → 2p  (Δℓ = −1)"
  answer: 2
  explanation: "The selection rule Δℓ = ±1 comes from conservation of angular momentum: a photon carries spin-1, so the atom must gain or lose one unit of orbital angular momentum. The 1s → 2s transition has Δℓ = 0, violating this rule. 'Forbidden' doesn't mean impossible — the transition can still occur through weaker mechanisms (two-photon emission, magnetic dipole) with lifetimes orders of magnitude longer than allowed transitions (~ns vs. seconds)."

- question: "The dark absorption lines in the solar spectrum and the bright emission lines in laboratory hydrogen spectra occur at exactly the same frequencies."
  type: true-false
  answer: true
  explanation: "Absorption and emission are reciprocal processes involving identical energy gaps. Cool solar gas absorbs photons from the background continuum at precisely the frequencies that match its energy level gaps, producing dark Fraunhofer lines. Hot gas in emission produces bright lines at those same frequencies as excited electrons de-excite. Same energy gaps — same frequencies. The solar spectrum's dark lines directly reveal the elemental composition of the solar atmosphere."

- question: "The Balmer series encompasses all observable spectral lines of hydrogen."
  type: true-false
  answer: false
  explanation: "The Balmer series covers only transitions to the n=2 level, which happen to fall in the visible range — which is why it was the first series discovered. Hydrogen has multiple series: Lyman (transitions to n=1, ultraviolet), Balmer (to n=2, visible), Paschen (to n=3, infrared), and others. The Rydberg formula ν = R_H(1/n_f² − 1/n_i²) predicts all series with the same formula, just different values of n_f."

- question: "Why do atoms produce line spectra — discrete frequencies — rather than continuously absorbing and emitting across all frequencies?"
  type: short-answer
  answer: "Because atomic energy levels are quantized — electrons can only occupy specific allowed energies. A photon is absorbed only if its energy exactly matches the gap between two energy levels (hf = E_upper − E_lower); photons with other energies don't interact with the atom. De-excitation emits photons at exactly those same gap frequencies. The result is a set of discrete bright or dark lines, each corresponding to a specific transition between specific energy levels."
  explanation: "This is the direct observational consequence of quantized energy levels. A classical electron orbiting continuously could absorb and emit any frequency — leading to continuous spectra and the spiral collapse of the electron into the nucleus (the ultraviolet catastrophe for atoms). Quantization resolves both: it explains discrete spectra and stable ground states. The exact photon-matching condition is both the constraint that produces line spectra and the tool that makes spectroscopy so powerful for identifying atomic composition."
```

## Explainer

From the Planck-Einstein relation, you know that photons carry energy E = hf proportional to their frequency. From hydrogen's energy levels, you know the allowed energies are E_n = −13.6 eV/n², a discrete ladder extending from n = 1 (ground state) upward to n = ∞ (ionization). These two pieces of knowledge combine in a single organizing principle: an atom and a photon interact only when the photon's energy *exactly* matches an energy gap between two atomic levels. The atom cannot absorb a photon with the wrong energy — energy conservation forbids it. This selectivity is why atoms produce **line spectra** rather than continuous absorption or emission across all frequencies.

**Absorption** excites the electron from a lower level to a higher one. Pass white light through a cool gas and the gas removes precisely those frequencies matching its level gaps; what you see is a continuous spectrum with dark absorption lines at those frequencies — the **Fraunhofer lines** in the solar spectrum are exactly this. **Emission** is the reverse: an excited electron drops to a lower level, releasing a photon whose energy equals the gap. Hot gas glows with bright emission lines at those same frequencies. The spectral lines of hydrogen are grouped into named series: the Lyman series (transitions to n = 1, in the UV), the Balmer series (transitions to n = 2, visible light), and the Paschen series (transitions to n = 3, infrared). The Rydberg formula ν = R_H(1/n_f² − 1/n_i²) predicts all lines, with R_H ≈ 3.29×10¹⁵ Hz.

Not all transitions are equally likely. **Selection rules** restrict which transitions are allowed with high probability. For electric dipole transitions (the dominant mechanism), the rule is Δℓ = ±1: the orbital quantum number must change by exactly ±1. This comes from conservation of angular momentum — the photon carries one unit of angular momentum (spin-1), so the atom must gain or lose one unit of orbital angular momentum. Transitions like 1s → 2s (Δℓ = 0) are "forbidden" by the electric dipole selection rule and occur only through much weaker mechanisms (two-photon emission, magnetic dipole) with much longer lifetimes. Allowed transitions have typical lifetimes of nanoseconds; forbidden transitions can have lifetimes of seconds or longer.

The quantitative exactness of atomic spectral lines has practical consequences everywhere. Atomic clocks keep time by counting oscillations of a microwave transition in cesium (Δf/f ~ 10⁻¹⁶). Astronomical spectroscopy identifies the composition, temperature, velocity (via Doppler shift), and redshift of distant stars from their emission and absorption spectra. Lasers exploit **stimulated emission** — an incoming photon of the right frequency stimulates an excited atom to emit an identical photon — to produce coherent, monochromatic light. All of these technologies rest on the same foundation: quantized energy levels and the photon energy matching condition you are learning here.
