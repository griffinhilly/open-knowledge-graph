---
id: electroanalytical-overview
title: Electroanalytical Methods Overview
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: analytical-chemistry-intro
  type: hard
- id: electric-current-definition
  type: soft
- id: electric-potential
  type: soft
- id: electron-transfer
  type: soft
builds-toward:
- potentiometry
- voltammetry
- coulometry
- conductometry
tags:
- electroanalytical
- electrochemistry
- potentiometry
- voltammetry
- coulometry
- conductometry
stage: advanced
status: validated
---

# Electroanalytical Methods Overview

## Core Idea
Electroanalytical chemistry encompasses a family of techniques that extract analytical information from the electrical properties of a solution containing an analyte. The four principal branches are distinguished by what they measure: potentiometry measures voltage at zero current (revealing activity or concentration via the Nernst equation), voltammetry measures current as a function of applied potential (revealing redox identity and concentration), coulometry measures total charge passed during complete electrolysis (yielding absolute amounts without calibration), and conductometry measures solution conductance (reflecting total ionic content). Each branch offers different strengths — potentiometry for selective ion sensing, voltammetry for trace-level sensitivity, coulometry for primary-standard accuracy, and conductometry for non-selective bulk monitoring.

## How It's Best Learned
Survey all four techniques side-by-side using the same analyte (e.g., Cu²⁺): measure its potential with a copper electrode, run a voltammogram, electrolyze it coulometrically, and monitor conductance during a titration. Seeing the same species through four different electrical lenses clarifies what each technique uniquely reveals.

## Common Misconceptions
- Electroanalytical methods do not all require the analyte to undergo a redox reaction; potentiometry and conductometry are non-faradaic and measure equilibrium or transport properties without electrolysis.
- The four branches are complementary, not competitive — choosing among them depends on whether the analytical question demands selectivity, sensitivity, absolute accuracy, or simplicity.

## Questions

```yaml
- question: "An environmental chemist needs to measure lead (Pb²⁺) at parts-per-trillion concentrations in drinking water. Which electroanalytical branch is best suited to this task, and why?"
  type: multiple-choice
  options:
    - "Potentiometry, because ion-selective electrodes can detect any metal ion with extreme selectivity"
    - "Conductometry, because total ionic content is directly proportional to trace metal concentration"
    - "Voltammetry (specifically stripping voltammetry), because analytes can be pre-concentrated at the electrode surface before measurement, achieving trace-level sensitivity"
    - "Coulometry, because it yields absolute amounts without a calibration curve, eliminating matrix effects"
  answer: 2
  explanation: "Stripping voltammetry achieves sub-ppb and even ppt detection limits for trace metals by exploiting a two-step process: the analyte is electrodeposited (concentrated) onto the working electrode surface during a deposition step, then stripped off in a voltage scan that produces a sharp current peak. This pre-concentration step amplifies the analytical signal by orders of magnitude compared to measuring the dilute solution directly. Potentiometry (A) lacks the sensitivity for ppt levels and ion-selective electrodes are not available for all metals. Conductometry (B) cannot distinguish Pb²⁺ from other ions and is insensitive to trace levels. Coulometry (D) is accurate but not inherently trace-sensitive — it measures everything that is electrolyzed, not trace amounts pre-concentrated at an electrode."

- question: "What property makes coulometry a 'primary' analytical method — one that can yield accurate results without a calibration curve?"
  type: multiple-choice
  options:
    - "Coulometry uses multiple electrodes that cross-validate each other, eliminating systematic error"
    - "Coulometry measures total charge passed during complete electrolysis, and since Q = nFN, the amount of analyte is calculated directly from charge using Faraday's constant without reference to any standard"
    - "Coulometry is performed at equilibrium, so the Nernst equation relates charge directly to analyte activity"
    - "Coulometry is the only method that requires the analyte to undergo a redox reaction, ensuring specificity"
  answer: 1
  explanation: "The relationship Q = nFN (charge = electrons per molecule × Faraday's constant × moles of analyte) is a fundamental physical law. If you measure the total charge passed during the complete electrolysis of an analyte, you can calculate the exact number of moles from the charge and Faraday's constant — no comparison to a standard solution is needed. This makes coulometry a primary method in the metrological sense: its accuracy is grounded in a physical constant rather than in the accuracy of a prepared standard. This stands in contrast to potentiometry and voltammetry, which require calibration curves using known standards to convert their signals (voltage or current) into concentrations."

- question: "A pH meter measures hydrogen ion activity using potentiometry, even though no current flows through the solution and no oxidation or reduction occurs at the glass membrane."
  type: true-false
  answer: true
  explanation: "This is the defining feature of potentiometry — it is a non-faradaic technique. The glass membrane develops a voltage (potential difference) in response to the difference in hydrogen ion activity on its two sides, and this equilibrium potential is measured without passing current through the sample. No redox reaction occurs at the membrane; ion exchange equilibrium across the glass generates the signal. This directly contradicts the common misconception that all electroanalytical methods require the analyte to undergo a redox reaction. Potentiometry listens to the system's equilibrium electrical state rather than driving a reaction."

- question: "All four branches of electroanalytical chemistry require the analyte to be oxidized or reduced at an electrode surface to generate the analytical signal."
  type: true-false
  answer: false
  explanation: "Potentiometry and conductometry are non-faradaic methods — they do not require or involve electrode reactions. Potentiometry measures the equilibrium potential that develops across a selective membrane based on the chemical activity of the target ion, with no current flowing. Conductometry measures the ability of the solution to conduct an AC current, which depends on ion mobility and concentration, not on any redox chemistry. Only voltammetry and coulometry are faradaic methods that rely on electron transfer at an electrode. Confusing all electroanalytical methods with redox reactions is one of the most common conceptual errors in this area."

- question: "A researcher needs to determine the concentration of fluoride (F⁻) in a complex environmental sample containing many other ions (Na⁺, Cl⁻, SO₄²⁻, Ca²⁺, etc.). Explain why potentiometry with a fluoride-selective electrode is more appropriate than conductometry for this task."
  type: short-answer
  answer: "Conductometry measures the total ionic conductance of the solution — the combined contribution of all ions present, weighted by their concentration and mobility. In a complex matrix containing many ions, a change in F⁻ concentration would produce a negligible change in total conductance that could not be distinguished from changes in the other ionic species. Conductometry therefore cannot selectively detect F⁻ in the presence of a background of other ions at similar or higher concentrations. A fluoride-selective electrode (a lanthanum fluoride crystal membrane) responds specifically to fluoride ion activity with very little response to most other common anions, generating a voltage that varies logarithmically with fluoride activity according to the Nernst equation. This selectivity arises from the crystal structure of the membrane, which admits only F⁻ at its surface. The measurement is thus resistant to interference from the complex matrix, providing the ion-specific information that conductometry cannot."
  explanation: "The core principle is that potentiometry's selectivity comes from the electrode membrane, which acts as a chemical filter — responding to one ion while ignoring others. Conductometry has no such filter and cannot distinguish among ionic species. Matching the right electroanalytical technique to the analytical question (here: selective single-ion measurement in a complex matrix) is the practical skill that this overview is designed to build."
```

