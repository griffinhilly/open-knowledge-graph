---
id: darcy-weisbach-equation-application
title: 'Darcy-Weisbach Equation: Major Head Loss Calculation'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: laminar-pipe-flow
  type: hard
- id: turbulent-pipe-flow
  type: hard
- id: mechanical-energy-balance-pump-turbine
  type: hard
builds-toward:
- friction-factor-determination-methods
- pipe-network-solutions-hardy-cross
tags:
- head-loss
- friction
- pipe-flow
- energy
stage: expert
status: validated
---

# Darcy-Weisbach Equation: Major Head Loss Calculation

## Core Idea
The Darcy-Weisbach equation, H_loss = f(L/D)(V²/2g), quantifies major (friction) head loss in pipes. The friction factor f depends on Reynolds number and relative roughness. This equation is universal for all pipe diameters, lengths, and flow velocities, making it the standard tool for piping system calculations in industry and engineering practice.

## Questions

```yaml
- question: "Water flows through a commercial steel pipe at Re = 100,000 (turbulent). An engineer doubles the pipe's wall roughness ε by switching to a rougher material while keeping the same pipe diameter, length, and flow velocity. What happens to the friction factor f and the head loss?"
  type: multiple-choice
  options:
    - "f is unchanged because Reynolds number is unchanged, and head loss stays the same"
    - "f increases because higher relative roughness ε/D raises f in turbulent flow on the Moody diagram, so head loss also increases"
    - "f decreases because a rougher surface disrupts the turbulent boundary layer and actually reduces skin friction"
    - "f is not defined for rough commercial pipes; Darcy-Weisbach only applies to hydraulically smooth surfaces"
  answer: 1
  explanation: "In turbulent flow, the friction factor depends on both Reynolds number AND relative roughness ε/D. On the Moody diagram, for a given Re, moving to a higher ε/D curve gives a higher f. Since head loss H = f(L/D)(V²/2g) and f increases, head loss increases proportionally. This contrasts with laminar flow, where f = 64/Re depends only on Re and roughness is irrelevant — the viscous sublayer completely covers the roughness peaks in laminar flow, so they produce no additional resistance."

- question: "Two geometrically identical pipes carry fluid in laminar flow at the same Reynolds number. One pipe has smooth walls; the other has significant wall roughness ε/D = 0.05. Which has the higher Darcy friction factor?"
  type: multiple-choice
  options:
    - "The rough pipe, because roughness always increases friction regardless of flow regime"
    - "Both have identical friction factors — in laminar flow, f = 64/Re regardless of wall roughness"
    - "The smooth pipe, because turbulent eddies cannot form on smooth walls, reducing overall flow resistance"
    - "The rough pipe at low Re, but both are identical only at very high laminar Reynolds numbers"
  answer: 1
  explanation: "This is a counterintuitive result that students who apply turbulent reasoning to laminar flow consistently get wrong. In laminar flow (Re < 2300), the velocity profile is dominated by viscosity; the fluid moves in orderly layers, and the viscous sublayer completely submerges any roughness features. The theoretical result f = 64/Re is exact for laminar pipe flow and has no roughness term. Roughness only matters when the flow is turbulent and roughness elements protrude through the viscous sublayer to disturb the turbulent eddies."

- question: "At very high Reynolds numbers in rough pipes (the 'fully rough' turbulent regime), the Darcy friction factor f becomes independent of Reynolds number and is determined solely by the relative roughness ε/D."
  type: true-false
  answer: true
  explanation: "This is visible on the Moody diagram as the horizontal 'plateaus' at high Re for each roughness curve. The physical reason: at very high Re, the viscous sublayer becomes thinner than the roughness height ε. The roughness peaks protrude fully into the turbulent flow field and dominate friction, while viscous effects become negligible. In this regime, each constant-roughness curve on the Moody diagram flattens to a constant f value given by the fully rough formula (1/√f = −2 log(ε/3.7D) from the Colebrook equation at Re → ∞)."

- question: "Doubling the length of a pipe in a Darcy-Weisbach calculation doubles the friction factor f."
  type: true-false
  answer: false
  explanation: "This confuses two different quantities. The friction factor f is a dimensionless property of the flow regime and pipe roughness — it depends on Re and ε/D, not on pipe length. What doubles when you double pipe length is the head loss H_loss = f(L/D)(V²/2g). The factor (L/D) doubles, so H_loss doubles, but f itself is unchanged. f is an intensive property of the flow; H_loss is the extensive result of applying f over a given pipe geometry."

- question: "Why does expressing head loss in meters of fluid column — rather than in pascals — make the Darcy-Weisbach equation useful across different fluids without modification?"
  type: short-answer
  answer: "Head loss in meters of fluid (H_loss = f(L/D)(V²/2g)) is a measure of energy per unit weight of fluid, and it is independent of fluid density. To convert to pressure drop, you multiply by ρg: ΔP = ρg·H_loss. Since different fluids have different densities, expressing the result in meters keeps the equation form identical regardless of fluid — you simply multiply by the appropriate ρg at the end. This means the same friction factor and the same equation apply whether you are pumping water, crude oil, or air through a pipe."
  explanation: "This is the practical engineering power of the Darcy-Weisbach formulation over the Fanning friction factor or direct pressure-drop equations. In Bernoulli-form energy equations, all terms (velocity head V²/2g, elevation head z, pressure head P/ρg) share the same units of meters. Head loss drops in directly without needing to know the fluid density. The Moody diagram gives f as a function of Re and ε/D for any fluid; the density enters only when converting back to pressure for pump sizing."
```

