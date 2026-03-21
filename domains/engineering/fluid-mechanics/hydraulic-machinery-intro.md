---
id: hydraulic-machinery-intro
title: 'Hydraulic Machinery: Pumps and Turbines'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: bernoullis-equation
  type: hard
- id: pipe-system-losses
  type: soft
- id: dimensional-analysis-and-similarity
  type: soft
- id: control-volume-momentum
  type: soft
tags:
- pumps
- turbines
- pump curve
- system curve
- specific speed
- NPSH
stage: advanced
status: validated
---
# Hydraulic Machinery: Pumps and Turbines

## Core Idea
Pumps add energy to a fluid; turbines extract it. The operating point of a pump-system combination is found at the intersection of the pump head-flow curve (H-Q curve) and the system curve (which includes static head plus friction losses as a function of Q). Similarity laws (affinity laws) — derived from dimensional analysis — relate pump performance at different speeds: Q∝N, H∝N², Power∝N³. Net Positive Suction Head (NPSH) must be checked to prevent cavitation at the pump inlet.

## How It's Best Learned
Plot a pump H-Q curve and a system curve on the same axes; the intersection is the operating point. Apply affinity laws to determine the effect of changing pump speed. Calculate NPSH available vs. required to identify cavitation risk, adjusting inlet pipe geometry as needed.

## Common Misconceptions
- A pump curve shows head produced at each flow rate, not what the pump delivers to the fluid regardless of the system — the actual operating point depends on both curves.
- Cavitation occurs when local pressure drops below vapor pressure, causing bubble collapse that damages impellers — it is not just 'boiling' but a damaging collapse event.
- Specific speed is a dimensionless (or quasi-dimensional) design parameter that categorizes pump type (centrifugal, mixed-flow, axial); it is evaluated at the best efficiency point, not at arbitrary conditions.

## Questions

```yaml
- question: "A pump is rated at 25 m of head at 8 L/s on its H-Q curve. The system requires 10 m of static head plus friction losses of 0.3·Q² meters (with Q in L/s). At what flow rate does this pump-system combination operate?"
  type: multiple-choice
  options:
    - "8 L/s — the pump always delivers its rated flow regardless of the system"
    - "The operating point must be found graphically or algebraically; it is where the pump head equals the system head demand, not necessarily at the rated point"
    - "0 L/s — the static head of 10 m exceeds the pump's shutoff head"
    - "The pump cannot operate because its rated head (25 m) is too high for the system"
  answer: 1
  explanation: "The operating point is not a property of the pump alone — it is the intersection of the pump H-Q curve with the system curve. The pump 'wants' to deliver various combinations of head and flow (defined by its curve); the system 'demands' more head as flow increases (static head + friction losses ∝ Q²). The actual flow rate is where supply equals demand: pump head = system head. This may or may not coincide with the pump's rated or best-efficiency point. Option A captures the most common misconception: students think the pump determines flow unilaterally, ignoring that the system curve constrains the operating point."

- question: "A pump running at 1200 RPM consumes 80 kW. The operator uses a variable-frequency drive to reduce speed to 960 RPM. Approximately how much power does the pump now consume?"
  type: multiple-choice
  options:
    - "64 kW — power scales linearly with speed (960/1200 × 80)"
    - "51.2 kW — power scales as the square of the speed ratio ((960/1200)² × 80)"
    - "40.96 kW — power scales as the cube of the speed ratio ((960/1200)³ × 80)"
    - "80 kW — power is determined by the system demand, not the pump speed"
  answer: 2
  explanation: "The affinity laws state P ∝ N³. Speed ratio = 960/1200 = 0.8. New power = 80 × (0.8)³ = 80 × 0.512 = 40.96 kW. This cubic relationship is why variable-speed drives are so effective for energy savings: a modest speed reduction produces a dramatic power reduction. A 20% speed reduction cuts power consumption by nearly 49%. Option A (linear) and B (square) represent common partial-knowledge errors — students sometimes remember that Q ∝ N or H ∝ N² but forget the correct exponent for power."

- question: "The operating point of a pump-piping system is determined solely by the pump's H-Q curve — it is the flow rate at which the pump reaches its maximum efficiency."
  type: true-false
  answer: false
  explanation: "The operating point is determined by the intersection of two curves: the pump's H-Q curve (head supplied vs. flow) and the system curve (head demanded vs. flow). Neither curve alone determines the operating point. The system curve depends on static head (elevation difference) and dynamic losses (pipe friction, fittings), both of which are properties of the piping system, not the pump. Maximum efficiency is a property of the pump curve and may or may not coincide with the operating point — good system design tries to match them, but they are conceptually distinct."

- question: "Reducing pump speed by 20% reduces power consumption by approximately 49%, because pump power scales as the cube of the speed ratio."
  type: true-false
  answer: true
  explanation: "By the affinity law P ∝ N³: P₂/P₁ = (N₂/N₁)³ = (0.8)³ = 0.512. So the new power is 51.2% of the original — a reduction of 48.8%, approximately 49%. This cubic law is the quantitative basis for variable-speed drive energy savings. It also means the effect is asymmetric: a 20% speed increase multiplies power by (1.2)³ = 1.728, a 73% increase. Understanding this scaling is essential for energy-efficient pump selection and operation."

- question: "Explain what cavitation is, why it damages pump impellers, and what conditions at the pump inlet cause it to occur."
  type: short-answer
  answer: "Cavitation occurs when local pressure in the pump inlet drops below the liquid's vapor pressure, causing the liquid to locally vaporize and form vapor bubbles. These bubbles are carried into higher-pressure regions of the impeller where they collapse violently, generating micro-shock waves that erode the impeller surface over time. The result is noise, vibration, reduced performance, and progressive mechanical damage. NPSH_available = (absolute inlet pressure head) − (vapor pressure head) quantifies the margin before cavitation. Cavitation occurs when NPSH_available falls below NPSH_required (the manufacturer's threshold). NPSH_available decreases with: high pump elevation above liquid source (increases suction lift), high suction pipe friction losses, high liquid temperature (increases vapor pressure), and high altitude operation (lower atmospheric pressure)."
  explanation: "Cavitation is not simply 'boiling' — the collapse event is the damaging mechanism. Bubbles form in low-pressure zones and collapse in nanoseconds when they reach higher pressure, releasing energy that locally exceeds the yield strength of even hardened steel. Preventing it requires keeping NPSH_available > NPSH_required with a safety margin, which constrains pump placement, inlet pipe sizing, and operating conditions."
```

