---
id: shallow-water-wave-theory
title: Shallow-Water Wave Theory and Tidal Waves
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: gravity-waves-wind-ocean-surface
  type: soft
builds-toward:
- coastal-processes-and-waves
tags:
- shallow-water-waves
- long-waves
- wave-speed
- tsunami
stage: advanced
status: validated
---

# Shallow-Water Wave Theory and Tidal Waves

## Core Idea
When water depth is less than one wavelength, waves transition to shallow-water (long-wave) behavior where wave speed depends only on water depth (c = √gh), not frequency. Tidal waves, storm surge, and tsunamis are shallow-water waves that travel across ocean basins with minimal attenuation and amplify dramatically in shallow bays and harbors.

## How It's Best Learned
Compare wave speeds in deep ocean and near shore; examine how tsunami waves slow and steepen as they approach land.

## Common Misconceptions
Students often think tsunami waves are large everywhere; they are actually small-amplitude in deep ocean and only become dangerous near shore.

## Questions

```yaml
- question: "A tsunami is generated near Japan. In the deep Pacific (depth ≈ 4,000 m) it is 40 cm tall and virtually undetectable to ships. Near the Hawaiian coast (depth ≈ 10 m), the same tsunami has become several meters tall. What explains this amplification?"
  type: multiple-choice
  options:
    - "The earthquake continues to pump energy into the wave as it crosses the ocean"
    - "As depth decreases, the wave slows (c = √gh), compressing its energy into a shorter wavelength and greater amplitude — a process called shoaling"
    - "Waves naturally grow taller over time due to cumulative wind forcing"
    - "Coastal reflection from the shoreline doubles the wave height"
  answer: 1
  explanation: "Shoaling is the key mechanism. The formula c = √(gh) means wave speed is proportional to the square root of depth. As a tsunami approaches shore and depth decreases from 4,000 m to 10 m, speed falls by a factor of 20. The trailing portion of the wave, still in deeper water, continues at high speed and 'piles into' the slowing front — compressing wave energy into a shorter wavelength and greater height. Energy is conserved, not added. This is why tsunamis are nearly undetectable in the open ocean but devastating at the coast."

- question: "A tsunami (wavelength ≈ 200 km) and a wind-generated ocean swell (wavelength ≈ 100 m) are both traveling across the Pacific in water 4,000 m deep. Which statement correctly describes their wave behavior?"
  type: multiple-choice
  options:
    - "Both behave as deep-water waves because they are both traveling in deep ocean"
    - "The tsunami behaves as a shallow-water wave (wavelength >> depth) while the swell behaves as a deep-water wave; they travel at very different speeds governed by different physics"
    - "The swell travels faster because shorter waves have higher frequency and thus more energy"
    - "The tsunami is a deep-water wave because it originates from seafloor displacement in deep water"
  answer: 1
  explanation: "Whether a wave is 'shallow-water' or 'deep-water' depends on the ratio of wavelength to depth, not on the absolute depth. The tsunami's wavelength (200 km) is vastly larger than the ocean depth (4 km), so the entire water column participates in wave motion — shallow-water behavior, speed = √(gh) ≈ 200 m/s. The swell's wavelength (100 m) is much shorter than the depth (4,000 m), so water particles form full orbits without touching the bottom — deep-water behavior, speed depends on wavelength. The same water body is 'shallow' for the tsunami and 'deep' for the swell."

- question: "For shallow-water waves, wave speed increases as water depth increases — meaning a tsunami travels faster in the deep ocean than near shore."
  type: true-false
  answer: true
  explanation: "This follows directly from c = √(gh): wave speed scales with the square root of depth. In the deep Pacific (h ≈ 4,000 m), c ≈ 200 m/s (~720 km/h). Near shore (h = 10 m), c ≈ 10 m/s. The dramatic slowdown as the tsunami approaches land is precisely what causes shoaling and wave amplification. This speed-depth relationship also explains why tsunami arrival times can be predicted accurately: the wave travels at a known speed that depends only on the known bathymetry along its path."

- question: "Tsunamis are dangerous primarily because they are large-amplitude waves even in the deep ocean — the same wall of water that devastates coastlines travels across the ocean basin."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about tsunamis. In the open ocean, a tsunami may be only 30–50 cm tall, spread over a wavelength of 100–200 km. Ships experience it as a gentle rise and fall over several minutes, almost imperceptible. The tsunami becomes dangerous only near shore, where shoaling — caused by the speed reduction from c = √(gh) — compresses the wave energy into a much shorter, much taller form. The wave that causes devastation is not the same amplitude as what crossed the ocean; it grew during the final approach."

- question: "Explain how the formula c = √(gh) accounts for both why a tsunami is imperceptible in the deep ocean and why it becomes devastating near the coast."
  type: short-answer
  answer: "In deep water (h ≈ 4,000 m), the tsunami travels at c = √(9.8 × 4000) ≈ 198 m/s (~700 km/h). At this speed, its enormous wavelength (200 km) means the wave passes any point in about 17 minutes — a barely noticeable rise and fall of 30–50 cm over that time. As the tsunami approaches shore and h decreases to 10 m, c drops to about 10 m/s. The wave slows dramatically, but the energy carried by the wave is conserved. Because wave energy depends on amplitude squared and the wave energy is conserved, the amplitude must increase as the wavelength shortens — this is shoaling. The same energy that was spread over 200 km of low-amplitude wave in the deep ocean is now concentrated into a wave that may be 10+ meters tall and just a few km long. The speed formula makes both the deep-ocean invisibility and the coastal catastrophe the same phenomenon."
  explanation: "The key is that c = √(gh) makes wave speed vary continuously with depth, which means every meter of bathymetry along the tsunami's path affects its behavior. This is also why tsunami forecasting works: instrument networks measure the tsunami in deep water, models apply the depth-speed relationship across known bathymetry, and accurate arrival times and coastal amplitudes can be predicted hours in advance."
```

