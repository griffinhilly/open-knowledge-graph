---
id: tidal-equilibrium-mechanics
title: Tidal Equilibrium Theory and Tidal Mechanics
domain: earth-and-space-sciences
course: oceanography
prerequisites: []
builds-toward:
- tides
- shallow-water-wave-theory
tags:
- tides
- lunar-tides
- solar-tides
- equilibrium-theory
stage: advanced
status: validated
---

# Tidal Equilibrium Theory and Tidal Mechanics

## Core Idea
Tides arise from the gravitational attraction of the Moon and Sun on Earth's oceans and are modified by Earth's rotation. Equilibrium tidal theory predicts two tidal bulges per day, with the amplitude depending on latitude and the alignment of lunar and solar cycles. Semi-diurnal (two tides per day) and diurnal tides dominate; the interaction of solar and lunar forcing creates spring and neap tides at two-week intervals.

## Questions

```yaml
- question: "Most people understand why there is a tidal bulge on the side of Earth facing the Moon (the Moon pulls that water toward it). Why is there also a tidal bulge on the opposite side of Earth, away from the Moon?"
  type: multiple-choice
  options:
    - "Earth's rotation generates centrifugal force that flings water outward on the far side"
    - "On the far side, the Moon's gravity is weaker than average, so that water is effectively left behind as Earth's center is pulled more strongly toward the Moon"
    - "The Sun creates the far-side bulge while the Moon creates the near-side bulge"
    - "The far-side bulge is a pressure wave reflected from the near-side bulge through Earth's rigid interior"
  answer: 1
  explanation: "Tides arise from the differential in gravity across Earth's diameter — not from gravity itself. The Moon pulls the near-side ocean stronger than Earth's center, and pulls Earth's center stronger than the far-side ocean. From Earth's reference frame, the far-side ocean is 'left behind' as Earth accelerates toward the Moon. The result is two bulges — one pulled toward the Moon, one left behind — which is why most coastlines experience two high tides per day. Option A (centrifugal force) is a common misconception; rotation alone cannot explain why both bulges track the Earth-Moon line."

- question: "The Sun is 27 million times more massive than the Moon, yet the Moon produces tides roughly twice as large as the Sun's. Why?"
  type: multiple-choice
  options:
    - "The Moon orbits closer to sea level and therefore exerts tidal force more directly on surface water"
    - "The tide-generating force falls off with the cube of distance — not the square — so the Moon's proximity more than compensates for the Sun's greater mass"
    - "The Sun's light and radiation counteract its gravitational pull on the oceans"
    - "The Moon orbits in the same plane as Earth's equator, maximizing its tidal effect"
  answer: 1
  explanation: "This is the key quantitative insight of tidal mechanics. Gravitational force itself falls off as the square of distance (inverse square law). But the tide-generating force — the differential in gravity across Earth's diameter — falls off with the cube of distance. This means proximity matters enormously more for tides than for gravity. The Sun is about 390 times farther from Earth than the Moon. Although the Sun is 27 million times more massive, the cube of 390 (about 59 million) overcomes that mass advantage, leaving the Moon with roughly twice the Sun's tidal effect."

- question: "Spring tides — the largest tidal ranges — occur when the Moon is at its closest orbital point to Earth (perigee), maximizing its gravitational pull on the oceans."
  type: true-false
  answer: false
  explanation: "Spring tides are caused by the alignment of the Sun, Earth, and Moon — at new moon and full moon — not by the Moon's orbital distance. When the Sun and Moon are aligned, their tidal bulges reinforce each other, producing larger combined tides. When the Moon is at perigee (closest approach), tides are also somewhat larger (called perigean tides), but that is a separate effect. The spring-neap cycle is driven purely by the angular relationship between the Sun and Moon as seen from Earth, repeating every ~14.8 days as the Moon orbits."

- question: "Equilibrium tidal theory predicts that most locations on Earth should experience two high tides and two low tides each lunar day (approximately 24 hours and 50 minutes)."
  type: true-false
  answer: true
  explanation: "In the equilibrium model, two tidal bulges remain fixed along the Earth-Moon line while Earth rotates beneath them. Any point on the equator therefore passes through both bulges — two high tides — and the two troughs between them — two low tides — per lunar day. This semi-diurnal pattern dominates at most coastlines worldwide. The 50-minute offset from a solar day arises because the Moon advances in its orbit, so Earth must rotate slightly more than 360° to return to the same Moon-relative position."

- question: "Why do tides arise from the differential in gravitational force across Earth's diameter, rather than from the Moon's gravity simply pulling the ocean toward it?"
  type: short-answer
  answer: "If the Moon's gravity pulled uniformly on all of Earth, it would accelerate the entire planet — ocean, land, and core — equally, and no tides would form. What creates tides is the variation in the Moon's pull: stronger on the near side, average at the center, weaker on the far side. This differential stretches the ocean into an elongated shape. On the near side, water is pulled more strongly than Earth's center; on the far side, water is pulled less strongly and is effectively left behind. The tide-generating force is this difference — not the Moon's gravity itself."
  explanation: "This differential origin is why the tide-generating force falls off with the cube of distance rather than the square. Gravity (the average pull) falls as 1/r². The differential across Earth's diameter is proportional to the change in gravity over distance d, which scales as d/r³ — one additional power of distance in the denominator. This is why distance matters so much more for tides than for ordinary gravity, and why the Moon dominates tides despite being far less massive than the Sun."
```