## Explainer

Bernoulli's equation tells you that energy per unit weight of fluid — called **head** — can be expressed as a sum of pressure head, velocity head, and elevation head. A pump's job is to add head to the flow; a turbine's job is to extract it. The **H-Q curve** (pump characteristic curve) shows how much head a centrifugal pump delivers at each flow rate: at zero flow, head is maximum (the shutoff head); as flow increases, head decreases because more energy is lost overcoming internal flow velocities. This inverse relationship is the fundamental shape of every centrifugal pump curve.

The **system curve** represents what the system demands: it is the sum of static head (the fixed elevation difference the pump must overcome regardless of flow) and dynamic head losses (pipe friction, fittings, valves — all of which scale approximately as Q²). The system curve always starts at the static head value and rises parabolically. Where these two curves intersect is the **operating point** — the one flow rate and head at which supply exactly meets demand. If you increase flow demand (open a valve), the system curve flattens, the operating point shifts right, and the pump delivers more flow at lower head. This graphical intersection method is the core tool for pump-system design.

The **affinity laws**, derived from dimensional analysis and similarity, are among the most useful rules in fluid machinery. When you change pump speed from N₁ to N₂: flow scales as Q ∝ N, head scales as H ∝ N², and power scales as P ∝ N³. The cubic relationship between power and speed is why variable-speed drives save so much energy — reducing pump speed by 20% reduces power consumption by nearly 50%. The same laws apply to geometrically similar pumps of different sizes (scaled by diameter), making them invaluable for selecting among a family of impeller sizes.

**Net Positive Suction Head (NPSH)** connects directly to cavitation. NPSH_available is the absolute pressure at the pump inlet expressed as head, minus the vapor pressure head of the liquid — it tells you how much pressure margin exists before cavitation. NPSH_required is specified by the pump manufacturer based on testing; it represents the margin the pump needs to avoid internal cavitation. The design rule is simply NPSH_available > NPSH_required with some safety factor. NPSH_available decreases when the pump is positioned high above the liquid source, when suction pipe losses are large, when liquid temperature is high (increasing vapor pressure), or when operating at high altitude. Every pump installation must verify this inequality before commissioning.
