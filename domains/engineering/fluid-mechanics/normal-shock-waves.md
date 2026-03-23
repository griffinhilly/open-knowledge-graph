---
id: normal-shock-waves
title: Normal Shock Waves
domain: engineering
course: fluid-mechanics
prerequisites:
- id: compressible-flow-basics
  type: hard
tags:
- normal shock
- Rankine-Hugoniot
- shock relations
- total pressure loss
- supersonic to subsonic
stage: formal-systems
status: validated
---
# Normal Shock Waves

## Core Idea
A normal shock wave is an extremely thin (~micrometers), stationary discontinuity perpendicular to the flow direction across which a supersonic flow abruptly decelerates to subsonic. Conservation of mass, momentum, and energy across the shock — the Rankine-Hugoniot relations — uniquely determine the downstream conditions given the upstream Mach number. Across a normal shock: static pressure, temperature, density, and entropy all increase, while velocity, Mach number, and total (stagnation) pressure all decrease. The total temperature remains constant (adiabatic process), but the process is irreversible, so total pressure is permanently lost. The strength of these jumps increases with upstream Mach number — at Ma₁ = 1 the shock vanishes (no discontinuity), while at Ma₁ = 2 in air (γ = 1.4), the pressure ratio is 4.5 and the downstream Mach number is 0.577. Normal shocks appear in supersonic inlets, at the exit of overexpanded nozzles, and ahead of blunt bodies in supersonic flight.

## How It's Best Learned
Use the normal shock tables (or derive them from the Rankine-Hugoniot relations) to compute downstream conditions for several upstream Mach numbers. Plot pressure ratio, temperature ratio, and total pressure ratio vs. Ma₁ to see the nonlinear growth. Analyze a converging-diverging nozzle at an intermediate back pressure where a normal shock stands in the diverging section: locate the shock position, compute conditions on each side, and verify that the exit pressure matches the imposed back pressure.

## Common Misconceptions
- A normal shock is not isentropic — entropy increases across the shock. This means total pressure decreases, which is why shock waves in engine inlets degrade performance and engineers design inlets to minimize or oblique the shocks.
- The flow downstream of a normal shock is always subsonic (Ma₂ < 1), regardless of how strong the upstream supersonic flow is. This is a mathematical consequence of the conservation equations, not an assumption.
- Normal shocks cannot exist in subsonic flow. If Ma₁ < 1, the Rankine-Hugoniot relations would require entropy to decrease, violating the second law of thermodynamics. Compression in subsonic flow occurs smoothly through pressure waves, not shocks.

## Questions

```yaml
- question: "Two supersonic inlet designs are proposed for a jet engine operating at Mach 2. Design A uses a single normal shock to decelerate flow to subsonic before the compressor. Design B uses two oblique shocks that progressively slow the flow, followed by a weak normal shock. Which design recovers more total pressure, and why?"
  type: multiple-choice
  options:
    - "Design A, because one strong shock is more efficient than multiple weak ones"
    - "Design B, because a sequence of weaker shocks each generates less entropy than one strong shock, preserving more total pressure"
    - "Both designs recover equal total pressure, since both obey the Rankine-Hugoniot relations"
    - "Design A, because total pressure is conserved in normal shocks since no heat is added"
  answer: 1
  explanation: "Total pressure loss across a shock is a measure of irreversibility — entropy generated. The total pressure ratio P₀₂/P₀₁ decreases steeply with increasing upstream Mach number. One strong normal shock at Mach 2 yields P₀₂/P₀₁ ≈ 0.72 (28% loss). Two weaker oblique shocks and a final weak normal shock at, say, Mach 1.3 can achieve P₀₂/P₀₁ ≈ 0.97 (only 3% loss). This is the fundamental principle behind variable-geometry supersonic inlets: replacing one strong normal shock with multiple weaker oblique shocks dramatically reduces entropy generation and total pressure loss. Option D is a critical misconception — normal shocks are adiabatic but NOT isentropic; entropy always increases across a shock."

- question: "A normal shock occurs in a flow with upstream Mach number Ma₁ = 3. Which statement correctly describes the flow immediately downstream of the shock?"
  type: multiple-choice
  options:
    - "The flow is supersonic with Ma₂ ≈ 2, since stronger shocks slow the flow more gradually"
    - "The flow is subsonic (Ma₂ < 1), with higher static pressure and temperature than upstream"
    - "The flow has the same total temperature and total pressure as upstream, since energy is conserved"
    - "The flow is subsonic only if the upstream pressure is above a critical threshold"
  answer: 1
  explanation: "The Rankine-Hugoniot relations guarantee that the flow downstream of any normal shock is subsonic — Ma₂ < 1 always, for any Ma₁ > 1. At Ma₁ = 3, Ma₂ ≈ 0.475. Static pressure and temperature both increase sharply across the shock (pressure ratio ≈ 10.3, temperature ratio ≈ 2.7 for air). Option C is incorrect: while total temperature T₀ IS conserved (adiabatic process), total pressure P₀ is NOT — it decreases irreversibly as entropy increases. Option A is wrong categorically: normal shocks always produce subsonic downstream flow, regardless of shock strength."

- question: "The total temperature T₀ is conserved across a normal shock because the shock process is adiabatic — no heat is transferred across the shock wave."
  type: true-false
  answer: true
  explanation: "Total (stagnation) temperature T₀ = T(1 + (γ−1)/2 · M²) is conserved because the shock is adiabatic: the shock itself generates no heat exchange with the surroundings. Energy is conserved in the form of enthalpy, which gives constant total enthalpy and therefore constant total temperature. This is sometimes confused with the shock being isentropic — it is not. The shock IS adiabatic (constant T₀) but is NOT isentropic: entropy increases, and therefore total pressure P₀ decreases. The distinction between adiabatic and isentropic is critical in compressible flow analysis."

- question: "A normal shock wave can form in a subsonic flow if the pressure difference across the shock is large enough to drive the transition."
  type: true-false
  answer: false
  explanation: "Normal shocks cannot exist in subsonic flow. The Rankine-Hugoniot relations, derived from conservation of mass, momentum, and energy, require that Ma₁ > 1 for a physically realizable normal shock. If you attempt to apply the shock relations with Ma₁ < 1, the equations yield a downstream state with lower entropy than upstream — a violation of the second law of thermodynamics, which is physically impossible. In subsonic flow, pressure disturbances propagate upstream as sound waves and the flow adjusts smoothly, without discontinuities. Shocks are a uniquely supersonic phenomenon arising from the inability of supersonic flow to 'sense' and respond to downstream conditions."

- question: "Why does total pressure decrease across a normal shock even though no work is done on or by the flow and no heat is transferred? Where does the 'missing' mechanical energy go?"
  type: short-answer
  answer: "Total pressure represents the maximum recoverable work from a flowing fluid. Across the shock, the extremely rapid, irreversible compression within the thin shock layer (~micrometers) generates entropy — molecular-scale disorder increases as kinetic energy of directed flow is converted to random thermal motion (increased static temperature). This entropy increase irreversibly degrades the flow's ability to do useful work, reflected in the drop in total pressure. The total enthalpy (and therefore total temperature) is conserved — the energy hasn't been lost, but it has been thermodynamically degraded from organized mechanical energy into disordered thermal energy that cannot be fully converted back into work."
  explanation: "This is the distinction between energy conservation (first law) and entropy generation (second law). The first law is satisfied: total enthalpy is unchanged. But the second law governs the quality of energy: the entropy increase across the shock means some fraction of the mechanical energy has been irreversibly converted to heat. In engineering terms, the loss in total pressure represents a permanent reduction in the work-extracting capacity of the flow — which is why minimizing shock strength is critical in turbomachinery and propulsion system design."
```

