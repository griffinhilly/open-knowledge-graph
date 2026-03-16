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
stage: formal-systems
status: draft
---

# Electroanalytical Methods Overview

## Core Idea
Electroanalytical chemistry encompasses a family of techniques that extract analytical information from the electrical properties of a solution containing an analyte. The four principal branches are distinguished by what they measure: potentiometry measures voltage at zero current (revealing activity or concentration via the Nernst equation), voltammetry measures current as a function of applied potential (revealing redox identity and concentration), coulometry measures total charge passed during complete electrolysis (yielding absolute amounts without calibration), and conductometry measures solution conductance (reflecting total ionic content). Each branch offers different strengths — potentiometry for selective ion sensing, voltammetry for trace-level sensitivity, coulometry for primary-standard accuracy, and conductometry for non-selective bulk monitoring.

## How It's Best Learned
Survey all four techniques side-by-side using the same analyte (e.g., Cu²⁺): measure its potential with a copper electrode, run a voltammogram, electrolyze it coulometrically, and monitor conductance during a titration. Seeing the same species through four different electrical lenses clarifies what each technique uniquely reveals.

## Common Misconceptions
- Electroanalytical methods do not all require the analyte to undergo a redox reaction; potentiometry and conductometry are non-faradaic and measure equilibrium or transport properties without electrolysis.
- The four branches are complementary, not competitive — choosing among them depends on whether the analytical question demands selectivity, sensitivity, absolute accuracy, or simplicity.

## Explainer

Electroanalytical methods exploit a fundamental connection you already understand from your prerequisites: chemical species in solution carry charge and participate in electron-transfer reactions, and these electrical properties can be measured with remarkable precision. The beauty of electroanalytical chemistry is that electricity is both the probe and the signal — you use electrodes immersed in the sample solution to either passively listen to the system's electrical state or actively drive reactions and measure the response.

**Potentiometry** is the most passive of the four branches. You place a selective electrode (like a glass pH electrode or an ion-selective electrode for fluoride) into the solution and measure the voltage that develops at zero current. The Nernst equation — which you know from electrochemistry — relates this voltage to the logarithm of the analyte's activity. No current flows, no reaction is driven, and the measurement is essentially non-destructive. The selectivity comes from the electrode membrane, which responds preferentially to one ion. This is why your pH meter works: the glass membrane generates a voltage proportional to hydrogen ion activity, largely ignoring the hundreds of other ions present.

**Voltammetry** takes the opposite approach — it actively applies a varying potential to a working electrode and measures the resulting current as electroactive species are oxidized or reduced. The current-voltage curve (voltammogram) is an analytical fingerprint: the potential at which current flows identifies *what* species is reacting, and the magnitude of the current reveals *how much* is present. Because you can concentrate analytes at the electrode surface before the measurement sweep (a technique called stripping voltammetry), detection limits can reach parts-per-trillion levels for trace metals. **Coulometry** measures the total charge passed during complete electrolysis of the analyte. Since charge equals moles times Faraday's constant times electrons transferred (Q = nFN), you get an absolute measurement of amount — no calibration curve needed, making coulometry a primary analytical method.

**Conductometry** is the simplest conceptually: it measures how well the solution conducts electricity, which depends on the total concentration and mobility of all ions present. It lacks selectivity — it cannot distinguish sodium from potassium — but this makes it ideal for monitoring total ionic content, detecting endpoints in acid-base or precipitation titrations (where ionic composition changes sharply), and checking water purity. The choice among these four branches depends entirely on your analytical question: need selective single-ion measurement? Use potentiometry. Need ultra-trace sensitivity? Voltammetry. Need calibration-free accuracy? Coulometry. Need a simple, robust bulk measurement? Conductometry. Understanding all four as a family, rather than as isolated techniques, lets you match the right electrical measurement to each analytical problem.
