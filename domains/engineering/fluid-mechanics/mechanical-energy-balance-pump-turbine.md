---
id: mechanical-energy-balance-pump-turbine
title: Mechanical Energy Balance with Pump and Turbine Work
domain: engineering
course: fluid-mechanics
prerequisites:
- id: first-law-open-systems
  type: hard
- id: bernoulli-real-fluid-limitations
  type: hard
- id: mechanical-energy-head-forms
  type: soft
builds-toward:
- centrifugal-pump-curves-selection
- pipe-network-solutions-hardy-cross
tags:
- energy-equation
- pump-work
- turbine-work
- head
stage: formal-systems
status: validated
---
# Mechanical Energy Balance with Pump and Turbine Work

## Core Idea
The steady-flow mechanical energy equation (p₁/ρg + v₁²/2g + z₁ + H_pump = p₂/ρg + v₂²/2g + z₂ + H_turbine + H_loss) extends Bernoulli to include work interactions and irreversibilities. Pump head and turbine head represent useful work transfer; head loss represents energy dissipated as heat by viscous friction. This equation is the foundation for all piping system design.

## Questions

```yaml
- question: "A pump moves water from a lower tank to an elevated tank through a long pipe. After applying the mechanical energy equation, a student finds H_pump = 40 m but the elevation difference is only 30 m and velocity/pressure differences are negligible. What happened to the missing 10 m of head?"
  type: multiple-choice
  options:
    - "It was stored as potential energy in the pipe walls"
    - "It was dissipated as heat by viscous friction in the pipe (head loss)"
    - "It was converted to turbine work downstream"
    - "The pump under-performed; 10 m of head was never delivered to the fluid"
  answer: 1
  explanation: "The energy equation is a strict accounting statement: H_pump = Δz + H_turbine + H_loss. With no turbine and 30 m of elevation gain, the remaining 10 m must equal H_loss — energy permanently destroyed by viscous friction and converted to heat. Head loss always appears on the outlet side of the equation and can never be recovered."

- question: "A pump delivers Q = 0.05 m³/s against a pump head of H = 30 m. The pump's efficiency is η = 0.75. What shaft power must be supplied to the pump?"
  type: multiple-choice
  options:
    - "ρgQH = 14.7 kW — shaft power equals hydraulic power"
    - "ρgQH / η = 19.6 kW — shaft power is higher because energy is lost in the pump itself"
    - "η × ρgQH = 11.0 kW — shaft power is lower because the pump multiplies input power"
    - "ρg Q H η² = 8.3 kW — two efficiency factors apply, one for suction and one for discharge"
  answer: 1
  explanation: "The hydraulic power delivered to the fluid is P_hydraulic = ρgQH ≈ 14.7 kW. But because the pump is only 75% efficient, not all shaft power becomes fluid power — some is lost to friction, heat, and mechanical losses inside the pump. Therefore P_shaft = ρgQH / η = 14.7 / 0.75 ≈ 19.6 kW. Option A is the common error of forgetting that shaft power must be greater than delivered hydraulic power when efficiency < 1."

- question: "In the mechanical energy equation, head loss appears on the outlet side of the equation because it represents energy removed from the fluid, just like turbine head."
  type: true-false
  answer: false
  explanation: "Head loss and turbine head are both on the outlet (right) side, but for fundamentally different reasons. Turbine head represents useful work extracted — energy transferred to rotating machinery that can do work elsewhere. Head loss represents energy permanently destroyed by viscous friction and converted to heat; it cannot be recovered or redirected. The two terms have opposite physical significance: one is useful extraction, the other is irreversible waste."

- question: "The concept of 'head' expresses each energy term in the mechanical energy equation as an equivalent height in meters, obtained by dividing energy per unit weight (J/N) by the gravitational constant."
  type: true-false
  answer: true
  explanation: "Dividing each energy term (J/kg) by g gives units of meters — a 'height equivalent' of energy. Pressure head P/ρg is the height a static column would reach; velocity head V²/2g is the kinetic energy expressed as height; elevation head z is the actual height. Expressing everything in meters of head makes all terms directly comparable and greatly simplifies piping system calculations."

- question: "A hydroelectric turbine extracts H_turbine = 50 m of head from water flowing at Q = 2 m³/s, and the turbine's efficiency is 0.85. What is the shaft power output, and why is it less than ρgQH_turbine?"
  type: short-answer
  answer: "P_shaft = η × ρgQH_turbine = 0.85 × 1000 × 9.81 × 2 × 50 ≈ 835 kW. It is less than the full hydraulic power (ρgQH_turbine ≈ 981 kW) because the turbine cannot convert all fluid energy to shaft work — internal friction, fluid leakage, and mechanical losses dissipate some energy within the turbine itself."
  explanation: "The hydraulic power available from the fluid equals ρgQH_turbine. A turbine with efficiency η < 1 converts only a fraction of that to useful shaft output; the rest is dissipated internally. This mirrors the pump case: shaft input > hydraulic output for pumps (η < 1 means you pay more than you get), and shaft output < hydraulic input for turbines (η < 1 means you get less than is available)."
```

## Explainer

You already know that Bernoulli's equation is an energy balance along a streamline for an ideal, inviscid fluid: pressure energy, kinetic energy, and potential energy trade off while their sum stays constant. But Bernoulli breaks down when the fluid passes through a machine (pump or turbine) or when friction is significant. The mechanical energy equation is the corrected version: it adds terms for work added by pumps, work extracted by turbines, and energy destroyed by friction — all expressed in the same units of length called **head**.

**Head** is the most important concept here. By dividing each energy term by ρg, you convert joules per kilogram into meters — a "height equivalent" of energy. Pressure head (P/ρg) is the height a column of fluid would reach if all pressure energy were converted to elevation. Velocity head (V²/2g) is the equivalent height for kinetic energy. Elevation head z is the actual height. **Pump head** H_pump is the mechanical energy added to the fluid per unit weight of fluid — it increases the total head at the pump discharge. **Turbine head** H_turbine is the energy extracted. **Head loss** H_loss is energy permanently destroyed by viscous friction and converted to heat; it always appears on the right side of the equation because you always lose it, regardless of which way you write the balance.

The equation p₁/ρg + V₁²/2g + z₁ + H_pump = p₂/ρg + V₂²/2g + z₂ + H_turbine + H_loss reads as: total head at inlet, plus any head added by a pump, equals total head at outlet, plus any head extracted by a turbine, plus all head losses in between. This is an accounting statement: every joule of energy that enters a control volume must go somewhere. To use it in a piping system problem, pick two points (usually where conditions are known, like tank surfaces), write the equation, and solve for the unknown — typically pump head, flow rate, or pressure at some point.

The power required by or delivered by a machine follows directly from the head: P = ρgQH, where Q is volumetric flow rate. This connects the hydraulic head concept back to the first-law open-system analysis you learned earlier — power is the rate of energy transfer. Real pumps and turbines have efficiencies less than 1, so the shaft power input to a pump is P_shaft = ρgQH_pump/η_pump, and the shaft power output from a turbine is P_shaft = η_turbine · ρgQH_turbine. Correctly applying this equation is what allows engineers to size pumps for water distribution systems, calculate hydroelectric power output, or determine whether a pipe network can deliver the required flow rate.
