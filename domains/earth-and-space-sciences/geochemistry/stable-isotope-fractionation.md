---
id: stable-isotope-fractionation
title: Stable Isotope Fractionation
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: geochemical-thermodynamics
  type: hard
builds-toward:
- oxygen-isotopes-geochemistry
- carbon-isotopes-geochemistry
- hydrogen-nitrogen-isotopes
- isotope-hydrology
tags:
- stable-isotopes
- fractionation
- delta-notation
- isotope-effects
stage: expert
status: validated
---

# Stable Isotope Fractionation

## Core Idea
Stable isotope fractionation refers to the partitioning of isotopes between coexisting phases, molecules, or during physical/chemical processes. Heavier isotopes form slightly stronger bonds (higher vibrational frequency, lower zero-point energy), causing systematic mass-dependent differences in reaction rates and equilibrium distributions. This fractionation is expressed using delta notation: delta = [(R-sample/R-standard) - 1] x 1000, in per mil. Equilibrium fractionation is temperature-dependent (decreasing with increasing T), providing geothermometers. Kinetic fractionation accompanies incomplete or unidirectional processes (evaporation, diffusion, biological reactions) and is typically larger. These small but measurable isotopic variations are powerful tracers of processes, sources, and temperatures throughout Earth systems.

## Questions

```yaml
- question: "Two coexisting minerals -- quartz and magnetite -- are analyzed for oxygen isotopes. The fractionation between them (delta-18O-quartz minus delta-18O-magnetite) is 6 per mil. How is this used as a geothermometer?"
  type: multiple-choice
  options:
    - "Larger fractionation indicates higher temperature"
    - "The fractionation between coexisting minerals decreases with increasing temperature; a calibrated relationship between the fractionation factor and temperature (typically 1000*ln(alpha) proportional to 1/T^2) allows calculation of the equilibrium temperature from the measured isotopic difference"
    - "The absolute delta-18O value of either mineral gives the temperature directly"
    - "Oxygen isotope thermometry only works for igneous rocks"
  answer: 1
  explanation: "Equilibrium isotope fractionation between two phases decreases systematically with increasing temperature because thermal energy increasingly overcomes the small bond-energy differences between isotopes. The quartz-magnetite fractionation has been experimentally calibrated: 6 per mil corresponds to approximately 600 C. Smaller fractionation would indicate higher temperature, larger fractionation would indicate lower temperature."

- question: "Kinetic isotope fractionation always favors the lighter isotope in the product."
  type: true-false
  answer: true
  explanation: "Kinetic fractionation arises because lighter isotopes have higher velocities (at the same kinetic energy) and lower activation energies for bond breaking. In unidirectional or incomplete processes -- diffusion, evaporation, biological reactions -- the lighter isotope reacts or moves faster, becoming enriched in the product relative to the reactant. This is why evaporated water vapor is enriched in H-16O relative to H-18O, and why biologically fixed carbon (organic matter) is enriched in 12C relative to 13C."

- question: "Explain why stable isotope fractionation decreases with increasing temperature and what this means for isotope geothermometry."
  type: short-answer
  answer: "Fractionation arises from differences in zero-point vibrational energy between isotopically substituted molecules. At low temperatures, these differences are significant relative to thermal energy (kT), causing strong preferential partitioning of heavy isotopes into phases with higher bond stiffness. As temperature increases, thermal energy dominates over zero-point energy differences, the vibrational energy levels converge, and fractionation decreases -- approaching zero at very high temperatures where all isotopes behave identically. For geothermometry, this T-dependence means the isotopic difference between coexisting minerals is a monotonic function of temperature, enabling temperature calculation from measured isotopic compositions."
  explanation: "The 1/T^2 dependence of fractionation is the physical basis of isotope geothermometry: at high T, phases are isotopically similar; at low T, they diverge."
```

## Explainer

Stable isotopes are among the most versatile tools in geochemistry because the fractionation effects are universal -- every chemical and physical process partitions isotopes to some degree -- and the measurements are precise enough (modern mass spectrometers resolve differences of 0.01 per mil) to detect these subtle effects.

The delta notation standardizes isotopic measurements relative to international standards: VSMOW for oxygen and hydrogen, VPDB for carbon and oxygen in carbonates, atmospheric N2 for nitrogen. A sample with delta-18O = +10 per mil is enriched in 18O by 10 parts per thousand relative to VSMOW. This relative notation avoids the need to report absolute isotope ratios (which are measured with lower precision) and allows direct comparison between laboratories.

Equilibrium fractionation reflects the thermodynamic preference for heavy isotopes in phases with stiffer bonds. In the carbonate-water system, 18O concentrates in the carbonate (stronger C-O bonds) relative to the water. The fractionation factor alpha (approximately 1.03 at 25 C) decreases smoothly with temperature, forming the basis of paleothermometry -- measuring delta-18O in ancient carbonates to reconstruct past ocean temperatures. This technique, pioneered by Harold Urey in the 1940s, remains one of the most important tools in paleoclimatology.

Kinetic fractionation reflects the mass-dependent differences in reaction rates and transport properties. During evaporation, lighter H2-16O molecules escape the liquid surface faster than heavier H2-18O molecules, leaving the residual liquid enriched in 18O. During photosynthesis, the enzyme RuBisCO preferentially fixes 12CO2 over 13CO2, depleting organic matter in 13C. These kinetic effects are process-specific tracers: the magnitude and direction of fractionation fingerprint the mechanism responsible, enabling reconstruction of past environmental conditions, biological activity, and chemical pathways from isotopic measurements in rocks, water, and organic matter.
