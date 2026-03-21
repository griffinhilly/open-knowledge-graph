---
id: potential-flow-theory
title: Potential Flow Theory
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-kinematics
  type: hard
- id: partial-derivatives
  type: hard
- id: gradient-vector
  type: soft
- id: bernoullis-equation
  type: soft
- id: navier-stokes-equations
  type: soft
builds-toward:
- drag-and-lift-aerodynamics
tags:
- potential flow
- irrotational
- stream function
- velocity potential
- superposition
stage: advanced
status: validated
---
# Potential Flow Theory

## Core Idea
For irrotational, incompressible flow (∇×V = 0 and ∇·V = 0), the velocity field can be derived from a scalar potential φ: V = ∇φ, where φ satisfies Laplace's equation ∇²φ = 0. A stream function ψ can also be defined such that V = ∇×(ψk̂). Because Laplace's equation is linear, elementary flows (uniform flow, source, sink, doublet, vortex) can be superposed to construct complex flows. Potential flow gives excellent pressure distributions away from walls but fails near boundaries where viscous effects matter.

## How It's Best Learned
Build complex flows by superposing elementary solutions: uniform flow + doublet = flow past a cylinder; add a vortex to get lift. Verify with the Bernoulli equation that the pressure distribution is correct. Note the symmetric pressure distribution for the cylinder case (d'Alembert's paradox: zero drag in potential flow) and discuss why real flows differ.

## Common Misconceptions
- Potential flow is not just 'inviscid flow' — it additionally requires irrotationality. Viscous wakes and boundary layers can produce rotational regions even in high-Re flows.
- d'Alembert's paradox (zero drag in potential flow) seems to contradict reality; real drag comes from viscous effects and the separated wake not captured by potential flow.
- Streamlines and equipotential lines are always orthogonal in 2D potential flow, which helps visualize the flow but can be mistaken for a general truth.

## Questions

```yaml
- question: "Potential flow predicts zero drag on a circular cylinder (d'Alembert's paradox). This result fails for real fluids because:"
  type: multiple-choice
  options:
    - "Potential flow incorrectly predicts the velocity magnitude at the cylinder surface"
    - "Laplace's equation cannot be solved accurately for curved geometries like cylinders"
    - "The irrotational assumption breaks down in the viscous boundary layer and separated wake, where vorticity is generated"
    - "The pressure distribution predicted by potential flow is incorrect everywhere around the cylinder, including far from the surface"
  answer: 2
  explanation: "D'Alembert's paradox arises because potential flow is fore-aft symmetric — the pressure distribution on the front half exactly mirrors the back half, producing no net pressure force. In reality, viscosity creates a boundary layer on the cylinder surface and a separated wake behind it; both regions contain strong vorticity. The real pressure distribution on the rear of the cylinder is much lower than potential flow predicts (because the separated wake maintains a low-pressure region), producing the net pressure drag that potential flow entirely misses."

- question: "Why can complex flow patterns be constructed by adding together elementary solutions (uniform flow, source, doublet, vortex) in potential flow theory?"
  type: multiple-choice
  options:
    - "Because the Navier-Stokes equations are linear at high Reynolds number"
    - "Because irrotational flows share identical boundary conditions that allow solutions to combine"
    - "Because Laplace's equation is linear, so any linear combination of solutions is also a solution"
    - "Because all real flows can be decomposed into a finite number of elementary vortex structures"
  answer: 2
  explanation: "The superposition principle applies directly because Laplace's equation ∇²φ = 0 is linear. If φ₁ and φ₂ both satisfy ∇²φ = 0, then c₁φ₁ + c₂φ₂ does too. This is not true of the Navier-Stokes equations, which contain nonlinear inertial terms — option A is incorrect. The linearity of Laplace's equation is precisely why potential flow has a vast catalog of analytical solutions: once you know a library of elementary solutions, you can construct complex flows by superposition."

- question: "Potential flow applies to all inviscid flows — any flow with high enough Reynolds number qualifies as potential flow, since viscosity becomes negligible."
  type: true-false
  answer: false
  explanation: "False. Potential flow additionally requires irrotationality (∇×V = 0), which is a separate and stronger condition than inviscid flow. In many high-Reynolds-number flows, viscosity is indeed negligible in the bulk — but near solid surfaces, viscosity generates vorticity in the boundary layer, and wakes downstream contain strong vortical structures. These rotational regions violate the irrotational assumption even where viscosity is small. Potential flow applies only to the outer, irrotational region of a high-Re flow, not to boundary layers, wakes, or separated flow regions."

- question: "In 2D potential flow, streamlines (lines of constant stream function ψ) and equipotential lines (lines of constant velocity potential φ) are always perpendicular to each other."
  type: true-false
  answer: true
  explanation: "True. The stream function ψ and velocity potential φ satisfy the Cauchy-Riemann equations: ∂φ/∂x = ∂ψ/∂y and ∂φ/∂y = −∂ψ/∂x. This makes φ and ψ conjugate harmonic functions, and a theorem from complex analysis states that the level curves of two conjugate harmonic functions are everywhere orthogonal. Together, lines of constant φ and ψ form a flow net — an orthogonal grid that provides a powerful visual tool for analyzing 2D potential flows."

- question: "Explain why irrotationality is both the source of potential flow theory's power and the reason for its practical limitations."
  type: short-answer
  answer: "Irrotationality allows the velocity field to be derived from a scalar potential φ satisfying Laplace's equation, which is linear. Linearity enables superposition of elementary solutions, analytical tractability, and the full machinery of complex analysis — enormous computational power. But viscosity generates vorticity wherever fluid contacts a solid surface, violating the irrotational assumption in boundary layers and wakes. Potential flow therefore correctly describes the outer flow and gives accurate pressure predictions for lift, but completely fails to predict drag, which depends on the viscous wake it ignores."
  explanation: "This tradeoff is the conceptual foundation of boundary layer theory: match an outer potential-flow solution (irrotational, analytically tractable) to an inner viscous boundary-layer solution (rotational, thin). The two regions capture different physics. The outer flow determines the pressure distribution that drives lift; the inner boundary layer determines skin friction and separation that drives drag. Understanding where potential flow is valid — and where it breaks down — is as important as knowing how to compute it."
```

