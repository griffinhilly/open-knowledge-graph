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

## Questions

```yaml
- question: "A bar magnet with its north pole toward a conducting loop is being pulled away. The induced current in the loop will:"
  type: multiple-choice
  options:
    - "Flow in the same direction as when the magnet was approaching"
    - "Create a magnetic field that repels the receding magnet, speeding its departure"
    - "Create a magnetic field that attracts the receding magnet, opposing the decrease in flux"
    - "Vanish immediately, since the magnet is no longer approaching"
  answer: 2
  explanation: "As the magnet recedes, the flux through the loop is decreasing. Lenz's law says the induced current must oppose the change — here, it must oppose the decrease — so it creates a field in the same direction as the original (north-facing) field to maintain the flux. By the right-hand rule this produces a current that, from the magnet's side, makes the loop look like a north pole, attracting the receding magnet. Option B has the direction exactly backwards — a field opposing the receding magnet's motion would attract it, not repel it. Option A is wrong because the direction reverses when the change reverses."

- question: "Which is the deepest reason why the induced current cannot flow in the direction that aids the flux change?"
  type: multiple-choice
  options:
    - "Faraday's law limits the magnitude of induced EMF, preventing a large enough aiding current"
    - "The resistance of the loop dissipates energy before the aiding current can grow large enough to matter"
    - "An aiding current would cause the flux to grow indefinitely, generating unlimited energy from no external source — violating conservation of energy"
    - "Lenz's law is an empirical rule with no known theoretical justification"
  answer: 2
  explanation: "If the induced current aided the flux change instead of opposing it, increasing flux would induce a current that increases the flux further, which induces more current, in a runaway chain that produces limitless energy. This violates conservation of energy, which is why it cannot happen. Lenz's law is not an empirical accident — it is conservation of energy applied to electromagnetic induction. The external agent changing the flux must do work against the opposing force, and that work is the source of the electrical energy dissipated in the loop."

- question: "Lenz's law states that the induced current opposes the magnetic flux through the loop."
  type: true-false
  answer: false
  explanation: "This is the most common misstatement of Lenz's law. The induced current opposes the *change* in flux, not the flux itself. If a large flux is steady (not changing), there is no induced current at all. If the flux is decreasing, the induced current creates a field in the same direction as the existing flux — it is 'helping' maintain the flux, which means it is opposing the decrease. Confusing flux with change in flux leads to incorrect predictions about current direction."

- question: "Magnetic braking (as in eddy-current brakes) is a direct application of Lenz's law because the induced currents always create forces that oppose the motion producing the flux change."
  type: true-false
  answer: true
  explanation: "This is correct. Any moving conductor in a magnetic field experiences flux changes that induce eddy currents; by Lenz's law, those currents flow in directions that create forces opposing the motion. This is why a magnet falling through a copper tube decelerates smoothly, why eddy-current brakes slow trains and roller coasters without contact, and why galvanometer needles are damped. In every case, faster motion means faster flux change, which means stronger opposition — a natural self-regulating mechanism."

- question: "Using the principle of conservation of energy, explain why the induced current in a conducting loop must oppose the change in flux that caused it."
  type: short-answer
  answer: "If the induced current aided the change in flux, it would create a feedback loop: increasing flux induces a current that increases the flux further, generating ever-greater electrical energy with no external energy input. This contradicts conservation of energy. The opposition enforces the energy budget: whatever agent is changing the flux — a moving magnet, a changing current — must do work against the opposing force created by the induced current. That work is the energy source. The induced current cannot produce more energy than is put in by the external agent."
  explanation: "This is why Lenz's law is sometimes stated as 'nature opposes change' — it is the electromagnetic manifestation of the universe's resistance to free energy. The minus sign in Faraday's law (ε = −dΦ/dt) encodes this thermodynamic constraint mathematically."
```

## Explainer

Faraday's law gives you the magnitude of the induced EMF: ε = −dΦ_B/dt. But it also hands you something you might be tempted to ignore — the minus sign. That minus sign is Lenz's law, and it tells you the direction of the induced current. The induced EMF drives a current that creates a magnetic field **opposing the change in flux** that produced it. To apply this correctly, the two-step procedure is: (1) determine whether flux is increasing or decreasing through the loop, then (2) use the right-hand rule to find which current direction would produce a field opposing that change.

Here is the classic scenario: a bar magnet with its north pole pointing toward a conducting loop, moving closer. The magnetic flux through the loop is increasing (more field lines penetrating it from the left). The induced current must oppose this increase — so it must create its own field pointing to the left inside the loop (away from the incoming magnet, to partially cancel the increasing flux). Curl your right hand: fingers pointing left inside the loop corresponds to a current flowing counterclockwise when viewed from the magnet's side. If the magnet is then pulled away, flux decreases, and the induced current reverses to maintain the field — now the loop acts like a magnet attracting the receding bar magnet.

The deeper reason Lenz's law must be true is conservation of energy. Suppose the induced current aided the flux change instead of opposing it: an increasing external flux would induce a current that increases the flux further, which would induce more current, which would increase the flux even more — a runaway process generating unlimited energy from nothing. This is impossible. The opposition is nature's way of enforcing energy bookkeeping. Whatever external agent is changing the flux — a moving magnet, a changing current in a nearby wire — must do work against the opposing force, and that work appears as electrical energy dissipated in the resistance of the loop.

**Magnetic braking** is a direct application. When a conducting plate moves through a magnetic field, Lenz's law predicts that the induced eddy currents will always flow in the direction that opposes the motion. The braking force on a falling magnet above a copper tube, the smooth deceleration of roller coasters using eddy current brakes, and the damping of galvanometer needle oscillations all follow the same principle: the faster you try to change the flux, the stronger the opposing current and the stronger the retarding force. Lenz's law does not prevent the change — friction does not stop motion either — but it always opposes it.

