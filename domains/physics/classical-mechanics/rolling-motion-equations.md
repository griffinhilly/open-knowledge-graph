---
id: rolling-motion-equations
title: 'Rolling Motion Without Slipping: Equations and Analysis'
domain: physics
course: classical-mechanics
prerequisites:
- id: rolling-without-slipping
  type: hard
- id: rigid-body-planar-motion
  type: hard
builds-toward:
- gyroscopic-motion-precession
tags:
- rolling
- constraints
- motion
stage: formal-systems
status: validated
---

# Rolling Motion Without Slipping: Equations and Analysis

## Core Idea
Rolling without slipping means the contact point has zero velocity, giving the constraint v_cm = Rω. This reduces the degrees of freedom and allows complete analysis of motion down inclines, through loops, and in collisions.

## Questions

```yaml
- question: "A hollow cylinder (I = mR²) and a solid cylinder (I = ½mR²) of identical mass and radius are released from rest at the top of the same incline. Which reaches the bottom first, and why?"
  type: multiple-choice
  options:
    - "The hollow cylinder, because its mass concentrated at the rim gives it more rotational momentum"
    - "They arrive at the same time, because they have identical masses and the same gravitational force acts on both"
    - "The solid cylinder, because its smaller moment of inertia means less gravitational energy goes into rotation, leaving more for translational acceleration"
    - "The hollow cylinder, because distributing mass at the rim increases the total kinetic energy available"
  answer: 2
  explanation: "The acceleration is a_cm = g sin θ / (1 + I/mR²). For the solid cylinder (I = ½mR²): a_cm = (2/3)g sin θ. For the hollow cylinder (I = mR²): a_cm = (1/2)g sin θ. The solid cylinder accelerates faster and wins. The rolling constraint forces some gravitational PE into rotational KE; the more mass concentrated at the rim, the larger I/mR², the more energy goes into spinning rather than translating. Total mass is irrelevant — it cancels in the formula."

- question: "Why does static friction do no work on an object rolling without slipping?"
  type: multiple-choice
  options:
    - "Static friction is too small to transfer significant energy in rolling motion"
    - "The contact point is instantaneously at rest, so the friction force acts through zero displacement and does zero work"
    - "Static friction acts perpendicular to the direction of motion, so its work component is zero by the dot product"
    - "Energy conservation only applies when there is no friction; static friction means energy is not conserved"
  answer: 1
  explanation: "Work is force times displacement in the direction of the force. The no-slip condition v_cm = Rω ensures the contact point has zero velocity — it is instantaneously stationary. Since the contact point undergoes zero displacement during an infinitesimal time interval, the static friction force does zero work regardless of its magnitude. This is why energy is fully conserved in rolling without slipping: no mechanical energy is converted to heat."

- question: "For an object rolling without slipping down an incline, the acceleration of the center of mass is independent of the object's total mass."
  type: true-false
  answer: true
  explanation: "The formula a_cm = g sin θ / (1 + I/mR²) looks like it depends on m, but for uniform objects, I is proportional to mR² — so I/mR² is a pure geometric factor depending only on mass distribution, not total mass. For a solid disk, I/mR² = 1/2 regardless of m; for a ring, I/mR² = 1 regardless of m. Total mass cancels, and acceleration depends only on mass distribution geometry and incline angle. This is analogous to how all objects fall at the same rate in free fall."

- question: "Static friction causes energy loss in rolling without slipping, similar to how kinetic friction converts mechanical energy to heat in sliding."
  type: true-false
  answer: false
  explanation: "Static friction does NO work in rolling without slipping because the contact point is instantaneously at rest — work = force × displacement, and displacement is zero. Therefore no mechanical energy is converted to heat, and total mechanical energy (translational + rotational KE + gravitational PE) is conserved. Kinetic friction in sliding does convert energy to heat because the contact point IS moving relative to the surface. The contrast between static and kinetic friction in this context is one of the key insights of rolling motion."

- question: "Explain why a hollow cylinder rolls more slowly down a ramp than a solid cylinder of the same mass and radius. Connect your answer to the rolling constraint and mass distribution."
  type: short-answer
  answer: "The rolling constraint v_cm = Rω links translational and rotational motion, so all gravitational PE released as the object descends must split between translational KE (½mv_cm²) and rotational KE (½Iω²). For the hollow cylinder (I = mR²), the total KE is ½mv_cm²(1 + 1) = mv_cm² — the energy is split evenly. For the solid cylinder (I = ½mR²), total KE is ½mv_cm²(3/2) — less goes to rotation. Since the same mgh is available, the hollow cylinder must allocate more energy to spinning, leaving less for translational acceleration. Mass concentrated at the rim (large I) is 'expensive' to spin under the constraint ω = v_cm/R, which is why it trades translational speed for rotational speed compared to the solid cylinder."
  explanation: "The key is understanding that the rolling constraint is a coupling — you cannot increase v_cm without proportionally increasing ω. The hollow cylinder's large moment of inertia makes spinning energetically expensive, which is why it must slow its translational acceleration to satisfy the constraint. Students who think heavier objects roll slower miss this: mass cancels in the formula, and only the geometry of mass distribution (I/mR²) matters."
```

