---
id: transient-climate-response
title: Transient Climate Response to Forcing
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: equilibrium-climate-sensitivity
  type: hard
- id: climate-models-and-projections
  type: hard
- id: marine-heat-content-and-thermal-inertia
  type: soft
builds-toward:
- climate-models-and-projections
- sea-level-change
tags:
- climate-response
- transient
- heat-uptake
- near-term-warming
stage: advanced
status: validated
---

# Transient Climate Response to Forcing

## Core Idea
Transient Climate Response (TCR) is the temperature change during a period of rising CO₂ (e.g., when CO₂ doubles exponentially), accounting for incomplete ocean heat uptake. TCR (~1.8°C for doubled CO₂) is less than ECS (~3°C) because the deep ocean has not yet warmed. TCR is more relevant for near-term (next century) projections. The difference between TCR and ECS depends on ocean heat uptake efficiency, which varies across climate models and is uncertain.

## Questions

```yaml
- question: "Atmospheric CO₂ has been rising for decades. According to the TCR/ECS framework, which statement best describes the current state of global surface temperatures?"
  type: multiple-choice
  options:
    - "Surface temperatures have already risen by the full ECS value (~3°C above pre-industrial), since forcing has been applied for over a century."
    - "Surface temperatures have risen by roughly the transient response (less than ECS), with additional committed warming still in the pipeline because the deep ocean has not yet equilibrated."
    - "Surface temperatures will not change meaningfully until CO₂ stops rising, after which ECS warming occurs instantaneously."
    - "TCR and ECS are numerically identical, so the distinction doesn't affect current temperature predictions."
  answer: 1
  explanation: "We are in the transient regime: CO₂ is still rising, the deep ocean is still absorbing heat, and the surface has not yet warmed to its eventual equilibrium. The observed warming to date reflects the transient response — less than ECS because ocean thermal inertia has absorbed a fraction of the energy imbalance. The gap between current observed warming and ECS represents 'committed' or 'pipeline' warming: even if emissions stopped today, temperatures would continue rising for decades to centuries as the ocean slowly equilibrates. This is why TCR better describes near-term observations while ECS describes ultimate outcomes."

- question: "A climate model has very vigorous deep-ocean heat transport. Compared to a model with sluggish deep-ocean mixing, how would this model's TCR relate to its ECS?"
  type: multiple-choice
  options:
    - "TCR would be closer to ECS, because efficient mixing transports surface heat downward and returns it quickly, reducing the lag."
    - "TCR would be further below ECS, because efficient deep mixing shuttles more heat into the deep ocean, keeping the surface temporarily cooler during the transient period."
    - "TCR and ECS are determined by atmospheric feedbacks alone; ocean mixing affects neither."
    - "ECS would be lower in this model, because efficient mixing dissipates heat before feedbacks can amplify it."
  answer: 1
  explanation: "Ocean heat uptake efficiency is the key variable governing the TCR-ECS gap. A model with vigorous deep-ocean mixing rapidly transports heat from the surface mixed layer into the deep interior. This efficient heat removal keeps the surface cooler than it would otherwise be during the transient period, producing a TCR well below ECS. Conversely, a model with sluggish deep mixing keeps more heat at the surface, causing faster surface warming and a TCR closer to ECS. This is one of the dominant sources of spread across climate models and a major reason TCR is uncertain."

- question: "If global CO₂ emissions stopped today, some additional surface warming would still occur over the coming decades because the deep ocean has not yet fully equilibrated with the current energy imbalance."
  type: true-false
  answer: true
  explanation: "This 'committed warming' or 'warming in the pipeline' is a direct consequence of the ocean's enormous heat capacity. Even at current CO₂ concentrations, Earth's energy budget is out of balance — more energy is entering the system than leaving. The deep ocean is gradually absorbing this excess, but it does so slowly. Until the ocean equilibrates with the current forcing, surface temperatures will continue to rise even without further emissions. Estimates suggest 0.3–0.5°C of additional committed warming is already locked in from past and present emissions."

- question: "TCR is generally a better predictor of long-term climate consequences than ECS, because TCR is derived from observations rather than theoretical models."
  type: true-false
  answer: false
  explanation: "TCR and ECS serve different purposes — neither is universally 'better.' TCR is more useful for near-term projections (next 50–100 years) because it describes the transient warming we actually experience while emissions continue. ECS is essential for long-term consequences: it captures the full committed warming, including the centuries-long tail of ocean heat uptake that will unfold even after emissions cease. TCR systematically underestimates ultimate consequences, while ECS overestimates near-term change. Policy decisions on different timescales need both numbers."

- question: "Explain why TCR is always less than ECS, and what this implies about the difference between near-term observed warming and the long-term committed warming."
  type: short-answer
  answer: "TCR is less than ECS because the deep ocean acts as a thermal buffer during the transient period. ECS is defined as the eventual surface warming after the entire climate system — including the deep ocean — fully equilibrates with doubled CO₂. But equilibration of the deep ocean takes centuries to millennia. TCR measures warming at the moment CO₂ doubles (after ~70 years of 1%/year rise), when the ocean has absorbed only part of the committed heat. The difference between TCR (~1.8°C) and ECS (~3°C) represents warming that is physically committed — it will eventually occur — but is currently 'hidden' in the ocean's heat capacity. This gap means near-term observed warming underestimates the full long-term consequences of today's atmospheric CO₂ concentrations."
  explanation: "The ocean's delayed response creates a fundamental asymmetry in climate change: the forcing (CO₂) acts quickly on geological timescales, but the full temperature response unfolds over much longer periods as heat slowly penetrates the deep ocean. TCR captures what we observe on human timescales; ECS captures what we have committed to on civilizational timescales. The 'pipeline warming' between them is not hypothetical — it is physically guaranteed by the energy imbalance already present in the Earth system and is observable in ocean heat content measurements."
```

