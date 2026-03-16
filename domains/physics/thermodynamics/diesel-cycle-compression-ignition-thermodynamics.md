---
id: diesel-cycle-compression-ignition-thermodynamics
title: The Diesel Cycle and Compression Ignition Engines
domain: physics
course: thermodynamics
prerequisites:
- id: otto-cycle-internal-combustion
  type: hard
- id: thermodynamic-processes
  type: soft
builds-toward:
- pv-diagram-interpretation
tags:
- cycles
- engines
- efficiency
stage: formal-systems
status: draft
---

# The Diesel Cycle and Compression Ignition Engines

## Core Idea
The Diesel cycle differs from the Otto cycle by having isobaric (constant-pressure) heat addition instead of constant-volume heat addition, reflecting the combustion process in diesel engines. The Diesel cycle efficiency is η = 1 - (1/r^(γ-1))[r_c^γ - 1]/[r_c - 1], where r is the compression ratio and r_c is the cutoff ratio; it is always lower than Otto cycle efficiency at the same compression ratio. Diesel engines achieve better fuel economy because they can operate at higher compression ratios than gasoline engines.

## How It's Best Learned
Compare Otto and Diesel cycles on the same P-V diagram. Calculate efficiency for typical compression ratios and cutoff ratios.

## Common Misconceptions
- Thinking Diesel efficiency is higher than Otto at the same compression ratio (it is actually lower).
- Confusing the cutoff ratio with other cycle parameters.
- Assuming constant-volume combustion (Otto) is more realistic than isobaric (Diesel).

## Explainer

From the Otto cycle, you know that an ideal gasoline engine operates on four strokes approximated by alternating adiabatic compressions/expansions and constant-volume heat additions/rejections. The efficiency of the Otto cycle depends only on the compression ratio r — and higher r means higher efficiency. Diesel engines also run on a four-stroke cycle, but they differ in one critical way: the fuel is not premixed with air. Instead, air alone is compressed so forcefully that it becomes hot enough to ignite the fuel when it is injected. This physical difference — no spark plug, just heat of compression — changes the thermodynamic model.

In the Diesel cycle, heat addition is modeled as an **isobaric (constant-pressure) process** rather than the Otto cycle's constant-volume process. Here is why: diesel fuel is injected gradually during part of the expansion stroke, not all at once. As the piston starts to move outward, burning fuel releases energy that maintains roughly constant pressure even as the volume increases. This continues until the fuel cutoff, after which the gas expands adiabatically as in the Otto cycle. The ratio of the volume at fuel cutoff to the volume at the start of injection is the **cutoff ratio** r_c. When r_c = 1 (instantaneous combustion), the Diesel cycle degenerates to the Otto cycle.

The efficiency formula η = 1 - (1/r^(γ-1)) × (r_c^γ - 1)/(γ(r_c - 1)) has a crucial feature: the bracketed factor is always greater than 1 for r_c > 1. This means the Diesel efficiency is always *lower* than an Otto cycle operating at the same compression ratio. This seems to contradict real-world observation — diesel engines are more fuel-efficient than gasoline engines. The resolution is that diesel engines operate at much higher compression ratios (typically 14–22:1, vs. 8–12:1 for gasoline) precisely because they are not limited by premature detonation ("knock"). Gasoline ignites spontaneously above a certain compression, but diesel fuel is specifically designed to ignite only when injected into hot compressed air. So the real-world comparison is not at the same compression ratio: diesel runs at a higher r, and even though its efficiency at that r is penalized by the r_c > 1 factor, the higher r more than compensates.

Plotting both cycles on a P-V diagram makes the difference vivid. The Otto cycle shows a vertical (constant-volume) line during heat addition — a spike in pressure. The Diesel cycle shows a horizontal (constant-pressure) line — the pressure stays fixed while volume increases as the piston moves. The area enclosed by each cycle on the P-V diagram equals the net work output. The Diesel cycle tends to enclose a different-shaped region, reflecting the different combustion process. Understanding these geometric differences — and how they translate into efficiency equations — is the heart of engineering thermodynamics applied to real engines.
