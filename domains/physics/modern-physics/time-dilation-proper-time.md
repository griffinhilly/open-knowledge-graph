---
id: time-dilation-proper-time
title: Time Dilation and Proper Time
domain: physics
course: modern-physics
prerequisites:
- id: relativity-of-simultaneity
  type: hard
- id: time-dilation
  type: soft
builds-toward:
- twin-paradox-proper-time
tags:
- special-relativity
- spacetime
- time
stage: advanced
status: draft
---

# Time Dilation and Proper Time

## Core Idea
Time intervals measured in a moving frame are longer than proper time (the time measured in the frame where events occur at the same location). The relationship is Δt = γΔt₀, where Δt₀ is proper time. This time dilation is real and measurable, not a mere perceptual effect—muon decay in the upper atmosphere provides direct experimental confirmation.

## Explainer

The concept of **proper time** is built on the relativity of simultaneity you already understand: because whether two spatially separated events are simultaneous depends on the observer's frame, time intervals between events must also be frame-dependent. Proper time Δt₀ is the special case where a clock is *present at both events* — it travels with the process being timed. Because this clock has no spatial displacement in its own rest frame, it measures only "pure time" between the events. Any other clock, moving relative to the first, measures a longer elapsed time. Proper time is the minimum time interval that can elapse between two events connected by a physical process.

The formula Δt = γΔt₀ makes this precise. Here γ = 1/√(1 − v²/c²) ≥ 1 is the **Lorentz factor**, which grows without bound as v → c. At everyday speeds, γ ≈ 1 and the difference is negligible. At v = 0.866c, γ = 2: a clock that ticks off 1 second of proper time is seen, from the lab frame, to take 2 seconds. The moving clock runs slow — not because it is malfunctioning, but because time itself is passing differently along its worldline.

The muon decay experiment makes this concrete and eliminates any doubt that time dilation is a real physical effect rather than a coordinate artifact. Muons produced by cosmic rays at ~15 km altitude travel at ~0.999c and have a proper lifetime of ~2.2 μs — enough to travel only ~660 m before decaying. Yet they arrive at Earth's surface in abundance. In the lab frame, γ ≈ 22, stretching their apparent lifetime to ~50 μs, long enough to cover ~15 km. From the muon's own rest frame, the lifetime is still ~2.2 μs, but Earth's surface rushes up from only ~680 m away (Lorentz-contracted by the same factor γ ≈ 22). Both frames agree that the muon survives the journey — they disagree on which effect is responsible. The physical outcome is frame-independent; the description is not.

A key conceptual move: proper time is a **Lorentz scalar** — it has the same value in every inertial frame. Coordinate time Δt is frame-dependent. This is why proper time will become the natural "arc length" of a worldline when you encounter spacetime geometry: it is the invariant measure of time along a path, analogous to how arc length in ordinary space is independent of the coordinate system you use to describe it. When you encounter the twin paradox, the asymmetry resolves immediately from this vantage point — the traveling twin's worldline is curved (accelerated), and curved worldlines through spacetime are always shorter in proper time than straight (inertial) ones connecting the same two events.
