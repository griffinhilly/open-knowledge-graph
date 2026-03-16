---
id: total-mechanical-energy-conservation
title: Total Mechanical Energy and Energy Conservation
domain: physics
course: classical-mechanics
prerequisites:
- id: conservation-of-energy
  type: hard
- id: conservative-vector-fields-mechanics
  type: hard
builds-toward:
- energy-conservation-applications
- effective-potential-central-forces
tags:
- energy
- conservation
- mechanics
stage: formal-systems
status: draft
---

# Total Mechanical Energy and Energy Conservation

## Core Idea
The total mechanical energy E = K + U is conserved when only conservative forces act. This powerful principle reduces dynamics to finding turning points and velocities without integrating the equations of motion.

## Explainer

Your prerequisites give you the two building blocks: conservation of energy as a general principle, and the result from conservative vector fields that **F** = −∇U means all work done by such forces is stored in potential energy. This topic is where those ideas combine into a practical problem-solving tool. The statement E = K + U = constant is simple, but its implications are far-reaching — it lets you answer questions about particle motion without ever solving a differential equation.

**Kinetic energy** K = ½mv² is always non-negative (it is zero when the particle is at rest, never below zero). This single fact is extraordinarily useful. Since E = K + U and K ≥ 0, we have U ≤ E always. Wherever the potential energy U(x) exceeds the total energy E, the particle *cannot be* — it has no kinetic energy to spare, and being there would require negative K. Points where U(x) = E are **turning points**: the particle arrives with K = 0, momentarily stops, and reverses direction. The particle is confined to regions where U(x) ≤ E, and you can read these regions directly off a graph of U(x) without solving any equations.

Consider a particle in a potential well shaped like a valley: U rises on both sides of a minimum. If E is just above the minimum, the particle bounces back and forth between two turning points, never escaping. If E is raised high enough to exceed the height of a potential barrier, the particle can pass over. This gives you oscillation, confinement, tunneling-analog problems — all from a picture. For a specific example: a pendulum at angle θ has U = mgL(1 − cos θ). Given initial conditions (and thus E), you immediately know the maximum angle (where K = 0) without solving the nonlinear pendulum equation.

The method extends to multi-dimensional problems via **effective potential** — a technique you will encounter next, where angular momentum contributes an additional term to the potential, and radial motion in central-force problems reduces to a one-dimensional energy problem. The key conceptual point is that conservation of energy transforms dynamics (about motion in time) into statics (about regions in space). Instead of asking "what force acts here and how does the particle accelerate?", you ask "what is E, where is U(x) ≤ E, and where is the minimum of U?" — and the answers give you qualitative and quantitative information about the trajectory with minimal calculation. This is why energy methods dominate advanced mechanics: they exploit symmetry (the time-translation symmetry that implies energy conservation) to bypass the heavy machinery of integrating equations of motion.
