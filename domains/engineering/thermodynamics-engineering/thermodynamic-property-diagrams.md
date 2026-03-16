---
id: thermodynamic-property-diagrams
title: Thermodynamic Property Diagrams and Representations
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: pure-substance-phase-diagrams
  type: hard
- id: entropy-calculation-properties
  type: hard
builds-toward:
- rankine-cycle-thermodynamic-analysis
- brayton-cycle-gas-turbine
- refrigeration-thermodynamic-analysis
tags:
- property-diagrams
- ts-diagram
- hs-diagram
- ph-diagram
- visualization
stage: advanced
status: draft
---

# Thermodynamic Property Diagrams and Representations

## Core Idea
Thermodynamic property diagrams (T-s, h-s, P-h, P-v) are graphical representations of substance properties that enable rapid design calculations for cycles and processes. The T-s diagram directly shows reversibility via enclosed areas representing work and heat. These diagrams are indispensable tools for thermodynamic cycle analysis and optimization in engineering practice.

## Explainer

You already know how to read a phase diagram and how to compute entropy changes for processes. Property diagrams bring those two skills together into a single graphical framework that makes thermodynamic cycle analysis visual and intuitive, replacing equation-solving with pattern recognition.

The **T-s diagram** (temperature–entropy) is the most conceptually revealing. Recall that for a reversible process, δQ_rev = T dS, so the area under a reversible process curve on a T-s diagram equals the heat exchanged. For a complete reversible cycle, the net enclosed area equals the net work output. The Carnot cycle traces a rectangle: two horizontal isothermal processes (constant T) and two vertical isentropic processes (constant s, no heat). Its efficiency is immediately visible as the ratio of rectangle height to the height of the heat-input isotherm measured from absolute zero. Real cycles deviate from this rectangle, and the T-s diagram shows exactly where — irreversibilities show up as rightward drift (entropy generation).

The **h-s diagram** (enthalpy–entropy, also called the **Mollier diagram**) is the working engineer's primary tool for turbines and compressors. Enthalpy differences directly equal work for adiabatic devices, and ideal isentropic devices move vertically on the diagram (s constant, h decreasing for turbines). Real expansion moves down and to the right — entropy increases due to friction and irreversibilities. The ratio of actual enthalpy drop to ideal (isentropic) enthalpy drop defines **isentropic efficiency**, and reading it from the Mollier diagram requires only two enthalpy values.

The **P-h diagram** (pressure–enthalpy) is the standard tool for refrigeration and heat pump analysis. The vapor-compression refrigeration cycle plots as a rectangle straddling the two-phase dome: the condenser is a horizontal line at high pressure (heat rejection at constant pressure), the evaporator is a horizontal line at low pressure (heat absorption), the compressor raises pressure at roughly constant entropy, and the expansion valve drops pressure at constant enthalpy. Coefficient of performance is read directly as a ratio of enthalpy differences. Four numbers from the diagram give a complete cycle analysis.

The power of property diagrams lies in pattern recognition built up over repeated use. Once you know what a Rankine cycle looks like on a T-s diagram — a teardrop shape pressed against the two-phase dome — you can immediately see the effect of superheating (extends the top edge rightward), reheating (adds a second expansion loop), or regeneration (narrows the heat-addition temperature range). You stop solving equations for every cycle variant and start reading design tradeoffs directly from the diagram's geometry.
