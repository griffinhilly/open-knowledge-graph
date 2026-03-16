---
id: state-functions-path-functions
title: State Functions and Path Functions in Thermodynamics
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: fundamentals-thermodynamic-systems
  type: hard
- id: first-law-closed-systems
  type: hard
builds-toward:
- entropy-balance-equations
- thermodynamic-property-equations-engineering
tags:
- properties
- state
- path
- differentials
- exactness
stage: advanced
status: draft
---

# State Functions and Path Functions in Thermodynamics

## Core Idea
State functions (internal energy, enthalpy, entropy, Gibbs free energy) depend only on initial and final states, not on process path, making them exact differentials: ∮dU = 0 around any cycle. Path functions (heat and work) depend on the specific process followed. This distinction is fundamental: properties can be tabulated, but heat and work must be calculated for each process.

## Explainer

Think about hiking from the base to the summit of a mountain. Your change in altitude depends only on where you started and where you ended — it doesn't matter whether you took the steep direct route or the winding switchback trail. Altitude is a **state function**: its value is determined entirely by your current state. Now think about how much physical effort you expended, or how far you walked. Those depend entirely on which path you took. That is the distinction between state functions and **path functions** in thermodynamics.

Internal energy U, enthalpy H, entropy S, and Gibbs free energy G are all state functions. Their values are fixed once you specify the thermodynamic state — pressure, temperature, and composition, or equivalently any two independent intensive properties. This is what makes steam tables and refrigerant property tables possible: because H at a given (T, P) is unique, you can look it up. You used this in the first law of closed systems: ΔU = Q − W, and you could look up U₁ and U₂ in tables without knowing *how* the process happened. The first law works precisely because U is a state function.

**Heat Q and work W are not state functions — they are path functions.** The same initial and final states can be connected by infinitely many different processes, each delivering a different amount of heat and work, but always giving the same ΔU (because U is a state function). To emphasize this, thermodynamicists use the notation δQ and δW for infinitesimal quantities of heat and work — the "d" notation with a stroke through it signals that these are *inexact* differentials. They cannot be integrated without knowing the process path. A consequence: "heat content" and "work content" of a system are meaningless phrases. A system stores energy (U or H), not heat or work.

This distinction has immediate practical consequences. When you analyze a thermodynamic cycle — a power cycle, refrigeration cycle, or heat pump — the working fluid returns to its initial state after one complete cycle. Because U is a state function, ΔU = 0 over a full cycle: ∮dU = 0. The net work done and net heat transferred over the cycle are not zero, but they must be equal in magnitude (from the first law: W_net = Q_net). Every efficiency calculation you will ever do for a cycle depends on this: the work and heat quantities depend on which processes make up the cycle, but the state properties (temperature, pressure, enthalpy) at each cycle point depend only on the state, not on how you got there. Recognizing what can be tabulated versus what must be process-calculated is the organizational principle behind all thermodynamic analysis.
