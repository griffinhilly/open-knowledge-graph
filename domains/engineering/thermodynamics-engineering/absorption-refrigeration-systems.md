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
stage: formal-systems
status: validated
---

# Absorption Refrigeration Systems

## Core Idea
Absorption cycles use a sorbent (lithium bromide-water or ammonia-water) to absorb refrigerant vapor instead of mechanical compression, driven by low-grade heat (steam, hot water). They reduce electricity consumption at the cost of higher heat input; performance depends on solution thermodynamics and regenerator effectiveness. Common in industrial cooling and when waste heat is available.

## Questions

```yaml
- question: "A facility manager compares an absorption chiller (COP ≈ 0.7, heat-driven) with a vapor-compression chiller (COP ≈ 4.5, electricity-driven). She concludes the vapor-compression unit is always superior because its COP is higher. In which situation would the absorption chiller be the better economic choice?"
  type: multiple-choice
  options:
    - "When the cooling load is very small and the absorption unit is cheaper to purchase"
    - "When the facility has abundant waste heat from industrial processes at near-zero economic cost"
    - "When ambient temperatures are extremely high, reducing vapor-compression efficiency"
    - "When refrigerant regulations prohibit the use of synthetic refrigerants like R-134a"
  answer: 1
  explanation: "The COP comparison is misleading when the energy sources differ in cost. A vapor-compression COP of 4.5 means 4.5 units of cooling per unit of *expensive* electricity. An absorption COP of 0.7 means 0.7 units of cooling per unit of *waste heat that would otherwise be discarded*. If waste heat is available at near-zero marginal cost, the absorption system produces essentially free cooling despite its lower thermodynamic efficiency. The relevant economic comparison is cost per unit of cooling delivered, not COP alone. This is the central insight of absorption refrigeration: it is not more thermodynamically efficient — it is economically efficient when the right energy source is available."

- question: "In a lithium bromide-water absorption refrigeration system, which component or pair of components serves the same functional role as the compressor in a vapor-compression system?"
  type: multiple-choice
  options:
    - "The condenser — it rejects heat at high pressure"
    - "The expansion valve — it creates the pressure difference"
    - "The generator and absorber together — they raise refrigerant pressure by driving it out of solution with heat, then reabsorbing it at low pressure"
    - "The solution heat exchanger — it recovers energy between the high- and low-pressure sides"
  answer: 2
  explanation: "In vapor-compression, the compressor takes low-pressure refrigerant vapor and raises it to high pressure mechanically. In absorption refrigeration, the generator uses heat to drive refrigerant vapor out of the rich solution (equivalent to 'creating' high-pressure vapor), and the absorber reabsorbs vapor at low pressure (equivalent to 'completing the compression cycle' chemically). Together, the generator and absorber perform the pressure elevation that the compressor achieves mechanically. The expansion valve exists in both systems to drop pressure from condenser to evaporator. The solution heat exchanger is an efficiency-improving feature with no direct compressor analogue."

- question: "In an absorption refrigeration system, the refrigerant vapor is chemically absorbed into a liquid sorbent and then driven off by heating, effectively replacing mechanical compression with a thermochemical cycle."
  type: true-false
  answer: true
  explanation: "This is the defining principle of absorption refrigeration. Refrigerant vapor at low pressure dissolves exothermically into a liquid sorbent (LiBr or water, depending on the fluid pair) in the absorber. The rich solution is then pumped (with minimal work) to higher pressure and heated in the generator, which drives the refrigerant vapor back out of solution at high pressure. The vapor then proceeds through a standard condenser-expansion valve-evaporator cycle. The net effect is that low-grade heat performs the pressure elevation that an electric compressor would otherwise provide."

- question: "Absorption refrigeration systems have a higher COP than vapor-compression systems of equivalent cooling capacity, making them thermodynamically superior whenever electricity is available."
  type: true-false
  answer: false
  explanation: "Absorption systems have substantially *lower* COP than vapor-compression systems: single-effect absorption COP is typically 0.6–0.8, while vapor-compression COP is typically 3–5. Absorption systems are not thermodynamically superior — they trade thermodynamic efficiency for near-zero electricity consumption. Their economic advantage arises only when low-grade waste heat is available at low or zero marginal cost. When electricity is the only available energy source, vapor-compression refrigeration is almost always the better choice. The COP comparison is meaningful only when the cost and quality of the energy inputs are held constant."

- question: "Explain why comparing the COP of an absorption chiller to that of a vapor-compression chiller can be misleading, and under what specific circumstances an absorption system is the better engineering choice."
  type: short-answer
  answer: "COP comparisons are misleading when the energy inputs differ in cost and quality. Vapor-compression COP measures refrigeration per unit of high-grade electricity; absorption COP measures refrigeration per unit of low-grade heat. If the absorption system is driven by waste heat that would otherwise be rejected (at near-zero marginal cost), its effective cost of cooling can be far lower than a high-COP vapor-compression unit drawing on expensive electricity. Absorption systems are the better choice when: (1) low-grade waste heat is available (industrial processes, combined heat-and-power plants, solar thermal), (2) electricity is expensive or unavailable, and (3) near-zero electricity consumption is valued (remote locations, grid-constrained facilities). The engineering decision requires comparing total cost of cooling delivered — not raw COP — accounting for the actual cost of each energy input."
  explanation: "This question gets at a fundamental lesson in engineering economics: efficiency metrics only guide decisions when the inputs being compared have the same value. Waste heat and electricity are not equivalent inputs. A 'less efficient' system can be economically superior when it consumes a lower-cost resource. Double-effect absorption systems (COP ≈ 1.2–1.4) narrow the gap with vapor-compression at the cost of higher heat source temperatures and more complex equipment, but they still do not outperform vapor-compression on raw thermodynamic COP — they simply become viable in a wider range of waste-heat scenarios."
```

