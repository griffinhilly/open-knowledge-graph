---
id: michaelis-menten-enzyme-kinetics-physical-chemistry
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

## Explainer

You already understand rate laws and how to determine reaction order from experimental data. Enzyme kinetics applies these tools to a specific and ubiquitous class of reactions: those catalyzed by biological macromolecules that bind their substrates before converting them to products. The Michaelis-Menten model captures this process with a minimal mechanism — enzyme (E) binds substrate (S) to form a complex (ES), which then either dissociates back or proceeds to product (P) and free enzyme: E + S ⇌ ES → E + P.

Applying the **steady-state approximation** to the intermediate ES — assuming it forms and breaks down at the same rate so its concentration stays roughly constant — yields the Michaelis-Menten equation: v = Vₘₐₓ[S]/(Kₘ + [S]). This equation has two parameters with clear physical meanings. **Vₘₐₓ** is the maximum rate when every enzyme molecule is occupied by substrate (full saturation), equal to k_cat × [E]_total, where k_cat is the catalytic rate constant (turnover number). **Kₘ**, the Michaelis constant, is the substrate concentration at which the rate is exactly half of Vₘₐₓ. It combines the rates of ES dissociation (back to E + S) and forward catalysis (to E + P) relative to the rate of ES formation: Kₘ = (k₋₁ + k_cat)/k₁.

The equation describes a **hyperbolic saturation curve** when you plot v against [S]. At low [S] (where [S] << Kₘ), the equation simplifies to v ≈ (Vₘₐₓ/Kₘ)[S] — the reaction is first-order in substrate, and increasing [S] proportionally increases the rate. At high [S] (where [S] >> Kₘ), v approaches Vₘₐₓ — the reaction becomes zero-order in substrate because all enzyme active sites are occupied. The transition between these regimes is smooth, and Kₘ marks the midpoint. This saturation behavior is the hallmark of enzyme catalysis and distinguishes it from simple bimolecular reactions that never saturate.

To extract Kₘ and Vₘₐₓ from experimental data, the **Lineweaver-Burk plot** (1/v vs 1/[S]) linearizes the Michaelis-Menten equation: 1/v = (Kₘ/Vₘₐₓ)(1/[S]) + 1/Vₘₐₓ. The y-intercept gives 1/Vₘₐₓ and the slope gives Kₘ/Vₘₐₓ. This linearization also reveals how inhibitors work: a **competitive inhibitor** (which competes with substrate for the active site) increases the apparent Kₘ without changing Vₘₐₓ, altering the slope but not the intercept. A **noncompetitive inhibitor** (which binds elsewhere and reduces catalytic efficiency) decreases Vₘₐₓ without changing Kₘ. The ratio Vₘₐₓ/Kₘ, called the **specificity constant**, is the best single measure of catalytic efficiency — it captures how well the enzyme performs at low substrate concentrations and has an upper limit set by the diffusion rate of enzyme-substrate encounter, around 10⁸–10⁹ M⁻¹s⁻¹ for the fastest "diffusion-limited" enzymes.
