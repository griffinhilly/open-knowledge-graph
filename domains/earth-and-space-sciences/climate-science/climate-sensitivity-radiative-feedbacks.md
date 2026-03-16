---
id: climate-sensitivity-radiative-feedbacks
title: Climate Sensitivity and Radiative Feedbacks
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: radiative-forcing-definition
  type: hard
- id: energy-balance-models
  type: soft
- id: radiative-transfer-atmospheric
  type: hard
- id: feedback-mechanisms-in-climate
  type: soft
builds-toward:
- climate-projections-modeling
tags:
- sensitivity
- feedback
- forcing
- response
- equilibrium
stage: advanced
status: draft
---

# Climate Sensitivity and Radiative Feedbacks

## Core Idea
Climate sensitivity is the global temperature rise per unit radiative forcing (°C per W/m² or °C per doubling CO₂), determined by radiative feedback processes. Equilibrium climate sensitivity (ECS, temperature change at CO₂ doubling after full equilibration) is ~3°C (range 2.5–4°C); transient climate response (warming before ocean adjustment) is ~1.8°C. Radiative feedbacks—quantified as feedback parameters (W/m²/°C)—describe how the climate system responds: water vapor feedback is positive (warming increases atmospheric water vapor, trapping more heat); cloud feedback is uncertain; ice-albedo feedback is positive; lapse-rate feedback is negative. The net of all feedbacks determines sensitivity.

## How It's Best Learned
Run an energy balance model with different feedback strengths and observe how equilibrium temperature responds to a forcing change. Decompose climate model warming into forcing and feedback contributions using radiative kernels.

## Common Misconceptions
Climate sensitivity is not fixed; it can vary with forcing magnitude, background climate state, and spatial patterns of warming. Also, positive feedbacks do not lead to runaway warming if the radiative forcing is finite; the system reaches equilibrium.

## Questions

```yaml
- question: "Why is equilibrium climate sensitivity (ECS) larger than the transient climate response (TCR) for the same CO₂ doubling scenario?"
  type: multiple-choice
  options: ["ECS includes fast feedbacks; TCR includes only slow feedbacks", "ECS is reached after the ocean has fully equilibrated; TCR is measured while the ocean is still absorbing heat", "ECS assumes no cloud feedback; TCR includes all feedbacks", "ECS is measured over land only; TCR is the global average"]
  answer: 1
  explanation: "The ocean has enormous heat capacity and takes centuries to equilibrate with a new forcing. TCR is measured at the moment of CO₂ doubling (typically ~70 years into a 1% per year ramp-up), when the ocean is still absorbing heat and suppressing surface warming. ECS is the warming after full ocean equilibration, so it is always larger than TCR. The ratio ECS/TCR reflects how much additional warming is 'in the pipeline' even if emissions stopped."

- question: "A positive feedback in the climate system will cause temperatures to rise without bound (runaway warming) if the feedback is strong enough."
  type: true-false
  answer: false
  explanation: "Positive feedbacks amplify warming but do not automatically cause runaway. The climate system stabilizes when the increased outgoing longwave radiation from a warmer surface restores radiative balance. Runaway warming (like Venus) requires the feedback to overwhelm this restoring force entirely — a specific condition that Earth's current state does not satisfy for finite CO₂ increases. Positive feedbacks increase climate sensitivity; they do not eliminate the equilibrium."

- question: "Explain the water vapor feedback mechanism and why it is considered a positive feedback."
  type: short-answer
  answer: "As surface temperature rises, the atmosphere holds more water vapor (following the Clausius-Clapeyron relation). Water vapor is a potent greenhouse gas, so higher concentrations absorb more outgoing infrared radiation, causing additional warming — which in turn drives more evaporation. The feedback amplifies the initial temperature perturbation."
  explanation: "Water vapor feedback roughly doubles the warming that would occur from CO₂ alone (in the absence of other feedbacks). It is the single largest positive feedback in the climate system. Crucially, water vapor is not a forcing — humans do not directly add atmospheric water vapor at climatically relevant scales — it responds to temperature, making it a feedback rather than a driver."
```

## Explainer

When scientists say that doubling atmospheric CO₂ will warm the Earth by roughly 3°C, they are invoking the concept of climate sensitivity — a single number that summarizes how strongly the climate system responds to a radiative perturbation. Understanding where that number comes from requires understanding feedbacks: the secondary responses of the climate system that amplify or dampen the initial warming.

Start with a simple energy balance. The Sun delivers a certain amount of energy to Earth's surface; Earth must radiate the same amount back to space to stay at a stable temperature. CO₂ acts as a partial blanket, reducing the efficiency of outgoing infrared radiation. If you double CO₂ overnight, the Earth initially absorbs more energy than it emits (a radiative imbalance of roughly +3.7 W/m²). The surface warms until outgoing radiation increases enough to restore balance. Without any feedbacks, this warming would be about 1°C — the "Planck response." The actual sensitivity of ~3°C means feedbacks amplify this by a factor of roughly 3.

The most important feedbacks are: **water vapor** (strongly positive — warmer air holds more water vapor, which is itself a greenhouse gas), **ice-albedo** (positive — warming melts reflective ice, exposing darker ocean and land that absorb more sunlight), **lapse-rate** (negative in the tropics — the upper troposphere warms faster than the surface, increasing outgoing radiation), and **clouds** (uncertain — low clouds cool by reflecting sunlight, high clouds warm by trapping infrared; their net response to warming is the largest source of uncertainty in climate sensitivity estimates). Each feedback is quantified as a feedback parameter λᵢ (W/m²/°C); the net climate sensitivity parameter λ = Σλᵢ determines how much warming a given forcing produces.

Equilibrium climate sensitivity (ECS) is the warming after the entire climate system — including the deep ocean — reaches a new steady state. Because the ocean has immense heat capacity, this takes centuries. Transient climate response (TCR) is the more policy-relevant quantity: it measures warming at the moment of CO₂ doubling in a scenario where CO₂ increases 1% per year. TCR is smaller than ECS because the ocean is still absorbing heat and suppressing surface warming. The difference — ECS minus TCR — represents the "committed warming" that would occur even if emissions stopped today.

A critical misconception is that positive feedbacks imply runaway warming. They do not. Runaway would require the feedback gain to exceed 1 — meaning the feedback amplification exceeds the restoring force. Earth's current sensitivity does not meet this condition for realistic CO₂ scenarios. What positive feedbacks do is increase the equilibrium temperature for a given forcing. Knowing the sign, magnitude, and uncertainty of each feedback is therefore the central goal of climate sensitivity research, and the spread in ECS estimates (2.5–4°C) largely reflects disagreement about cloud feedbacks.
