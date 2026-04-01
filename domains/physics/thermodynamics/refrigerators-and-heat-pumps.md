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

## Questions

```yaml
- question: "A heat pump has COP_HP = 4. For every 1 joule of electrical work input, how many joules of heat are delivered to the warm space?"
  type: multiple-choice
  options:
    - "1 joule — the same as direct electric resistance heating"
    - "3 joules — equal to the heat extracted from the cold source"
    - "4 joules — equal to COP_HP × work input"
    - "5 joules — the sum of work input and heat extracted from the cold source"
  answer: 2
  explanation: "By definition, COP_HP = Q_H / W, so Q_H = COP_HP × W = 4 × 1 = 4 joules. Energy conservation confirms this: Q_H = Q_C + W, so Q_C = 3 joules were extracted from the cold reservoir. Option A describes resistance heating (COP = 1). Option B is Q_C — the heat removed from outdoors, not what is delivered indoors. Option D (5 joules) would violate energy conservation."

- question: "You leave a refrigerator door wide open in a perfectly sealed room for several hours. The net effect on the room's temperature is:"
  type: multiple-choice
  options:
    - "The room cools down, because the refrigerator is constantly removing heat from the air"
    - "The room temperature stays the same, since the refrigerator just moves heat within the room"
    - "The room warms up, because the refrigerator's motor continuously adds electrical energy to the room as heat"
    - "The room first cools, then returns to its original temperature at equilibrium"
  answer: 2
  explanation: "The refrigerator uses electrical work W to move Q_C from the compartment to the kitchen, depositing Q_H = Q_C + W into the room. With the door open, compartment and room temperatures equalize, but the motor keeps running, continuously injecting W joules of electrical energy into the room as heat. The sealed room warms because Q_H = Q_C + W always exceeds Q_C — the room receives more heat than the refrigerator removes from the air. This follows directly from energy conservation."

- question: "A heat pump with COP_HP = 3 can deliver 3 joules of heat per joule of electrical work without violating energy conservation, because it moves thermal energy from a cold source rather than creating it."
  type: true-false
  answer: true
  explanation: "COP > 1 is not magic — the heat pump extracts Q_C = 2 joules from cold outdoor air and adds the 1 joule of work, delivering Q_H = 3 joules. Energy is conserved: 2 (from outdoors) + 1 (electrical) = 3 (delivered). The 'extra' heat comes from the outdoor thermal reservoir, which loses energy in the process. No energy is created; it is relocated from cold to warm with mechanical assistance."

- question: "The coefficient of performance of a refrigerator or heat pump cannot exceed 1, because no device can deliver more energy output than it consumes."
  type: true-false
  answer: false
  explanation: "COP can greatly exceed 1, and this does not violate energy conservation. A refrigerator's useful output Q_C can exceed work W because additional energy Q_C comes from the thermal reservoir being cooled. For a heat pump, Q_H = Q_C + W > W always, so COP_HP > 1 always. Real heat pumps routinely achieve COP of 3–5. The first law is satisfied because energy is conserved across the entire system — the cold reservoir loses Q_C."

- question: "Why can a heat pump deliver more heat energy to a building than the electrical energy it consumes, without violating the first law of thermodynamics?"
  type: short-answer
  answer: "A heat pump doesn't create energy — it moves it. The electrical work W drives a thermodynamic cycle that extracts heat Q_C from a cold outdoor source and delivers the combined Q_H = Q_C + W to the building. The 'extra' heat comes from the outdoor thermal reservoir, which loses that energy. Energy is conserved: Q_C (from outdoors) + W (electricity) = Q_H (delivered indoors). The efficiency advantage over resistance heating arises because the device transports existing thermal energy rather than converting electricity directly into heat."
  explanation: "Analogy: a water pump delivers more water to a height than the energy put into the pump — the rest was already there; you paid only for the pumping. Similarly, a heat pump delivers more thermal energy than your electricity bill covers — you paid for the thermodynamic pumping of heat from cold to warm, while the rest came from the outdoor air for free."
```

## Explainer

A refrigerator seems to defy intuition: it keeps food cold even in a warm kitchen, and a heat pump warms a house in winter by extracting energy from frigid outdoor air. Neither device creates or destroys energy — both exploit the reversibility of thermodynamic cycles. The key insight is that a **heat engine run in reverse** becomes a refrigerator or heat pump.

Recall from your study of heat engines that a forward cycle takes heat Q_H from a hot reservoir, converts some fraction to work W, and dumps waste heat Q_C = Q_H − W to a cold reservoir. Now reverse every energy flow. A **refrigerator** uses input work W to pump heat Q_C from a cold reservoir (the food compartment) to a hot one (the kitchen). Energy is conserved: Q_H = Q_C + W is deposited into the hot reservoir. The **coefficient of performance** COP_R = Q_C / W measures the heat removed per unit of work input. A typical household refrigerator has COP_R ≈ 2–4: it removes 2–4 joules of heat for every joule of electrical work. This exceeds 1 without violating energy conservation because the refrigerator is not creating energy — it is moving energy downhill (thermodynamically) and we are merely paying for the "pumping" cost.

A **heat pump** runs the identical cycle but the goal is delivering heat to the warm side rather than removing it from the cold side. In winter, a heat pump extracts heat from outdoor air (even at −10°C, there is substantial thermal energy available) and delivers it at a higher temperature to your living space. COP_HP = Q_H / W = (Q_C + W) / W = COP_R + 1, which is always greater than 1 and typically reaches 3–5 in practice. Compare this to electric resistance heating, where COP = 1 by definition — every joule of electricity produces exactly one joule of heat. A heat pump is 3–5× more efficient because it moves heat rather than converting electricity into heat directly. The theoretical maximum is the **Carnot COP**: COP_max = T_C / (T_H − T_C) for a refrigerator, which increases as the temperature difference narrows. This is why ground-source heat pumps outperform air-source pumps in extreme cold: the ground stays at ~10°C year-round, providing a warmer source and a smaller T_H − T_C.

The conceptual unification of refrigerators, heat pumps, and air conditioners as variants of the same reversed Carnot cycle — governed by the same energy bookkeeping Q_H = Q_C + W — is one of the most practical payoffs of thermodynamic reasoning. The same physical device switching from heating mode to cooling mode (as air conditioners do in reverse) is not a coincidence: it is the same thermodynamic cycle with the "useful output" side toggled. Both the COP > 1 of a heat pump and the warming of a room by an open refrigerator follow directly from this single energy conservation relation.
