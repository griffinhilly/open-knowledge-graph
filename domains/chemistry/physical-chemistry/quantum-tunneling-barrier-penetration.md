---
id: quantum-tunneling-barrier-penetration
title: Quantum Tunneling and Barrier Penetration
domain: chemistry
course: physical-chemistry
prerequisites:
- id: potential-energy-surfaces
  type: hard
- id: quantum-chemistry-foundations
  type: hard
builds-toward:
- transition-state-geometry-activated-complex
tags:
- tunneling
- quantum-mechanics
- barrier-penetration
stage: advanced
status: draft
---

# Quantum Tunneling and Barrier Penetration

## Core Idea
The wave function has non-zero amplitude in classically forbidden regions where E < V; particles can tunnel through energy barriers with probability determined by barrier width and height. Tunneling enables processes like alpha decay, enzymatic hydrogen transfer, and low-temperature reaction rates. The tunneling probability decays exponentially with barrier width, making it very sensitive to molecular size.

## How It's Best Learned
Solve the Schrödinger equation for a rectangular barrier and calculate transmission coefficient. Examine how transmission varies with energy, barrier height, and width to understand chemical tunneling.

## Explainer

In classical mechanics, a ball rolling toward a hill will either have enough energy to go over the top or it will roll back — there is no third option. But from your study of quantum chemistry foundations, you know that particles are described by wave functions, and wave functions do not abruptly stop at boundaries. When a quantum particle encounters an energy barrier where its total energy E is less than the potential energy V, the wave function does not vanish — it **decays exponentially** inside the barrier. If the barrier is thin enough, the wave function emerges on the other side with diminished but non-zero amplitude. This is **quantum tunneling**: a particle passing through a barrier it classically could never surmount.

The mathematics follows directly from solving the Schrödinger equation in three regions: before the barrier, inside it, and after it. Inside the barrier, the solutions are real exponentials (decaying and growing) rather than oscillating waves. By matching boundary conditions — requiring the wave function and its derivative to be continuous at each interface — you derive the **transmission coefficient** T, which gives the probability that the particle passes through. For a rectangular barrier of height V₀ and width a, T depends exponentially on the product of barrier width and the square root of (V₀ − E): T ∝ exp(−2a√(2m(V₀ − E))/ℏ). This exponential sensitivity means that small changes in barrier width or particle mass produce enormous changes in tunneling probability.

The mass dependence is why tunneling matters most for the lightest particles. Hydrogen, being the lightest atom, tunnels far more readily than heavier atoms. This has profound chemical consequences: enzyme-catalyzed reactions involving hydrogen transfer (such as those catalyzed by alcohol dehydrogenase) show anomalously large kinetic isotope effects — replacing hydrogen with deuterium slows the reaction more than classical transition-state theory predicts, because the heavier deuterium tunnels less efficiently. At low temperatures, where few molecules have enough thermal energy to cross a barrier classically, tunneling can become the **dominant** reaction pathway.

Your knowledge of potential energy surfaces helps you see tunneling in a broader chemical context. A reaction coordinate on a potential energy surface passes through a transition state — an energy maximum along the minimum-energy path. Classical transition-state theory says only molecules with energy above this barrier can react. Tunneling allows molecules to short-cut through the barrier, effectively lowering the apparent activation energy. This is especially important in astrophysical chemistry, where reactions proceed at temperatures of 10–50 K and classical rates would be negligibly slow, yet molecules still form. The rectangular barrier model is a simplification — real barriers have curved shapes better described by Eckart or parabolic potentials — but the essential physics remains: wave-like behavior allows passage through classically forbidden regions, with probability that depends exponentially on barrier width, height, and particle mass.
