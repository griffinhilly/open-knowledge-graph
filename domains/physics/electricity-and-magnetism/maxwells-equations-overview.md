---
id: maxwells-equations-overview
title: Maxwell's Equations
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: gauss-law
  type: hard
- id: amperes-law
  type: hard
- id: faradays-law
  type: hard
- id: dielectrics
  type: soft
- id: curl-and-divergence
  type: soft
- id: divergence-theorem
  type: soft
- id: stokes-theorem
  type: soft
- id: energy-stored-in-fields
  type: soft
- id: maxwell-equations-overview
  type: soft
builds-toward:
- electromagnetic-waves
tags:
- Maxwell
- displacement-current
- unification
- electromagnetism
stage: advanced
status: validated
---
# Maxwell's Equations

## Core Idea
Maxwell's four equations unify electricity and magnetism into a single coherent theory. They are: (1) Gauss's law for E, ∮ E · dA = Q_enc/ε₀; (2) Gauss's law for B, ∮ B · dA = 0 (no monopoles); (3) Faraday's law, ∮ E · dl = −dΦ_B/dt; (4) Ampère-Maxwell law, ∮ B · dl = μ₀(I_enc + ε₀ dΦ_E/dt). Maxwell's key addition was the displacement current ε₀ dΦ_E/dt, which completes the symmetry between E and B and predicts that changing electric fields create magnetic fields — leading directly to electromagnetic waves.

## How It's Best Learned
Study each equation as a previously derived result (Gauss, Faraday, Ampère), then focus specifically on what Maxwell added — the displacement current — and why it was necessary to conserve charge at a capacitor gap. Verify that the equations in vacuum predict wave solutions.

## Common Misconceptions
- Maxwell did not discover most of these laws — his contribution was the displacement current term and the synthesis.
- The displacement current is not a real current (no charge moves); it is a changing electric flux.
- These four equations, in principle, describe all classical electromagnetic phenomena.

## Questions

```yaml
- question: "Without the displacement current term, what problem arises when applying Ampère's law to a circuit with a charging capacitor?"
  type: multiple-choice
  options:
    - "The magnetic field around the wire becomes infinite as the capacitor charges"
    - "The value of ∮ B · dl depends on which surface bounded by the Amperian loop you choose — a flat disk through the wire gives current I, but a balloon surface through the gap gives zero"
    - "Gauss's law for B gives a non-zero result inside the capacitor, implying magnetic monopoles"
    - "The electric field inside the capacitor cannot be calculated because the boundary conditions are incomplete"
  answer: 1
  explanation: "Ampère's original law, ∮ B · dl = μ₀I_enc, requires a surface bounded by the Amperian loop. For a loop around the wire feeding a capacitor, two valid surfaces exist: a flat disk that the wire pierces (current I passes through) and a balloon surface passing between the plates (no current passes through). These give different answers for the same path integral — a contradiction that signals the law is inconsistent for time-varying fields. Maxwell's displacement current term ε₀ dΦ_E/dt fixes this: the changing electric field between the plates contributes as if it were a current, giving the same answer for both surfaces."

- question: "How does Maxwell's addition of the displacement current lead directly to the prediction of electromagnetic waves?"
  type: multiple-choice
  options:
    - "The displacement current provides a physical medium through which light can propagate, replacing the aether"
    - "With the displacement current, Faraday's law and Ampère-Maxwell form a coupled system: changing E creates B and changing B creates E, producing a wave equation in vacuum with speed 1/√(μ₀ε₀)"
    - "The displacement current increases the effective speed of electric currents in conductors, and light is simply very fast current propagation"
    - "Maxwell's equations require accelerating charges to radiate, and this radiation was identified with light"
  answer: 1
  explanation: "The key is taking the curl of Faraday's law and substituting Ampère-Maxwell. Faraday: ∇ × E = −∂B/∂t. Ampère-Maxwell in free space: ∇ × B = μ₀ε₀ ∂E/∂t. Combining these gives ∇²E = μ₀ε₀ ∂²E/∂t² — a wave equation with speed v = 1/√(μ₀ε₀). Computing from known constants gives exactly the measured speed of light. Without the displacement current, Ampère's law has no ∂E/∂t term, the symmetry between E and B is broken, and no wave equation emerges. The displacement current is not optional — it is what makes electromagnetic waves possible."

- question: "The displacement current ε₀ dΦ_E/dt is not an actual electric current — no charge moves when it is nonzero."
  type: true-false
  answer: true
  explanation: "Despite the name 'current,' the displacement current involves no motion of electric charges. It represents a changing electric flux — the rate at which the electric field strength is changing through a surface. Maxwell called it a 'current' because it plays the same mathematical role in Ampère's law as real current does, and because it has units of amperes. But physically, it is a field quantity, not a flow of charge. This is why displacement current exists in a vacuum between capacitor plates where no charges are present."

- question: "Maxwell discovered all four of the equations that bear his name."
  type: true-false
  answer: false
  explanation: "This is a common misconception the topic explicitly addresses. Gauss's law for E was developed by Gauss; Gauss's law for B (no magnetic monopoles) was known before Maxwell; Faraday's law was Faraday's discovery; and the original Ampère's law was Ampère's. Maxwell's contribution was recognizing that Ampère's law was inconsistent for time-varying fields, adding the displacement current term to correct it, and synthesizing all four equations into a unified system — which revealed that light is an electromagnetic wave."

- question: "Explain why the displacement current term was logically necessary — what would go wrong mathematically without it — and what physical insight it encodes."
  type: short-answer
  answer: "Without the displacement current, Ampère's law ∇ × B = μ₀J is only mathematically consistent for steady currents. The inconsistency appears by taking the divergence of both sides: ∇ · (∇ × B) = 0 always (divergence of curl is zero), but ∇ · (μ₀J) = −μ₀ ∂ρ/∂t ≠ 0 when charge is accumulating (as in a charging capacitor). Maxwell's term ε₀ ∂E/∂t has divergence ∂ρ/∂t (from Gauss's law), which exactly cancels the charge accumulation term and restores mathematical consistency. The physical insight is the symmetry: just as Faraday showed that a changing B creates E, Maxwell's correction shows that a changing E creates B. This symmetric coupling is what allows electromagnetic fields to sustain themselves through space — the mechanism for wave propagation."
  explanation: "The displacement current serves a double role: it is both a mathematical necessity (required by charge conservation) and a physical discovery (a new relationship between changing electric fields and magnetic fields). These two aspects are not coincidental — the mathematical inconsistency in Ampère's law was pointing toward a genuine physical truth that Maxwell uncovered."
```

