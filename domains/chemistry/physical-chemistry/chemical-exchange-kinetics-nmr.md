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
