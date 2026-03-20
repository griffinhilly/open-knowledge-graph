---
id: warm-rain-process-collision-coalescence
title: Warm Rain Process and Collision-Coalescence
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: cloud-condensation-nuclei-activation
  type: hard
- id: precipitation-types-and-processes
  type: soft
builds-toward:
- graupel-and-hail-formation
- tropical-weather-systems
tags:
- microphysics
- precipitation
- warm-clouds
stage: advanced
status: draft
---

# Warm Rain Process and Collision-Coalescence

## Core Idea
In warm tropical clouds where all particles remain liquid, precipitation occurs when larger droplets collide and coalesce with smaller ones. This process is much slower than the Bergeron process but dominates in warm clouds where freezing levels are high. The collision efficiency depends on relative droplet sizes: a broad droplet spectrum (from varying CCN or updraft variability) accelerates coalescence.

## How It's Best Learned
Calculate collision kernel and collision efficiency for different droplet size pairs; compare precipitation development timescales between warm and mixed-phase clouds; examine maritime vs continental cloud spectra.

## Common Misconceptions
- Thinking warm rain requires clouds to be very warm (occurs in clouds below 0°C if all droplets stay liquid).
- Assuming uniform droplet sizes accelerate warm rain (broad spectra accelerate coalescence).

## Explainer

You know from studying cloud condensation nuclei that cloud droplets form when water vapor condenses onto tiny aerosol particles, and that the initial droplets produced are extremely small — typically 10–20 micrometers in diameter. A raindrop, by contrast, is about 2 millimeters across, roughly a million times the volume of a cloud droplet. The **warm rain process** explains how cloud droplets bridge this enormous size gap in clouds that remain entirely above freezing, where ice-based precipitation mechanisms cannot operate.

The process begins with a size advantage. Not all cloud droplets are the same size — variations in CCN composition, updraft strength, and local supersaturation produce a **spectrum of droplet sizes**. Some droplets grow slightly larger than their neighbors through condensation. These larger droplets fall faster than smaller ones because gravity's pull scales with mass (which goes as the cube of diameter) while air resistance scales more slowly. A droplet of 30 micrometers falls noticeably faster than one of 10 micrometers, which means it sweeps through a cloud full of smaller droplets and collides with them.

**Collision efficiency** — the probability that a large falling droplet actually hits a small droplet in its path — is the critical parameter. Very small droplets tend to follow the airstream around the falling drop and get swept aside, like dust particles flowing around your hand as you move it through air. Collision efficiency is low when both droplets are small and highest when there is a large size difference (collector drops of 100+ micrometers sweeping up drops of 10–20 micrometers). Once collision occurs, **coalescence efficiency** determines whether the droplets actually merge or bounce apart. Coalescence is favored when droplets are small enough that surface tension can absorb the impact. The combined **collection efficiency** (collision × coalescence) determines how fast the growing drop accumulates mass.

The process is self-accelerating: as a collecting drop grows, it falls faster, sweeps a wider path, and collects droplets more efficiently, which makes it grow even faster. This positive feedback is why warm rain, once initiated, develops rapidly — a drop can grow from 100 micrometers to raindrop size in 15–20 minutes. Maritime clouds, which form on fewer but larger CCN, produce broader initial droplet spectra and develop warm rain much more efficiently than continental clouds, which form on abundant small CCN and produce narrow spectra of uniformly tiny droplets. This is why brief, heavy showers are common over tropical oceans but continental cumulus clouds of similar depth often evaporate without producing rain — the initial droplet spectrum determines whether the collision-coalescence chain reaction can get started.
