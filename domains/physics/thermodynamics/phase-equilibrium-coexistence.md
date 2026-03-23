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
stage: advanced
status: validated
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

## Questions

```yaml
- question: "Two phases are in contact at the same temperature and pressure. What additional condition must be satisfied for them to coexist stably at equilibrium?"
  type: multiple-choice
  options:
    - "The two phases must have equal entropy per particle"
    - "The two phases must have equal chemical potential"
    - "The latent heat of the transition between them must be zero"
    - "The total Gibbs free energy of the system must equal zero"
  answer: 1
  explanation: "Thermodynamic equilibrium requires three conditions between coexisting phases: equal temperature (no heat flow), equal pressure (no mechanical work), and equal chemical potential (no particle transfer). Equal T and P are necessary but not sufficient — it is the chemical potential equality μ_α(T,P) = μ_β(T,P) that selects which (T,P) combinations allow coexistence. When μ differs between phases, particles migrate from the high-μ phase to the low-μ phase until equality is restored or one phase disappears. The phase diagram is a map of the (T,P) locus where these chemical potentials are equal."

- question: "A student says: 'I can tell which phase is stable at a given temperature and pressure by finding which phase has higher entropy — nature maximizes entropy.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "At fixed temperature and pressure, the stable phase is the one with lower Gibbs free energy (lower chemical potential per particle) — entropy maximization applies to isolated systems, not systems at fixed T and P"
    - "Entropy is completely irrelevant to phase stability"
    - "Nature always prefers the solid phase because it has the lowest entropy"
    - "Only temperature determines phase stability; pressure is irrelevant"
  answer: 0
  explanation: "The entropy maximization principle applies to isolated systems (fixed U, V, N). At fixed temperature and pressure — the typical experimental condition — the relevant criterion is minimization of the Gibbs free energy G = H − TS. The phase with lower G (equivalently, lower chemical potential μ = G/N) is thermodynamically stable. This correctly incorporates both energetic and entropic contributions: at high T, the entropy term −TS dominates and favors disordered phases (liquid, gas); at low T, the enthalpy H dominates and favors ordered phases (solid). Entropy alone would always favor the gas phase."

- question: "The solid-liquid phase boundary for water slopes negatively in the P-T diagram, meaning that applying pressure at constant temperature can cause ice to melt."
  type: true-false
  answer: true
  explanation: "The Clausius-Clapeyron equation gives dP/dT = L/(TΔV), where ΔV = V_liquid − V_solid. For water, ice is less dense than liquid water, so V_liquid < V_solid and ΔV < 0. With L > 0 (melting absorbs heat) and T > 0, the slope dP/dT is negative. This means the melting point decreases as pressure increases — apply enough pressure at a temperature just below 0°C and the ice will melt. This anomaly (water expanding on freezing) is rare among substances and has practical consequences including ice skating."

- question: "Above the critical point in a substance's phase diagram, there is still a phase boundary separating the liquid from the gas phase."
  type: true-false
  answer: false
  explanation: "Above the critical point (Tc, Pc), the distinction between liquid and gas disappears entirely. The latent heat goes to zero and the density difference ΔV → 0 as the critical point is approached. Above it, the substance exists as a supercritical fluid — a single phase that can be continuously converted from liquid-like to gas-like density without crossing any phase boundary. The liquid-gas boundary in the P-T diagram terminates at the critical point; it does not extend beyond it. This means you can take liquid water, heat it above Tc at high pressure, reduce pressure, and end up as steam — never crossing a phase boundary."

- question: "Why is equal chemical potential — rather than just equal temperature and pressure — the correct condition for phase coexistence, and how does this directly lead to the Clausius-Clapeyron equation?"
  type: short-answer
  answer: "Chemical potential μ is the free energy cost of adding one particle at fixed T and P. Any imbalance in μ between phases drives particle flow from the high-μ phase to the low-μ phase, just as a temperature difference drives heat flow. At equilibrium, T, P, and μ must all be equal between coexisting phases. The phase diagram traces the (T,P) locus where μ_α(T,P) = μ_β(T,P). The Clausius-Clapeyron equation follows directly: as T changes along this coexistence curve, P must adjust to maintain μ_α = μ_β. Using dμ = −s dT + v dP (from the Gibbs-Duhem relation), setting dμ_α = dμ_β gives (−s_α + v_α dP/dT) dT = (−s_β + v_β dP/dT) dT, which rearranges to dP/dT = (s_β − s_α)/(v_β − v_α) = ΔS/ΔV = L/(TΔV), where L = TΔS is the latent heat. The slope of every phase boundary is determined by the latent heat and the volume change at that transition."
```

## Explainer

From your study of chemical potential, you know that μ = (∂G/∂N)_{T,P} — it is the free energy cost of adding one particle to the system. At equilibrium, μ is uniform throughout the system: any inhomogeneity in μ drives a particle current to equalize it, just as a temperature gradient drives heat flow and a pressure gradient drives mechanical flow. When two phases coexist (ice and water in the same cup), they must satisfy all three equilibrium conditions simultaneously: T_solid = T_liquid, P_solid = P_liquid, and μ_solid(T,P) = μ_liquid(T,P). The last condition is the one that determines where in the (T,P) plane coexistence is possible.

The **Clausius-Clapeyron equation** dP/dT = L/(TΔV) tells you the slope of the phase boundary in the P-T diagram. Its derivation follows directly from the coexistence condition: if you shift T slightly along the phase boundary, P must shift to maintain μ_α = μ_β. Using dμ = −sdT + vdP (where s and v are entropy and volume per particle), the condition dμ_α = dμ_β gives −s_α dT + v_α dP = −s_β dT + v_β dP, rearranging to dP/dT = (s_β − s_α)/(v_β − v_α) = ΔS/ΔV = L/(TΔV), where L = TΔS is the **latent heat**. Notice what this tells you qualitatively: the slope of the phase boundary is large when ΔV is small (as for solid-liquid water, which is nearly incompressible), and it is positive unless ΔV is negative. Water is anomalous: ice is less dense than liquid water (ΔV < 0 on melting), so its solid-liquid boundary has a negative slope — increased pressure lowers the melting point. This is why ice skating is possible.

The **phase diagram** (P-T plot) organizes this information. The liquid-gas boundary ends at the **critical point** (Tc, Pc) where the distinction between liquid and gas vanishes — the latent heat goes to zero and ΔV → 0. Above the critical point, you can continuously convert liquid to gas without crossing a phase boundary. The solid-liquid boundary typically extends without a critical point (it is very hard to continuously convert solid to liquid). The solid, liquid, and gas regions meet at the **triple point**, the unique (T,P) combination where all three phases coexist simultaneously. For water, the triple point is at 273.16 K and 611.7 Pa — it defines the kelvin on the International Temperature Scale.

A practical skill from this topic: given a phase diagram, you can immediately determine the direction of phase change in response to any (T,P) perturbation. Decreasing pressure below the vapor pressure at fixed T → liquid boils (or solid sublimes). Increasing pressure at fixed T along the solid-liquid boundary of water → ice melts. These are not memorization tasks — they follow from asking "which phase has lower μ at the new (T,P)?" The phase with lower chemical potential is always thermodynamically favored, and the phase diagram is a map of which phase wins where.
