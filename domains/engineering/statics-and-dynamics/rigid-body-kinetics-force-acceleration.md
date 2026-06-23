---
id: rigid-body-kinetics-force-acceleration
title: Rigid Body Kinetics — Force and Acceleration
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: dynamics-newtons-second-law
  type: hard
- id: mass-moment-of-inertia
  type: hard
- id: rigid-body-kinematics-general-motion
  type: soft
- id: rigid-body-kinematics-rotation
  type: soft
- id: systems-of-particles-mechanics
  type: soft
builds-toward:
- rigid-body-work-energy
- angular-impulse-momentum
tags:
- dynamics
- kinetics
- rigid bodies
- Newton's second law
- rotation
- translation
stage: formal-systems
status: validated
---

# Rigid Body Kinetics — Force and Acceleration

## Core Idea
Newton's second law for a rigid body in planar motion consists of three coupled equations: ΣF_x = m*(a_G)_x, ΣF_y = m*(a_G)_y, and ΣM_G = I_G*alpha, where G is the mass center, a_G is the acceleration of the mass center, I_G is the mass moment of inertia about G, and alpha is the angular acceleration. Alternatively, moments can be summed about any point P using ΣM_P = I_G*alpha + (moment of m*a_G about P). For pure translation, alpha = 0 and the moment equation constrains force locations. For fixed-axis rotation, the mass center itself accelerates (normal and tangential components), coupling the force and moment equations. For general planar motion, all three equations are fully coupled and must be solved simultaneously with kinematic constraints.

## How It's Best Learned
Draw a free-body diagram showing all external forces and a kinetic diagram showing m*a_G at the mass center and I_G*alpha as a couple. Match the two diagrams term by term when writing the three equations of motion. For rolling problems, identify whether the wheel rolls without slip (kinematic constraint: a_G = alpha*r) or with slip (friction = mu_k * N). Always check that the number of equations matches the number of unknowns.

## Common Misconceptions
- Summing moments about the mass center and forgetting to use I_G (not I about the contact point or support, unless applying the alternative moment equation with the m*a_G transport term).
- Assuming friction at a rolling contact equals mu*N — for rolling without slip, friction is an unknown that must be solved for, and it is often less than mu_s*N.
- Neglecting the normal component of mass-center acceleration (omega^2*r toward the pivot) for fixed-axis rotation problems, which affects the pin reaction forces.

## Questions

```yaml
- question: "A uniform disk rolls without slipping down an inclined plane. A student writes the friction force as f = µ_k × N in the equations of motion. What error has the student made?"
  type: multiple-choice
  options:
    - "The student should use µ_s instead of µ_k, since the disk is not slipping"
    - "Friction at a no-slip rolling contact is an unknown to be solved from the equations of motion, not a known force equal to µN"
    - "The normal force N must be resolved differently on an inclined surface before multiplying by µ"
    - "Static friction is zero when a disk rolls without slipping, so the term should be omitted entirely"
  answer: 1
  explanation: "For rolling without slip, friction is a static friction force — it takes whatever value is required to enforce the kinematic constraint (zero slip at the contact point). This value is not µ_s×N or µ_k×N; those are the *limits* of static and kinetic friction, respectively. The actual friction force is an unknown that emerges from solving the three equations of motion simultaneously with the rolling constraint a_G = α·r. After solving, you check whether the required friction is less than µ_s×N to verify the no-slip assumption is valid. Assuming f = µN at the outset is incorrect and gives the wrong answer."

- question: "A uniform rod is pinned at one end (fixed axis rotation) and swings from rest. As it swings, it has angular velocity ω and angular acceleration α. A student accounts for the tangential acceleration of the mass center (r·α) when writing force equations, but gets incorrect pin reactions. What term was likely forgotten?"
  type: multiple-choice
  options:
    - "The weight of the rod, which acts at the mass center and must appear in the free-body diagram"
    - "The normal (centripetal) acceleration of the mass center (ω²·r directed toward the pin), which contributes to pin reaction forces"
    - "The moment of inertia, which should be computed about the pin rather than the mass center"
    - "The applied moment equation, which must always be written before the force equations for rotating bodies"
  answer: 1
  explanation: "For fixed-axis rotation, the mass center moves in a circle. It therefore has two acceleration components: tangential (r·α, perpendicular to the radius) from angular acceleration, and normal (ω²·r, directed toward the pin) from the existing angular velocity. The normal component is often forgotten because it is zero at the instant of release from rest (ω = 0), but it grows as the rod gains angular velocity. Neglecting ω²·r means the pin reactions are calculated incorrectly at any point after motion begins."

- question: "When taking moments about the mass center G of a rigid body in planar motion, the rotational equation of motion is ΣM_G = I_G·α, with no additional correction terms needed."
  type: true-false
  answer: true
  explanation: "Summing moments about the mass center G is the 'clean' choice for the rotational equation because it eliminates the transport term. When you sum moments about any other point P, you must include the moment of the m·a_G vector about P as an additional term: ΣM_P = I_G·α + (r_{G/P} × m·a_G). This transport term is zero when P = G (the moment arm is zero). Many errors in rigid body kinetics come from summing moments about a convenient point like the contact patch and forgetting to add this term."

- question: "For a rigid body in pure translation (α = 0), the net moment about the mass center is expected to be zero, which means no individual forces can create moments about G."
  type: true-false
  answer: false
  explanation: "Pure translation means α = 0, so the moment equation gives ΣM_G = I_G·(0) = 0 — the net moment about G is zero. But individual forces can still create nonzero moments that happen to cancel. For example, in a block sliding on a surface, gravity acts downward at G, the normal force acts upward at the contact surface below G, and friction acts horizontally at the contact. Each creates a moment about G, but they sum to zero for pure translation. The moment equation in this case constrains where the resultant force must act, not that no forces have moment arms."

- question: "When analyzing a rigid body rolling without slip, why must friction be treated as an unknown to solve for rather than set equal to µN? Walk through the correct procedure."
  type: short-answer
  answer: "Friction at a no-slip rolling contact is static friction, which adjusts to whatever value is needed to prevent slipping — it can be anywhere from zero to µ_s×N. Its actual value depends on the applied forces, the geometry, and the inertia of the body. The correct procedure: (1) Write the three equations of motion (ΣF_x = m·a_G, ΣF_y = m·a_G, ΣM_G = I_G·α) with friction f as an unknown. (2) Apply the rolling constraint: a_G = α·r, giving a fourth equation. (3) Solve the system for all unknowns including f. (4) Check: if |f| ≤ µ_s×N, rolling without slip is valid. If |f| > µ_s×N, the body actually slips — restart with f = µ_k×N as a known and the rolling constraint removed."
  explanation: "The procedure reveals why the no-slip check comes at the end: you need to know what friction the no-slip condition demands before you can check whether it is physically achievable. Assuming f = µN at the start is incorrect because it imposes a specific friction value that may or may not match what the rolling constraint requires."
```

