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

## Explainer

Fatigue failure has two distinct phases, and from your study of fatigue crack initiation you already understand the first: a crack nucleates at a surface defect, stress concentration, or inclusion after enough cycles of reversed plasticity. Once a crack exists, the question shifts: how quickly will it grow under continued cyclic loading, and how many cycles remain before it reaches the critical size at which catastrophic fast fracture occurs (K = K_IC)? This is the propagation phase, and it is governed by fracture mechanics.

The central result is the **Paris law**: da/dN = C·ΔK^m, where a is the crack half-length, N is the number of cycles, and ΔK = K_max − K_min is the **stress intensity range** — the cyclic variation in the stress intensity factor you computed using K = Yσ√(πa). The constants C and m are material-specific empirical parameters measured by growing a crack in a test specimen under controlled cyclic loading. For metals, m typically ranges from 2 to 4, meaning that crack growth rate scales as the second to fourth power of the stress intensity range — a steep relationship that makes crack growth strongly sensitive to stress amplitude.

Crack propagation unfolds in **three regimes**. In the near-threshold regime (ΔK < ΔK_th), the crack grows so slowly — or not at all — that it is practically dormant; ΔK_th defines the threshold below which cyclic loading is indefinitely safe. In the **Paris regime** (intermediate ΔK), the log-log plot of da/dN vs ΔK is linear with slope m, and this is where most engineering life is spent. In the fast-fracture regime (ΔK approaching K_IC), the crack accelerates toward instability and the Paris relationship breaks down. The transition points are set by material toughness K_IC and the threshold ΔK_th.

Life prediction using the Paris law requires integrating da/dN from the initial crack size a_0 (from inspection detection limits or assumed flaw size) to the critical crack size a_c (where K_max = K_IC). For a through crack in an infinite plate with m ≠ 2, this integral yields N_f = (a_c^(1−m/2) − a_0^(1−m/2)) / (C·(Yσ_max√π)^m · (1−m/2)). The result quantifies **damage tolerance**: for a given stress amplitude and material, how large a crack can be tolerated before failure? This framework drives inspection intervals in aerospace — if a crack below the detection limit is assumed to exist, how many flights until it grows to critical size? Inspection must occur before that limit with sufficient margin.

Two important modifying factors are the **stress ratio** R = σ_min / σ_max and environment. A high compressive minimum stress (negative R) can close the crack for part of the cycle, reducing the effective ΔK and slowing growth — this is the basis for **crack closure** corrections. Corrosive environments can dramatically accelerate growth by weakening bonds at the crack tip through **stress corrosion cracking** or hydrogen embrittlement, effectively reducing K_IC and increasing the crack growth rate constant C. In practice, Paris law coefficients must be measured in the relevant environment, not just in air, to give conservative life estimates for real service conditions.
