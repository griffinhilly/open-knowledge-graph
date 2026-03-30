---
id: heterogeneous-catalysis-metal-surfaces
title: Heterogeneous Catalysis on Metal Surfaces
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: solid-state-chemistry-fundamentals
  type: hard
- id: catalytic-cycles-wilkinson-grubbs
  type: soft
builds-toward: []
tags:
- heterogeneous catalysis
- surface chemistry
- chemisorption
- Haber-Bosch
- Sabatier principle
- volcano plot
stage: expert
status: validated
---

# Heterogeneous Catalysis on Metal Surfaces

## Core Idea
Heterogeneous catalysis occurs at the interface between a solid catalyst (typically a transition metal or metal oxide) and gas-phase or liquid-phase reactants. Substrates adsorb onto the surface (chemisorption), undergo bond-breaking and bond-making at active sites (often under-coordinated metal atoms at steps, edges, and defects), and desorb as products. The Sabatier principle and volcano plots correlate catalytic activity with the strength of substrate-surface interaction, providing a rational framework for catalyst selection and design.

## Questions

```yaml
- question: "The Haber-Bosch process for ammonia synthesis (N₂ + 3H₂ → 2NH₃) uses iron as the catalyst. Why is iron near the peak of the volcano plot for this reaction?"
  type: multiple-choice
  options:
    - "Iron is the cheapest transition metal available in industrial quantities"
    - "Iron binds N₂ strongly enough to dissociate the N≡N triple bond but not so strongly that the nitrogen atoms cannot be hydrogenated and the product NH₃ cannot desorb — it balances the competing requirements of activation and product release"
    - "Iron has the highest surface area of any metal"
    - "Iron is the most electronegative transition metal, enabling it to donate electrons to nitrogen"
  answer: 1
  explanation: "The Sabatier principle states that optimal catalysis requires intermediate binding strength. For ammonia synthesis, the rate-limiting step changes across the volcano plot: metals that bind N₂ too weakly (like Cu, Ag) cannot dissociate the extremely strong N≡N triple bond (945 kJ/mol). Metals that bind nitrogen too strongly (like Mo, W) can dissociate N₂ but hold the nitrogen atoms so tightly that hydrogenation and NH₃ desorption become prohibitively slow. Iron sits near the peak — it dissociates N₂ with modest activation energy and releases NH₃ at a practical rate. Ruthenium is actually slightly better but too expensive for industrial use."

- question: "Chemisorption involves the formation of chemical bonds between the adsorbate and the metal surface, while physisorption involves only weak van der Waals interactions."
  type: true-false
  answer: true
  explanation: "The distinction between chemisorption and physisorption is fundamental to heterogeneous catalysis. Chemisorption involves the formation of genuine chemical bonds (covalent or ionic) between the substrate and surface metal atoms, with adsorption energies typically 40-400 kJ/mol. The substrate's electronic structure is significantly perturbed, often leading to bond weakening or dissociation. Physisorption involves only van der Waals forces (5-40 kJ/mol), is non-specific, and does not significantly alter the substrate's bonds. Only chemisorption activates substrates for catalytic reaction. The d-band model (Hammer and Norskov) explains trends in chemisorption strength across the transition metals."

- question: "The d-band center model predicts that metals with d-band centers closer to the Fermi level will have stronger chemisorption of adsorbates."
  type: true-false
  answer: true
  explanation: "The Hammer-Norskov d-band model provides a simple electronic structure explanation for trends in chemisorption. When an adsorbate orbital interacts with the metal d-band, it forms bonding and antibonding states. If the d-band center is high (close to the Fermi level), more of the antibonding states lie above the Fermi level and are empty — resulting in stronger net bonding (more bonding electrons, fewer antibonding). If the d-band center is low (far below the Fermi level), the antibonding states are filled, weakening the bond. This model explains why early transition metals (high d-band center) bind adsorbates strongly while late transition metals (low d-band center) bind weakly, and it provides the electronic-structure basis for the volcano plot."

- question: "Explain why heterogeneous catalysts are often prepared as nanoparticles on a support rather than as bulk metal, and describe two properties of nanoparticles that enhance catalytic activity."
  type: short-answer
  answer: "Nanoparticles maximize the fraction of metal atoms exposed at the surface (the surface-to-volume ratio increases as particle size decreases). A 2 nm nanoparticle has ~50% of its atoms on the surface, while a 20 nm particle has only ~5%. Since catalysis occurs exclusively at the surface, smaller particles provide more active sites per gram of metal. Two additional properties enhance activity: (1) Nanoparticles have a high density of under-coordinated atoms at edges, corners, and steps — these low-coordination sites bind adsorbates more strongly and often have lower activation barriers for bond-breaking. (2) The electronic structure of nanoparticles differs from bulk metal — quantum confinement and surface effects shift the d-band center, tuning adsorption strengths. The support (typically alumina, silica, or carbon) prevents nanoparticles from sintering (aggregating into larger, less active particles) at reaction temperatures."
  explanation: "This is why modern heterogeneous catalyst development focuses on controlling nanoparticle size, shape, and composition. Single-atom catalysts (isolated metal atoms on a support) represent the extreme limit, maximizing atom efficiency and offering unique selectivity due to their distinctive electronic environment."
```

## Explainer

Heterogeneous catalysis is the workhorse of the chemical industry — responsible for producing fuels, fertilizers, polymers, and commodity chemicals on scales of millions of tons per year. The catalyst is a solid (typically a transition metal, metal oxide, or metal sulfide), and the reactants are gases or liquids that interact with the catalyst surface. Understanding these surface reactions requires combining the principles of coordination chemistry with the physics of surfaces and the thermodynamics of adsorption.

The catalytic cycle on a surface parallels the homogeneous catalytic cycle in concept but differs in execution. A molecule from the gas phase approaches the surface and adsorbs — either weakly (physisorption) or strongly with bond formation (chemisorption). Chemisorbed species can diffuse along the surface, encounter other adsorbed species or surface sites, undergo bond-breaking and bond-making, and eventually desorb as products. The surface provides the same functions as a homogeneous catalyst: it activates substrates by weakening bonds, brings reactants into proximity, and provides a reaction pathway with lower activation energy than the uncatalyzed process.

The Sabatier principle — optimal catalysis requires intermediate binding strength — is the organizing framework for heterogeneous catalyst selection. For any reaction, plotting catalytic activity against the binding strength of a key intermediate produces a volcano-shaped curve. Metals that bind too weakly cannot activate the substrate (left side of the volcano). Metals that bind too strongly cannot release the product (right side). The best catalysts sit near the peak, balancing activation and release. The Haber-Bosch process for ammonia synthesis is the classic example: iron sits near the volcano peak for nitrogen binding, which is why it catalyzes the most important industrial chemical reaction (enabling the fertilizer production that feeds half the world's population).

Modern computational catalysis uses density functional theory (DFT) to predict binding energies on specific metal surfaces, constructing theoretical volcano plots that guide catalyst discovery without exhaustive experimental screening. The d-band center model provides the physical insight: the position of the metal d-band relative to the Fermi level determines how strongly adsorbates bind, and this position varies systematically across the transition metals and can be tuned by alloying, nanostructuring, or using bimetallic catalysts. This computational-experimental feedback loop has accelerated catalyst development for energy applications — including electrocatalysts for fuel cells, CO₂ reduction, and water splitting — where finding the right metal or alloy to sit at the volcano peak is the central design challenge.
