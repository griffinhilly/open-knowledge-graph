---
id: alpha-decay-emission
title: Alpha Decay and Helium Nucleus Emission
domain: physics
course: modern-physics
prerequisites:
- id: nuclear-mass-binding-energy
  type: hard
- id: quantum-tunneling
  type: hard
builds-toward:
- decay-constant-half-life-exponential
tags:
- nuclear
- radioactivity
- decay
stage: expert
status: validated
---

# Alpha Decay and Helium Nucleus Emission

## Core Idea
In alpha decay, a nucleus emits an alpha particle (⁴₂He nucleus), transforming into a lighter nucleus. Alpha particles are highly stable due to strong binding energy, making alpha emission favorable for heavy nuclei. The process occurs via quantum tunneling through the Coulomb barrier; the alpha particle's existence inside the nucleus is unstable due to electrostatic repulsion.

## Questions

```yaml
- question: "Uranium-238 (Q ≈ 4.3 MeV) has a half-life of 4.5 billion years, while Polonium-212 (Q ≈ 9.0 MeV) decays in 300 nanoseconds. What is the primary reason for this 23-order-of-magnitude difference?"
  type: multiple-choice
  options:
    - "Po-212 has a much higher atomic number, so Coulomb repulsion is stronger and pushes the alpha out more forcefully"
    - "The tunneling probability depends exponentially on the barrier integral, so a larger Q-value dramatically thins the Coulomb barrier and increases the decay rate"
    - "U-238 produces a less stable alpha particle than Po-212, slowing the emission process"
    - "Higher-Z nuclei require more time to assemble the alpha particle from individual nucleons before emission"
  answer: 1
  explanation: "The Gamow factor places the barrier integral in an exponent — small changes in Q produce enormous changes in tunneling probability. A larger Q-value means the alpha's energy is closer to the top of the Coulomb barrier, making the classically forbidden region thinner and easier to tunnel through. The difference between 4.3 MeV and 9 MeV in barrier geometry, amplified by exponential sensitivity, generates the 23-order-of-magnitude difference in half-lives. Option A conflates barrier height with tunneling probability; higher Z raises the barrier but the Q-value determines how thick the forbidden region is at the alpha's actual energy."

- question: "Why does alpha decay preferentially emit a helium-4 nucleus rather than, say, a single proton or a deuteron?"
  type: multiple-choice
  options:
    - "Alpha particles are the only fragments light enough to tunnel through the Coulomb barrier"
    - "The ⁴He nucleus has exceptionally high binding energy per nucleon (~7.07 MeV) due to fully-paired spins in a complete nuclear shell, making alpha emission strongly Q-positive for heavy nuclei"
    - "A single proton carries too little charge to interact with the Coulomb barrier, so it cannot be emitted"
    - "The strong nuclear force exclusively binds nucleons in groups of four, so only alpha particles can be released"
  answer: 1
  explanation: "Energetic favorability — not tunneling geometry — determines which fragment is emitted. The alpha particle has an unusually high binding energy per nucleon because it is a doubly-magic nucleus with all nucleon spins paired. Emitting an alpha releases substantially more energy than emitting a single proton, making the Q-value positive for heavy nuclei. The reaction is favored because the products (alpha + daughter) are more tightly bound in total than the parent, and that released energy (kinetic energy) is what the emitted fragment carries away."

- question: "Alpha particles escape the nucleus by gaining enough kinetic energy to classically surmount the Coulomb barrier."
  type: true-false
  answer: false
  explanation: "This is the central misconception about alpha decay. The alpha's total energy is *less* than the height of the Coulomb barrier — it occupies a classically forbidden region between the nuclear surface and the classical turning point. Classical mechanics predicts zero escape probability. Quantum mechanically, the alpha's wavefunction decays exponentially through this forbidden region but emerges on the other side with nonzero amplitude, allowing a small but real probability of detection outside the nucleus at any moment. This is quantum tunneling, not classical barrier-clearing."

- question: "A nucleus with a larger Q-value for alpha decay will generally have a shorter half-life than an otherwise-identical nucleus with a smaller Q-value."
  type: true-false
  answer: true
  explanation: "The Geiger-Nuttall law captures exactly this relationship: the log of the decay constant is linear in the log of the alpha's energy, spanning many orders of magnitude across different nuclides. A larger Q-value raises the alpha's kinetic energy relative to the Coulomb barrier, thinning the classically forbidden region. Since the Gamow factor places the barrier integral in an exponent, even a moderate increase in Q produces a dramatically higher tunneling probability and therefore a much shorter half-life."

- question: "Why does alpha decay require quantum tunneling rather than classical barrier crossing, and what does this imply about the energy of the emitted alpha particle?"
  type: short-answer
  answer: "The Coulomb barrier between the nuclear surface and the classical turning point has a potential energy that exceeds the alpha's total kinetic energy. Classically, the alpha cannot exist in this region and cannot escape. Quantum mechanically, the wavefunction decays exponentially but remains nonzero through the forbidden region, giving a finite — though small — probability of the alpha being found outside the nucleus. This means the emitted alpha does not have enough energy to have gone over the barrier; it tunnels through it. Its kinetic energy after emission equals the Q-value of the decay, which is less than the peak Coulomb barrier height."
  explanation: "The key insight is the gap between the barrier height and the alpha's energy. For U-238, the Coulomb barrier peaks at around 30 MeV, yet the emitted alpha has only ~4.3 MeV. Classically, escape is impossible. Quantum mechanically, the wavefunction leaks through, and the rate of leakage — set by the Gamow factor — depends exponentially on the barrier thickness, which in turn depends on Q. This explains both why alpha decay can occur at all and why its rate is so sensitive to the decay energy."
```

