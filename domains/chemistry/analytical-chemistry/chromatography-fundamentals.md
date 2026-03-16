---
id: chromatography-fundamentals
title: 'Chromatography: Principles and Theoretical Plate Model'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: analytical-chemistry-intro
  type: hard
- id: intermolecular-forces
  type: hard
- id: colligative-properties
  type: soft
- id: sample-preparation
  type: soft
- id: diffusion-and-ficks-laws
  type: soft
builds-toward:
- gas-chromatography
- hplc
- thin-layer-chromatography
tags:
- chromatography
- stationary phase
- mobile phase
- retention factor
- resolution
- theoretical plates
stage: advanced
status: validated
---
# Chromatography: Principles and Theoretical Plate Model

## Core Idea
Chromatography separates mixtures by differential migration through a system with a stationary phase and a flowing mobile phase; analytes are separated because they partition between the two phases to different extents. The retention factor k = (time in stationary phase)/(time in mobile phase) characterizes analyte affinity. The theoretical plate model treats a column as N discrete equilibration stages; column efficiency N = (tR/σ)² governs peak width. Resolution R = (ΔtR)/(average peak width) must exceed 1.5 for baseline separation and depends on selectivity, efficiency, and retention.

## How It's Best Learned
Calculate N, k, and R from a real chromatogram before exploring how changes in mobile phase, temperature, or column length affect each parameter. The van Deemter equation connecting N to mobile phase velocity illustrates the trade-off between speed and efficiency.

## Common Misconceptions
- More theoretical plates always improve resolution, but only to the extent that selectivity (α) is non-unity — a column with 10,000 plates cannot separate two compounds with identical partition coefficients.
- Peak tailing is not normal; it indicates poor column packing, active sites, or column overloading.

## Questions

```yaml
- question: "A chemist doubles the column length. How does this affect the number of theoretical plates N and the resolution R between two peaks?"
  type: multiple-choice
  options:
    - "N doubles, R doubles"
    - "N doubles, R increases by a factor of √2"
    - "N stays the same, R doubles"
    - "Both N and R increase by a factor of √2"
  answer: 1
  explanation: "N is proportional to column length (N = L/H, where H is plate height), so doubling L doubles N. Resolution R is proportional to √N, so doubling N increases R by √2 ≈ 1.41. The practical implication: to double resolution, you must quadruple column length, which means gains from longer columns are subject to diminishing returns — and increasing selectivity (α) is almost always a more efficient path to better resolution."

- question: "Two compounds with identical partition coefficients can be baseline-separated by using a sufficiently long column with high plate count."
  type: true-false
  answer: false
  explanation: "Resolution depends on both efficiency (N) and selectivity (α = k₂/k₁). If two compounds have identical partition coefficients, α = 1 — they interact identically with both phases and migrate at exactly the same speed. No increase in N will separate them because there is no differential migration. Separation requires changing α by altering mobile phase composition, stationary phase chemistry, or temperature to create a difference in how the compounds interact with the system."

- question: "What does a large retention factor (k >> 1) tell you about an analyte's interaction with the stationary and mobile phases?"
  type: short-answer
  answer: "A large k means the analyte spends much more time in the stationary phase than in the mobile phase — it has strong affinity for the stationary phase relative to the mobile phase, based on favorable intermolecular interactions (e.g., hydrogen bonding, London dispersion). The analyte migrates slowly through the column and elutes late, with a broad, dilute peak."
  explanation: "k = (time in stationary phase)/(time in mobile phase). If k = 10, the analyte spends 10 times as long sorbed onto the stationary phase as it does moving with the mobile phase. Practical chromatography aims for k values between 1 and 10: too small and compounds elute too quickly for good separation; too large and peaks are very broad and take a long time to elute, wasting time and increasing detection limits."
```

## Explainer

Chromatography separates mixtures by exploiting a simple idea: if different molecules prefer different environments to different degrees, and you force them to continuously choose between two phases, they will travel through the system at different speeds and eventually separate. All chromatographic methods share the same fundamental architecture — a stationary phase that stays fixed and a mobile phase that flows through it. Analytes partition between the two phases based on the balance of intermolecular forces you have already studied: polar analytes are retained longer by polar stationary phases; nonpolar analytes prefer nonpolar environments. A compound with strong affinity for the stationary phase lingers there, moving slowly; a compound that prefers the mobile phase travels quickly.

The retention factor k quantifies this preference numerically: k = (time spent in stationary phase) / (time spent in mobile phase). From a chromatogram, you calculate it as k = (tR − tM) / tM, where tR is the analyte's retention time and tM is the dead time (the time a completely unretained compound takes to elute). A k of 0 means no retention (the compound moves at the same speed as the mobile phase); a k of 10 means the analyte spends ten times as long in the stationary phase as in the mobile phase. Practical separations target k values between 1 and 10 — below 1, compounds elute too quickly for good separation; above 10, peaks become excessively broad and run times are impractical.

The theoretical plate model quantifies how efficiently a column performs its job. Borrowed from distillation theory, it imagines the column divided into N discrete equilibration stages ("plates"), each representing one complete equilibration of the analyte between phases. More plates mean more opportunities for differential migration — peaks stay narrower and the column is more efficient. In practice, N is measured from the chromatogram as N = (tR/σ)², where σ is related to peak width. The height equivalent to a theoretical plate (HETP or H = L/N) is the more physically meaningful quantity: a smaller H means more plates per unit length. Sharp, narrow peaks indicate high N; broad peaks indicate low N or column problems.

Resolution R is the ultimate performance metric: R = ΔtR / (average baseline peak width), and R ≥ 1.5 defines baseline separation. The resolution equation R ∝ (√N/4) × (α−1)/α × k/(1+k) reveals three independent levers. Efficiency (√N) is the column quality lever — improved by using longer columns or smaller particle sizes, but with diminishing returns. Retention (k) is the phase chemistry lever — adjusted by changing mobile phase strength or temperature. Most powerfully, selectivity α = k₂/k₁ is the ratio of the two analytes' retention factors; because it enters the equation as (α−1)/α, even a small difference in α has an outsized effect on resolution compared to increasing N. This is why choosing the right stationary phase chemistry or mobile phase composition is far more impactful than simply buying a longer column.

The van Deemter equation extends the plate model by describing how plate height H depends on the mobile phase flow velocity u: H = A + B/u + Cu. The A term (eddy diffusion) captures multiple flow paths through packed particles; the B/u term (longitudinal diffusion) dominates at low velocities; the Cu term (mass transfer resistance) dominates at high velocities. There is an optimal flow velocity u_opt that minimizes H and therefore maximizes N. Running faster than this optimum speeds up the analysis but degrades efficiency — a fundamental trade-off every analytical chemist must balance based on whether speed or resolution is the priority.
