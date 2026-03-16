---
id: analytical-selectivity-and-specificity
title: 'Analytical Selectivity and Specificity: Method Discrimination'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: analytical-chemistry-intro
  type: hard
- id: analyte-identification-interferences
  type: hard
builds-toward:
- analytical-method-validation-core-parameters
tags:
- selectivity
- specificity
- interferences
- interference-removal
stage: advanced
status: draft
---

# Analytical Selectivity and Specificity: Method Discrimination

## Core Idea
Specificity measures an analytical method's ability to uniquely identify and measure the target analyte in the presence of expected sample components (matrix and potential interferents). High selectivity is essential for accurate quantitation in complex matrices where the method must distinguish the analyte from potential interferences.

## How It's Best Learned
Design method discrimination studies by spiking known interferents and evaluating signal separation and recovery.

## Common Misconceptions
Assuming selectivity and specificity are identical. Believing a clean standard solution signal proves selectivity—must test with matrix present.

## Explainer

When you measure an analyte in a real sample, you are never looking at the analyte alone. The sample contains dozens or hundreds of other compounds — the **matrix** — and some of those compounds may produce signals that overlap with or distort the signal from your target. Selectivity and specificity describe how well your analytical method can tell the analyte apart from everything else in the sample. From your work on analyte identification and interferences, you already know that interferents can cause false signals. Selectivity and specificity formalize how you evaluate and quantify that discrimination ability.

**Specificity** is the stronger claim: a perfectly specific method responds to only the target analyte and nothing else. In practice, true specificity is rare. Most methods have some degree of **selectivity** — they can distinguish the analyte from many but not necessarily all potential interferents. Think of it like tuning a radio: a highly selective receiver picks up your station clearly even when nearby frequencies are broadcasting, while a perfectly specific receiver would only ever detect a single frequency. The distinction matters because regulatory agencies (FDA, ICH, EPA) require you to demonstrate that your method can handle the specific interferences present in your sample type, not just work in clean solvent.

To evaluate selectivity, you run deliberate experiments called **discrimination studies**. The standard approach is to analyze blank matrix samples (everything except the analyte), blank matrix spiked with the analyte, and blank matrix spiked with known interferents both alone and together with the analyte. You then compare the signals: does the analyte peak shift, broaden, or change in area when interferents are present? Does a blank matrix produce any signal at the analyte's retention time or wavelength? If the analyte signal remains clean and quantitatively unchanged in the presence of matrix components, the method demonstrates acceptable selectivity for that matrix.

A critical mistake is testing selectivity only in pure solvent standards. A method that gives a beautiful, sharp peak for your analyte dissolved in methanol tells you nothing about how that peak behaves in blood plasma, river water, or soil extract. The matrix itself is the challenge — co-eluting compounds can suppress ionization in mass spectrometry, absorb at overlapping wavelengths in UV detection, or co-precipitate in gravimetric methods. This is why method validation protocols always require selectivity testing in the actual sample matrix, using representative blank samples that contain all expected components except the analyte.
