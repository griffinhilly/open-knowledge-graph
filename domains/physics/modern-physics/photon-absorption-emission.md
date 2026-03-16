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
stage: advanced
status: draft
---

# Photon Absorption and Emission by Atoms

## Core Idea
An atom absorbs a photon if its energy matches the difference between two energy levels: hf = E_upper − E_lower. The electron is excited to the upper level; de-excitation emits an identical photon. For hydrogen, the Rydberg formula ν = R(1/n_lower² − 1/n_upper²) predicts all observed lines. Selection rules (Δℓ = ±1) govern which transitions are allowed, explaining why certain lines appear and others vanish.

## Explainer

From the Planck-Einstein relation, you know that photons carry energy E = hf proportional to their frequency. From hydrogen's energy levels, you know the allowed energies are E_n = −13.6 eV/n², a discrete ladder extending from n = 1 (ground state) upward to n = ∞ (ionization). These two pieces of knowledge combine in a single organizing principle: an atom and a photon interact only when the photon's energy *exactly* matches an energy gap between two atomic levels. The atom cannot absorb a photon with the wrong energy — energy conservation forbids it. This selectivity is why atoms produce **line spectra** rather than continuous absorption or emission across all frequencies.

**Absorption** excites the electron from a lower level to a higher one. Pass white light through a cool gas and the gas removes precisely those frequencies matching its level gaps; what you see is a continuous spectrum with dark absorption lines at those frequencies — the **Fraunhofer lines** in the solar spectrum are exactly this. **Emission** is the reverse: an excited electron drops to a lower level, releasing a photon whose energy equals the gap. Hot gas glows with bright emission lines at those same frequencies. The spectral lines of hydrogen are grouped into named series: the Lyman series (transitions to n = 1, in the UV), the Balmer series (transitions to n = 2, visible light), and the Paschen series (transitions to n = 3, infrared). The Rydberg formula ν = R_H(1/n_f² − 1/n_i²) predicts all lines, with R_H ≈ 3.29×10¹⁵ Hz.

Not all transitions are equally likely. **Selection rules** restrict which transitions are allowed with high probability. For electric dipole transitions (the dominant mechanism), the rule is Δℓ = ±1: the orbital quantum number must change by exactly ±1. This comes from conservation of angular momentum — the photon carries one unit of angular momentum (spin-1), so the atom must gain or lose one unit of orbital angular momentum. Transitions like 1s → 2s (Δℓ = 0) are "forbidden" by the electric dipole selection rule and occur only through much weaker mechanisms (two-photon emission, magnetic dipole) with much longer lifetimes. Allowed transitions have typical lifetimes of nanoseconds; forbidden transitions can have lifetimes of seconds or longer.

The quantitative exactness of atomic spectral lines has practical consequences everywhere. Atomic clocks keep time by counting oscillations of a microwave transition in cesium (Δf/f ~ 10⁻¹⁶). Astronomical spectroscopy identifies the composition, temperature, velocity (via Doppler shift), and redshift of distant stars from their emission and absorption spectra. Lasers exploit **stimulated emission** — an incoming photon of the right frequency stimulates an excited atom to emit an identical photon — to produce coherent, monochromatic light. All of these technologies rest on the same foundation: quantized energy levels and the photon energy matching condition you are learning here.
