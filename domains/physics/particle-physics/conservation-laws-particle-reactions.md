---
id: conservation-laws-particle-reactions
title: 'Conservation Laws in Particle Reactions: Baryon Number, Lepton Number, and Strangeness'
domain: physics
course: particle-physics
prerequisites:
- id: conservation-of-electric-charge
  type: hard
- id: beta-emission-weak-force
  type: soft
- id: pair-production-annihilation
  type: soft
- id: four-momentum-energy-conservation
  type: soft
builds-toward:
- quark-model-hadron-spectroscopy
- lepton-flavor
- leptogenesis-and-baryogenesis
tags:
- conservation-laws
- baryon-number
- lepton-number
- strangeness
- selection-rules
stage: advanced
status: validated
---

# Conservation Laws in Particle Reactions: Baryon Number, Lepton Number, and Strangeness

## Core Idea
Particle reactions and decays obey conservation of energy, momentum, angular momentum, and electric charge, plus additional additive quantum numbers. Baryon number (+1 for protons, neutrons, and other baryons, −1 for antibaryons, 0 for mesons and leptons) has never been seen to change. Lepton numbers, counted separately for the electron, muon, and tau families, are conserved in all observed reactions except neutrino oscillations. Strangeness is conserved by the strong and electromagnetic interactions but can change by one unit in weak decays, which is why strange particles live far longer than strong-interaction time scales.

## How It's Best Learned
Build a table of particles with columns for charge, baryon number, each lepton number, and strangeness. Then test proposed reactions column by column, marking which law each forbidden reaction breaks. Use observed lifetimes to show how strangeness-changing decays are slow. Finish with the stability of the proton as the most striking consequence of baryon number conservation.

## Common Misconceptions
- Antileptons carry lepton number +1, like leptons. (Antileptons, including antineutrinos and positrons, carry lepton number −1.)
- Strangeness is conserved in every process. (Weak decays such as Λ⁰ → p + π⁻ change strangeness by one unit.)
- Rest mass is conserved in particle reactions. (Total energy is conserved, but rest mass can be converted into kinetic energy and back; the sum of rest masses usually changes.)

## Questions

```yaml
- question: "Which of these processes is allowed by all the conservation laws?"
  type: multiple-choice
  options: ["n → p + e⁻ + νₑ", "n → p + e⁻ + ν̄ₑ", "p → π⁰ + e⁺", "π⁻ → μ⁻ + ν_μ"]
  answer: 1
  explanation: "Neutron decay produces an electron (Lₑ = +1) and an electron antineutrino (Lₑ = −1), keeping Lₑ = 0. The first option has Lₑ = 2, the third changes baryon number from 1 to 0, and the fourth has L_μ = 2."
- question: "The decay Λ⁰ → p + π⁻ conserves strangeness."
  type: true-false
  answer: false
  explanation: "The Λ⁰ (uds) has strangeness −1, while the proton and pion have strangeness 0. Strangeness changes by one unit, so the decay must proceed by the weak interaction, giving the Λ⁰ a lifetime of about 2.6 × 10⁻¹⁰ s."
- question: "Why is the proton stable, even though lighter particles such as positrons and pions exist?"
  type: multiple-choice
  options: ["It has no electric charge", "It is the lightest baryon, so any decay would have to change baryon number", "It is a lepton", "It has zero strangeness"]
  answer: 1
  explanation: "Every decay product lighter than the proton is a meson or lepton with baryon number 0. Experiments set the proton lifetime above about 10³⁴ years."
- question: "Check the decay μ⁻ → e⁻ + ν̄ₑ + ν_μ for electron and muon lepton number."
  type: short-answer
  answer: "L_μ: 1 → 0 + 0 + 1 = 1. Lₑ: 0 → 1 + (−1) + 0 = 0. Both are conserved."
  explanation: "The muon's L_μ passes to the muon neutrino, while the electron and electron antineutrino carry opposite Lₑ values that sum to zero."
```

## Explainer
Energy, momentum, angular momentum, and charge are conserved in every reaction ever observed. They do not explain everything, though. A proton could decay into a positron and a neutral pion while satisfying all four, yet no such decay has been seen. Physicists therefore introduced further conserved quantities, each an integer that adds up over all particles in a reaction.

Baryon number B is +1 for each baryon (proton, neutron, Λ, and so on), −1 for each antibaryon, and 0 for mesons, leptons, and photons. In the quark model each quark carries B = 1/3. No experiment has ever seen B change. The proton, as the lightest baryon, has nowhere to go: any decay would lower B. Large detectors such as Super-Kamiokande have watched enormous numbers of protons and place the lifetime above about 10³⁴ years, vastly longer than the age of the universe.

Lepton number comes in three kinds, Lₑ, L_μ, and L_τ. The electron and electron neutrino have Lₑ = +1, and their antiparticles have Lₑ = −1, with the same pattern for the muon and tau families. In neutron decay, n → p + e⁻ + ν̄ₑ, the electron and antineutrino carry Lₑ = +1 and −1, so the total stays zero. This is why the neutral particle emitted in beta-minus decay is an antineutrino. The separate family numbers are broken only by neutrino oscillations, in which a neutrino created as one flavor is later detected as another.

Strangeness S tracks the strange quark, with S = −1 for each s quark and +1 for each anti-s. In the 1950s, particles such as kaons and the Λ⁰ puzzled physicists. They were produced copiously in strong collisions but decayed slowly, with lifetimes near 10⁻¹⁰ s instead of the 10⁻²³ s typical of strong decays. Murray Gell-Mann and Kazuhiko Nishijima explained this with strangeness. It is conserved by the strong interaction, so strange particles are made in pairs, as in π⁻ + p → K⁰ + Λ⁰, where S goes from 0 to +1 − 1 = 0. The lightest strange particles can decay only by changing S, which only the weak interaction does, so their decays are slow.

These rules turn particle physics into bookkeeping that can be checked. For any proposed reaction, add up charge, B, each L, and S on both sides. A strong or electromagnetic process that changes S is forbidden. A process that changes B or the total lepton number has never been observed, and experiments continue to search for one, because some theories beyond the Standard Model predict very rare violations.
