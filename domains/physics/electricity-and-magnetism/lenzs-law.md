---
id: lenzs-law
title: Lenz's Law
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: faradays-law
  type: hard
- id: conservation-of-energy
  type: soft
builds-toward:
- inductance-and-inductors
tags:
- Lenz-law
- induced-current-direction
- opposition
- energy-conservation
stage: formal-systems
status: validated
---

# Lenz's Law

## Core Idea
Lenz's law states that the direction of the induced current is such that it opposes the change in magnetic flux that caused it. It is the physical interpretation of the negative sign in Faraday's law and is a direct consequence of energy conservation — an induced current that aided the flux change would provide free energy, violating conservation of energy. In practice: if flux through a loop increases, the induced current creates a field opposing that increase; if flux decreases, the induced current creates a field to maintain it.

## How It's Best Learned
For each scenario, first determine whether flux is increasing or decreasing, then use the right-hand rule to find the direction of induced current needed to oppose the change. Practice with bar magnet approaching/receding a loop, and with a switch-opened circuit near a conductor.

## Common Misconceptions
- The induced current opposes the change in flux, not the flux itself.
- Lenz's law does not prevent the change — it merely opposes it (like friction opposes motion but doesn't stop it).
- The opposition requires energy input from whatever is changing the flux — magnetic braking is a direct consequence.

## Explainer

Faraday's law gives you the magnitude of the induced EMF: ε = −dΦ_B/dt. But it also hands you something you might be tempted to ignore — the minus sign. That minus sign is Lenz's law, and it tells you the direction of the induced current. The induced EMF drives a current that creates a magnetic field **opposing the change in flux** that produced it. To apply this correctly, the two-step procedure is: (1) determine whether flux is increasing or decreasing through the loop, then (2) use the right-hand rule to find which current direction would produce a field opposing that change.

Here is the classic scenario: a bar magnet with its north pole pointing toward a conducting loop, moving closer. The magnetic flux through the loop is increasing (more field lines penetrating it from the left). The induced current must oppose this increase — so it must create its own field pointing to the left inside the loop (away from the incoming magnet, to partially cancel the increasing flux). Curl your right hand: fingers pointing left inside the loop corresponds to a current flowing counterclockwise when viewed from the magnet's side. If the magnet is then pulled away, flux decreases, and the induced current reverses to maintain the field — now the loop acts like a magnet attracting the receding bar magnet.

The deeper reason Lenz's law must be true is conservation of energy. Suppose the induced current aided the flux change instead of opposing it: an increasing external flux would induce a current that increases the flux further, which would induce more current, which would increase the flux even more — a runaway process generating unlimited energy from nothing. This is impossible. The opposition is nature's way of enforcing energy bookkeeping. Whatever external agent is changing the flux — a moving magnet, a changing current in a nearby wire — must do work against the opposing force, and that work appears as electrical energy dissipated in the resistance of the loop.

**Magnetic braking** is a direct application. When a conducting plate moves through a magnetic field, Lenz's law predicts that the induced eddy currents will always flow in the direction that opposes the motion. The braking force on a falling magnet above a copper tube, the smooth deceleration of roller coasters using eddy current brakes, and the damping of galvanometer needle oscillations all follow the same principle: the faster you try to change the flux, the stronger the opposing current and the stronger the retarding force. Lenz's law does not prevent the change — friction does not stop motion either — but it always opposes it.

