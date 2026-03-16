---
id: food-composition-and-contaminant-analysis
title: Food Composition and Contaminant Analysis
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: analytical-chemistry-intro
  type: hard
- id: chromatography-fundamentals
  type: hard
tags:
- food analysis
- contaminants
- nutrients
stage: advanced
status: draft
---

# Food Composition and Contaminant Analysis

## Core Idea
Food analysis measures nutritional content (vitamins, minerals, macronutrients), additives, and contaminants (pesticides, heavy metals, mycotoxins). Methods must handle complex matrices and meet food safety regulatory thresholds for various analytes.

## Explainer

Food is among the most challenging matrices in analytical chemistry. A single sample of peanut butter, for instance, contains proteins, fats, carbohydrates, water, salts, vitamins, trace minerals, and potentially pesticide residues, mycotoxins, and heavy metals — all at vastly different concentrations. Your foundation in analytical chemistry and chromatography fundamentals prepares you to understand the individual measurement techniques, but food analysis demands that you combine them strategically and account for the unique difficulties that biological matrices create.

**Compositional analysis** determines what is supposed to be in a food product. Protein content is classically measured by the **Kjeldahl method**, which digests all nitrogen-containing compounds and back-calculates protein using a conversion factor — though this famously cannot distinguish protein nitrogen from melamine nitrogen, as the 2008 milk contamination scandal demonstrated. Fat is extracted with organic solvents (Soxhlet extraction), moisture by oven drying or Karl Fischer titration, and minerals by ashing followed by atomic spectroscopy. Vitamins present special challenges because they degrade during extraction; fat-soluble vitamins (A, D, E, K) require saponification to free them from lipid matrices before HPLC separation, while water-soluble vitamins like vitamin C oxidize readily and need antioxidant stabilizers during sample preparation.

**Contaminant analysis** asks a harder question: what should not be present, and is it there at dangerous levels? Pesticide residues are typically screened using the **QuEChERS method** (Quick, Easy, Cheap, Effective, Rugged, and Safe) — a streamlined extraction and cleanup procedure followed by GC-MS or LC-MS/MS analysis that can detect hundreds of pesticides simultaneously at parts-per-billion levels. Heavy metals like lead, cadmium, arsenic, and mercury are measured by ICP-MS or graphite furnace AAS after acid digestion. **Mycotoxins** — toxic metabolites produced by molds on grains, nuts, and dried fruits — require immunoaffinity column cleanup to isolate them from the complex food matrix before chromatographic quantitation. Each contaminant class has regulatory limits set by agencies like the FDA, EU Commission, and Codex Alimentarius, and methods must be validated to demonstrate they can reliably detect analytes at or below these thresholds.

The common thread across all food analysis is **matrix effects** — the ways in which the sample itself interferes with your measurement. A fatty matrix can suppress ionization in a mass spectrometer, a high-sugar matrix can co-elute with target peaks in chromatography, and pigmented foods can interfere with spectroscopic detection. Overcoming these effects requires careful method validation using matrix-matched calibration standards or standard addition, recovery studies to verify that sample preparation does not lose analyte, and proficiency testing against certified reference materials. The analyst must think about the entire workflow — from how the sample was collected in the field, through grinding and homogenization, extraction and cleanup, to final instrumental measurement — because error introduced at any stage propagates through to the reported result.
