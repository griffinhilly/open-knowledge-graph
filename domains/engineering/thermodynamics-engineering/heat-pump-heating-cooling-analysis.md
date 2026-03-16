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
stage: advanced
status: draft
---

# Heat Pump Systems for Heating and Cooling

## Core Idea
A heat pump is a refrigeration cycle that delivers heating by reversing the flow direction or by using separate condensing and evaporating conditions. Heating performance is quantified by COP_heating = Q_out / W_net, which is always greater than unity (COP_cooling + 1). Heat pumps are energy-efficient for space heating in moderate climates but lose effectiveness as outdoor temperature drops, requiring backup electric resistance heat.

## Explainer

From your prerequisite on vapor-compression refrigeration, you know that the cycle moves heat from a cold reservoir to a hot reservoir by doing work — heat flows from the evaporator (cold side) to the condenser (hot side), driven by the compressor. A refrigerator uses this cycle to keep its interior cold and dumps heat to the warm kitchen. A heat pump uses the *same* cycle but asks a different question: instead of caring about the cold side, we want the heat being rejected at the hot side. In the winter, the hot side is your living space; the cold side is the outdoor air (or ground). The compressor "pumps" heat from cold outdoors into your warm house.

This is why **COP_heating** is always greater than 1 — and it is a useful fact to internalize. A resistance heater converts one unit of electrical work into exactly one unit of heat: COP = 1. A heat pump converts one unit of work into more than one unit of heat, because it also moves heat from the outdoor environment. The energy balance is: Q_H (heat delivered to the house) = Q_L (heat absorbed from outdoors) + W_net (compressor work). Since Q_H = Q_L + W_net, dividing both sides by W_net gives COP_heating = Q_H/W_net = (Q_L/W_net) + 1 = COP_cooling + 1. A system with COP_cooling of 2.5 (reasonable for moderate conditions) has COP_heating of 3.5 — delivering 3.5 units of heat for every 1 unit of electricity consumed. That is a threefold advantage over resistance heating.

The limitation is that COP depends on the temperature difference between the heat source and the heat sink. As outdoor temperature drops, two things happen: the evaporator pressure drops (the refrigerant must be colder than the outdoor air to absorb heat), and the condensing pressure stays high (the refrigerant must be hotter than the indoor air to deliver heat). A larger pressure ratio means more compressor work, reducing COP. At very low outdoor temperatures — below about −10°C to −15°C for standard heat pumps — the COP falls close to 1, and resistance backup heat becomes economically and thermodynamically necessary. Modern **cold-climate heat pumps** use variable-speed compressors and improved refrigerants to maintain reasonable COP down to −25°C or colder.

In summer, the cycle reverses: the indoor unit becomes the evaporator (cooling the house), and the outdoor unit becomes the condenser (rejecting heat to hot outdoor air). This is standard air conditioning. The same hardware handles both modes by reversing a four-way valve. The **balance point** is the outdoor temperature at which the heat pump's capacity exactly matches the building's heating load; below this temperature, supplemental heat is needed. Sizing a heat pump for a specific climate means finding the right balance point for the expected heating degree-days — a calculation that requires the cycle COP as a function of outdoor temperature, which you can now derive from the Carnot bound and isentropic compressor analysis.