## Explainer

You already understand **equilibrium climate sensitivity** (ECS) — the eventual warming after CO₂ doubles and the climate system fully adjusts. But "fully adjusts" is doing enormous work in that definition. The deep ocean takes centuries to millennia to reach thermal equilibrium with a new forcing. On the timescales that matter for policy — decades to a century — the climate system is still catching up. **Transient Climate Response** (TCR) measures how much warming actually occurs while CO₂ is still rising, before the slow ocean has finished absorbing heat.

The standard definition uses a specific thought experiment: CO₂ increases at 1% per year (compounding) until it doubles, which takes about 70 years. TCR is the global mean surface temperature change at the moment of doubling. Because the deep ocean is still absorbing heat at that point — acting as a thermal buffer — TCR is always less than ECS. Current best estimates place TCR around 1.8°C compared to ECS around 3°C. The gap between them reflects how much warming is "in the pipeline" — committed but not yet realized because ocean thermal inertia delays the surface temperature response. From your understanding of ocean heat content, you can see why this matters: the ocean's enormous heat capacity means it takes decades to warm, and until it does, the surface stays cooler than it ultimately will.

The quantity that governs how large the TCR-ECS gap is called **ocean heat uptake efficiency** — how effectively the ocean transports heat from the surface mixed layer into the deep interior. Models with vigorous deep-ocean mixing have high heat uptake efficiency: they shuttle more heat downward, keeping the surface temporarily cooler and producing a lower TCR relative to their ECS. Models with sluggish deep mixing warm the surface faster, yielding TCR closer to ECS. This is one of the largest sources of spread across climate models, because ocean mixing involves turbulent processes at scales far below what models resolve directly.

For near-term climate projections — the next 50 to 100 years — TCR is more useful than ECS precisely because we live in the transient regime. The world is not waiting for equilibrium; emissions continue to rise, and what we experience is the transient response. TCR connects more directly to observable quantities: it can be estimated from the historical record of warming and forcing, making it better constrained by data than ECS. However, TCR underestimates the full consequences of today's emissions, because the committed warming embedded in ocean heat uptake will continue to emerge for centuries even if emissions stop. Understanding both TCR and ECS is essential — TCR tells you what happens soon, ECS tells you what you have locked in.
