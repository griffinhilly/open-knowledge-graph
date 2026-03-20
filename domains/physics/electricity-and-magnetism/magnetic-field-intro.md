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
- magnetic-force-on-moving-charges
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

## Explainer

You already know from your study of electric fields that a charge creates a region of influence around itself — a field — that exerts force on other charges. The **magnetic field B** is a second kind of field that exerts forces on charges, but with a crucial twist: it only acts on charges that are *moving*. A charge sitting still in a magnetic field feels nothing. This velocity-dependence is not a minor detail — it is the defining character of magnetic forces and the source of some of the most counter-intuitive results in electromagnetism.

The magnetic force on a moving charge is given by the cross product **F** = q**v** × **B**. The cross product means the force is always perpendicular to both the velocity and the field direction. Think about what this implies: since force is always perpendicular to velocity, the field can never speed up or slow down a particle — it can only change the direction of motion. A charge moving perpendicular to a uniform magnetic field traces a perfect circle, with the magnetic force providing the centripetal acceleration. This is the principle behind cyclotrons and particle accelerators. The field does no work because the displacement (along the velocity) is always perpendicular to the force.

Magnetic **field lines** encode both direction and relative strength, just as electric field lines do. But there is a fundamental difference in topology: electric field lines begin on positive charges and end on negative charges, while magnetic field lines form **closed loops** with no beginning or end. There are no magnetic monopoles — no isolated "north charge" or "south charge" analogous to an electric charge. Every bar magnet, no matter how finely you cut it, produces two poles. This is captured by one of Maxwell's equations: ∇·**B** = 0, meaning the divergence of **B** is always zero.

The sources of magnetic fields in classical electromagnetism are moving charges and currents. A long straight wire carrying current I produces circular field lines wrapping around it; the right-hand rule (curl the right hand with thumb pointing in the direction of current flow, and fingers curl in the direction of B) gives the field direction. The Earth's magnetic field, compass needles, MRI machines, and the fields of current loops all follow this same geometry. Mastering the right-hand rule and the closed-loop topology of field lines is the foundation for Biot-Savart law, Ampère's law, and electromagnetic induction that you will encounter next.
