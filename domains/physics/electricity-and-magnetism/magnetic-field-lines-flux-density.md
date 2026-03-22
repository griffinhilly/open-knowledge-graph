---
id: magnetic-field-lines-flux-density
title: Magnetic Field Lines, Flux, and Flux Density
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-field-intro
  type: hard
- id: magnetic-flux-and-induction
  type: hard
builds-toward:
- solenoid-magnetic-field-properties
tags:
- magnetism
- field visualization
- flux
stage: formal-systems
status: draft
---

# Magnetic Field Lines, Flux, and Flux Density

## Core Idea
Magnetic field lines form closed loops because there are no magnetic monopoles. The density of field lines is proportional to flux density B. Magnetic flux through a surface is Φ_B = ∫ B·dA. Unlike electric field lines, magnetic field lines never begin or end.

## Questions

```yaml
- question: "A physicist places an imaginary closed surface of arbitrary shape (like a balloon) anywhere in a magnetic field. What is the total magnetic flux through that closed surface?"
  type: multiple-choice
  options:
    - "It equals B times the total surface area"
    - "It depends on the orientation of the surface relative to the field lines"
    - "It is always exactly zero, regardless of the field strength or surface shape"
    - "It equals the number of field lines entering the surface from outside"
  answer: 2
  explanation: "Gauss's law for magnetism states ∮ B·dA = 0 for any closed surface — always. Because magnetic field lines always form closed loops (no monopoles), every field line that enters the closed surface must also exit it. The flux contributions from entering and exiting lines cancel exactly. This is fundamentally different from Gauss's law for electric fields, where a closed surface enclosing a net charge gives nonzero flux. The zero result is not a coincidence — it is a direct consequence of the nonexistence of magnetic monopoles."

- question: "A flat loop of area A sits in a uniform magnetic field of magnitude B. In which orientation does the magnetic flux through the loop equal exactly BA?"
  type: multiple-choice
  options:
    - "When the plane of the loop is parallel to the magnetic field"
    - "When the loop is tilted at 45° to the field direction"
    - "When the normal to the loop's surface is parallel to the field (the field passes perpendicularly through the loop)"
    - "When the loop is oriented so the field lines graze along its surface"
  answer: 2
  explanation: "Magnetic flux is Φ_B = BA cos θ, where θ is the angle between the field B and the surface normal. Flux is maximized (and equals BA) when θ = 0° — that is, when the field is perfectly perpendicular to the surface, meaning it passes straight through. This is when the field is parallel to the surface normal. Options A and D describe the opposite orientation (field parallel to the plane, normal perpendicular to B), which gives θ = 90° and zero flux — the most common confusion. The field threading through the loop is what counts, not the field running alongside it."

- question: "Gauss's law for magnetism states that the total magnetic flux through any closed surface is always exactly zero."
  type: true-false
  answer: true
  explanation: "This is one of Maxwell's four fundamental equations and follows directly from the nonexistence of magnetic monopoles. Because every magnetic field line forms a complete closed loop, any field line that enters a closed surface must also exit it — the inward and outward contributions to the flux integral cancel precisely. This is written ∮ B·dA = 0 and holds for any closed surface, any field configuration, and any orientation. It is the magnetic analog of Gauss's law for electric fields, but with zero on the right-hand side because there are no magnetic charges."

- question: "Magnetic field lines begin at north poles and end at south poles, analogous to how electric field lines begin at positive charges and end at negative charges."
  type: true-false
  answer: false
  explanation: "This is the central misconception to avoid. Electric field lines do begin on positive charges and end on negative charges. Magnetic field lines never begin or end anywhere — they always form complete closed loops. Outside a bar magnet, field lines arc from north to south. Inside the magnet, they continue from south pole back to north, completing the loop. There is no point where a magnetic field line originates or terminates, because there are no magnetic monopoles — no isolated north or south 'charge' from which lines could source or sink."

- question: "Why must magnetic field lines always form closed loops, and what physical fact does this requirement reflect?"
  type: short-answer
  answer: "Magnetic field lines must form closed loops because there are no magnetic monopoles — no point sources or sinks from which field lines could originate or at which they could terminate. Every magnet has both a north and a south pole; no isolated magnetic charge has ever been observed. This is encoded in Gauss's law for magnetism: ∮ B·dA = 0, meaning the total magnetic flux through any closed surface is zero. Every line entering must exit. This distinguishes magnetism fundamentally from electrostatics, where positive and negative charges allow field lines to begin and end."
  explanation: "The closed-loop property is not a visual convention but a statement of deep physics. It has consequences throughout electromagnetism: it rules out magnetic monopoles in classical theory, it constrains how magnetic fields can be configured in space, and it is why changing magnetic flux (Faraday's law) is so powerful — you can never 'trap' or 'absorb' magnetic flux the way you can with electric flux, only redirect it."
```

## Explainer

Magnetic field lines offer a visual grammar for understanding how magnetic fields are organized in space. Unlike electric field lines, which begin on positive charges and end on negative charges, **magnetic field lines always close on themselves** — they form complete loops with no beginning and no end. This is not a coincidence or a convention; it reflects a deep physical fact: there are no magnetic monopoles. Every north pole comes attached to a south pole, so there is never a point where field lines can originate or terminate.

The spacing of field lines encodes field strength: **magnetic flux density** B (measured in tesla) is high where lines are crowded together and low where they spread apart. This is the same visual convention as for electric field lines, so your intuition carries over directly. Inside a bar magnet, field lines run from south pole to north pole (completing the loop that arcs from north to south outside). Near a long straight wire carrying current, field lines form concentric circles — perfect closed loops with no beginning or end. Near a solenoid, lines emerge from one end, arc through the surrounding space, and re-enter at the other end.

**Magnetic flux** Φ_B = ∫ B·dA counts how many field lines thread through a surface. If the field is uniform and perpendicular to a flat surface of area A, the integral simplifies to Φ_B = BA. If the field makes an angle θ with the surface normal, it becomes Φ_B = BA cos θ — only the perpendicular component of B threads through. This concept directly underpins Faraday's law from your prerequisite study: changing magnetic flux through a loop induces an EMF. The flux density B makes that relationship precise by quantifying the field locally at every point.

A key consequence of closed field lines is that the total flux through any closed surface is exactly zero: ∮ B·dA = 0. This is **Gauss's law for magnetism** — the magnetic analog of Gauss's law for electric fields, but with zero on the right-hand side because there are no magnetic charges. Every field line entering a closed surface must also exit it. This constraint fundamentally distinguishes the structure of magnetism from electrostatics and has deep consequences throughout electromagnetism: it is one of Maxwell's four equations and rules out any possibility of magnetic monopoles in classical theory.
