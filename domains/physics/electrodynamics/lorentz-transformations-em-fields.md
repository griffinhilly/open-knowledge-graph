---
id: lorentz-transformations-em-fields
title: Lorentz Transformations of Electromagnetic Fields
domain: physics
course: electrodynamics
prerequisites:
- id: lorentz-covariance-em
  type: hard
- id: lorentz-transformation
  type: hard
tags:
- field-transformation
- relativity
- electric-magnetic-duality
stage: advanced
status: draft
---

# Lorentz Transformations of Electromagnetic Fields

## Core Idea
Lorentz transformations relate electric and magnetic fields measured in different reference frames according to specific transformation rules. These rules reveal that E and B transform in an interdependent way: what appears as a pure electric field in one frame has a magnetic component in another, and vice versa. This 'electric-magnetic duality' demonstrates that the distinction between E and B is relative and depends on the observer's motion.

## Questions

```yaml
- question: "In frame S, a point charge is at rest, producing E⃗ ≠ 0 and B⃗ = 0 everywhere. An observer in frame S' moves at velocity v relative to S. What does the S' observer measure?"
  type: multiple-choice
  options:
    - "The same pure electric field E⃗ and B⃗ = 0, because the charge itself is unchanged"
    - "Both a modified electric field and a nonzero magnetic field, as a consequence of the Lorentz transformation"
    - "Only a magnetic field B⃗ ≠ 0, because the charge appears to be moving in S'"
    - "Zero field, because the Lorentz transformation preserves the vacuum"
  answer: 1
  explanation: "The Lorentz transformation mixes E and B: transverse field components transform as E_y′ = γ(E_y − vB_z) and B_y′ = γ(B_y + vE_z/c²). Starting from a pure E field (B = 0 in S), the S' observer finds a modified E field and a new nonzero B field — exactly the fields of a moving charge calculated by Biot-Savart. Option A is the Newtonian intuition that fields are absolute. Option C overcorrects by eliminating E. This demonstrates that the magnetic field of a moving charge is simply the electric field of that charge as seen from another frame."

- question: "A physicist argues: 'The magnetic force on a particle moving near a current-carrying wire is a distinct physical effect from electric attraction — they have different causes.' What does the relativistic treatment of field transformations reveal about this claim?"
  type: multiple-choice
  options:
    - "The claim is correct — electric and magnetic forces are fundamentally distinct phenomena with independent origins"
    - "The claim is misleading — the magnetic force in one frame is the electric (Coulomb) force in another frame; both are expressions of the same electromagnetic interaction"
    - "The claim is partially correct — the forces are equivalent only at relativistic speeds"
    - "The claim is correct for static configurations but wrong for time-varying fields"
  answer: 1
  explanation: "The wire-force example illustrates this directly: in the lab frame, a nearby moving charge experiences a magnetic force. In the charge's rest frame, Lorentz contraction increases the positive ion density of the wire, producing a net electric force. Same physical force, different descriptions in different frames. The 'distinction' between E and B is frame-dependent, not fundamental — both are components of the single electromagnetic field tensor Fᵘᵛ."

- question: "If E⃗ · B⃗ = 0 in one inertial frame, there must exist another inertial frame where E⃗ · B⃗ ≠ 0."
  type: true-false
  answer: false
  explanation: "E⃗ · B⃗ is a Lorentz invariant — all inertial observers agree on its value. If it is zero in one frame, it is zero in all frames. This is one of two key invariants (the other being E² − c²B²). If E and B are perpendicular in one frame, they remain perpendicular in every frame. Invariants carry observer-independent physical information, in contrast to the individual values of E and B which are frame-dependent."

- question: "The distinction between 'electric field' and 'magnetic field' is physically meaningful only in the context of a specific reference frame."
  type: true-false
  answer: true
  explanation: "E and B are not independently invariant physical objects — they are components of the electromagnetic field tensor Fᵘᵛ that mix under Lorentz boosts. The same field configuration can appear as a pure electric field in one frame and as a combination of electric and magnetic fields in another. Two observers disagree on how much of the field is 'electric' and how much is 'magnetic,' yet they agree on the physical effects (forces, energy). The observer-independent object is Fᵘᵛ itself."

- question: "Why does the existence of the electromagnetic field tensor Fᵘᵛ imply that the separation of fields into 'electric' and 'magnetic' parts is frame-dependent?"
  type: short-answer
  answer: "E and B are not separate 4-vectors but components of the same antisymmetric rank-2 tensor Fᵘᵛ. Under a Lorentz boost, the tensor transforms by the standard tensor transformation law, which mixes the components corresponding to E with those corresponding to B. Just as a Lorentz boost mixes time and space components of a 4-vector (so 'time' and 'space' are frame-dependent), a boost mixes the E and B components of Fᵘᵛ. What one observer labels 'electric' another calls a combination of electric and magnetic. The physical object — Fᵘᵛ — is the same in all frames; only the decomposition differs."
  explanation: "The analogy to spacetime mixing is precise: just as there is no absolute 'spatial' or 'temporal' component of a displacement (only the spacetime interval is invariant), there is no absolute 'electric' or 'magnetic' part of an electromagnetic field — only E·B and E²−c²B² are observer-independent."
```

