---
id: thevenin-norton-circuit-equivalents
title: Thévenin and Norton Circuit Equivalents
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: combination-series-parallel-networks
  type: hard
- id: kirchhoffs-rules
  type: hard
builds-toward:
- maximum-power-transfer
tags:
- circuit analysis
- equivalence
- network reduction
stage: formal-systems
status: validated
---

# Thévenin and Norton Circuit Equivalents

## Core Idea
Any linear circuit can be replaced by a Thévenin equivalent: a voltage source V_th in series with resistance R_th. Equivalently, it can be represented as a Norton equivalent: current source I_N = V_th/R_th in parallel with R_N = R_th. These equivalents greatly simplify analysis by replacing complex networks with simple elements when analyzing terminal behavior.

## How It's Best Learned
For a given circuit, calculate V_th (open-circuit voltage), I_sc (short-circuit current), and R_th = V_th/I_sc. Verify equivalence by comparing terminal characteristics for different load resistances.

## Common Misconceptions
- Thévenin and Norton are fundamentally different (they are equivalent representations).
- Thévenin resistance is the internal resistance of an actual voltage source (it is the equivalent resistance seen looking into the circuit).
- These equivalents apply to nonlinear circuits (they only apply to linear circuits).

## Questions

```yaml
- question: "A circuit contains 12 resistors, 4 voltage sources, and 2 current sources. An engineer wants to test how different loads will behave when connected to two output terminals. What does the Thévenin equivalent tell her?"
  type: multiple-choice
  options:
    - "She must re-solve the full circuit for every different load value"
    - "The circuit looks like a single voltage source in series with a single resistor to any load connected at those terminals"
    - "The circuit can be simplified only if the sources are all identical"
    - "The equivalent works for this circuit only because it has more resistors than sources"
  answer: 1
  explanation: "Thévenin's theorem states that ANY linear circuit — regardless of complexity — appears to an external load as just V_th in series with R_th. The engineer computes these two values once, then uses the simple voltage-divider formula V_load = V_th × R_load / (R_th + R_load) for every different load. The theorem's power is precisely that it eliminates re-solving the full circuit for each load."

- question: "A Norton equivalent has I_N = 4 A and R_N = 10 Ω. What is the Thévenin equivalent voltage V_th?"
  type: multiple-choice
  options:
    - "0.4 V — divide current by resistance"
    - "14 V — add current and resistance"
    - "40 V — multiply current by resistance"
    - "Cannot be determined without knowing the original circuit topology"
  answer: 2
  explanation: "Thévenin and Norton are dual representations of the same terminal behavior. The conversion is V_th = I_N × R_N = 4 A × 10 Ω = 40 V, with R_th = R_N = 10 Ω. No knowledge of the original circuit is needed once you have the Norton equivalent — that is the entire point of circuit equivalents. Option D is the most tempting misconception: students think the original topology matters, but all terminal information is already captured in I_N and R_N."

- question: "Thévenin and Norton equivalents always produce identical terminal behavior — they are two representations of the same underlying circuit, not two different approximations."
  type: true-false
  answer: true
  explanation: "Thévenin (V_th in series with R_th) and Norton (I_N in parallel with R_N) are mathematically dual representations related by source transformation: I_N = V_th / R_th and R_N = R_th. Any voltage or current measured at the terminals is identical for both equivalents. The choice between them is purely one of analytical convenience."

- question: "R_th in a Thévenin equivalent is the actual internal resistance of the voltage source that exists inside the original circuit."
  type: true-false
  answer: false
  explanation: "This is a common and important misconception. R_th is the equivalent resistance seen looking back into the circuit from the terminals, computed by turning off all independent sources (replacing voltage sources with short circuits and current sources with open circuits) and finding the equivalent resistance of the remaining resistor network. An original circuit may contain no actual source resistance at all, yet still yield a non-zero R_th because of how resistors are arranged around the terminals."

- question: "Why does maximum power transfer to a load occur when R_load = R_th, and why does this matter for engineering applications?"
  type: short-answer
  answer: "With R_load = R_th, the load receives exactly half of V_th as voltage (by the voltage divider), which maximizes the power product V × I delivered to the load. For smaller R_load, more current flows but the voltage across the load is too small; for larger R_load, the voltage is close to V_th but too little current flows. The product P = V²/R is maximized at R_load = R_th."
  explanation: "The Thévenin equivalent makes this optimization transparent: without it, you would need to optimize over the full complex circuit. With it, you reduce the problem to a one-parameter comparison. This principle governs impedance matching in amplifier output stages, transmission line design, and sensor circuits — wherever transferring maximum power to a load is the design goal."
```

## Explainer

From Kirchhoff's laws and series-parallel combination, you can already solve any linear circuit — but for a circuit with many components, applying KVL and KCL directly can require solving large systems of equations. Thévenin's theorem offers a drastic shortcut: from the perspective of any pair of terminals, an entire network of resistors and sources looks like just one voltage source in series with one resistor. This is the **Thévenin equivalent**.

To find it, you need two numbers. The **Thévenin voltage** V_th is the open-circuit voltage across the terminals — what a voltmeter would read with nothing connected. This requires the full circuit analysis, but you only have to do it once. The **Thévenin resistance** R_th is the equivalent resistance seen looking back into the circuit with all independent sources turned off (voltage sources replaced by short circuits, current sources by open circuits). For the two-terminal equivalent, R_th = V_th / I_sc, where I_sc is the short-circuit current (the current that flows if you place a wire across the terminals). Once you have V_th and R_th, any load connected to those terminals sees exactly V_th in series with R_th — no matter how complex the original circuit was.

The **Norton equivalent** is the current-source dual: the same circuit appears as a current source I_N = V_th / R_th in parallel with R_N = R_th. Thévenin and Norton are interchangeable representations — a source transformation converts one to the other. The choice between them is purely one of convenience: if your load connects in series with the circuit, Thévenin is more natural; if your load connects in parallel, Norton is. Either way, the terminal behavior is identical.

The real power of these theorems appears when you want to analyze how a circuit responds to different loads. Instead of re-solving the whole circuit for each load value, you compute V_th and R_th once, then use the simple voltage divider V_load = V_th × R_load / (R_th + R_load). The **maximum power transfer theorem** — which builds directly on Thévenin equivalents — states that maximum power is delivered to a load when R_load = R_th. This has concrete engineering implications for amplifier output stages, transmission lines, and sensor circuits. The Thévenin framework reduces a complex matching problem to a one-parameter comparison.