## Explainer

Your prerequisite — rolling without slipping — established the constraint: when a round object rolls without slipping on a surface, the contact point has zero velocity, which forces v_cm = Rω. Taking the time derivative gives a_cm = Rα. These constraints link translation and rotation, reducing what looks like a two-degree-of-freedom problem to a one-degree-of-freedom problem: specify either the linear acceleration or the angular acceleration and the other is determined.

The power of these constraints becomes clear on an incline. A disk of mass m and radius R rolls down a ramp at angle θ. Two forces act: gravity (at the center of mass, pulling down the slope) and static friction (at the contact point, pointing up the slope). Newton's second law for translation gives mg sin θ − f = ma_cm. The rotational equation about the center of mass gives fR = Iα (only friction provides torque about the center — gravity acts through the center and has zero moment arm). Substituting α = a_cm/R from the rolling constraint: f = Ia_cm/R². Plugging back into the translational equation: mg sin θ = ma_cm + Ia_cm/R² = a_cm(m + I/R²). Solving: **a_cm = g sin θ / (1 + I/mR²)**. This single formula predicts everything. For a solid disk (I = ½mR²): a_cm = (2/3)g sin θ. For a solid sphere (I = ⅖mR²): a_cm = (5/7)g sin θ. For a thin ring (I = mR²): a_cm = (1/2)g sin θ. The pattern: more mass concentrated at the rim means more rotational inertia relative to mR², which means the rolling constraint requires more of the available gravitational force to go into spinning rather than accelerating the center, so the center accelerates more slowly. A ring beats a disk beats a sphere in a "slowness" race down a ramp — entirely because of geometry and mass distribution.

Energy methods complement the force approach and are often more direct for initial-to-final problems. The total kinetic energy of a rolling object is KE = ½mv_cm² + ½Iω². Substituting ω = v_cm/R: KE = ½mv_cm²(1 + I/mR²). An object rolling from rest down a height h satisfies mgh = ½mv_cm²(1 + I/mR²), immediately giving v_cm at the bottom without tracking forces or friction at all. This works because **static friction does no work**: the contact point is instantaneously at rest, so no displacement occurs there and the friction force acts through zero distance. Energy is conserved — none goes to heat — and the total mechanical energy simply redistributes between translational and rotational kinetic energy as the object descends.

The two methods — Newton's laws with the rolling constraint, and energy conservation — are complementary. Force methods give you accelerations and friction forces step by step through the motion, which matters when you need forces (to check whether static friction is sufficient, or to find normal forces in loops). Energy methods give you relationships between the initial and final states directly, which is far faster when you only care about speeds at specific points. Rolling motion is a clean test of both approaches, and mastering the constraint v_cm = Rω is the key that unlocks both.
