---
id: eddy-currents-and-energy-dissipation
title: Eddy Currents and Energy Dissipation
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: faraday-law-of-induction
  type: hard
- id: joule-heating-resistive-power
  type: hard
builds-toward:
- transformer-efficiency
tags:
- induction
- energy dissipation
- losses
stage: formal-systems
status: draft
---

# Eddy Currents and Energy Dissipation

## Core Idea
Changing magnetic fields induce circular currents (eddy currents) in conductors that produce fields opposing the change (Lenz's law). These eddy currents dissipate energy as Joule heat. Eddy current losses increase with the square of frequency and conductivity. Laminating conductors reduces eddy current losses by confining them to smaller loops.

## How It's Best Learned
Observe eddy current effects using a magnet and conducting plate. Calculate power dissipation from eddy currents in a plate in an AC magnetic field.

## Common Misconceptions
- Eddy currents are desirable (they dissipate energy and reduce efficiency).
- Lamination eliminates eddy currents (it reduces them by confining to smaller loops).
- Eddy currents are the same as primary circuit currents (they are separate, induced effects).

## Questions

```yaml
- question: "Why does laminating a transformer core reduce eddy current losses rather than eliminating them?"
  type: multiple-choice
  options:
    - "Laminations reduce the core's magnetic permeability, weakening the induced EMF"
    - "Laminations confine eddy currents to smaller loops, reducing the induced EMF and increasing the effective resistance of each loop, dramatically cutting dissipated power"
    - "Laminations cool the core by increasing surface area, reducing resistive heating"
    - "Laminations replace the magnetic material with a non-conducting material between sheets"
  answer: 1
  explanation: "Laminations work by confining current paths — each insulated layer limits eddy currents to loop within that thin sheet rather than across the full cross-section. Smaller loops mean smaller enclosed flux and thus smaller induced EMF; thinner conduction paths also mean higher resistance. Since P = V²/R, the combination of smaller V (EMF) and larger R reduces power loss dramatically — scaling as the square of the lamination thickness. Laminations do not eliminate eddy currents; residual currents still flow within each lamination sheet."

- question: "A transformer core operates at twice the frequency. By approximately what factor does eddy current power loss change?"
  type: multiple-choice
  options:
    - "Doubles — power is proportional to frequency"
    - "Increases by a factor of 4 — power is proportional to frequency squared"
    - "Stays the same — eddy current losses depend only on material resistance"
    - "Halves — higher frequency means current has less time per cycle to flow"
  answer: 1
  explanation: "Eddy current power loss scales with the square of frequency. At twice the frequency, the magnetic flux changes twice as fast, doubling the induced EMF. By P = V²/R, doubling voltage quadruples power. This is why high-frequency power devices (switching supplies, radio-frequency transformers) cannot use laminated steel cores — even thin laminations are insufficient at high frequencies. Ferrite cores with very high resistivity are used instead, nearly eliminating eddy current paths altogether."

- question: "Eddy currents in a falling-magnet experiment produce a braking force because the induced currents oppose the change in flux that created them."
  type: true-false
  answer: true
  explanation: "This is Lenz's law applied to eddy currents. A falling magnet increases the downward magnetic flux through the conducting plate below it. By Lenz's law, the induced eddy currents flow in a direction that opposes this increase — they create an upward magnetic field that pushes back on the falling magnet. The result is a braking force: the magnet falls more slowly than it would under gravity alone. This is the operating principle of magnetic brakes in trains, roller coasters, and laboratory damping systems."

- question: "Lamination eliminates eddy currents entirely in a transformer core."
  type: true-false
  answer: false
  explanation: "This is explicitly listed as a misconception. Lamination reduces eddy currents by confining them to smaller loops within each insulated sheet, but it does not eliminate them. Eddy currents still flow within each lamination layer — they simply cannot cross the insulating gaps between layers. The power loss is dramatically reduced (scaling as the square of lamination thickness), but only approaches zero in the limit of infinitely thin laminations or infinitely resistive material (like ferrite). In practice, some eddy current loss always remains."

- question: "Why do eddy current losses scale with the square of frequency, and what practical consequence does this have for high-frequency power devices?"
  type: short-answer
  answer: "Eddy current losses scale as frequency squared because EMF is proportional to the rate of flux change (Faraday's law), which is proportional to frequency. Doubling frequency doubles EMF, and since P = V²/R, power quadruples. At high frequencies (switching power supplies, radio-frequency transformers), even thin laminated steel cores produce unacceptable losses. The practical consequence is that high-frequency devices use ferrite cores — ceramic magnetic materials with very high electrical resistivity — which nearly eliminate eddy current paths and thus keep losses manageable at frequencies where steel would turn the core into a resistive heater."
  explanation: "The f² scaling means that eddy current losses become the dominant loss mechanism as frequency increases, outweighing other considerations. This is why AC power grid frequency is low (50–60 Hz) — keeping eddy current losses in transformers manageable. Switching power supplies operate at 50–500 kHz and require ferrite cores for the same reason. Understanding the f² relationship allows engineers to predict how losses scale and choose the right core material for the operating frequency."
```

## Explainer

Faraday's law says that any changing magnetic flux through a conducting loop induces an EMF. In a wire coil, we channel this EMF to drive current through a defined circuit. But conductors don't come in neat loops — a solid block of aluminum or steel is just a sea of free charges embedded in a conductor with no preferred path. When a changing magnetic field threads through such a bulk conductor, EMF is induced everywhere, and current flows in whatever closed loops it can find within the material. These are **eddy currents**: closed swirls of current circling inside a conductor, named by analogy to the eddies that form when water flows around an obstacle.

Lenz's law, which you know from Faraday's law, governs eddy currents just as it governs coil currents: the induced current always flows in the direction that opposes the change causing it. If a magnet falls toward a conducting plate, the eddy currents in the plate create a magnetic field that pushes back against the falling magnet — producing a braking force. This is the principle behind magnetic brakes in trains and roller coasters. Unlike friction brakes, magnetic braking produces no wear and adjusts automatically: the faster the motion, the greater the flux change, the stronger the induced currents, and the stronger the braking force.

The energy side connects directly to your prerequisite on Joule heating. Eddy currents are real currents flowing through material with finite resistance. By P = I²R (or equivalently P = V²/R in the per-loop picture), they dissipate energy as heat. The loss scales with the square of frequency: at twice the frequency, the flux changes twice as fast, doubling the induced EMF, quadrupling the current and therefore quadrupling the power dissipated. This is why **lamination** is the key engineering solution. If you slice a transformer core into thin sheets separated by thin insulating layers, you prevent eddy currents from looping across the full cross-section. Each lamination can still carry eddy currents, but they are confined to a much smaller area, with much smaller loops — and since EMF scales with the loop area while resistance increases (thinner path), the eddy current and its associated loss drop dramatically. The power lost per unit volume scales as the square of the lamination thickness, so thinner laminations are strongly favored.

This trade-off is central to power engineering: a solid iron transformer core would be far too lossy for the AC frequencies used in power grids. High-frequency devices like switching power supplies require even thinner laminations, or better yet, ferrite cores (ceramic magnetic materials with very high resistivity) that nearly eliminate eddy current paths altogether. The principle generalizes: wherever you want to carry magnetic flux efficiently without turning the material into a resistive heater, you must either restrict current paths or use materials that resist current flow.
