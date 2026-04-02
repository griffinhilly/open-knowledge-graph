---
id: alpha-decay-tunneling-nuclear
title: Alpha Decay and Tunneling Through the Coulomb Barrier
domain: physics
course: modern-physics
prerequisites:
- id: barrier-tunneling-transmission-probability
  type: hard
- id: radioactive-decay
  type: hard
tags:
- alpha-decay
- tunneling
- nuclear-physics
stage: expert
status: validated
---

# Alpha Decay and Tunneling Through the Coulomb Barrier

## Core Idea
In alpha decay, a nucleus emits an alpha particle (helium nucleus) and transforms to a lighter nucleus. The Coulomb barrier between the alpha particle and daughter nucleus is several MeV high, yet alpha particles are emitted with 4–9 MeV kinetic energy. This is only possible through quantum tunneling. The half-life is exponentially sensitive to the tunneling probability, explaining huge variations (from microseconds to billions of years) in alpha-decay rates.

## How It's Best Learned
Calculate the Coulomb barrier height and width for an alpha-emitting nucleus. Use WKB tunneling probability to estimate the alpha decay rate and half-life. Compare with experimental values and understand order-of-magnitude agreements and discrepancies.

## Common Misconceptions
The alpha particle is not ejected due to centrifugal effects overcoming the barrier (tunneling is quantum-mechanical). The Q-value (kinetic energy available from mass-energy) is less than the barrier height, yet decay occurs due to tunneling. Increasing the barrier thickness dramatically reduces the decay rate (exponentially).

## Questions

```yaml
- question: "Nucleus A emits alpha particles with 5 MeV kinetic energy and has a half-life of 10,000 years. Nucleus B has a similar structure but emits alphas at 6 MeV. What should you expect for nucleus B's half-life?"
  type: multiple-choice
  options:
    - "Slightly shorter — perhaps around 8,000 to 9,000 years, since 6 MeV is only modestly higher"
    - "Dramatically shorter — possibly many orders of magnitude shorter — due to the exponential sensitivity of the Gamow factor"
    - "Longer — higher-energy alphas face a wider effective barrier because of larger Coulomb repulsion"
    - "Essentially the same — a 20% energy increase has a small effect on a quantum-mechanical process"
  answer: 1
  explanation: "This is the key insight of the Gamow factor: the tunneling probability is exponentially sensitive to the alpha energy. The Gamow exponent G = ∫κ(r) dr decreases as alpha energy increases (the classically forbidden region narrows), but because G enters as exp(−2G), even a small change in G produces an enormous change in decay rate. The Geiger-Nuttall law captures this empirically: alpha energies span only a factor of ~2 (4–9 MeV) while half-lives span 25 orders of magnitude (microseconds to billions of years). A 1 MeV increase in alpha energy can easily reduce the half-life by a factor of 10⁶ or more."

- question: "Why can't classical mechanics account for alpha decay in heavy nuclei?"
  type: multiple-choice
  options:
    - "Classical mechanics doesn't include the strong nuclear force, so it cannot model nuclear binding"
    - "The alpha particle's kinetic energy (4–9 MeV) is less than the Coulomb barrier height (~25–30 MeV), so classically the alpha is permanently trapped inside the nucleus"
    - "Classical mechanics predicts too fast a decay rate, since it allows the alpha to bounce off the barrier indefinitely"
    - "Classical mechanics cannot handle Coulomb interactions at the femtometer scale"
  answer: 1
  explanation: "The Coulomb barrier between the alpha particle and the daughter nucleus peaks at roughly 25–30 MeV for heavy nuclei, yet the alpha's kinetic energy (set by Q-value) is only 4–9 MeV. Classically, a particle cannot cross an energy barrier higher than its kinetic energy — it would bounce back every time. Yet alpha decay does occur, in some nuclei with extraordinary speed. The only explanation is quantum tunneling: the alpha's wavefunction has nonzero amplitude in the classically forbidden barrier region and emerges on the other side with finite probability. This is not a correction to classical mechanics; it is a fundamentally quantum phenomenon."

- question: "The Geiger-Nuttall law — which shows that alpha-decay half-lives span 25 orders of magnitude while emitted alpha energies vary by only a factor of two — is a direct consequence of the exponential sensitivity of tunneling probability to the Gamow factor."
  type: true-false
  answer: true
  explanation: "Yes. The Gamow factor G enters the tunneling probability as exp(−2G), so small changes in G (driven by small changes in alpha energy) produce enormous changes in the decay rate. The Gamow-Sommerfeld factor for the Coulomb barrier decreases steeply with increasing alpha energy, amplifying a factor-of-2 energy range into a 10²⁵ range of half-lives. The Geiger-Nuttall law is not an independent empirical coincidence — it is a quantitative prediction of the WKB tunneling calculation applied to the Coulomb barrier."

- question: "Uranium-238 and polonium-212 have vastly different half-lives (4.5 billion years vs. 300 nanoseconds) because they decay by fundamentally different nuclear mechanisms."
  type: true-false
  answer: false
  explanation: "Both nuclei decay by exactly the same mechanism: quantum tunneling of an alpha particle through the Coulomb barrier. The 25-order-of-magnitude difference in half-life arises entirely from the Gamow factor. Polonium-212 emits alphas at ~8.8 MeV; uranium-238 at ~4.3 MeV. This ~2× energy difference makes the Gamow exponent much smaller for Po-212, giving a tunneling probability that is roughly 10²⁵ times larger. Same mechanism, same physics — only the Gamow factor differs, and exponential amplification does the rest. This is one of the most striking demonstrations of exponential sensitivity in all of physics."

- question: "Why does a small increase in the kinetic energy of the emitted alpha particle produce such a dramatic decrease in the nucleus's half-life?"
  type: short-answer
  answer: "The tunneling probability is T ≈ exp(−2G), where G is the Gamow factor — the integral of the local inverse decay length through the classically forbidden barrier region. A higher alpha energy means the particle's energy is closer to the barrier height, so the classically forbidden region (where E < V(r)) is narrower and shallower. This reduces G, but because G enters as an exponent, even a modest reduction in G produces an exponentially large increase in T. The decay rate λ = ν × T (attempt frequency times tunneling probability), so an exponentially larger T means an exponentially larger decay rate — and exponentially shorter half-life. The factor-of-2 range in alpha energies translates into a 10²⁵ range in half-lives through this exponential mechanism."
  explanation: "This exponential sensitivity is the defining feature of quantum tunneling in nuclear physics. It means that half-life is extraordinarily sensitive to the nuclear structure details that determine the Q-value (the mass-energy difference available for the decay). Nuclei that are 'almost stable' against alpha decay can be pushed to instability by surprisingly small changes in the alpha energy, and this sensitivity makes the Geiger-Nuttall law both a striking empirical regularity and a precise quantitative prediction of WKB theory."
```

