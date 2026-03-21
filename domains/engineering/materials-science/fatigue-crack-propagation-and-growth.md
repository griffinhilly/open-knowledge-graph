---
id: fatigue-crack-propagation-and-growth
title: Fatigue Crack Propagation and Paris Law
domain: engineering
course: materials-science
prerequisites:
- id: fatigue-crack-initiation
  type: hard
- id: stress-intensity-factor-and-fracture
  type: soft
builds-toward:
- fatigue-in-materials
tags:
- fatigue
- crack-propagation
- paris-law
- growth-rate
stage: advanced
status: draft
---

# Fatigue Crack Propagation and Paris Law

## Core Idea
Fatigue cracks propagate incrementally under cyclic loading; the Paris law (da/dN = C·ΔKm) relates crack growth rate to stress intensity range ΔK. Crack propagation occurs in three regimes: near-threshold (low ΔK), Paris power-law regime (intermediate), and unstable growth (ΔK → KIC). Understanding these regimes enables fracture-mechanics-based fatigue life prediction.

## Questions

```yaml
- question: "An engineer doubles the cyclic stress amplitude on a component with a propagating crack. The Paris exponent m = 4. By what factor does the crack growth rate increase?"
  type: multiple-choice
  options:
    - "2× — growth rate is proportional to stress amplitude"
    - "4× — growth rate scales as m times the stress increase"
    - "16× — ΔK scales linearly with stress, so da/dN scales as (2)^4 = 16 times"
    - "8× — stress doubles, but the growing crack also increases ΔK independently"
  answer: 2
  explanation: "The Paris law is da/dN = C·ΔK^m. The stress intensity range ΔK = Yσ√(πa), so ΔK is proportional to σ. Doubling stress doubles ΔK. The growth rate then scales as (2ΔK)^m = 2^m·ΔK^m = 2^4·ΔK^4 = 16 times the original rate. This power-law sensitivity is the key insight: a modest stress increase produces a disproportionately large increase in crack propagation rate, which is why fatigue life is so sensitive to cyclic load amplitude. Linear thinking about stress-life relationships misses this crucial nonlinearity."

- question: "Why does fatigue crack growth accelerate as the crack gets longer, eventually leading to rapid fracture?"
  type: multiple-choice
  options:
    - "Longer cracks are more likely to intersect microstructural defects like grain boundaries"
    - "The stress intensity factor K ∝ √a increases as the crack grows, so ΔK rises and da/dN increases — growth feeds on itself"
    - "The material ahead of a longer crack tip is progressively weakened by accumulated plastic deformation"
    - "Longer cracks expose more surface area to environmental attack, accelerating corrosion-assisted growth"
  answer: 1
  explanation: "The stress intensity factor K = Yσ√(πa) grows with crack length a. As the crack propagates, a increases, so ΔK increases, which increases da/dN according to Paris law (da/dN = C·ΔK^m). This is a self-accelerating process: growth makes the crack longer, which increases the driving force, which accelerates growth further. Eventually ΔK approaches K_IC and fast fracture begins. This acceleration is why most fatigue life is spent in the early Paris regime when the crack is small and ΔK is low — the final crack growth from moderate to critical size occurs relatively quickly."

- question: "Most of a component's fatigue life (in terms of number of cycles) is consumed in the final fast-fracture stage, when the crack is nearly at its critical size."
  type: true-false
  answer: false
  explanation: "This reverses the actual life distribution. Fast fracture is rapid and consumes very few cycles — once ΔK approaches K_IC, the crack accelerates dramatically and failure occurs quickly. The vast majority of fatigue life is spent in the near-threshold and early Paris regime, when the crack is small, ΔK is low, and growth per cycle is tiny. This has a practical implication: inspection intervals should focus on detecting cracks before they grow out of the slow-growth regime, not on the final fast-fracture phase."

- question: "According to the Paris law, a small increase in cyclic stress amplitude causes a disproportionately large increase in crack growth rate."
  type: true-false
  answer: true
  explanation: "The Paris law da/dN = C·ΔK^m is a power law with m typically between 2 and 4 for metals. Since ΔK scales linearly with stress amplitude, a 10% increase in stress causes a 10%^m increase in growth rate — approximately 21% to 46% faster, depending on m. A 2× stress increase causes a 4× to 16× increase in growth rate. This strong nonlinearity means that reducing cyclic stress is far more effective at extending fatigue life than a linear model would suggest, and that small stress concentrations (notches, corrosion pits) can dramatically reduce component life."

- question: "Explain how the Paris law is used to determine inspection intervals in aerospace structures. What information is needed, and what does the calculation tell you?"
  type: short-answer
  answer: "Paris law integration gives the number of cycles for a crack to grow from an initial size a_0 to a critical size a_c. Integrating da/dN = C·ΔK^m from a_0 to a_c yields N_f — the remaining fatigue life. The required inputs are: material constants C and m (measured from fatigue crack growth tests), the geometry factor Y, the applied cyclic stress amplitude σ, the initial crack size a_0 (from inspection detection limits or assumed worst-case flaw), and the critical crack size a_c (where K_max = K_IC). The result tells you how many cycles — or flight hours — remain before the crack reaches critical size. Inspection intervals are set to a fraction of N_f (with safety margin), ensuring cracks are detected and repaired before they become dangerous."
  explanation: "The damage tolerance philosophy underlying aerospace inspection is: assume a crack already exists at the detection threshold size, calculate how long it takes to reach critical size under typical service loads, and inspect at intervals short enough to catch it before then. This is why Paris law integration is safety-critical: it converts fracture mechanics theory into actionable maintenance schedules."
```

