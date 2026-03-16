---
id: charged-particle-motion-in-fields
title: Charged Particle Motion in Fields
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-force-on-moving-charges
  type: hard
- id: electric-field
  type: soft
builds-toward:
- modern-physics
tags:
- cyclotron
- velocity selector
- mass spectrometer
- Hall effect
- charged particles
stage: formal-systems
status: validated
---

# Charged Particle Motion in Fields

## Core Idea
When charged particles move through electric and magnetic fields, the resulting trajectories enable powerful measurement and separation techniques. In a uniform magnetic field alone, a charged particle follows a circular path with cyclotron radius r = mv/(|q|B), which is the operating principle of the cyclotron particle accelerator. A velocity selector uses crossed electric and magnetic fields (E perpendicular to B) so that only particles with v = E/B pass through undeflected — particles moving faster or slower are curved out of the beam. Mass spectrometers combine a velocity selector with a magnetic deflection region to separate ions by mass-to-charge ratio, since the deflection radius depends on m/q. The Hall effect occurs when a current-carrying conductor is placed in a transverse magnetic field: the magnetic force on moving charges creates a voltage (Hall voltage) perpendicular to both current and field, used to measure magnetic field strength and determine charge carrier sign and density.

## How It's Best Learned
Derive the velocity selector condition v = E/B by balancing electric and magnetic forces, then trace the path of ions through a mass spectrometer to predict how isotopes of different mass are separated. Calculate the Hall voltage for a copper strip in a known magnetic field to connect theory to a measurable quantity.

## Common Misconceptions
- The magnetic force does no work on charged particles — it changes direction but not speed, so the kinetic energy of a particle in a purely magnetic field is constant.
- The Hall effect is not limited to metals; it is used in semiconductors to determine carrier type (electrons vs. holes) and is the basis of modern Hall-effect sensors.

## Explainer

The magnetic force on a moving charge is F = qv × B — always perpendicular to the velocity. Because this force never has a component along the motion, it cannot do work: the particle's speed stays constant while its direction changes continuously. The result is uniform circular motion, with the magnetic force providing centripetal acceleration. Setting qvB = mv²/r gives the **cyclotron radius** r = mv/(|q|B). Heavier particles curve more gently; faster ones curve more widely; stronger fields produce tighter circles. This is why a charged particle spirals in a magnetic field rather than accelerating or decelerating — the field acts purely as a steering force.

The **velocity selector** exploits a balance between the electric and magnetic forces. Place crossed electric and magnetic fields (E pointing one way, B perpendicular) so that the electric force qE and magnetic force qvB act in opposite directions on a positive charge. Only particles with exactly v = E/B experience zero net force and travel straight through undeflected. Faster particles feel a stronger magnetic deflection; slower ones feel a stronger electric deflection — both are curved out of the beam. This device filters a beam to a single velocity without touching any particle mechanically, regardless of mass or charge magnitude.

A **mass spectrometer** chains a velocity selector to a magnetic deflection region. All ions entering the deflector have the same speed v = E/B (guaranteed by the selector), so when they enter a second uniform field B', the radius r = mv/(|q|B') depends only on the mass-to-charge ratio m/q. Ions of different masses land at different positions on a detector, separating, for example, uranium-235 from uranium-238 — the basis of isotope separation used in nuclear programs. Two ions with the same m/q always strike the same spot regardless of how they got there.

The **Hall effect** is the same physics in a conductor geometry. Current flowing through a conductor means charge carriers drifting along the wire. Place a transverse magnetic field perpendicular to this current, and the magnetic force deflects moving carriers toward one face of the conductor. Charge accumulates there, building up a transverse electric field — the **Hall voltage** — that opposes further deflection. At equilibrium, the Hall field exactly cancels the magnetic force: qE_H = qv_d B. The sign of the Hall voltage reveals whether current is carried by positive or negative charges, which is how physicists confirmed that conduction in metals is by electrons, not protons. In semiconductors, the Hall effect distinguishes between electron conduction and hole conduction, making it essential for characterizing transistor materials.
