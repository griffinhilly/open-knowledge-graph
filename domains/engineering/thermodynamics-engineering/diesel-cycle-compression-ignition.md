---
id: diesel-cycle-compression-ignition
title: Diesel Cycle and Compression-Ignition Engines
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: otto-cycle-spark-ignition-engine
  type: hard
tags:
- diesel-cycle
- compression-ignition
- engines
stage: advanced
status: draft
---

# Diesel Cycle and Compression-Ignition Engines

## Core Idea
The Diesel cycle replaces constant-volume combustion with constant-pressure combustion (isobaric heat addition), allowing compression ignition without spark plugs. The Diesel cycle has lower thermal efficiency than the Otto cycle at the same compression ratio but achieves higher efficiency overall due to higher practical compression ratios. Analysis requires tracking the expansion ratio and cutoff ratio (the fraction of stroke at constant pressure)

## Explainer

You already know the Otto cycle from your prerequisite: it compresses air-fuel mixture, ignites it (adding heat at constant volume), expands the hot gas to do work, and exhausts the products. The Diesel cycle keeps the same four-stroke structure but changes one critical process. Instead of adding heat at constant volume (an explosive pressure spike), it adds heat at **constant pressure** while the piston continues to move outward. This is the isobaric heat addition that defines the Diesel cycle, and it changes both the combustion mechanism and the efficiency analysis.

The physical motivation is **compression ignition**. In the Diesel cycle, only air is compressed during the compression stroke — no fuel is present. The compression ratio is much higher than in an Otto engine, typically 14:1 to 22:1 versus 8:1 to 12:1 for gasoline engines. Compressing air to this ratio raises its temperature to around 700–900°C, well above the autoignition temperature of diesel fuel. Fuel is then injected directly into the hot compressed air and ignites spontaneously — no spark plug required. Because the fuel is injected gradually and burns as it enters the cylinder, combustion occurs at roughly constant pressure as the piston moves. This is the **cutoff ratio** r_c = V₃/V₂ (the volume at the end of heat addition divided by the volume at the start) — it quantifies what fraction of the stroke combustion occupies.

The thermal efficiency of the ideal Diesel cycle is η = 1 − (1/r_v^(γ-1)) · [(r_c^γ − 1)/(γ(r_c − 1))], where r_v is the volumetric compression ratio. Comparing to the Otto efficiency η_Otto = 1 − 1/r_v^(γ-1), you can see the Diesel efficiency includes an extra factor in brackets. That factor is always greater than 1 (since r_c > 1), so at the *same compression ratio*, the Diesel cycle is less efficient than the Otto cycle. Intuitively, heat addition at constant pressure instead of constant volume means some of the added energy is used to push the piston rather than raise temperature — a less effective heat addition. However, the much higher compression ratio achievable in Diesel engines (because there's no pre-mixed fuel to cause knocking) more than compensates. In practice, diesel engines achieve higher thermal efficiencies than gasoline engines precisely because they operate at higher r_v.

Analyzing a Diesel cycle problem follows the same state-by-state approach you used for the Otto cycle: identify the four states (bottom and top of compression, end of heat addition, end of expansion), apply the isentropic relations for the adiabatic processes (1→2 and 3→4), use the isobaric heat addition condition for process 2→3 (P constant, so T₃/T₂ = V₃/V₂ = r_c), and use the isochoric heat rejection for process 4→1. Once temperatures at all four states are known, net work and heat input follow directly, and efficiency is their ratio. The two key cycle parameters — volumetric compression ratio and cutoff ratio — completely determine the ideal Diesel cycle's performance.
