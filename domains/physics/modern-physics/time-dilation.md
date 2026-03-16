---
id: time-dilation
title: Time Dilation
domain: physics
course: modern-physics
prerequisites:
- id: special-relativity-postulates
  type: hard
builds-toward:
- length-contraction
- lorentz-transformation
- relativistic-momentum-energy
tags:
- relativity
- time
- gamma-factor
- proper-time
stage: formal-systems
status: validated
---

# Time Dilation

## Core Idea
A clock moving relative to an observer ticks more slowly than an identical clock at rest — this is time dilation. The relationship is Δt = γ Δτ, where Δτ is the proper time measured by the moving clock and γ = 1/√(1−v²/c²) ≥ 1. Proper time is the shortest elapsed time between two events, measured by a clock that is present at both. Time dilation has been experimentally confirmed by muon lifetimes, GPS corrections, and atomic clocks on aircraft.

## How It's Best Learned
Derive time dilation from the light-clock thought experiment: two mirrors separated by distance d, with a photon bouncing between them. In the rest frame the path is vertical; in the moving frame the path is diagonal and longer, yet c is fixed, so the period must be longer. Only then introduce the formula.

## Common Misconceptions
- 'Time slows down for the moving observer' — the moving observer's own clock feels normal; it is the other frame's observer who measures the dilated time.
- Time dilation is an illusion caused by signal travel time — it is real; the twin paradox resolution confirms asymmetric aging.
- γ equals v/c — γ = 1/√(1−v²/c²); they are very different quantities.

## Explainer

The starting point is the two postulates you already know: the laws of physics are the same in all inertial frames, and the speed of light c is the same for all observers regardless of source motion. These two postulates seem innocuous, but they force a radical conclusion — time itself must be frame-dependent. The light-clock thought experiment makes this vivid. Imagine a clock built from two parallel mirrors with a photon bouncing vertically between them. In the rest frame of the clock, each tick is the time for the photon to travel up and back: Δτ = 2d/c. Now observe this same clock from a frame in which it moves horizontally at speed v. The photon still travels at c, but now its path is diagonal — a longer path. Since c is fixed, the longer path takes more time. The moving observer measures a longer tick interval Δt > Δτ. The clock appears to run slow.

The quantitative result is **Δt = γΔτ**, where **γ = 1/√(1−v²/c²)** is the **Lorentz factor**. Notice that γ ≥ 1 always, with equality only when v = 0. As v approaches c, γ diverges — the moving clock appears to slow toward a stop. The quantity **Δτ** is called **proper time**: the elapsed time measured by a clock that is physically present at both events (here, both bounces of the photon). Proper time is the minimum elapsed time between two events — no other observer measures a shorter elapsed time. This is not an optical illusion; it reflects the genuine geometry of spacetime.

A powerful real-world confirmation comes from muons produced by cosmic ray collisions in the upper atmosphere. Muons have a half-life of about 2.2 μs in their rest frame — too short to travel the ~10 km to Earth's surface at any speed below c. Yet they arrive at sea level in large numbers. From Earth's frame, muon clocks run slow by a factor of γ ≈ 10–50, extending their apparent lifetime enough to survive the journey. From the muon's frame, it is the Earth that is moving and the atmosphere that is length-contracted (the companion concept you'll meet next). Both perspectives give the same physical prediction: most muons reach the ground.

A common confusion is thinking that the moving observer experiences their time as strange or slow — they do not. Each observer's own clock always ticks at one second per second. Time dilation only appears when you compare two frames. The observer moving with the clock measures Δτ (proper time, the short one); the observer in relative motion measures Δt = γΔτ (the dilated, longer one). The asymmetry is real: if two clocks start together, one moves away and returns, the traveling clock shows less elapsed time — this is the twin paradox, resolved by recognizing the traveling twin must accelerate to turn around, breaking the symmetry between the frames.
