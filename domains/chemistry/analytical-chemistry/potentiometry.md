---
id: potentiometry
title: Potentiometry and Ion-Selective Electrodes
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: electrochemistry-basics
  type: hard
- id: electrochemical-cells
  type: hard
- id: ph-and-acid-base-calculations
  type: soft
builds-toward:
- voltammetry
- coulometry
tags:
- potentiometry
- Nernst equation
- ion-selective electrode
- pH electrode
- reference electrode
stage: advanced
status: draft
---

# Potentiometry and Ion-Selective Electrodes

## Core Idea
Potentiometry measures cell potential at zero current flow to determine analyte concentration, using the Nernst equation: E = E° − (RT/nF)ln(Q). The glass pH electrode is an ion-selective electrode (ISE) whose membrane potential varies with H⁺ activity; analogous membranes enable ISEs for F⁻, NO₃⁻, Ca²⁺, and other ions. Potentiometric titrations (pH, pIon, or pE vs volume) locate equivalence points precisely from inflection points, avoiding indicator ambiguity. Reference electrodes (SHE, Ag/AgCl, saturated calomel) provide a stable potential against which the indicator electrode is measured.

## How It's Best Learned
Calibrate a pH electrode using three buffers, measure unknown samples, then repeat a strong acid–strong base titration potentiometrically and graphically locate the equivalence point by the first or second derivative method. Comparing to the indicator endpoint quantifies the titration error.

## Common Misconceptions
- The glass electrode measures H⁺ activity, not concentration — in high ionic strength solutions, activity corrections (activity coefficients) are needed.
- All ISEs have a selectivity coefficient for interfering ions; complete selectivity does not exist, and the Nikolsky–Eisenman equation describes the interference.
