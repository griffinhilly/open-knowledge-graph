---
id: atlantic-meridional-overturning-stability
title: Atlantic Meridional Overturning Circulation Stability
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: atlantic-meridional-overturning-circulation
  type: hard
- id: thermohaline-circulation-physics
  type: hard
- id: climate-tipping-points
  type: soft
builds-toward:
- climate-models-and-projections
- climate-sensitivity-radiative-feedbacks
tags:
- ocean-circulation
- stability
- bistability
- freshwater-forcing
stage: advanced
status: draft
---

# Atlantic Meridional Overturning Circulation Stability

## Core Idea
The Atlantic Meridional Overturning Circulation (AMOC) is maintained by dense water formation in the North Atlantic that drives deep return flow. Climate models show AMOC can exhibit bistability: if freshwater input increases (from melting ice sheets or increased precipitation), the circulation can weaken or collapse, with regional climate consequences (cooling in the North Atlantic, northward shift of tropical rainfall). Paleoclimate evidence suggests AMOC has collapsed during past climate changes; future freshwater forcing could trigger another collapse.

## Questions

```yaml
- question: "As freshwater from melting ice sheets enters the North Atlantic, the AMOC weakens. As it weakens, it imports less salty subtropical water northward, further reducing surface salinity and sinking — which further weakens the AMOC. This dynamic is an example of:"
  type: multiple-choice
  options:
    - "Negative feedback that will eventually stabilize the AMOC at a new, weaker equilibrium"
    - "Positive feedback that can drive runaway weakening toward a collapsed state"
    - "Thermohaline equilibration, where thermal effects compensate for salinity changes"
    - "Isostatic adjustment of ocean basins in response to reduced ice mass"
  answer: 1
  explanation: "This is the salt-advection positive feedback: weaker AMOC → less salt imported → lower surface density → less sinking → weaker AMOC. Positive feedback amplifies perturbations rather than restoring the original state. Once freshwater forcing crosses the tipping threshold, this loop accelerates rather than decelerating, which is why the transition to a collapsed state can be rapid and why recovery requires conditions substantially more favorable than those that triggered the collapse. Negative feedback would act in the opposite direction — for example, cooling from reduced heat transport might slightly increase density, partially counteracting the freshwater dilution."

- question: "What does 'bistability' mean in the context of AMOC dynamics?"
  type: multiple-choice
  options:
    - "The AMOC oscillates periodically between a strong and weak state on a predictable schedule"
    - "The AMOC can exist in two distinct self-reinforcing stable states: a vigorous 'on' circulation and a collapsed 'off' state"
    - "The AMOC's stability is governed by exactly two variables: North Atlantic temperature and salinity"
    - "The AMOC has two circulation cells — a surface cell and a deep cell — that operate independently"
  answer: 1
  explanation: "Bistability means the system has two stable equilibria separated by an unstable threshold. In the 'on' state, the salt-advection feedback sustains the overturning: salty water brought north keeps surface density high, which drives sinking, which keeps the circulation strong. In the 'off' state, no salty water is imported, the North Atlantic stays fresh, density is too low for sinking, and the circulation stays collapsed. Both states are self-reinforcing. The system is like a light switch: it can remain stably in either position, but once pushed past the threshold, it switches states and stays there."

- question: "Paleoclimate records from Greenland ice cores show that the AMOC has only weakened gradually over geological time and has never undergone rapid collapse."
  type: true-false
  answer: false
  explanation: "Greenland ice cores record the opposite: Heinrich events and Dansgaard-Oeschger oscillations during the last glacial period show North Atlantic temperatures changing by 5–10°C within decades — far too fast for gradual forcing. These events are best explained by rapid AMOC shutdowns triggered by massive freshwater pulses from collapsing ice sheets, followed by restarts. The paleoclimate record is one of the strongest lines of evidence that AMOC bistability and rapid transitions are real physical phenomena, not model artifacts. This historical evidence is why current observations of AMOC weakening and Greenland melt are taken seriously as potential precursors."

- question: "Once the AMOC collapses into its 'off' state, removing the freshwater forcing that triggered the collapse is sufficient to immediately restart circulation."
  type: true-false
  answer: false
  explanation: "Bistability implies hysteresis: the conditions required to restart the AMOC are more demanding than simply reversing the conditions that caused it to collapse. In the collapsed state, the North Atlantic freshens (no salty subtropical water being imported) and the positive feedback maintains the off state. Restarting requires either a sufficiently large perturbation of salty water into the sinking regions or reduction of freshwater input far below the threshold that triggered collapse — not just returning to the pre-collapse forcing level. This irreversibility is what makes AMOC collapse a potential climate tipping point rather than a reversible weakening."

- question: "Explain how the salt-advection feedback creates bistability in the AMOC, and why the collapsed 'off' state is self-reinforcing."
  type: short-answer
  answer: "In the 'on' state, the AMOC transports warm, salty subtropical water northward. This salty water cools in the North Atlantic, becoming dense enough to sink. The sinking drives the overturning, which continues to import salt — a self-reinforcing positive feedback (more circulation → more salt → more sinking → more circulation). In the 'off' state, no subtropical water is imported. Without the salty inflow, the North Atlantic surface freshens over time from precipitation and river input. Fresh water is less dense than salty water, so there is no longer enough density contrast to drive sinking. No sinking → no circulation → no salt import → the surface stays fresh → still no sinking. Both states are thus self-reinforcing: the 'on' state maintains the salinity gradient that drives it, and the 'off' state maintains the freshness that prevents it from restarting."
  explanation: "The bistability arises from the salt-advection feedback operating as a positive feedback in both directions: it amplifies both the 'on' state (keeping it going) and the 'off' state (keeping it from restarting). The threshold between states is where the freshwater forcing is large enough to overwhelm the salt import and tip the balance from the positive feedback maintaining the 'on' state to the positive feedback maintaining the 'off' state."
```

