---
id: circuit-topology-and-elements
title: Circuit Topology and Basic Circuit Elements
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-current-and-resistance
  type: hard
- id: ohms-law
  type: hard
builds-toward:
- series-circuits-resistance-voltage
- parallel-circuits-conductance-current
tags:
- circuits
- network analysis
- components
stage: formal-systems
status: draft
---

# Circuit Topology and Basic Circuit Elements

## Core Idea
A circuit is a closed path for current flow containing sources and elements. Series connections have identical current; parallel connections have identical voltage. Ideal elements are characterized by simple voltage-current relationships: V = IR for resistors, Q = CV for capacitors, V = L(dI/dt) for inductors.

## Explainer

From your study of Ohm's law and electric current, you know that current flows through a conducting path when a potential difference drives it, and that resistance quantifies how much a material opposes that flow. A **circuit** extends this idea into a network: instead of a single resistor, you have multiple components connected in a closed loop. The **topology** of that network — which elements connect to which — determines how current distributes and how voltages divide.

The two fundamental topologies are series and parallel. In a **series connection**, every element shares the same current — there is only one path for charge to flow, so the same number of coulombs per second must pass through each element. Voltages, however, add: the total voltage across the series chain equals the sum of individual drops. In a **parallel connection**, the situation inverts: every element shares the same voltage across its terminals, but current divides among the branches. Charge splits at the junction, with more flowing through lower-resistance paths. Recognizing which topology you are dealing with is the first step in any circuit analysis.

Beyond resistors, real circuits contain **capacitors** and **inductors** — components whose behavior depends on how voltages and currents change over time. A capacitor stores charge on two conducting plates separated by an insulator; the charge stored is proportional to the voltage across it: Q = CV, where C is the **capacitance** in farads. When voltage changes, the capacitor draws or supplies current to adjust its stored charge. An **inductor** — typically a coil of wire — stores energy in the magnetic field it creates when current flows. Its governing equation, V = L(dI/dt), tells you that a voltage appears across the inductor only when current is *changing*; it resists changes in current the same way a mass resists changes in velocity. Resistors, capacitors, and inductors are the three passive building blocks of virtually every circuit you will analyze.

The power of circuit topology is that it lets you apply a handful of rules — Ohm's law, Kirchhoff's voltage law (the sum of voltages around any closed loop is zero), and Kirchhoff's current law (the sum of currents into any junction is zero) — to predict behavior in arbitrarily complex networks. Whether analyzing a smartphone amplifier or a power grid, you are always identifying the topology first, labeling elements, then writing the governing equations. The series and parallel cases you study now are the building blocks that all network analysis reduces to.
