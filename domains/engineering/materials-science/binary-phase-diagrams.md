---
id: binary-phase-diagrams
title: Reading and Interpreting Binary Phase Diagrams
domain: engineering
course: materials-science
prerequisites:
- id: phase-diagrams-binary-mixtures
  type: hard
- id: lever-rule
  type: soft
builds-toward:
- phase-transformations-kinetics
- heat-treatment-steels
tags:
- phase-diagrams
- binary-systems
- alloys
- equilibrium
stage: advanced
status: draft
---

# Reading and Interpreting Binary Phase Diagrams

## Core Idea
Binary phase diagrams map the stable phases present at equilibrium for different temperatures and compositions in two-component systems. Key features include single-phase regions (where one phase is stable), two-phase regions (where two phases coexist in equilibrium), and invariant reactions (eutectic, peritectic, eutectoid) where three or more phases meet. Phase diagrams enable prediction of equilibrium microstructure and serve as a guide for heat treatment design.

## Explainer

Think of a binary phase diagram as a map. The horizontal axis is composition — the fraction of component B in a mixture of A and B, running from pure A on the left to pure B on the right. The vertical axis is temperature. Every point on this map corresponds to a specific alloy at a specific temperature, and the diagram tells you which phase or phases are thermodynamically stable at that condition. Reading the map correctly is the core skill.

The most important feature is the distinction between **single-phase regions** and **two-phase regions**. In a single-phase region, the alloy exists as one homogeneous phase throughout — all atoms are in the same arrangement. In a two-phase region, two distinct phases coexist simultaneously, each with its own composition and crystal structure. When you are inside a two-phase region, a horizontal tie line connects the boundaries of the surrounding single-phase regions. The endpoints of that tie line give you the compositions of each coexisting phase at that temperature. From your prerequisite knowledge of the **lever rule**, you can calculate the *fraction* of each phase: the fraction of a phase is proportional to how far the overall composition is from that phase's boundary, divided by the full width of the two-phase region.

**Invariant reactions** are the points where three phases coexist simultaneously — a condition so constrained that it occurs only at one specific temperature and composition. The most important is the **eutectic reaction**: on cooling through the eutectic point, a liquid of fixed composition simultaneously solidifies into two solid phases. This produces the characteristic fine-scale lamellar or rod microstructure visible in eutectic alloys. The eutectic temperature is the lowest melting point in the system, which is why eutectic compositions are used in solders — they melt sharply at a lower temperature than either pure component. Peritectic and eutectoid reactions follow similar logic but involve different phase combinations (solid + liquid → solid, and solid → two solids, respectively).

The phase diagram encodes equilibrium — what the system *would* reach given infinite time. Real processing is kinetically constrained: cooling rapidly can suppress equilibrium transformations, trapping high-temperature phases at room temperature. Heat treatment deliberately exploits this gap between equilibrium and kinetics. By reading the phase diagram, an engineer can identify the temperature range where a particular phase is stable, then use cooling rate to control whether that phase is retained or transformed. This is the foundation of steel heat treatment: the iron-carbon phase diagram tells you where austenite is stable; the cooling rate determines whether it transforms to pearlite, bainite, or martensite.
