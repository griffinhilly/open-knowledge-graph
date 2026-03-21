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

## Questions

```yaml
- question: "You record ¹H NMR spectra of N,N-dimethylformamide (DMF) at temperatures from −30°C to 150°C. At −30°C you observe two sharp methyl peaks separated by 40 Hz. At 150°C you observe one sharp peak. Where does this single peak appear in the spectrum?"
  type: multiple-choice
  options:
    - "At the frequency of the more upfield (shielded) methyl peak"
    - "At the population-weighted average frequency of the two original peaks"
    - "At the frequency of the more downfield (deshielded) methyl peak"
    - "Anywhere between the two original peaks, depending on instrumental conditions"
  answer: 1
  explanation: "In the fast-exchange limit, the nucleus switches between both environments so rapidly that it reports only a time-averaged frequency. Since both methyl groups in DMF are present in equal populations (50% each), the single high-temperature peak appears exactly midway between the two slow-exchange peaks. If the two sites had unequal populations (e.g., 70%/30%), the averaged peak would appear 70% of the way toward the major-site frequency. This population-weighted averaging is a hallmark of fast exchange and is distinct from the two-peak slow-exchange pattern."

- question: "A researcher claims that the exchange rate constant at coalescence equals the frequency separation between the two peaks (k = Δν). What is wrong with this statement?"
  type: multiple-choice
  options:
    - "Nothing is wrong — this is the correct coalescence condition"
    - "The correct condition is k = πΔν/√2, which differs numerically from k = Δν"
    - "The exchange rate cannot be determined from the coalescence temperature alone"
    - "Coalescence occurs when k equals π/Δν, the inverse of the frequency separation"
  answer: 1
  explanation: "The correct coalescence condition is k = πΔν/√2 ≈ 2.22Δν, not k = Δν. This is one of the most common quantitative errors in NMR exchange analysis. The coalescence condition is derived from the Bloch equations modified for exchange, and the factor of π/√2 arises from the mathematical criterion for the two peaks to just merge into a single broad hump. Using k = Δν underestimates the rate constant at coalescence by roughly a factor of 2.2, leading to significant errors in activation parameters extracted from Eyring analysis."

- question: "In the fast-exchange limit, NMR reports a single peak at the population-weighted average of the two exchanging sites' resonance frequencies."
  type: true-false
  answer: true
  explanation: "True. When the exchange rate greatly exceeds the frequency separation (k >> πΔν), a nucleus switches environments so rapidly that it effectively samples both during the measurement. The NMR spectrometer records the time-averaged precession frequency: ν_obs = p_A × ν_A + p_B × ν_B, where p_A and p_B are the fractional populations of the two sites. Equal populations (50/50) give a peak exactly midway; unequal populations skew it toward the more abundant site."

- question: "Lowering the temperature of a sample showing fast-exchange NMR behavior will cause the single averaged peak to split immediately into two sharp peaks."
  type: true-false
  answer: false
  explanation: "False. The transition from fast exchange to slow exchange does not produce an immediate clean splitting. Passing through intermediate exchange as temperature decreases, the single peak first *broadens*, then flattens and merges around the coalescence temperature, and only then resolves into two separate (initially broadened, then sharpening) peaks as the temperature continues to fall. The intermediate exchange regime always produces broadened lines — never an abrupt doubling of a sharp peak."

- question: "Explain why intermediate exchange — when the exchange rate is comparable to the frequency separation — causes NMR peaks to broaden and eventually coalesce, rather than simply showing two sharp peaks or one sharp averaged peak."
  type: short-answer
  answer: "Broadening arises from the uncertainty principle applied to frequency. A nucleus must reside in a given environment for time τ to define its resonance frequency with precision ~1/τ. In intermediate exchange, τ is comparable to 1/Δν — the nucleus doesn't stay put long enough to define a precise frequency, introducing frequency uncertainty that manifests as line broadening. As the rate increases further, both environments are sampled so rapidly that neither gives a distinct frequency; a time-averaged frequency dominates and the line resharpens into one peak."
  explanation: "This is the energy-time uncertainty principle applied to NMR line shapes. Exchange contributes an additional dephasing mechanism: each exchange event interrupts the coherent precession of a spin, shortening its transverse coherence time and broadening its peak. When k ≈ Δν, exchange-induced dephasing is maximized (maximum line broadening and coalescence). When k >> Δν, rapid averaging 'motionally narrows' the line to give a single sharp peak. Variable-temperature NMR exploits this: the temperature-dependent line shape encodes the exchange rate at each temperature."
```

## Explainer

You already know from NMR relaxation that nuclear spins in different chemical environments resonate at different frequencies, and that the widths and shapes of NMR peaks carry information about molecular dynamics. **Chemical exchange** adds a new layer: what happens when a nucleus physically moves between two different chemical environments on a timescale comparable to the NMR measurement? The answer is that the spectrum changes dramatically, and analyzing those changes gives you rate constants for the exchange process.

Consider a concrete example: the two methyl groups in N,N-dimethylformamide (DMF). At room temperature, rotation around the C–N bond is slow enough that the two methyls experience distinct chemical environments (one cis to the oxygen, one trans), producing two separate NMR peaks. As you heat the sample, rotation speeds up. The peaks first broaden, then merge into a single broad hump at the **coalescence temperature**, and finally sharpen into one narrow peak at high temperature. This progression from two peaks to one encodes the exchange rate at every temperature.

The physics is governed by the relationship between the **exchange rate k** and the **frequency separation Δν** between the two sites. In the **slow-exchange limit** (k << πΔν), each nucleus stays in one environment long enough to report its distinct frequency — you see two sharp peaks. In the **fast-exchange limit** (k >> πΔν), the nucleus switches environments so rapidly that it reports only the population-weighted average frequency — one sharp peak. The interesting regime is **intermediate exchange**, where k ≈ πΔν. Here the uncertainty principle comes into play: the nucleus does not stay in either environment long enough to define a precise frequency, so both peaks broaden and eventually merge. At the coalescence point, k = πΔν/√2, giving you the rate constant directly from the known frequency separation.

By measuring coalescence temperatures or fitting full line shapes across a temperature range, you extract k at multiple temperatures. Plotting ln(k/T) versus 1/T using the **Eyring equation** yields the activation enthalpy ΔH‡ and entropy ΔS‡ for the exchange process. This connects NMR observables directly to transition-state thermodynamics from your kinetics background. The method is extraordinarily powerful for studying processes on the microsecond-to-millisecond timescale — conformational changes like cyclohexane ring flips, amide bond rotation, tautomerization, and even protein dynamics — all accessible through careful analysis of how NMR line shapes change with temperature.
