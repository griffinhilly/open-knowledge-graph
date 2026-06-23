---
id: diesel-cycle-compression-ignition
title: Diesel Cycle and Compression-Ignition Engines
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: otto-cycle-spark-ignition-engine
  type: hard
- id: otto-cycle-internal-combustion
  type: soft
tags:
- diesel-cycle
- compression-ignition
- engines
stage: formal-systems
status: validated
---

# Diesel Cycle and Compression-Ignition Engines

## Core Idea
The Diesel cycle replaces constant-volume combustion with constant-pressure combustion (isobaric heat addition), allowing compression ignition without spark plugs. The Diesel cycle has lower thermal efficiency than the Otto cycle at the same compression ratio but achieves higher efficiency overall due to higher practical compression ratios. Analysis requires tracking the expansion ratio and cutoff ratio (the fraction of stroke at constant pressure)

## Questions

```yaml
- question: "An ideal Otto cycle and an ideal Diesel cycle both operate at a compression ratio of 14:1. The Diesel cycle has a cutoff ratio of 2. Which cycle has higher thermal efficiency?"
  type: multiple-choice
  options:
    - "The Diesel cycle — compression ignition is inherently more efficient than spark ignition"
    - "The Otto cycle — at the same compression ratio, constant-volume heat addition is thermodynamically superior to constant-pressure"
    - "They are equal — efficiency depends only on compression ratio, not the heat addition process"
    - "The Diesel cycle — because it operates at a higher temperature during combustion"
  answer: 1
  explanation: "At the same compression ratio, the Otto cycle efficiency η = 1 − 1/r^(γ−1) is higher than the Diesel cycle efficiency, which includes an extra bracket factor (r_c^γ − 1)/(γ(r_c − 1)) > 1. Constant-volume heat addition is more effective than constant-pressure: in the Diesel cycle, some energy goes into moving the piston during combustion rather than raising temperature. However, real diesel engines are more efficient overall because they operate at much higher compression ratios (14–22:1 vs. 8–12:1 for gasoline), more than compensating for the per-cycle disadvantage."

- question: "Why can diesel engines use much higher compression ratios than gasoline engines without the knocking problem?"
  type: multiple-choice
  options:
    - "Diesel fuel has a higher octane rating than gasoline, resisting autoignition"
    - "Diesel engines compress only air during the compression stroke, so there is no premixed fuel-air mixture to autoignite prematurely"
    - "Diesel engines use lower cylinder pressures because combustion is spread over a longer stroke"
    - "Diesel fuel is injected at lower pressure, preventing the energy concentrations that cause knock"
  answer: 1
  explanation: "In a diesel engine, only air is present during compression — fuel is injected directly at the top of the stroke. Autoignition of a premixed fuel-air charge (knock) cannot occur when there is no fuel present during compression. In a gasoline engine, the premixed charge can spontaneously ignite as compression ratio rises above ~12:1, causing knock. Diesel's compression-ignition design intentionally uses the high temperature from compression to ignite injected fuel, so knocking is not a constraint. This allows compression ratios of 14–22:1, which is the key to diesel engines' superior real-world efficiency."

- question: "The Diesel cycle is more thermodynamically efficient than the Otto cycle at the same compression ratio because constant-pressure combustion is inherently a superior heat addition process."
  type: true-false
  answer: false
  explanation: "This is the central misconception about diesel engine efficiency. At the same compression ratio, the Otto cycle (constant-volume heat addition) is actually MORE efficient than the Diesel cycle. Constant-volume addition raises temperature most effectively for a given heat input; constant-pressure addition diverts some energy into moving the piston rather than raising working gas temperature. Diesel engines achieve higher practical efficiency than gasoline engines not because of any per-cycle advantage, but because they can operate at much higher compression ratios — which dramatically increases efficiency for both cycle types, and diesel engines can reach compression ratios that gasoline engines cannot."

- question: "In the Diesel cycle, the cutoff ratio r_c = V₃/V₂ represents the fraction of the power stroke over which heat is added at constant pressure, and increasing r_c (more fuel burned at constant pressure) reduces thermal efficiency."
  type: true-false
  answer: true
  explanation: "The thermal efficiency formula η = 1 − (1/r_v^(γ−1)) · [(r_c^γ − 1)/(γ(r_c − 1))] shows that the bracket factor increases with r_c. Since the bracket is always > 1 (it represents the efficiency penalty for constant-pressure vs. constant-volume addition), a larger r_c means more heat is added in the less-efficient isobaric process, reducing overall efficiency. This is why diesel engines operate with small cutoff ratios (injecting just enough fuel for the desired load) — maximum efficiency corresponds to r_c → 1, which approaches the Otto cycle limit."

- question: "Explain why it seems paradoxical that the Diesel cycle is less efficient than the Otto cycle at the same compression ratio, yet diesel engines typically achieve higher thermal efficiency than gasoline engines in practice."
  type: short-answer
  answer: "At the same compression ratio, constant-volume heat addition (Otto) is thermodynamically superior to constant-pressure heat addition (Diesel) — the bracket term in the Diesel efficiency formula is always greater than 1, penalizing the isobaric process. However, gasoline engines are limited to compression ratios of about 8–12:1 because the pre-mixed fuel-air charge autoignites (knocks) at higher compression. Diesel engines compress only air, so fuel cannot knock during compression. They can therefore operate at 14–22:1, where the enormous efficiency gain from higher compression ratio far outweighs the per-cycle disadvantage of constant-pressure combustion."
  explanation: "This apparent paradox dissolves when you recognize that the comparison must be made at realistic operating compression ratios, not at the same theoretical compression ratio. Comparing a gasoline engine at r_v = 10 to a diesel engine at r_v = 18, the diesel wins decisively on efficiency even though it uses the less efficient heat addition mode. The lesson is that compression ratio is the dominant variable in thermal efficiency, and the choice of combustion mode is really a constraint on what compression ratios are achievable."
```

