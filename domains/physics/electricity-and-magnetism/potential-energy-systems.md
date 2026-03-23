---
id: potential-energy-systems
title: Electric Potential Energy in Charge Systems
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-potential-definition
  type: hard
builds-toward:
- capacitance-definition
- energy-density-electric-field
tags:
- energy
- work
- configuration
stage: formal-systems
status: validated
---

# Electric Potential Energy in Charge Systems

## Core Idea
Potential energy U = qV for a charge q at potential V. For systems of multiple charges, U = ½Σᵢ qᵢVᵢ (factor of ½ avoids double counting). Energy is required to assemble charges against the field.

## Questions

```yaml
- question: "For a system of three charges, you compute q₁V₁ + q₂V₂ + q₃V₃, where Vᵢ is the total potential at charge i due to the other two charges. Why must you multiply this sum by ½ to get the correct potential energy?"
  type: multiple-choice
  options:
    - "Because Vᵢ includes the charge's own self-energy, which must be halved to remove it"
    - "Because each pairwise interaction U₁₂ appears once in q₁V₁ and once in q₂V₂ — the raw sum counts every pair twice"
    - "Because the ½ reflects that only half the energy is stored in the electric field; the rest is kinetic"
    - "Because the formula applies only to point charges, and ½ corrects for the extended-charge approximation"
  answer: 1
  explanation: "When you compute q₁V₁, the potential V₁ at charge 1's location includes contributions from charges 2 and 3 — so q₁V₁ contains the interaction energy U₁₂ and U₁₃. Similarly, q₂V₂ contains U₁₂ and U₂₃ again. Every pairwise interaction is counted twice in the raw sum. The factor of ½ corrects for this double-counting. The same reason underlies the ½ in the capacitor energy formula U = ½CV²."

- question: "A capacitor is charged to voltage V with charge Q on its plates. A student argues that the stored energy should be QV (charge times voltage), not ½QV. What physical reasoning explains the factor of ½?"
  type: multiple-choice
  options:
    - "Half the energy is stored in the electric field and half remains on the plates as surface energy"
    - "The voltage across the capacitor builds from 0 to V during charging; the average voltage during charge transfer is V/2, so total work done is Q × (V/2) = ½QV"
    - "The factor of ½ comes from the quantum mechanical zero-point energy of the capacitor"
    - "Energy is lost to resistance during charging, so only half of QV is actually stored"
  answer: 1
  explanation: "As charge accumulates on the capacitor, the voltage increases proportionally from 0 to the final value V. Each infinitesimal charge dq transferred must be moved against the current voltage q/C, so dW = (q/C)dq. Integrating from 0 to Q gives W = Q²/(2C) = ½QV = ½CV². The factor ½ is not a correction or loss — it reflects that the potential is not constant during charging, so you cannot simply multiply the final Q by the final V. The same ½ arises from the double-counting argument in the assembly formula."

- question: "Assembling two positive charges from infinite separation to a finite distance releases energy, because like charges naturally attract."
  type: true-false
  answer: false
  explanation: "Like charges repel. Work must be done against the repulsive force to bring two positive charges closer together — this requires energy input, not energy release. The potential energy U = kq₁q₂/r is positive for like charges, reflecting stored energy that would be released if the charges flew apart to infinity. Opposite charges attract: assembling them releases energy (U < 0), and energy must be supplied to separate them. The sign of U directly encodes this: positive U = energy was stored (forced together against repulsion), negative U = bound configuration (held together by attraction)."

- question: "For a single charge q placed at a location where the electric potential is V, the potential energy is U = qV with no factor of ½."
  type: true-false
  answer: true
  explanation: "The factor of ½ only appears when summing qᵢVᵢ over a system of multiple interacting charges, to correct for double-counting each pair. For a single test charge q at a location where an external potential V has already been established, there is no double-counting: the charge interacts with the external field, and the energy is simply U = qV. The ½ is not a universal factor — it is a correction for a specific counting issue in the multi-charge assembly formula."

- question: "Explain why the formula for total potential energy of a system of charges is U = ½ΣᵢqᵢVᵢ rather than ΣᵢqᵢVᵢ, and identify at least one other formula in electrostatics that contains a ½ for the same reason."
  type: short-answer
  answer: "The raw sum ΣᵢqᵢVᵢ counts each pairwise interaction twice: the interaction between charges i and j appears in both qᵢVⱼ and qⱼVᵢ. Dividing by 2 corrects for this. The same factor appears in the capacitor energy U = ½CV² = ½QV: as charge builds up on a capacitor, each increment dq is transferred at voltage q/C, and integrating gives the ½. The factor also appears in the energy density of the electric field, u = ½ε₀E², for the same underlying reason — all three formulas count the self-consistent assembly of a charge distribution."
  explanation: "A useful mnemonic: whenever you sum over all charges or fields in a self-consistent system (where each element contributes to the field felt by every other), a factor of ½ appears to avoid double-counting. It shows up throughout both electrostatics and magnetostatics (magnetic energy density u = B²/(2μ₀), inductor energy U = ½LI²)."
```

## Explainer

From your study of electric potential, you know that the electric potential V at a point in space is the potential energy per unit charge placed there. This gives the simplest formula in this topic: if a charge q sits at a location where the potential is V, its potential energy is U = qV. This is a direct product — no integration required. The sign matters: a positive charge at a positive potential has positive potential energy (it would release energy if allowed to move to lower potential); a positive charge at a negative potential has negative potential energy (it is in a bound configuration).

The subtlety arises with **systems of multiple charges**: what is the total potential energy stored in an assembly of N charges? You might try summing qᵢVᵢ over all charges, but this double-counts: charge 1's interaction with charge 2 is identical to charge 2's interaction with charge 1, and a naive sum counts each pair twice. The correct result is U = ½Σᵢ qᵢVᵢ, where Vᵢ is the total potential at the location of charge i due to all other charges. The factor of ½ is the fix for double-counting, and it appears throughout electrostatics whenever you move from pairwise interactions to a self-consistent sum.

Think of assembling the system step by step, bringing charges in from infinity one at a time. The first charge costs no energy (no existing field to work against). The second charge must be brought in against the field of the first, costing U₁₂ = kq₁q₂/r₁₂. The third charge must be brought in against the fields of both previous charges, costing U₁₃ + U₂₃. The total is the sum over all unique pairs — which is exactly what the ½Σᵢ qᵢVᵢ formula computes. This assembly energy equals the energy stored in the electric field throughout all space, a deep connection that becomes explicit when you study energy density of the electric field.

The practical consequence is that **energy is required to assemble like charges and is released when opposite charges are brought together**. The binding energy of charge distributions — from capacitors (charges on two plates held at a potential difference) to atomic electron shells — is computed from exactly this accounting. For a capacitor, the stored energy U = ½QV = ½CV² emerges directly from this framework: the ½ has the same origin as the ½ in the charge assembly formula.