## Explainer

From your study of nuclear mass and binding energy, you know that nuclei are held together by the strong nuclear force competing against the electromagnetic repulsion between protons. The strong force is short-range (a few femtometers) and very powerful; Coulomb repulsion is long-range and grows as Z increases. For light and medium nuclei, the strong force wins comfortably. For very heavy nuclei (Z > 82 or so), the nucleus is large enough that the short-range strong force cannot effectively bind every nucleon pair across the full diameter, while Coulomb repulsion among the growing number of protons keeps increasing. These nuclei are energetically unstable against shedding mass.

Why emit an alpha particle specifically — two protons plus two neutrons — rather than a single proton, two protons, or some other fragment? The answer lies in binding energy. The alpha particle (⁴He nucleus) has an exceptionally high binding energy per nucleon (~7.07 MeV), the result of a fully filled nuclear shell with all spins paired. Emitting an alpha releases substantially more energy per nucleon removed than emitting, say, a single proton. The **Q-value** — the difference in total binding energy between the parent and the alpha-plus-daughter system — is positive for heavy nuclei, meaning the products are more tightly bound than the parent. This energy appears as kinetic energy of the emitted alpha and recoiling daughter. Energetically favorable does not yet mean it happens, however.

This is where **quantum tunneling** — your other prerequisite — becomes essential. Plot the potential energy of an alpha particle as a function of its distance from the center of the parent nucleus. Inside the nucleus, the strong force creates a potential well — the alpha is bound. Outside, the Coulomb repulsion creates a tall positive barrier, rising from the nuclear surface and declining as the alpha moves farther away. Between the nuclear surface and the distance where the Coulomb barrier drops back to the alpha's energy, there is a classically forbidden region: the alpha's total energy is *less* than the potential energy of the barrier. Classically, it cannot escape. Quantum mechanically, the alpha's wavefunction does not abruptly vanish at the barrier — it decays exponentially through the classically forbidden region and emerges on the other side with nonzero amplitude. There is a small but real probability of finding the alpha outside the nucleus at any moment. This leakage is alpha decay.

The decay rate depends exponentially on the barrier integral, through a factor known as the **Gamow factor**: G ~ exp(−2∫√(2m(V(r)−E)/ℏ²) dr). Because this integral is in the exponent, small changes in the alpha's energy Q lead to enormous changes in decay rate. This extreme sensitivity is captured by the **Geiger-Nuttall law**: a log-log plot of decay constant versus alpha energy gives a straight line across many orders of magnitude. Uranium-238 has a Q-value of ~4.3 MeV, a tall thick barrier, and a half-life of 4.5 billion years. Polonium-212 has Q ~ 8.95 MeV, a thinner barrier, and decays in 300 nanoseconds. The same mechanism, differing only in barrier geometry, spans 23 orders of magnitude in half-life — one of the most striking quantitative successes of early quantum mechanics applied to nuclear physics.
