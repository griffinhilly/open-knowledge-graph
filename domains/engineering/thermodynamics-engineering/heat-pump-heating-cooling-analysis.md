---
id: heat-pump-heating-cooling-analysis
title: Heat Pump Systems for Heating and Cooling
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: vapor-compression-refrigeration-cycle
  type: hard
tags:
- heat-pump
- heating
- cooling
stage: formal-systems
status: draft
---

# Heat Pump Systems for Heating and Cooling

## Core Idea
A heat pump is a refrigeration cycle that delivers heating by reversing the flow direction or by using separate condensing and evaporating conditions. Heating performance is quantified by COP_heating = Q_out / W_net, which is always greater than unity (COP_cooling + 1). Heat pumps are energy-efficient for space heating in moderate climates but lose effectiveness as outdoor temperature drops, requiring backup electric resistance heat.

## Questions

```yaml
- question: "A heat pump system has a COP_cooling of 2.8 when operating in air-conditioning mode. What is its COP_heating when operating in heating mode under the same conditions?"
  type: multiple-choice
  options:
    - "2.8 — COP is a property of the hardware and doesn't change with mode"
    - "1.8 — you subtract 1 because some energy is lost reversing the cycle"
    - "3.8 — COP_heating = COP_cooling + 1"
    - "1.0 — heat pumps in heating mode are equivalent to resistance heaters"
  answer: 2
  explanation: "The energy balance gives Q_H = Q_L + W_net. Dividing by W_net: COP_heating = Q_H/W_net = (Q_L/W_net) + 1 = COP_cooling + 1 = 3.8. The extra 1 unit comes from the compressor work itself being converted to heat at the condenser. This relationship always holds: heating COP is exactly 1 greater than cooling COP under the same operating conditions. Option D is the classic misconception — a heat pump always outperforms resistance heating (COP = 1) as long as any heat is harvested from the outdoor air."

- question: "A homeowner's heat pump delivers 4 units of heat per unit of electricity on a mild 10°C winter day. On an extremely cold −20°C day, what would you expect?"
  type: multiple-choice
  options:
    - "The same COP of 4 — the heat pump's efficiency is a fixed equipment specification"
    - "A higher COP — colder outdoor air creates a larger temperature differential that drives more heat transfer"
    - "A lower COP — the larger temperature differential between indoor and outdoor requires more compressor work"
    - "COP exactly equals 1 — heat pumps cannot extract heat below freezing"
  answer: 2
  explanation: "COP depends on the temperature ratio between the hot and cold reservoirs (bounded above by Carnot COP). At −20°C, the evaporator must run even colder to absorb heat from the outdoor air, while the condenser still must heat the house — a much larger pressure ratio. More compressor work per unit of heat moved means lower COP. At extreme cold, COP can fall near 1, at which point supplemental resistance heating becomes necessary. Option B reverses the logic: a larger temperature difference always reduces thermodynamic efficiency, not improves it."

- question: "A heat pump with COP_heating of 3.5 violates conservation of energy because it delivers more heat energy than it consumes in electrical energy."
  type: true-false
  answer: false
  explanation: "No energy is created. The heat pump delivers Q_H = Q_L + W_net: 3.5 units of heat to the house, but 2.5 of those units come from outdoor heat extracted by the evaporator, and only 1 unit comes from the electrical input. Energy is fully conserved — the 'extra' heat comes from the environment, not from nothing. COP > 1 does not violate thermodynamics; it simply means the device moves more energy than it consumes as work."

- question: "A heat pump's COP_heating always exceeds 1 (as long as the system is functioning), whereas an electric resistance heater always has COP_heating = 1."
  type: true-false
  answer: true
  explanation: "This is the fundamental thermodynamic advantage of heat pumps. A resistance heater converts electrical work directly to heat with 100% conversion efficiency — exactly 1 unit of heat per unit of work, so COP = 1. A heat pump also converts the compressor work to heat, but additionally extracts heat from the outdoor environment, delivering Q_H = Q_L + W_net > W_net. As long as the system moves any heat at all from outdoors (Q_L > 0), COP_heating > 1. Even a poorly performing heat pump in very cold conditions is at least marginally better than resistance heat."

- question: "Explain why a heat pump's COP_heating decreases as the outdoor temperature drops. What thermodynamic mechanism causes this?"
  type: short-answer
  answer: "As outdoor temperature drops, the evaporator must operate at a lower temperature (below outdoor air) to absorb heat. Meanwhile, the condenser pressure stays high to deliver heat indoors. This wider temperature (and pressure) differential requires more compressor work per unit of heat transferred. Since COP_heating = Q_H / W_net, and W_net rises faster than Q_H as the temperature difference grows, COP falls. The upper bound is the Carnot COP = T_H / (T_H − T_L); as T_L drops, this bound decreases, pulling the real COP down with it."
  explanation: "The core insight is that COP is not a fixed equipment property — it depends on operating conditions. The compressor must overcome the pressure difference between the evaporator and condenser. Larger temperature differences mean larger pressure ratios, more compression work, and lower efficiency. This is why heat pumps are most efficient in mild climates and why cold-climate models require variable-speed compressors to maintain reasonable COP at low temperatures."
```

