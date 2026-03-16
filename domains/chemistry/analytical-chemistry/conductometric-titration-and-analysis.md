---
id: conductometric-titration-and-analysis
title: Conductometric Titration and Analysis
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: conductometry
  type: hard
- id: titrimetric-analysis-intro
  type: soft
builds-toward:
- analytical-method-validation-core-parameters
tags:
- conductometry
- titration
- conductivity
- endpoint-detection
stage: advanced
status: draft
---

# Conductometric Titration and Analysis

## Core Idea
Conductometric titration detects the equivalence point by measuring solution conductivity changes as ions are titrated. This non-specific method works for any ion-forming reaction and doesn't require indicators, making it valuable for colored samples, turbid solutions, and systems where traditional indicators fail.

## How It's Best Learned
Perform conductometric titrations on samples unsuitable for indicator-based methods (colored solutions, precipitation reactions).

## Common Misconceptions
Assuming conductivity changes linearly throughout the titration (the relationship depends on the relative conductances of reactants and products). Neglecting temperature effects on conductivity measurements.

## Explainer

In a conventional titration, you watch for a color change from an indicator dye to signal the equivalence point. But what if your solution is already deeply colored, or turbid, or the reaction has no suitable indicator? **Conductometric titration** solves this by tracking the solution's electrical conductivity instead. Since ions carry current through solution, and different ions carry current at different rates, the total conductivity changes as the titration reaction replaces one set of ions with another. By plotting conductivity against the volume of titrant added, you can locate the equivalence point from the intersection of two straight-line segments — no indicator needed.

The key to understanding conductometric titrations is remembering that different ions have different **molar conductivities**. From your conductometry prerequisite, you know that H⁺ and OH⁻ are exceptionally fast charge carriers — roughly five to ten times more conductive than typical ions like Na⁺ or Cl⁻. This means that titrations involving strong acids or strong bases produce dramatic conductivity changes. For example, when you titrate HCl with NaOH, each addition of NaOH replaces a highly conductive H⁺ ion with a much less conductive Na⁺ ion. Conductivity drops steeply until the equivalence point, then rises as excess OH⁻ (also highly conductive) accumulates. The V-shaped curve makes the equivalence point unmistakable.

The shape of the conductivity curve depends entirely on which ions are being consumed and which are being produced. A strong acid–strong base titration gives a sharp V. A weak acid–strong base titration gives a curve that initially drops gently (because the weak acid is barely ionized, contributing little conductivity) then rises steeply after the equivalence point. **Precipitation titrations** work beautifully by conductometry — when you titrate Ba²⁺ with SO₄²⁻, the conducting ions precipitate out as insoluble BaSO₄, causing conductivity to drop until the equivalence point and then rise as excess sulfate ions remain in solution.

One practical advantage of conductometric titrations is that you do not need data points right at the equivalence point. Because the equivalence point is found by extrapolating two linear segments to their intersection, you only need enough points on either side of the equivalence point to define the lines. This makes the method tolerant of slow equilibration near the endpoint — a common problem in precipitation and complexometric titrations. However, you must control temperature carefully, since conductivity is strongly temperature-dependent (roughly 2% per degree Celsius), and you should minimize dilution effects by using a concentrated titrant so the total volume change stays small relative to the sample volume.
