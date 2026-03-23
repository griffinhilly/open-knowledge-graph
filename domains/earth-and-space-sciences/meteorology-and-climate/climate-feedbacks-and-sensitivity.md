---
id: climate-feedbacks-and-sensitivity
title: Climate Feedbacks and Climate Sensitivity
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: climate-change-science
  type: hard
- id: climate-sensitivity-radiative-feedbacks
  type: soft
- id: earths-radiative-balance
  type: soft
builds-toward:
- climate-tipping-points
- climate-extremes-and-attribution
tags:
- feedback
- positive
- negative
- sensitivity
- climate-response
stage: formal-systems
status: validated
---

# Climate Feedbacks and Climate Sensitivity

## Core Idea
Feedback mechanisms either amplify or dampen climate changes, determining how much the Earth warms for a given increase in greenhouse gases (climate sensitivity). Positive feedbacks like the ice-albedo feedback (melting ice reduces reflectivity, causing more warming) amplify warming. Negative feedbacks like increased cloud cover reflecting sunlight dampen warming. The balance of these feedbacks—which remain poorly constrained—is the primary source of uncertainty in climate projections.

## How It's Best Learned
Use energy balance models to show quantitatively how feedbacks change the sensitivity parameter. Compare projections with and without various feedbacks to demonstrate their relative importance.

## Common Misconceptions
- Feedbacks operate on the surface temperature alone; they operate throughout the climate system including the atmosphere, cryosphere, and biosphere. - All feedbacks are linear; many feedbacks are nonlinear and become stronger at larger temperature changes.

## Questions

```yaml
- question: "Without any feedbacks, doubling CO₂ produces roughly 1°C of warming. With all feedbacks, best estimates of climate sensitivity range from 2.5°C to 4°C. What primarily accounts for the difference between 1°C and ~3°C?"
  type: multiple-choice
  options:
    - "Scientists have systematically underestimated the direct radiative forcing from CO₂ absorption"
    - "Positive feedbacks — especially the water vapor feedback — amplify the initial forcing, roughly tripling the no-feedback warming"
    - "Negative feedbacks cool the planet more than CO₂ warms it, so the 3°C figure is an underestimate"
    - "The 3°C figure includes warming contributions from non-CO₂ greenhouse gases like methane and nitrous oxide"
  answer: 1
  explanation: "The ~1°C no-feedback warming is the well-constrained direct response to CO₂ doubling. The amplification to ~3°C comes from positive feedbacks, primarily the water vapor feedback (warmer air holds more water vapor, a potent greenhouse gas, causing further warming) and the ice-albedo feedback. Negative feedbacks like the Planck response are already accounted for in the 1°C baseline. The uncertainty range 2.5–4°C reflects poorly constrained feedback magnitudes, especially cloud feedbacks, not uncertainty in the basic CO₂ forcing."

- question: "A student argues that negative feedbacks will prevent significant warming because they stabilize the climate system. Which response best identifies the flaw in this reasoning?"
  type: multiple-choice
  options:
    - "There are no negative feedbacks in the climate system; all feedbacks are positive"
    - "Negative feedbacks eventually dominate, but only at temperatures hundreds of degrees above current levels"
    - "Negative feedbacks do prevent runaway warming, but positive feedbacks still amplify the initial CO₂ forcing to 3–4°C before the system re-equilibrates at a new, higher temperature"
    - "Negative feedbacks operate only on seasonal timescales and are too slow to affect decadal warming"
  answer: 2
  explanation: "The student conflates 'no runaway warming' with 'no significant warming.' The Planck response (a fundamental negative feedback) does ensure the climate reaches a new equilibrium rather than warming indefinitely. But positive feedbacks amplify the initial forcing substantially before equilibrium is reached — the stable endpoint is roughly 3°C warmer than pre-industrial, not 1°C. Negative feedbacks set the ceiling against runaway; they don't prevent the amplified warming that positive feedbacks produce on the way to that ceiling."

- question: "The water vapor feedback is self-limiting because the additional water vapor it produces forms clouds that cool the planet, ultimately canceling out the positive feedback."
  type: true-false
  answer: false
  explanation: "The water vapor feedback and cloud feedbacks are distinct processes and must not be conflated. The water vapor feedback is straightforwardly positive: warmer air holds more water vapor (Clausius-Clapeyron), and water vapor is itself a potent greenhouse gas, trapping more heat and causing further warming. This feedback is well-quantified and not self-limiting. Cloud feedbacks are separate, involving changes in cloud type, coverage, and altitude — and their net sign remains uncertain. Some cloud effects cool, some warm; they do not automatically neutralize the water vapor warming."

- question: "The primary source of uncertainty in climate sensitivity estimates is disagreement among scientists about the spectroscopic physics of how CO₂ absorbs infrared radiation."
  type: true-false
  answer: false
  explanation: "The spectroscopic physics of CO₂ absorption is well-established and not seriously contested. The uncertainty in climate sensitivity arises from poorly constrained feedback strengths, particularly cloud feedbacks. Clouds simultaneously trap outgoing longwave radiation (warming) and reflect incoming shortwave radiation (cooling). Small changes in cloud type, altitude, or fractional coverage can tip the net effect either way. Constraining how clouds respond to warming is the central challenge — not the basic CO₂ physics, which has been understood for over a century."

- question: "Why is climate sensitivity described as an 'emergent property of interacting feedbacks' rather than a fixed physical constant, and what are the implications for climate projections?"
  type: short-answer
  answer: "Climate sensitivity cannot be derived from a single physical law because it emerges from the combined, interacting effects of multiple feedbacks — water vapor, ice-albedo, clouds, carbon cycle feedbacks, and others. These feedbacks are not independent: water vapor amplifies the ice-albedo feedback; permafrost thaw releases methane that amplifies warming further; some feedbacks are nonlinear and strengthen at higher temperatures. Because the sensitivity is the net result of these interacting, partially uncertain processes, it cannot be a fixed constant — it must be estimated from paleoclimate records, observational data, and model ensembles. This means projections must report a range rather than a single number, and the width of that range represents genuine physical uncertainty, not scientific disagreement about basic facts."
  explanation: "Understanding this explains why sensitivity research is still active and why '3°C' is a best estimate with a meaningful uncertainty range, not a calculated constant. It also explains why improving cloud representation in climate models is a high-priority research challenge."
```

