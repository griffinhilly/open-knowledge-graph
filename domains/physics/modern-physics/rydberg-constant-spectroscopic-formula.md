---
id: rydberg-constant-spectroscopic-formula
title: Rydberg Constant and Spectroscopic Line Formula
domain: physics
course: modern-physics
prerequisites:
- id: bohr-model
  type: hard
- id: hydrogen-atom-spectrum
  type: hard
tags:
- atomic-physics
- spectroscopy
- quantum-mechanics
stage: advanced
status: validated
---

# Rydberg Constant and Spectroscopic Line Formula

## Core Idea
The Rydberg formula 1/λ = R(1/n₁² − 1/n₂²) gives the wavelengths of spectral lines emitted by hydrogen as electrons transition between energy levels. The Rydberg constant R ≈ 1.097 × 10⁷ m⁻¹ can be derived from the Bohr model as R = me⁴/(4πε₀²ℏ²). Different series correspond to transitions ending at n₁ = 1 (Lyman), 2 (Balmer), 3 (Paschen), etc.

## How It's Best Learned
Derive the Rydberg formula from Bohr energy levels. Calculate visible spectral lines using the Balmer series (n₁=2). Measure or look up observed wavelengths and compare to predictions.

## Common Misconceptions
The Rydberg constant is the same for all hydrogen isotopes (it varies slightly due to the reduced mass effect). The formula applies to any hydrogen-like ion by replacing R with R×Z².

## Questions

```yaml
- question: "A hydrogen-like ion He⁺ (Z = 2) undergoes an electron transition from n = 3 to n = 2. Compared to the same transition in neutral hydrogen, what happens to the wavelength of the emitted photon?"
  type: multiple-choice
  options:
    - "The wavelength is identical — the transition n = 3 → 2 is fixed by quantum numbers, independent of the element"
    - "The wavelength is longer — helium is heavier and its electrons move more slowly"
    - "The wavelength is shorter — He⁺ has Z = 2, replacing R with R·Z² = 4R, giving a larger 1/λ and thus a smaller wavelength"
    - "The wavelength cannot be predicted by the Rydberg formula because He⁺ is not hydrogen"
  answer: 2
  explanation: "For hydrogen-like ions, the Rydberg formula becomes 1/λ = R·Z²(1/n₁² − 1/n₂²). With Z = 2, the effective Rydberg constant is four times larger. For the n = 3 → 2 transition: 1/λ = 4R(1/4 − 1/9) = 4R · 5/36 = 5R/9, compared to 1/λ = R · 5/36 for hydrogen. The photon from He⁺ has 4× the inverse wavelength and thus 1/4 the wavelength — much shorter than the corresponding hydrogen line. The intuition: Z = 2 binds the electron tighter, compressing all energy levels by Z², which increases all transition energies and shifts spectral lines to shorter wavelengths."

- question: "The Balmer series was discovered before the Lyman or Paschen series. Which explanation best accounts for this historical fact?"
  type: multiple-choice
  options:
    - "The Balmer series has more spectral lines than the other series, making it easier to detect statistically"
    - "The Balmer series corresponds to the highest-energy transitions and was thus most easily detected by early equipment"
    - "The Balmer series (n₁ = 2) falls in or near visible light, making it directly accessible to early spectroscopists using optical instruments and to astronomers observing starlight without infrared or ultraviolet detectors"
    - "Balmer personally measured all lines in his series; the others were theoretically predicted before being observed"
  answer: 2
  explanation: "The named spectral series correspond to different choices of the final level n₁. Lyman (n₁ = 1) emits in the ultraviolet, invisible to the naked eye and to early optical detectors. Paschen (n₁ = 3) and higher series emit in the infrared. The Balmer series (n₁ = 2) uniquely falls in visible and near-visible wavelengths, which is why it was the first discovered — it was literally the most visible. Astronomers could see Balmer lines in stellar spectra with prism spectroscopes, long before UV or IR detectors existed. The formula was found empirically for Balmer lines, and the Rydberg generalization came after."

- question: "The Rydberg constant R∞ has exactly the same value for all hydrogen isotopes (protium, deuterium, tritium), since it is a universal constant derived from fundamental physics."
  type: true-false
  answer: false
  explanation: "False. R∞ (with the ∞ subscript) is derived assuming infinite nuclear mass. Real isotopes have finite nuclear mass, requiring a reduced-mass correction: the actual Rydberg constant for a specific isotope is R = R∞ × μ/mₑ, where μ is the reduced mass of the electron-nucleus system. Since deuterium has a heavier nucleus than protium, its reduced mass is slightly larger, and its spectral lines are shifted to slightly shorter wavelengths. This isotope shift is small but measurable and was historically important: in 1932, Urey identified deuterium by detecting this predicted shift in hydrogen's spectral lines."

- question: "Within a given spectral series (fixed n₁), the spectral lines crowd closer together as n₂ increases, converging toward a series limit at a finite wavelength corresponding to ionization from that shell."
  type: true-false
  answer: true
  explanation: "True. The Rydberg formula gives 1/λ = R(1/n₁² − 1/n₂²). As n₂ increases, 1/n₂² → 0, so 1/λ approaches R/n₁² from below — a fixed value that corresponds to the ionization wavelength from shell n₁. The spacing between successive lines decreases: the gap between n₂ = 3 and n₂ = 4 is larger than the gap between n₂ = 100 and n₂ = 101. This convergence is directly visible in spectra: lines pile up toward a sharp ionization limit, beyond which lies the continuous spectrum corresponding to ionized electrons."

- question: "Explain how the Rydberg formula is derived from the Bohr model, and what physical process each spectral line corresponds to."
  type: short-answer
  answer: "In the Bohr model, electrons occupy discrete energy levels Eₙ = −13.6/n² eV. When an electron transitions from a higher level n₂ to a lower level n₁, it releases a photon whose energy equals the difference: ΔE = E_{n₁} − E_{n₂} = 13.6(1/n₁² − 1/n₂²) eV. Using E = hc/λ to convert energy to wavelength and substituting the Bohr energy formula, the result is 1/λ = R(1/n₁² − 1/n₂²), where the Rydberg constant R bundles together the electron mass, charge, Planck's constant, and permittivity of free space. Each spectral line corresponds to a specific downward transition between two energy levels. The named series (Lyman, Balmer, Paschen) group lines by their common final level n₁."
  explanation: "The formula is not empirical curve-fitting: it follows mathematically from the Bohr energy quantization condition. The fact that it agrees with observation to high precision was a major confirmation of the Bohr model, and later derivation from quantum mechanics confirmed it more rigorously."
```

