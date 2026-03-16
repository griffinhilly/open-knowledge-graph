---
id: potentiometry-ph-and-ion-measurement
title: 'Potentiometry: pH and Ion-Selective Electrode Measurement'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: potentiometry
  type: hard
- id: ion-selective-electrodes
  type: hard
- id: electrochemistry-nernst-equation
  type: soft
tags:
- potentiometry
- pH-measurement
- ion-selective-electrodes
- ISE
- electrochemistry
stage: advanced
status: draft
---

# Potentiometry: pH and Ion-Selective Electrode Measurement

## Core Idea
Potentiometric measurements (pH, ion concentration) use the Nernst equation to relate electrode potential to analyte activity. Ion-selective electrodes (ISEs) for specific ions (K⁺, Ca²⁺, NO₃⁻, etc.) provide rapid, non-destructive analysis in complex matrices including biological fluids and environmental samples without reagent consumption.

## Explainer

From your study of potentiometry and ion-selective electrodes, you know the basic principle: an electrode develops a voltage that depends on the activity of a specific ion in solution, and you measure that voltage to determine the ion's concentration. pH measurement is the most familiar example — the glass pH electrode responds selectively to H⁺ ions, and its potential follows the **Nernst equation**: E = E° + (RT/nF)ln(a), where *a* is the ion activity. At 25°C, this works out to a change of about 59.2 mV per tenfold change in H⁺ activity (one pH unit). This topic brings together potentiometry, ISE technology, and the Nernst relationship into a unified practical framework for measuring ions directly in solution.

The **glass pH electrode** is the prototype for all ISE measurements. A thin glass membrane separates two solutions: the internal reference solution of known pH and the external sample. H⁺ ions interact with the hydrated glass surface on both sides, creating a charge difference across the membrane that is proportional to the difference in H⁺ activity. The beauty of this design is that no current flows and no chemical reaction occurs — the measurement is **non-destructive**, leaving the sample unchanged. A high-impedance voltmeter measures the potential difference between the pH electrode and a reference electrode (typically Ag/AgCl), and the meter converts that voltage to pH using the Nernst relationship.

**Ion-selective electrodes** extend this concept beyond H⁺ to dozens of other ions. A fluoride ISE uses a lanthanum fluoride crystal membrane that responds selectively to F⁻; a potassium ISE uses a valinomycin-doped polymer membrane that selectively binds K⁺. In each case, the membrane creates a potential that follows the Nernst equation for the target ion, and calibration with standards of known concentration converts measured voltages to concentrations. The selectivity is never perfect — every ISE has some response to interfering ions, quantified by **selectivity coefficients** — but for many applications the selectivity is sufficient for direct measurement in complex matrices like blood, river water, or soil extracts.

A critical practical distinction is that ISEs measure **ion activity**, not concentration. Activity accounts for the fact that ions in solution interact with each other, and at higher ionic strengths these interactions reduce the "effective concentration" that the electrode sees. For dilute solutions, activity and concentration are nearly equal. For concentrated or high-ionic-strength samples (like seawater or blood plasma), the difference matters. Clinical analyzers that use ISEs for electrolyte measurements (Na⁺, K⁺, Cl⁻, Ca²⁺) handle this by either diluting the sample to low ionic strength (indirect ISE) or measuring undiluted and calibrating against standards that mimic the ionic strength of plasma (direct ISE). Understanding when activity and concentration diverge — and which one your ISE is actually measuring — is essential to interpreting potentiometric results correctly.
