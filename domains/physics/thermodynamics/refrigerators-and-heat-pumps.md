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
