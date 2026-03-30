---
id: gravitational-redshift
title: Gravitational Redshift
domain: physics
course: general-relativity
prerequisites:
- id: schwarzschild-solution
  type: hard
- id: equivalence-principle
  type: hard
tags:
- redshift
- time-dilation
- gravitational-potential
- pound-rebka
- clocks
stage: expert
status: validated
---

# Gravitational Redshift

## Core Idea
Gravitational redshift is the decrease in frequency (increase in wavelength) of light as it climbs out of a gravitational potential well, and the corresponding blueshift as light falls in. For the Schwarzschild metric, a photon emitted at radius r_e with frequency ν_e is observed at radius r_o with frequency ν_o = ν_e √[(1 - r_s/r_e)/(1 - r_s/r_o)], where r_s = 2GM/c². In the weak-field limit, the fractional shift is Δν/ν ≈ ΔΦ/c², where ΔΦ is the difference in Newtonian gravitational potential. Equivalently, clocks at lower gravitational potentials tick more slowly than clocks at higher potentials. Gravitational redshift was predicted by Einstein from the equivalence principle alone (before the full theory was complete), confirmed by the Pound-Rebka experiment (1959), and is an essential correction in the GPS satellite system.

## Questions

```yaml
- question: "A photon is emitted from the surface of a neutron star and observed by a distant astronomer. Compared to the same atomic transition measured in the astronomer's laboratory, the neutron-star photon appears:"
  type: multiple-choice
  options:
    - "Blueshifted, because the strong gravitational field accelerates the photon"
    - "Redshifted, because the photon loses energy climbing out of the deep gravitational potential"
    - "Unchanged, because photons are massless and unaffected by gravity"
    - "Redshifted or blueshifted depending on the photon's direction of emission"
  answer: 1
  explanation: "A photon climbing out of a gravitational well is redshifted — its frequency decreases. For a neutron star with r_s/R ≈ 0.4, the redshift factor (1 - r_s/R)^{1/2} ≈ 0.77, meaning the observed frequency is about 77% of the emitted frequency — a substantial 23% redshift. The photon does not 'lose energy' in the Newtonian sense (there is no well-defined local gravitational potential energy for photons in GR), but the relationship between the emitter's proper time and the observer's proper time produces the frequency shift."

- question: "Gravitational time dilation and gravitational redshift are two descriptions of the same physical phenomenon."
  type: true-false
  answer: true
  explanation: "A clock at lower gravitational potential ticks slower relative to a clock at higher potential — this is gravitational time dilation. A photon emitted by the lower clock (which oscillates at the lower clock's rate) arrives at the upper clock with fewer oscillations per unit of the upper clock's time — this is gravitational redshift. They are the same effect described from different perspectives: one in terms of clock rates, the other in terms of photon frequencies. The fractional frequency shift equals the fractional difference in clock rates."

- question: "In the Pound-Rebka experiment, gamma rays were sent vertically through a height difference of 22.6 meters in Earth's gravitational field. Calculate the expected fractional frequency shift and explain why this experiment was feasible despite the tiny effect."
  type: short-answer
  answer: "The fractional frequency shift is Δν/ν = gΔh/c² = (9.8)(22.6)/(3×10⁸)² ≈ 2.46 × 10⁻¹⁵. This extraordinarily small shift was measurable because Pound and Rebka used the Mossbauer effect — nuclear gamma-ray resonance with ⁵⁷Fe, which has a natural linewidth narrow enough (Δν/ν ~ 10⁻¹³) to resolve the gravitational shift. By moving the source at a controlled velocity (Doppler compensation), they could scan across the resonance line and measure the gravitational frequency shift to about 10% accuracy, later improved to about 1% by Pound and Snider."
  explanation: "The Pound-Rebka experiment was the first direct measurement of gravitational redshift in a laboratory setting. The key enabling technology was the Mossbauer effect, discovered in 1958, which provided the spectral precision needed to detect a shift of parts in 10¹⁵."

- question: "GPS satellites orbit at about 20,200 km altitude and carry atomic clocks. In what direction does gravitational time dilation shift the satellite clocks relative to ground clocks, and by approximately how much per day?"
  type: short-answer
  answer: "Satellite clocks at higher gravitational potential tick faster than ground clocks. The gravitational time dilation effect causes the satellite clocks to gain about 45 microseconds per day relative to ground clocks. (There is a competing special-relativistic time dilation of about -7 microseconds/day due to the satellites' orbital speed, giving a net gain of about 38 microseconds/day.) Without correction, this would cause position errors accumulating at about 10 km per day, rendering GPS useless for navigation."
  explanation: "GPS is one of the most tangible everyday consequences of general relativity. The 38 μs/day net correction is pre-programmed into the satellite clocks by adjusting their frequency before launch. The fact that both special-relativistic and general-relativistic corrections are needed, and that they act in opposite directions, makes GPS a beautiful demonstration of both theories."
```

