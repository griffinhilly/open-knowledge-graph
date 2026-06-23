---
id: alpha-emission-helium
title: Alpha Decay and Helium Nucleus Emission
domain: physics
course: modern-physics
prerequisites:
- id: spontaneous-radioactive-decay
  type: hard
- id: nuclear-structure
  type: soft
- id: alpha-decay-tunneling-nuclear
  type: soft
tags:
- nuclear-physics
- decay
stage: advanced
status: validated
---
# Alpha Decay and Helium Nucleus Emission

## Core Idea
Alpha decay (A → A−4 + ⁴He) occurs in heavy nuclei where emission of a ⁴He nucleus (alpha particle) reaches the stability curve. Alpha particles are tightly bound (high binding energy), making alpha emission energetically favorable. The Q-value α-decay = (M_parent − M_daughter − M_He)c² provides recoil kinetic energies split between daughter nucleus and alpha particle (inverse mass ratio). Alpha decay competes with beta and spontaneous fission.

## Questions

```yaml
- question: "Why does alpha decay specifically emit a helium-4 nucleus (2 protons + 2 neutrons) rather than, say, two separate protons or some other combination of nucleons?"
  type: multiple-choice
  options:
    - "The helium-4 nucleus is the smallest charged fragment, so it experiences the least Coulomb repulsion from the daughter nucleus"
    - "The alpha particle has exceptionally high binding energy (28.3 MeV), making its emission energetically far more favorable than releasing the same four nucleons individually or in other groupings"
    - "Nuclear selection rules prohibit the emission of fragments with odd mass numbers"
    - "Heavy nuclei shed exactly 2 protons and 2 neutrons to maintain the neutron-to-proton ratio in the daughter"
  answer: 1
  explanation: "The reason alpha emission is preferred over other fragmentation modes is energetic: the alpha particle is extraordinarily tightly bound (28.3 MeV total binding energy), so the Q-value for alpha emission is positive (energy is released) while emitting the same nucleons individually or in other configurations would require energy. It's not the smallest fragment (option A) that matters — it's the tightest-bound one. Option D is partially true as a consequence but not the cause; the real driver is the alpha particle's exceptional stability."

- question: "Nucleus A emits alpha particles with kinetic energy of 8 MeV and has a half-life of about 1 microsecond. Nucleus B emits alpha particles with kinetic energy of 5 MeV. Based on the Geiger-Nuttall law, what do you expect for Nucleus B's half-life?"
  type: multiple-choice
  options:
    - "Similar to Nucleus A — small energy differences don't significantly affect nuclear decay rates"
    - "Slightly longer than Nucleus A, perhaps a few milliseconds"
    - "Much longer than Nucleus A — possibly billions of years — because the tunneling probability decreases exponentially with lower alpha energy"
    - "Much shorter than Nucleus A, because slower alphas spend more time near the barrier and tunnel more easily"
  answer: 2
  explanation: "The Geiger-Nuttall law reveals an extreme exponential sensitivity: the tunneling probability depends exponentially on the barrier width, which itself depends on alpha energy. A 3 MeV reduction in alpha energy (from 8 to 5 MeV) translates to an enormously wider and taller effective barrier, reducing the tunneling probability by many orders of magnitude. The half-life range from microseconds (high energy) to billions of years (lower energy) corresponds to alpha energies spanning only about 4–9 MeV. Option D is wrong — slower alphas tunnel *less* easily because they must penetrate more of the barrier."

- question: "Alpha decay in heavy nuclei has a positive Q-value (energy is released), which means the alpha particle has enough energy to exist outside the nucleus. Therefore, the classical picture is sufficient to explain alpha decay — quantum tunneling is not required."
  type: true-false
  answer: false
  explanation: "This is the classic misconception. A positive Q-value means the final state (daughter + alpha) has less energy than the initial state — the decay is thermodynamically favorable. But the alpha must pass *through* the Coulomb barrier to get there. Inside a certain radius, the nuclear attractive force holds the alpha; outside, the Coulomb repulsion pushes it away. The barrier height (tens of MeV) far exceeds the alpha's kinetic energy (~4–9 MeV), so classically the alpha is permanently trapped. Only quantum tunneling — the alpha having a nonzero probability of penetrating the classically forbidden region — allows the decay to occur. This was one of the first great triumphs of quantum mechanics in nuclear physics."

- question: "Alpha particles emitted from a single isotope are nearly monoenergetic (sharply defined energy), unlike beta particles, which have a continuous energy spectrum."
  type: true-false
  answer: true
  explanation: "Alpha particles are monoenergetic because the Q-value is fixed by the masses of parent, daughter, and alpha particle, and this Q-value is almost entirely converted to kinetic energy split in fixed ratio between the alpha and the recoiling daughter (by momentum conservation). Each decay of the same isotope produces an alpha with the same kinetic energy. Beta particles, by contrast, share the Q-value with an antineutrino (or neutrino), which carries away a variable fraction — giving beta particles a continuous energy spectrum from near-zero to Q_max. This historical observation that beta spectra were continuous (while energy conservation requires a fixed Q) was the puzzle that led Pauli to postulate the neutrino."

- question: "Why do small differences in alpha particle energy (say, 4 MeV vs. 8 MeV) translate into an enormous range of radioactive half-lives — from microseconds to billions of years?"
  type: short-answer
  answer: "The half-life is determined by the quantum tunneling probability through the Coulomb barrier. This probability depends exponentially on the barrier penetration integral — roughly proportional to the barrier width and height that the alpha must tunnel through. A higher-energy alpha 'reaches' the outer edge of the barrier much sooner (the barrier is thinner for it), dramatically increasing tunneling probability. Because the tunneling probability enters as an exponential, even a factor-of-two change in alpha energy translates into tunneling probabilities spanning many orders of magnitude. This exponential sensitivity (captured quantitatively by the Geiger-Nuttall law) explains why isotopes with similar nuclear structure can have half-lives ranging from microseconds to the age of the universe."
  explanation: "The intuition is: tunneling probability ∝ e^(−2γ) where γ depends on the integral of √(V(r) − E) through the barrier. Small changes in E change γ significantly because E appears under a square root and the integral is over a large range. This exponential amplification of small energy differences into enormous half-life differences is why nuclear physicists can date billion-year-old rocks using uranium decay while other alpha emitters decay almost instantly."
```