## Explainer

You already know the Otto cycle from your prerequisite: it compresses air-fuel mixture, ignites it (adding heat at constant volume), expands the hot gas to do work, and exhausts the products. The Diesel cycle keeps the same four-stroke structure but changes one critical process. Instead of adding heat at constant volume (an explosive pressure spike), it adds heat at **constant pressure** while the piston continues to move outward. This is the isobaric heat addition that defines the Diesel cycle, and it changes both the combustion mechanism and the efficiency analysis.

The physical motivation is **compression ignition**. In the Diesel cycle, only air is compressed during the compression stroke — no fuel is present. The compression ratio is much higher than in an Otto engine, typically 14:1 to 22:1 versus 8:1 to 12:1 for gasoline engines. Compressing air to this ratio raises its temperature to around 700–900°C, well above the autoignition temperature of diesel fuel. Fuel is then injected directly into the hot compressed air and ignites spontaneously — no spark plug required. Because the fuel is injected gradually and burns as it enters the cylinder, combustion occurs at roughly constant pressure as the piston moves. This is the **cutoff ratio** r_c = V₃/V₂ (the volume at the end of heat addition divided by the volume at the start) — it quantifies what fraction of the stroke combustion occupies.

The thermal efficiency of the ideal Diesel cycle is η = 1 − (1/r_v^(γ-1)) · [(r_c^γ − 1)/(γ(r_c − 1))], where r_v is the volumetric compression ratio. Comparing to the Otto efficiency η_Otto = 1 − 1/r_v^(γ-1), you can see the Diesel efficiency includes an extra factor in brackets. That factor is always greater than 1 (since r_c > 1), so at the *same compression ratio*, the Diesel cycle is less efficient than the Otto cycle. Intuitively, heat addition at constant pressure instead of constant volume means some of the added energy is used to push the piston rather than raise temperature — a less effective heat addition. However, the much higher compression ratio achievable in Diesel engines (because there's no pre-mixed fuel to cause knocking) more than compensates. In practice, diesel engines achieve higher thermal efficiencies than gasoline engines precisely because they operate at higher r_v.

Analyzing a Diesel cycle problem follows the same state-by-state approach you used for the Otto cycle: identify the four states (bottom and top of compression, end of heat addition, end of expansion), apply the isentropic relations for the adiabatic processes (1→2 and 3→4), use the isobaric heat addition condition for process 2→3 (P constant, so T₃/T₂ = V₃/V₂ = r_c), and use the isochoric heat rejection for process 4→1. Once temperatures at all four states are known, net work and heat input follow directly, and efficiency is their ratio. The two key cycle parameters — volumetric compression ratio and cutoff ratio — completely determine the ideal Diesel cycle's performance.
