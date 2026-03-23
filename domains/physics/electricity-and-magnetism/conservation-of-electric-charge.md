---
id: conservation-of-electric-charge
title: Conservation of Electric Charge
domain: physics
course: electricity-and-magnetism
prerequisites: []
builds-toward:
- coulomb-force-superposition
tags:
- charge
- conservation
- continuity
stage: formal-systems
status: validated
---

# Conservation of Electric Charge

## Core Idea
Electric charge is conserved in all interactions within an isolated system. Charge cannot be created or destroyed, only transferred between objects or separated. This fundamental conservation principle is encoded in the continuity equation ∂ρ/∂t + ∇·J⃗ = 0, which relates charge density to current density.

## Questions

```yaml
- question: "A glass rod is rubbed with silk and becomes positively charged. What happened to the total electric charge of the glass-and-silk system?"
  type: multiple-choice
  options:
    - "It increased — the rubbing created new positive charge on the glass"
    - "It stayed the same — electrons moved from the glass to the silk, leaving the glass positive and the silk equally negative"
    - "It decreased — some charge was lost as heat during the rubbing"
    - "It stayed the same only if the rubbing was done in an insulated environment"
  answer: 1
  explanation: "Charge is never created or destroyed — only transferred. When glass is rubbed with silk, electrons (negative charge carriers) migrate from the glass surface onto the silk. The glass loses electrons and becomes positively charged; the silk gains those electrons and becomes equally negatively charged. The total charge of the system (glass + silk) remains exactly zero, the same as before rubbing. Charge conservation applies everywhere, not just in insulated environments."

- question: "A neutron (charge = 0) undergoes beta decay and produces a proton (charge = +1) and an electron (charge = −1). What does charge conservation require about the antineutrino emitted in this process?"
  type: multiple-choice
  options:
    - "The antineutrino must carry charge +1 to balance the proton"
    - "The antineutrino must carry charge −1 to cancel the electron"
    - "The antineutrino must carry zero charge, since the proton and electron already balance each other"
    - "Charge conservation doesn't constrain the antineutrino's charge in nuclear processes"
  answer: 2
  explanation: "Before decay: total charge = 0 (neutron). After decay: proton (+1) + electron (−1) + antineutrino = 0 requires the antineutrino to carry zero charge. And indeed, neutrinos and antineutrinos are electrically neutral. Charge conservation applies in every physical process without exception — nuclear, atomic, particle — and is precise enough to constrain properties of particles. Option D is false: charge conservation holds universally."

- question: "When an electron and a positron (anti-electron) are created together from a high-energy gamma ray, net electric charge is created in that region of space."
  type: true-false
  answer: false
  explanation: "In electron-positron pair production, a gamma ray creates one electron (charge −1) and one positron (charge +1) simultaneously. The total charge created is −1 + 1 = 0. No net charge is created. This is not coincidence — charge conservation requires that any particle created from a chargeless photon must be accompanied by its antiparticle with equal and opposite charge. The total charge of the universe remains constant in every process."

- question: "The continuity equation ∂ρ/∂t + ∇·J⃗ = 0 states that charge can disappear from one location and reappear instantaneously at a distant location."
  type: true-false
  answer: false
  explanation: "The continuity equation expresses the opposite: charge is locally conserved. If charge density decreases in a region (∂ρ/∂t < 0), it can only decrease because charge is flowing out through the boundary (∇·J⃗ > 0). Charge cannot teleport — it must flow continuously through space. This is the 'local' form of conservation: not only is the total charge in the universe constant, but charge cannot jump from one place to another without traversing the space in between. This local conservation is a stronger statement than global conservation."

- question: "Explain what the continuity equation ∂ρ/∂t + ∇·J⃗ = 0 means physically, and why it is called a 'local' conservation law."
  type: short-answer
  answer: "The continuity equation says that the rate of change of charge density at any point in space equals the negative of the divergence of current density. In plain terms: if charge is leaving a small region (∇·J⃗ > 0, net outflow), then the charge density inside that region must be decreasing (∂ρ/∂t < 0) at exactly the same rate — nothing more, nothing less. It is 'local' because it holds at every point in space independently: charge cannot disappear here and appear elsewhere without flowing continuously through the intervening space. This rules out teleportation of charge. By contrast, a 'global' conservation law would only say that the total charge in the universe is constant, without specifying that it flows."
  explanation: "The distinction between local and global conservation is physically important. A global law could be satisfied by charge vanishing in one galaxy and appearing in another simultaneously. The continuity equation rules this out — it enforces charge accounting at every infinitesimal volume. This local form is what is actually encoded in Maxwell's equations and what underpins Kirchhoff's current law: current can't pile up at a circuit node, it must flow through."
```

## Explainer

**Electric charge** is one of the most fundamental properties of matter, and its conservation is one of the most thoroughly tested laws in physics. When you rub a glass rod with silk, the rod becomes positively charged — but not because charge was created. Instead, electrons (negative charge carriers) moved from the glass onto the silk, leaving the glass with a net positive charge and the silk with an equal net negative charge. The total charge of the glass-plus-silk system is exactly what it was before: zero. Charge is always transferred, never manufactured.

This seemingly simple observation has deep consequences. No known physical process — chemical reactions, nuclear decays, particle–antiparticle creation — has ever been observed to change the net electric charge of an isolated system. When a neutron decays into a proton, an electron, and an antineutrino, the total charge before (zero) equals the total charge after (+1 − 1 + 0 = 0). When a gamma ray creates an electron–positron pair, a negative and positive charge appear simultaneously and in equal magnitude, keeping the total at zero. Conservation of charge is exact and universal.

The mathematical backbone of this principle is the **continuity equation**: ∂ρ/∂t + ∇·J⃗ = 0. Here ρ is the charge density (charge per unit volume) at a point in space, and J⃗ is the current density (charge flowing per unit area per unit time). The divergence ∇·J⃗ measures how much charge is flowing *out* of a small volume per unit time. If charge is flowing out of a region (∇·J⃗ > 0), then the charge density inside must be decreasing (∂ρ/∂t < 0) at exactly the same rate. This is the local statement of conservation: charge doesn't teleport. If charge leaves a region, it flows out continuously through the boundary.

Think of it as a bookkeeping identity for charge, identical in structure to mass conservation in fluid mechanics — which you may already know as the continuity equation for fluids. If water flows out of a volume faster than it flows in, the volume must be draining. Charge obeys the same logic. This conservation law underpins Kirchhoff's current law in circuits (the sum of currents entering a node equals the sum leaving), the behavior of capacitors, and the derivation of Gauss's law from Maxwell's equations. Every electromagnetic calculation you will do rests on this foundation.

Conservation of charge is also connected to a deep principle in theoretical physics: **Noether's theorem** tells us that every continuous symmetry of the laws of physics corresponds to a conserved quantity. Conservation of charge corresponds to a symmetry of the electromagnetic field equations under a certain class of transformations of the potentials (gauge invariance). In this sense, conservation of charge is not an empirical accident but a structural necessity of the theory. As you advance into electrodynamics and quantum field theory, this connection will become progressively more concrete and powerful.
