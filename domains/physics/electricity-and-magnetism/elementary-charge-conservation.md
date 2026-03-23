---
id: elementary-charge-conservation
title: Elementary Charge and Charge Conservation
domain: physics
course: electricity-and-magnetism
prerequisites: []
builds-toward:
- coulomb-law-point-interactions
- electric-current-definition
tags:
- charge
- fundamental
- conservation
stage: formal-systems
status: validated
---

# Elementary Charge and Charge Conservation

## Core Idea
Electric charge comes in discrete units; the elementary charge e ≈ 1.6×10⁻¹⁹ C is the smallest unit. Charge is conserved in isolated systems—the total charge cannot be created or destroyed, only transferred between objects.

## How It's Best Learned
Start with simple demonstrations: rubbing materials and observing attraction/repulsion. Quantify charge through electrostatic experiments and relate to electron/proton masses.

## Common Misconceptions
- Charge can be created or destroyed. - All charge is the same type (forgetting positive/negative distinction).

## Questions

```yaml
- question: "You rub a glass rod with a silk cloth. The rod becomes positively charged. What happened at the microscopic level?"
  type: multiple-choice
  options:
    - "Positive charge was created on the glass surface by the friction energy"
    - "Electrons transferred from the glass rod to the silk cloth, leaving the rod with a deficit of negative charge"
    - "Protons were knocked free from the silk and deposited on the glass"
    - "Both positive and negative charges were created in equal amounts on the two objects"
  answer: 1
  explanation: "Charge conservation forbids creation or destruction of charge. What actually happens is electron transfer: electrons (the mobile charge carriers in most materials) move from the glass to the silk. The glass loses electrons and becomes positively charged; the silk gains electrons and becomes negatively charged. The total charge of the glass+silk system remains zero throughout. Protons are tightly bound in atomic nuclei and do not transfer during everyday friction."

- question: "An isolated system initially contains particles with charges +5e, −3e, and +2e. After a series of interactions, collisions, and charge transfers within the system, what must be true?"
  type: multiple-choice
  options:
    - "The total charge could be anything — interactions can redistribute charge freely"
    - "The total charge remains +4e — charge is conserved in isolated systems"
    - "The total charge approaches zero as positive and negative charges neutralize each other"
    - "The total charge is +4e only if no particles left the system"
  answer: 1
  explanation: "Charge conservation is absolute in isolated systems: the algebraic sum of all charges never changes. Starting with +5e − 3e + 2e = +4e, the total must remain +4e regardless of what interactions occur internally. Option C is a common misconception: positive and negative charges can neutralize each other locally (like an electron and positron annihilating), but in any such event the total charge is preserved — in annihilation, the photons produced carry zero charge, and the −e of the electron exactly cancels the +e of the positron."

- question: "In an isolated system, negative charge can be destroyed if an equal positive charge is brought nearby — the two charges annihilate and cancel."
  type: true-false
  answer: false
  explanation: "Charge conservation is absolute: charge cannot be created or destroyed in any process. When an electron (−e) and positron (+e) annihilate, they produce photons with zero charge — the total charge before (+e − e = 0) equals the total charge after (0 from photons). The charges do not 'cancel out and disappear'; rather, the charged particles transform into uncharged photons while the total charge of the system is preserved. No experiment has ever observed a net change in total charge."

- question: "A photon has zero electric charge. When a high-energy photon produces an electron-positron pair, charge conservation is satisfied because the positron carries positive charge that offsets the electron's negative charge."
  type: true-false
  answer: true
  explanation: "This is a clean example of charge conservation at the particle physics level. The photon has charge 0; the electron has charge −e; the positron has charge +e. Total charge before: 0. Total charge after: −e + e = 0. Charge is conserved exactly. This is why pair production always creates a particle and its antiparticle together — charge conservation demands it. You cannot create just an electron from a photon without violating charge conservation."

- question: "Why is it physically incorrect to say that 'rubbing creates charge'? What actually happens, and what law of physics does this illustrate?"
  type: short-answer
  answer: "Rubbing does not create charge — it transfers existing charge between objects. When two materials are rubbed together, electrons move from one object to the other based on the materials' relative electron affinities. The object that gains electrons becomes negatively charged; the object that loses electrons becomes positively charged by an equal amount. The total charge of the system (both objects combined) remains exactly what it was before rubbing — typically zero if both started neutral. This illustrates charge conservation: the total electric charge in an isolated system is constant and cannot be created or destroyed."
  explanation: "The language 'creates charge' is misleading because it implies charge came from nothing, which violates conservation. A better description is 'separates charge' — rubbing moves already-existing charge from one place to another. The conservation law is not a guideline but an exact empirical fact: it holds in every known physical process, from static electricity to nuclear reactions to particle annihilation, always with zero exceptions."
```

## Explainer

Electric charge is one of the most fundamental properties of matter, alongside mass. Unlike mass, which is always positive, charge comes in two varieties — positive and negative — and opposite charges attract while like charges repel. The **elementary charge** e ≈ 1.6×10⁻¹⁹ C is the magnitude carried by a single proton (positive) or electron (negative). All observable charge is an integer multiple of e: you can have 3e or −7e, but never 2.4e. This **quantization of charge** is a foundational fact of nature that Millikan's oil-drop experiment confirmed in 1909.

The second foundational fact is **charge conservation**: in any isolated system, the total electric charge — the algebraic sum of all positive and negative charges — never changes. When you rub a glass rod with silk, you don't create charge; you transfer it. The silk gains as many electrons as the glass loses, so the combined system remains neutral. This conservation law is as robust as conservation of energy — no experiment has ever observed a net creation or destruction of charge. In particle physics, charge is conserved even when particles are created or annihilated: a photon (charge 0) can produce an electron and positron (charges −e and +e), and the total remains zero.

It helps to build a microscopic picture. Ordinary matter is made of atoms containing positively-charged protons in the nucleus and negatively-charged electrons in the surrounding cloud. Most objects are electrically neutral because the number of protons and electrons match. When electrons are transferred between objects (as when rubbing materials together), one object becomes negatively charged and the other positively charged by equal amounts. **Conductors** allow electrons to move freely through the material; **insulators** hold electrons tightly in place, so charge can only be deposited on the surface.

Understanding that charge is discrete, conserved, and comes in two kinds is the conceptual foundation for everything that follows in electrostatics and circuit analysis. Coulomb's law quantifies the force between charges; electric current is the rate of charge flow; circuits are systems for controlling and exploiting the energy stored in charge separation. Every subsequent concept in electricity and magnetism builds on these two facts: charge is quantized, and charge is conserved.
