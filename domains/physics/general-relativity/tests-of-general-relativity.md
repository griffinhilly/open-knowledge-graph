---
id: tests-of-general-relativity
title: Tests of General Relativity
domain: physics
course: general-relativity
prerequisites:
- id: schwarzschild-solution
  type: hard
- id: gravitational-waves
  type: soft
- id: equivalence-principle
  type: hard
tags:
- experimental-tests
- solar-system-tests
- strong-field-tests
- gravitational-wave-tests
- equivalence-principle-tests
stage: expert
status: validated
---

# Tests of General Relativity

## Core Idea
General relativity has been tested across an extraordinary range of scales and field strengths, from laboratory experiments to cosmological observations, passing every test with remarkable precision. The classical solar-system tests include: perihelion precession of Mercury (43 arcsec/century, confirmed to 0.1%), deflection of light by the Sun (1.75 arcsec, confirmed to 0.01% via VLBI), gravitational redshift (Pound-Rebka, GPS, confirmed to 10⁻⁵), and Shapiro time delay (confirmed to 0.001%). Strong-field tests include binary pulsar orbital decay (PSR B1913+16, matching the gravitational wave quadrupole formula to 0.2%), direct gravitational wave detection (LIGO/Virgo, confirming the nonlinear strong-field regime), black hole shadow imaging (Event Horizon Telescope), and frame-dragging measurements (Gravity Probe B, LAGEOS). Cosmological tests include the expansion history consistent with the Friedmann equations and the spectrum of CMB anisotropies. No confirmed deviation from GR has been found.

## Questions

```yaml
- question: "Which test of general relativity probes the strong-field, highly dynamical regime where the theory differs most from Newtonian gravity and linearized approximations?"
  type: multiple-choice
  options:
    - "The Pound-Rebka gravitational redshift experiment"
    - "Mercury's perihelion precession"
    - "LIGO's detection of binary black hole mergers"
    - "The deflection of starlight by the Sun"
  answer: 2
  explanation: "LIGO's gravitational wave detections probe the regime where two black holes spiral together and merge — gravitational fields are extreme (v/c ~ 0.5, GM/(rc²) ~ 0.5), the dynamics are highly nonlinear, and the full nonlinear Einstein equations (solved numerically) are needed to predict the waveform. All other listed tests are in the weak-field (GM/(rc²) << 1) or quasi-static regime, where linearized or post-Newtonian approximations suffice. The LIGO observations confirmed for the first time that GR is correct in the strong-field, dynamical regime."

- question: "The Shapiro time delay is sometimes called the 'fourth classical test' of general relativity. It measures the extra time light takes to travel near a massive body."
  type: true-false
  answer: true
  explanation: "Predicted by Irwin Shapiro in 1964, the Shapiro delay is the extra time taken by a light signal (radar or radio) passing near a massive body due to the spatial curvature (the g_{rr} component of the Schwarzschild metric). For a signal passing near the Sun, the extra round-trip delay is about 240 microseconds. It was first measured using radar signals bounced off Mercury and Venus, and has been confirmed to 0.001% precision using the Cassini spacecraft's radio signal passing near the Sun (2003). It tests a different aspect of the metric than light deflection or precession, providing an independent check."

- question: "Explain how the binary pulsar PSR B1913+16 tests GR in ways that solar-system tests cannot."
  type: short-answer
  answer: "The binary pulsar provides tests in the strong-field (compact neutron stars with surface gravity ~10¹¹ g), high-velocity (orbital speeds ~0.1% of c), and radiative (energy loss via gravitational waves) regimes — all inaccessible to solar-system tests. Specifically: (1) The periastron advance (4.2°/yr) tests strong-field orbital dynamics. (2) The orbital period decay (matching the quadrupole formula to 0.2%) confirms gravitational wave emission. (3) The gravitational redshift and time dilation of pulsar signals test the strong-field equivalence principle. (4) The Shapiro delay when one pulsar passes behind the other tests strong-field light propagation. Multiple relativistic effects measured in a single system over-determine the two masses, providing a consistency check of GR with no adjustable parameters."
  explanation: "The Hulse-Taylor binary pulsar was the first system to provide evidence for gravitational waves (through orbital decay) and earned the 1993 Nobel Prize. The double pulsar J0737-3039 (discovered 2003) provides even more precise tests and measures additional effects."

- question: "Despite passing all tests to date, GR is not considered a complete theory. Name two reasons physicists expect it to break down."
  type: short-answer
  answer: "First, the singularity theorems prove that GR predicts its own breakdown — singularities (infinite curvature, geodesic incompleteness) form generically inside black holes and at the Big Bang, where a quantum theory of gravity is expected to take over. Second, GR is not renormalizable as a quantum field theory — perturbative quantization of the gravitational field produces infinities that cannot be absorbed into a finite number of parameters, unlike the successful quantum field theories of the Standard Model. These are not observational failures but theoretical inconsistencies that signal GR must be an effective (low-energy) theory, valid below the Planck scale (E ~ 10¹⁹ GeV, l ~ 10⁻³⁵ m) but superseded by a quantum gravity theory at higher energies."
  explanation: "Other motivations for beyond-GR physics include: dark matter (unexplained by GR + Standard Model alone, unless new particles exist), the cosmological constant problem (120-order-of-magnitude discrepancy with quantum field theory), and the information paradox (tension between black hole evaporation and quantum unitarity). Each suggests GR, while extraordinarily successful, is part of a larger theoretical framework."
```

