---
id: structure-elucidation-using-ir-nmr-and-ms
title: Structure Elucidation Using IR, NMR, and Mass Spectrometry
domain: chemistry
course: organic-chemistry
prerequisites:
- id: ir-spectroscopy-basics
  type: hard
- id: nmr-spectroscopy-basics
  type: hard
- id: mass-spectrometry-organic
  type: hard
builds-toward:
- retrosynthetic-analysis
tags:
- structure-determination
- spectroscopy
- ir-frequencies
- nmr-signals
- mass-fragmentation
stage: formal-systems
status: validated
---

# Structure Elucidation Using IR, NMR, and Mass Spectrometry

## Core Idea
Organic structures are determined by integrating data from multiple spectroscopic techniques: IR identifies functional groups via characteristic absorption frequencies; NMR (¹H and ¹³C) reveals connectivity and multiplicity patterns; mass spectrometry provides molecular weight and fragmentation patterns indicating functional groups and structure. Systematic analysis using degree of unsaturation, molecular formula, and spectroscopic clues yields the unique structure.

## Questions

```yaml
- question: "A compound has molecular formula C₄H₈O (degree of unsaturation = 1). The IR shows a carbonyl peak at 1715 cm⁻¹ with no O–H or N–H absorption. The ¹H NMR shows a triplet (3H) near 1.1 ppm, a quartet (2H) near 2.4 ppm, and a singlet (3H) near 2.1 ppm. What functional group is most consistent with all three pieces of evidence?"
  type: multiple-choice
  options:
    - "Ketone (methyl ethyl ketone)"
    - "Aldehyde"
    - "Carboxylic acid"
    - "Ester"
  answer: 0
  explanation: "Absence of O–H stretch rules out carboxylic acid; absence of a ~9.5 ppm CHO signal rules out aldehyde. The triplet/quartet pattern indicates an ethyl group (–CH₂CH₃), and the singlet is an adjacent methyl. Together: CH₃CO–CH₂CH₃ (methyl ethyl ketone), which matches the carbonyl at 1715 cm⁻¹ and C₄H₈O formula. The misconception is guessing aldehyde simply because a carbonyl is present — NMR would show a distinctive downfield singlet (~9.5 ppm) for CHO, which is absent here."

- question: "Which combination of spectroscopic evidence best confirms the presence of an aromatic ring in an unknown compound?"
  type: multiple-choice
  options:
    - "A carbonyl absorption at 1700 cm⁻¹ and an NMR singlet between 7–9 ppm"
    - "A degree of unsaturation of 4, IR absorptions at 1600 and 1500 cm⁻¹, and NMR signals between 7–8 ppm integrating for 5H"
    - "A molecular ion at m/z = 78 in the mass spectrum alone"
    - "A ¹³C NMR signal between 120–150 ppm alone"
  answer: 1
  explanation: "The convergence of multiple lines of evidence is required. DoU = 4 is necessary for a benzene ring (3 double bonds + 1 ring). The 1600/1500 cm⁻¹ IR absorptions are diagnostic for aromatic C=C stretches. The NMR signals at 7–8 ppm integrating for 5H are characteristic of a monosubstituted arene. A single technique (options C or D) can be consistent with multiple structures; only integration rules out alternatives."

- question: "The absence of a broad O–H stretch in the IR spectrum rules out any carbonyl-containing functional group."
  type: true-false
  answer: false
  explanation: "Several carbonyl-containing functional groups lack O–H stretches: ketones, aldehydes, and esters all show C=O absorptions without any O–H. An O–H stretch is diagnostic for carboxylic acids and alcohols, but its absence simply narrows the field — it does not rule out carbonyl groups generally. The IR alone distinguishes functional groups by the combination of which absorptions are present AND absent."

- question: "The degree of unsaturation cannot distinguish between a compound containing one ring and no double bonds versus one containing no rings but one double bond."
  type: true-false
  answer: true
  explanation: "Both a ring and a double bond each contribute exactly one degree of unsaturation. A DoU of 1 means 'one ring or one double bond,' not which one. Distinguishing between them requires other evidence: a C=C or C=O stretch in the IR would indicate a double bond, while NMR connectivity patterns can reveal ring structures. This is precisely why structure elucidation requires integrating all techniques."

- question: "Why is it necessary to verify a proposed structure against all spectroscopic data, rather than stopping once a structure consistent with one technique has been identified?"
  type: short-answer
  answer: "Each spectroscopic technique is consistent with multiple possible structures on its own. A carbonyl in the IR could belong to an aldehyde, ketone, ester, or carboxylic acid. NMR connectivity may fit two different skeletal arrangements. Only the structure that simultaneously satisfies the molecular formula (from MS), functional group pattern (from IR), and connectivity/multiplicity data (from NMR) is the correct answer. A structure that fits one technique but contradicts another must be rejected."
  explanation: "This is the core skill: structure elucidation is an integration problem. Experienced chemists check each proposed structure against every piece of data as a consistency test — not just using each technique to generate candidates independently. Any inconsistency reveals a wrong structure or misinterpreted data."
```

