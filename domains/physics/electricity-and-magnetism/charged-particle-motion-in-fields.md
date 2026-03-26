---
id: charged-particle-motion-in-fields
title: Charged Particle Motion in Fields
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-force-moving-charges
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

## Questions

```yaml
- question: "A proton enters a uniform magnetic field with its velocity perpendicular to the field. What happens to the proton's speed and path?"
  type: multiple-choice
  options:
    - "Speed increases and the path curves — the magnetic force accelerates the proton along its direction of motion"
    - "Speed stays constant and the path is circular — the magnetic force acts perpendicular to velocity, changing direction without doing work"
    - "Speed decreases as kinetic energy is transferred to the magnetic field"
    - "The path is helical, with the radius increasing over time as the proton gains energy"
  answer: 1
  explanation: "The magnetic force F = qv × B is always perpendicular to the velocity vector. A force perpendicular to motion cannot do work (W = F·d = 0 when F ⊥ displacement), so kinetic energy — and therefore speed — stays constant. The direction changes continuously, and since the force magnitude is also constant (|F| = qvB, with v constant), the particle follows uniform circular motion. Options A and C both imply the magnetic force does work on the particle, which is fundamentally wrong. Option D describes helical motion, which occurs when velocity has a component parallel to B — not the case here."

- question: "In a velocity selector with perpendicular electric field E and magnetic field B, a positive particle moving faster than v = E/B will:"
  type: multiple-choice
  options:
    - "Travel straight through undeflected, since it satisfies the balance condition"
    - "Be deflected in the direction of the electric force, since faster particles experience greater electric force"
    - "Be deflected in the direction of the magnetic force, since the magnetic force qvB exceeds the electric force qE"
    - "Slow down until it reaches v = E/B, then travel straight"
  answer: 2
  explanation: "At v = E/B, the electric force qE and magnetic force qvB balance exactly — zero net force, straight trajectory. For v > E/B, the magnetic force qvB > qE, so the magnetic force dominates and deflects the particle in the direction of −(v × B). The electric force does not change with speed (it depends only on q and E), but the magnetic force grows with speed. Faster particles experience net magnetic deflection; slower particles experience net electric deflection. Option D incorrectly suggests the device decelerates particles — the fields exert forces but cannot remove kinetic energy in this configuration (the magnetic force does no work)."

- question: "A magnetic field can accelerate a charged particle — that is, increase its kinetic energy — if the particle moves through a strong enough field."
  type: true-false
  answer: false
  explanation: "This is a fundamental misconception. The magnetic force F = qv × B is always perpendicular to the velocity. Since work equals force times displacement in the direction of force (W = F · d), and the magnetic force has zero component along the displacement, it does no work. A particle in a purely magnetic field maintains constant speed (and thus constant kinetic energy) forever, regardless of field strength. Only an electric field — which can have a component along the particle's motion — can change kinetic energy. This is why cyclotrons need an alternating electric field to accelerate particles, not just the magnetic field."

- question: "Two ions with identical mass-to-charge ratios (m/q) but different speeds will still strike the same location in a mass spectrometer."
  type: true-false
  answer: true
  explanation: "A mass spectrometer uses a velocity selector to ensure all ions entering the magnetic deflection region have the same speed v = E/B. Since cyclotron radius r = mv/(|q|B), and all ions have the same v and B, the radius depends only on m/q. Two ions with the same m/q will curve with the same radius regardless of any speed differences they had before the selector — the selector eliminates that variable. They land at the same location. This is why the velocity selector is an essential first stage: it collapses the variable of speed, leaving m/q as the only determinant of deflection."

- question: "Why does the magnetic force cause circular motion rather than acceleration? What fundamental property of the force is responsible?"
  type: short-answer
  answer: "The magnetic force is always perpendicular to the particle's velocity (F = qv × B is a cross product). A force perpendicular to motion can never do work — it has no component along the displacement, so it transfers no energy. Instead of speeding the particle up or slowing it down, the force continuously redirects it. Because the speed stays constant, so does the magnitude of the force (|F| = q|v||B|sin θ = qvB for perpendicular entry). A constant-magnitude force always pointing toward a fixed axis is exactly the centripetal force condition for uniform circular motion. The geometry is self-sustaining: the force stays perpendicular because the velocity keeps rotating."
  explanation: "This question tests whether students understand the cross-product geometry of the Lorentz force rather than just memorizing 'magnetic forces cause circular motion.' The key chain of reasoning is: perpendicular force → no work → constant speed → constant force magnitude → centripetal condition → circular path. Breaking any link in this chain reveals a misconception. The perpendicularity of the cross product is the root cause; everything else follows."
```

## Explainer

The magnetic force on a moving charge is F = qv × B — always perpendicular to the velocity. Because this force never has a component along the motion, it cannot do work: the particle's speed stays constant while its direction changes continuously. The result is uniform circular motion, with the magnetic force providing centripetal acceleration. Setting qvB = mv²/r gives the **cyclotron radius** r = mv/(|q|B). Heavier particles curve more gently; faster ones curve more widely; stronger fields produce tighter circles. This is why a charged particle spirals in a magnetic field rather than accelerating or decelerating — the field acts purely as a steering force.

The **velocity selector** exploits a balance between the electric and magnetic forces. Place crossed electric and magnetic fields (E pointing one way, B perpendicular) so that the electric force qE and magnetic force qvB act in opposite directions on a positive charge. Only particles with exactly v = E/B experience zero net force and travel straight through undeflected. Faster particles feel a stronger magnetic deflection; slower ones feel a stronger electric deflection — both are curved out of the beam. This device filters a beam to a single velocity without touching any particle mechanically, regardless of mass or charge magnitude.

A **mass spectrometer** chains a velocity selector to a magnetic deflection region. All ions entering the deflector have the same speed v = E/B (guaranteed by the selector), so when they enter a second uniform field B', the radius r = mv/(|q|B') depends only on the mass-to-charge ratio m/q. Ions of different masses land at different positions on a detector, separating, for example, uranium-235 from uranium-238 — the basis of isotope separation used in nuclear programs. Two ions with the same m/q always strike the same spot regardless of how they got there.

The **Hall effect** is the same physics in a conductor geometry. Current flowing through a conductor means charge carriers drifting along the wire. Place a transverse magnetic field perpendicular to this current, and the magnetic force deflects moving carriers toward one face of the conductor. Charge accumulates there, building up a transverse electric field — the **Hall voltage** — that opposes further deflection. At equilibrium, the Hall field exactly cancels the magnetic force: qE_H = qv_d B. The sign of the Hall voltage reveals whether current is carried by positive or negative charges, which is how physicists confirmed that conduction in metals is by electrons, not protons. In semiconductors, the Hall effect distinguishes between electron conduction and hole conduction, making it essential for characterizing transistor materials.
