---
id: lenz-law
title: Lenz's Law and Direction of Induction
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: self-inductance
  type: soft
- id: faraday-induced-emf
  type: hard
builds-toward:
- ac-impedance
tags:
- lenz-law
- direction
- opposition
stage: formal-systems
status: validated
---

# Lenz's Law and Direction of Induction

## Core Idea
Lenz's law states that an induced EMF, current, or magnetic field opposes the change in magnetic flux that caused it. This is expressed by the minus sign in Faraday's law: ε = −dΦ_B/dt. If flux increases, the induced field opposes the increase. If flux decreases, the induced field opposes the decrease. Lenz's law is a consequence of energy conservation.

## Questions

```yaml
- question: "A bar magnet is pushed toward a conducting ring, increasing the magnetic flux through the ring. In which direction does the induced current flow?"
  type: multiple-choice
  options:
    - "In the direction that creates a magnetic field aligned with the magnet's field, assisting the increasing flux"
    - "In the direction that creates a magnetic field opposing the increasing flux — effectively repelling the approaching magnet"
    - "In a direction perpendicular to the field, producing no net opposition"
    - "The direction depends on the magnet's speed, not on the direction of flux change"
  answer: 1
  explanation: "By Lenz's law, the induced current opposes the *change* in flux. Since flux is increasing (magnet approaching), the induced current must create a field that opposes that increase — pointing opposite to the magnet's field through the loop. By the right-hand rule, this current flows in the direction that effectively repels the approaching magnet. If you instead pull the magnet away (decreasing flux), the induced current reverses to try to maintain the flux, attracting the magnet back."

- question: "Why does Lenz's law require that induced effects oppose the change in flux, rather than assist it?"
  type: multiple-choice
  options:
    - "It is an empirical observation that happens to hold in all tested cases, with no deeper theoretical explanation"
    - "Opposing the change is required by conservation of energy — if the induced effect aided the change, it would create a runaway feedback loop generating energy from nothing"
    - "Aiding the change would violate Newton's third law applied to magnetic forces"
    - "The magnetic field lines always point in opposite directions by the definition of magnetic flux"
  answer: 1
  explanation: "This is the deep point: Lenz's law is not a separate empirical rule but a consequence of energy conservation. If the induced current aided the flux increase, it would strengthen the field, inducing a larger current, which would strengthen the field further — a positive feedback loop producing infinite energy from nothing. Conservation of energy prohibits this. The minus sign in Faraday's law (ε = −dΦ_B/dt) encodes this thermodynamic requirement mathematically."

- question: "Lenz's law states that the induced magnetic field always opposes the existing magnetic flux through a loop."
  type: true-false
  answer: false
  explanation: "The induced field opposes the *change* in flux, not the flux itself. This distinction is critical. If flux is decreasing (magnet moving away), the induced current creates a field in the *same* direction as the original flux — trying to maintain it, not oppose it. If Lenz's law opposed existing flux, it would always try to reduce it to zero, which is wrong. The correct statement: the induced response always acts against whatever *change* is being imposed on the flux."

- question: "A generator produces electricity by rotating a coil in a magnetic field. By Lenz's law, the induced current in the coil creates a force that resists the rotation, which is why mechanical work must be done continuously to keep the generator running."
  type: true-false
  answer: true
  explanation: "This is a direct application of Lenz's law. As the coil rotates, the changing flux induces a current. By Lenz's law, that current flows in a direction that creates a force opposing the rotation. This is not a design flaw — it is energy conservation in action: the mechanical work done against this opposing force is exactly what becomes electrical energy in the circuit. Every electrical generator, motor back-EMF, and eddy-current brake exemplifies this principle."

- question: "Explain why Lenz's law is not just a rule for finding the direction of induced current, but a direct consequence of energy conservation."
  type: short-answer
  answer: "If the induced current aided the flux change rather than opposing it, it would strengthen the changing field, inducing an even larger current, which would strengthen the field further — a self-reinforcing loop generating unlimited energy from no input. This violates conservation of energy. The minus sign in Faraday's law (ε = −dΦ_B/dt) mathematically encodes this requirement: the induced EMF must be negative relative to the rate of flux increase. Lenz's law is the physical statement of what that minus sign means — nature always responds to oppose the change you impose, because any other response would create energy from nothing."
  explanation: "This reasoning generalizes: back-EMF in motors, the drag felt when pulling a conducting plate through a magnetic field, and the reactive behavior of inductors all follow from the same logic. In each case, the induced effect opposes what drives it, extracting real work from whatever tries to change the flux. The magnitude of the opposition equals the work done per unit charge, which is the energy being converted."
```

## Explainer

From Faraday's law, you know that a changing magnetic flux through a loop induces an EMF equal to −dΦ_B/dt. Faraday's law tells you the magnitude of this EMF and includes a minus sign — but what does that minus sign mean physically? **Lenz's law** is the physical interpretation: the induced EMF drives a current in the direction that **opposes** the change in flux that caused it.

Think of it this way: nature resists change. If you push a bar magnet toward a conducting loop, the increasing flux through the loop induces a current. By Lenz's law, that current must create a magnetic field that opposes the increase — so the induced current flows in the direction that creates a field pointing opposite to the approaching magnet's field, effectively repelling the magnet. If you pull the magnet away, flux decreases, and the induced current reverses direction to try to maintain the flux by creating a field aligned with the departing magnet, effectively attracting it back. In either case, the induced response works against whatever change you are imposing.

This opposition is required by **energy conservation**. If the induced current aided the flux increase instead of opposing it, it would create a stronger field, inducing a still larger current, creating an even stronger field — a runaway process generating energy from nothing. The minus sign in Faraday's law is thermodynamics encoded in an equation. Any time you see an induced effect, it will always act to make your life harder: the induced current in a generator opposes the rotation of the coil (you feel resistance when turning the crank), and the **back-EMF** in a motor opposes the applied voltage that drives it.

A vivid application is **self-inductance**, where a changing current in a coil induces a back-EMF in that same coil. When current increases, the growing magnetic flux through the coil's own turns induces a voltage opposing the increase — this is why inductors resist sudden changes in current and store energy in their magnetic fields. The same principle governs eddy-current braking (the drag felt by a metal plate swinging through a magnet), transformer operation, and the reactive impedance of coils in AC circuits. In every case, you can determine the direction of the induced response by asking: what change is occurring in flux, and what direction of induced current would oppose that change?