## Explainer

General relativity makes precise, quantitative predictions that can be tested against observation, and it has passed every test conducted over more than a century. The classical solar-system tests — perihelion precession, light deflection, gravitational redshift — were the first confirmations and remain among the most precise. Mercury's anomalous perihelion precession of 42.98 arcsec/century was the first quantitative test (1915). Light deflection by the Sun (1.75 arcsec at the limb) was confirmed in 1919 and has since been verified to 0.01% precision using VLBI radio observations. Gravitational redshift has been confirmed from the Pound-Rebka experiment (10%) through Gravity Probe A (0.007%) to modern optical atomic clocks (which detect the redshift over centimeter height differences). The Shapiro time delay, confirmed to 0.001% by the Cassini spacecraft, tests the spatial curvature component of the metric independently of the other effects.

Binary pulsars transformed GR testing by providing access to strong-field, high-velocity, and radiative gravity. The Hulse-Taylor binary pulsar PSR B1913+16 (discovered 1974) consists of two neutron stars in a tight, eccentric orbit. Its periastron advance (4.2°/year — 35,000 times Mercury's rate), gravitational time dilation, and Shapiro delay test strong-field gravity. Most dramatically, the cumulative orbital phase shift from gravitational wave energy loss matches the GR quadrupole formula prediction to 0.2% over four decades of observation — indirect proof that gravitational waves exist and carry energy. The double pulsar PSR J0737-3039 (discovered 2003) provides five or more independent tests of GR in a single system, all consistent.

The direct detection of gravitational waves by LIGO in 2015 opened a new frontier. The first signal (GW150914) matched the numerical-relativity prediction for a binary black hole merger — two 30-solar-mass black holes spiraling together, merging, and ringing down to a single Kerr black hole — with extraordinary precision. This tested GR in the most extreme regime possible: velocities approaching c, gravitational fields at the Planck curvature scale, and the fully nonlinear dynamics of merging horizons. Subsequent detections have confirmed the GR predictions for binary neutron star mergers (GW170817, also observed electromagnetically across the spectrum) and black hole-neutron star mergers. The gravitational wave speed was constrained to equal the speed of light to within 10⁻¹⁵, ruling out many modified gravity theories.

Additional tests continue to accumulate. The Event Horizon Telescope imaged the shadows of the supermassive black holes M87* and Sgr A*, confirming that the shadow size and shape are consistent with the Kerr metric. Gravity Probe B confirmed frame dragging (Lense-Thirring precession) in Earth orbit. Cosmological observations — the CMB spectrum, baryon acoustic oscillations, Type Ia supernovae — are consistent with the Friedmann equations derived from GR. Laboratory tests of the equivalence principle (torsion-balance experiments) confirm the equality of gravitational and inertial mass to 10⁻¹³ precision. Despite this extraordinary success, physicists expect GR to break down at the Planck scale, where quantum gravitational effects become important — a regime not yet accessible to experiment.
