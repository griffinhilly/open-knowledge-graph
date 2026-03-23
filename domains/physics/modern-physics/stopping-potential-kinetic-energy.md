---
id: stopping-potential-kinetic-energy
title: Stopping Potential and Maximum Kinetic Energy
domain: physics
course: modern-physics
prerequisites:
- id: work-function-photoelectric-analysis
  type: hard
tags:
- quantum-mechanics
- photons
- experimental-verification
stage: advanced
status: validated
---

# Stopping Potential and Maximum Kinetic Energy

## Core Idea
The stopping potential V_s is the reverse voltage needed to stop (turn back) the fastest photoelectrons. Since eV_s = KE_max, the stopping potential directly measures the maximum kinetic energy of emitted electrons. A plot of V_s versus frequency is linear, with slope h/e and intercept −W/e.

## How It's Best Learned
Set up a simple photoelectric apparatus with variable reverse bias. Measure stopping potential as a function of light frequency. Extract Planck's constant and the work function from the data.

## Common Misconceptions
The stopping potential is always the same regardless of light intensity (it depends only on frequency). Below-threshold frequencies produce no current at any (positive) applied voltage.

## Questions

```yaml
- question: "A physicist doubles the intensity of monochromatic light hitting a metal surface while keeping the frequency constant. What happens to the stopping potential?"
  type: multiple-choice
  options:
    - "It doubles, because twice the energy is hitting the surface per second"
    - "It increases, but by less than a factor of two, due to electron-electron interactions"
    - "It remains unchanged, because stopping potential depends only on photon frequency, not intensity"
    - "It decreases, because more electrons compete for the available energy"
  answer: 2
  explanation: "This is the central experimental fingerprint of quantization. Stopping potential measures KE_max = hf − W, which depends only on the frequency of the photons and the work function of the metal. Doubling intensity means twice as many photons per second — so twice as many electrons are ejected (higher photocurrent) — but each photon still carries energy hf, so each emitted electron still has the same maximum kinetic energy. The stopping potential is unchanged. A classical wave model would predict that higher intensity means higher amplitude and thus more energy delivered to each electron — precisely what the experiments refuted."

- question: "A plot of stopping potential V_s versus light frequency f for a metal produces a straight line. The slope of this line equals:"
  type: multiple-choice
  options:
    - "The work function W of the metal"
    - "The threshold frequency f₀ below which no electrons are emitted"
    - "h/e — Planck's constant divided by the elementary charge"
    - "e/h — the elementary charge divided by Planck's constant"
  answer: 2
  explanation: "Rearranging eV_s = hf − W gives V_s = (h/e)f − W/e. This is a linear equation in f with slope h/e and y-intercept −W/e. Since the electron charge e is independently known (from Millikan's oil-drop experiment), measuring the slope of this line gives a direct experimental determination of Planck's constant h. This is historically significant: Millikan's careful measurements of this slope confirmed Einstein's quantum hypothesis and provided one of the first precise values of h."

- question: "The y-intercept of a V_s versus frequency plot is negative, equal to −W/e, where W is the work function of the metal."
  type: true-false
  answer: true
  explanation: "From V_s = (h/e)f − W/e, the y-intercept (the value of V_s when f = 0) is −W/e, which is negative since W > 0. This is physically consistent: at zero frequency there are no photons with enough energy to eject electrons, and the intercept simply reflects the threshold energy barrier. The x-intercept (where V_s = 0) corresponds to f₀ = W/h, the threshold frequency below which no photoemission occurs."

- question: "Increasing the intensity of monochromatic light increases the maximum kinetic energy of emitted photoelectrons, because a higher-amplitude wave delivers more energy to each electron at the surface."
  type: true-false
  answer: false
  explanation: "This is precisely what classical wave theory predicted — and precisely what experiments disproved. In the quantum picture, light consists of photons each carrying energy hf regardless of intensity. Increasing intensity means more photons per second, so more electrons are ejected (higher photocurrent), but each individual photon-electron interaction delivers the same energy hf. KE_max = hf − W is intensity-independent. The classical wave prediction (more intensity → more energy per electron) was falsified by the fact that V_s doesn't change with intensity."

- question: "Why does the experimental relationship between stopping potential and light frequency provide direct evidence for the quantization of light?"
  type: short-answer
  answer: "If light were a classical continuous wave, its energy would scale with intensity (amplitude squared), so higher-intensity light should eject electrons with greater maximum kinetic energy — the stopping potential would depend on intensity. Instead, experiments show that V_s depends linearly on frequency and is completely unaffected by intensity. This can only be explained if light delivers energy in discrete packets (photons) of fixed size hf: each photon-electron interaction transfers exactly hf regardless of how many photons arrive per second. The linear V_s vs. f plot with slope h/e is the direct experimental signature of this quantization."
  explanation: "This is historically one of the cleanest experimental demonstrations that energy quantization is not a mathematical convenience but a physical fact. Millikan set out to disprove Einstein's photon hypothesis and ended up confirming it precisely. The prediction of a linear relationship with slope h/e — and its verification — was a major step in establishing quantum mechanics."
```

## Explainer

From your study of the work function and photoelectric analysis, you know that a photon of energy hf can eject an electron only if hf exceeds the work function W. Any energy left over — hf − W — goes into the kinetic energy of the ejected electron. But electrons inside a metal have a range of energies, so not all ejected electrons carry the same kinetic energy. The **maximum kinetic energy** KE_max belongs to electrons that started at the Fermi surface, where the binding energy is exactly W. Those electrons are the most energetic ones that escape.

The stopping potential V_s is the experimental tool for measuring KE_max precisely. Imagine connecting the photoelectric apparatus in reverse: instead of collecting emitted electrons, you apply a voltage that pushes them back. As you increase the reverse voltage, slower electrons are stopped first. At the exact voltage V_s, even the fastest electrons — those with KE_max — are turned around and never reach the collector. The current drops to zero. The energy equation is simple: the work done by the electric field eV_s must exactly equal the kinetic energy it removes, giving **eV_s = KE_max** = hf − W.

This measurement has a beautiful consequence for extracting fundamental constants. Rearranging: V_s = (h/e)f − W/e. If you plot V_s on the y-axis against light frequency f on the x-axis for different frequencies of light, you get a straight line. The **slope is h/e** — the ratio of Planck's constant to the electron charge. Since e is independently known, this gives a direct experimental determination of h. The **y-intercept is −W/e**, giving the work function of the metal. This linear relationship is precisely what Einstein predicted and Millikan eventually confirmed, and it provided some of the first strong evidence that light comes in discrete quanta.

One critical point reinforces a key lesson about the photoelectric effect: changing the intensity of light at fixed frequency does not change V_s. More intensity means more photons per second, so more electrons are ejected — but each photon still carries the same energy hf, so each ejected electron still has the same maximum KE. The stopping potential is a frequency-dependent quantity, not an intensity-dependent one. This is the experimental fingerprint of quantization: energy comes in fixed-size packets hf, not in continuously variable amounts proportional to wave amplitude.
