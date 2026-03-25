---
id: stagnation-pressure-and-total-head
title: Stagnation Pressure and Total Head
domain: engineering
course: fluid-mechanics
prerequisites:
- id: bernoullis-equation
  type: hard
- id: fluid-kinematics
  type: soft
- id: form-drag-pressure-drag-components
  type: soft
- id: mechanical-energy-head-forms
  type: soft
builds-toward:
- isentropic-nozzle-flow-choked-conditions
- rayleigh-line-flow-stagnation-conditions
tags:
- pressure
- energy
- compressible-flow
stage: formal-systems
status: validated
---
# Stagnation Pressure and Total Head

## Core Idea
Stagnation pressure (total pressure) represents the pressure a moving fluid would reach if brought to rest isentropically. It equals static pressure plus dynamic pressure: P₀ = P + (1/2)ρV². The stagnation temperature similarly combines thermal and kinetic energy, remaining constant along streamlines in adiabatic flows. This concept is fundamental for understanding energy transformations in pumps, compressors, and jet flows.

## How It's Best Learned
Measure pressure at a stagnation point on a Pitot tube and compare to static pressure measured in the free stream. Verify Bernoulli's equation by showing the sum is constant. Then apply to subsonic nozzles where stagnation conditions are set by inlet state.

## Common Misconceptions
Stagnation pressure is not a 'real' pressure at every point—it is the pressure the fluid would have if brought to rest. Static pressure and dynamic pressure are not added linearly in compressible flows; you must use isentropic relations to convert between them.

## Questions

```yaml
- question: "An engineer says 'the stagnation pressure at this point in the flow is 150 kPa.' What does this actually mean, physically?"
  type: multiple-choice
  options:
    - "A pressure gauge installed at that point in the flow reads 150 kPa"
    - "If the fluid at that point were brought to rest isentropically (without losses), it would have a pressure of 150 kPa — this value encodes the total mechanical energy the fluid carries"
    - "The velocity at that point is zero and the static pressure is 150 kPa"
    - "The flow is everywhere at 150 kPa pressure, and velocity only increases at narrowed sections"
  answer: 1
  explanation: "Stagnation pressure is not a 'real' pressure that a gauge at every point would read — it is a thermodynamic bookkeeping quantity representing the total mechanical energy per unit volume in the flow. Only at an actual stagnation point (like the tip of a Pitot tube, where velocity genuinely equals zero) does a pressure gauge read the stagnation pressure directly. Everywhere else, the gauge reads the lower static pressure P, and V > 0. The stagnation pressure is best understood as: 'if I could stop this parcel isentropically, how much pressure would it have?' That hypothetical value encodes its kinetic + pressure energy combined."

- question: "A Pitot tube in an airflow reads stagnation pressure P₀ = 120 kPa at its stagnation port. A static port nearby reads P = 100 kPa. The air density is ρ = 1.2 kg/m³. Using the incompressible Bernoulli relation, what is the flow velocity?"
  type: multiple-choice
  options:
    - "V = √(2 × 20,000 / 1.2) ≈ 183 m/s"
    - "V = (120,000 − 100,000) / 1.2 ≈ 16,700 m/s"
    - "V = √(120,000 / 1.2) ≈ 316 m/s"
    - "V = 2 × (120,000 − 100,000) / 1.2 ≈ 33,333 m/s"
  answer: 0
  explanation: "From P₀ = P + ½ρV², we get V = √(2(P₀ − P)/ρ) = √(2 × 20,000 / 1.2) = √(33,333) ≈ 183 m/s. The pressure difference ΔP = 20,000 Pa (not 20 Pa), so unit consistency is critical. Option B divides rather than takes the square root — a common error. Option C uses P₀ directly rather than the pressure difference, which is wrong because P₀ includes both static and dynamic contributions; only the difference (P₀ − P) represents the kinetic energy converted to pressure at the stagnation point."

- question: "In steady, inviscid, incompressible flow, stagnation pressure P₀ = P + ½ρV² is constant everywhere in the flow field."
  type: true-false
  answer: false
  explanation: "Bernoulli's equation guarantees that P₀ is constant *along a streamline* in irrotational, inviscid, incompressible, steady flow. Different streamlines can — and generally do — have different stagnation pressures, especially if they originate from different upstream conditions. Only in a uniform, irrotational flow field does every streamline carry the same stagnation pressure, making P₀ constant throughout the field. In a viscous flow or across a shock wave, stagnation pressure drops due to irreversible energy losses."

- question: "In compressible flow at Mach 0.8, the static pressure equals the stagnation pressure minus the incompressible dynamic pressure: P = P₀ − ½ρV²."
  type: true-false
  answer: false
  explanation: "The formula P₀ = P + ½ρV² is the *incompressible* approximation, valid only at low Mach numbers where density variations are negligible. At M = 0.8, compressibility effects are significant and the correct relation is the isentropic formula: P₀/P = (1 + (γ−1)/2 × M²)^(γ/(γ−1)). For air (γ = 1.4) at M = 0.8, this gives P₀/P ≈ 1.524, meaning P ≈ 0.656 P₀ — substantially different from what the incompressible formula predicts. Using the incompressible formula at transonic Mach numbers introduces significant error and would predict incorrect velocities in aircraft applications."

- question: "Explain why stagnation conditions (P₀, T₀) are the natural reference state for analyzing compressible nozzle flows, and what physical processes would change them."
  type: short-answer
  answer: "In an isentropic (adiabatic and frictionless) process, stagnation pressure P₀ and stagnation temperature T₀ remain constant along streamlines even as static pressure and temperature vary dramatically. As fluid accelerates through a converging nozzle, static pressure and temperature fall sharply while velocity increases — but P₀ and T₀ stay fixed, encoding the total energy content of the flow. This makes them ideal reference quantities: all local flow conditions can be expressed as fractions of these fixed reference values using isentropic ratios, and the entire flow field is characterized by specifying the inlet stagnation conditions alone. What changes them: frictional losses (viscosity, boundary layers) irreversibly reduce P₀ by converting ordered kinetic energy to thermal energy (entropy production); a normal shock wave dramatically drops P₀; heat addition increases T₀ and reduces P₀ (Rayleigh flow). Any process that generates entropy reduces P₀ — so a drop in stagnation pressure along a duct is a direct thermodynamic measure of irreversibility."
```

