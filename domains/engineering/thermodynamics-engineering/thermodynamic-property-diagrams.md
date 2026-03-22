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

## Questions

```yaml
- question: "On a T-s diagram, what does the net enclosed area of a complete reversible thermodynamic cycle represent?"
  type: multiple-choice
  options:
    - "The total heat input to the cycle"
    - "The net work output of the cycle"
    - "The total entropy generated during the cycle"
    - "The thermal efficiency of the cycle as a percentage"
  answer: 1
  explanation: "For a reversible process, δQ_rev = T dS, so the area under a curve on a T-s diagram equals heat exchanged. For a complete cycle, the positive and negative heat areas cancel, leaving only the net enclosed area — which equals net work output (by the first law, net work = net heat for a cycle). Efficiency is dimensionless and can be read as a ratio from the diagram, but the area itself represents net work, not efficiency."

- question: "An engineer plots an ideal (isentropic) and a real turbine expansion on an h-s (Mollier) diagram between the same inlet state and exit pressure. The real process endpoint lies to the right of the ideal endpoint at the same exit pressure. What does this rightward shift indicate?"
  type: multiple-choice
  options:
    - "The real turbine produces more work than the ideal turbine because it reaches a higher enthalpy state"
    - "The real expansion is faster, generating more kinetic energy that appears as higher enthalpy"
    - "Entropy was generated due to internal irreversibilities, so actual enthalpy drop — and work output — is less than ideal"
    - "The fluid has crossed into the two-phase dome, causing condensation losses"
  answer: 2
  explanation: "An ideal isentropic turbine moves vertically downward (s constant). A real turbine generates entropy due to friction and irreversibilities, so the exit state shifts rightward (higher s) at the same exit pressure. Because enthalpy is also higher at that rightward point on the isobar, the actual enthalpy drop (and thus work output) is smaller than the ideal drop. This ratio defines isentropic efficiency — readable directly from two h values on the diagram."

- question: "On a T-s diagram, the Carnot cycle traces a perfect rectangle because its heat-exchange processes are isothermal and its work processes are isentropic."
  type: true-false
  answer: true
  explanation: "True. Isothermal heat addition/rejection at constant T traces horizontal lines, and isentropic compression/expansion at constant s traces vertical lines. The resulting rectangle makes Carnot efficiency visually immediate: it is the ratio of the net work rectangle to the heat input area, which simplifies to (T_H - T_L) / T_H."

- question: "The P-h diagram is the preferred tool for analyzing steam power (Rankine) cycles because enthalpy differences directly equal turbine and pump work."
  type: true-false
  answer: false
  explanation: "False. The P-h (pressure-enthalpy) diagram is the standard tool for refrigeration and heat pump cycles, where the vapor-compression cycle plots as a near-rectangle. Rankine cycle analysis is typically done on T-s or h-s diagrams, where the teardrop shape against the two-phase dome makes superheat, reheat, and regeneration effects visually clear. Both diagrams use enthalpy differences for work, but each is optimized for different cycle geometries."

- question: "Why is the T-s diagram described as 'conceptually revealing' in a way that other property diagrams are not?"
  type: short-answer
  answer: "The T-s diagram has a direct physical interpretation: area equals heat. This means cycle quality and irreversibility are geometrically visible — a Carnot cycle is a rectangle, real cycles deviate from it, and entropy generation shows up as rightward drift. Other diagrams (P-v, P-h) are useful for calculations but don't make thermodynamic quality and lost work visually immediate in the same way."
  explanation: "The key is the identity δQ_rev = T dS: it connects geometry to physics. On a T-s diagram, you can literally see where a cycle loses quality — where heat is rejected at high temperature needlessly, or where irreversibilities widen the cycle. This makes the T-s diagram a diagnostic tool, not just a calculation aid."
```

## Explainer

You already know how to read a phase diagram and how to compute entropy changes for processes. Property diagrams bring those two skills together into a single graphical framework that makes thermodynamic cycle analysis visual and intuitive, replacing equation-solving with pattern recognition.

The **T-s diagram** (temperature–entropy) is the most conceptually revealing. Recall that for a reversible process, δQ_rev = T dS, so the area under a reversible process curve on a T-s diagram equals the heat exchanged. For a complete reversible cycle, the net enclosed area equals the net work output. The Carnot cycle traces a rectangle: two horizontal isothermal processes (constant T) and two vertical isentropic processes (constant s, no heat). Its efficiency is immediately visible as the ratio of rectangle height to the height of the heat-input isotherm measured from absolute zero. Real cycles deviate from this rectangle, and the T-s diagram shows exactly where — irreversibilities show up as rightward drift (entropy generation).

The **h-s diagram** (enthalpy–entropy, also called the **Mollier diagram**) is the working engineer's primary tool for turbines and compressors. Enthalpy differences directly equal work for adiabatic devices, and ideal isentropic devices move vertically on the diagram (s constant, h decreasing for turbines). Real expansion moves down and to the right — entropy increases due to friction and irreversibilities. The ratio of actual enthalpy drop to ideal (isentropic) enthalpy drop defines **isentropic efficiency**, and reading it from the Mollier diagram requires only two enthalpy values.

The **P-h diagram** (pressure–enthalpy) is the standard tool for refrigeration and heat pump analysis. The vapor-compression refrigeration cycle plots as a rectangle straddling the two-phase dome: the condenser is a horizontal line at high pressure (heat rejection at constant pressure), the evaporator is a horizontal line at low pressure (heat absorption), the compressor raises pressure at roughly constant entropy, and the expansion valve drops pressure at constant enthalpy. Coefficient of performance is read directly as a ratio of enthalpy differences. Four numbers from the diagram give a complete cycle analysis.

The power of property diagrams lies in pattern recognition built up over repeated use. Once you know what a Rankine cycle looks like on a T-s diagram — a teardrop shape pressed against the two-phase dome — you can immediately see the effect of superheating (extends the top edge rightward), reheating (adds a second expansion loop), or regeneration (narrows the heat-addition temperature range). You stop solving equations for every cycle variant and start reading design tradeoffs directly from the diagram's geometry.
