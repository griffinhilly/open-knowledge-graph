---
id: phase-diagrams
title: Phase Diagrams and Phase Boundaries
domain: physics
course: statistical-mechanics
prerequisites:
- id: clausius-clapeyron-equation
  type: hard
- id: gibbs-free-energy
  type: soft
tags:
- phase-diagrams
- coexistence
- thermodynamics
stage: expert
status: validated
---

# Phase Diagrams and Phase Boundaries

## Core Idea
Phase diagrams map regions of (T,P,composition) space where different phases are stable. Phase boundaries are loci where two phases have equal Gibbs free energy. Triple points (three phases coexist) and critical points (liquid-gas distinction vanishes) are special points. Maxwell equal-area rule applies to first-order transitions; Clausius-Clapeyron gives the boundary slope.

## Questions

```yaml
- question: "A substance's solid-liquid phase boundary has a negative slope (dP/dT < 0) on its phase diagram. What physical property of the substance does this imply?"
  type: multiple-choice
  options:
    - "The solid phase is denser than the liquid phase, so pressure stabilizes the solid"
    - "The liquid phase is denser than the solid phase — applying pressure destabilizes the solid, favoring the denser liquid"
    - "The latent heat of melting is negative, meaning the substance releases energy upon melting"
    - "The substance sublimes rather than melts at atmospheric pressure"
  answer: 1
  explanation: "The Clausius-Clapeyron slope is dP/dT = L/(TΔv), where Δv = v_liquid − v_solid. A negative slope means Δv < 0, i.e., the liquid is denser than the solid (v_liquid < v_solid). Water is the classic example: ice is less dense than liquid water, so applying pressure favors the denser liquid phase and melts the ice. This anomalous negative slope is why ice skating works and why increased pressure can melt ice below 0°C."

- question: "Why does solid CO₂ (dry ice) sublime directly to gas at atmospheric pressure, without passing through a liquid phase?"
  type: multiple-choice
  options:
    - "CO₂ is a gas at room temperature, so its solid form is metastable and immediately decomposes"
    - "CO₂'s triple point is at 5.1 atm — atmospheric pressure is below the triple point, so the liquid phase is never stable at 1 atm"
    - "CO₂ lacks a liquid-gas coexistence curve because it is a linear molecule"
    - "The critical point of CO₂ is below room temperature, which eliminates the liquid phase entirely"
  answer: 1
  explanation: "A horizontal line at 1 atm on CO₂'s phase diagram crosses from the solid region directly into the gas region — it never passes through the liquid region, because the liquid region only exists above 5.1 atm. The triple point is the minimum pressure at which liquid CO₂ can exist. Below that pressure, you move directly from solid to gas (sublimation) as temperature increases. The location of the triple point is thus directly diagnostic of whether a substance can be liquid at a given pressure."

- question: "The triple point of a substance is a small range of temperatures and pressures where all three phases can coexist, and its location shifts depending on how quickly the sample is heated."
  type: true-false
  answer: false
  explanation: "The triple point is a unique, invariant point — a single specific temperature and pressure where all three phases simultaneously coexist in equilibrium. It is fixed by the molecular properties of the substance. It is so reproducible that the triple point of water (273.16 K, 611.7 Pa) serves as a primary calibration standard for thermometry. Heating rate, sample history, and external conditions do not affect where the triple point is — they can affect whether you reach it, but not its location."

- question: "Above the critical point, increasing pressure on a gas will eventually trigger a sharp, discontinuous condensation transition to liquid."
  type: true-false
  answer: false
  explanation: "The critical point is precisely where the sharp liquid-gas distinction disappears. Above T_c and P_c, there is only one supercritical fluid phase — no phase boundary exists, and you can move continuously from gas-like to liquid-like conditions without any discontinuous transition. Supercritical CO₂, used in industrial extraction, exploits this: its density and solvent power vary continuously with pressure, with no sudden phase jump."

- question: "At any point on a phase boundary in a phase diagram, what determines which phase is stable on each side, and what is true right at the boundary itself?"
  type: short-answer
  answer: "On each side of a boundary, the stable phase is the one with the lower Gibbs free energy G = U + PV − TS at those conditions. Different phases have different T and P dependences of G (primarily through their entropy and volume differences). At the boundary itself, both phases have exactly equal Gibbs free energy — this coexistence condition G₁(T,P) = G₂(T,P) defines the curve, and the Clausius-Clapeyron equation gives its slope dP/dT = L/(TΔv)."
  explanation: "This equal-G framework unifies all phase behavior: the ice-water boundary has a particular slope because of water's anomalous density; CO₂ has its triple point at high pressure because of its molecular interactions; the critical point is where the G difference between liquid and gas vanishes continuously. Reading a phase diagram as a map of Gibbs free energy minimization turns a collection of empirical facts into a single coherent principle."
```

## Explainer

A **phase diagram** is a map of matter: it shows which physical state — solid, liquid, gas, or more exotic phases — is thermodynamically stable for each combination of temperature and pressure. You can read it as a decision boundary. Cross a line on the diagram and the material undergoes a phase transition. Understanding the diagram requires only two things you already know: Gibbs free energy determines which phase is stable, and the Clausius-Clapeyron equation determines where the boundary lines run.

The stability rule is simple: at given T and P, the phase with the **lowest Gibbs free energy** G = U + PV − TS is the equilibrium state. When two phases have equal G they coexist — that is exactly the phase boundary. Because G depends on T and P differently for different phases (gases have much higher entropy than solids, for instance), the coexistence condition G₁(T,P) = G₂(T,P) defines a curve in the T-P plane. The slope of this curve is the Clausius-Clapeyron relation: dP/dT = L/(TΔv), where L is the latent heat and Δv is the molar volume change. For the liquid-gas boundary, ΔS > 0 and Δv > 0, so the slope is always positive. For the ice-water boundary in ordinary water, the anomalous negative slope (dP/dT < 0) reflects the fact that ice is less dense than liquid water — increasing pressure melts ice by making the denser liquid phase more favorable.

The three phases meet at the **triple point**, a unique T and P where solid, liquid, and gas are all in mutual equilibrium. The triple point has only one possible location — it is an invariant point set by the material's molecular properties. Moving in any direction from the triple point takes you into a single-phase region. The **critical point** terminates the liquid-gas coexistence curve at high temperature and pressure. Above it, the distinction between liquid and gas disappears: the system becomes a **supercritical fluid** with no discontinuous transition between the two. Near the critical point, the Maxwell equal-area rule is needed to handle the region where the equation of state predicts unphysical behavior (negative compressibility), replacing it with a horizontal tie line representing two-phase coexistence.

Phase diagrams encode practical wisdom. The fact that CO₂ has a triple point at 5.1 atm means that at atmospheric pressure solid CO₂ (dry ice) sublimes directly to gas — the liquid phase is simply never stable at 1 atm. A pressure cooker raises the boiling point of water by moving up the liquid-gas coexistence curve to where the equilibrium temperature is higher. Mountain cooking requires adjustment because lower atmospheric pressure moves down the same curve, lowering the boiling point. Reading a phase diagram fluently is the same skill as reading a topographic map: every boundary and special point tells a concrete story about what the material will do under those conditions.
