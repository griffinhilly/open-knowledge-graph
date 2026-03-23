---
id: planetary-migration-mechanisms
title: Planetary Migration in Protoplanetary Disks
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: protoplanetary-disk-structure
  type: hard
- id: orbital-mechanics
  type: soft
- id: kepler-laws-planetary-orbits
  type: hard
- id: orbital-resonances-dynamics
  type: soft
- id: conservation-of-angular-momentum
  type: hard
builds-toward:
- orbital-resonance-capture
- multi-planet-system-architecture
tags:
- migration
- torques
- disk-interaction
- planetary-dynamics
stage: expert
status: validated
---

# Planetary Migration in Protoplanetary Disks

## Core Idea
Planets embedded in protoplanetary disks experience asymmetric gravitational torques from the disk that cause orbital decay (inward migration) or outward migration depending on disk properties and planet mass. Type I migration (low-mass planets), Type II migration (gap-opening planets), and Type III migration (high-mass planets) each operate in distinct regimes and occur on timescales of 10⁴–10⁶ years.

## Questions

```yaml
- question: "A textbook on planet formation states that planets orbit where they formed. Based on migration theory, what is wrong with this assumption, and what evidence most directly contradicts it?"
  type: multiple-choice
  options:
    - "Nothing is wrong — migration theory only applies to unstable multi-planet systems, not single planets"
    - "The assumption ignores gravitational disk-planet torques; hot Jupiters — gas giants orbiting within 0.1 AU — could not have assembled there because insufficient gas existed at those distances, so they must have migrated inward"
    - "The assumption applies only to rocky planets; gas giants always form in situ regardless of disk torques"
    - "The assumption is wrong because planets migrate outward, not inward, placing them farther than their formation location"
  answer: 1
  explanation: "Hot Jupiters are the canonical evidence against in situ formation: gas giants require massive amounts of gas to accrete during formation, and the inner disk (close to the star) has too little gas to form them. They must have formed farther out where gas was abundant, then migrated inward through disk-planet gravitational interactions. This is a concrete, observationally confirmed case where assuming 'planets sit where they formed' leads to an impossible formation scenario. The broader lesson is that migration is a normal phase of planetary system evolution, not an exceptional event."

- question: "A newly discovered exoplanet is a 2-Jupiter-mass gas giant orbiting at 0.04 AU from its star. Which migration mechanism most likely produced this configuration?"
  type: multiple-choice
  options:
    - "Type I migration — low-mass planets migrate fastest due to asymmetric disk torques"
    - "Type III (runaway) migration — it reached this orbit because positive feedback exponentially accelerated its inward movement"
    - "Type II migration — it formed farther out where gas was abundant, opened a gap in the disk as it grew massive, then migrated inward locked to the disk's viscous evolution"
    - "No migration occurred — Jupiter-mass planets are too heavy to be moved by disk torques"
  answer: 2
  explanation: "A 2-Jupiter-mass planet is massive enough to open a gap in the disk, placing it in the Type II regime. Type I applies to low-mass (roughly Earth-mass) planets that cannot disturb the disk structure. Type III applies to a narrow intermediate mass range with partial gap-opening. Once a planet opens a full gap, it becomes locked into the gap and migrates inward as the disk itself viscously evolves — the 'boat in a river' analogy. This slower, gap-locked migration is the standard explanation for hot Jupiters. Option A is wrong because a 2-Jupiter-mass planet is far too massive for Type I; option D is wrong because Type II migration is specifically the mechanism for massive planets."

- question: "Type I migration can be fast enough to destroy a forming planet — an Earth-mass planet at 5 AU could spiral into its star in roughly 100,000 years, which is far shorter than the disk's multi-million-year lifetime."
  type: true-false
  answer: true
  explanation: "This timescale problem is one of the central puzzles of planet formation theory: if Type I migration acts so quickly, how do terrestrial planets survive long enough to form at all? Theoretical responses include migration stalls at disk density transitions, outward migration in regions of certain disk temperature gradients, and the fact that formation itself is rapid. The short Type I timescale is not an artifact — it is a real challenge to standard formation models and motivates study of mechanisms that can slow or reverse inward migration."

- question: "A planet undergoing Type II migration moves faster than a Type I migrating planet, because gap-opening releases additional gravitational energy that accelerates the inward drift."
  type: true-false
  answer: false
  explanation: "Type II migration is significantly slower than Type I. In Type I, the planet is swept inward by the net torque imbalance between inner and outer disk spiral arms — this can be alarmingly fast. In Type II, the planet has opened a gap and becomes coupled to the disk's own viscous evolution timescale, which is typically 10⁵–10⁶ years — slower than Type I. Gap-opening does not release energy that accelerates migration; it instead decouples the planet from the fastest torque mechanisms by removing the local gas that was driving rapid Type I drift. The gap is a throttle, not an accelerator."

- question: "What causes the net inward migration of low-mass planets in Type I migration, even though both the inner and outer disk exert gravitational torques on the planet?"
  type: short-answer
  answer: "The outer disk's gravitational torque on the planet is slightly stronger than the inner disk's torque, creating a net angular momentum loss. When a planet loses angular momentum, it falls to a lower orbit (closer to the star). The asymmetry arises because the outer spiral wave the planet excites in the disk is typically stronger than the inner one due to disk density and temperature gradients."
  explanation: "Angular momentum conservation governs orbital mechanics: to move inward, a planet must lose angular momentum to the disk. The planet excites spiral density waves both inside and outside its orbit. The outer wave extracts angular momentum from the planet (negative torque on planet), while the inner wave deposits angular momentum into the planet (positive torque). When the outer torque exceeds the inner, the net effect is angular momentum loss and inward migration. This asymmetry is sensitive to disk structure, which is why migration rates depend so strongly on local disk density and temperature profiles — and why some disk conditions can produce outward migration or migration traps."
```

