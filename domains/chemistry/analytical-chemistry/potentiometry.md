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
- id: electric-potential
  type: soft
- id: electric-current-and-resistance
  type: soft
- id: electric-potential-definition
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
stage: formal-systems
status: validated
---

# Potentiometry and Ion-Selective Electrodes

## Core Idea
Potentiometry measures cell potential at zero current flow to determine analyte concentration, using the Nernst equation: E = E° − (RT/nF)ln(Q). The glass pH electrode is an ion-selective electrode (ISE) whose membrane potential varies with H⁺ activity; analogous membranes enable ISEs for F⁻, NO₃⁻, Ca²⁺, and other ions. Potentiometric titrations (pH, pIon, or pE vs volume) locate equivalence points precisely from inflection points, avoiding indicator ambiguity. Reference electrodes (SHE, Ag/AgCl, saturated calomel) provide a stable potential against which the indicator electrode is measured.

## How It's Best Learned
Calibrate a pH electrode using three buffers, measure unknown samples, then repeat a strong acid–strong base titration potentiometrically and graphically locate the equivalence point by the first or second derivative method. Comparing to the indicator endpoint quantifies the titration error.

## Common Misconceptions
- The glass electrode measures H⁺ activity, not concentration — in high ionic strength solutions, activity corrections (activity coefficients) are needed.
- All ISEs have a selectivity coefficient for interfering ions; complete selectivity does not exist, and the Nikolsky–Eisenman equation describes the interference.

## Questions

```yaml
- question: "According to the Nernst equation, what does the cell potential measured in potentiometry directly reflect?"
  type: multiple-choice
  options: ["The current flowing through the cell", "The activity of the analyte ion", "The concentration of the reference electrode solution", "The resistance of the ion-selective membrane"]
  answer: 1
  explanation: "The Nernst equation E = E° − (RT/nF)ln(Q) relates cell potential to the activity (not concentration) of the ions involved. Potentiometry exploits this by measuring potential at zero current, so the measured voltage directly encodes the analyte's activity in solution."

- question: "A glass pH electrode measures the concentration of H⁺ ions in solution."
  type: true-false
  answer: false
  explanation: "The glass electrode responds to H⁺ activity, not concentration. Activity and concentration differ especially at high ionic strengths, where activity coefficients deviate significantly from 1. This is why accurate pH measurements require ionic strength adjustment or calibration in solutions that closely match the sample matrix."

- question: "Why is a stable reference electrode essential in a potentiometric measurement?"
  type: short-answer
  answer: "A reference electrode provides a fixed, known potential so that any change in the measured cell voltage can be attributed entirely to the indicator electrode responding to the analyte. Without a stable reference, you cannot isolate the signal from the analyte."
  explanation: "Potentiometry measures the potential difference between two electrodes. If the reference electrode potential drifts, it is impossible to determine whether a voltage change reflects a change in analyte concentration or a change in the reference. Common reference electrodes (Ag/AgCl, saturated calomel) maintain constant potential through well-buffered redox couples."
```

## Explainer

Potentiometry is a form of electroanalytical chemistry that extracts concentration information from voltage, not from current. The key insight is the Nernst equation: at equilibrium (zero current), the potential of an electrochemical cell depends logarithmically on the activity of the ions in solution. By measuring that potential with a high-impedance voltmeter — so virtually no current flows — you can read out the analyte activity without disturbing the system.

The glass pH electrode is the most familiar ion-selective electrode. The electrode contains a thin glass membrane whose inner surface is in contact with a known reference solution, and whose outer surface is exposed to the sample. H⁺ ions exchange with sodium ions in the glass lattice, generating a membrane potential proportional to the difference in H⁺ activity across the glass. This potential, when measured against a stable reference electrode, gives pH directly. The elegance is that the membrane itself is the sensor — it is selective because only certain ions interact favorably with the glass lattice.

The same principle extends to other ions. Fluoride ISEs use a lanthanum fluoride crystal membrane; nitrate ISEs use a liquid membrane with a lipophilic ion exchanger. No membrane is perfectly selective: every ISE responds to some degree to interfering ions, described quantitatively by the Nikolsky–Eisenman equation. Understanding selectivity coefficients is critical when measuring dilute analytes in complex matrices.

A key misconception to address: the glass electrode measures H⁺ activity, not concentration. In pure water, activity ≈ concentration, so the distinction rarely matters in introductory work. But in high-ionic-strength solutions like blood or seawater, activity coefficients deviate substantially from 1, and ignoring this introduces systematic error. Calibrating in buffers that match the sample's ionic strength is standard practice in rigorous work.

Potentiometric titrations extend the technique to equivalence point location. Instead of watching a color change from an indicator, you plot cell potential versus volume of titrant added. The equivalence point appears as an inflection point — sharpest at the steepest part of the sigmoidal curve. Taking the first or second derivative of the potential-vs-volume plot localizes the equivalence point precisely, eliminating the subjectivity of indicator endpoint observations.
