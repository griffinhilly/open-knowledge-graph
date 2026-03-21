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

## Questions

```yaml
- question: "Two walls of equal thickness separate the same indoor and outdoor temperatures. Wall A is made of copper (k ≈ 400 W/m·K) and wall B is made of foam insulation (k ≈ 0.04 W/m·K). Assuming equal cross-sectional area, the heat flow rate through wall A is approximately:"
  type: multiple-choice
  options:
    - "The same as wall B, since both walls have the same thickness and temperature difference"
    - "Lower than wall B, because copper's high conductivity means it reaches thermal equilibrium faster and then stops conducting"
    - "About 10,000 times higher than wall B, because k appears directly in the numerator of Fourier's law"
    - "Lower than wall B, because denser materials create more thermal resistance"
  answer: 2
  explanation: "Fourier's law states Q̇ = kA(ΔT/L). With equal A, ΔT, and L, the heat flow is directly proportional to k. Copper's k ≈ 400 W/(m·K) versus foam's k ≈ 0.04 W/(m·K) gives a ratio of about 10,000. This is why metals are terrible insulators and air-trapping foams are excellent ones — the thermal conductivity alone determines conductive heat flow when geometry and temperature difference are fixed. The common misconception (option B) confuses dynamic equilibration with steady-state flow: once a steady temperature gradient is established, conduction is continuous, not a one-time event."

- question: "A builder doubles the thickness of a wall's insulation layer while keeping everything else the same. According to the thermal resistance analogy, the heat flow rate through the wall will:"
  type: multiple-choice
  options:
    - "Double, because there is now twice as much insulating material absorbing heat"
    - "Remain the same, since the temperature difference driving heat flow hasn't changed"
    - "Halve, because the thermal resistance R_th = L/(kA) doubles when L doubles"
    - "Decrease by a fixed amount equal to the original heat flow through one layer"
  answer: 2
  explanation: "Thermal resistance R_th = L/(kA). Doubling L doubles R_th. Since Q̇ = ΔT/R_th, doubling R_th halves Q̇ for the same ΔT. This is the direct analogue of Ohm's law: doubling resistance halves current for the same voltage. The R-value system used to rate building insulation is precisely this thermal resistance — an R-19 wall has half the heat flow per unit area of an R-9.5 wall at the same indoor-outdoor temperature difference. Option B is the most tempting wrong answer: a larger temperature difference does drive more heat flow, but the temperature difference hasn't changed here — only the resistance has."

- question: "The negative sign in Fourier's law (Q̇ = −kA dT/dx) indicates that heat flows in the direction of increasing temperature."
  type: true-false
  answer: false
  explanation: "The negative sign encodes the physical direction of heat flow: heat moves from hot to cold, i.e., in the direction of decreasing temperature. If temperature decreases in the +x direction (dT/dx < 0), the negative sign makes Q̇ positive — heat flows in the +x direction, consistent with flowing from the hotter side to the cooler side. Without the negative sign, the formula would predict heat flowing uphill in temperature, which violates the second law of thermodynamics. The sign is not a mathematical convention — it encodes a physical law."

- question: "Wet clothing feels colder than dry clothing at the same air temperature primarily because water has much higher thermal conductivity than air, so it conducts heat away from the body more rapidly."
  type: true-false
  answer: true
  explanation: "This is a direct application of Fourier's law. Dry clothing traps air (k ≈ 0.025 W/(m·K)) next to the skin, severely limiting conductive heat loss. Water (k ≈ 0.6 W/(m·K)) is about 24 times more thermally conductive than air. When clothing is wet, the insulating air layer is replaced by conducting water, dramatically increasing the heat flow rate from your skin. The temperature difference (skin temperature minus environment) is the same, but the increased k of water multiplies the heat loss rate proportionally — which is why wet conditions are so much more dangerous for hypothermia than dry conditions at the same temperature."

- question: "Why is the thermal resistance analogy (R_th = L/kA) useful for analyzing heat flow through composite walls, and what does a higher R-value mean physically for a building material?"
  type: short-answer
  answer: "The thermal resistance analogy maps Fourier's law onto Ohm's law: temperature difference drives heat flow through a resistance, exactly as voltage drives current through electrical resistance. For composite walls (plaster + insulation + brick), thermal resistances in series add directly — R_total = R_1 + R_2 + R_3 — making multi-layer analysis as simple as adding resistors. A higher R-value means greater thermal resistance: less heat flows per degree of temperature difference per unit area. Doubling R-value halves heat loss for the same indoor-outdoor temperature difference."
  explanation: "The power of the analogy is that it converts integral calculus (Fourier's full equation) into simple arithmetic for engineers designing walls and windows. An R-value is not a material property alone — it includes thickness: R_th = L/(kA). Adding more insulation increases R linearly with thickness, while switching to a lower-k material also increases R. Building codes specify minimum R-values for walls, roofs, and floors because these are the quantities that directly determine heating and cooling energy demand. The analogy also clarifies why adding insulation has diminishing returns: the first inch of insulation reduces heat flow far more than the tenth inch, because the total R grows but the marginal reduction in Q̇ = ΔT/R_th decreases as R grows large."
```

## Explainer

You know from calculus that a derivative measures the rate of change of a quantity in space. Fourier's law says that heat flows in response to a **temperature gradient** — a spatial variation in temperature — and the bigger the gradient, the faster the flow. Written as Q̇ = −kA(dT/dx), each piece has a physical role: Q̇ is the rate of heat transfer (watts), A is the cross-sectional area through which heat flows, dT/dx is the temperature gradient (degrees per meter), and k is the **thermal conductivity** — a material constant with units W/(m·K). The negative sign ensures heat flows from hot to cold: if temperature decreases in the +x direction (dT/dx < 0), then Q̇ is positive, meaning heat flows in the +x direction, down the gradient.

The analogy to electrical circuits is powerful and exact. Ohm's law says current I = ΔV/R — voltage difference drives current through a resistance. Fourier's law says Q̇ = ΔT/R_th, where the **thermal resistance** R_th = L/(kA) (length divided by conductivity times area). Just as electrical resistors in series add their resistances, slabs of material in series add their thermal resistances. A wall made of plaster, insulation, and brick has total R_th = L₁/(k₁A) + L₂/(k₂A) + L₃/(k₃A). This is why building insulation is characterized by **R-values** — they are thermal resistances, and higher R means less heat flow per degree of temperature difference.

The thermal conductivity k varies enormously across materials. Metals like copper have k ≈ 400 W/(m·K) — their free electrons carry both electrical current and heat efficiently. Still air has k ≈ 0.025 W/(m·K), about 16,000 times less. This is why air gaps and porous foams are excellent insulators: they trap air, preventing convection and limiting conduction to the sluggish gas molecules. Water at k ≈ 0.6 W/(m·K) is intermediate — much better than air but far worse than metal, which is why wet clothing feels cold (it replaces the insulating air layer with conducting water). Comparing k values explains everyday thermal phenomena directly.

Fourier's law in one dimension is the steady-state case. In the time-dependent case — for instance, how quickly a metal rod equilibrates after one end is heated — the same physics gives the **heat equation**: ∂T/∂t = α ∇²T, where α = k/(ρc_p) is the **thermal diffusivity** (ρ is density, c_p is specific heat). This partial differential equation says that the temperature at a point changes in time in proportion to its spatial curvature. A flat temperature profile (∇²T = 0) does not evolve — it is already in steady state. Peaks and troughs smooth out over time, with the timescale set by α and the length scale of the temperature variation. The heat equation is the same in structure as the diffusion equation, connecting thermal conduction directly to diffusive transport more broadly.


