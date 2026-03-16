---
id: heat-transfer-conduction-fourier
title: Thermal Conduction and Fourier's Law
domain: physics
course: thermodynamics
prerequisites:
- id: derivatives
  type: soft
tags:
- heat-transfer
- conduction
- temperature-gradient
stage: formal-systems
status: draft
---

# Thermal Conduction and Fourier's Law

## Core Idea
Fourier's law states that the heat flow rate through a material is proportional to the temperature gradient and the cross-sectional area, inversely proportional to thickness: Q̇ = −kA(dT/dx). The constant k (thermal conductivity) is a material property indicating how readily heat diffuses through it.

## Explainer

You know from calculus that a derivative measures the rate of change of a quantity in space. Fourier's law says that heat flows in response to a **temperature gradient** — a spatial variation in temperature — and the bigger the gradient, the faster the flow. Written as Q̇ = −kA(dT/dx), each piece has a physical role: Q̇ is the rate of heat transfer (watts), A is the cross-sectional area through which heat flows, dT/dx is the temperature gradient (degrees per meter), and k is the **thermal conductivity** — a material constant with units W/(m·K). The negative sign ensures heat flows from hot to cold: if temperature decreases in the +x direction (dT/dx < 0), then Q̇ is positive, meaning heat flows in the +x direction, down the gradient.

The analogy to electrical circuits is powerful and exact. Ohm's law says current I = ΔV/R — voltage difference drives current through a resistance. Fourier's law says Q̇ = ΔT/R_th, where the **thermal resistance** R_th = L/(kA) (length divided by conductivity times area). Just as electrical resistors in series add their resistances, slabs of material in series add their thermal resistances. A wall made of plaster, insulation, and brick has total R_th = L₁/(k₁A) + L₂/(k₂A) + L₃/(k₃A). This is why building insulation is characterized by **R-values** — they are thermal resistances, and higher R means less heat flow per degree of temperature difference.

The thermal conductivity k varies enormously across materials. Metals like copper have k ≈ 400 W/(m·K) — their free electrons carry both electrical current and heat efficiently. Still air has k ≈ 0.025 W/(m·K), about 16,000 times less. This is why air gaps and porous foams are excellent insulators: they trap air, preventing convection and limiting conduction to the sluggish gas molecules. Water at k ≈ 0.6 W/(m·K) is intermediate — much better than air but far worse than metal, which is why wet clothing feels cold (it replaces the insulating air layer with conducting water). Comparing k values explains everyday thermal phenomena directly.

Fourier's law in one dimension is the steady-state case. In the time-dependent case — for instance, how quickly a metal rod equilibrates after one end is heated — the same physics gives the **heat equation**: ∂T/∂t = α ∇²T, where α = k/(ρc_p) is the **thermal diffusivity** (ρ is density, c_p is specific heat). This partial differential equation says that the temperature at a point changes in time in proportion to its spatial curvature. A flat temperature profile (∇²T = 0) does not evolve — it is already in steady state. Peaks and troughs smooth out over time, with the timescale set by α and the length scale of the temperature variation. The heat equation is the same in structure as the diffusion equation, connecting thermal conduction directly to diffusive transport more broadly.


