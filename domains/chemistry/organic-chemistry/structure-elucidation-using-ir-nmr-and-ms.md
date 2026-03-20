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
stage: advanced
status: draft
---

# Structure Elucidation Using IR, NMR, and Mass Spectrometry

## Core Idea
Organic structures are determined by integrating data from multiple spectroscopic techniques: IR identifies functional groups via characteristic absorption frequencies; NMR (¹H and ¹³C) reveals connectivity and multiplicity patterns; mass spectrometry provides molecular weight and fragmentation patterns indicating functional groups and structure. Systematic analysis using degree of unsaturation, molecular formula, and spectroscopic clues yields the unique structure.

## Explainer

You have already learned each spectroscopic technique individually — IR tells you what functional groups are present, NMR tells you how atoms are connected and what their chemical environments look like, and mass spectrometry tells you the molecular weight and how the molecule breaks apart. Structure elucidation is the art of combining all three into a single coherent picture. Think of it as detective work: each technique gives you different clues, and no single technique alone is usually sufficient to determine a structure unambiguously.

Start every problem the same way. First, extract the **molecular formula** from the mass spectrum (the molecular ion peak M⁺ gives the molecular weight; high-resolution MS can give the exact formula). From the molecular formula, calculate the **degree of unsaturation** (also called index of hydrogen deficiency): DoU = (2C + 2 + N − H − X) / 2 for a formula CₓHᵧNₙOₒXₓ. Each degree of unsaturation represents one ring or one double bond; four degrees of unsaturation strongly suggest an aromatic ring. This single number immediately constrains the possibilities — if DoU = 0, you know the molecule is saturated and acyclic; if DoU = 5, you are probably looking at a substituted benzene ring plus one additional unsaturation.

Next, check the **IR spectrum** for diagnostic absorptions. A broad O–H stretch around 2500–3300 cm⁻¹ with a carbonyl near 1710 cm⁻¹ screams carboxylic acid. A sharp N–H stretch around 3300–3500 cm⁻¹ suggests an amine or amide. A carbonyl at 1735 cm⁻¹ points to an ester, while 1680 cm⁻¹ suggests an amide or conjugated carbonyl. The IR acts as a quick filter — it tells you which functional groups to look for (and which to rule out) before you even touch the NMR data.

The **NMR data** is where the real structural assembly happens. Count the number of distinct ¹H signals and their integrations to determine how many types of hydrogen are present and in what ratio. Chemical shifts tell you the electronic environment: hydrogens near electronegative atoms or pi systems appear downfield (higher ppm). Splitting patterns (the n+1 rule) reveal how many neighboring hydrogens each signal has. ¹³C NMR and DEPT experiments tell you how many distinct carbon environments exist and whether each carbon bears 0, 1, 2, or 3 hydrogens. Piece together fragments by matching splitting patterns to connectivity — if a triplet integrating for 3H appears at 1.2 ppm and a quartet integrating for 2H appears at 4.1 ppm, you are almost certainly looking at an ethyl ester (–OCH₂CH₃).

The final step is **assembling the fragments** into a complete structure that is consistent with all the data. Propose a structure, then verify: does it predict the correct number of NMR signals with the right shifts and splitting? Does it account for every IR absorption? Does it match the molecular formula and degree of unsaturation? If anything does not fit, revise. With practice, this integration becomes rapid — experienced chemists can solve routine structures in minutes by recognizing signature patterns across techniques.