## Explainer

Fatigue failure has two distinct phases, and from your study of fatigue crack initiation you already understand the first: a crack nucleates at a surface defect, stress concentration, or inclusion after enough cycles of reversed plasticity. Once a crack exists, the question shifts: how quickly will it grow under continued cyclic loading, and how many cycles remain before it reaches the critical size at which catastrophic fast fracture occurs (K = K_IC)? This is the propagation phase, and it is governed by fracture mechanics.

The central result is the **Paris law**: da/dN = C·ΔK^m, where a is the crack half-length, N is the number of cycles, and ΔK = K_max − K_min is the **stress intensity range** — the cyclic variation in the stress intensity factor you computed using K = Yσ√(πa). The constants C and m are material-specific empirical parameters measured by growing a crack in a test specimen under controlled cyclic loading. For metals, m typically ranges from 2 to 4, meaning that crack growth rate scales as the second to fourth power of the stress intensity range — a steep relationship that makes crack growth strongly sensitive to stress amplitude.

Crack propagation unfolds in **three regimes**. In the near-threshold regime (ΔK < ΔK_th), the crack grows so slowly — or not at all — that it is practically dormant; ΔK_th defines the threshold below which cyclic loading is indefinitely safe. In the **Paris regime** (intermediate ΔK), the log-log plot of da/dN vs ΔK is linear with slope m, and this is where most engineering life is spent. In the fast-fracture regime (ΔK approaching K_IC), the crack accelerates toward instability and the Paris relationship breaks down. The transition points are set by material toughness K_IC and the threshold ΔK_th.

Life prediction using the Paris law requires integrating da/dN from the initial crack size a_0 (from inspection detection limits or assumed flaw size) to the critical crack size a_c (where K_max = K_IC). For a through crack in an infinite plate with m ≠ 2, this integral yields N_f = (a_c^(1−m/2) − a_0^(1−m/2)) / (C·(Yσ_max√π)^m · (1−m/2)). The result quantifies **damage tolerance**: for a given stress amplitude and material, how large a crack can be tolerated before failure? This framework drives inspection intervals in aerospace — if a crack below the detection limit is assumed to exist, how many flights until it grows to critical size? Inspection must occur before that limit with sufficient margin.

Two important modifying factors are the **stress ratio** R = σ_min / σ_max and environment. A high compressive minimum stress (negative R) can close the crack for part of the cycle, reducing the effective ΔK and slowing growth — this is the basis for **crack closure** corrections. Corrosive environments can dramatically accelerate growth by weakening bonds at the crack tip through **stress corrosion cracking** or hydrogen embrittlement, effectively reducing K_IC and increasing the crack growth rate constant C. In practice, Paris law coefficients must be measured in the relevant environment, not just in air, to give conservative life estimates for real service conditions.
