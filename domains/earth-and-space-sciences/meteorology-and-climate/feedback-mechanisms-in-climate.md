---
id: feedback-mechanisms-in-climate
title: Climate Feedback Mechanisms
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: climate-change-science
  type: hard
- id: solar-radiation-and-earth-energy-balance
  type: hard
- id: greenhouse-effect
  type: hard
- id: anthropogenic-climate-forcing
  type: soft
- id: earths-radiative-balance
  type: soft
- id: surface-energy-budget-fluxes
  type: soft
builds-toward:
- climate-models-and-projections
tags:
- positive-feedback
- negative-feedback
- ice-albedo
- water-vapor
- cloud-feedback
- climate-sensitivity
stage: advanced
status: validated
---
# Climate Feedback Mechanisms

## Core Idea
Climate feedbacks amplify or dampen the initial warming from a radiative forcing. Positive feedbacks include water vapor (warming increases atmospheric water vapor, the dominant greenhouse gas, amplifying warming ~2×), ice-albedo (melting ice exposes dark ocean or land, decreasing albedo and absorbing more heat), and permafrost carbon release. Negative feedbacks include increased outgoing longwave radiation from a warmer planet (Planck response, the primary stabilizing feedback). Cloud feedbacks are the largest source of uncertainty: low clouds cool by reflecting sunlight, high clouds warm by trapping longwave radiation, and their responses to warming differ. Equilibrium climate sensitivity — warming per CO₂ doubling — is ~2.5–4°C, largely constrained by these feedbacks.

## How It's Best Learned
Start from the Planck response as the baseline negative feedback, then add each positive feedback in turn. Use a simple energy balance model to quantify how feedbacks compound: a 1 W/m² forcing without feedbacks produces ~0.3°C warming; with all feedbacks, the same forcing might produce ~1.0°C.

## Common Misconceptions
- Positive feedback does not mean the system will inevitably 'run away' to a catastrophic state — it means amplification, bounded by negative feedbacks.
- Water vapor is a feedback, not a forcing; its concentration in the atmosphere is controlled by temperature, not directly by emissions.
- Tipping points are thresholds where a feedback becomes self-sustaining even without continued forcing — they are distinct from ordinary feedbacks.

## Questions

```yaml
- question: "Which of the following correctly describes the role of water vapor in the climate system?"
  type: multiple-choice
  options:
    - "Water vapor is a primary forcing that directly drives warming when humans emit it"
    - "Water vapor is a feedback that amplifies warming because a warmer atmosphere holds more moisture"
    - "Water vapor is a negative feedback because clouds formed from it reflect sunlight"
    - "Water vapor has negligible effect on climate because it is too short-lived in the atmosphere"
  answer: 1
  explanation: "Water vapor is a feedback, not a forcing. Its atmospheric concentration is controlled by temperature: as the surface warms (from CO₂ forcing), evaporation increases, raising atmospheric humidity, which then traps more longwave radiation and amplifies the initial warming. Humans do not meaningfully emit water vapor as a climate forcing — it rains out quickly."

- question: "A positive climate feedback means the climate system will inevitably spiral into a runaway warming state with no stable endpoint."
  type: true-false
  answer: false
  explanation: "Positive feedback means amplification of an initial perturbation, not unbounded runaway. The system has both positive and negative feedbacks operating simultaneously. The Planck response (increased outgoing longwave radiation from a warmer planet) is a strong negative feedback that ultimately stabilizes the system at a new, warmer equilibrium. Runaway warming is a specific threshold phenomenon (relevant to Venus-like scenarios), not a consequence of ordinary positive feedbacks."

- question: "Why are cloud feedbacks the largest source of uncertainty in estimates of equilibrium climate sensitivity?"
  type: short-answer
  answer: "Low clouds cool the planet by reflecting incoming sunlight, while high clouds warm it by trapping outgoing longwave radiation. Whether warming increases or decreases each cloud type — and by how much — is difficult to determine from observations and varies across climate models, creating a wide range of possible net cloud feedback values."
  explanation: "Cloud behavior depends on many interacting processes (convection, humidity, aerosols) that operate at scales too small for global climate models to fully resolve. Since low and high clouds have opposite effects and both respond to warming in uncertain ways, cloud feedback can be anywhere from mildly negative to strongly positive, which directly widens the range of projected equilibrium climate sensitivity."
```

## Explainer

Climate feedbacks are the responses that either amplify or dampen a change in Earth's energy balance. If the planet warms slightly due to increased CO₂ (the initial forcing), the warming itself triggers additional changes in the climate system — changes that may add further warming (positive feedbacks) or counteract it (negative feedbacks). The net effect of all feedbacks together determines how much total warming ultimately results from a given forcing.

The most important baseline negative feedback is the Planck response: a warmer planet radiates more energy to space as infrared radiation. This acts like a thermostat — the hotter the planet gets, the more energy it loses, which resists further warming. Without this, even a small forcing could produce runaway warming. Every other feedback is assessed relative to this stabilizing baseline.

On top of the Planck response, several positive feedbacks amplify warming significantly. Water vapor is the largest: because warmer air holds more moisture, surface warming increases atmospheric humidity, and water vapor is itself a potent greenhouse gas. This roughly doubles the warming from CO₂ alone. The ice-albedo feedback adds more: as polar ice melts, it exposes darker ocean or land beneath, which absorbs more sunlight rather than reflecting it. Permafrost thaw, which releases stored carbon, is a third positive feedback that is increasingly important over longer timescales.

Cloud feedbacks are where the science remains most uncertain. Low clouds (stratus, stratocumulus) act like parasols, reflecting incoming solar radiation and cooling the planet. High clouds (cirrus) act like blankets, trapping outgoing infrared radiation and warming it. Whether warming increases or decreases each type of cloud — and in what regions — varies significantly across climate models. This uncertainty is the main reason equilibrium climate sensitivity (warming per CO₂ doubling) spans a range of roughly 2.5–4°C rather than a single precise number.

A common and important misconception to avoid: a positive feedback does not mean "bad" or "unstable." It means the system amplifies an input, but it does so to a new stable equilibrium set by the balance of all feedbacks together. Tipping points — where a feedback becomes self-reinforcing even after the initial forcing stops — are a distinct and more extreme phenomenon. Most climate feedbacks produce amplified but bounded responses, not permanent runaway.
