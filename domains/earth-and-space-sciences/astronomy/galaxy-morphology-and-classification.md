---
id: galaxy-morphology-and-classification
title: Galaxy Morphology and Classification
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: stellar-evolution-main-sequence-to-giant
  type: soft
- id: stellar-parallax-and-distance
  type: soft
builds-toward:
- milky-way-structure
- active-galactic-nuclei
- hubble-law-and-cosmic-expansion
tags:
- Hubble-tuning-fork
- elliptical-galaxies
- spiral-galaxies
- barred-spirals
- irregular-galaxies
- lenticular-galaxies
stage: formal-systems
status: validated
---

# Galaxy Morphology and Classification

## Core Idea
Galaxies are gravitationally bound systems of stars, gas, dust, and dark matter ranging from dwarf galaxies with millions of stars to giant ellipticals with trillions. Hubble's tuning-fork diagram classifies galaxies into ellipticals (E0–E7, spherical to flattened), lenticulars (S0), spirals (Sa–Sd, with winding arms), and barred spirals (SBa–SBd). Ellipticals contain mostly old stars and little cold gas; spirals have active star formation in their arms. Irregular galaxies lack symmetry, often due to tidal interactions or mergers. Morphology correlates with environment: ellipticals dominate dense galaxy cluster cores.

## How It's Best Learned
Classify a sample of galaxy images from SDSS or the Galaxy Zoo citizen science database using Hubble's scheme. Study real examples of interacting galaxies (Antennae, Mice) to understand how mergers distort morphology.

## Common Misconceptions
- Hubble's tuning-fork is not an evolutionary sequence; galaxies do not evolve from irregulars to ellipticals along the diagram.
- Elliptical galaxies are not simpler than spirals — they often contain complex stellar kinematics built up through multiple mergers.

## Questions

```yaml
- question: "An astronomy student learns that Hubble labeled elliptical galaxies 'early-type' and spirals 'late-type.' She concludes that galaxies begin as spirals and evolve into ellipticals over cosmic time. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The terminology is inverted — Hubble actually labeled spirals as early-type and ellipticals as late-type"
    - "The Hubble tuning-fork is a morphological classification of present appearance, not an evolutionary sequence; 'early' and 'late' were arbitrary labels. Modern evidence shows mergers of spirals can produce ellipticals — the opposite direction from the student's assumption"
    - "The student is correct — observations confirm that galaxies gradually develop spiral arms as they age and then lose them to become ellipticals"
    - "The tuning-fork diagram cannot be used to make any inferences about galaxy evolution"
  answer: 1
  explanation: "Hubble's 'early-type' and 'late-type' labels were not intended to describe an evolutionary sequence — they were descriptive names for positions in a classification diagram. Modern galaxy formation theory and observations indicate that ellipticals often form through mergers of spiral galaxies, which is the reverse of what the student assumed. The tuning-fork organizes visual morphology, not evolutionary history."

- question: "A galaxy survey finds that dense cluster cores are dominated by elliptical and lenticular galaxies, while the outskirts and field regions contain many more spirals. Which explanation best accounts for this morphology-density relation?"
  type: multiple-choice
  options:
    - "Spiral galaxies form in cluster cores and gradually migrate outward over time"
    - "The early universe produced different galaxy types in different-density regions purely by chance, and those initial populations have been preserved"
    - "Dense cluster environments actively transform galaxies: tidal stripping, ram-pressure removal of cold gas, and frequent mergers convert gas-rich spirals into gas-poor, star-formation-quenched ellipticals and lenticulars"
    - "Elliptical galaxies require neighboring galaxies to be detectable, so they only appear to dominate in dense regions"
  answer: 2
  explanation: "The morphology-density relation reflects ongoing environmental transformation, not just initial conditions. Cluster environments actively strip gas from spirals (removing star-formation fuel via ram pressure), strip stars from outer disks through tidal interactions, and cause frequent galaxy-galaxy mergers that destroy spiral structure and build spheroidal systems. This predicts that gas-poor, red ellipticals should dominate cluster cores — exactly what is observed."

- question: "Elliptical galaxies are structurally simpler than spirals because they lack spiral arms, dust lanes, and ongoing star formation."
  type: true-false
  answer: false
  explanation: "Elliptical galaxies can have highly complex internal kinematics built up through multiple merger events. Some contain counterrotating stellar cores, kinematically distinct components, or shell structures from past accretion events. Their smooth appearance belies complicated formation histories. The absence of visible arms and dust does not mean structural simplicity — it means the gas has been consumed or removed and the stellar orbits have been randomized through mergers."

- question: "Moving from Sa to Sd along the spiral branch of the Hubble tuning-fork, the central bulge becomes smaller and the spiral arms become more open and prominent."
  type: true-false
  answer: true
  explanation: "This is a genuine morphological trend along the spiral sequence. Sa galaxies have a large dominant bulge and tightly wound, smooth arms; Sd galaxies have a tiny or absent bulge, loosely wound arms, and prominent knots of active star formation. The fraction of blue, young stars also increases from a to d. This correlation between bulge size and arm winding is one of the real structural trends that the Hubble classification captures."

- question: "Why do spiral galaxies have ongoing star formation in their arms while elliptical galaxies do not, and how does this relate to their morphological differences?"
  type: short-answer
  answer: "Spiral arms contain abundant cold molecular gas and dust — the raw material for star formation. When gas clouds reach sufficient density, they collapse gravitationally to form new stars. Elliptical galaxies have little cold gas remaining: it was either consumed in earlier intense star-formation episodes, expelled by supernovae and AGN feedback, or stripped away by environmental processes in galaxy clusters. Without cold gas, new stars cannot form. The morphological difference — ordered disk with arms versus smooth spheroid — thus directly reflects the difference in gas content and star-formation history."
  explanation: "This connection between morphology and star-formation activity also explains the color difference: spirals appear bluer (young, hot stars in the arms) while ellipticals appear redder (old, cool stars from long-past formation). Morphology, color, and star-formation rate are all correlated because they all trace the same underlying property: available cold gas."
```