## Explainer

Tides are so familiar — the sea rises and falls twice a day at most coastlines — that it is easy to underestimate the elegance of the physics behind them. The starting point is Newton's law of gravitation: the Moon pulls on every particle of Earth, but it pulls harder on the side of Earth nearest to it and weaker on the far side. What drives tides is not the Moon's gravity itself but the **differential** in that gravity across Earth's diameter. This difference — called the **tide-generating force** — stretches the ocean into an elongated shape with two bulges: one on the side facing the Moon (where the Moon's pull exceeds the average) and one on the opposite side (where the Moon's pull is less than the average, so water is effectively "left behind" relative to Earth's center).

**Equilibrium tidal theory**, developed by Newton, imagines what the ocean would look like if it could respond instantly and perfectly to these forces — as if Earth were entirely covered by a deep, frictionless ocean. In this idealized picture, the two tidal bulges remain fixed along the Earth-Moon line while Earth rotates beneath them. A point on the equator would therefore pass through two high tides and two low tides every lunar day (about 24 hours and 50 minutes, since the Moon advances in its orbit). This is the origin of the **semi-diurnal** tide — two highs and two lows per day — that dominates most of the world's coastlines.

The Sun produces its own pair of tidal bulges by exactly the same mechanism. Although the Sun is far more massive than the Moon, it is also much farther away, and because the tide-generating force falls off with the cube of distance (not the square, as gravity itself does), the Sun's tidal effect is only about 46% as strong as the Moon's. When the Sun and Moon align — at new moon and full moon — their bulges reinforce each other, producing the extra-large tidal range known as **spring tides**. When they are at right angles (first and third quarter moon), the Sun's bulge partially cancels the Moon's, producing the reduced range called **neap tides**. This spring-neap cycle repeats every ~14.8 days, tracking the lunar phases.

Equilibrium theory explains the basic rhythm of tides beautifully, but real tides on Earth deviate from this idealized picture in important ways. Continents block the free flow of water, ocean basins have their own resonant frequencies, and friction with the seafloor dissipates tidal energy. These complications mean that actual tidal ranges, timing, and patterns (some coastlines experience only one tide per day, others have dramatically unequal highs and lows) depend heavily on local geography. Understanding why the Bay of Fundy has 16-meter tides while the Mediterranean barely notices requires dynamic tidal theory, which treats the ocean basins as resonant systems responding to the equilibrium forcing. But the equilibrium framework remains essential: it tells you the forcing — the "input signal" — that all those complex basin responses are reacting to.
