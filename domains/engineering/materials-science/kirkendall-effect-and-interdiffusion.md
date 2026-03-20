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

## Explainer

From Fick's laws, you know that atoms in a solid diffuse down their concentration gradient, driven by the reduction in chemical potential. But Fick's laws describe the net flux of each species without specifying the atomic mechanism. Before 1947, the dominant assumption was that diffusion in metals occurs by **direct atom exchange** — an A atom and a B atom simply swap positions. If this were true, A would diffuse as fast as B in a binary couple, since every A jump is matched by a B jump. The Kirkendall effect demolished this picture.

In 1947, Ernest Kirkendall placed inert molybdenum wire markers at the interface between copper and alpha-brass (a copper-zinc alloy) and annealed the couple at 785°C for hundreds of hours. If diffusion were atom exchange, the markers would stay put. Instead, they moved — toward the brass, into the side where zinc was originally concentrated. The interpretation: **zinc diffuses faster than copper**. Zinc atoms are leaving the brass side faster than copper atoms are arriving. The brass shrinks, the copper swells, and the original interface (marked by the Mo wires) migrates with the brass.

The mechanism is the **vacancy mechanism**, which your study of point defects introduced. Each time a zinc atom jumps into a neighboring vacancy, the vacancy jumps in the opposite direction. With zinc hopping faster than copper, there are more zinc-vacancy jumps per second than copper-vacancy jumps. The net vacancy flux is therefore directed toward the brass (opposite to the net zinc flux). This unequal flux creates excess vacancies on the zinc-rich side and a vacancy deficit on the copper-rich side. The excess vacancies on the brass side condense into **Kirkendall voids** — microscopic pores that grow at or near the original interface. These voids are a serious failure mode in microelectronics: aluminum-gold wire bonds and copper-tin solder joints develop voids by this mechanism under thermal cycling, eventually causing electrical failures.

Quantitatively, the **Darken equations** describe interdiffusion when the two species have unequal intrinsic diffusivities D_A and D_B. The **interdiffusion coefficient** is D̃ = x_A D_B + x_B D_A, a composition-weighted average that governs the concentration profiles observable by composition measurements. The lattice velocity (the Kirkendall velocity, giving the shift of the marker plane) is v_K = (D_A − D_B)(∂x_A/∂x), proportional to the diffusivity difference and the local composition gradient. Where the gradient is steepest and the diffusivity difference is largest, the markers move fastest. The Kirkendall effect thus turned what was a puzzling experimental anomaly into a quantitative window into atomic mechanisms — and a lasting warning to designers of bonded dissimilar-metal joints.
