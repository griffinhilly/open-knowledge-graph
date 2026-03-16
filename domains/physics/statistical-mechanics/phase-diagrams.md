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
stage: advanced
status: draft
---

# Phase Diagrams and Phase Boundaries

## Core Idea
Phase diagrams map regions of (T,P,composition) space where different phases are stable. Phase boundaries are loci where two phases have equal Gibbs free energy. Triple points (three phases coexist) and critical points (liquid-gas distinction vanishes) are special points. Maxwell equal-area rule applies to first-order transitions; Clausius-Clapeyron gives the boundary slope.

## Explainer

A **phase diagram** is a map of matter: it shows which physical state — solid, liquid, gas, or more exotic phases — is thermodynamically stable for each combination of temperature and pressure. You can read it as a decision boundary. Cross a line on the diagram and the material undergoes a phase transition. Understanding the diagram requires only two things you already know: Gibbs free energy determines which phase is stable, and the Clausius-Clapeyron equation determines where the boundary lines run.

The stability rule is simple: at given T and P, the phase with the **lowest Gibbs free energy** G = U + PV − TS is the equilibrium state. When two phases have equal G they coexist — that is exactly the phase boundary. Because G depends on T and P differently for different phases (gases have much higher entropy than solids, for instance), the coexistence condition G₁(T,P) = G₂(T,P) defines a curve in the T-P plane. The slope of this curve is the Clausius-Clapeyron relation: dP/dT = L/(TΔv), where L is the latent heat and Δv is the molar volume change. For the liquid-gas boundary, ΔS > 0 and Δv > 0, so the slope is always positive. For the ice-water boundary in ordinary water, the anomalous negative slope (dP/dT < 0) reflects the fact that ice is less dense than liquid water — increasing pressure melts ice by making the denser liquid phase more favorable.

The three phases meet at the **triple point**, a unique T and P where solid, liquid, and gas are all in mutual equilibrium. The triple point has only one possible location — it is an invariant point set by the material's molecular properties. Moving in any direction from the triple point takes you into a single-phase region. The **critical point** terminates the liquid-gas coexistence curve at high temperature and pressure. Above it, the distinction between liquid and gas disappears: the system becomes a **supercritical fluid** with no discontinuous transition between the two. Near the critical point, the Maxwell equal-area rule is needed to handle the region where the equation of state predicts unphysical behavior (negative compressibility), replacing it with a horizontal tie line representing two-phase coexistence.

Phase diagrams encode practical wisdom. The fact that CO₂ has a triple point at 5.1 atm means that at atmospheric pressure solid CO₂ (dry ice) sublimes directly to gas — the liquid phase is simply never stable at 1 atm. A pressure cooker raises the boiling point of water by moving up the liquid-gas coexistence curve to where the equilibrium temperature is higher. Mountain cooking requires adjustment because lower atmospheric pressure moves down the same curve, lowering the boiling point. Reading a phase diagram fluently is the same skill as reading a topographic map: every boundary and special point tells a concrete story about what the material will do under those conditions.
