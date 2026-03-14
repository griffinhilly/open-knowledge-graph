---
id: ion-selective-electrodes
title: Ion-Selective Electrodes
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: potentiometry
  type: hard
tags:
- ISE
- glass electrode
- membrane potential
- Nernst equation
- selectivity coefficient
- pH electrode
- fluoride electrode
stage: formal-systems
status: draft
---

# Ion-Selective Electrodes

## Core Idea
An ion-selective electrode (ISE) develops a potential across a membrane that responds preferentially to one target ion, allowing its activity (and, with appropriate calibration, concentration) to be measured potentiometrically. The glass pH electrode is the most familiar example: a thin glass membrane generates a potential proportional to the logarithm of H⁺ activity according to the Nernst equation. Other ISEs use crystalline membranes (fluoride electrode with LaF₃), liquid membranes (calcium electrode with organophosphate ionophore), or polymer membranes doped with selective ionophores. The selectivity coefficient quantifies how much an interfering ion contributes to the measured potential; a smaller coefficient means better selectivity for the target ion.

## How It's Best Learned
Calibrate a fluoride ISE with a series of standards in TISAB (total ionic strength adjustment buffer), construct a Nernst plot of potential vs. log[F⁻], and then measure fluoride in a tap water sample. Observing the near-ideal 59.2/n mV slope and seeing how ionic-strength adjustment matters builds intuition for the technique's strengths and practical requirements.

## Common Misconceptions
- ISEs measure ion activity, not concentration; converting to concentration requires controlling or knowing the ionic strength, which is why total ionic strength adjustment buffers are essential for accurate work.
- No ISE is perfectly selective — the selectivity coefficient is never zero, so high concentrations of interfering ions can bias results even with a supposedly 'selective' electrode.
