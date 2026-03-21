---
id: voltage-and-current-source-characteristics
title: Voltage and Current Source Characteristics
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-element-types-and-definitions
  type: hard
builds-toward:
- rc-circuit-charging-and-discharging
- rl-circuit-transient-analysis
- DC-steady-state-circuit-solution
tags:
- sources
- ideal-sources
- source-characteristics
stage: formal-systems
status: draft
---

# Voltage and Current Source Characteristics

## Core Idea
An ideal voltage source maintains a constant voltage across its terminals regardless of current drawn; an ideal current source delivers a constant current regardless of the voltage across it. Real sources deviate from these ideals due to internal resistance. These abstractions allow us to model batteries, generators, and other sources in circuit analysis.

## Questions

```yaml
- question: "A real battery has an open-circuit voltage of 9 V and an internal resistance of 1 Ω. It is connected to a 2 Ω external load. What is the terminal voltage under load?"
  type: multiple-choice
  options:
    - "9 V — the battery maintains its rated voltage regardless of load"
    - "6 V — the internal resistance drops 3 V at 3 A of current"
    - "3 V — the voltage splits equally between internal and external resistance"
    - "4.5 V — the terminal voltage is always half the open-circuit voltage under load"
  answer: 1
  explanation: "Current flows: I = 9 V / (1 Ω + 2 Ω) = 3 A. The internal resistance drops I × r_s = 3 × 1 = 3 V. Terminal voltage = V_s − I·r_s = 9 − 3 = 6 V. Option A is the ideal voltage source behavior — a real source 'sags' under load because current through the internal resistance creates an internal voltage drop. This is why a weak battery may still read 9 V with no load but deliver less under load."

- question: "An ideal current source is connected to a circuit. As the external load resistance increases from 10 Ω to 10 kΩ, what happens to the current delivered by the source?"
  type: multiple-choice
  options:
    - "The current decreases proportionally as resistance increases (Ohm's law)"
    - "The current remains constant at I_s; only the terminal voltage changes"
    - "The current increases to compensate for the higher resistance"
    - "The current drops to zero because the high resistance blocks current flow"
  answer: 1
  explanation: "An ideal current source maintains constant current I_s regardless of the terminal voltage or external resistance — this is its defining characteristic. The terminal voltage adjusts to whatever value is needed: V = I_s × R_load. This is the dual of an ideal voltage source (which maintains constant voltage regardless of current). Option A reflects Ohm's law thinking, which applies to resistors, not to current sources whose whole purpose is to fix the current."

- question: "An ideal voltage source has zero internal resistance, meaning it can supply unlimited current at its rated voltage without any voltage drop."
  type: true-false
  answer: true
  explanation: "By definition, an ideal voltage source maintains V_s at its terminals for any current, from zero to infinity. Zero internal resistance means no I·r_s drop. Of course, no real physical source achieves this — real sources have finite internal resistance that causes terminal voltage to sag under heavy current draw. The ideal model is an abstraction useful for circuit analysis when the internal resistance is negligible compared to the load."

- question: "A real battery with significant internal resistance will deliver higher terminal voltage when supplying heavy current than when supplying light current."
  type: true-false
  answer: false
  explanation: "The opposite is true. Terminal voltage = V_s − I·r_s. As current I increases, the drop I·r_s increases, so terminal voltage decreases. A heavily loaded battery delivers less voltage than the same battery under light load. This is why car headlights dim briefly when you start the engine (starter motor draws huge current), and why a weak battery's terminal voltage 'collapses' under load even if it reads near full voltage when idle."

- question: "What is internal resistance in a real battery, and why does it cause the terminal voltage to be lower than the open-circuit (rated) voltage when current is flowing?"
  type: short-answer
  answer: "Internal resistance r_s represents the resistance within the battery itself — arising from electrode chemistry, electrolyte conductivity, and contact resistance. When current I flows, Ohm's law requires a voltage drop I·r_s across this internal resistance. The terminal voltage (available to the external circuit) is V_terminal = V_s − I·r_s, which is less than the ideal open-circuit voltage V_s. A larger current draw causes a larger internal drop and a lower terminal voltage."
  explanation: "The model 'ideal voltage source + series internal resistance' is also the basis for Thévenin equivalent circuits: any two-terminal network with sources and resistors can be reduced to exactly this form. Understanding that real sources sag under load is essential for battery selection, motor drive circuits, and any application where significant current will be drawn."
```

## Explainer

From your study of circuit elements and definitions, you know that circuit analysis requires models — mathematical abstractions that capture the essential behavior of physical components without every microscopic detail. Sources are the most fundamental active elements: they supply energy to the circuit. Two ideal models cover the vast majority of sources you will encounter, and understanding their defining characteristics — and the ways real sources fall short of these ideals — is essential before applying any circuit analysis technique.

An **ideal voltage source** is defined by one constraint: its terminal voltage is constant at V_s, regardless of how much current flows through it. The current is determined entirely by the external circuit — the source will supply whatever current the load demands, at the specified voltage. Graphically, the voltage source's V-I characteristic is a horizontal line at V = V_s: constant voltage for any current from −∞ to +∞. This is the model for an ideal battery or an ideal bench power supply. The internal resistance is exactly zero: no matter how much current you draw, there is no voltage drop inside the source.

An **ideal current source** is the dual: it maintains a constant current I_s regardless of the voltage that develops across its terminals. The external circuit determines the terminal voltage; the source will supply exactly I_s no matter what. The V-I characteristic is a vertical line at I = I_s. Current sources appear less often in introductory circuits but are essential for modeling transistors (a BJT's collector acts approximately like a current source controlled by the base current) and for using Norton equivalent circuits.

Real sources deviate from both ideals. A real battery has an **internal resistance** r_s in series with the ideal voltage source. When current I flows, the terminal voltage drops to V_terminal = V_s − I × r_s. A fresh AA battery might have V_s = 1.5 V and r_s ≈ 0.5 Ω; drawing 500 mA reduces the terminal voltage to 1.25 V. As the battery depletes, r_s increases, causing greater voltage sag under load. This model — ideal source plus series internal resistance — is the basis for Thévenin equivalent circuits, which you will use to simplify any two-terminal network containing sources and resistors into this same simple form.