## Explainer

From your prerequisite study of compressible flow basics, you know that the character of a flow changes fundamentally at Mach 1. In subsonic flow, pressure disturbances propagate as sound waves in all directions — including upstream — so the flow can sense and adjust to obstacles ahead. In supersonic flow, disturbances propagate only downstream; the flow has no advance warning of what is coming. When a supersonic flow must decelerate to match a downstream boundary condition — the stagnation pressure at a blunt body's nose, a subsonic nozzle exit, or the back pressure in a duct — it cannot do so gradually by sending information upstream. Instead it adjusts instantaneously, in an extraordinarily thin region called a **normal shock wave**.

Across the shock, conservation of mass, momentum, and energy — the **Rankine-Hugoniot relations** — uniquely determine all downstream conditions given only the upstream Mach number Ma₁. The results are sharp and counter-intuitive: static pressure, temperature, and density all jump upward, while velocity and Mach number drop. The downstream flow is always subsonic, with a Mach number Ma₂ that depends only on Ma₁ and the specific heat ratio γ. At Ma₁ = 2 in air (γ = 1.4), Ma₂ = 0.577, the static pressure ratio is 4.5, and the temperature ratio is 1.69. As Ma₁ → 1 from above, the shock weakens to zero; as Ma₁ → ∞, Ma₂ approaches a finite lower limit ((γ−1)/(2γ))^(1/2) ≈ 0.378 for air. The conservation equations determine the outcome completely — there is no choice.

The most important thermodynamic fact about a normal shock is its irreversibility. **Total temperature** T₀ is conserved — the process is adiabatic, with no heat transfer across the thin shock. But **total pressure** P₀ decreases, and it does so irreversibly: entropy increases across every shock, consistent with the second law. The total pressure ratio P₀₂/P₀₁ < 1 is a direct measure of the shock's entropy generation, and it decreases rapidly as Ma₁ increases above 1. This total pressure loss is the central performance penalty in propulsion systems. A jet engine ingesting a Mach 2 flow through a single normal shock loses about 27% of its total pressure before the air even reaches the compressor — an enormous efficiency hit. Supersonic inlet design is largely the art of replacing one strong normal shock with a sequence of weaker oblique shocks, each generating less entropy, collectively achieving higher total pressure recovery.

Normal shocks appear wherever supersonic flow must match a subsonic exit condition. In a converging-diverging nozzle operated at an intermediate back pressure, a normal shock stands in the diverging section, converting the supersonic core to subsonic. As back pressure decreases toward the design exit pressure, the shock moves toward the nozzle exit and weakens; at the design condition the shock disappears. Ahead of a blunt body in supersonic flight, a detached **bow shock** forms: it curves from nearly normal at the stagnation streamline (where the full deceleration to zero velocity occurs) to increasingly oblique off to the sides (where the deceleration is partial and the entropy rise is smaller). The stagnation point streamline, which crosses the normal portion of the bow shock, experiences the largest total pressure loss — this is why streamlining and pointed noses reduce supersonic drag.
