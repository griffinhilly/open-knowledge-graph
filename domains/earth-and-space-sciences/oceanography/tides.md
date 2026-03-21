---
id: tides
title: 'Tides: Gravitational Forcing and Tidal Patterns'
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: newtons-law-of-gravitation
  type: hard
- id: ocean-surface-waves
  type: soft
- id: trigonometric-ratios-review
  type: soft
builds-toward:
- coastal-processes-and-waves
tags:
- tides
- spring tides
- neap tides
- tidal forcing
- amphidromic point
stage: advanced
status: validated
---

# Tides: Gravitational Forcing and Tidal Patterns

## Core Idea
Tides are the periodic rise and fall of sea level caused primarily by the differential gravitational pull of the Moon (and secondarily the Sun) on Earth's ocean. The Moon creates two tidal bulges: one facing the Moon and one on the opposite side due to inertia. As Earth rotates, most locations experience two high tides and two low tides per day (semidiurnal), though geographic and basin resonance effects produce diurnal or mixed tidal patterns in many regions. Spring tides (stronger) occur when the Sun, Earth, and Moon align; neap tides (weaker) occur when they form a right angle.

## How It's Best Learned
Draw diagrams of tidal forcing geometry for new moon, full moon, and quarter moon configurations. Compare tidal gauge records from different coastal stations to observe how geography influences tidal range and pattern.

## Common Misconceptions
- Tides are not caused by the Moon's gravitational pull alone — the differential (tidal) force across Earth's diameter is what matters, not the absolute force.
- The highest tides don't necessarily occur when the Moon is overhead — basin resonance and coastal geometry can shift timing significantly.

## Questions

```yaml
- question: "If the Moon's gravity pulls ocean water toward the Moon, why is there a high tide on the OPPOSITE side of Earth from the Moon simultaneously?"
  type: multiple-choice
  options:
    - "The Sun's gravity counteracts the Moon's pull, pushing water to the far side"
    - "Earth's rotation creates centrifugal force that flings water to the far side"
    - "The tidal force is a differential force: the far side experiences weaker-than-average gravitational pull, so inertia from Earth-Moon orbital motion carries water outward relative to Earth's center"
    - "There is no high tide on the far side; the second daily high tide is caused by Earth rotating through the Moon-side bulge twice"
  answer: 2
  explanation: "This is the most misunderstood aspect of tides. The Moon pulls on Earth as a whole, but the near side is pulled more strongly and the far side more weakly than Earth's center. The tidal force is the difference in gravitational pull from one side to the other. On the far side, the gravitational pull is slightly weaker than average, and the orbital motion (inertia) 'outpaces' gravity slightly, producing a bulge pointing away from the Moon. Both bulges arise from the differential nature of the tidal force, not from two separate mechanisms."

- question: "The Bay of Fundy has the world's largest tidal range (>16 meters). What best explains this, given that its geographic location doesn't make it face the Moon more directly than other places?"
  type: multiple-choice
  options:
    - "It is located at a geographic pole where tidal forces are concentrated"
    - "The bay's funnel shape and length create a natural resonance frequency close to the semidiurnal tidal period, amplifying the tidal signal dramatically"
    - "Exceptionally strong spring tides permanently persist in that region due to local magnetic anomalies"
    - "Deep water in the bay focuses tidal energy, similar to how ocean waves grow in shallow water"
  answer: 1
  explanation: "Basin resonance — not geography relative to the Moon — determines local tidal range. The Bay of Fundy is approximately 270 km long with a natural sloshing period close to 12.4 hours (the semidiurnal tidal period). This near-resonance amplifies each tidal cycle, much like pushing a child on a swing at exactly its natural period. This explains why a location's tidal range can be far larger or smaller than neighboring coastlines."

- question: "Spring tides occur when the Moon is closest to Earth (at perigee), producing stronger gravitational pull."
  type: true-false
  answer: false
  explanation: "Spring tides occur when the Sun, Earth, and Moon are aligned — at new moon and full moon — so the tidal forces of the Sun and Moon add together. This happens twice per month regardless of the Moon's distance from Earth. Perigean spring tides (when spring tides coincide with the Moon's closest orbital approach) are unusually large, but spring tides themselves are defined by alignment, not by lunar distance."

- question: "Most coastal locations experience two high tides per day because Earth rotates through the Moon's gravitational field twice in 24 hours."
  type: true-false
  answer: true
  explanation: "Roughly correct, with an important qualifier: the cycle is 24 hours and 50 minutes, not exactly 24 hours, because the Moon advances in its orbit while Earth rotates. Earth must rotate slightly extra to 'catch up' to the Moon's new position each day. This is why tide times shift by about 50 minutes later each day. Most locations pass through both the near-side and far-side tidal bulges once each, producing two high tides per tidal day."

- question: "Why don't the highest tides occur when the Moon is directly overhead at a given location, and what actually determines the timing of high tide at a specific coast?"
  type: short-answer
  answer: "The tidal bulges from the Moon represent a forcing signal, but each ocean basin responds like a resonant system — water sloshes within the basin at its own natural frequency. The response depends on basin geometry, depth, and how that geometry resonates with the tidal forcing period. Additionally, Coriolis forces rotate the tidal wave around amphidromic points. The result is that the timing of high tide at a specific coast reflects the basin's resonance and geography, not just the Moon's overhead position. High tide can be hours ahead or behind the Moon's transit."
  explanation: "This is why tidal prediction requires harmonic analysis with dozens of constituents rather than simply tracking the Moon's position. The ocean doesn't respond instantaneously — it has its own dynamics. Understanding the difference between tidal forcing (astronomical) and tidal response (oceanographic) is key to predicting real tides."
```