## Explainer

For a single particle, Newton's second law is F = ma — one vector equation relating the net force to the product of mass and acceleration. A rigid body is more complex: it has both a translational state (where its mass center is going) and a rotational state (how fast it's spinning). From your prerequisite on mass moment of inertia, you know that I_G quantifies a body's resistance to angular acceleration, just as mass quantifies resistance to translational acceleration. Rigid body kinetics couples these two behaviors through three equations of motion.

The translational equations are simply Newton's second law applied to the mass center: ΣF_x = m(a_G)_x and ΣF_y = m(a_G)_y. All external forces, regardless of where they are applied on the body, contribute to accelerating the mass center. The rotational equation ΣM_G = I_G·α is the angular counterpart: net moment about the mass center equals the mass moment of inertia times angular acceleration. This equation accounts for the *torque* effect of forces — the same force applied at different distances from G produces different angular accelerations. Together, these three equations govern all planar rigid body motion.

The coupling between translation and rotation depends on the type of motion. For **pure translation** (no rotation), α = 0, and the moment equation constrains the location of the resultant force. For **fixed-axis rotation** (a door on a hinge, a wheel on a fixed axle), the mass center moves in a circle around the fixed point, so it has both tangential acceleration (r·α, from angular acceleration) and normal acceleration (ω²·r, from existing angular velocity) — this normal component is frequently overlooked. For **general planar motion** (a wheel rolling across the floor, a connecting rod in an engine), both translational and rotational accelerations are nonzero and fully coupled, requiring all three equations plus a kinematic constraint like a_G = α·r.

The diagram method is the clearest way to organize these equations. Draw a free-body diagram showing all external forces (weights, applied loads, normal forces, friction). Draw a separate kinetic diagram showing the inertia terms: a vector m·**a_G** at the mass center and a couple I_G·α representing the rotational inertia. Then match the free-body diagram to the kinetic diagram equation by equation. This visual accounting prevents the most common errors — especially when taking moments about a point other than G, where you must include the moment of the m·**a_G** vector about that point as a transport term.

Rolling contact deserves special attention. When a body rolls without slipping, the contact point has zero velocity, giving the kinematic constraint a_G = α·r. But friction at the contact is *not* µN — it is whatever value is needed to enforce the rolling constraint, which you solve for from the equations of motion. Only after solving do you check whether the required friction is less than µ_s·N; if not, the body slips instead of rolling, and you must redo the problem with kinetic friction µ_k·N as a known force and the no-slip kinematic constraint removed.
