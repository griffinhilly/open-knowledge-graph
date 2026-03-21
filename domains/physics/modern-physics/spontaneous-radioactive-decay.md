---
id: spontaneous-radioactive-decay
title: Spontaneous Radioactive Decay
domain: physics
course: modern-physics
prerequisites:
- id: radioactive-decay
  type: hard
- id: binding-energy-stability-curve
  type: soft
builds-toward:
- alpha-emission-helium
- beta-emission-weak-force
tags:
- nuclear-physics
- radioactivity
stage: advanced
status: draft
---

# Spontaneous Radioactive Decay

## Core Idea
Unstable nuclei decay spontaneously to reach the stability curve, releasing energy via particle or photon emission. The decay rate follows exponential law N(t) = N₀ exp(−λt), where λ is the decay constant and half-life t₁/₂ = (ln 2)/λ. The three main decay modes are alpha (⁴He emission), beta (electron emission), and gamma (photon emission). Q-value (energy released) determines whether a decay is energetically allowed.

## Questions

```yaml
- question: "A particular radioactive nucleus has a half-life of 10 years. A sample nucleus has existed for 30 years without decaying. Compared to a freshly created nucleus of the same isotope, what is the probability that this 'old' nucleus decays in the next second?"
  type: multiple-choice
  options:
    - "Higher — the old nucleus has built up energy and is now overdue for decay"
    - "Lower — the fact that it survived 30 years suggests it is an unusually stable specimen"
    - "Identical — each nucleus has the same constant decay probability per unit time regardless of age"
    - "It depends on the decay mode — alpha decay is age-independent, but beta decay is not"
  answer: 2
  explanation: "Radioactive decay is a quantum process: each nucleus has a fixed, age-independent probability λ of decaying per unit time. A nucleus that has 'survived' 30 years is not 'overdue' — there is no internal clock counting down, no built-up pressure, and no memory of past survival. This is the quantum analogue of a fair coin: heads on the last flip tells you nothing about the next flip. The exponential decay law follows directly from this constant-probability assumption. Options A and B both commit the 'gambler's fallacy' at the nuclear level — a common misconception that the probabilistic nature of decay eliminates."

- question: "Why is alpha decay the dominant spontaneous decay mode for the heaviest nuclei (mass number A > 200), rather than single-proton or single-neutron emission?"
  type: multiple-choice
  options:
    - "Alpha particles have the highest charge and therefore the greatest ability to tunnel through the Coulomb barrier"
    - "Alpha particles are the largest particles that can escape the nucleus; heavier fragments are always trapped"
    - "The alpha particle (⁴He) is doubly magic and extraordinarily tightly bound, so emitting it releases more energy (Q > 0) than emitting individual nucleons for these heavy nuclei"
    - "Heavy nuclei are neutron-rich, and alpha emission is the only way to simultaneously remove both protons and neutrons"
  answer: 2
  explanation: "The key is the Q-value. The alpha particle is one of the most tightly bound nuclei per nucleon (doubly magic: Z=2, N=2). For very heavy nuclei on the right side of the binding energy curve, total binding energy increases when the heavy nucleus loses four nucleons as an alpha particle — the daughter is more tightly bound per nucleon than the parent, so Q > 0. Emitting a single proton or neutron yields a much smaller energy release because the individual nucleon is not specially stabilized. Option D has some truth (heavy nuclei are often above the stability line), but misidentifies the mechanism — alpha decay is favored by energetics, not by the need to remove equal numbers of each nucleon type."

- question: "Two radioactive samples of different isotopes both contain exactly 10²⁴ atoms. They will necessarily have the same activity (decays per second)."
  type: true-false
  answer: false
  explanation: "Activity A = λN, where λ is the decay constant and N is the number of atoms. Two samples with the same N but different decay constants λ will have dramatically different activities. For example, ¹⁴C (t₁/₂ ≈ 5,730 years, so λ is very small) and ²¹⁰Po (t₁/₂ = 138 days, λ is much larger) would show orders-of-magnitude different activity from the same number of atoms. A nuclide with a shorter half-life has a larger λ and therefore higher activity per atom. Equal atom counts tell you nothing about equal decay rates."

- question: "A nuclear decay is spontaneous if and only if the Q-value is positive — meaning the total mass-energy of the products is less than that of the parent nucleus."
  type: true-false
  answer: true
  explanation: "The Q-value is defined as Q = [M(parent) − Σ M(products)]c², representing the energy released. If Q > 0, energy is released and the decay is energetically allowed to proceed spontaneously. If Q < 0, the products would have more mass-energy than the parent, which violates conservation of energy — the decay cannot proceed without an external energy input. Q > 0 is a necessary condition for spontaneous decay (though a positive Q doesn't guarantee a fast decay — some decays are energetically allowed but kinetically inhibited by a large Coulomb barrier, as in alpha decay from heavy nuclei)."

- question: "Explain why the exponential decay law N(t) = N₀ exp(−λt) follows from the assumption that each nucleus has a constant, age-independent probability of decaying per unit time."
  type: short-answer
  answer: "If each nucleus has a constant probability λ of decaying per unit time (independent of age), then in a small interval dt, the number of decays from a population of N nuclei is dN = −λN dt. Rearranging: dN/N = −λ dt. Integrating both sides from 0 to t gives ln(N/N₀) = −λt, which exponentiates to N(t) = N₀ exp(−λt). The exponential form is a direct mathematical consequence of the constant-probability-per-unit-time assumption — nothing more is required. The half-life t₁/₂ = ln(2)/λ is the time at which N = N₀/2, found by setting exp(−λt) = 1/2."
  explanation: "This derivation reveals that the exponential law is not a complicated empirical fact but follows from a single simple assumption: memorylessness (each nucleus decays independently with fixed probability per unit time). This is the continuous-time analogue of a geometric distribution. Understanding this connection helps explain why radioactive decay is used in dating — the constant λ means the exponential clock runs at a fixed rate regardless of temperature, pressure, or chemical environment."
```

