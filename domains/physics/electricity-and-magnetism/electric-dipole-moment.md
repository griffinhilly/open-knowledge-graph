---
id: electric-dipole-moment
title: Electric Dipoles and Dipole Moment
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: equipotential-surfaces
  type: soft
- id: electric-potential-field
  type: hard
builds-toward:
- dielectric-polarization
tags:
- dipole
- moment
- polarization
stage: formal-systems
status: draft
---

# Electric Dipoles and Dipole Moment

## Core Idea
An electric dipole consists of charges +q and −q separated by distance d, with dipole moment p⃗ = qd⃗. In a uniform external field, a dipole experiences torque τ⃗ = p⃗ × E⃗ and has potential energy U = −p⃗·E⃗. Far from a dipole, the potential falls as V ∝ cos(θ)/r², defining the dipole field pattern.

## Questions

```yaml
- question: "A water molecule (a permanent electric dipole with moment p⃗) is placed in a perfectly uniform external electric field E⃗, with p⃗ initially perpendicular to E⃗. What happens to the molecule?"
  type: multiple-choice
  options:
    - "It accelerates in the direction of E⃗, because the positive end is pulled toward lower potential"
    - "It experiences a torque that tends to align p⃗ with E⃗, but no net translational force"
    - "It experiences a net force away from regions of high field strength"
    - "Nothing happens, because the equal and opposite charges produce forces that cancel in all respects"
  answer: 1
  explanation: "In a uniform field, the force on the +q end is qE⃗ and the force on the −q end is −qE⃗. These are equal in magnitude and opposite in direction, so they sum to zero net force — the dipole does not translate. However, the forces act at different locations (separated by d), creating a torque τ⃗ = p⃗ × E⃗ that rotates the dipole toward alignment with E⃗. The common misconception is that a dipole accelerates toward one plate of a capacitor in a uniform field — it does not. Net forces on dipoles require non-uniform fields."

- question: "A dipole with moment p⃗ is placed in an external electric field E⃗. In which orientation does it have the lowest potential energy (most stable equilibrium)?"
  type: multiple-choice
  options:
    - "p⃗ perpendicular to E⃗, where U = 0"
    - "p⃗ antiparallel to E⃗, where U = +pE (maximum energy)"
    - "p⃗ parallel to E⃗, where U = −pE (minimum energy)"
    - "The potential energy is the same in all orientations because the net force is always zero"
  answer: 2
  explanation: "The potential energy is U = −p⃗·E⃗ = −pE cos(θ). This is minimized when θ = 0 (p⃗ parallel to E⃗), giving U = −pE. Physically, alignment with the field is stable because any small perturbation creates a restoring torque back toward alignment. The antiparallel configuration (U = +pE) is an unstable equilibrium — any perturbation leads to rotation toward alignment, not back toward antiparallel. The perpendicular case (U = 0) is the reference point, not a stability criterion."

- question: "The electric potential of a dipole falls off as 1/r² at large distances, more rapidly than the 1/r potential of a point charge."
  type: true-false
  answer: true
  explanation: "Correct. A point charge produces V = kq/r (falls as 1/r). A dipole has equal and opposite charges that nearly cancel at large distance; the small residual goes as V = (1/4πε₀)(p cos θ)/r², which falls as 1/r². This faster falloff is the signature of the dipole: its net charge is zero, so the monopole term vanishes, and the leading contribution is the dipole term at 1/r². Higher-order charge distributions (quadrupoles, etc.) fall off even more steeply."

- question: "A dipole placed in a non-uniform electric field experiences no net translational force — only a torque."
  type: true-false
  answer: false
  explanation: "A net translational force on a dipole requires a non-uniform field. In a uniform field, the forces on +q and −q are equal and opposite, producing zero net force (but a torque). In a non-uniform field, the field strength at the +q position differs from the strength at the −q position, so the magnitudes of the two forces are unequal — the net force is non-zero. This is why polar molecules are attracted toward regions of stronger field in an inhomogeneous setup, and it underlies the physics of dielectrophoresis."

- question: "Explain why a dipole in a uniform electric field experiences a torque but not a net translational force. Use the forces on each individual charge in your explanation."
  type: short-answer
  answer: "In a uniform field E⃗, every point in space has the same field vector. The force on the +q charge is F₊ = +qE⃗ (in the direction of E⃗), and the force on the −q charge is F₋ = −qE⃗ (opposite to E⃗). Since these forces are equal in magnitude but opposite in direction, their vector sum is zero — no net translational force. However, they act at different positions separated by the dipole distance d, so they form a couple: two equal and opposite forces with different lines of action. A couple produces a pure torque τ = qEd sin θ = pE sin θ, tending to rotate the dipole until p⃗ aligns with E⃗."
  explanation: "The key is that 'equal and opposite forces' cancels net force but not torque. Torque depends on both the force magnitude and the perpendicular distance between the force lines of action (the moment arm). In a non-uniform field, the force magnitudes on +q and −q differ because the field is different at each location, breaking the cancellation and producing a net translational force in addition to the torque."
```

## Explainer

From your study of electric potential, you know that a single point charge produces a potential V = kq/r that falls as 1/r. An **electric dipole** — a pair of equal and opposite charges +q and −q separated by a small distance d — is the next level of complexity. At large distances, the positive and negative contributions to the potential nearly cancel, but not perfectly: the small offset between the charges creates a residual potential proportional to 1/r². This faster falloff is the defining signature of the dipole.

The **dipole moment** p⃗ = qd⃗ captures both the strength and orientation of the dipole in a single vector: it points from the negative charge to the positive charge, and its magnitude is qd. The far-field potential is V = (1/4πε₀) · (p⃗ · r̂)/r² = (1/4πε₀) · p cos(θ)/r², where θ is measured from the dipole axis. Notice that the potential is maximum along the axis (θ = 0), zero in the perpendicular plane (θ = 90°), and most negative anti-parallel to p⃗. The corresponding electric field lines form the classic two-lobed dipole pattern you have likely seen: field lines emerge from the positive charge, arc around, and terminate on the negative charge.

When a dipole is placed in an **external electric field** E⃗, the two charges experience equal and opposite forces that sum to zero — so there is no net force in a uniform field — but they create a net torque τ⃗ = p⃗ × E⃗ that tends to align p⃗ with E⃗. The potential energy of this alignment is U = −p⃗ · E⃗. When p⃗ is parallel to E⃗, U is at its minimum (most stable); antiparallel gives maximum U (unstable equilibrium). This torque-and-alignment physics governs the behavior of polar molecules in electric fields — a water molecule, for instance, acts as a permanent dipole that orients itself in response to applied fields.

The dipole model is not just a textbook abstraction. It is the first term in the **multipole expansion** of any charge distribution: every localized charge distribution can be described at large distance as a sum of a monopole (net charge), dipole, quadrupole, and so on. If the net charge is zero, the dipole term dominates at large r. This framework connects directly to **dielectric polarization** — your next topic — where dipole moments induced in atoms and molecules by an external field collectively modify how the material responds to electric fields.