## Explainer

When real fluid flows through a pipe, some of the mechanical energy is permanently lost to viscous friction and turbulent dissipation — this is **major head loss**, or friction head loss. Your prerequisite on the mechanical energy balance extended the Bernoulli equation for real fluids by adding a head loss term H_loss on the right side: energy added by pumps minus energy extracted by turbines minus friction losses equals the net change in fluid mechanical energy. The Darcy-Weisbach equation gives you the precise value to substitute for H_loss.

The equation H_loss = f(L/D)(V²/2g) has a clear physical structure. The term V²/2g is the **velocity head** — the kinetic energy per unit weight of fluid, measured in meters of fluid column. The ratio L/D counts how many pipe diameters the fluid has traveled; a 5 m pipe with a 25 mm diameter has L/D = 200, meaning the fluid has traversed 200 pipe diameters of frictional surface. The **Darcy friction factor** f scales these together and encapsulates the effect of flow regime and pipe roughness. Head loss grows linearly with pipe length and inversely with diameter — a pipe twice as long loses twice the head, and a pipe twice as wide at the same velocity loses half the head.

The friction factor f is where your prerequisites on laminar and turbulent pipe flow become essential. For laminar flow (Re < 2300), theory yields f = 64/Re exactly — the smoother the laminar layers, the less friction, regardless of pipe wall roughness. For turbulent flow (Re > 4000), you must use the **Moody diagram** (or the Colebrook equation it represents), which shows f as a function of both Reynolds number and **relative roughness** ε/D, where ε is the average wall roughness height. At moderate Reynolds numbers, viscous effects damp out roughness contributions; at very high Reynolds numbers, f flattens to a constant set by ε/D alone — the "fully rough" regime where the roughness peaks protrude through the viscous sublayer and dominate friction.

The universality of Darcy-Weisbach is what makes it the engineering standard. Whether the fluid is water or crude oil, the pipe is 12 mm or 1.2 m in diameter, flow is laminar or fully turbulent — the same equation applies. You simply look up or calculate the appropriate f. Because head loss is expressed in meters of fluid rather than pascals, it is independent of fluid density and adds directly to the Bernoulli terms. A piping network calculation — sizing pumps, checking if flow rates are achievable, comparing parallel and series pipe branches — reduces to writing energy equations between nodes with Darcy-Weisbach supplying each pipe's friction term.
