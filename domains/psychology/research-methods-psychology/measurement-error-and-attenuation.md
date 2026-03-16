---
id: measurement-error-and-attenuation
title: Measurement Error and Attenuation of Effects
domain: psychology
course: research-methods-psychology
prerequisites:
- id: construct-definition-and-measurement
  type: hard
- id: reliability-in-measurement
  type: soft
builds-toward:
- effect-size-reporting-interpretation
- sample-size-determination-practical-application
tags:
- measurement
- error
- reliability
stage: abstract-reasoning
status: draft
---

# Measurement Error and Attenuation of Effects

## Core Idea
All psychological measurements contain random error that weakens the observed relationships between variables. This phenomenon, called attenuation, means that unreliable measures produce correlations and effect sizes smaller than the true relationship. Understanding how reliability affects statistical power is critical for interpreting null findings and planning adequate measurement precision.

## How It's Best Learned
Calculate disattenuated correlations using the formula: true correlation = observed correlation / sqrt(reliability_x × reliability_y). Compare power analyses with instruments of different reliabilities (e.g., α = .60 vs. α = .90) to show how measurement error requires larger sample sizes.

## Common Misconceptions
- If an instrument has moderate reliability (e.g., α = .70), it's still acceptable and doesn't substantially reduce power; attenuation is proportional—.70 reliability reduces correlations by ~30%.
- Increasing sample size compensates for low measurement reliability; attenuation cannot be recovered through larger N, only through better measurement.
- Random measurement error is negligible compared to systematic bias; random error directly reduces effect sizes and statistical power.

## Explainer

Your prerequisite on reliability in measurement established that reliability indexes how consistently an instrument measures — whether you get the same result when nothing has actually changed. This topic connects that concept to its statistical consequences. Unreliable measurement doesn't just add noise; it systematically shrinks the relationships you can observe between variables. This shrinkage is called **attenuation**, and understanding it is essential for interpreting research honestly.

Here is the core insight: every observed score is a combination of the true score and random error. When you correlate two measures, you're correlating two mixtures of signal and noise. The noise in each measure is uncorrelated with everything — including the noise in the other measure — so it dilutes the relationship. Formally, the expected observed correlation between two variables is the true (latent) correlation multiplied by the geometric mean of their reliabilities: r_observed = r_true × √(r_xx × r_yy). If both instruments have reliability .81, you'd observe only 81% of the true correlation. If both have reliability .64, you'd observe only 64%. The **disattenuation formula** inverts this: r_true = r_observed / √(r_xx × r_yy), letting you estimate what the true relationship would be with perfect measurement.

To make this concrete: suppose the true correlation between conscientiousness and job performance is .40, and your conscientiousness scale has reliability .70 while your job performance rating has reliability .60. Your expected observed correlation is .40 × √(.70 × .60) = .40 × .648 ≈ .26. You set up a study to detect a moderate effect, powered for r ≈ .40, but you actually observe r ≈ .26 — underpowered by a wide margin. You may conclude the relationship is weaker than it is, or miss it entirely. This is why many classic null results in psychology have been reinterpreted after improvements in measurement: the relationship was always there; the instruments were too noisy to reveal it.

The critical practical implication is that **attenuation cannot be fixed by increasing sample size**. Adding more participants increases your power to detect whatever effect exists in your data, but the observed effect is already attenuated. Doubling N from 100 to 200 does not change the fact that your r of .26 represents a true r of .40; it just makes you more confident in the attenuated estimate. The only way to recover the true effect size is to improve the reliability of your measures. This is why measurement quality is not a secondary concern in research design — it determines the ceiling on what you can detect, and no amount of statistical power can raise that ceiling if your instruments are noisy.
