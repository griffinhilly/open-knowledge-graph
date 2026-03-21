---
id: turbine-staging-multistage
title: Multistage Turbine Design and Reheat
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: polytropic-efficiency-real-machinery
  type: hard
- id: rankine-cycle-thermodynamic-analysis
  type: soft
builds-toward:
- rankine-cycle-reheat-regeneration
- brayton-cycle-intercooling-reheating
tags:
- turbine
- multistage
- reheat
- expansion-ratio
- power-output
stage: advanced
status: draft
---

# Multistage Turbine Design and Reheat

## Core Idea
Multistage turbines with intermediate reheat maximize power output by preventing excessive moisture formation in the final stages. Reheat between stages restores enthalpy and increases turbine work. Optimal staging distributes entropy generation such that final conditions remain in the two-phase region while meeting metallurgical temperature limits.

## Questions

```yaml
- question: "A single-stage steam turbine expands from 10 MPa to condenser pressure (10 kPa). The principal mechanical failure risk in the final stages of this turbine is:"
  type: multiple-choice
  options:
    - "Thermal creep and failure of superalloy blades due to sustained high temperature at the inlet"
    - "Liquid droplet erosion of turbine blades as steam enters the two-phase region during expansion"
    - "Compressor surge caused by excessive pressure ratio across a single stage"
    - "Acoustic resonance in the blade passages due to high-velocity steam"
  answer: 1
  explanation: "As steam expands over a large pressure ratio, the isentropic expansion path crosses into the two-phase (wet steam) region on the Mollier diagram. Liquid droplets in high-velocity steam act like sand — they erode blade surfaces catastrophically. A maximum moisture content of about 10–12% (quality ≥ 0.88) is the standard design constraint. This moisture erosion problem, not thermal limits, is the primary reason single-stage expansion over large pressure ratios is impractical for large turbines."

- question: "In a two-stage turbine with intermediate reheat, why does the total turbine work output increase compared to a single-stage turbine with the same inlet and exhaust conditions?"
  type: multiple-choice
  options:
    - "Reheating reduces friction losses between the two stages, recovering otherwise wasted energy"
    - "Reheating adds enthalpy back into the steam at intermediate pressure, and that additional enthalpy is converted to work in the second stage"
    - "The second stage operates at higher efficiency because steam enters it at a lower pressure"
    - "Reheating reduces the entropy increase, making the overall process closer to isentropic"
  answer: 1
  explanation: "Reheat adds heat to the steam between stages, raising its enthalpy (moving up and right on the Mollier diagram). This additional enthalpy is then available for conversion to work in the second turbine stage. The total work output equals the sum of enthalpy drops across both stages — and adding enthalpy between stages directly increases the second-stage enthalpy drop. Reheat also raises the mean temperature at which heat is added to the cycle, improving thermodynamic efficiency by approaching the Carnot ideal more closely."

- question: "Reheat in a multistage turbine serves two distinct purposes: preventing excessive moisture in low-pressure stages and increasing total work output."
  type: true-false
  answer: true
  explanation: "Both benefits are real and physically distinct. First, reheat restores the steam to a superheated state before entering the next stage, moving the expansion path rightward and upward on the Mollier diagram so that the final exhaust quality stays above the ~88% erosion threshold. Second, the added heat (enthalpy) at intermediate pressure is converted to additional shaft work in the subsequent stages, increasing total power output. These are complementary benefits — reheat simultaneously protects the hardware and improves cycle performance."

- question: "The primary purpose of reheat in a multistage turbine is to reduce the total heat input to the cycle, thereby improving thermal efficiency."
  type: true-false
  answer: false
  explanation: "Reheat actually increases total heat input to the cycle — you add fuel energy in the reheater(s) in addition to the main boiler. The efficiency improvement (when it occurs) comes not from reduced heat input but from the higher mean temperature at which that heat is added: adding heat at intermediate pressure is thermodynamically superior to the alternative of letting that steam expand wet and losing both blade integrity and work potential. The Carnot framework shows that efficiency improves when heat addition occurs at higher average temperature — reheat moves heat addition higher on the temperature scale."

- question: "On a Mollier (h-s) diagram, trace what reheat does to the expansion path and explain why this is desirable from both a mechanical and thermodynamic standpoint."
  type: short-answer
  answer: "In a single-stage expansion from high pressure to condenser pressure, the expansion path descends steeply into the two-phase (wet) region — moisture forms and erodes blades. With reheat, the first stage expands partway (path goes down-right), then reheat adds enthalpy while holding pressure constant (path moves straight up, back into the superheated region), and the second stage expands the rest of the way (another down-right path). Mechanically, keeping the path in the superheated region prevents liquid droplet formation. Thermodynamically, adding heat at a higher temperature (the reheat pressure) raises the mean temperature of heat addition, increasing cycle efficiency toward the Carnot ideal."
  explanation: "On the Mollier diagram, constant-pressure lines slope upward to the right. Reheating at constant intermediate pressure moves the state point vertically upward to higher enthalpy and slightly higher entropy. The subsequent expansion resumes from this higher enthalpy point, producing more work per unit mass (larger enthalpy drop) before reaching condenser conditions — and arriving at higher quality (less moisture) than without reheat. The two benefits — moisture avoidance and work increase — are both visible as the two-segment expansion path remaining above the saturation dome."
```

## Explainer

From the Rankine cycle and your study of polytropic efficiency, you know that real turbines suffer from irreversibility: entropy increases as steam expands, and the actual work output is less than the isentropic ideal. For a large pressure ratio — say, expanding from 10 MPa to 10 kPa — a single turbine stage faces a severe problem: by the time the steam reaches low pressure, the expansion trajectory crosses deep into the two-phase (liquid-vapor) region. Liquid droplets in high-speed steam erode turbine blades catastrophically. Multistage design with reheat solves this by intercepting the expansion before it gets wet.

In a **multistage turbine with reheat**, steam expands through a high-pressure (HP) turbine stage, doing work. When the steam temperature has dropped to near saturation, it exits and returns to a **reheater** — a heat exchanger that restores the steam to a high temperature (often back to the original turbine inlet temperature). The reheated steam then enters an intermediate-pressure (IP) or low-pressure (LP) turbine and expands again. This cycle can repeat. Each reheat stage adds heat at an intermediate pressure, which on the h-s (Mollier) diagram shifts the expansion path rightward (toward higher entropy) and upward (higher enthalpy), keeping the steam well within the superheated region for most of the expansion.

The benefit is twofold. First, **moisture is avoided**: the final turbine exhaust quality stays above roughly 88–90% (typically required to prevent blade erosion), even for large overall pressure ratios. Second, **total turbine work increases**: reheating adds enthalpy back into the cycle at intermediate pressure, and that additional enthalpy is converted to additional work output in the subsequent stages. The net plant efficiency often improves as well, because the reheat raises the mean temperature at which heat is added to the cycle — closer to the Carnot ideal of adding all heat at the highest possible temperature.

The engineering tradeoffs in staging design are: how many stages to use, at what pressure to reheat, and to what temperature. More stages yield diminishing returns in efficiency while adding capital cost and complexity. The optimal reheat pressure for a two-reheat cycle is roughly the geometric mean of inlet and exhaust pressures for equal work split. Metallurgical limits cap reheat temperatures — today's advanced superalloys allow inlet temperatures around 650°C, with future targets pushing higher. Understanding staging from a thermodynamic perspective directly informs the more complex Rankine cycle configurations (regeneration + reheat) and the analogous intercooled-reheat Brayton cycles used in gas turbines.
