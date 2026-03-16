---
id: natural-experiments-design
title: Natural Experiments and Quasi-Experimental Design
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: causal-inference-observational-data
  type: hard
- id: research-design-advanced
  type: hard
tags:
- natural-experiments
- quasi-experiments
- policy-variation
- validity-threats
stage: advanced
status: draft
---

# Natural Experiments and Quasi-Experimental Design

## Core Idea
Examines research designs that exploit naturally occurring policy changes, discontinuities, or accidents as quasi-experiments. Covers identification assumptions, threats to internal validity, and methodological issues in leveraging natural experiments. Discusses examples from policy evaluation and organizational research.

## How It's Best Learned
Identify natural experiment variations in your research domain, evaluate whether identification assumptions are plausible, discuss alternative explanations for observed effects.

## Common Misconceptions
- Natural experiments are as good as randomization
- Timing of exposure automatically proves causation
- Natural experiments eliminate all confounding

## Explainer

You already know the core problem in causal inference from observational data: people and units do not randomly select into treatment, so observed differences between treated and untreated groups might reflect pre-existing differences rather than any effect of the treatment itself. **Natural experiments** are cases where some external process — a policy change, an administrative cutoff, a lottery, a natural disaster — creates variation in treatment that is effectively independent of the characteristics that would ordinarily confound it. The appeal is enormous: you get something approximating experimental logic without actually running an experiment.

The canonical example is the **Vietnam draft lottery**, used by Joshua Angrist to estimate the earnings effects of military service. The U.S. Selective Service assigned draft priority by a randomized lottery based on birth date. Men with low lottery numbers faced much higher probability of induction. Crucially, lottery number was unrelated to anything else about a young man's characteristics — it was literally random. This allows comparison of earnings outcomes between men with low and high lottery numbers as if they had been randomly assigned to serve, isolating the causal effect of military service from the selection effects that would plague any simple comparison of veterans and non-veterans.

**Regression discontinuity design (RDD)** exploits a different kind of natural experiment: an administrative cutoff that creates a sharp threshold. If you score 70 or above on an entrance exam, you get the scholarship; below 70, you don't. Students just above and just below the threshold are nearly identical in all respects except which side of the cutoff they fall on — this local comparison yields a valid estimate of the scholarship's effect. Card and Krueger's famous minimum wage study compared fast-food workers just across the New Jersey–Pennsylvania border, using geographic discontinuity as a natural control group. The logic is the same in every case: find a feature of the world that creates as-if random assignment.

The critical skill is evaluating **identification assumptions** — the claims that must hold for the natural experiment to actually identify a causal effect. For a lottery, there must be no sorting around the lottery. For RDD, units can't precisely control which side of the cutoff they land on. For **difference-in-differences** designs, the key assumption is parallel trends: treated and control groups would have followed the same trajectory absent the treatment. None of these assumptions are automatically satisfied; each requires empirical scrutiny and explicit defense. Natural experiments are not equivalent to true randomization — they get closer, but they require careful argument about why the specific variation at hand is plausibly exogenous to the outcome of interest.