## Explainer

From Newton's law of gravitation, you know that every mass attracts every other mass with a force proportional to their masses and inversely proportional to the square of the distance between them. Tides arise not from the Moon's gravitational pull itself, but from the **differential force** — the difference in gravitational pull across Earth's diameter. The side of Earth facing the Moon is about 12,740 km closer than the far side, so it feels a slightly stronger pull. This difference stretches the ocean into an elongated shape with two bulges: one toward the Moon (where gravity is slightly stronger than average) and one on the opposite side (where gravity is slightly weaker, and inertia from Earth-Moon orbital motion carries the water outward). As Earth rotates through these two bulges roughly once per day, most coastal locations experience two high tides and two low tides in each 24-hour-and-50-minute tidal cycle (the extra 50 minutes accounting for the Moon's orbital advance).

The Sun also exerts a tidal force on Earth's oceans — its enormous mass compensates partly for its much greater distance — but its tidal effect is only about 46% of the Moon's. When the Sun, Earth, and Moon align (at new moon and full moon), their tidal forces add together, producing **spring tides** with the largest tidal ranges. When the Sun and Moon are at right angles relative to Earth (first and third quarter moon), their forces partially cancel, producing **neap tides** with the smallest ranges. This fortnightly cycle between spring and neap tides is one of the most predictable rhythms in the ocean, and you can verify it by checking any tide table for two weeks of data.

If Earth were a smooth sphere uniformly covered by deep ocean, the tidal pattern would be simple and symmetric. But continents, ocean basin shapes, and seafloor topography complicate the picture enormously. Each ocean basin responds to tidal forcing as a resonant system — water sloshes back and forth within the basin like water in a bathtub, and the basin's natural resonance period determines how it amplifies or dampens the tidal signal. The result is a pattern of **amphidromic points** — locations where the tidal range is essentially zero — around which the tidal wave rotates. The Bay of Fundy in Canada has the world's largest tidal range (over 16 meters) not because it faces the Moon most directly, but because its geometry creates a near-perfect resonance with the semidiurnal tidal period.

These geographic effects also explain why some locations experience patterns other than the standard two-highs-two-lows semidiurnal tide. Parts of the Gulf of Mexico have **diurnal tides** (one high and one low per day), while much of the Pacific coast sees **mixed tides** (two unequal highs and lows per day). Tidal prediction uses **harmonic analysis**, decomposing the observed tide into dozens of individual sinusoidal components (called tidal constituents), each corresponding to a specific astronomical forcing frequency. The principal lunar semidiurnal constituent (M₂) is the strongest, but accurate prediction requires summing many constituents. This approach — rooted in the trigonometric ratios you reviewed as a prerequisite — allows tide tables to forecast water levels years in advance with remarkable precision, which is essential for navigation, coastal engineering, and understanding how tidal currents transport sediment and nutrients.