## Explainer

From fluid kinematics you know that the **vorticity** of a flow, ∇×V, describes the local rotation of fluid elements. Setting vorticity to zero — **irrotational flow** — is a strong constraint, but it purchases an enormous simplification: the velocity field can be written as the gradient of a scalar function, V = ∇φ. This **velocity potential** φ plays the same role that gravitational potential plays in mechanics: just as gravitational force is minus the gradient of potential energy, fluid velocity is the gradient of φ. Combining irrotationality with incompressibility (∇·V = 0) yields Laplace's equation ∇²φ = 0 — one of the most studied equations in mathematics, with a vast catalog of known solutions.

The second key function is the **stream function** ψ, defined so that streamlines (paths of constant ψ) coincide with the actual flow paths. In 2D, ψ and φ are related as **conjugate harmonic functions**: ∂φ/∂x = ∂ψ/∂y and ∂φ/∂y = −∂ψ/∂x. This means that lines of constant φ (equipotential lines) are always perpendicular to lines of constant ψ (streamlines), forming an orthogonal grid that is extremely useful for visualizing flow patterns. Together, φ and ψ can be combined into a single **complex potential** w = φ + iψ, which is an analytic function of the complex variable z = x + iy — opening the full power of complex analysis to fluid flow problems.

The reason potential flow is so useful is that **Laplace's equation is linear**: any linear combination of solutions is also a solution. This means you can build complex flows by adding together simple **elementary flows**. The catalog includes uniform flow (φ = Ux), a point source (φ = m ln r / 2π), a doublet (two opposite sources merged in the limit), and a point vortex (φ = Γθ / 2π). Superposing uniform flow and a doublet gives exactly the velocity field for flow past a circular cylinder. Add a vortex of circulation Γ to the cylinder, and the flow develops an asymmetry — the pressure on top and bottom differs, producing a net **lift force** proportional to Γ. This is the Kutta-Joukowski theorem, and it is the foundation of classical airfoil theory.

Once you have the velocity field from φ, you recover pressure using the Bernoulli equation from your prerequisites: p + ½ρV² = constant along any streamline (and throughout the entire potential flow field, since the flow is irrotational). The pressure distribution around the cylinder with no vortex is symmetric fore-and-aft, leading to the famous **d'Alembert's paradox**: potential flow predicts zero drag on any body, which is obviously wrong for real fluids. The paradox is resolved by recognizing what potential flow omits — viscosity, boundary layers, and the separated wake that forms behind bluff bodies. In those regions, vorticity is generated and the irrotational assumption breaks down entirely.

The practical scope of potential flow is thus limited to the region **away from solid boundaries** in high-Reynolds-number flows: in the outer flow far from walls, irrotationality is a good approximation, and potential flow correctly predicts the pressure distribution that drives lift. Near the surface, the viscous boundary layer must be treated separately. This matching of an outer potential solution to an inner viscous solution is the conceptual foundation of boundary layer theory, and understanding where potential flow succeeds and fails is as important as knowing how to compute it.
