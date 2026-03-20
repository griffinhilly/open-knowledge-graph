---
id: lenz-law-induced-currents
title: Lenz's Law and Direction of Induced Currents
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: faraday-law-electromagnetic-induction
  type: hard
builds-toward:
- inductance-circuits-rl-transients
tags:
- lenz-law
- direction
- opposition
stage: advanced
status: draft
---

# Lenz's Law and Direction of Induced Currents

## Core Idea
Lenz's law states that induced currents flow in a direction to oppose the change in magnetic flux that caused them. If flux into a loop increases, induced current creates a field out; if flux decreases, induced field points in. This minimizes energy change.

## Explainer

From Faraday's law, you know that a changing magnetic flux through a loop induces an EMF proportional to the rate of change: EMF = −dΦ/dt. But this equation gives the *magnitude* of the EMF — it doesn't immediately tell you which direction the induced current flows. Lenz's law fills that gap with a physical principle: the induced current always flows in whatever direction is needed to *oppose the change* that caused it.

The procedure for applying Lenz's law is systematic. First, identify what is changing — specifically, whether the magnetic flux through the loop is increasing or decreasing. Second, ask: what magnetic field direction would oppose that change? If flux is increasing through the loop in one direction, the induced current must create a field in the *opposite* direction to resist the increase. If flux is decreasing, the induced current must create a field in the *same* direction as the original field to resist the decrease. Third, use the right-hand rule to find which current direction produces that field. The direction you find is the direction of induced current.

Lenz's law is conservation of energy in disguise. Imagine what would happen if induced currents *aided* the change instead of opposing it: an approaching magnet would attract the loop, accelerating toward it, increasing flux, inducing more current, creating more attraction — a runaway process that would generate energy from nothing. Lenz's law forbids this. The induced current always creates a force opposing the cause — a braking effect. To push a magnet toward a loop, you must do work against this braking force, and that work is exactly the electrical energy deposited in the circuit.

This opposition principle explains a range of phenomena. Pulling a magnet out of a coil requires effort — the induced current acts to drag the magnet back in. A metal disk dropped past a magnet slows down — **eddy currents** (closed current loops induced in the bulk metal) create upward magnetic forces opposing the fall. Electric brakes on trains use this same effect: the rolling wheels cut through a magnetic field, inducing eddy currents whose braking force slows the train. In each case, Lenz's law is the single unifying principle: induced currents always act as a brake on the change in flux, transforming mechanical energy into electrical energy in the process.
