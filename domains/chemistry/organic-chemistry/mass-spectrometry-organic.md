---
id: mass-spectrometry-organic
title: Mass Spectrometry in Organic Chemistry
domain: chemistry
course: organic-chemistry
prerequisites:
- id: organic-chemistry-intro
  type: hard
- id: nmr-spectroscopy-basics
  type: soft
- id: lorentz-force-complete-em
  type: soft
- id: lorentz-force-on-moving-charge
  type: soft
- id: coulomb-force-superposition
  type: soft
- id: mass-energy-equivalence
  type: soft
- id: ion-formation-from-electron-transfer
  type: soft
builds-toward: []
tags:
- mass spectrometry
- molecular ion
- fragmentation
- McLafferty rearrangement
- isotope pattern
- M+1
- base peak
stage: advanced
status: draft
---
# Mass Spectrometry in Organic Chemistry

## Core Idea
Mass spectrometry measures the mass-to-charge ratio of ionized molecules and their fragments, providing the molecular weight and structural clues for organic compounds. The molecular ion peak (M+) gives the exact molecular mass; its even/odd value indicates whether the molecule contains an odd or even number of nitrogen atoms (the nitrogen rule). Fragmentation patterns reveal structural features: the molecule breaks at weak bonds and at positions that generate stable cations (benzylic, allylic, adjacent to heteroatoms). The McLafferty rearrangement — a characteristic gamma-hydrogen transfer followed by bond cleavage — is diagnostic for carbonyl compounds with a gamma-hydrogen. Isotope patterns (especially the M+2 peak from Cl and Br) identify the presence and number of halogens.

## How It's Best Learned
Start by interpreting simple spectra: find the molecular ion, apply the nitrogen rule, then identify the base peak and major fragments. Calculate mass losses (M - 15 = loss of CH3, M - 18 = loss of H2O, M - 29 = loss of CHO) to identify what departed. Practice recognizing the McLafferty rearrangement in spectra of ketones and esters. Compare spectra of isomers to see how fragmentation distinguishes structures that have the same molecular weight.

## Common Misconceptions
- The molecular ion peak is not always the tallest peak (base peak) — the base peak is the most abundant fragment, which may have a completely different mass.
- The M+1 peak is primarily due to 13C, not to a protonated molecular ion; its intensity relative to M+ helps estimate the number of carbons.
- Mass spectrometry does not directly reveal functional groups the way IR does — it shows fragments and masses. Structural assignment usually requires combining MS data with IR, NMR, and other spectroscopic methods.

## Questions

```yaml
- question: "A mass spectrum shows a molecular ion at m/z = 136 with an M+2 peak approximately one-third the height of M+. Which element is most likely present?"
  type: multiple-choice
  options:
    - "Carbon (due to 13C isotope)"
    - "Chlorine (35Cl/37Cl)"
    - "Bromine (79Br/81Br)"
    - "Nitrogen"
  answer: 1
  explanation: "Chlorine has two major isotopes: 35Cl (75%) and 37Cl (25%), giving M:M+2 intensity ratio of approximately 3:1, so M+2 is about one-third of M+. Bromine's isotopes (79Br and 81Br) are nearly equal in abundance, giving M:M+2 ≈ 1:1. Carbon-13 produces a small M+1 peak, not M+2. The distinctive M+2 isotope pattern is one of the most reliable indicators of halogen presence in a mass spectrum."

- question: "The base peak in a mass spectrum always corresponds to the molecular ion (M+)."
  type: true-false
  answer: false
  explanation: "The base peak is simply the most abundant (tallest) peak in the spectrum and is used as the 100% reference. It can be any fragment — in many compounds the molecular ion fragments so readily that M+ has very low abundance or is absent entirely. The base peak must be identified by its m/z value. For example, in many branched alkanes the molecular ion is weak and a stable carbenium ion fragment is the base peak."

- question: "A compound produces a molecular ion at m/z = 57 (odd mass). What does this tell you about the compound's nitrogen content, and why does this rule hold?"
  type: short-answer
  answer: "An odd molecular mass indicates the compound contains an odd number of nitrogen atoms (one, three, etc.). This is the nitrogen rule: nitrogen is the only common organic element whose most abundant isotope has an even mass (14) but an odd valence (3), causing each nitrogen to shift the molecular mass by an odd net amount."
  explanation: "For molecules containing only C, H, O, S, and halogens, all of which have even-mass isotopes and even valences, the molecular mass is always even. Each nitrogen (mass 14, valence 3) behaves differently: adding a nitrogen to a molecular formula adds 14 (even) in mass but also forces the H count to adjust by an odd amount due to valence bookkeeping, producing an overall odd shift. The rule is simple and reliable: odd M+ = odd number of nitrogens."
```

## Explainer

Mass spectrometry works by ionizing molecules — typically by bombarding them with high-energy electrons (electron ionization, EI) — which knocks out one electron to produce a radical cation M⁺•, the molecular ion. This molecular ion is then accelerated through a magnetic or electric field, and because different masses curve differently, the detector separates ions by their mass-to-charge ratio (m/z). The resulting spectrum is essentially a bar chart: each peak is a fragment (or the intact molecular ion) at a specific m/z value, and the height reflects how abundant that fragment is.

The molecular ion peak gives you the molecular mass directly — one of the most fundamental pieces of structural information. But M⁺ is not always visible: in compounds that fragment easily (especially branched alkanes or alcohols), the molecular ion is unstable and may be nearly absent. If you see no peak at the highest m/z, consider that M⁺ may be very small or absent, and look for characteristic fragments. The base peak is the tallest peak (100% reference), but it could be any fragment, not M⁺.

Fragmentation is not random — it follows rules that reflect bond strengths and carbocation stability. Molecules break preferentially at weak bonds (such as C–C bonds adjacent to heteroatoms or double bonds) and at positions that generate stable cations (tertiary carbocations, benzylic/allylic cations, acylium ions). Learning the common mass losses — 15 (−CH₃), 18 (−H₂O), 29 (−CHO or −C₂H₅), 31 (−OCH₃) — lets you read a spectrum as a structural puzzle: the difference between M⁺ and the base peak tells you what left the molecule.

Two special features deserve attention. First, the nitrogen rule: if the molecular ion has an odd mass, the molecule contains an odd number of nitrogen atoms (one, three, etc.); an even mass means zero or an even number. This is a fast filter before any detailed analysis. Second, isotope patterns: chlorine (75% ³⁵Cl, 25% ³⁷Cl) gives a distinctive M+2 peak about one-third the height of M⁺; bromine (approximately 50/50) gives M and M+2 peaks of nearly equal height. Spotting these patterns immediately tells you whether halogens are present, and the relative intensities can count the number of halogen atoms.

Mass spectrometry is rarely used alone in structural determination — it is most powerful in combination with IR (which identifies functional groups) and NMR (which maps connectivity). The MS provides molecular weight and fragmentation clues; IR confirms functional groups; NMR resolves the carbon skeleton. Together they reduce an unknown compound to a small set of candidates that can often be confirmed against databases of known spectra.
