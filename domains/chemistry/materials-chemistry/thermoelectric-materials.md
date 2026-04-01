---
id: thermoelectric-materials
title: Thermoelectric Materials
domain: chemistry
course: materials-chemistry
prerequisites:
- id: electronic-band-theory-of-solids
  type: hard
- id: crystal-structures-and-unit-cells
  type: hard
- id: defect-chemistry
  type: soft
- id: semiconductor-materials-chemistry
  type: soft
builds-toward: []
tags:
- thermoelectric
- Seebeck-effect
- Peltier-effect
- figure-of-merit
- ZT
- waste-heat-recovery
stage: expert
status: validated
---

# Thermoelectric Materials

## Core Idea
Thermoelectric materials convert temperature differences directly into electrical voltage (Seebeck effect) or use electrical current to pump heat (Peltier effect). Their efficiency is governed by the dimensionless figure of merit ZT = S^2 sigma T / kappa, where S is the Seebeck coefficient, sigma is the electrical conductivity, T is the absolute temperature, and kappa is the thermal conductivity. The central materials chemistry challenge is that S, sigma, and kappa are interdependent through carrier concentration: increasing carrier concentration raises sigma but lowers S and increases the electronic contribution to kappa. Achieving high ZT requires decoupling these properties, typically through nanostructuring to scatter phonons without scattering electrons, band engineering to enhance the Seebeck coefficient, or compositional complexity to suppress lattice thermal conductivity.

## Questions

```yaml
- question: "The thermoelectric figure of merit ZT = S^2*sigma*T/kappa contains both electrical conductivity (sigma) and thermal conductivity (kappa). Why can't you simply maximize sigma and minimize kappa independently?"
  type: short-answer
  answer: "Electrical conductivity and thermal conductivity are coupled through charge carriers. The Wiedemann-Franz law states that the electronic contribution to thermal conductivity is proportional to electrical conductivity: kappa_electronic = L*sigma*T, where L is the Lorenz number. Increasing sigma to improve the power factor (S^2*sigma) simultaneously increases the electronic thermal conductivity, partially canceling the benefit. Additionally, increasing carrier concentration to raise sigma reduces the Seebeck coefficient S (more carriers means less entropy per carrier, lower voltage per degree). This three-way coupling between S, sigma, and kappa means the optimal carrier concentration is a compromise, typically around 10^19 to 10^21 carriers per cm^3, characteristic of heavily doped semiconductors."
  explanation: "This interdependence is the fundamental reason why thermoelectric efficiency has been so difficult to improve. The Wiedemann-Franz law sets a floor on thermal conductivity for any given electrical conductivity. The only truly independent parameter is the lattice (phonon) contribution to thermal conductivity, which is why most modern strategies for improving ZT focus on reducing kappa_lattice through nanostructuring, point defects, or intrinsically low-kappa crystal structures."

- question: "Which strategy has been most effective for improving ZT beyond the bulk single-crystal limit?"
  type: multiple-choice
  options:
    - "Increasing the crystal purity to reduce electron scattering"
    - "Nanostructuring to introduce grain boundaries and interfaces that scatter phonons more effectively than electrons, reducing lattice thermal conductivity while preserving electrical conductivity"
    - "Using metals instead of semiconductors to maximize electrical conductivity"
    - "Operating at cryogenic temperatures where thermal conductivity is naturally low"
  answer: 1
  explanation: "Nanostructuring has been the most successful approach for pushing ZT above 1. Phonons have a broad spectrum of mean free paths (nanometers to micrometers), while electrons in heavily doped semiconductors have relatively short mean free paths (a few nanometers). Grain boundaries, nanoparticle inclusions, and hierarchical architectures with features at multiple length scales (atomic point defects, nanoscale precipitates, mesoscale grain boundaries) scatter mid- and long-wavelength phonons that carry most of the heat without significantly affecting electron transport. Biswas et al. (2012) demonstrated ZT ~ 2.2 in hierarchically structured PbTe using this 'all-scale' phonon scattering approach."

- question: "Bismuth telluride (Bi2Te3) has remained the dominant room-temperature thermoelectric material for over 60 years despite intensive research into alternatives."
  type: true-false
  answer: true
  explanation: "Bi2Te3 and its alloys (Bi2Te3-Sb2Te3 for p-type, Bi2Te3-Bi2Se3 for n-type) have ZT ~ 1 near room temperature and remain the commercial standard for Peltier coolers and low-temperature waste heat recovery. The layered crystal structure with weak van der Waals bonding between Te-Bi-Te-Bi-Te quintuple layers gives intrinsically low cross-plane thermal conductivity. While nanostructured variants of PbTe, SnSe, and other materials have achieved higher ZT values in laboratory settings at elevated temperatures, no material has displaced Bi2Te3 for room-temperature applications in commercial devices. This longevity reflects both the difficulty of the thermoelectric optimization problem and the additional practical requirements (mechanical strength, chemical stability, contact resistance) that laboratory ZT champions often fail to meet."

- question: "SnSe attracted enormous attention after Zhao et al. (2014) reported a ZT of 2.6 along the b-axis of single-crystal SnSe at 923 K. What structural property of SnSe contributes to its ultralow lattice thermal conductivity?"
  type: short-answer
  answer: "SnSe has a layered orthorhombic crystal structure (Pnma space group) with strong anharmonic bonding — the Sn-Se bonds have large Gruneisen parameters, meaning the bonds are highly asymmetric in their potential energy curves. This anharmonicity leads to strong phonon-phonon scattering (Umklapp processes), giving an intrinsically ultralow lattice thermal conductivity of ~0.23 W/m-K along certain crystallographic directions. The structure also undergoes a phase transition near 800 K from Pnma to the higher-symmetry Cmcm phase, further disrupting phonon transport near the operating temperature."
  explanation: "SnSe exemplifies the 'intrinsically low kappa' strategy: rather than engineering low thermal conductivity through nanostructuring of an otherwise high-kappa material, the crystal chemistry itself produces anomalously low phonon conduction. Other materials in this category include Cu2Se (liquid-like copper sublattice), AgSbTe2 (cation disorder), and various clathrates (rattling guest atoms). However, SnSe's extreme anisotropy, difficulty of single-crystal growth, and questions about reproducibility have limited practical adoption."
```

