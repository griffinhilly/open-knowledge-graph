---
id: kirkendall-effect-and-interdiffusion
title: The Kirkendall Effect and Interdiffusion
domain: engineering
course: materials-science
prerequisites:
- id: diffusion-in-solids
  type: hard
- id: point-defects-vacancies-and-interstitials
  type: soft
tags:
- kirkendall-effect
- interdiffusion
- vacancy-flow
- marker-motion
stage: advanced
status: draft
---

# The Kirkendall Effect and Interdiffusion

## Core Idea
The Kirkendall effect demonstrates that net material transport occurs through vacancy movement, not atom exchange. When two different metals interdiffuse, inert marker particles at the original interface move relative to the growing intermetallic compound because of unequal diffusion rates. This vacancy flux creates voids on the side with faster diffusion.

## Questions

```yaml
- question: "In Kirkendall's 1947 experiment, inert molybdenum wire markers were placed at the copper-brass interface and the couple was annealed. After annealing, the markers had moved toward the brass. What does this marker motion reveal about the diffusion mechanism?"
  type: multiple-choice
  options:
    - "Copper diffuses faster than zinc, causing the copper side to swell and push the markers toward the brass"
    - "Zinc diffuses faster than copper; the brass side loses mass faster than it gains copper, causing the interface (and markers) to shift toward the brass"
    - "Both species diffuse at equal rates, and the marker motion is caused by thermal expansion of the brass"
    - "The markers moved because the annealing temperature caused partial melting of the brass near the interface"
  answer: 1
  explanation: "Zinc diffuses faster than copper in this system. The brass (zinc-rich) side loses zinc atoms faster than it receives copper atoms; the copper side gains zinc faster than it loses copper. The original interface — marked by the inert Mo wires — therefore moves toward the brass as the brass 'shrinks' and the copper 'swells.' The key insight is that if diffusion were by direct atom exchange (every A jump paired with a B jump), both sides would maintain equal flux and the markers would not move. Marker motion is direct evidence of unequal diffusivities and a vacancy-mediated mechanism."

- question: "In a copper-zinc diffusion couple where zinc diffuses faster, Kirkendall voids form preferentially on which side, and through what mechanism?"
  type: multiple-choice
  options:
    - "On the copper side, where copper atoms leave gaps as they diffuse toward the zinc"
    - "Equally on both sides, because diffusion always creates vacancies wherever atoms move"
    - "On the zinc-rich (brass) side, where the net outflow of zinc atoms creates excess vacancies that condense into voids"
    - "At the center of the diffusion zone, where the two fluxes collide and interfere"
  answer: 2
  explanation: "Each zinc atom jump into a vacancy displaces the vacancy in the opposite direction — the net vacancy flux is directed toward the zinc-rich side (opposite to the net zinc flux). This creates an excess of vacancies on the brass side. Above a supersaturation threshold, these vacancies condense into voids — just as excess interstitials can condense into dislocation loops. The copper side, receiving more atoms than it loses, has a vacancy deficit and no void formation. This asymmetry is the direct fingerprint of the vacancy mechanism: voids always form on the faster-diffusing side."

- question: "If two species in a diffusion couple had exactly equal intrinsic diffusivities (D_A = D_B), no Kirkendall marker displacement or void formation would be observed."
  type: true-false
  answer: true
  explanation: "True. The Kirkendall velocity v_K = (D_A − D_B)(∂x_A/∂x) is proportional to the diffusivity difference. When D_A = D_B, the Kirkendall velocity is zero everywhere — no net vacancy flux, no marker motion, no void formation. Each A jump is exactly matched by a B jump in the opposite direction, just as the discredited atom-exchange model predicted. The Kirkendall effect is specifically a consequence of *unequal* diffusivities, which only a vacancy mechanism can produce. This is why the observation of marker motion was decisive: it proved unequal fluxes, ruling out symmetric exchange."

- question: "Kirkendall voids form on the side of the diffusion couple where the slower-diffusing species originated."
  type: true-false
  answer: false
  explanation: "False — voids form on the faster-diffusing side. The faster species leaves its side more rapidly than the slower species arrives to fill the vacated sites. The net vacancy flux directed into the faster-diffusing side causes local supersaturation of vacancies, which condense into voids. In the classic copper-brass couple, zinc diffuses faster than copper, so voids form on the zinc-rich brass side. This counterintuitive result — voids form where atoms are *leaving*, not where they are *arriving* — is a direct consequence of the vacancy mechanism and is the source of reliability failures in Al-Au wire bonds and Cu-Sn solder joints."

- question: "Explain why the Kirkendall effect disproved the atom-exchange mechanism of diffusion and what it revealed about how atoms actually move in metals."
  type: short-answer
  answer: "The atom-exchange mechanism predicted that every A atom jumping to an adjacent site would be matched by a B atom jumping back — a perfect pairwise exchange. This would produce equal and opposite fluxes for both species, so no net mass transport would occur on either side of the couple, and inert markers would never move. Kirkendall's observation that the markers shifted toward the brass proved that zinc and copper were NOT moving at equal rates. One species (zinc) was crossing the interface faster than the other. The only known atomic mechanism consistent with unequal fluxes is the vacancy mechanism: atoms move by jumping into adjacent vacancies, and the rate depends on each species' jump frequency (activation energy and attempt frequency). Unequal jump rates produce a net vacancy flux and net matter flux, explaining both the marker motion and the void formation."
  explanation: "The Darken equations formalized this: the interdiffusion coefficient D̃ = x_A D_B + x_B D_A is a composition-weighted average of the individual intrinsic diffusivities D_A and D_B, which are generally unequal. The vacancy mechanism predicts exactly this structure. Direct atom exchange would require D_A = D_B everywhere, contradicting Kirkendall's measurements."
```