## Explainer

You already know how coordinates and velocities transform between inertial frames under the Lorentz transformation, and you know from Lorentz covariance of electromagnetism that E⃗ and B⃗ together form the antisymmetric **electromagnetic field tensor** Fᵘᵛ. The transformation rules for the fields are simply what you get when you apply the Lorentz transformation to this tensor. For a boost with velocity v along the x-axis, the components parallel to the boost direction are unchanged (E_x′ = E_x, B_x′ = B_x), while the transverse components mix: E_y′ = γ(E_y − vB_z), E_z′ = γ(E_z + vB_y), and the corresponding equations for B′. The structure is exactly parallel to how time and space mix under a boost — but now it's E and B mixing.

The cleanest illustration is a stationary point charge. In the charge's rest frame, there is a pure electrostatic field E⃗ pointing radially outward and B⃗ = 0 everywhere. Now boost to a frame where the charge is moving (equivalently, look at the fields of a moving charge from a stationary observer's perspective). The Lorentz transformation produces both a modified electric field and a nonzero magnetic field — exactly the fields you'd calculate by applying the Biot-Savart law to the moving charge. There is no new physics: the magnetic field of a moving charge is simply the electric field of the charge *as seen from a different inertial frame*. This is the deepest meaning of **electric-magnetic duality**: E and B are not independent physical objects but two aspects of a single electromagnetic field, whose decomposition into "electric" and "magnetic" parts depends on the observer's state of motion.

Two key **invariants** survive the transformation unchanged. The quantity E² − c²B² is a Lorentz scalar: all observers agree on its value. The quantity E⃗·B⃗ is also invariant. These invariants carry real information: if E⃗·B⃗ = 0 in one frame, it is zero in all frames (so perpendicular E and B remain perpendicular under any boost). If E² > c²B² in one frame, there exists a frame where B = 0; if B² > E²/c², there exists a frame where E = 0. These conditions tell you whether a given field configuration is "more electric" or "more magnetic" in an observer-independent sense.

The transformation rules resolve the classic paradox of a current-carrying wire seen from different frames. In the wire's rest frame, there is a magnetic field surrounding the wire and zero net electric field (the wire is neutral overall). But from the frame of a drifting electron in the wire, the positive lattice ions are moving — their Lorentz-contracted spacing increases the positive charge density, producing a net electric field. The electron's drift in the lab frame corresponds to a Coulomb attraction in its own rest frame. Both descriptions predict the same physical force on a nearby test charge; they just attribute it to E in one frame and B in another. This is not coincidence — it is the Lorentz transformation guaranteeing that forces and their physical effects are the same in all inertial frames.
