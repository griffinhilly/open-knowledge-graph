---
id: chemical-exchange-kinetics-nmr
title: Chemical Exchange Kinetics from NMR Line Shapes
domain: chemistry
course: physical-chemistry
prerequisites:
- id: nmr-relaxation-and-correlation-times
  type: hard
- id: integrated-rate-laws
  type: hard
tags:
- nmr
- kinetics
- exchange
- rate-constants
stage: advanced
status: draft
---

# Chemical Exchange Kinetics from NMR Line Shapes

## Core Idea
When NMR timescales and chemical exchange timescales overlap, two-site exchange broadens or coalesces NMR resonances. Analysis of line shapes as temperature varies yields exchange rates; in the slow-exchange limit, two sharp peaks; in the fast-exchange limit, one averaged peak. This elegant method measures conformational equilibria and kinetics (e.g., ring flips, tautomerization, protein dynamics) on microsecond to millisecond timescales.

## How It's Best Learned
Record temperature-dependent NMR spectra of N,N-dimethylformamide (amide rotation) or cyclohexane (chair flip); measure coalescence temperature; calculate rate constant using the Eyring equation; extract ΔG‡ and compare to computational predictions.

## Common Misconceptions
- Assuming coalescence temperature corresponds to rate constant Δν = k; coalescence occurs at k ≈ πΔν/√2, a different condition. - Thinking only forward and reverse rates matter; simultaneous multiple exchange pathways complicate analysis in multi-site systems.

## Explainer

You already know from NMR relaxation that nuclear spins in different chemical environments resonate at different frequencies, and that the widths and shapes of NMR peaks carry information about molecular dynamics. **Chemical exchange** adds a new layer: what happens when a nucleus physically moves between two different chemical environments on a timescale comparable to the NMR measurement? The answer is that the spectrum changes dramatically, and analyzing those changes gives you rate constants for the exchange process.

Consider a concrete example: the two methyl groups in N,N-dimethylformamide (DMF). At room temperature, rotation around the C–N bond is slow enough that the two methyls experience distinct chemical environments (one cis to the oxygen, one trans), producing two separate NMR peaks. As you heat the sample, rotation speeds up. The peaks first broaden, then merge into a single broad hump at the **coalescence temperature**, and finally sharpen into one narrow peak at high temperature. This progression from two peaks to one encodes the exchange rate at every temperature.

The physics is governed by the relationship between the **exchange rate k** and the **frequency separation Δν** between the two sites. In the **slow-exchange limit** (k << πΔν), each nucleus stays in one environment long enough to report its distinct frequency — you see two sharp peaks. In the **fast-exchange limit** (k >> πΔν), the nucleus switches environments so rapidly that it reports only the population-weighted average frequency — one sharp peak. The interesting regime is **intermediate exchange**, where k ≈ πΔν. Here the uncertainty principle comes into play: the nucleus does not stay in either environment long enough to define a precise frequency, so both peaks broaden and eventually merge. At the coalescence point, k = πΔν/√2, giving you the rate constant directly from the known frequency separation.

By measuring coalescence temperatures or fitting full line shapes across a temperature range, you extract k at multiple temperatures. Plotting ln(k/T) versus 1/T using the **Eyring equation** yields the activation enthalpy ΔH‡ and entropy ΔS‡ for the exchange process. This connects NMR observables directly to transition-state thermodynamics from your kinetics background. The method is extraordinarily powerful for studying processes on the microsecond-to-millisecond timescale — conformational changes like cyclohexane ring flips, amide bond rotation, tautomerization, and even protein dynamics — all accessible through careful analysis of how NMR line shapes change with temperature.
