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
stage: advanced
status: draft
---

# Planetary Migration in Protoplanetary Disks

## Core Idea
Planets embedded in protoplanetary disks experience asymmetric gravitational torques from the disk that cause orbital decay (inward migration) or outward migration depending on disk properties and planet mass. Type I migration (low-mass planets), Type II migration (gap-opening planets), and Type III migration (high-mass planets) each operate in distinct regimes and occur on timescales of 10⁴–10⁶ years.

## Explainer

From your study of protoplanetary disk structure, you know that young stars are surrounded by rotating disks of gas and dust from which planets form. From Kepler's laws and angular momentum conservation, you know that orbits are stable in isolation — a planet should stay where it formed. The puzzle is that we observe giant planets orbiting far closer to their stars than any formation model predicts they could have assembled. Planetary migration explains how planets move after formation, and the mechanism is elegantly simple: gravitational conversation between the planet and the disk.

A planet embedded in a gas disk creates density perturbations — **spiral waves** — in the disk material both interior and exterior to its orbit. The inner spiral arm (closer to the star) and the outer spiral arm each exert a gravitational torque on the planet. If these torques balanced perfectly, the planet would stay put. But they almost never balance. The outer disk's torque tends to be slightly stronger, which removes angular momentum from the planet and drives it inward. This is the basic mechanism behind **Type I migration**, which applies to low-mass planets (roughly Earth-mass) that are too small to significantly disturb the disk's overall structure. Type I migration can be alarmingly fast — an Earth-mass planet at 5 AU could spiral into the star in as little as 100,000 years, far shorter than the disk's lifetime.

When a planet becomes massive enough — typically reaching Jupiter's mass — it gravitationally clears a **gap** in the disk around its orbit, sweeping the local gas away. Now the planet is locked into the gap and migrates with the disk as it viscously evolves, a slower process called **Type II migration**. Think of the planet as a boat in a river: a small boat (Type I) gets pushed by the current, while a large boat (Type II) partially dams the river and drifts with the flow itself. Type II migration is slower and more controlled, operating on the disk's own viscous timescale of 10⁵–10⁶ years. **Type III migration** (sometimes called runaway migration) occurs in a narrow intermediate regime where the planet is massive enough to partially clear a gap but not fully, creating a positive feedback loop: migration displaces gas asymmetrically, which increases the torque imbalance, which accelerates migration further.

The practical importance of migration is enormous: it explains **hot Jupiters** (gas giants that migrated inward to hug their stars), resonant chains of exoplanets (where migrating planets captured each other into orbital resonances), and the architecture of our own solar system. Models like the **Grand Tack hypothesis** propose that Jupiter migrated inward to roughly Mars's orbit before Saturn's growth reversed the migration, sculpting the inner solar system's mass distribution in the process. Migration also explains why it is so difficult to form planets in situ — many planets we observe could not have assembled where we find them today, because the raw materials were insufficient at those locations. Migration is the missing link between where planets form and where they end up.
