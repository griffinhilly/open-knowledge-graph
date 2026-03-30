---
id: cosmological-constant-dark-energy
title: Cosmological Constant and Dark Energy
domain: physics
course: general-relativity
prerequisites:
- id: friedmann-equations
  type: hard
- id: einstein-field-equations
  type: hard
tags:
- cosmological-constant
- dark-energy
- accelerating-expansion
- vacuum-energy
- lambda
stage: expert
status: validated
---

# Cosmological Constant and Dark Energy

## Core Idea
The cosmological constant Λ, introduced by Einstein in 1917 to allow a static universe and later "retracted" when expansion was discovered, is now understood as the simplest model of dark energy — the component driving the observed accelerating expansion of the universe. In the field equations G_μν + Λg_μν = (8πG/c⁴)T_μν, the Λg_μν term acts as a perfect fluid with equation of state p = -ρc² (w = -1) and constant energy density ρ_Λ = Λc²/(8πG). Its negative pressure produces gravitational repulsion, accelerating the expansion. Dark energy constitutes about 68% of the total energy density of the universe. The observed value Λ ~ 10⁻⁵² m⁻² is 120 orders of magnitude smaller than the naive quantum field theory prediction for vacuum energy — the "cosmological constant problem," widely considered the worst fine-tuning problem in physics.

## Questions

```yaml
- question: "The cosmological constant Λ can be equivalently described as a contribution to the geometry (left side of Einstein's equations) or as a form of energy (right side). What equation of state does it correspond to when treated as a fluid?"
  type: multiple-choice
  options:
    - "p = 0 (pressureless dust)"
    - "p = ρc²/3 (radiation)"
    - "p = -ρc² (w = -1)"
    - "p = -ρc²/3 (curvature-like)"
  answer: 2
  explanation: "Moving the Λg_μν term to the right side of the Einstein equations, it acts as a stress-energy tensor T^(Λ)_μν = -(Λc⁴/8πG)g_μν, which is that of a perfect fluid with constant energy density ρ_Λ = Λc²/(8πG) and pressure p_Λ = -ρ_Λ c². This gives equation of state parameter w = p/(ρc²) = -1. The negative pressure is the key: in the Friedmann acceleration equation, the combination ρ + 3p/c² = ρ - 3ρ = -2ρ < 0, so the cosmological constant produces gravitational repulsion."

- question: "The cosmological constant problem arises because the observed value of Λ is much smaller than quantum field theory predicts for the vacuum energy."
  type: true-false
  answer: true
  explanation: "Quantum field theory predicts that the vacuum has a zero-point energy density on the order of the Planck energy density: ρ_QFT ~ M_Pl c²/l_Pl³ ~ 10⁹³ g/cm³. The observed dark energy density is ρ_Λ ~ 10⁻²⁹ g/cm³ — a discrepancy of about 120 orders of magnitude. Even with more conservative cutoffs (the electroweak scale), the discrepancy is about 56 orders of magnitude. Why the vacuum energy is so extraordinarily small compared to any natural quantum field theory scale — but not exactly zero — is the cosmological constant problem, and no satisfactory solution exists."

- question: "Explain how Type Ia supernovae observations in 1998 provided evidence for accelerating expansion and hence dark energy."
  type: short-answer
  answer: "Type Ia supernovae are 'standardizable candles' — their peak luminosity can be calibrated from their light-curve shape, allowing their absolute distance to be determined. By comparing this luminosity distance with their redshift z, the expansion history a(t) can be reconstructed. Two independent teams (the Supernova Cosmology Project and the High-z Supernova Search Team) found that distant supernovae (z ~ 0.5-1) were dimmer than expected in a decelerating universe — they were farther away than a matter-dominated model predicts. This implied the expansion has been accelerating for the past ~5 billion years, which requires a component with negative pressure (w < -1/3) dominating the energy budget. The simplest explanation is a cosmological constant with w = -1."
  explanation: "The 1998 discovery earned Perlmutter, Schmidt, and Riess the 2011 Nobel Prize in Physics. The result has been independently confirmed by CMB observations (Planck), baryon acoustic oscillations (SDSS, DESI), and other probes. All evidence is consistent with w = -1, though slight deviations cannot be ruled out."

- question: "Could dark energy be something other than a cosmological constant? What would distinguish a dynamical dark energy model from Λ observationally?"
  type: short-answer
  answer: "Yes — dark energy could be a dynamical scalar field (quintessence) or some other exotic component with time-varying energy density and equation of state w(z) ≠ -1. A cosmological constant has w = -1 exactly and constant energy density. A dynamical model would have w ≠ -1 or w varying with redshift. Observationally, the distinction requires measuring the expansion history H(z) and the growth rate of cosmic structure with sufficient precision to detect deviations from w = -1. Current data (CMB, supernovae, BAO) are consistent with w = -1 to within about 5%, but next-generation surveys (DESI, Euclid, Rubin/LSST) aim to measure w(z) to percent-level precision. Recent DESI BAO results (2024) hint at possible evolution of w with redshift, though the evidence is not yet conclusive."
  explanation: "The nature of dark energy is one of the most important open questions in physics. If w is exactly -1, dark energy is likely the cosmological constant (vacuum energy), and the cosmological constant problem is the central puzzle. If w ≠ -1 or varies with time, entirely new physics is at work."
```

