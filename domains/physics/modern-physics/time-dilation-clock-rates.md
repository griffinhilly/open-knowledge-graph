---
id: time-dilation-clock-rates
title: Time Dilation and Moving Clocks
domain: physics
course: modern-physics
prerequisites:
- id: time-dilation
  type: hard
builds-toward:
- mass-energy-equivalence-relativity
tags:
- special-relativity
- time
- clocks
stage: advanced
status: draft
---

# Time Dilation and Moving Clocks

## Core Idea
Moving clocks run slow compared to stationary clocks by a factor of γ = 1/√(1 − v²/c²)—the Lorentz factor. This effect is symmetric: each observer sees the other's clock running slow. Time dilation is not an illusion but a fundamental feature of spacetime; proper time measured along an object's worldline is invariant across frames.

## Questions

```yaml
- question: "Alice's rocket moves past Bob at 0.6c (γ = 1.25). Bob observes Alice's clock running slow, ticking at 80% of his own clock's rate. What does Alice observe about Bob's clock?"
  type: multiple-choice
  options:
    - "Alice sees Bob's clock running fast, at 125% of her own clock's rate — because she is 'actually' the one in motion"
    - "Alice sees Bob's clock running slow, at 80% of her own clock's rate — because in her frame, Bob is moving at 0.6c"
    - "Alice sees Bob's clock running at the same rate as her own, because both clocks keep absolute time"
    - "Alice cannot determine Bob's clock rate without knowing which frame is 'really' stationary"
  answer: 1
  explanation: "In special relativity there is no preferred frame — 'in motion' is a frame-dependent description. From Alice's perspective, she is at rest and Bob is moving at 0.6c in the opposite direction. By the same time dilation formula, she observes Bob's clock running at 80% of her own rate. Both Bob's and Alice's observations are correct within their respective frames. This is not a contradiction; it reflects the frame-dependence of simultaneity. Each is comparing clock readings at different pairs of events, and those pairs are not the same."

- question: "A muon created in the upper atmosphere has a half-life of 2.2 μs in its rest frame, but reaches Earth's surface (roughly 15 km away) in large numbers. Which calculation correctly uses the Lorentz factor?"
  type: multiple-choice
  options:
    - "The muon travels 15 km in about 50 μs of Earth time; with γ ≈ 22, only 50/22 ≈ 2.3 μs of proper time elapses on the muon — within its half-life"
    - "The muon's half-life increases in the Earth frame by factor γ; with γ ≈ 22, the effective half-life is 2.2 × 22 ≈ 48 μs — long enough to reach the surface"
    - "Both A and B describe the same physical fact: the muon ages more slowly, consistent with γ ≈ 22, whether calculated as less proper time or longer lab-frame half-life"
    - "Time dilation only applies to artificial clocks, not to decay rates of elementary particles"
  answer: 2
  explanation: "Both option A and B are correct descriptions of the same physical reality from different frames — which is why option C is the best answer. In the Earth frame, time dilation extends the muon's lab-frame half-life by γ ≈ 22, giving ~48 μs to traverse the ~15 km. In the muon's rest frame, length contraction reduces the 15 km to ~680 m, which takes only ~2.3 μs of proper time — within the half-life. Both calculations give the same answer (the muon survives) because proper time is invariant. This is the canonical experimental confirmation of relativistic time dilation."

- question: "If Alice observes Bob's clock running slow, and Bob simultaneously observes Alice's clock running slow, then one of them must be making an error."
  type: true-false
  answer: false
  explanation: "False. This symmetry is real and contains no contradiction. The apparent paradox arises from assuming there is a single objective 'present moment' shared by both observers — that there exists a unique instant where both clocks can be directly compared. Special relativity denies this: simultaneity is frame-dependent. When Bob says 'at this moment, Alice's clock reads T while mine reads T₀,' he is referring to events that are not simultaneous in Alice's frame. Both observers are correct about what they each observe, but they are observing different pairs of events."

- question: "Proper time — the time measured by a clock traveling with an object — is invariant: every inertial observer calculates the same proper time accumulated between two events on the object's worldline."
  type: true-false
  answer: true
  explanation: "True. Proper time τ = t/γ (where t is coordinate time in the 'stationary' frame) is a Lorentz-invariant quantity — it is the same number regardless of which frame you use to calculate it. This is the deep resolution of the symmetry puzzle: while coordinate time measurements differ between frames, proper time is the objective, frame-independent measure of 'how much a clock aged.' The twin paradox is resolved because the traveling twin's worldline has less proper time than the stay-at-home twin's, and every frame agrees on both proper time values."

- question: "Why doesn't the symmetry of time dilation lead to a logical contradiction — if Alice sees Bob's clock running slow, and Bob sees Alice's clock running slow, how can both be correct?"
  type: short-answer
  answer: "There is no contradiction because the two observers are comparing different pairs of events. 'Bob's clock reads 8 while Alice's clock reads 10' is a statement about two events — one on Bob's worldline and one on Alice's — that are simultaneous in one frame but not in the other. Simultaneity is frame-dependent in special relativity, so each observer picks a different pair of events to compare, and there is no single absolute comparison. Proper time resolves any apparent paradox: if both observers actually meet at two specific events, every frame agrees on how much proper time each accumulated between those events."
  explanation: "The symmetry becomes paradoxical only if you smuggle in an assumption of absolute simultaneity — that there is one objective 'now' at which both clocks can be compared. Once you accept that simultaneity is frame-dependent (a direct consequence of the two postulates of special relativity), the symmetry is not paradoxical but expected. Each observer's statement about the other's clock refers to a relativized comparison, not an absolute one. The twin paradox appears because one twin accelerates, breaking the symmetry: the non-inertial path accumulates less proper time, and all frames agree on the total difference when they reunite."
```

## Explainer

From your prerequisite study of time dilation, you know that time runs at different rates for observers in relative motion. Now we go deeper: what does this mean for actual clocks, how do we calculate it precisely, and how do we resolve the apparent paradox that both observers see the other's clock running slow?

The **Lorentz factor** γ = 1/√(1 − v²/c²) is the central quantity. Notice its behavior: when v ≪ c, the factor under the square root is nearly 1, so γ ≈ 1 and clocks agree — recovering everyday experience. As v approaches c, the denominator approaches zero and γ grows without bound. A clock moving at 0.6c runs at γ = 1/√(0.64) = 1.25, meaning it ticks only 80% as fast as a stationary clock. At 0.99c, γ ≈ 7.1 — the moving clock runs more than seven times slower. GPS satellites must account for this effect to maintain centimeter-level positioning accuracy.

The symmetry of time dilation is the part that trips people up. If Alice's rocket moves past Bob at 0.6c, Bob sees Alice's clock running slow. But from Alice's frame, Bob is moving at 0.6c in the opposite direction — so Alice sees Bob's clock running slow. Both are correct. This is not a contradiction; it reflects that simultaneity is frame-dependent. The two observers are not comparing the same pair of events when they say "my clock reads T₁ while your clock reads T₂."

The resolution comes through **proper time**: the time measured by a clock that travels with the object being timed. Proper time τ along a worldline is invariant — every observer agrees on how much proper time a moving clock accumulates between two events on its worldline. The formula is τ = t/γ, where t is the coordinate time in the "stationary" frame. Proper time is shorter than coordinate time because the moving clock is traversing a path through spacetime, and spacetime geometry makes paths through time shorter when more spatial distance is covered. This is the deeper statement: time dilation is not a mechanical effect on clocks but a geometric fact about the structure of spacetime itself.
