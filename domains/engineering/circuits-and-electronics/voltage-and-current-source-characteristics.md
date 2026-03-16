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

## Explainer

From your study of circuit elements and definitions, you know that circuit analysis requires models — mathematical abstractions that capture the essential behavior of physical components without every microscopic detail. Sources are the most fundamental active elements: they supply energy to the circuit. Two ideal models cover the vast majority of sources you will encounter, and understanding their defining characteristics — and the ways real sources fall short of these ideals — is essential before applying any circuit analysis technique.

An **ideal voltage source** is defined by one constraint: its terminal voltage is constant at V_s, regardless of how much current flows through it. The current is determined entirely by the external circuit — the source will supply whatever current the load demands, at the specified voltage. Graphically, the voltage source's V-I characteristic is a horizontal line at V = V_s: constant voltage for any current from −∞ to +∞. This is the model for an ideal battery or an ideal bench power supply. The internal resistance is exactly zero: no matter how much current you draw, there is no voltage drop inside the source.

An **ideal current source** is the dual: it maintains a constant current I_s regardless of the voltage that develops across its terminals. The external circuit determines the terminal voltage; the source will supply exactly I_s no matter what. The V-I characteristic is a vertical line at I = I_s. Current sources appear less often in introductory circuits but are essential for modeling transistors (a BJT's collector acts approximately like a current source controlled by the base current) and for using Norton equivalent circuits.

Real sources deviate from both ideals. A real battery has an **internal resistance** r_s in series with the ideal voltage source. When current I flows, the terminal voltage drops to V_terminal = V_s − I × r_s. A fresh AA battery might have V_s = 1.5 V and r_s ≈ 0.5 Ω; drawing 500 mA reduces the terminal voltage to 1.25 V. As the battery depletes, r_s increases, causing greater voltage sag under load. This model — ideal source plus series internal resistance — is the basis for Thévenin equivalent circuits, which you will use to simplify any two-terminal network containing sources and resistors into this same simple form.