## Explainer

A conventional vapor-compression refrigerator uses an electric compressor to raise refrigerant pressure. An **absorption refrigeration system** achieves the same pressure elevation without a compressor, replacing mechanical work with heat. To anyone who has studied the basic absorption cycle, the question becomes: how do real systems implement this, and what engineering tradeoffs govern their performance?

The working principle is chemical: instead of mechanically compressing refrigerant vapor, the absorption system dissolves it into a liquid **sorbent**. The two most common fluid pairs are **lithium bromide–water** (LiBr-H₂O), where water is the refrigerant and LiBr is the absorbent, and **ammonia–water** (NH₃-H₂O), where ammonia is the refrigerant. When refrigerant vapor contacts the cool, dilute sorbent in the **absorber**, it dissolves exothermically — releasing heat to a cooling water loop. The resulting rich solution (high refrigerant content) is pumped to the **generator**, where low-grade heat (waste steam, solar heat, or combustion products) drives the refrigerant vapor back out of solution. That vapor then enters a standard condenser–expansion valve–evaporator cycle, producing the desired cooling effect. The now-dilute weak solution returns to the absorber to close the loop. The only moving part requiring significant power is the small solution pump.

The thermodynamic performance depends critically on **solution thermodynamics**, connecting directly to your prerequisites on partial molar properties. The vapor pressure of refrigerant above the solution is a function of temperature and solution concentration — this relationship governs how much heat is required in the generator and how much cooling is extracted in the evaporator. The **coefficient of performance** COP = refrigeration effect / heat input typically reaches 0.6–0.8 for single-effect systems, far below the COP of 3–5 achievable by vapor-compression systems drawing on high-grade electricity. But the comparison is misleading when waste heat — with near-zero economic cost — is the heat source. A **solution heat exchanger** between the hot weak solution leaving the generator and the cold rich solution from the absorber preheats the incoming stream, reducing the generator heat load and improving effective COP.

The practical advantage of absorption systems is their near-zero electricity consumption, making them attractive wherever low-grade heat is available: industrial process waste heat, combined heat-and-power plants, solar thermal collectors, or direct-fired natural gas units in locations with high electricity costs. **Double-effect systems** introduce a second generator stage at higher pressure, using the high-temperature vapor produced in the first stage to drive a second evaporation step before condensing. This extracts more refrigeration per unit of heat input, raising COP to roughly 1.2–1.4 at the cost of requiring a higher-temperature heat source (above ~160°C) and more complex equipment. The engineering tradeoff is always between capital cost, available heat source temperature, and target COP — absorption refrigeration earns its place precisely when the waste heat is already there and electricity is expensive or scarce.