## Explainer

Start with a simple thought experiment grounded in what you know about Earth's radiative balance. Suppose we add CO₂ to the atmosphere, reducing outgoing longwave radiation and creating an energy imbalance. The planet warms until it radiates enough energy to restore balance. If nothing else changed, the warming needed would be modest — roughly 1°C for a doubling of CO₂. But other things do change, and those changes are **climate feedbacks**: processes that either amplify or dampen the initial warming.

The most powerful positive feedback is the **water vapor feedback**. Warmer air holds more water vapor (the Clausius-Clapeyron relationship you encountered in prerequisite material), and water vapor is itself a potent greenhouse gas. So initial warming → more water vapor → more greenhouse trapping → more warming. This single feedback roughly doubles the warming you would get from CO₂ alone. The **ice-albedo feedback** works through reflectivity: warming melts bright ice and snow, exposing darker ocean or land that absorbs more sunlight, which causes further warming. Together, these two positive feedbacks are well-understood and well-quantified.

**Negative feedbacks** work in the opposite direction. The most fundamental is the **Planck response** — as the planet warms, it radiates more energy to space (Stefan-Boltzmann law), which inherently limits runaway warming. Some cloud feedbacks may also be negative: certain types of low clouds could become more reflective or widespread in a warmer world, bouncing more sunlight back to space. However, cloud feedbacks remain the largest source of uncertainty in climate science because clouds simultaneously trap outgoing radiation (warming effect) and reflect incoming sunlight (cooling effect), and small shifts in cloud type, altitude, or coverage can tip the balance either way.

**Climate sensitivity** is the number that captures the net effect of all feedbacks combined. It is defined as the equilibrium warming expected from a doubling of CO₂ concentration. Current best estimates place it between 2.5°C and 4°C, with a most likely value near 3°C. The range persists because feedbacks interact — the water vapor feedback strengthens the ice-albedo feedback, which in turn affects cloud distributions. Some feedbacks also become nonlinear at higher temperatures: permafrost thaw releases methane, a feedback that barely registers at 1°C of warming but could become significant at 3–4°C. Understanding that climate sensitivity is not a fixed number but an emergent property of interacting feedbacks is essential for interpreting the range of projections in climate models and the policy decisions that depend on them.
