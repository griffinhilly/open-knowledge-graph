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

## Questions

```yaml
- question: "A clinical lab uses a direct ISE to measure K⁺ in undiluted blood plasma. The measured K⁺ activity is 3.8 mM, but the total K⁺ concentration determined by atomic absorption is 4.2 mM. Why does this discrepancy exist?"
  type: multiple-choice
  options:
    - "The ISE is malfunctioning because blood plasma contains too many interfering ions that overwhelm the K⁺ selectivity"
    - "In high ionic strength solutions like plasma, ion-ion interactions reduce the effective concentration the electrode senses — the ISE measures activity, not total concentration, and these diverge at high ionic strength"
    - "The ISE has been incorrectly calibrated with low-ionic-strength aqueous standards instead of plasma-matched standards"
    - "K⁺ in blood plasma is partially bound to albumin and not freely ionized, which the ISE cannot detect"
  answer: 1
  explanation: "Ion-selective electrodes respond to ion activity, not total concentration. Activity = γ × c, where γ is the activity coefficient and c is the concentration. In dilute solutions γ ≈ 1 and activity ≈ concentration. In high ionic strength matrices like blood plasma, ion-ion interactions cause γ < 1, so activity is systematically lower than concentration. The ISE faithfully reports activity (3.8 mM) while atomic absorption reports total concentration (4.2 mM); neither is wrong — they measure different quantities. Understanding which one your method gives is essential for clinical interpretation."

- question: "The glass pH electrode measures pH without consuming any reagent or altering the sample. This non-destructive character arises because:"
  type: multiple-choice
  options:
    - "The glass membrane catalyzes a reversible acid-base reaction that regenerates itself, consuming no net reagent"
    - "No electrical current flows through the measurement circuit — a high-impedance voltmeter detects the potential difference across the glass membrane without driving any electrochemical reaction in the sample"
    - "The internal reference buffer solution neutralizes any pH changes caused by the measurement, restoring the sample"
    - "H⁺ ions are temporarily absorbed into the glass and then released back to the solution after measurement"
  answer: 1
  explanation: "Potentiometric measurement is a zero-current technique. A high-impedance voltmeter draws essentially no current, so no electrochemical reactions are driven in the sample and no analyte is consumed or altered. The glass membrane develops a potential difference due to H⁺ activity differences on its two faces, but this is an equilibrium property that does not require net ion transfer. This is why ISE measurements can be made in very small, precious, or reactive samples — the electrode reads the signal without changing the system."

- question: "Ion-selective electrodes measure the activity of the target ion, which equals its molar concentration in all aqueous solutions at standard conditions."
  type: true-false
  answer: false
  explanation: "Activity equals concentration only in the limit of infinite dilution, where activity coefficient γ → 1. At any real ionic strength, activity = γ × c, and γ < 1 due to electrostatic interactions among ions. For clinical samples (blood plasma, urine) or environmental samples (seawater, concentrated soil extracts), ionic strength is high enough that activity and concentration differ meaningfully. Failing to account for this is a common source of error when interpreting ISE results alongside concentration-based reference methods."

- question: "The Nernst equation predicts that a tenfold change in H⁺ activity (one pH unit) produces a change of approximately 59.2 mV in the glass pH electrode potential at 25°C."
  type: true-false
  answer: true
  explanation: "The Nernst equation for the glass electrode is E = E° + (RT/F) × ln(a_H⁺). At 25°C, RT/F = 25.7 mV, and multiplying by ln(10) ≈ 2.303 gives the Nernstian slope: 59.2 mV per decade change in activity (i.e., per pH unit). A real glass electrode's slope deviates slightly from this theoretical value due to membrane imperfections; calibration with two buffers determines the actual slope and intercept for that specific electrode. The theoretical 59.2 mV/pH is the reference expectation."

- question: "What is the difference between ion activity and ion concentration, and why does this distinction matter for interpreting ISE measurements in biological or environmental samples?"
  type: short-answer
  answer: "Ion concentration is the total amount of an ion per unit volume (mol/L). Ion activity is the thermodynamically effective concentration — the concentration corrected for the non-ideal behavior of ions in solution: activity = γ × concentration, where γ is the activity coefficient. In dilute solutions γ ≈ 1 and the two are essentially equal. In high ionic strength matrices (blood plasma, seawater, concentrated buffers), ions interact electrostatically with each other, reducing their effective activity so that γ < 1. ISEs respond to activity, not concentration. This matters because a blood K⁺ ISE reading of 3.8 mM (activity) corresponds to a somewhat higher total concentration; using the activity value directly as a concentration when interpreting against concentration-based normal ranges can introduce clinically significant errors. Clinical analyzers handle this either by diluting samples (making γ ≈ 1) or by calibrating against activity-matched plasma standards."
  explanation: "The activity vs. concentration distinction also affects method comparison: atomic absorption and flame photometry measure total concentration; ISEs measure activity. When results from these methods are compared in the same sample, the difference reflects ionic strength effects, not measurement error."
```

## Explainer

From your study of potentiometry and ion-selective electrodes, you know the basic principle: an electrode develops a voltage that depends on the activity of a specific ion in solution, and you measure that voltage to determine the ion's concentration. pH measurement is the most familiar example — the glass pH electrode responds selectively to H⁺ ions, and its potential follows the **Nernst equation**: E = E° + (RT/nF)ln(a), where *a* is the ion activity. At 25°C, this works out to a change of about 59.2 mV per tenfold change in H⁺ activity (one pH unit). This topic brings together potentiometry, ISE technology, and the Nernst relationship into a unified practical framework for measuring ions directly in solution.

The **glass pH electrode** is the prototype for all ISE measurements. A thin glass membrane separates two solutions: the internal reference solution of known pH and the external sample. H⁺ ions interact with the hydrated glass surface on both sides, creating a charge difference across the membrane that is proportional to the difference in H⁺ activity. The beauty of this design is that no current flows and no chemical reaction occurs — the measurement is **non-destructive**, leaving the sample unchanged. A high-impedance voltmeter measures the potential difference between the pH electrode and a reference electrode (typically Ag/AgCl), and the meter converts that voltage to pH using the Nernst relationship.

**Ion-selective electrodes** extend this concept beyond H⁺ to dozens of other ions. A fluoride ISE uses a lanthanum fluoride crystal membrane that responds selectively to F⁻; a potassium ISE uses a valinomycin-doped polymer membrane that selectively binds K⁺. In each case, the membrane creates a potential that follows the Nernst equation for the target ion, and calibration with standards of known concentration converts measured voltages to concentrations. The selectivity is never perfect — every ISE has some response to interfering ions, quantified by **selectivity coefficients** — but for many applications the selectivity is sufficient for direct measurement in complex matrices like blood, river water, or soil extracts.

A critical practical distinction is that ISEs measure **ion activity**, not concentration. Activity accounts for the fact that ions in solution interact with each other, and at higher ionic strengths these interactions reduce the "effective concentration" that the electrode sees. For dilute solutions, activity and concentration are nearly equal. For concentrated or high-ionic-strength samples (like seawater or blood plasma), the difference matters. Clinical analyzers that use ISEs for electrolyte measurements (Na⁺, K⁺, Cl⁻, Ca²⁺) handle this by either diluting the sample to low ionic strength (indirect ISE) or measuring undiluted and calibrating against standards that mimic the ionic strength of plasma (direct ISE). Understanding when activity and concentration diverge — and which one your ISE is actually measuring — is essential to interpreting potentiometric results correctly.
