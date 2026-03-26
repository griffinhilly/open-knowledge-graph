---
id: magnetic-field-intro
title: Magnetic Fields
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-field
  type: soft
- id: vectors-in-two-dimensions
  type: hard
builds-toward:
- magnetic-force-moving-charges
- biot-savart-law
- magnetic-flux-and-induction
tags:
- magnetic-field
- B-field
- magnetism
- dipole
stage: formal-systems
status: validated
---

# Magnetic Fields

## Core Idea
A magnetic field B (measured in tesla, T) exerts forces on moving charges and current-carrying conductors but does no work on them since the magnetic force is always perpendicular to velocity. Magnetic field lines form closed loops — there are no magnetic monopoles — unlike electric field lines that begin and end on charges. The Earth's magnetic field, bar magnets, and current loops all produce characteristic dipole field patterns.

## How It's Best Learned
Use iron filings experiments (physical or simulated) to visualize field lines around bar magnets. Master the right-hand rule for field direction relative to current before tackling quantitative calculations.

## Common Misconceptions
- Magnetic fields do zero work on charges, so they cannot change a particle's speed — only direction.
- Magnetic monopoles do not exist in classical electromagnetism; field lines always close on themselves.
- A stationary charge experiences no magnetic force, regardless of the field strength.

## Questions

```yaml
- question: "A proton enters a region of strong uniform magnetic field perpendicular to its velocity. Which of the following correctly describes what happens?"
  type: multiple-choice
  options:
    - "The proton accelerates in the direction of the magnetic field lines"
    - "The magnetic force changes the proton's direction but not its speed, causing it to curve in a circle"
    - "The magnetic force does positive work on the proton, increasing its kinetic energy"
    - "A proton moving slowly through the field experiences a stronger force than one moving quickly"
  answer: 1
  explanation: "The magnetic force F = qv × B is always perpendicular to the velocity. Since force is perpendicular to displacement (which is along v), the force does zero work and cannot change the particle's kinetic energy or speed. It only changes direction — the result is circular motion when B is uniform and perpendicular to v. Option C is the classic misconception: students often assume a strong field accelerates particles, but magnetic fields cannot change speed, only direction."

- question: "A bar magnet is cut in half along the axis perpendicular to its length, separating the north and south poles. What do the two pieces become?"
  type: multiple-choice
  options:
    - "One piece becomes a pure north magnetic monopole; the other becomes a pure south monopole"
    - "Each piece becomes a complete dipole with its own north and south poles"
    - "Both pieces lose all magnetism because the magnetic field depended on the charge separation"
    - "One piece retains the full original field strength; the other has no field"
  answer: 1
  explanation: "There are no magnetic monopoles in classical electromagnetism. No matter how many times you cut a magnet, each piece develops its own north and south poles — the closed-loop topology of magnetic field lines is preserved at every scale. The misconception (that cutting separates the poles) reflects an analogy to positive and negative electric charges that simply does not apply to magnetism. Maxwell's equation ∇·B = 0 captures this: the divergence of B is always zero, meaning field lines never begin or end."

- question: "Because the magnetic force on a moving charge is always perpendicular to the velocity, a magnetic field alone cannot increase or decrease a charged particle's kinetic energy."
  type: true-false
  answer: true
  explanation: "Work equals force times displacement in the direction of force. Since the magnetic force is always perpendicular to the velocity (and hence to the displacement), no work is done — W = F·d = 0. Kinetic energy remains constant; only the direction of motion changes. This is why magnetic confinement in particle accelerators like cyclotrons can curve particle paths without speeding them up or slowing them down — a separate electric field is needed to actually accelerate the particles."

- question: "Magnetic field lines behave like electric field lines: they originate on north poles and terminate on south poles."
  type: true-false
  answer: false
  explanation: "Electric field lines begin on positive charges and end on negative charges — they have sources and sinks. Magnetic field lines form closed loops with no beginning or end: they emerge from one end of a magnet, arc around through the surrounding space, and re-enter through the other end, continuing through the magnet itself. There are no magnetic monopoles to serve as sources or sinks. This is captured by ∇·B = 0 (Gauss's law for magnetism), one of Maxwell's four equations."

- question: "Why does a charged particle moving perpendicular to a uniform magnetic field travel in a circle? Explain the physical mechanism, not just the formula."
  type: short-answer
  answer: "The magnetic force on the particle is always perpendicular to its velocity. Perpendicular forces change direction but not speed — exactly the condition for circular motion. As the particle curves, its velocity direction changes, and the magnetic force direction changes with it, always staying perpendicular. This continuous redirection traces a perfect circle, with the magnetic force providing the centripetal acceleration. The radius depends on the particle's mass, charge, speed, and field strength — the particle essentially orbits in the magnetic field the way a satellite orbits a planet under gravity, except gravity does do work while the magnetic force does not."
  explanation: "The physical picture is: force perpendicular to velocity → direction changes → force direction updates to stay perpendicular → closed circular orbit. This is why cyclotrons can bend particle beams without changing their energy, and why the concept of 'magnetic confinement' in fusion reactors is possible."
```

## Explainer

You already know from your study of electric fields that a charge creates a region of influence around itself — a field — that exerts force on other charges. The **magnetic field B** is a second kind of field that exerts forces on charges, but with a crucial twist: it only acts on charges that are *moving*. A charge sitting still in a magnetic field feels nothing. This velocity-dependence is not a minor detail — it is the defining character of magnetic forces and the source of some of the most counter-intuitive results in electromagnetism.

The magnetic force on a moving charge is given by the cross product **F** = q**v** × **B**. The cross product means the force is always perpendicular to both the velocity and the field direction. Think about what this implies: since force is always perpendicular to velocity, the field can never speed up or slow down a particle — it can only change the direction of motion. A charge moving perpendicular to a uniform magnetic field traces a perfect circle, with the magnetic force providing the centripetal acceleration. This is the principle behind cyclotrons and particle accelerators. The field does no work because the displacement (along the velocity) is always perpendicular to the force.

Magnetic **field lines** encode both direction and relative strength, just as electric field lines do. But there is a fundamental difference in topology: electric field lines begin on positive charges and end on negative charges, while magnetic field lines form **closed loops** with no beginning or end. There are no magnetic monopoles — no isolated "north charge" or "south charge" analogous to an electric charge. Every bar magnet, no matter how finely you cut it, produces two poles. This is captured by one of Maxwell's equations: ∇·**B** = 0, meaning the divergence of **B** is always zero.

The sources of magnetic fields in classical electromagnetism are moving charges and currents. A long straight wire carrying current I produces circular field lines wrapping around it; the right-hand rule (curl the right hand with thumb pointing in the direction of current flow, and fingers curl in the direction of B) gives the field direction. The Earth's magnetic field, compass needles, MRI machines, and the fields of current loops all follow this same geometry. Mastering the right-hand rule and the closed-loop topology of field lines is the foundation for Biot-Savart law, Ampère's law, and electromagnetic induction that you will encounter next.