## Explainer

Each of Maxwell's four equations is a law you have already studied. What Maxwell did was assemble them, notice an inconsistency in one of them, fix it with a single added term, and discover — to his apparent astonishment — that the corrected system predicted the existence of electromagnetic waves traveling at the speed of light. The synthesis is one of the great achievements in the history of physics.

The first two equations are the Gauss's laws. **Gauss's law for E**, ∮ E⃗ · dA⃗ = Q_enc/ε₀, says electric field lines begin on positive charges and end on negative ones — field lines have sources and sinks. **Gauss's law for B**, ∮ B⃗ · dA⃗ = 0, says magnetic field lines never begin or end: there are no magnetic monopoles, and every field line is a closed loop. These two equations constrain the divergence (source structure) of the two fields.

The next two equations are the curl laws — they describe how the fields circulate and how they generate each other. **Faraday's law**, ∮ E⃗ · dL⃗ = −dΦ_B/dt, says a changing magnetic flux induces a circulating electric field. This is the principle behind generators, transformers, and inductors. The original **Ampère's law**, ∮ B⃗ · dL⃗ = μ₀I_enc, says a current produces a circulating magnetic field. Maxwell noticed a problem: apply the divergence theorem to Ampère's law and you get a statement that only holds for steady currents. At a charging capacitor, current flows in the wire but not between the plates — yet charge is accumulating, meaning electric flux is changing. Maxwell added the **displacement current** term, ε₀ dΦ_E/dt, to give: ∮ B⃗ · dL⃗ = μ₀(I_enc + ε₀ dΦ_E/dt). This term completes the symmetry: just as a changing B creates E (Faraday), a changing E creates B (Ampère-Maxwell).

That symmetry has profound consequences. In free space with no charges or currents, the four equations reduce to two coupled equations relating E⃗ and B⃗. Take the curl of Faraday's law, substitute Ampère-Maxwell, and the result is ∇²E⃗ = μ₀ε₀ ∂²E⃗/∂t² — a **wave equation**. The predicted speed is 1/√(μ₀ε₀), which when computed from the known values of μ₀ and ε₀ gives exactly the measured speed of light. This was not a coincidence; it was the discovery that light is an electromagnetic wave. The unification of electricity, magnetism, and optics into four equations is the moment classical physics reached its apex — and the tension those equations would later create with Newtonian mechanics set the stage for special relativity and quantum mechanics.