## Explainer

Thermoelectric materials occupy a unique niche in energy technology: they convert heat directly into electricity with no moving parts, no working fluid, and no maintenance. A thermoelectric generator placed on a hot exhaust pipe generates voltage from the temperature difference between the hot side and the ambient environment. A thermoelectric cooler, run in reverse, uses electrical current to pump heat, enabling solid-state refrigeration. The physics is straightforward — the Seebeck effect (voltage from temperature gradient) and Peltier effect (heat pumping from current) are bulk transport phenomena present in all conductors. The challenge is entirely one of materials chemistry: making these effects large enough to be practical.

The **figure of merit** ZT = S^2 sigma T / kappa encapsulates the optimization problem. The numerator, S^2 sigma (called the power factor), represents the material's ability to generate electrical power from a temperature difference. The denominator, kappa, represents parasitic heat flow that short-circuits the temperature difference. High ZT requires a material that conducts electricity well (high sigma), generates large voltage per degree (high S), and blocks heat flow (low kappa). The problem is that these properties are not independent. Free electrons carry both charge and heat; increasing their concentration improves sigma but worsens both S and the electronic part of kappa. The optimum carrier concentration falls in the heavily-doped semiconductor range (10^19-10^21 cm^-3), far above intrinsic semiconductors but well below metals.

Since the electronic properties are tightly coupled, most modern strategies target the **lattice thermal conductivity** kappa_lattice, the only quasi-independent parameter. Three approaches dominate. **Nanostructuring** introduces boundaries at length scales (10-100 nm) that scatter heat-carrying phonons without significantly impeding electrons. Spark plasma sintering of ball-milled nanopowders, in-situ precipitation of nanoscale second phases, and superlattice thin films all exploit this principle. **Compositional complexity** uses point defects (alloying), rattling atoms in cage structures (skutterudites, clathrates), or liquid-like sublattices (Cu2Se) to disrupt phonon propagation at the atomic scale. **Intrinsic anharmonicity** selects crystal structures where the chemical bonding itself produces strong phonon-phonon scattering — SnSe, with its record-setting ZT of 2.6 in single crystals, exemplifies this approach.

The gap between laboratory records and commercial reality remains wide. Most high-ZT results are measured on single crystals along favorable crystallographic directions, at elevated temperatures, and under conditions difficult to replicate in manufacturing. Commercial thermoelectric modules still use Bi2Te3 alloys (ZT ~ 1) for room-temperature applications and SiGe alloys for high-temperature applications like NASA's radioisotope thermoelectric generators. Bridging this gap requires not only high ZT but also mechanical robustness, chemical stability over thousands of thermal cycles, low contact resistance at electrode junctions, and scalable synthesis — a materials engineering challenge as formidable as the fundamental physics.
