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
- lenzs-law
- direction
- opposition
stage: advanced
status: validated
---

# Lenz's Law and Direction of Induced Currents

## Core Idea
Lenz's law states that induced currents flow in a direction to oppose the change in magnetic flux that caused them. If flux into a loop increases, induced current creates a field out; if flux decreases, induced field points in. This minimizes energy change.

## Questions

```yaml
- question: "A bar magnet with its north pole pointing downward is pulled away from (below) a horizontal conducting loop. The downward magnetic flux through the loop is therefore decreasing. What does Lenz's law predict about the induced current?"
  type: multiple-choice
  options:
    - "The induced current flows counterclockwise (viewed from above), creating an upward field to oppose the downward flux"
    - "The induced current flows clockwise (viewed from above), creating a downward field to resist the decrease in downward flux"
    - "No current is induced because the magnet is moving away, not toward the loop"
    - "The induced current flows counterclockwise to repel the magnet and speed its departure"
  answer: 1
  explanation: "Lenz's law says the induced current opposes the *change* in flux, not the flux itself. The flux is downward and decreasing, so the induced current must try to maintain that flux by creating a magnetic field pointing downward. By the right-hand rule, a clockwise current (when viewed from above) produces a magnetic field pointing downward through the loop. This also creates an attractive force on the retreating magnet — you must do work to pull the magnet away, consistent with energy conservation. Option A describes opposing the flux itself (not the change), which is the classic misconception."

- question: "Eddy current braking in trains works by passing conducting wheels through a magnetic field. What provides the braking force?"
  type: multiple-choice
  options:
    - "The magnetic field directly attracts the iron in the wheels, slowing them"
    - "Eddy currents induced in the moving conductor create magnetic forces that oppose the motion causing them"
    - "The braking force comes from friction between the magnetic field lines and the wheel surface"
    - "The induced EMF drives current into a resistor, heating it, and the wheel cools and contracts"
  answer: 1
  explanation: "As the conducting wheel moves through the magnetic field, the flux through different regions of the wheel changes, inducing closed loops of current (eddy currents) within the metal. By Lenz's law, these currents flow in directions that oppose the change in flux — which means they create forces opposing the wheel's motion. The kinetic energy of the wheel is converted to electrical energy (and then heat) in the conductor. No mechanical friction is involved in the braking itself."

- question: "If a permanent magnet is held stationary inside a coil, a steady induced current flows in the coil as long as the magnet remains inside."
  type: true-false
  answer: false
  explanation: "Faraday's law states EMF = −dΦ/dt: it is the *rate of change* of flux that drives the EMF, not the flux itself. A stationary magnet produces constant flux through the coil, so dΦ/dt = 0, and no EMF — and therefore no current — is induced. Current flows only while the flux is changing. This is a crucial distinction: the presence of a magnetic field does not induce current; only a *changing* magnetic field does."

- question: "Lenz's law is a consequence of conservation of energy: if induced currents aided the change in flux rather than opposing it, energy would be created from nothing."
  type: true-false
  answer: true
  explanation: "Imagine if induced currents aided the increase in flux: an approaching magnet would attract the loop, accelerating toward it, increasing the flux, inducing more current, creating more attraction — a runaway chain that produces energy from nothing. The fact that induced currents always oppose the change prevents this. The opposing force means you must do work to maintain the change (e.g., push a magnet toward a loop), and that work is exactly the electrical energy deposited in the circuit. Lenz's law is energy conservation applied to electromagnetic induction."

- question: "A conducting ring is dropped from rest and falls through a region of uniform, horizontal magnetic field (entering from above, exiting below). Describe how the induced current and the ring's acceleration change as it enters, passes fully through, and exits the field region."
  type: short-answer
  answer: "Entering: flux through the ring increases, so an induced current flows to oppose the increase. This creates an upward magnetic braking force, so the ring accelerates more slowly than free fall. Fully inside: the flux is constant (uniform field, ring fully enclosed), so no current is induced and no braking force acts — the ring accelerates at g. Exiting: flux decreases, inducing a current that tries to maintain the flux, again producing an upward braking force and slowing the acceleration below g."
  explanation: "The key is tracking what is changing. Only the rate of change of flux matters, not the flux itself. When the ring is partially in or out of the field, flux changes and braking occurs. When fully inside a uniform field, flux is constant and the ring is in free fall. This three-phase behavior is a direct application of Lenz's law and explains why a superconducting ring would fall at constant velocity (infinite resistance → perfect Lenz braking) or no braking at all depending on the scenario."
```

## Explainer

From Faraday's law, you know that a changing magnetic flux through a loop induces an EMF proportional to the rate of change: EMF = −dΦ/dt. But this equation gives the *magnitude* of the EMF — it doesn't immediately tell you which direction the induced current flows. Lenz's law fills that gap with a physical principle: the induced current always flows in whatever direction is needed to *oppose the change* that caused it.

The procedure for applying Lenz's law is systematic. First, identify what is changing — specifically, whether the magnetic flux through the loop is increasing or decreasing. Second, ask: what magnetic field direction would oppose that change? If flux is increasing through the loop in one direction, the induced current must create a field in the *opposite* direction to resist the increase. If flux is decreasing, the induced current must create a field in the *same* direction as the original field to resist the decrease. Third, use the right-hand rule to find which current direction produces that field. The direction you find is the direction of induced current.

Lenz's law is conservation of energy in disguise. Imagine what would happen if induced currents *aided* the change instead of opposing it: an approaching magnet would attract the loop, accelerating toward it, increasing flux, inducing more current, creating more attraction — a runaway process that would generate energy from nothing. Lenz's law forbids this. The induced current always creates a force opposing the cause — a braking effect. To push a magnet toward a loop, you must do work against this braking force, and that work is exactly the electrical energy deposited in the circuit.

This opposition principle explains a range of phenomena. Pulling a magnet out of a coil requires effort — the induced current acts to drag the magnet back in. A metal disk dropped past a magnet slows down — **eddy currents** (closed current loops induced in the bulk metal) create upward magnetic forces opposing the fall. Electric brakes on trains use this same effect: the rolling wheels cut through a magnetic field, inducing eddy currents whose braking force slows the train. In each case, Lenz's law is the single unifying principle: induced currents always act as a brake on the change in flux, transforming mechanical energy into electrical energy in the process.
