---
id: magnetic-field-definition
title: Definition and Properties of Magnetic Field
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-force-moving-charges
  type: hard
builds-toward:
- biot-savart-law-applications
- ampere-law-applications
tags:
- magnetic-field
- definition
- units
stage: formal-systems
status: validated
---

# Definition and Properties of Magnetic Field

## Core Idea
Magnetic field B is defined via the Lorentz force F = q(v × B); units are tesla (T) or weber/m² (Wb/m²). Magnetic field lines are continuous (no magnetic monopoles): ∇⋅B = 0. Field circulates around currents.

## Questions

```yaml
- question: "A proton enters a region of uniform magnetic field with speed v perpendicular to B. Which of the following describes its subsequent motion?"
  type: multiple-choice
  options:
    - "It moves in a circle at constant speed, because the magnetic force is always perpendicular to v"
    - "It accelerates along the field direction, gaining speed"
    - "It spirals outward, gaining kinetic energy from the field"
    - "It decelerates and stops, as the magnetic force opposes motion"
  answer: 0
  explanation: "The magnetic force F = q(v × B) is always perpendicular to the velocity. A force perpendicular to velocity changes direction but does no work (W = F · ds = 0 when F ⊥ v). Since no work is done, kinetic energy is constant and speed does not change. The force acts as a centripetal force, curving the path into a circle. Options B, C, and D all involve speed changes, which require work — something the magnetic force cannot do."

- question: "A bar magnet is cut in half. What happens to the magnetic poles?"
  type: multiple-choice
  options:
    - "Each half becomes a complete magnet with its own north and south pole — you cannot isolate a magnetic monopole"
    - "One half has only the north pole; the other has only the south pole"
    - "Both halves lose their magnetism, since the poles cancel each other"
    - "The north pole migrates to the cut surface of one half; the south pole migrates to the other"
  answer: 0
  explanation: "The condition ∇·B = 0 (no magnetic monopoles) means magnetic field lines always form closed loops — there are no isolated magnetic 'charges' analogous to electric charges. Cutting a magnet does not isolate a pole; each half develops new poles at the cut surface. Unlike electric field lines that begin on + charges and end on − charges, magnetic field lines have no sources or sinks."

- question: "A magnetic field can do positive work on a moving charged particle, increasing its kinetic energy."
  type: true-false
  answer: false
  explanation: "The magnetic force F = q(v × B) is always perpendicular to the velocity v. Work requires a force component parallel to displacement. Since the magnetic force is perpendicular to motion at every instant, the work done is always zero: W = ∫F · ds = 0. A magnetic field can only change the direction of a moving charge, never its speed or kinetic energy."

- question: "Magnetic field lines always form closed loops with no starting or ending points."
  type: true-false
  answer: true
  explanation: "The equation ∇·B = 0 states that the divergence of B is zero everywhere — there are no magnetic monopoles. In vector calculus, zero divergence means field lines have no sources or sinks. Contrast with the electric field: ∇·E = ρ/ε₀ shows that electric field lines begin on positive charges and end on negative ones. Magnetic field lines circulate in closed loops around the currents that produce them, never starting or stopping anywhere."

- question: "Why does the magnetic force on a moving charge do no work? Explain using the geometry of the cross product F = q(v × B)."
  type: short-answer
  answer: "The cross product v × B is always perpendicular to v. Since the magnetic force F = q(v × B) is perpendicular to the velocity, it is also perpendicular to the displacement at every instant. Work is defined as W = F · ds; a force perpendicular to displacement contributes zero. Therefore the magnetic force does no work, cannot transfer energy to the charge, and can only change the direction of motion — not the speed."
  explanation: "This explains why magnets can steer charged particles (in particle accelerators and the Earth's magnetosphere) without accelerating them — they act as direction-changers, not speed-changers. The practical implication is also why current-carrying wires can experience magnetic forces: the force acts on the collective drift of charge carriers constrained by the wire, so the wire is pushed even though individual electrons cannot gain net kinetic energy from B alone."
```

## Explainer

You have already learned that a moving charge experiences a magnetic force. That force depends on the charge's velocity — but velocity relative to what, and through what? The magnetic field **B** is the answer: it is the field permeating space that mediates the interaction between moving charges. Just as the electric field E tells you the force per unit charge on a stationary test charge, the magnetic field B tells you the force per unit charge per unit velocity on a moving one, with the crucial twist that the force direction depends on the cross product v × B.

The defining equation F = q(v × B) has several important geometric consequences that follow directly from the cross product. The force is always **perpendicular** to both the velocity and the field — which means the magnetic force does no work on the charge (it cannot speed it up or slow it down, only change its direction). A charge moving parallel to B feels no force at all; the force is maximum when v is perpendicular to B. For a positive charge moving in the +x direction through a field pointing in the +z direction, the force is in the +y direction; reverse the charge sign or reverse the velocity, and the force reverses. The right-hand rule encodes all of this geometry. Units of B are **teslas (T)**: one tesla is the field strength that exerts 1 N of force on a 1 C charge moving at 1 m/s perpendicular to the field.

The deep structural property of the magnetic field is stated by ∇·B = 0: there are no **magnetic monopoles**. Electric field lines begin on positive charges and end on negative charges — but magnetic field lines have no beginnings or endings. They form closed loops. Break a bar magnet in half and you get two smaller magnets, each with their own north and south poles, not an isolated north pole. This is a fundamental symmetry distinction between electricity and magnetism: the electric field has sources (charges), but the magnetic field does not. All magnetic fields are produced by electric currents (moving charges) or changing electric fields. The field "circulates" around its current source rather than radiating away from it — a hint of the Biot-Savart and Ampère's law physics you will develop next.

The **tesla** is a large unit for everyday purposes: the Earth's magnetic field is about 50 microtesla, MRI machines operate around 1–3 T, and the strongest continuous laboratory magnets reach about 45 T. When you study how currents create magnetic fields via Biot-Savart and Ampère's law, you will be computing the B field produced by specific current configurations. The framework you are building now — that B is defined by its force on moving charges and its lines form closed loops — is the foundation for all of that analysis.
