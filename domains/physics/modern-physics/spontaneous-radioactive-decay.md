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

## Explainer

The binding-energy curve you studied earlier tells you which nuclei are stable and which are not. A nucleus sitting away from the valley of stability — either too neutron-rich, too proton-rich, or too heavy — has excess energy relative to a lower-energy configuration. Spontaneous radioactive decay is the process by which such a nucleus rearranges itself to shed that excess energy, emitting particles or photons in the process. The driving force is always the same: the final products have lower total mass-energy than the parent, and that difference — the **Q-value** — is released as kinetic energy of the emitted particles. If Q < 0, the decay is energetically forbidden; if Q > 0, it can proceed spontaneously.

The exponential decay law N(t) = N₀ exp(−λt) follows from a single profound assumption: each nucleus decays independently with a constant probability λ per unit time, regardless of age. This is the quantum nature of decay — there is no "built-up pressure" that makes an old nucleus more likely to decay than a fresh one. Because each nucleus decides independently, a sample of N nuclei loses dN = −λN dt nuclei per interval, which integrates directly to the exponential law. The **half-life** t₁/₂ = (ln 2)/λ is the time after which exactly half the original sample remains on average. Note that two different nuclides can have the same total number of atoms but very different activity (decays per second), because activity A = λN depends on both population and decay constant.

The three main decay modes each serve a different purpose on the stability chart. **Alpha decay** (emission of ⁴He) is how heavy nuclei above A ≈ 150 shed both protons and neutrons efficiently; the alpha particle is doubly magic and extraordinarily tightly bound, making its emission energetically favorable despite the Coulomb barrier the particle must tunnel through. **Beta decay** shifts a nucleus along constant-A isobars — beta-minus (n → p + e⁻ + antineutrino) moves neutron-rich nuclei toward stability, while beta-plus moves proton-rich ones. **Gamma decay** does not change A or Z at all; it is the nucleus shedding excess energy after a previous alpha or beta decay has left it in an excited nuclear state, exactly analogous to atomic photon emission after an electron transition. Understanding which mode applies requires reading the nucleus's position on the N-Z chart relative to the valley of stability.

The Q-value bridges the binding-energy curve to specific decays. For alpha decay, Q = [M(parent) − M(daughter) − M(⁴He)]c². If your binding-energy curve shows that removing four nucleons increases binding energy per nucleon in the daughter, Q > 0 and the decay is allowed. This is why alpha decay dominates for very heavy elements — their binding energy per nucleon is actually lower than that of lighter nuclei, so shedding nucleons increases total binding energy. The same logic explains why spontaneous fission becomes competitive with alpha decay for the heaviest elements: splitting into two medium-mass fragments releases even more binding energy than emitting a single alpha particle.
