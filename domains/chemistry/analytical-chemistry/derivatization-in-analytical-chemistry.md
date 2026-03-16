---
id: derivatization-in-analytical-chemistry
title: Derivatization in Analytical Chemistry
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: functional-groups-overview
  type: hard
tags:
- derivatization
- chemical modification
stage: advanced
status: draft
---

# Derivatization in Analytical Chemistry

## Core Idea
Derivatization chemically modifies analytes to enhance detection sensitivity, selectivity, or separation. Common strategies include silylation for GC, acylation for UV-active tags, and fluorescent labeling for sensitive detection.

## How It's Best Learned
Study derivatization reagent reactivity and product properties; consider yield, selectivity, and side reactions when designing analytical derivatization schemes.

## Explainer

Your knowledge of functional groups is the foundation here — derivatization is fundamentally about exploiting the reactivity of specific functional groups to attach something analytically useful to the analyte. The analyte itself may be perfectly real and present in your sample, but if the instrument cannot see it well enough to measure it accurately, you need to change the analyte's chemical properties before analysis. Derivatization is the controlled chemical transformation that bridges this gap.

Consider amino acids, which are polar, non-volatile, and absorb UV light weakly. Gas chromatography requires volatile analytes, so amino acids cannot be injected directly into a GC. **Silylation** — replacing active hydrogens (–OH, –NH, –COOH) with trimethylsilyl (TMS) groups — converts amino acids into volatile, thermally stable derivatives that chromatograph beautifully on GC columns. The TMS group is bulky and nonpolar, which raises vapor pressure and eliminates hydrogen bonding that would otherwise cause tailing or adsorption. This is derivatization for *separation*: the analyte's identity is preserved in the mass spectrum, but its physical properties are transformed to suit the instrument.

Derivatization for *detection* works differently. If you need to measure picomolar concentrations of a primary amine in a biological fluid, attaching a **fluorescent tag** like dansyl chloride or o-phthalaldehyde (OPA) to the amine group converts it from an analytically invisible compound into one that fluoresces brilliantly when excited at the right wavelength. Fluorescence detection is often 100 to 1,000 times more sensitive than UV absorption, so the derivatization step directly determines whether the analysis succeeds or fails. Similarly, **acylation** with reagents like pentafluorobenzoyl chloride creates derivatives with high electron-capture detector (ECD) response, enabling ultra-sensitive detection of hydroxyl- or amine-containing compounds.

The practical challenge is that derivatization adds a sample preparation step that introduces its own sources of error. The reaction must go to completion (or at least to a reproducible extent), side products must not interfere with the analyte peak, and excess reagent must be removed or must elute away from the peaks of interest. Incomplete derivatization produces two peaks for the same analyte — derivatized and underivatized — splitting the signal and ruining quantitation. This is why analytical derivatization protocols specify precise reaction conditions: temperature, time, solvent, reagent excess, and pH. Each parameter targets a specific functional group reaction, and your understanding of how functional groups react under different conditions is exactly what lets you predict whether a derivatization scheme will work for a new analyte or need modification.
