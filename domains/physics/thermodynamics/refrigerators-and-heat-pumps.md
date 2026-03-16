---
id: refrigerators-and-heat-pumps
title: Refrigerators and Heat Pumps
domain: physics
course: thermodynamics
prerequisites:
- id: heat-engines
  type: hard
- id: thermal-efficiency
  type: soft
builds-toward:
- second-law-of-thermodynamics
tags:
- refrigerator
- heat-pump
- COP
- coefficient-of-performance
- reversed-engine
stage: formal-systems
status: validated
---

# Refrigerators and Heat Pumps

## Core Idea
A refrigerator is a heat engine run in reverse: work W is input to move heat Q_C from a cold reservoir to a hot one. The coefficient of performance (COP) for a refrigerator is COP_R = Q_C/W, and for a heat pump (which heats a space) COP_HP = Q_H/W. Since Q_H = Q_C + W, both COPs can exceed 1. Heat naturally flows from hot to cold; refrigerators and heat pumps do the thermodynamically costly reverse, requiring external work.

## How It's Best Learned
Compare a refrigerator to a heat engine on an energy flow diagram — arrows point in the opposite direction. Calculate COP for a refrigerator maintaining −18°C in a 25°C room and compare to the Carnot COP limit.

## Common Misconceptions
- A heat pump does not 'create' heat — it moves heat from outdoors to indoors; the COP > 1 does not violate energy conservation.
- Leaving a refrigerator door open in a room does not cool the room — the heat pump cycle deposits Q_H into the room, warming it.

## Explainer

A refrigerator seems to defy intuition: it keeps food cold even in a warm kitchen, and a heat pump warms a house in winter by extracting energy from frigid outdoor air. Neither device creates or destroys energy — both exploit the reversibility of thermodynamic cycles. The key insight is that a **heat engine run in reverse** becomes a refrigerator or heat pump.

Recall from your study of heat engines that a forward cycle takes heat Q_H from a hot reservoir, converts some fraction to work W, and dumps waste heat Q_C = Q_H − W to a cold reservoir. Now reverse every energy flow. A **refrigerator** uses input work W to pump heat Q_C from a cold reservoir (the food compartment) to a hot one (the kitchen). Energy is conserved: Q_H = Q_C + W is deposited into the hot reservoir. The **coefficient of performance** COP_R = Q_C / W measures the heat removed per unit of work input. A typical household refrigerator has COP_R ≈ 2–4: it removes 2–4 joules of heat for every joule of electrical work. This exceeds 1 without violating energy conservation because the refrigerator is not creating energy — it is moving energy downhill (thermodynamically) and we are merely paying for the "pumping" cost.

A **heat pump** runs the identical cycle but the goal is delivering heat to the warm side rather than removing it from the cold side. In winter, a heat pump extracts heat from outdoor air (even at −10°C, there is substantial thermal energy available) and delivers it at a higher temperature to your living space. COP_HP = Q_H / W = (Q_C + W) / W = COP_R + 1, which is always greater than 1 and typically reaches 3–5 in practice. Compare this to electric resistance heating, where COP = 1 by definition — every joule of electricity produces exactly one joule of heat. A heat pump is 3–5× more efficient because it moves heat rather than converting electricity into heat directly. The theoretical maximum is the **Carnot COP**: COP_max = T_C / (T_H − T_C) for a refrigerator, which increases as the temperature difference narrows. This is why ground-source heat pumps outperform air-source pumps in extreme cold: the ground stays at ~10°C year-round, providing a warmer source and a smaller T_H − T_C.

The conceptual unification of refrigerators, heat pumps, and air conditioners as variants of the same reversed Carnot cycle — governed by the same energy bookkeeping Q_H = Q_C + W — is one of the most practical payoffs of thermodynamic reasoning. The same physical device switching from heating mode to cooling mode (as air conditioners do in reverse) is not a coincidence: it is the same thermodynamic cycle with the "useful output" side toggled. Both the COP > 1 of a heat pump and the warming of a room by an open refrigerator follow directly from this single energy conservation relation.