## Explainer

When you look at images of galaxies, the most immediately striking feature is their shape. Some are smooth, featureless ellipses; others have dramatic spiral arms winding outward from a central bulge; still others are chaotic, irregular smears of light. **Galaxy morphology** is the systematic classification of these shapes, and the organizing framework that has endured since the 1920s is Edwin Hubble's **tuning-fork diagram**.

The tuning fork splits galaxies into two main sequences that branch from a common point. On the left sit **elliptical galaxies**, labeled E0 through E7 based on how elongated they appear (E0 is nearly circular, E7 is highly flattened). Ellipticals are dominated by old, red stars and contain very little cold gas or dust, meaning they have largely stopped forming new stars. At the fork's junction sit **lenticular galaxies** (S0), which have a central bulge and a disk like spirals but lack prominent spiral arms — they are transitional in appearance. The two prongs of the fork represent **normal spirals** (Sa through Sd) and **barred spirals** (SBa through SBd), where a linear bar of stars extends through the center. Moving from "a" to "d" along either branch, the central bulge gets smaller, the spiral arms become more open and prominent, and the fraction of young blue stars increases.

Beyond the tuning fork, **irregular galaxies** lack the symmetry of any Hubble type. Many irregulars are small, gas-rich systems (like the Magellanic Clouds), while others have been distorted by gravitational interactions — galaxy mergers and tidal encounters can warp spirals into unrecognizable shapes. The Antennae Galaxies, two spirals in the process of colliding, show dramatic tidal tails and triggered bursts of star formation that defy simple classification. Morphology is therefore not static; it evolves as galaxies interact and merge over cosmic time.

An important pattern connects morphology to environment. Galaxy clusters — dense concentrations of hundreds or thousands of galaxies — are dominated by ellipticals and lenticulars in their cores, while spirals are more common in the less crowded outskirts and in the general field. This **morphology-density relation** suggests that the cluster environment transforms galaxies: tidal stripping, ram-pressure removal of gas, and frequent mergers can convert gas-rich spirals into gas-poor ellipticals. Understanding why galaxies look the way they do is therefore inseparable from understanding the environments they inhabit and the histories they have lived through.
