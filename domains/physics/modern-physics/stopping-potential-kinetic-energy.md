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
status: draft
---

# Stopping Potential and Maximum Kinetic Energy

## Core Idea
The stopping potential V_s is the reverse voltage needed to stop (turn back) the fastest photoelectrons. Since eV_s = KE_max, the stopping potential directly measures the maximum kinetic energy of emitted electrons. A plot of V_s versus frequency is linear, with slope h/e and intercept −W/e.

## How It's Best Learned
Set up a simple photoelectric apparatus with variable reverse bias. Measure stopping potential as a function of light frequency. Extract Planck's constant and the work function from the data.

## Common Misconceptions
The stopping potential is always the same regardless of light intensity (it depends only on frequency). Below-threshold frequencies produce no current at any (positive) applied voltage.

## Explainer

From your study of the work function and photoelectric analysis, you know that a photon of energy hf can eject an electron only if hf exceeds the work function W. Any energy left over — hf − W — goes into the kinetic energy of the ejected electron. But electrons inside a metal have a range of energies, so not all ejected electrons carry the same kinetic energy. The **maximum kinetic energy** KE_max belongs to electrons that started at the Fermi surface, where the binding energy is exactly W. Those electrons are the most energetic ones that escape.

The stopping potential V_s is the experimental tool for measuring KE_max precisely. Imagine connecting the photoelectric apparatus in reverse: instead of collecting emitted electrons, you apply a voltage that pushes them back. As you increase the reverse voltage, slower electrons are stopped first. At the exact voltage V_s, even the fastest electrons — those with KE_max — are turned around and never reach the collector. The current drops to zero. The energy equation is simple: the work done by the electric field eV_s must exactly equal the kinetic energy it removes, giving **eV_s = KE_max** = hf − W.

This measurement has a beautiful consequence for extracting fundamental constants. Rearranging: V_s = (h/e)f − W/e. If you plot V_s on the y-axis against light frequency f on the x-axis for different frequencies of light, you get a straight line. The **slope is h/e** — the ratio of Planck's constant to the electron charge. Since e is independently known, this gives a direct experimental determination of h. The **y-intercept is −W/e**, giving the work function of the metal. This linear relationship is precisely what Einstein predicted and Millikan eventually confirmed, and it provided some of the first strong evidence that light comes in discrete quanta.

One critical point reinforces a key lesson about the photoelectric effect: changing the intensity of light at fixed frequency does not change V_s. More intensity means more photons per second, so more electrons are ejected — but each photon still carries the same energy hf, so each ejected electron still has the same maximum KE. The stopping potential is a frequency-dependent quantity, not an intensity-dependent one. This is the experimental fingerprint of quantization: energy comes in fixed-size packets hf, not in continuously variable amounts proportional to wave amplitude.