## Explainer

The binding-energy curve you studied earlier tells you which nuclei are stable and which are not. A nucleus sitting away from the valley of stability — either too neutron-rich, too proton-rich, or too heavy — has excess energy relative to a lower-energy configuration. Spontaneous radioactive decay is the process by which such a nucleus rearranges itself to shed that excess energy, emitting particles or photons in the process. The driving force is always the same: the final products have lower total mass-energy than the parent, and that difference — the **Q-value** — is released as kinetic energy of the emitted particles. If Q < 0, the decay is energetically forbidden; if Q > 0, it can proceed spontaneously.

The exponential decay law N(t) = N₀ exp(−λt) follows from a single profound assumption: each nucleus decays independently with a constant probability λ per unit time, regardless of age. This is the quantum nature of decay — there is no "built-up pressure" that makes an old nucleus more likely to decay than a fresh one. Because each nucleus decides independently, a sample of N nuclei loses dN = −λN dt nuclei per interval, which integrates directly to the exponential law. The **half-life** t₁/₂ = (ln 2)/λ is the time after which exactly half the original sample remains on average. Note that two different nuclides can have the same total number of atoms but very different activity (decays per second), because activity A = λN depends on both population and decay constant.

The three main decay modes each serve a different purpose on the stability chart. **Alpha decay** (emission of ⁴He) is how heavy nuclei above A ≈ 150 shed both protons and neutrons efficiently; the alpha particle is doubly magic and extraordinarily tightly bound, making its emission energetically favorable despite the Coulomb barrier the particle must tunnel through. **Beta decay** shifts a nucleus along constant-A isobars — beta-minus (n → p + e⁻ + antineutrino) moves neutron-rich nuclei toward stability, while beta-plus moves proton-rich ones. **Gamma decay** does not change A or Z at all; it is the nucleus shedding excess energy after a previous alpha or beta decay has left it in an excited nuclear state, exactly analogous to atomic photon emission after an electron transition. Understanding which mode applies requires reading the nucleus's position on the N-Z chart relative to the valley of stability.

The Q-value bridges the binding-energy curve to specific decays. For alpha decay, Q = [M(parent) − M(daughter) − M(⁴He)]c². If your binding-energy curve shows that removing four nucleons increases binding energy per nucleon in the daughter, Q > 0 and the decay is allowed. This is why alpha decay dominates for very heavy elements — their binding energy per nucleon is actually lower than that of lighter nuclei, so shedding nucleons increases total binding energy. The same logic explains why spontaneous fission becomes competitive with alpha decay for the heaviest elements: splitting into two medium-mass fragments releases even more binding energy than emitting a single alpha particle.