## Explainer

From your study of barrier tunneling, you know that a quantum particle can penetrate a potential energy barrier even when its total energy is less than the barrier height — the transmission probability depends exponentially on the barrier's width and height. From radioactive decay, you know that certain unstable nuclei emit particles with characteristic half-lives. Alpha decay is where these two ideas collide: the enormous puzzle of how an alpha particle escapes the nucleus is resolved entirely by quantum tunneling, producing one of the most dramatic demonstrations of exponential sensitivity in all of physics.

Inside the nucleus, the alpha particle (a helium-4 nucleus: 2 protons, 2 neutrons, tightly bound) is held in by the **strong nuclear force**, which creates a deep potential well extending to the nuclear radius (~1–10 fm). Outside the nucleus, the strong force turns off abruptly, and the alpha particle experiences only **Coulomb repulsion** from the daughter nucleus — a barrier that rises steeply as the alpha approaches from outside. The barrier peak is typically 25–30 MeV for heavy nuclei, yet the alpha's kinetic energy (the Q-value set by mass-energy conservation) is only 4–9 MeV. Classically, the alpha is permanently trapped. Quantum mechanically, its wavefunction has nonzero amplitude in the classically forbidden region, decaying exponentially through the barrier but emerging with a small but finite amplitude on the outside — corresponding to a finite probability of escape per unit time.

The **Gamow factor** G = exp(−2∫κ(r) dr) captures the tunneling probability, where κ(r) = √(2m[V(r)−E])/ℏ is the local inverse decay length inside the barrier. For the Coulomb barrier, this integral can be evaluated analytically using the WKB approximation, giving the **Gamow-Sommerfeld factor** that decreases steeply with decreasing alpha energy. The extraordinary feature is exponential sensitivity: a small change in alpha energy produces a huge change in the tunneling exponent, and thus in the half-life. This explains the **Geiger-Nuttall law** — the empirical observation that alpha-decay half-lives span 25 orders of magnitude (from microseconds for some transuranic nuclei to 4.5 billion years for uranium-238) while the emitted alpha energies vary by only a factor of two (4–9 MeV). The exponential in the Gamow factor amplifies tiny energy differences into astronomical half-life ratios.

The physical picture is vivid: the alpha particle rattles around inside the nucleus at nuclear velocities (~0.01c), striking the Coulomb barrier roughly 10²¹ times per second. Each attempt has a small tunneling probability T ≈ exp(−2G), and the decay rate is λ = ν × T where ν is the attempt frequency. For uranium-238, T is so small (~10⁻³⁸) that the average wait before escape is ~4.5 billion years. For polonium-212, a slightly higher alpha energy reduces the barrier integral enough to make T many orders of magnitude larger — and the half-life shrinks to 300 nanoseconds. Both nuclei decay by exactly the same mechanism; only the Gamow factor differs, and that difference, amplified exponentially, accounts for the entire 25-order-of-magnitude range. This is quantum tunneling operating at its most dramatic scale.