## Explainer

Electroanalytical methods exploit a fundamental connection you already understand from your prerequisites: chemical species in solution carry charge and participate in electron-transfer reactions, and these electrical properties can be measured with remarkable precision. The beauty of electroanalytical chemistry is that electricity is both the probe and the signal — you use electrodes immersed in the sample solution to either passively listen to the system's electrical state or actively drive reactions and measure the response.

**Potentiometry** is the most passive of the four branches. You place a selective electrode (like a glass pH electrode or an ion-selective electrode for fluoride) into the solution and measure the voltage that develops at zero current. The Nernst equation — which you know from electrochemistry — relates this voltage to the logarithm of the analyte's activity. No current flows, no reaction is driven, and the measurement is essentially non-destructive. The selectivity comes from the electrode membrane, which responds preferentially to one ion. This is why your pH meter works: the glass membrane generates a voltage proportional to hydrogen ion activity, largely ignoring the hundreds of other ions present.

**Voltammetry** takes the opposite approach — it actively applies a varying potential to a working electrode and measures the resulting current as electroactive species are oxidized or reduced. The current-voltage curve (voltammogram) is an analytical fingerprint: the potential at which current flows identifies *what* species is reacting, and the magnitude of the current reveals *how much* is present. Because you can concentrate analytes at the electrode surface before the measurement sweep (a technique called stripping voltammetry), detection limits can reach parts-per-trillion levels for trace metals. **Coulometry** measures the total charge passed during complete electrolysis of the analyte. Since charge equals moles times Faraday's constant times electrons transferred (Q = nFN), you get an absolute measurement of amount — no calibration curve needed, making coulometry a primary analytical method.

**Conductometry** is the simplest conceptually: it measures how well the solution conducts electricity, which depends on the total concentration and mobility of all ions present. It lacks selectivity — it cannot distinguish sodium from potassium — but this makes it ideal for monitoring total ionic content, detecting endpoints in acid-base or precipitation titrations (where ionic composition changes sharply), and checking water purity. The choice among these four branches depends entirely on your analytical question: need selective single-ion measurement? Use potentiometry. Need ultra-trace sensitivity? Voltammetry. Need calibration-free accuracy? Coulometry. Need a simple, robust bulk measurement? Conductometry. Understanding all four as a family, rather than as isolated techniques, lets you match the right electrical measurement to each analytical problem.