## Explainer

From your prerequisite on vapor-compression refrigeration, you know that the cycle moves heat from a cold reservoir to a hot reservoir by doing work — heat flows from the evaporator (cold side) to the condenser (hot side), driven by the compressor. A refrigerator uses this cycle to keep its interior cold and dumps heat to the warm kitchen. A heat pump uses the *same* cycle but asks a different question: instead of caring about the cold side, we want the heat being rejected at the hot side. In the winter, the hot side is your living space; the cold side is the outdoor air (or ground). The compressor "pumps" heat from cold outdoors into your warm house.

This is why **COP_heating** is always greater than 1 — and it is a useful fact to internalize. A resistance heater converts one unit of electrical work into exactly one unit of heat: COP = 1. A heat pump converts one unit of work into more than one unit of heat, because it also moves heat from the outdoor environment. The energy balance is: Q_H (heat delivered to the house) = Q_L (heat absorbed from outdoors) + W_net (compressor work). Since Q_H = Q_L + W_net, dividing both sides by W_net gives COP_heating = Q_H/W_net = (Q_L/W_net) + 1 = COP_cooling + 1. A system with COP_cooling of 2.5 (reasonable for moderate conditions) has COP_heating of 3.5 — delivering 3.5 units of heat for every 1 unit of electricity consumed. That is a threefold advantage over resistance heating.

The limitation is that COP depends on the temperature difference between the heat source and the heat sink. As outdoor temperature drops, two things happen: the evaporator pressure drops (the refrigerant must be colder than the outdoor air to absorb heat), and the condensing pressure stays high (the refrigerant must be hotter than the indoor air to deliver heat). A larger pressure ratio means more compressor work, reducing COP. At very low outdoor temperatures — below about −10°C to −15°C for standard heat pumps — the COP falls close to 1, and resistance backup heat becomes economically and thermodynamically necessary. Modern **cold-climate heat pumps** use variable-speed compressors and improved refrigerants to maintain reasonable COP down to −25°C or colder.

In summer, the cycle reverses: the indoor unit becomes the evaporator (cooling the house), and the outdoor unit becomes the condenser (rejecting heat to hot outdoor air). This is standard air conditioning. The same hardware handles both modes by reversing a four-way valve. The **balance point** is the outdoor temperature at which the heat pump's capacity exactly matches the building's heating load; below this temperature, supplemental heat is needed. Sizing a heat pump for a specific climate means finding the right balance point for the expected heating degree-days — a calculation that requires the cycle COP as a function of outdoor temperature, which you can now derive from the Carnot bound and isentropic compressor analysis.
