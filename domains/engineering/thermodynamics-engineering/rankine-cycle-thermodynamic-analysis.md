---
id: rankine-cycle-thermodynamic-analysis
title: Rankine Cycle and Steam Power Plants
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-closed-systems
  type: hard
- id: saturated-superheated-property-regions
  type: hard
- id: carnot-cycle
  type: soft
- id: heat-engine-efficiency-and-carnot
  type: soft
builds-toward:
- rankine-cycle-reheat-regeneration
tags:
- rankine-cycle
- steam-power
- power-cycles
stage: advanced
status: draft
---

# Rankine Cycle and Steam Power Plants

## Core Idea
The Rankine cycle (pumping, isobaric heating, isentropic expansion, isobaric condensation) models the steam power plant and defines thermal efficiency in terms of heat input and rejection. Typical Rankine cycles operate between fixed saturation pressures with throttling and actual pressure drops reducing efficiency below the Carnot limit. State-by-state analysis using property tables reveals where irreversibilities occur and what pressure ratios maximize output.

## How It's Best Learned
Sketch the Rankine cycle on T-s and h-P diagrams, labeling each state and process. Calculate all four state properties at each state point using steam tables. Compute pump work (approximately ν * ΔP for liquid), turbine work (using isentropic or actual efficiency), heat transfers, and thermal efficiency. Compare to Carnot cycle efficiency to quantify the gap.

## Common Misconceptions
- The Rankine cycle achieves higher efficiency than Carnot because it uses two-phase expansion; Carnot is the absolute upper limit and Rankine achieves less.
- Increasing boiler pressure always increases thermal efficiency; higher pressure increases work but also reduces heat rejected, with complex tradeoffs.
- The pump work is negligible because liquids are incompressible; pumping liquid still requires work proportional to ν ΔP, which increases with boiler pressure.

## Questions

```yaml
- question: "Why is the thermal efficiency of the ideal Rankine cycle always less than the Carnot efficiency operating between the same maximum and minimum temperatures?"
  type: multiple-choice
  options:
    - "The Rankine cycle rejects more heat because the condenser is less efficient than an ideal isothermal heat sink"
    - "Heat is added over a range of temperatures in the boiler, making the mean addition temperature less than T_H, unlike Carnot's isothermal heat addition at T_H"
    - "The pump consumes work, reducing net output in a way the Carnot cycle does not"
    - "The Rankine cycle uses a two-phase working fluid, which reduces the work output of the turbine"
  answer: 1
  explanation: "Carnot efficiency η = 1 − T_L/T_H assumes all heat is added at T_H. In the Rankine cycle, heat is added across the entire boiler process: first heating subcooled liquid to saturation temperature, then boiling, then possibly superheating — so heat enters at temperatures ranging from below T_H up to T_H. The *mean* temperature of heat addition is lower than T_H, reducing efficiency below Carnot. The T-s diagram shows this graphically: the Rankine heat addition rectangle is 'smaller' than the Carnot rectangle with the same T_H and T_L limits."

- question: "In the ideal Rankine cycle, what is the expression for pump work per unit mass, and why is it small compared to turbine work?"
  type: multiple-choice
  options:
    - "w_pump = h₃ − h₄; it is small because steam expands at high enthalpy"
    - "w_pump = ν(P₂ − P₁); it is small because liquids have very low specific volume"
    - "w_pump = R·T·ln(P₂/P₁); it is small because the temperature ratio is modest"
    - "w_pump = c_p(T₂ − T₁); it is small because liquid heat capacity is low"
  answer: 1
  explanation: "Pump work for an incompressible fluid is w_pump = ν(P₂ − P₁), where ν is the specific volume of the liquid. Liquid water has a very small specific volume (~0.001 m³/kg), so even a large pressure rise (e.g., from 10 kPa to 10 MPa) produces relatively small pump work. Compare this to turbine work, which involves expanding compressible steam from high enthalpy at high pressure — the turbine handles far more energy per unit mass, which is why net work output is dominated by the turbine term."

- question: "The Rankine cycle can theoretically achieve Carnot efficiency if the boiler pressure is increased to a sufficiently high value."
  type: true-false
  answer: false
  explanation: "The Carnot efficiency is an absolute upper limit — no heat engine operating between two temperature reservoirs can exceed it. The Rankine cycle is always less efficient than Carnot because heat is added over a range of temperatures rather than isothermally at T_H. Increasing boiler pressure does raise thermal efficiency by elevating the mean temperature of heat addition, but the Rankine efficiency asymptotically approaches the Carnot limit as a bound it can never reach. Furthermore, very high pressures create practical problems (turbine blade erosion from wet steam) before the efficiency gain is fully realized."

- question: "Superheating steam beyond the saturation point at constant boiler pressure simultaneously raises thermal efficiency and reduces moisture content at the turbine exit."
  type: true-false
  answer: true
  explanation: "Superheating achieves two benefits at once. First, it raises the mean temperature of heat addition (since heat enters at higher temperatures during superheating), directly improving thermal efficiency. Second, the turbine exit state (State 4 on the T-s diagram) moves to the right — toward higher quality (lower moisture fraction) — because the expansion starts from a higher-enthalpy, higher-entropy state. Wet steam (high moisture) erodes turbine blades, so reducing moisture is an important practical constraint, and superheating solves both problems simultaneously."

- question: "Use the T-s diagram to explain why the Rankine cycle's thermal efficiency is always less than Carnot efficiency between the same temperature limits."
  type: short-answer
  answer: "On the T-s diagram, Carnot efficiency corresponds to a rectangle bounded by T_H at the top, T_L at the bottom, and two vertical (isentropic) sides — all heat is added at T_H. The Rankine cycle's heat addition process traces a path that begins at low temperature (subcooled liquid), rises through the saturation dome, and only reaches T_H at the end of superheating (if present). The area under this non-rectangular heat addition path represents lower average temperature than T_H. Since efficiency depends on the mean temperature of heat addition, not just the peak, the Rankine cycle's mean T_add < T_H, giving η_Rankine < η_Carnot."
  explanation: "The T-s diagram makes this geometric: Carnot's heat addition is a horizontal line at T_H; Rankine's is a rising curve. The area under Rankine's curve (heat added) divided by the total area of the process gives a lower ratio than Carnot's rectangle. Any cycle that cannot add all its heat at T_H will fall short of the Carnot limit."
```

