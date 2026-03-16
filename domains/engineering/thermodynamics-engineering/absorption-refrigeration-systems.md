---
id: absorption-refrigeration-systems
title: Absorption Refrigeration Systems
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: absorption-refrigeration-cycles
  type: hard
- id: partial-molar-properties-solutions
  type: soft
builds-toward:
- heat-pump-cycles-detailed
tags:
- absorption
- refrigeration
- heat-driven
- thermodynamics
stage: advanced
status: draft
---

# Absorption Refrigeration Systems

## Core Idea
Absorption cycles use a sorbent (lithium bromide-water or ammonia-water) to absorb refrigerant vapor instead of mechanical compression, driven by low-grade heat (steam, hot water). They reduce electricity consumption at the cost of higher heat input; performance depends on solution thermodynamics and regenerator effectiveness. Common in industrial cooling and when waste heat is available.

## Explainer

A conventional vapor-compression refrigerator uses an electric compressor to raise refrigerant pressure. An **absorption refrigeration system** achieves the same pressure elevation without a compressor, replacing mechanical work with heat. To anyone who has studied the basic absorption cycle, the question becomes: how do real systems implement this, and what engineering tradeoffs govern their performance?

The working principle is chemical: instead of mechanically compressing refrigerant vapor, the absorption system dissolves it into a liquid **sorbent**. The two most common fluid pairs are **lithium bromide–water** (LiBr-H₂O), where water is the refrigerant and LiBr is the absorbent, and **ammonia–water** (NH₃-H₂O), where ammonia is the refrigerant. When refrigerant vapor contacts the cool, dilute sorbent in the **absorber**, it dissolves exothermically — releasing heat to a cooling water loop. The resulting rich solution (high refrigerant content) is pumped to the **generator**, where low-grade heat (waste steam, solar heat, or combustion products) drives the refrigerant vapor back out of solution. That vapor then enters a standard condenser–expansion valve–evaporator cycle, producing the desired cooling effect. The now-dilute weak solution returns to the absorber to close the loop. The only moving part requiring significant power is the small solution pump.

The thermodynamic performance depends critically on **solution thermodynamics**, connecting directly to your prerequisites on partial molar properties. The vapor pressure of refrigerant above the solution is a function of temperature and solution concentration — this relationship governs how much heat is required in the generator and how much cooling is extracted in the evaporator. The **coefficient of performance** COP = refrigeration effect / heat input typically reaches 0.6–0.8 for single-effect systems, far below the COP of 3–5 achievable by vapor-compression systems drawing on high-grade electricity. But the comparison is misleading when waste heat — with near-zero economic cost — is the heat source. A **solution heat exchanger** between the hot weak solution leaving the generator and the cold rich solution from the absorber preheats the incoming stream, reducing the generator heat load and improving effective COP.

The practical advantage of absorption systems is their near-zero electricity consumption, making them attractive wherever low-grade heat is available: industrial process waste heat, combined heat-and-power plants, solar thermal collectors, or direct-fired natural gas units in locations with high electricity costs. **Double-effect systems** introduce a second generator stage at higher pressure, using the high-temperature vapor produced in the first stage to drive a second evaporation step before condensing. This extracts more refrigeration per unit of heat input, raising COP to roughly 1.2–1.4 at the cost of requiring a higher-temperature heat source (above ~160°C) and more complex equipment. The engineering tradeoff is always between capital cost, available heat source temperature, and target COP — absorption refrigeration earns its place precisely when the waste heat is already there and electricity is expensive or scarce.
