---
id: bohr-model
title: Bohr Model of the Hydrogen Atom
domain: physics
course: modern-physics
prerequisites:
- id: emission-absorption-spectra
  type: hard
- id: electric-potential
  type: hard
- id: circular-motion-dynamics
  type: hard
builds-toward:
- quantum-numbers
- wave-particle-duality
- nuclear-structure
tags:
- atomic
- hydrogen
- energy-levels
- quantization
- bohr
stage: advanced
status: validated
---

# Bohr Model of the Hydrogen Atom

## Core Idea
Bohr (1913) proposed that electrons orbit the nucleus only at certain quantized radii where the angular momentum is an integer multiple of ℏ: L = nℏ. Combining this quantization condition with the balance between Coulomb attraction and centripetal acceleration gives the allowed energy levels E_n = −13.6 eV / n². Photons are emitted or absorbed when electrons transition between levels, with hf = E_initial − E_final, reproducing the Rydberg formula exactly for hydrogen.

## How It's Best Learned
Derive the quantized radii and energies from the two conditions (circular orbit + angular momentum quantization). Verify that the energy differences reproduce Balmer series wavelengths numerically. Note what the model cannot explain (multi-electron atoms, line intensities, fine structure) to motivate quantum mechanics.

## Common Misconceptions
- The Bohr model is correct quantum mechanics — it is a semi-classical approximation that works for hydrogen by luck; it fails for helium and cannot predict transition probabilities.
- Electrons in the ground state are 'at rest' — n=1 is the lowest-energy orbit, not rest; the electron has quantized kinetic energy.
- The quantization of angular momentum was derived from first principles — Bohr postulated it; de Broglie later gave it a wave interpretation.

## Questions

```yaml
- question: "An electron in hydrogen transitions from n=3 (E = −1.51 eV) to n=1 (E = −13.6 eV). What is emitted and with what energy?"
  type: multiple-choice
  options: ["A photon absorbed with energy 12.09 eV", "A photon emitted with energy 12.09 eV", "A photon absorbed with energy 15.11 eV", "A photon emitted with energy 1.51 eV"]
  answer: 1
  explanation: "Transitioning from n=3 to n=1 is a downward transition (higher to lower energy), so the electron loses energy by emitting a photon. The photon energy equals the difference: −1.51 − (−13.6) = 12.09 eV. This ultraviolet photon belongs to the Lyman series. Absorption occurs only for upward transitions."

- question: "The Bohr model fails for helium because Bohr made an arithmetic error; the underlying physics is correct for all atoms."
  type: true-false
  answer: false
  explanation: "The Bohr model fails for helium because of a fundamental physical limitation, not an arithmetic one. It assumes a single electron experiencing only Coulomb attraction from the nucleus. With two electrons, electron-electron repulsion introduces interactions the model cannot handle. The model's semi-classical orbit picture also cannot predict transition probabilities or fine structure even for hydrogen."

- question: "What two physical conditions does Bohr combine to derive the allowed orbital radii in hydrogen?"
  type: short-answer
  answer: "Bohr combines (1) the balance between Coulomb attraction and centripetal force for a circular orbit, and (2) the postulate that angular momentum is quantized as L = nℏ. Solving these two equations simultaneously yields the discrete allowed radii r_n = n²a₀."
  explanation: "The circular orbit condition (Coulomb = centripetal) alone would allow any radius. The angular momentum quantization condition restricts radius and speed to a discrete set. Only by combining both conditions does Bohr obtain the quantized energy levels E_n = −13.6 eV/n². This two-condition approach is the core derivation strategy."
```

## Explainer

Before 1913, the hydrogen emission spectrum was an empirical puzzle. Experiment showed hydrogen emits light only at specific discrete wavelengths — a pattern summarized by the Rydberg formula — but no one knew why. Classical physics predicted catastrophe: an orbiting electron should radiate energy continuously (accelerating charges emit electromagnetic radiation) and spiral into the nucleus in about 10⁻¹¹ seconds. Atoms clearly did not behave this way, so something was fundamentally missing.

Bohr's solution was audacious: he simply postulated that electrons can only occupy circular orbits where the angular momentum equals an integer multiple of ℏ (L = nℏ). This is not derived from anything more fundamental — it is an assumption. He then combined this quantization rule with the ordinary classical condition that Coulomb attraction provides the centripetal force for a circular orbit. Solving these two equations together yields the allowed radii r_n = n²a₀ (where a₀ ≈ 0.053 nm is the Bohr radius) and the allowed energies E_n = −13.6 eV / n². The integer n, which you will later call the principal quantum number, labels each orbit.

The payoff is the emission rule: when an electron drops from energy level E_i to level E_f, the energy difference is carried away by a single photon with frequency f = (E_i − E_f)/h. Plugging in E_n = −13.6/n² reproduces the Rydberg formula exactly for every series of hydrogen lines — the Lyman series (UV, n→1), Balmer series (visible, n→2), and so on. Predicting these wavelengths from first principles was a triumph no classical model had achieved.

Despite this success, the Bohr model is a semi-classical hybrid that happens to give right answers for hydrogen by a kind of lucky coincidence. It fails completely for helium, cannot predict the relative intensities of spectral lines, and misses the fine structure (small splittings) observed in high-resolution spectroscopy. Most fundamentally, electrons do not actually travel in circular paths — quantum mechanics replaced orbits with probability wavefunctions. The angular momentum quantization that Bohr postulated was later understood by de Broglie as the condition for a standing electron wave to fit around the orbit, and by full quantum mechanics as a consequence of the wavefunction's angular structure.

What survives from Bohr into modern physics is the conceptual framework: discrete energy levels, photon emission and absorption as transitions between those levels, and the ground state as the lowest-energy configuration (not a state of rest). These ideas carry directly into quantum mechanics, spectroscopy, lasers, and atomic clocks. The numerical result E_n = −13.6 eV/n² also remains correct in the full quantum treatment of hydrogen.