## Explainer

From your study of the AMOC and thermohaline circulation, you know that the Atlantic's overturning is driven by the formation of dense water in the North Atlantic — warm, salty water carried northward by surface currents cools, becomes dense enough to sink, and returns southward at depth. This circulation transports enormous quantities of heat northward, keeping northwestern Europe several degrees warmer than equivalent latitudes elsewhere. The stability question asks: could this system shut down, and if so, what would happen?

The critical concept is **bistability** — the idea that the AMOC can exist in two stable states. In the "on" state, the salt-advection feedback sustains circulation: the overturning brings salty subtropical water northward, maintaining high surface density in the sinking regions, which reinforces the sinking and keeps the circulation going. In the "off" state, no salty water is imported, the North Atlantic freshens, density is too low for sinking, and the circulation remains collapsed. Both states are self-reinforcing, and the system can flip between them if pushed hard enough. This is analogous to a light switch — it can be stably on or stably off, but a sufficient push tips it from one to the other.

The push that can trigger a transition is **freshwater forcing**. Adding fresh water to the North Atlantic — from melting ice sheets, increased rainfall, or river discharge — dilutes the surface salinity, reduces density, and weakens the sinking that drives the overturning. If freshwater input crosses a critical threshold, the positive salt-advection feedback reverses: weaker circulation imports less salt, which further reduces density, which further weakens circulation — a runaway collapse. Climate models identify this threshold but disagree on its exact value, making it one of the most consequential uncertainties in climate science.

Paleoclimate evidence confirms this is not hypothetical. During the last glacial period, massive freshwater pulses from collapsing ice sheets triggered **Heinrich events** and **Dansgaard-Oeschger oscillations** — abrupt climate swings recorded in Greenland ice cores where North Atlantic temperatures changed by 5–10°C within decades. These events are best explained by AMOC shutdowns and restarts. The consequences extended far beyond the North Atlantic: tropical rainfall belts shifted, monsoon systems reorganized, and Southern Hemisphere temperatures responded with an antiphase "seesaw" pattern. Today, Greenland ice sheet melt is accelerating and AMOC strength appears to be declining, raising the question of whether modern freshwater forcing could approach the tipping point that paleoclimate records show was crossed repeatedly in the past.