## Explainer

The Rankine cycle is the thermodynamic model underlying every coal, nuclear, and natural gas steam power plant on earth. You already know the Carnot cycle, which defines the theoretical efficiency limit η = 1 − T_L/T_H, and you know how to use steam tables to find enthalpy and entropy values for water at any pressure-temperature state. The Rankine cycle puts these together into a practical cycle that exploits the phase-change properties of water — specifically, the fact that condensing and boiling happen at constant temperature and pressure.

The cycle has four states and four processes. **State 1**: saturated liquid leaving the condenser at low pressure. **Process 1→2**: the **pump** compresses the liquid to high pressure. Because liquids are nearly incompressible, the specific volume ν is approximately constant, and pump work w_pump = ν(P_2 − P_1) is small. **State 2**: subcooled liquid at high pressure. **Process 2→3**: the **boiler** adds heat at constant pressure, heating the water through the subcooled liquid region, across the saturation dome (boiling), and potentially into the superheated vapor region. **State 3**: high-pressure steam (saturated or superheated). **Process 3→4**: the **turbine** expands the steam isentropically (in ideal analysis) to low pressure, doing work. **State 4**: low-quality wet steam at condenser pressure. **Process 4→1**: the **condenser** rejects heat at constant pressure as the steam condenses back to liquid.

Thermal efficiency is η = (w_turbine − w_pump) / q_boiler = (h_3 − h_4 − (h_2 − h_1)) / (h_3 − h_2). The dominant term is the turbine work h_3 − h_4; pump work is small by comparison because pumping liquid requires much less work than compressing vapor. The T-s diagram shows immediately where the cycle loses efficiency relative to Carnot: heat is added over a range of temperatures (from subcooled liquid through the dome to superheated steam), not at a single maximum temperature. The mean temperature of heat addition is less than T_H, which is why Rankine efficiency is always below Carnot efficiency between the same temperature limits.

The levers for improving efficiency follow directly from this picture. **Increasing boiler pressure** raises the saturation temperature and shifts more heat addition to higher temperatures, improving η — but it also increases moisture at the turbine exit (state 4 moves deeper into the two-phase region), which erodes turbine blades. **Superheating** (heating beyond saturation at constant pressure) raises both the mean addition temperature and the turbine exit quality, improving efficiency and reducing moisture simultaneously. **Lowering condenser pressure** (thus lowering T_L) increases the temperature difference and efficiency. These three modifications — higher pressure, superheating, lower condenser pressure — are standard in real power plants and each has a clear thermodynamic explanation once you can read the T-s diagram.
