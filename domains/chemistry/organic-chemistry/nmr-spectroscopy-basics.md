---
id: nmr-spectroscopy-basics
title: NMR Spectroscopy Basics
domain: chemistry
course: organic-chemistry
prerequisites:
- id: organic-chemistry-intro
  type: hard
- id: atomic-structure-basics
  type: soft
builds-toward:
- ir-spectroscopy-basics
tags:
- NMR
- spectroscopy
- chemical shift
- splitting
- integration
- structure determination
- 1H NMR
- 13C NMR
stage: formal-systems
status: draft
---

# NMR Spectroscopy Basics

## Core Idea
Nuclear Magnetic Resonance (NMR) spectroscopy exploits the quantum spin properties of atomic nuclei (especially ¹H and ¹³C) in an external magnetic field to provide detailed structural information. In ¹H NMR, the chemical shift (in ppm, referenced to TMS at 0 ppm) encodes the electronic environment of each proton — deshielded protons (near electronegative groups or in aromatic rings) resonate at higher ppm values. Integration gives the relative count of equivalent protons in each environment, and the splitting pattern (multiplet structure following the n+1 rule) reveals the number of adjacent non-equivalent protons. Together, these three features allow unambiguous structural assignment.

## How It's Best Learned
Work through ¹H NMR spectra of simple known molecules (ethanol, acetone, diethyl ether) before tackling unknowns. For each spectrum: first count signals (distinct environments), then use integration for H counts, then decode splitting. Sketch expected shift ranges: CH₃ (~1 ppm), vinyl (~5–6 ppm), aromatic (~7–8 ppm), aldehyde (~9–10 ppm), carboxylic acid (~11–12 ppm).

## Common Misconceptions
- Chemical shift values are not absolute — they are relative to TMS and can shift slightly with solvent, concentration, and temperature.
- The n+1 rule applies only to magnetically non-equivalent neighboring protons and assumes first-order coupling; complex molecules show higher-order patterns.
- ¹³C NMR spectra are typically broad-band decoupled and individual peak heights are NOT proportional to the number of carbons.
