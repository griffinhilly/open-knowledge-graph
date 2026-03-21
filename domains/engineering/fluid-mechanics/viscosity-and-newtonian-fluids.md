---
id: viscosity-and-newtonian-fluids
title: Viscosity and Newtonian Fluid Behavior
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-properties-and-continuum
  type: hard
builds-toward:
- navier-stokes-equations
- reynolds-number
- laminar-pipe-flow
tags:
- viscosity
- shear stress
- Newtonian fluid
- non-Newtonian
- no-slip condition
stage: advanced
status: validated
---

# Viscosity and Newtonian Fluid Behavior

## Core Idea
A Newtonian fluid obeys Newton's law of viscosity: shear stress τ = μ(du/dy), where μ is the dynamic viscosity and du/dy is the velocity gradient (shear rate). The no-slip condition requires that fluid in contact with a solid boundary moves at the boundary's velocity. Non-Newtonian fluids (shear-thinning, shear-thickening, Bingham plastics) have viscosity that depends on shear rate, making them fundamentally different from Newtonian ones like water and air.

## How It's Best Learned
Derive Couette flow (flow between parallel plates with one moving) from Newton's viscosity law to see how a linear velocity profile emerges. Compare viscosities of different fluids in tables and connect units (Pa·s = kg/(m·s)) to physical meaning.

## Common Misconceptions
- Viscosity is a resistance to flow due to internal friction, not a measure of 'thickness' per se; some thick gels are non-Newtonian.
- The no-slip condition is an empirical observation that holds for most engineering flows but breaks down at very low pressures (slip flow regime).
- Kinematic viscosity ν = μ/ρ is not the same as dynamic viscosity μ; both matter in different contexts.

## Questions

```yaml
- question: "Ketchup flows very slowly when you gently tilt the bottle, but pours freely after you shake it vigorously. What type of fluid behavior does this describe, and what does it imply about ketchup's viscosity?"
  type: multiple-choice
  options:
    - "Newtonian behavior — viscosity is constant, and shaking simply adds kinetic energy to help it flow"
    - "Shear-thickening — the shear stress from shaking increases viscosity, making ketchup easier to pour"
    - "Shear-thinning — viscosity decreases with increasing shear rate, so vigorous shaking reduces resistance to flow"
    - "Bingham plastic behavior — shaking overcomes the yield stress, after which ketchup flows as a Newtonian fluid"
  answer: 2
  explanation: "Ketchup is a shear-thinning (pseudoplastic) non-Newtonian fluid: its viscosity decreases as shear rate increases. This means gentle tilting (low shear) produces high viscosity and little flow, while vigorous shaking (high shear) dramatically reduces viscosity and allows pouring. This directly violates Newton's law of viscosity, which predicts constant viscosity (linear τ–shear rate relationship) regardless of shear rate. Option D is a common near-miss — ketchup does have a slight yield stress, but the primary behavior is shear-thinning, not Bingham plastic."

- question: "In a Newtonian fluid flow between two parallel plates (Couette flow), if you double the velocity of the moving plate while keeping all else constant, what happens to the shear stress on the plates?"
  type: multiple-choice
  options:
    - "It remains the same — shear stress depends only on viscosity, not plate speed"
    - "It doubles — because shear stress equals μ times the velocity gradient, which doubles"
    - "It quadruples — because the kinetic energy of the flow increases with the square of velocity"
    - "It halves — because the fluid becomes thinner as it flows faster between the plates"
  answer: 1
  explanation: "For a Newtonian fluid, τ = μ(du/dy). Doubling the plate velocity doubles the velocity gradient du/dy (the velocity profile remains linear in Couette flow), which doubles the shear stress τ. This linear proportionality is precisely what defines a Newtonian fluid — constant μ means shear stress and shear rate are directly proportional. Non-Newtonian fluids break this proportionality; for them, doubling the shear rate would produce something other than a doubling of shear stress."

- question: "The no-slip condition means that fluid velocity at a solid boundary is zero in all engineering flows, which is why shear stress is maximized at walls rather than at the center of a flow."
  type: true-false
  answer: true
  explanation: "The no-slip condition states that fluid at a solid boundary moves at exactly the boundary's velocity — zero for a stationary wall. This creates the steepest velocity gradient (du/dy) right at the wall, which by Newton's law means maximum shear stress there. In pipe flow, for example, velocity is zero at the wall and maximum at the centerline, making wall shear stress responsible for all pipe friction. Without the no-slip condition, there would be no velocity gradient at the wall, no wall shear stress, and the entire analysis of pipe friction, drag, and boundary layers would be impossible."

- question: "Dynamic viscosity μ and kinematic viscosity ν = μ/ρ measure the same fluid property and can be used interchangeably in any calculation."
  type: true-false
  answer: false
  explanation: "Dynamic viscosity μ (units: Pa·s) measures a fluid's intrinsic resistance to shear — it appears directly in Newton's law of viscosity τ = μ(du/dy). Kinematic viscosity ν = μ/ρ (units: m²/s) combines this with density and appears naturally when inertial forces matter, such as in the Reynolds number Re = VL/ν. They are not interchangeable: comparing μ values across fluids tells you about their shearing resistance; comparing ν values tells you about momentum diffusion relative to inertia. Two fluids with equal μ can have very different ν if their densities differ, leading to completely different flow behaviors."

- question: "Why does water's dynamic viscosity decrease with increasing temperature, while most liquids behave similarly? What is the physical mechanism?"
  type: short-answer
  answer: "In liquids, viscosity arises from intermolecular attractive forces that resist layer-by-layer sliding. As temperature rises, molecules gain kinetic energy, more readily overcoming these cohesive bonds, allowing layers to slide past each other more easily — reducing viscosity. For water specifically, hydrogen bonding is the dominant cohesive mechanism, and elevated temperature weakens hydrogen bond networks, dramatically reducing viscosity (a roughly threefold drop from 20°C to 70°C). This contrasts with gases, where viscosity arises from momentum exchange between molecules colliding across adjacent layers — more thermal energy means more collisions and higher momentum transfer, so gas viscosity increases with temperature."
  explanation: "The physical mechanism differs fundamentally between liquids (intermolecular cohesion) and gases (molecular collision frequency). This is why the temperature dependence of viscosity runs in opposite directions for the two phases — a fact that surprises students who assume 'hotter = less viscous' universally. The liquid mechanism (cohesion weakening) is correct for water and most engineering liquids; the gas mechanism (collision frequency increasing) governs air, steam, and other gases at engineering conditions."
```

