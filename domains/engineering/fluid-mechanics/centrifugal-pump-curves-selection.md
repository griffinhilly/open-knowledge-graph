---
id: centrifugal-pump-curves-selection
title: Centrifugal Pump Performance Curves and System Selection
domain: engineering
course: fluid-mechanics
prerequisites:
- id: mechanical-energy-balance-pump-turbine
  type: hard
builds-toward:
- pump-system-matching-operating-point
tags:
- pumps
- performance
- head-capacity
stage: advanced
status: draft
---

# Centrifugal Pump Performance Curves and System Selection

## Core Idea
Pump manufacturers provide head-capacity curves (H vs. Q), efficiency curves, and power curves for specific pump models at rated speed. A pump operates at the intersection of its characteristic curve with the system resistance curve. Understanding pump curves enables prediction of operating flow rate and head, efficiency, and power consumption under different system conditions.

## Questions

```yaml
- question: "An existing piping system requires 400 GPM and is served by a single pump at its design point. To increase flow to 600 GPM without changing the piping, you consider adding a second identical pump. Should you add it in series or in parallel?"
  type: multiple-choice
  options:
    - "In series — series pumps add their flow rates, so two pumps give 800 GPM"
    - "In parallel — parallel pumps add their heads, doubling the pressure and forcing more flow through the system"
    - "In parallel — parallel pumps add their flow rates at the same head, shifting the combined H-Q curve to higher flows"
    - "In series — series pumps add their heads, and higher head is always needed for higher flow"
  answer: 2
  explanation: "Pumps in parallel add flow rates at the same head — the combined H-Q curve is the horizontal sum of the individual curves. When the combined curve intersects the unchanged system curve, the new operating point is at a higher flow rate. Pumps in series add heads at the same flow rate, appropriate when you need more head (e.g., to overcome additional elevation or friction) rather than more flow. Since the piping hasn't changed, parallel is the correct approach."

- question: "A pump H-Q curve shows 100 ft of head at zero flow and 60 ft at 500 GPM. The system curve requires 60 ft at 500 GPM. Where will the pump actually operate?"
  type: multiple-choice
  options:
    - "At shutoff head (100 ft, 0 GPM) because that is where the pump delivers maximum head"
    - "At 500 GPM and 60 ft — the intersection of the pump curve and the system curve"
    - "At the best efficiency point, regardless of the system curve"
    - "At maximum flow, where the pump curve crosses zero head"
  answer: 1
  explanation: "The operating point is always the intersection of the pump H-Q curve and the system curve — the unique combination where both are simultaneously satisfied. Here, the pump delivers 60 ft at 500 GPM and the system requires exactly 60 ft at 500 GPM, so that is the operating point. The pump does not 'choose' the BEP — the BEP is a property of the pump design, not a constraint that overrides the system curve."

- question: "The best efficiency point (BEP) is the flow rate at which a centrifugal pump converts shaft power to fluid head with maximum efficiency."
  type: true-false
  answer: true
  explanation: "The BEP is the design point where hydraulic, volumetric, and mechanical losses are minimized together, yielding the highest ratio of hydraulic power output to shaft power input. Operating away from BEP causes internal recirculation, increased turbulence, and additional mechanical stress. Selecting a pump so the expected operating point falls near the BEP is essential for both reliability and energy cost."

- question: "Adding two identical pumps in parallel doubles the head available to the system at any given flow rate."
  type: true-false
  answer: false
  explanation: "Pumps in parallel add their flow rates at the same head — the combined H-Q curve is the horizontal sum of the individual curves. At any given head, the combined pair can deliver twice the flow of one pump. Doubling the head at the same flow requires pumps in series (vertical sum of curves). Confusing series and parallel is one of the most common errors in pump system design."

- question: "What is the system curve, and how does it interact with the pump H-Q curve to determine the actual operating flow rate and head?"
  type: short-answer
  answer: "The system curve describes how much head is required to push flow through the piping system at every possible flow rate: H_system = H_static + R·Q², where H_static is the fixed head from elevation and pressure differences, and R·Q² captures friction losses that scale with the square of flow. When plotted on the same axes as the pump H-Q curve, the operating point is their intersection — the only flow rate and head at which the pump's output exactly matches what the system demands."
  explanation: "The intersection is a self-regulating equilibrium. If the pump produced more head than the system needed at some flow, the excess would accelerate fluid to higher flow rates until balance is reached. If it produced less, flow would decelerate to lower rates. The intersection is stable — the system naturally finds it. This is why you cannot simply 'select' an arbitrary operating point; it is determined by the physics of both the pump and the piping system together."
```

## Explainer

From the mechanical energy balance, you know that a pump adds head to a fluid and that the energy equation governs what head is required to move fluid from one point to another. A real pump cannot deliver arbitrary combinations of head and flow — its performance is characterized by a **head-capacity curve** (H–Q curve), which shows how much head the pump produces at each possible flow rate.

The H–Q curve has a characteristic shape: maximum head at zero flow (the **shutoff head**) and falling head as flow increases. This makes physical sense — the impeller is most effective at lifting fluid when nothing is flowing and progressively less effective as flow rate demands more energy to move fluid through the passages. Along with the H–Q curve, the manufacturer provides efficiency and **brake horsepower** (BHP) curves. The efficiency curve peaks at the **best efficiency point (BEP)** — the design condition where the pump converts shaft power to hydraulic energy most effectively. Operating far from BEP causes recirculation, vibration, and accelerated wear, which is why selecting a pump with the BEP near your design flow rate matters for reliability as much as for energy cost.

The **system curve** is the other half of the picture. The mechanical energy balance tells you that the head required to push flow through a piping system increases with flow rate — typically as H_system = H_static + R·Q², where H_static is the elevation and pressure difference to overcome and the R·Q² term captures friction and minor losses (which scale approximately with the square of velocity, hence Q²). Plotting the system curve and pump H–Q curve together on the same axes, the **operating point** is their intersection — the only combination of H and Q where both the pump and the system are simultaneously satisfied.

Pump selection means choosing a pump whose H–Q curve intersects the system curve at or near the BEP for the desired design flow rate. If the system needs 500 GPM at 80 ft of head, you need a pump whose curve passes through that point at good efficiency. If you need more flow than one pump can provide, pumps in **parallel** add their flow rates at the same head — the combined H–Q curve is the horizontal sum of the individual curves. If you need more head than one pump can provide, pumps in **series** add heads at the same flow rate — the combined curve is the vertical sum. In both cases, the combined curve intersects the system curve at the new operating point, which you read off to find the actual delivered flow and head.
