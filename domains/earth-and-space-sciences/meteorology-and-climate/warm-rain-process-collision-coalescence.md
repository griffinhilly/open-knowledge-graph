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

## Questions

```yaml
- question: "Two cumulus clouds have equal depth and liquid water content. Cloud A formed over the open ocean (low CCN concentration), Cloud B over a large city (high CCN concentration). Which is more likely to produce warm rain, and why?"
  type: multiple-choice
  options:
    - "Cloud B, because more CCN means more total droplets and therefore a higher collision rate"
    - "Cloud A, because fewer CCN produce a broader droplet size spectrum with some larger collector drops, while Cloud B's many tiny uniform droplets have nearly the same fall speed and poor collision efficiency with each other"
    - "Both equally, because both have the same liquid water content available for precipitation"
    - "Cloud B, because the urban heat island effect raises temperatures and 'warm rain' requires high temperatures"
  answer: 1
  explanation: "The breadth of the droplet size spectrum — not the total number of droplets — controls warm rain initiation. Maritime clouds form on few, often larger CCN, creating a broad spectrum where some droplets grow noticeably larger than others. These larger drops fall faster, sweeping up smaller ones to initiate coalescence. Continental clouds form on abundant tiny CCN, activating many more droplets that share the available water as nearly uniform, very small drops. Uniform drops fall at nearly the same speed, producing minimal relative velocity and very low collision efficiency. This is why tropical oceanic clouds produce frequent brief downpours while continental clouds of similar depth often dissipate without raining."

- question: "A 100 μm collector drop is falling through a cloud containing many 5 μm droplets. Despite the large size difference, collision efficiency is low. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The 5 μm droplets are too cold to coalesce with the larger warm drop"
    - "The 5 μm droplets are carried around the large drop by the airstream deflected around it, like dust particles flowing around a hand moving through air"
    - "The 5 μm droplets are moving faster than the 100 μm drop due to updrafts"
    - "Surface tension prevents 5 μm droplets from merging with a much larger drop"
  answer: 1
  explanation: "Very small droplets have so little inertia that they follow the airstream almost perfectly — they get swept around the falling collector drop rather than impacting it. Collision efficiency is the ratio of drops actually hit to drops in the geometric path, and it is lowest when the collected drops are very small relative to the collector. This is why warm rain is not efficient for a uniform population of very tiny droplets: even if a large collector exists, the smallest drops slip around it. The most efficient collection occurs when collected drops are around 10–20 μm, large enough to have some inertia but small enough relative to the collector to be swept up in large numbers."

- question: "Warm rain can only occur in clouds where all levels remain above 0°C, since ice formation would interfere with the collision-coalescence mechanism."
  type: true-false
  answer: false
  explanation: "'Warm rain' refers to the precipitation mechanism — liquid droplets growing through collision and coalescence — not to cloud temperature. Warm rain can occur in clouds that extend above the 0°C freezing level, provided the droplets remain supercooled liquid rather than freezing. Ice formation is not automatic at 0°C in clouds; supercooled liquid water commonly exists at temperatures well below freezing. The term 'warm rain' distinguishes the process from ice-based precipitation mechanisms (Bergeron process, riming), not from cold atmospheric conditions."

- question: "A broader droplet size spectrum accelerates warm rain development compared to a spectrum of uniformly small droplets of the same total liquid water content."
  type: true-false
  answer: true
  explanation: "Collision-coalescence requires relative motion between droplets, which requires size differences. In a broad spectrum, some droplets are larger and fall faster than others, creating the differential fall speeds needed for collisions. In a narrow, uniform spectrum, all droplets fall at nearly the same speed regardless of total water content — relative velocities are near zero, collision rates are negligible, and warm rain cannot initiate. Broad spectra arise in maritime clouds (few, larger CCN) or clouds with strong updraft variability that allows some drops to grow larger through preferential condensation."

- question: "Explain why the warm rain process is described as 'self-accelerating' once a collector drop reaches a threshold size."
  type: short-answer
  answer: "Once a droplet grows large enough to fall noticeably faster than surrounding cloud droplets, it begins collecting smaller droplets through collision and coalescence. The growth from collection increases the drop's mass, which increases its fall velocity (since terminal velocity scales with size). The faster fall speed increases the volume of air swept per unit time and improves collision geometry (larger cross-section), causing the drop to collect even more smaller droplets per second. This positive feedback loop — size → speed → more collection → more growth → more speed — continues until the drop reaches raindrop size (~2 mm) or becomes large enough to break up from aerodynamic forces. The process can advance from initial coalescence to precipitation reaching the surface in roughly 15–20 minutes."
  explanation: "The self-accelerating nature explains both the rapid onset of warm rain and why it requires a trigger: once the chain reaction starts (when the droplet size distribution produces a collector large enough), it amplifies itself. Without the initial size advantage from a broad spectrum, the chain reaction never gets started, regardless of how much liquid water is available."
```

## Explainer

You know from studying cloud condensation nuclei that cloud droplets form when water vapor condenses onto tiny aerosol particles, and that the initial droplets produced are extremely small — typically 10–20 micrometers in diameter. A raindrop, by contrast, is about 2 millimeters across, roughly a million times the volume of a cloud droplet. The **warm rain process** explains how cloud droplets bridge this enormous size gap in clouds that remain entirely above freezing, where ice-based precipitation mechanisms cannot operate.

The process begins with a size advantage. Not all cloud droplets are the same size — variations in CCN composition, updraft strength, and local supersaturation produce a **spectrum of droplet sizes**. Some droplets grow slightly larger than their neighbors through condensation. These larger droplets fall faster than smaller ones because gravity's pull scales with mass (which goes as the cube of diameter) while air resistance scales more slowly. A droplet of 30 micrometers falls noticeably faster than one of 10 micrometers, which means it sweeps through a cloud full of smaller droplets and collides with them.

**Collision efficiency** — the probability that a large falling droplet actually hits a small droplet in its path — is the critical parameter. Very small droplets tend to follow the airstream around the falling drop and get swept aside, like dust particles flowing around your hand as you move it through air. Collision efficiency is low when both droplets are small and highest when there is a large size difference (collector drops of 100+ micrometers sweeping up drops of 10–20 micrometers). Once collision occurs, **coalescence efficiency** determines whether the droplets actually merge or bounce apart. Coalescence is favored when droplets are small enough that surface tension can absorb the impact. The combined **collection efficiency** (collision × coalescence) determines how fast the growing drop accumulates mass.

The process is self-accelerating: as a collecting drop grows, it falls faster, sweeps a wider path, and collects droplets more efficiently, which makes it grow even faster. This positive feedback is why warm rain, once initiated, develops rapidly — a drop can grow from 100 micrometers to raindrop size in 15–20 minutes. Maritime clouds, which form on fewer but larger CCN, produce broader initial droplet spectra and develop warm rain much more efficiently than continental clouds, which form on abundant small CCN and produce narrow spectra of uniformly tiny droplets. This is why brief, heavy showers are common over tropical oceans but continental cumulus clouds of similar depth often evaporate without producing rain — the initial droplet spectrum determines whether the collision-coalescence chain reaction can get started.