## Explainer

You already know from fluid properties and continuum mechanics that a fluid deforms continuously under shear stress — unlike a solid, which deforms to a fixed amount and stops. But what determines the rate of deformation? Viscosity is the answer: it quantifies how much resistance a fluid offers to being sheared. The physical picture is one of fluid **layers** sliding past one another. Faster layers drag slower layers forward through molecular momentum exchange; slower layers drag faster layers backward. This internal friction, averaged over enormous numbers of molecular collisions, is what Newton's law of viscosity captures in a single equation.

**Newton's law of viscosity** states τ = μ(du/dy): the shear stress τ (force per unit area) between adjacent fluid layers equals the **dynamic viscosity** μ times the **velocity gradient** du/dy. A **Newtonian fluid** is defined precisely by this linear relationship — doubling the shear rate du/dy doubles the shear stress τ. Water and air are Newtonian across virtually all engineering conditions. The viscosity μ has units of Pa·s and depends strongly on temperature: water's viscosity drops by a factor of three between 20°C and 70°C (molecular mobility increases with thermal energy), while air's viscosity increases modestly with temperature (more frequent molecular collisions transfer more momentum). **Kinematic viscosity** ν = μ/ρ combines viscosity and density into a single parameter that governs how momentum diffuses through a fluid; it appears naturally in the Reynolds number Re = VL/ν.

The **no-slip condition** — that fluid immediately at a solid boundary moves at exactly the boundary's velocity — follows from molecular physics: fluid molecules collide with the wall, exchange momentum, and match its velocity. This is not an assumption imposed for convenience; it is an empirical observation holding for virtually all engineering flows. Its consequence is immediately practical: even a flow with high free-stream velocity has zero velocity at every solid wall, creating a velocity gradient du/dy and therefore a shear stress τ at every surface. Without the no-slip condition, viscosity would be irrelevant at walls — the entire study of boundary layers, pipe friction, and drag depends on it.

**Non-Newtonian fluids** break the linear τ–(du/dy) relationship in characteristic ways. **Shear-thinning** fluids (blood, ketchup, many polymer solutions) have viscosity that decreases with shear rate — they flow more easily when stirred faster, which is why ketchup suddenly pours after vigorous shaking. **Shear-thickening** fluids (dense cornstarch suspensions) stiffen under rapid deformation — the basis of "oobleck" that behaves as a solid under impact. **Bingham plastics** (toothpaste, mayonnaise) act as solids below a yield stress and flow only above it. Recognizing whether a fluid is Newtonian or not matters enormously in design: pipe and pump sizing formulas derived from Newton's viscosity law will give wrong answers for non-Newtonian fluids, sometimes catastrophically so in polymer processing, food engineering, and biological flow applications.
