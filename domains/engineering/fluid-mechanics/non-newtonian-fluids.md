---
id: non-newtonian-fluids
title: Non-Newtonian Fluids
domain: engineering
course: fluid-mechanics
prerequisites:
- id: viscosity-and-newtonian-fluids
  type: hard
tags:
- non-Newtonian
- shear thinning
- shear thickening
- Bingham plastic
- viscoelastic
- rheology
- power-law fluid
stage: formal-systems
status: draft
---
# Non-Newtonian Fluids

## Core Idea
Non-Newtonian fluids are those whose shear stress is not linearly proportional to the strain rate — their apparent viscosity varies with shear rate, time, or flow history. The most common models are: shear-thinning (pseudoplastic) fluids like blood, paint, and polymer solutions, where viscosity decreases with increasing shear rate (modeled by the power-law τ = Kγ̇ⁿ with n < 1); shear-thickening (dilatant) fluids like cornstarch suspensions, where viscosity increases with shear rate (n > 1); and Bingham plastics like toothpaste and drilling mud, which behave as solids below a yield stress τ_y and flow as viscous fluids above it (τ = τ_y + μ_p·γ̇). Viscoelastic fluids (like polymer melts) exhibit both viscous and elastic behavior — they can store energy and exhibit phenomena like die swell, rod climbing (Weissenberg effect), and elastic recoil. Rheometry — controlled shear and extensional testing — is used to characterize these complex behaviors.

## How It's Best Learned
Derive the velocity profile for a power-law fluid in a pipe (it changes from parabolic to blunted for n < 1 and pointed for n > 1) and compare it to the Newtonian parabolic profile. Sketch the shear stress vs. strain rate curves for Newtonian, shear-thinning, shear-thickening, and Bingham plastic fluids on the same axes. Study real examples: why does ketchup flow easily when shaken (thixotropy), why does paint stay on a wall after brushing (shear-thinning with recovery), and why does a polymer solution climb a rotating rod (normal stress differences).

## Common Misconceptions
- Shear-thinning and thixotropy are not the same. Shear-thinning is an instantaneous decrease of viscosity with shear rate; thixotropy is a time-dependent decrease at constant shear rate (the fluid's structure gradually breaks down). Many real fluids exhibit both.
- The power-law model τ = Kγ̇ⁿ fails at very low and very high shear rates, where real shear-thinning fluids approach constant Newtonian plateaus (zero-shear viscosity η₀ and infinite-shear viscosity η∞). The Carreau or Cross models capture these limits.
- Yield stress is a practical concept, not always a sharp physical threshold. Whether a material has a "true" yield stress or simply a very high viscosity at low shear rates is debated (the "yield stress myth" controversy), but the Bingham model remains a useful engineering approximation.