## Explainer

From your introduction to gravity waves on the ocean surface, you know that waves involve orbital motion of water particles and that wave behavior depends on the relationship between wavelength and water depth. The critical transition happens when water depth becomes less than about half the wavelength — at that point, the circular orbits of water particles flatten against the bottom, and the wave "feels" the seafloor. **Shallow-water waves** (also called long waves) are the extreme case: their wavelength is so much greater than the water depth that the entire water column participates in the wave motion, from surface to bottom.

The most important result in shallow-water wave theory is elegantly simple: wave speed depends only on water depth, given by **c = √(gh)**, where g is gravitational acceleration and h is water depth. Frequency and wavelength drop out entirely. This has profound consequences. In the deep ocean where h ≈ 4,000 meters, a shallow-water wave travels at about 200 m/s (roughly 700 km/h — the speed of a commercial jet). In coastal water where h = 10 meters, the same wave slows to about 10 m/s. The wave does not lose energy as it slows; instead, its energy compresses into a shorter wavelength and taller amplitude. This is why tsunamis and storm surges, which are barely detectable in the open ocean, become devastating walls of water at the coast.

A **tsunami** is the most dramatic shallow-water wave. Generated by seafloor displacement — earthquakes, submarine landslides, or volcanic eruptions — a tsunami can have a wavelength of 200 kilometers or more, making even the deepest ocean "shallow" relative to its wavelength. In the open Pacific, a tsunami might be only 30–50 centimeters tall, spread over a wavelength so long that a ship would rise and fall imperceptibly over several minutes. But as it approaches shore and water depth decreases, the c = √(gh) relationship forces the wave to slow dramatically. The trailing portion of the wave, still in deeper water, continues at high speed, compressing the wave energy into an ever-shorter, ever-taller form. This process — called **shoaling** — can amplify a half-meter open-ocean wave into a 10-meter-plus coastal surge.

Tidal waves are also shallow-water waves, though driven by gravitational forcing from the Moon and Sun rather than by sudden seafloor displacement. The tidal "wave" has a wavelength equal to half the Earth's circumference — there is no ocean deep enough for this to behave as a deep-water wave. Storm surge operates on the same physics: a broad dome of water pushed by sustained winds and low atmospheric pressure behaves as a long wave whose amplification on approach to shore follows the same depth-dependent speed relationship. Understanding c = √(gh) is the single key that unlocks the behavior of all these phenomena — from the arrival time of a tsunami across the Pacific to the amplification of storm surge in a narrowing bay.
