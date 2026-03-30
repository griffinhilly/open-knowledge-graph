---
id: semiconductor-materials-chemistry
title: Semiconductor Materials
domain: chemistry
course: materials-chemistry
prerequisites:
- id: electronic-band-theory-of-solids
  type: hard
- id: defect-chemistry
  type: hard
- id: crystal-structures-and-unit-cells
  type: soft
builds-toward:
- photovoltaic-materials-chemistry
- thin-film-deposition-cvd-pvd
tags:
- semiconductors
- doping
- p-n junction
- silicon
- compound semiconductors
stage: advanced
status: validated
---

# Semiconductor Materials

## Core Idea
Semiconductors are materials with band gaps small enough that their electrical conductivity can be precisely controlled through doping, temperature, and light exposure. Intrinsic semiconductors (pure Si, Ge) have equal numbers of electrons and holes from thermal excitation across the band gap. Extrinsic semiconductors are doped with electron donors (n-type: P in Si) or acceptors (p-type: B in Si) to create controlled carrier concentrations many orders of magnitude above intrinsic levels. The chemistry of semiconductor materials extends beyond elemental Si and Ge to compound semiconductors (III-V: GaAs, InP; II-VI: CdTe, ZnO) and emerging materials (perovskites, organic semiconductors), each offering different band gaps, mobilities, and optical properties.

## Questions

```yaml
- question: "When phosphorus (group 15) is doped into silicon (group 14), each P atom contributes one extra electron to the conduction band. Why does this make the material n-type rather than simply changing the lattice energy?"
  type: short-answer
  answer: "Phosphorus has 5 valence electrons versus silicon's 4. Four of P's electrons participate in covalent bonds with neighboring Si atoms, mimicking Si. The fifth electron is only weakly bound to the P+ core (binding energy ~45 meV, far less than kT at room temperature), so it ionizes into the conduction band at room temperature. This creates a free electron without creating a hole in the valence band, making the material n-type. The donor level sits just below the conduction band edge in the band diagram."
  explanation: "The key chemistry insight is that aliovalent substitution in a covalent crystal creates localized states near the band edges. Donors (extra electrons) create states just below the conduction band; acceptors (missing electrons) create states just above the valence band. The shallow binding energy (~40-50 meV for common dopants in Si) means complete ionization at room temperature, giving precise control over carrier concentration through dopant concentration. This is why semiconductor purity and controlled doping are central to the entire electronics industry."

- question: "GaAs is a direct band gap semiconductor (1.42 eV) while Si has an indirect band gap (1.12 eV). Which statement correctly explains why GaAs is preferred for LEDs and laser diodes?"
  type: multiple-choice
  options:
    - "GaAs has a larger band gap, so it emits higher-energy photons"
    - "In GaAs, electrons and holes recombine directly by emitting a photon without requiring a phonon, making radiative recombination far more efficient"
    - "GaAs has higher electron mobility, which increases the rate of photon emission"
    - "Silicon cannot emit light under any circumstances due to its crystal structure"
  answer: 1
  explanation: "In a direct gap material, the conduction band minimum and valence band maximum are at the same point in k-space (both at the Gamma point for GaAs). An electron can drop from the conduction band to the valence band by emitting a photon that carries away the energy — momentum is automatically conserved because Delta-k is approximately zero. In silicon's indirect gap, the band extrema are at different k-values, so recombination requires a phonon to conserve momentum. This three-particle process (electron + hole + phonon) is far less probable than the two-particle radiative process, making Si a very inefficient light emitter."

- question: "Compound semiconductors like GaAs offer tunable band gaps not available from elemental semiconductors."
  type: true-false
  answer: true
  explanation: "Elemental semiconductors are limited to the band gaps of Si (1.12 eV), Ge (0.67 eV), and diamond (5.5 eV). Compound semiconductors span a continuous range: InSb (0.17 eV) through GaAs (1.42 eV) to GaN (3.4 eV) to AlN (6.2 eV). Moreover, ternary and quaternary alloys (e.g., Al_xGa_{1-x}As, In_xGa_{1-x}N) allow continuous tuning of the band gap by varying composition x. This tunability is essential for designing materials that absorb or emit at specific wavelengths — the basis of LEDs, lasers, detectors, and multi-junction solar cells."

- question: "Silicon's dominance in the electronics industry is primarily due to its superior electronic properties compared to all other semiconductors."
  type: true-false
  answer: false
  explanation: "Silicon's dominance is primarily due to the exceptional quality of its native oxide (SiO2), the abundance of silicon in the Earth's crust, and decades of manufacturing optimization — not superior intrinsic electronic properties. GaAs has ~6x higher electron mobility; GaN has superior breakdown voltage and thermal stability; Ge has higher hole mobility. But SiO2 forms a near-perfect, stable, electrically insulating gate dielectric on Si surfaces, which was critical for MOSFET technology. The entire semiconductor industry was built on this fortunate chemical property."
```

## Explainer

Semiconductor materials sit in the electronic sweet spot between metals (which always conduct) and insulators (which never conduct). Their defining characteristic is a band gap small enough that conductivity can be controlled — by temperature, by light, and most importantly, by the deliberate introduction of impurity atoms. This controllability is why semiconductors underpin all of modern electronics: transistors, solar cells, LEDs, lasers, and sensors all exploit the ability to switch conductivity on and off or to convert between electrical and optical energy.

**Intrinsic** silicon at room temperature has about 10^10 free electrons per cm^3 — many orders of magnitude below the 10^22 atoms per cm^3 in the crystal. This feeble conductivity becomes technologically useful only through **doping**. Adding phosphorus at 10^16 atoms per cm^3 (about 1 ppm) increases the electron concentration by six orders of magnitude to 10^16 per cm^3. The chemistry is simple: P has one more valence electron than Si, and that extra electron requires only ~45 meV to escape to the conduction band — easily provided by room-temperature thermal energy. Boron doping works the opposite way: B has one fewer electron than Si, creating a hole (missing electron) in the valence band that acts as a positive charge carrier.

The chemistry of compound semiconductors opens design possibilities unavailable from elemental materials. **III-V compounds** (GaAs, InP, GaN) combine group 13 and group 15 elements to create isoelectronic analogs of silicon but with different band structures. GaAs has a direct band gap, making it the material of choice for optoelectronics. GaN's wide band gap (3.4 eV) enables blue and white LEDs — the invention that earned the 2014 Nobel Prize in Physics. **II-VI compounds** (CdTe, ZnSe, ZnO) pair group 12 and group 16 elements, offering even wider band gap ranges. The periodic table becomes a design palette.

The frontier of semiconductor materials chemistry lies in materials beyond traditional inorganic crystals. **Halide perovskites** (CH3NH3PbI3 and relatives) have emerged as remarkable photovoltaic materials with sharp optical absorption edges and long carrier diffusion lengths, despite being processed from solution at low temperatures. **Organic semiconductors** (conjugated polymers and small molecules) offer mechanical flexibility and low-cost processing. **Two-dimensional materials** (MoS2, WSe2) provide atomic-scale thickness with tunable band gaps. Each class presents distinct chemical challenges — perovskite stability, organic crystallinity, 2D defect control — that materials chemists are actively working to solve.