## Explainer

Einstein introduced the cosmological constant Λ in 1917 as a modification to his field equations to allow a static universe — at the time, the prevailing belief was that the universe was eternal and unchanging. The term Λg_μν on the left side of the equations provides a repulsive effect that can balance the attractive gravity of matter. When Hubble's 1929 observations established that the universe is expanding, the motivation for Λ evaporated, and Einstein reportedly called it his "greatest blunder." For most of the 20th century, Λ was set to zero by convention.

The dramatic reversal came in 1998, when two independent supernova survey teams discovered that the expansion of the universe is accelerating. Type Ia supernovae at redshift z ~ 0.5-1 appeared fainter (farther away) than expected in a decelerating matter-dominated universe. The most natural explanation within GR is a positive cosmological constant Λ > 0, which produces a repulsive gravitational effect that overwhelms matter's attractive gravity at late times. In the Friedmann acceleration equation ä/a = -(4πG/3)(ρ + 3p/c²) + Λ/3, the cosmological constant contributes positively to ä, driving accelerating expansion when Λ dominates over the matter term.

The cosmological constant can be equivalently interpreted as the energy density of empty space — vacuum energy. When the Λg_μν term is moved to the right side of the Einstein equations, it acts as a stress-energy tensor with constant energy density ρ_Λ = Λc²/(8πG) ≈ 6 × 10⁻¹⁰ J/m³ and pressure p_Λ = -ρ_Λc² (equation of state w = -1). This negative pressure, paradoxically, drives repulsive gravity — in GR, the gravitational effect of pressure is proportional to ρ + 3p/c², and for Λ this is -2ρ_Λ, which is negative. The vacuum energy constitutes about 68% of the total energy density of the universe, with dark matter contributing about 27% and ordinary matter about 5%.

The cosmological constant problem is the most severe fine-tuning problem in theoretical physics. Quantum field theory predicts that the vacuum should have an enormous energy density from zero-point fluctuations of all quantum fields, with a natural scale set by the Planck energy density (~10⁹³ g/cm³). The observed dark energy density is about 10⁻²⁹ g/cm³ — roughly 10¹²⁰ times smaller. Even using a lower cutoff (the electroweak scale ~100 GeV), the predicted vacuum energy exceeds the observed value by ~56 orders of magnitude. Some unknown mechanism must cancel the vacuum energy to extraordinary precision while leaving a tiny residual — or the cosmological constant's smallness has an entirely different explanation (anthropic selection, dynamical relaxation mechanisms, or modifications of gravity). No satisfactory resolution exists, and the problem remains one of the deepest unsolved questions at the intersection of general relativity and quantum field theory.