## Explainer

You have already learned each spectroscopic technique individually — IR tells you what functional groups are present, NMR tells you how atoms are connected and what their chemical environments look like, and mass spectrometry tells you the molecular weight and how the molecule breaks apart. Structure elucidation is the art of combining all three into a single coherent picture. Think of it as detective work: each technique gives you different clues, and no single technique alone is usually sufficient to determine a structure unambiguously.

Start every problem the same way. First, extract the **molecular formula** from the mass spectrum (the molecular ion peak M⁺ gives the molecular weight; high-resolution MS can give the exact formula). From the molecular formula, calculate the **degree of unsaturation** (also called index of hydrogen deficiency): DoU = (2C + 2 + N − H − X) / 2 for a formula CₓHᵧNₙOₒXₓ. Each degree of unsaturation represents one ring or one double bond; four degrees of unsaturation strongly suggest an aromatic ring. This single number immediately constrains the possibilities — if DoU = 0, you know the molecule is saturated and acyclic; if DoU = 5, you are probably looking at a substituted benzene ring plus one additional unsaturation.

Next, check the **IR spectrum** for diagnostic absorptions. A broad O–H stretch around 2500–3300 cm⁻¹ with a carbonyl near 1710 cm⁻¹ screams carboxylic acid. A sharp N–H stretch around 3300–3500 cm⁻¹ suggests an amine or amide. A carbonyl at 1735 cm⁻¹ points to an ester, while 1680 cm⁻¹ suggests an amide or conjugated carbonyl. The IR acts as a quick filter — it tells you which functional groups to look for (and which to rule out) before you even touch the NMR data.

The **NMR data** is where the real structural assembly happens. Count the number of distinct ¹H signals and their integrations to determine how many types of hydrogen are present and in what ratio. Chemical shifts tell you the electronic environment: hydrogens near electronegative atoms or pi systems appear downfield (higher ppm). Splitting patterns (the n+1 rule) reveal how many neighboring hydrogens each signal has. ¹³C NMR and DEPT experiments tell you how many distinct carbon environments exist and whether each carbon bears 0, 1, 2, or 3 hydrogens. Piece together fragments by matching splitting patterns to connectivity — if a triplet integrating for 3H appears at 1.2 ppm and a quartet integrating for 2H appears at 4.1 ppm, you are almost certainly looking at an ethyl ester (–OCH₂CH₃).

The final step is **assembling the fragments** into a complete structure that is consistent with all the data. Propose a structure, then verify: does it predict the correct number of NMR signals with the right shifts and splitting? Does it account for every IR absorption? Does it match the molecular formula and degree of unsaturation? If anything does not fit, revise. With practice, this integration becomes rapid — experienced chemists can solve routine structures in minutes by recognizing signature patterns across techniques.
