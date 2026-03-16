---
id: kirchhoff-circuit-laws-rules
title: 'Kirchhoff''s Circuit Laws: Voltage and Current'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electromotive-force-batteries
  type: hard
builds-toward:
- network-circuit-analysis-methods
tags:
- kirchhoff-laws
- circuit-rules
- conservation
stage: formal-systems
status: draft
---

# Kirchhoff's Circuit Laws: Voltage and Current

## Core Idea
Kirchhoff's voltage law (KVL): sum of potential changes around a closed loop is zero, ΣV = 0. Kirchhoff's current law (KCL): sum of currents into a node equals sum leaving, ΣI_in = ΣI_out. Both follow from energy conservation and charge conservation.

## Explainer

Kirchhoff's laws are conservation laws in disguise. **Kirchhoff's current law (KCL)** says that charge cannot pile up at a circuit node: whatever current flows in must flow out. Think of it like water at a pipe junction — if 5 liters per second arrive through two pipes, exactly 5 liters per second must leave through the others. In circuit terms, currents flowing into a node sum to zero when you assign a sign convention: currents in are positive, currents out are negative. KCL is charge conservation made local.

**Kirchhoff's voltage law (KVL)** says that electric potential is a single-valued function. If you walk around any closed path in a circuit and return to your starting point, your net change in altitude (potential) must be zero — just as hiking around a mountain and returning to base camp leaves your elevation unchanged. Each battery raises the potential (a gain), each resistor drops it (a loss). Going around a loop in one direction, these gains and losses must cancel exactly. KVL is energy conservation per unit charge.

To apply the laws systematically: label unknown currents with directions (guessing a wrong direction just gives a negative answer, which is fine). Write one KCL equation per independent node, and one KVL equation per independent loop. A circuit with N nodes gives N−1 independent KCL equations; a circuit with B branches and N nodes gives B−(N−1) independent loop equations. Together they produce exactly enough equations to solve for all unknown currents and voltages. This systematic approach — choose directions, write equations, solve — replaces the hit-or-miss intuition that works for simple series/parallel circuits but breaks down for complex networks with multiple loops.

A practical note on sign conventions: when you traverse a resistor in the direction of assumed current flow, the voltage *drops* (write −IR); against the current, it *rises* (write +IR). For a battery, traverse from − to + terminal gives a rise (+ε); from + to − gives a drop (−ε). Keeping these conventions consistent is the difference between getting the right answer and making an error that no amount of algebra can fix. Kirchhoff's laws provide the framework; discipline with signs provides the execution.