## Explainer

Bernoulli's equation — your core prerequisite — states that along a streamline in steady, inviscid, incompressible flow, P + ½ρV² + ρgz is constant. Each term represents energy per unit volume: pressure energy, kinetic energy, and gravitational potential energy. **Stagnation pressure** P₀ is what you get when all the kinetic energy is converted to pressure energy: P₀ = P + ½ρV². It represents the pressure a moving fluid parcel would have if brought to rest **isentropically** — without friction or heat transfer, so that no energy is lost in the conversion. Stagnation pressure does not exist as a local property everywhere in the flow; it is a hypothetical thermodynamic bookkeeping value that encodes the total mechanical energy the fluid carries.

The place where the flow actually reaches stagnation is the **stagnation point** — the tip of a Pitot tube, the leading edge of an airfoil, the nose of a blunt body. Here the velocity is literally zero and P = P₀. Every other location in the flow has V > 0 and therefore P < P₀. A **Pitot tube** exploits this directly: its open stagnation port measures P₀ while a nearby static port measures P. Velocity follows from V = √(2(P₀ − P)/ρ). This is how aircraft airspeed indicators work, and it is why Pitot tubes are the universal velocity sensor for any flow where you can make a stagnation point.

**Total head** H = P₀/(ρg) = P/(ρg) + V²/(2g) + z rewrites Bernoulli's equation in units of length — meters of fluid column — rather than pressure. Hydraulic engineers prefer head because they want to track energy budgets through systems with pumps, turbines, valves, and friction losses. A pump adds total head; a turbine extracts it; pipe friction dissipates it irreversibly. The hydraulic grade line (plotting P/(ρg) + z) and the energy grade line (plotting H) provide visual maps of how pressure and velocity energy are distributed and lost along a pipeline.

The stagnation concept becomes especially powerful — and qualitatively different — in compressible (high-speed) flows. In incompressible flow, P₀ = P + ½ρV² is exact. In compressible flow, density changes with velocity, and the correct relation is the isentropic stagnation formula: P₀/P = (1 + (γ−1)/2 × M²)^(γ/(γ−1)), where M is the Mach number. At low M this reduces to the incompressible result, but at M = 1 (sonic flow), P₀/P = 1.893 for air — the static pressure is only 53% of the stagnation pressure. In compressible nozzles and diffusers, **stagnation conditions** (P₀, T₀) remain constant through an isentropic process even as static pressure and temperature vary dramatically. They are the natural reference state for the entire flow field — the "energy bank account" that the fluid draws from as it accelerates through a nozzle.