## Explainer

From your study of protoplanetary disk structure, you know that young stars are surrounded by rotating disks of gas and dust from which planets form. From Kepler's laws and angular momentum conservation, you know that orbits are stable in isolation — a planet should stay where it formed. The puzzle is that we observe giant planets orbiting far closer to their stars than any formation model predicts they could have assembled. Planetary migration explains how planets move after formation, and the mechanism is elegantly simple: gravitational conversation between the planet and the disk.

A planet embedded in a gas disk creates density perturbations — **spiral waves** — in the disk material both interior and exterior to its orbit. The inner spiral arm (closer to the star) and the outer spiral arm each exert a gravitational torque on the planet. If these torques balanced perfectly, the planet would stay put. But they almost never balance. The outer disk's torque tends to be slightly stronger, which removes angular momentum from the planet and drives it inward. This is the basic mechanism behind **Type I migration**, which applies to low-mass planets (roughly Earth-mass) that are too small to significantly disturb the disk's overall structure. Type I migration can be alarmingly fast — an Earth-mass planet at 5 AU could spiral into the star in as little as 100,000 years, far shorter than the disk's lifetime.

When a planet becomes massive enough — typically reaching Jupiter's mass — it gravitationally clears a **gap** in the disk around its orbit, sweeping the local gas away. Now the planet is locked into the gap and migrates with the disk as it viscously evolves, a slower process called **Type II migration**. Think of the planet as a boat in a river: a small boat (Type I) gets pushed by the current, while a large boat (Type II) partially dams the river and drifts with the flow itself. Type II migration is slower and more controlled, operating on the disk's own viscous timescale of 10⁵–10⁶ years. **Type III migration** (sometimes called runaway migration) occurs in a narrow intermediate regime where the planet is massive enough to partially clear a gap but not fully, creating a positive feedback loop: migration displaces gas asymmetrically, which increases the torque imbalance, which accelerates migration further.

The practical importance of migration is enormous: it explains **hot Jupiters** (gas giants that migrated inward to hug their stars), resonant chains of exoplanets (where migrating planets captured each other into orbital resonances), and the architecture of our own solar system. Models like the **Grand Tack hypothesis** propose that Jupiter migrated inward to roughly Mars's orbit before Saturn's growth reversed the migration, sculpting the inner solar system's mass distribution in the process. Migration also explains why it is so difficult to form planets in situ — many planets we observe could not have assembled where we find them today, because the raw materials were insufficient at those locations. Migration is the missing link between where planets form and where they end up.