## Explainer

Gravitational redshift can be understood through the equivalence principle without any detailed knowledge of the Schwarzschild metric. Consider a photon emitted upward in a uniformly accelerating elevator. By the time the photon reaches the ceiling, the ceiling is moving faster than the floor was when the photon was emitted (the elevator accelerated during the photon's transit). The ceiling detector therefore sees the photon Doppler-shifted to a lower frequency. By the equivalence principle, the same effect occurs in a uniform gravitational field: a photon climbing up through height Δh acquires a redshift Δν/ν = gΔh/c². This argument was Einstein's original derivation, published in 1907 — eight years before the full field equations.

In the full Schwarzschild geometry, the redshift formula is exact: ν_o/ν_e = √[(1 - r_s/r_e)/(1 - r_s/r_o)]. For an observer at infinity (r_o → ∞) receiving light from radius r_e, this becomes ν_∞/ν_e = √(1 - r_s/r_e). At the event horizon (r_e = r_s), the redshift becomes infinite — photons emitted at the horizon are infinitely redshifted to zero frequency by the time they reach a distant observer. This infinite redshift is why a distant observer sees an infalling object fade and freeze at the horizon rather than crossing it. The formula reduces to the weak-field approximation Δν/ν ≈ ΔΦ/c² when r_s/r << 1, which is the regime relevant for Earth (r_s/R_Earth ≈ 1.4 × 10⁻⁹) and the Sun (r_s/R_Sun ≈ 4.2 × 10⁻⁶).

The equivalence between gravitational redshift and gravitational time dilation is exact. A clock at radius r in the Schwarzschild geometry ticks at a rate dτ = √(1 - r_s/r) dt relative to coordinate time t. Two clocks at different radii r₁ and r₂ therefore have a proper-time ratio dτ₁/dτ₂ = √[(1 - r_s/r₁)/(1 - r_s/r₂)], which is exactly the frequency ratio of light exchanged between them. The lower clock ticks slower, and photons emitted by it arrive at the higher clock with a proportionally lower frequency. These are not two separate effects but one phenomenon viewed from two perspectives: the photon's frequency is determined by the emitter's clock rate as seen by the receiver.

Experimental confirmation of gravitational redshift spans an impressive range of precision. The Pound-Rebka experiment (1959) measured the redshift of ⁵⁷Fe gamma rays over 22.6 meters in the Harvard physics building, confirming the predicted shift of about 2.5 × 10⁻¹⁵ to 10% accuracy. Hydrogen maser clocks flown on rockets (Gravity Probe A, 1976) confirmed the redshift to 7 × 10⁻⁵ precision. Most dramatically, the GPS satellite system provides a continuous, operational test: satellite atomic clocks at 20,200 km altitude gain about 45 μs/day from gravitational time dilation (offset by -7 μs/day from special-relativistic velocity effects), requiring a net correction of about 38 μs/day. Without this relativistic correction, GPS position errors would accumulate at roughly 10 km per day. Modern optical atomic clocks can detect the gravitational redshift between two laboratories separated by just 30 cm of vertical height, pushing precision to the 10⁻¹⁸ level.