## Explainer

From Fick's laws, you know that atoms in a solid diffuse down their concentration gradient, driven by the reduction in chemical potential. But Fick's laws describe the net flux of each species without specifying the atomic mechanism. Before 1947, the dominant assumption was that diffusion in metals occurs by **direct atom exchange** — an A atom and a B atom simply swap positions. If this were true, A would diffuse as fast as B in a binary couple, since every A jump is matched by a B jump. The Kirkendall effect demolished this picture.

In 1947, Ernest Kirkendall placed inert molybdenum wire markers at the interface between copper and alpha-brass (a copper-zinc alloy) and annealed the couple at 785°C for hundreds of hours. If diffusion were atom exchange, the markers would stay put. Instead, they moved — toward the brass, into the side where zinc was originally concentrated. The interpretation: **zinc diffuses faster than copper**. Zinc atoms are leaving the brass side faster than copper atoms are arriving. The brass shrinks, the copper swells, and the original interface (marked by the Mo wires) migrates with the brass.

The mechanism is the **vacancy mechanism**, which your study of point defects introduced. Each time a zinc atom jumps into a neighboring vacancy, the vacancy jumps in the opposite direction. With zinc hopping faster than copper, there are more zinc-vacancy jumps per second than copper-vacancy jumps. The net vacancy flux is therefore directed toward the brass (opposite to the net zinc flux). This unequal flux creates excess vacancies on the zinc-rich side and a vacancy deficit on the copper-rich side. The excess vacancies on the brass side condense into **Kirkendall voids** — microscopic pores that grow at or near the original interface. These voids are a serious failure mode in microelectronics: aluminum-gold wire bonds and copper-tin solder joints develop voids by this mechanism under thermal cycling, eventually causing electrical failures.

Quantitatively, the **Darken equations** describe interdiffusion when the two species have unequal intrinsic diffusivities D_A and D_B. The **interdiffusion coefficient** is D̃ = x_A D_B + x_B D_A, a composition-weighted average that governs the concentration profiles observable by composition measurements. The lattice velocity (the Kirkendall velocity, giving the shift of the marker plane) is v_K = (D_A − D_B)(∂x_A/∂x), proportional to the diffusivity difference and the local composition gradient. Where the gradient is steepest and the diffusivity difference is largest, the markers move fastest. The Kirkendall effect thus turned what was a puzzling experimental anomaly into a quantitative window into atomic mechanisms — and a lasting warning to designers of bonded dissimilar-metal joints.
