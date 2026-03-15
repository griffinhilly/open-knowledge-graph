---
id: diffusion-in-solids
title: Diffusion in Solids
domain: engineering
course: materials-science
prerequisites:
- id: crystal-defects
  type: hard
- id: diffusion-and-ficks-laws
  type: hard
- id: arrhenius-equation
  type: soft
- id: partial-derivatives
  type: soft
- id: differential-equations-intro
  type: soft
builds-toward:
- heat-treatment-of-steels
- sintering-and-powder-processing
tags:
- diffusion
- ficks-law
- vacancy-mechanism
- carburization
stage: formal-systems
status: validated
---

# Diffusion in Solids

## Core Idea
Diffusion in solids is the thermally activated migration of atoms through a crystal lattice, primarily via vacancy exchange or interstitial hopping. Fick's first law relates steady-state flux to a concentration gradient; Fick's second law describes time-dependent concentration profiles. The diffusivity D follows an Arrhenius relationship D = D₀ exp(−Qd/RT), where Qd is the activation energy for diffusion. Engineering processes such as carburization (adding carbon to steel surfaces) and dopant diffusion in semiconductors are directly governed by these principles.

## How It's Best Learned
Solve Fick's second law for the semi-infinite solid boundary condition (using the complementary error function solution) applied to carburization problems. Plot concentration vs. depth at different times to build intuition.

## Common Misconceptions
- Interstitial diffusion (e.g., carbon in iron) is much faster than substitutional diffusion because interstitials don't require a vacancy.
- Higher temperature dramatically accelerates diffusion; even a 50°C difference can change diffusivity by an order of magnitude.