## Explainer

The Rydberg formula is the crown jewel of early atomic spectroscopy — a compact equation that predicts every spectral line of hydrogen with extraordinary precision. To understand where it comes from, start with what you know from the Bohr model: electrons orbit the nucleus only at specific allowed radii, corresponding to discrete energy levels Eₙ = −13.6/n² eV. When an electron falls from a higher level n₂ to a lower level n₁, it releases a photon whose energy exactly equals the difference ΔE = E_{n₁} − E_{n₂}.

The photon's energy determines its wavelength through E = hc/λ, so you can relate the wavelength directly to the level indices. When you substitute the Bohr energy formula and simplify, the result is the Rydberg formula: 1/λ = R∞(1/n₁² − 1/n₂²), where the **Rydberg constant** R∞ ≈ 1.097 × 10⁷ m⁻¹ bundles together the fundamental constants — electron mass, electron charge, Planck's constant, and the permittivity of free space. The subscript ∞ means we assumed infinite nuclear mass; the small reduced-mass correction gives the isotope-specific value.

The named **spectral series** are just different choices of n₁. The **Lyman series** (n₁ = 1) emits in the ultraviolet — the electron is dropping all the way to the ground state. The **Balmer series** (n₁ = 2) falls in or near visible light, which is why it was discovered first: astronomers could see these lines in starlight. The **Paschen series** (n₁ = 3) and higher are infrared. For each series, n₂ runs from n₁ + 1 to infinity, producing a set of lines that crowd closer together as n₂ increases, converging toward the **series limit** at n₂ → ∞ — the ionization threshold from that shell.

For hydrogen-like ions — atoms stripped of all but one electron, like He⁺ or Li²⁺ — the formula generalizes by replacing R∞ with R∞Z², where Z is the nuclear charge. More nuclear charge pulls the electron tighter, raising all energies by Z², which compresses all wavelengths accordingly. This same scaling predicts X-ray emission lines from heavy elements, extending Rydberg's insight from visible spectroscopy to the entire electromagnetic spectrum of one-electron systems.