## Explainer

From your study of radioactive decay you know that unstable nuclei spontaneously transform to release energy, and from nuclear structure you know that the **binding energy per nucleon** peaks around mass number A ≈ 56 (iron) and decreases for very heavy nuclei. Alpha decay is the mechanism by which heavy nuclei (typically A > 140) shed four nucleons at once to move toward greater stability. The key to understanding why the emitted fragment is specifically a helium-4 nucleus — two protons and two neutrons — lies in its exceptional stability: the alpha particle has a binding energy of 28.3 MeV, making it one of the most tightly bound light nuclei. Emitting an alpha particle is energetically much more favorable than emitting four individual nucleons or even two separate protons and two separate neutrons.

The energetics are governed by the **Q-value**: Q = (M_parent − M_daughter − M_α)c². When Q > 0, energy is released and the decay is spontaneous. This Q-value appears almost entirely as kinetic energy of the products, split between the alpha particle and the recoiling daughter nucleus in the inverse mass ratio. Since the daughter nucleus is much heavier (A − 4 vs. 4), it recoils with very little kinetic energy, and the alpha particle carries away nearly all of the Q-value as kinetic energy. This is why alpha particles from a given decay appear as a nearly monoenergetic beam — their energy is sharply defined by Q, unlike the continuous energy spectrum of beta particles. Alpha spectroscopy exploits this: measuring the energy of emitted alpha particles identifies the parent nucleus.

There is, however, a profound puzzle. For heavy nuclei, the Q-value is positive — the decay is energetically allowed — yet the nucleus often persists for millions or billions of years before decaying. Classically, the alpha particle is trapped inside the nucleus by a **Coulomb barrier**: to escape, it would need to tunnel through a potential energy barrier (the electrostatic repulsion between the alpha's +2e charge and the daughter's +Ze charge) that is several tens of MeV high, far above the alpha's kinetic energy. This is impossible classically, but quantum mechanics allows **tunneling**: the alpha particle has a non-zero probability of penetrating the barrier. The tunneling probability depends exponentially on the barrier height and width, which explains the enormous variation in alpha-decay half-lives (from microseconds to billions of years) that correlates with relatively small variations in alpha energy (from about 4 to 9 MeV). This exponential sensitivity — known as the **Geiger-Nuttall law** — was one of the first quantitative triumphs of quantum tunneling in nuclear physics.

Alpha decay produces a daughter nucleus that is often left in an **excited state**, explaining why alpha decay is frequently followed by gamma emission. The daughter nucleus then de-excites by emitting one or more gamma-ray photons before reaching its ground state. The complete decay chain of heavy elements — thorium, uranium, radium — consists of alternating alpha and beta decays, each step moving the nucleus closer to the valley of stability on the nuclear chart, with gamma emission accompanying many steps.

