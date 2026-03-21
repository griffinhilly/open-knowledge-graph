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

## Questions

```yaml
- question: "A hydrogen atom and a deuterium atom (mass ≈ 2× hydrogen) face identical energy barriers in an enzyme active site. Classical transition-state theory predicts nearly identical reaction rates. Which experimental observation is most consistent with quantum tunneling?"
  type: multiple-choice
  options:
    - "Both atoms react at the same rate — particle mass does not affect tunneling probability"
    - "Deuterium reacts faster because heavier particles have more momentum to push through the barrier"
    - "Hydrogen reacts significantly faster, producing a kinetic isotope effect larger than classical theory predicts"
    - "Hydrogen reacts slightly faster only at high temperatures where tunneling is negligible anyway"
  answer: 2
  explanation: "Tunneling probability depends exponentially on particle mass: T ∝ exp(−2a√(2m(V₀−E))/ℏ). Because mass appears under a square root in the exponent, doubling the mass substantially reduces tunneling probability. The result is an anomalously large kinetic isotope effect (kH/kD >> 7) that cannot be explained by classical transition-state theory — a hallmark signature of tunneling."

- question: "What actually happens to a quantum particle's wave function when it encounters a barrier where E < V (classically forbidden region)?"
  type: multiple-choice
  options:
    - "The wave function abruptly drops to zero at the barrier boundary, reflecting the classical impossibility"
    - "The wave function oscillates within the barrier at a higher frequency to conserve energy"
    - "The wave function decays exponentially inside the barrier but remains non-zero, allowing non-zero amplitude on the far side if the barrier is thin"
    - "The particle momentarily gains kinetic energy from quantum fluctuations to surmount the barrier"
  answer: 2
  explanation: "In the classically forbidden region, the Schrödinger equation yields real exponential solutions rather than oscillating ones. The wave function decays as exp(−κx) where κ = √(2m(V₀−E))/ℏ, but it does not vanish — it threads through and emerges on the far side. Tunneling is a direct consequence of this non-zero amplitude, not of energy fluctuations or going around the barrier."

- question: "A quantum particle with total energy less than the barrier height has a non-zero probability of appearing on the far side of a sufficiently thin barrier."
  type: true-false
  answer: true
  explanation: "This is the defining statement of quantum tunneling. Because the wave function decays exponentially rather than vanishing inside the barrier, it emerges on the far side with reduced amplitude — which means non-zero probability of transmission. This probability approaches zero for very wide or tall barriers but is physically significant for light particles (especially hydrogen) tunneling through narrow barriers."

- question: "Quantum tunneling allows a particle to bypass an energy barrier by briefly borrowing energy from its surroundings to surmount the barrier classically."
  type: true-false
  answer: false
  explanation: "Tunneling does not involve energy borrowing. The particle penetrates the barrier without ever exceeding the barrier height — its total energy remains below V₀ throughout. The correct picture is wave-mechanical: the particle's wave function threads through the classically forbidden region with exponentially decaying amplitude. Energy is conserved; only the probabilistic interpretation of the wave function changes."

- question: "Why does doubling the width of an energy barrier reduce tunneling probability far more dramatically than doubling its height, even though both intuitively make the barrier 'harder' to penetrate?"
  type: short-answer
  answer: "Tunneling probability follows T ∝ exp(−2a√(2m(V₀−E))/ℏ), where a is the barrier width. Width enters the exponent linearly — doubling a doubles the exponent and squares T (e.g., if T = e⁻¹⁰, doubling width gives e⁻²⁰ = T²). Height appears only under a square root, so doubling (V₀−E) increases the exponent by only a factor of √2. This exponential sensitivity to width explains why tunneling is chemically relevant only for very thin barriers and very light particles."
  explanation: "The practical consequence: small changes in the distance between donor and acceptor atoms in enzyme active sites — even a fraction of an ångström — can change hydrogen transfer rates by orders of magnitude. Enzyme evolution can exploit this by precisely positioning reactive groups to minimize tunneling distances."
```

## Explainer

In classical mechanics, a ball rolling toward a hill will either have enough energy to go over the top or it will roll back — there is no third option. But from your study of quantum chemistry foundations, you know that particles are described by wave functions, and wave functions do not abruptly stop at boundaries. When a quantum particle encounters an energy barrier where its total energy E is less than the potential energy V, the wave function does not vanish — it **decays exponentially** inside the barrier. If the barrier is thin enough, the wave function emerges on the other side with diminished but non-zero amplitude. This is **quantum tunneling**: a particle passing through a barrier it classically could never surmount.

The mathematics follows directly from solving the Schrödinger equation in three regions: before the barrier, inside it, and after it. Inside the barrier, the solutions are real exponentials (decaying and growing) rather than oscillating waves. By matching boundary conditions — requiring the wave function and its derivative to be continuous at each interface — you derive the **transmission coefficient** T, which gives the probability that the particle passes through. For a rectangular barrier of height V₀ and width a, T depends exponentially on the product of barrier width and the square root of (V₀ − E): T ∝ exp(−2a√(2m(V₀ − E))/ℏ). This exponential sensitivity means that small changes in barrier width or particle mass produce enormous changes in tunneling probability.

The mass dependence is why tunneling matters most for the lightest particles. Hydrogen, being the lightest atom, tunnels far more readily than heavier atoms. This has profound chemical consequences: enzyme-catalyzed reactions involving hydrogen transfer (such as those catalyzed by alcohol dehydrogenase) show anomalously large kinetic isotope effects — replacing hydrogen with deuterium slows the reaction more than classical transition-state theory predicts, because the heavier deuterium tunnels less efficiently. At low temperatures, where few molecules have enough thermal energy to cross a barrier classically, tunneling can become the **dominant** reaction pathway.

Your knowledge of potential energy surfaces helps you see tunneling in a broader chemical context. A reaction coordinate on a potential energy surface passes through a transition state — an energy maximum along the minimum-energy path. Classical transition-state theory says only molecules with energy above this barrier can react. Tunneling allows molecules to short-cut through the barrier, effectively lowering the apparent activation energy. This is especially important in astrophysical chemistry, where reactions proceed at temperatures of 10–50 K and classical rates would be negligibly slow, yet molecules still form. The rectangular barrier model is a simplification — real barriers have curved shapes better described by Eckart or parabolic potentials — but the essential physics remains: wave-like behavior allows passage through classically forbidden regions, with probability that depends exponentially on barrier width, height, and particle mass.
