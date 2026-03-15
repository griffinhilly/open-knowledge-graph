---
id: michaelis-menten-enzyme-kinetics
title: Michaelis-Menten Kinetics and Enzyme Catalysis
domain: chemistry
course: physical-chemistry
prerequisites:
- id: rate-law-determination
  type: hard
- id: integrated-rate-laws
  type: hard
- id: first-order-linear-odes
  type: soft
builds-toward:
- autocatalytic-reactions-mechanisms
tags:
- enzyme
- michaelis-menten
- catalysis
- kinetics
stage: advanced
status: draft
---

# Michaelis-Menten Kinetics and Enzyme Catalysis

## Core Idea
Enzyme catalysis follows Michaelis-Menten kinetics: v = Vmₐₓ[S]/(Kₘ + [S]) where Vmₐₓ is maximum velocity and Kₘ is the Michaelis constant. At low substrate concentration ([S] << Kₘ), the reaction is first-order; at high [S], it becomes zero-order as enzyme becomes saturated. Kₘ reflects the enzyme-substrate affinity; Vmₐₓ depends on enzyme concentration. This kinetic behavior explains how enzymes efficiently catalyze biochemical reactions.

## How It's Best Learned
Plot velocity vs substrate concentration (hyperbolic curve); extract Vmₐₓ and Kₘ from Lineweaver-Burk plot (1/v vs 1/[S]). Design experiments to measure substrate kinetics. Examine how inhibitors shift these parameters.

## Common Misconceptions
- Kₘ always equals the dissociation constant Kd (only true when product release is fast compared to catalysis).
- Lower Kₘ always means better enzyme (depends on [S] in vivo; Vmₐₓ/Kₘ is the better efficiency metric).
