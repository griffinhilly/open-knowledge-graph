---
id: grand-tack-hypothesis
title: The Grand Tack Hypothesis
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: planetary-migration-mechanisms
  type: hard
- id: multi-planet-system-architecture
  type: hard
builds-toward:
- planetary-system-stability
- late-heavy-bombardment
tags:
- planet-migration
- jupiter
- solar-system
- formation
stage: advanced
status: draft
---

# The Grand Tack Hypothesis

## Core Idea
The Grand Tack hypothesis proposes that Jupiter migrated inward toward the Sun (the inbound tack) and then outward again (the outbound tack) early in solar system history. This inward-outward migration would explain the solar system's unusual architecture—the scarcity of terrestrial planets in the inner system and the asymmetric asteroid belt. The hypothesis elegantly reconciles observed planetary spacing with formation models.

## Questions

```yaml
- question: "According to the Grand Tack hypothesis, what caused Jupiter's inward migration to reverse direction and move outward?"
  type: multiple-choice
  options:
    - "Jupiter ran out of gas disk material to interact with and naturally decelerated"
    - "Saturn formed, caught up to Jupiter, entered a mean-motion resonance, and the shared gap reversed the disk torques"
    - "The growing terrestrial planets exerted enough gravitational pull to halt Jupiter's infall"
    - "Jupiter reached the inner edge of the gas disk and had nowhere left to migrate"
  answer: 1
  explanation: "The reversal happened when Saturn, which formed more slowly, caught up to Jupiter and locked into a 2:3 mean-motion resonance. Two giant planets sharing a gap in the gas disk create a torque balance that reverses the migration direction, pushing both outward together. The other options describe mechanisms that do not apply — terrestrial planets were far too small to halt Jupiter, and the disk's inner edge was not the relevant constraint."

- question: "The Grand Tack hypothesis predicts that Mars has only about one-tenth of Earth's mass. What is the proposed mechanism for this?"
  type: multiple-choice
  options:
    - "Mars formed later than Earth and had less time to accrete material before the disk dissipated"
    - "Mars is made of less dense material than Earth, so the same volume of solids produced less mass"
    - "Jupiter's inward migration through the Mars-forming region depleted the solid material available to build Mars"
    - "A giant impact in the Mars region ejected most of its mass into the asteroid belt"
  answer: 2
  explanation: "Jupiter migrating inward to approximately 1.5 AU — roughly where Mars orbits — scattered and cleared the planetesimals in that region, truncating the supply of material available for Mars to grow. Standard formation models without this migration consistently fail to reproduce Mars's small mass, generating a planet much more massive than observed. This is one of the Grand Tack's strongest predictive successes."

- question: "The Grand Tack hypothesis predicts that Jupiter's outward migration would scatter C-type (water-rich) asteroids from beyond the snow line inward, mixing them with the inner-belt S-type asteroids."
  type: true-false
  answer: true
  explanation: "This is a key prediction of the Grand Tack: as Jupiter migrated outward, it would scatter volatile-rich C-type material from the outer solar system inward into the asteroid belt, naturally producing the observed compositional gradient between the inner belt (S-types) and outer belt (C-types) while also explaining the presence of water-bearing bodies in the inner solar system."

- question: "Because Jupiter's migration reversed, the solar system's terrestrial planets contain roughly the same total mass as the densely packed super-Earth systems commonly found around other stars."
  type: true-false
  answer: false
  explanation: "The Grand Tack actually explains why the inner solar system has relatively little total mass compared to compact super-Earth systems around other stars. Jupiter's early inward incursion cleared out solid material that might otherwise have built much more massive inner planets. The result is that our inner system — with four small rocky planets — is unusually sparse compared to many observed planetary systems."

- question: "What two lines of evidence from the asteroid belt are specifically explained by Jupiter's inward-then-outward migration in the Grand Tack model?"
  type: short-answer
  answer: "First, the asteroid belt is depleted in total mass — Jupiter's passage scattered away much of the primordial solid material. Second, the belt contains two compositionally distinct populations (dry S-type asteroids in the inner belt, water-rich C-type asteroids in the outer belt) whose mixing is naturally explained by Jupiter's outward migration scattering C-type material inward from beyond the snow line while S-type material was left behind."
  explanation: "The Grand Tack ties together two facts about the asteroid belt that are otherwise hard to explain simultaneously: its low total mass and its compositional bimodality. The outward migration phase is responsible for the mixing — without it, C-type bodies should be confined to the outer solar system where they formed, not distributed through the belt alongside S-types."
```

## Explainer

From your study of planetary migration mechanisms and multi-planet system architecture, you know that giant planets do not necessarily stay where they form — gravitational interactions with the protoplanetary gas disk can cause them to migrate inward or outward over millions of years. The **Grand Tack hypothesis** applies this understanding to our own solar system, proposing a specific migration history for Jupiter that solves several longstanding puzzles about why the inner solar system looks the way it does.

The scenario begins about 3–5 million years after the Sun formed, when Jupiter had already accreted its massive gas envelope and was embedded in the remnant gas disk. Gravitational torques between Jupiter and the disk caused it to migrate inward — a well-understood process called **Type II migration** that has been observed in simulations of many planetary systems. In the Grand Tack model, Jupiter migrated inward to approximately 1.5 AU (roughly where Mars is today). This inward sweep was catastrophic for the inner disk: Jupiter's gravity scattered planetesimals and disrupted the solid material available to form terrestrial planets, effectively truncating the inner disk's mass supply.

The "tack" — the reversal — happened when Saturn, which formed more slowly, caught up to Jupiter and became locked in a **mean-motion resonance** (specifically a 2:3 resonance, where Saturn orbits twice for every three Jupiter orbits). Hydrodynamic simulations show that when two giant planets share a gap in the gas disk in this resonance configuration, the torques reverse: instead of migrating inward, the pair migrates outward together. Jupiter reversed course and retreated to approximately its current orbital distance of 5.2 AU, with Saturn following to about 7 AU (later evolving to 9.5 AU through subsequent dynamical interactions).

This inward-then-outward journey explains several otherwise puzzling features of the solar system. First, it accounts for **Mars's small mass**: Jupiter's passage through the Mars-forming region depleted the available building material, leaving Mars with only about one-tenth of Earth's mass — a result that standard formation models without migration consistently fail to reproduce. Second, it explains the **structure of the asteroid belt**, which contains two distinct populations (dry S-type asteroids in the inner belt and water-rich C-type asteroids in the outer belt). Jupiter's outward migration would have scattered C-type material inward from beyond the snow line while mixing it with S-type material left behind, naturally producing the observed compositional gradient. Third, the Grand Tack helps explain why the inner solar system has relatively little total mass compared to the tightly packed planetary systems discovered around other stars — Jupiter's early incursion cleared out material that might otherwise have built super-Earths. The hypothesis remains debated, with alternative models (like the "empty primordial belt" scenario) offering competing explanations, but it stands as one of the most influential frameworks for understanding our solar system's architecture as a product of dynamic history rather than static initial conditions.
