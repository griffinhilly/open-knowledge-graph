---
id: coulometric-titration
title: Coulometric Titration and Electroanalysis
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: coulometry
  type: hard
- id: titrimetric-analysis-intro
  type: soft
tags:
- coulometry
- coulometric-titration
- electroanalysis
- electrode-reactions
stage: advanced
status: draft
---

# Coulometric Titration and Electroanalysis

## Core Idea
Coulometric titration generates titrant electrochemically and measures the charge (coulombs) required for quantitative analysis. This approach avoids standardization errors, enables in-situ titrant generation, and applies to species difficult to titrate conventionally (e.g., strong oxidizing agents, easily oxidizable species) by using Faraday's law of electrolysis.

## Explainer

In a conventional titration, you add a standardized solution from a burette until the reaction is complete. The accuracy of that result depends entirely on knowing the exact concentration of your titrant — which itself requires a separate standardization step against a primary standard. **Coulometric titration** eliminates this dependency by generating the titrant in situ through electrolysis. Instead of measuring volume, you measure the total electrical charge passed through the solution, and Faraday's law converts that charge directly into moles of titrant produced. Since charge can be measured with extraordinary precision using modern electronics, coulometric titration is one of the most accurate quantitative techniques available.

The connection to your prerequisite knowledge of coulometry is direct: Faraday's law states that one mole of substance is produced or consumed by the passage of nF coulombs, where n is the number of electrons transferred and F is the Faraday constant (96,485 C/mol). In coulometric titration, you apply a constant current (called **controlled-current coulometry** or **coulometric titration at constant current**) and measure how long that current flows before the endpoint is reached. The total charge Q = I × t, and the moles of titrant generated equal Q/(nF). Because the titrant is produced electrochemically at the electrode surface and reacts immediately with the analyte, there is no need to prepare, store, or standardize a titrant solution.

A classic example is the coulometric determination of acids using electrogenerated hydroxide ions. A platinum cathode reduces water to produce OH⁻, which neutralizes the acid in solution. An endpoint indicator or potentiometric sensor detects when neutralization is complete, and the instrument records the total charge consumed. The Karl Fischer titration for water content is another widely used application: iodine is generated coulometrically at the anode and reacts stoichiometrically with water in the presence of sulfur dioxide and a base. This approach can measure water content down to the microgram level — far below what volumetric Karl Fischer can achieve.

The practical advantages extend beyond accuracy. Because the titrant is generated on demand, you can work with **unstable reagents** that would decompose if stored in solution — strong oxidants like bromine, chlorine, or silver(II) can be produced at the electrode and consumed immediately. The technique is also inherently miniaturizable: since you control the amount of titrant through current and time rather than volume, you can work with very small sample sizes. The main limitation is that the electrochemical generation reaction must proceed with 100% current efficiency — every electron must go toward producing the intended titrant species, with no side reactions. Verifying this efficiency is a critical part of method development for any new coulometric titration.
