---
id: absorption-refrigeration-cycles
title: Absorption and Adsorption Refrigeration Cycles
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: vapor-compression-refrigeration-cycle
  type: hard
- id: psychrometrics-humid-air-properties
  type: soft
tags:
- absorption
- adsorption
- refrigeration
- cop
- heat-pump
stage: advanced
status: draft
---

# Absorption and Adsorption Refrigeration Cycles

## Core Idea
Absorption cycles replace mechanical compression with heat-driven chemical separation (e.g., ammonia-water, lithium-bromide-water). A weak solution is heated in the generator to release refrigerant vapor; vapor cools in the condenser and expands to the evaporator, where it absorbs heat; concentrated solution returns to the generator via solution pump. Lower COP (0.5-0.8) than vapor-compression but enables waste heat recovery and reduced electric consumption.

## Explainer

In the vapor-compression cycle you already know, a mechanical compressor does the essential thermodynamic work: it raises the refrigerant vapor from low pressure (evaporator) to high pressure (condenser). That compression requires shaft work — electricity or a mechanical drive. The absorption cycle asks a different question: can we replace that electrical energy with *heat* instead? The answer is yes, because of a chemical trick: certain refrigerants (typically ammonia, NH₃) dissolve readily into absorbent solutions (typically water) at low temperature and low pressure, and are then driven back out of solution by heating.

Here is the substitution. In vapor-compression, the compressor receives low-pressure vapor and delivers high-pressure vapor. In absorption, this function is replaced by three components working together: an **absorber**, a **solution pump**, and a **generator**. In the absorber, refrigerant vapor from the evaporator is absorbed into the weak solution, releasing heat. The resulting strong solution (rich in refrigerant) is then pumped to high pressure — and pumping a *liquid* requires only about 1/1000 the work of compressing a *vapor* at the same pressure ratio, because liquids are nearly incompressible. In the generator, heat from an external source (waste heat, a gas flame, solar energy) drives the refrigerant back out of the strong solution as high-pressure vapor. The depleted solution returns to the absorber via an expansion valve, completing the solution circuit. Meanwhile, the high-pressure refrigerant vapor proceeds through a condenser and evaporator exactly as in the vapor-compression cycle.

The thermodynamic accounting changes because you are now supplying heat (Q_gen) rather than work (W_comp) as the primary input. The **COP** is defined as Q_evap / Q_gen — refrigeration delivered per unit of heat consumed — and typically falls between 0.5 and 0.8 for single-effect absorption systems, compared to 3–5 for vapor-compression. On the surface this looks worse, but the comparison is misleading when the heat input is essentially free: waste heat from an industrial process, exhaust from a generator, or solar thermal panels all have near-zero marginal cost. In those contexts, a COP of 0.7 with free heat beats a COP of 4 requiring expensive electricity.

The most common working pairs are **ammonia-water** (NH₃/H₂O), used where sub-zero evaporator temperatures are needed, and **lithium bromide-water** (LiBr/H₂O), used in large commercial chillers where evaporator temperatures stay above 0°C (since the refrigerant is water itself). The choice of pair determines the operating pressures, temperatures, the complexity of rectification needed to purify the refrigerant vapor, and the practical COP. Absorption refrigeration is widely used in industrial waste-heat recovery, natural-gas-fired cooling in remote locations, and wherever the economics favor heat over electricity as the driving energy.

