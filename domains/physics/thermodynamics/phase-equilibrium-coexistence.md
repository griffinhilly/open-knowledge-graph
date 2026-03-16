---
id: phase-equilibrium-coexistence
title: Phase Equilibrium and Coexistence Conditions
domain: physics
course: thermodynamics
prerequisites:
- id: phase-transitions
  type: hard
- id: chemical-potential
  type: hard
builds-toward:
- clausius-clapeyron-equation
tags:
- phase-transitions
- equilibrium
- chemical-potential
stage: formal-systems
status: draft
---

# Phase Equilibrium and Coexistence Conditions

## Core Idea
At equilibrium, different phases (solid, liquid, gas) coexist when their chemical potentials are equal: μ_solid = μ_liquid = μ_gas. The Clausius-Clapeyron equation dP/dT = L/(T·ΔV) relates the slope of phase boundaries to the latent heat L and volume change ΔV. The phase diagram (P-T plot) summarizes all equilibrium conditions and is essential for understanding when substances exist in different phases and the conditions for transitions.

## How It's Best Learned
Use Clausius-Clapeyron to predict phase boundary slopes. Compare theory with experimental phase diagrams. Identify triple and critical points.

## Common Misconceptions
- Confusing phase equilibrium with thermodynamic equilibrium (phase equilibrium is a special case).
- Assuming latent heat is constant over all temperatures (it weakly depends on T).
- Thinking the Clausius-Clapeyron equation is valid far from phase boundaries.

## Explainer

From your study of chemical potential, you know that μ = (∂G/∂N)_{T,P} — it is the free energy cost of adding one particle to the system. At equilibrium, μ is uniform throughout the system: any inhomogeneity in μ drives a particle current to equalize it, just as a temperature gradient drives heat flow and a pressure gradient drives mechanical flow. When two phases coexist (ice and water in the same cup), they must satisfy all three equilibrium conditions simultaneously: T_solid = T_liquid, P_solid = P_liquid, and μ_solid(T,P) = μ_liquid(T,P). The last condition is the one that determines where in the (T,P) plane coexistence is possible.

The **Clausius-Clapeyron equation** dP/dT = L/(TΔV) tells you the slope of the phase boundary in the P-T diagram. Its derivation follows directly from the coexistence condition: if you shift T slightly along the phase boundary, P must shift to maintain μ_α = μ_β. Using dμ = −sdT + vdP (where s and v are entropy and volume per particle), the condition dμ_α = dμ_β gives −s_α dT + v_α dP = −s_β dT + v_β dP, rearranging to dP/dT = (s_β − s_α)/(v_β − v_α) = ΔS/ΔV = L/(TΔV), where L = TΔS is the **latent heat**. Notice what this tells you qualitatively: the slope of the phase boundary is large when ΔV is small (as for solid-liquid water, which is nearly incompressible), and it is positive unless ΔV is negative. Water is anomalous: ice is less dense than liquid water (ΔV < 0 on melting), so its solid-liquid boundary has a negative slope — increased pressure lowers the melting point. This is why ice skating is possible.

The **phase diagram** (P-T plot) organizes this information. The liquid-gas boundary ends at the **critical point** (Tc, Pc) where the distinction between liquid and gas vanishes — the latent heat goes to zero and ΔV → 0. Above the critical point, you can continuously convert liquid to gas without crossing a phase boundary. The solid-liquid boundary typically extends without a critical point (it is very hard to continuously convert solid to liquid). The solid, liquid, and gas regions meet at the **triple point**, the unique (T,P) combination where all three phases coexist simultaneously. For water, the triple point is at 273.16 K and 611.7 Pa — it defines the kelvin on the International Temperature Scale.

A practical skill from this topic: given a phase diagram, you can immediately determine the direction of phase change in response to any (T,P) perturbation. Decreasing pressure below the vapor pressure at fixed T → liquid boils (or solid sublimes). Increasing pressure at fixed T along the solid-liquid boundary of water → ice melts. These are not memorization tasks — they follow from asking "which phase has lower μ at the new (T,P)?" The phase with lower chemical potential is always thermodynamically favored, and the phase diagram is a map of which phase wins where.
