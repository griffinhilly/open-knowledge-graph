---
id: natural-experiments
title: Natural Experiments and Quasi-Experimental Design
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: counterfactual-framework
  type: soft
builds-toward:
- regression-discontinuity-design
- difference-in-differences
- synthetic-control-methods
tags:
- quasi-experimental
- exogenous-variation
- policy-evaluation
stage: advanced
status: draft
---

# Natural Experiments and Quasi-Experimental Design

## Core Idea
Natural experiments leverage exogenous (policy-driven, geographic, or temporal) variation in exposure that is not controlled by individuals or affected by their underlying risk. When assignment is essentially random or unrelated to confounders, natural experiments provide causal evidence comparable to randomized trials despite their observational nature.

## Explainer

You know from the counterfactual framework that causal inference requires comparing what actually happened to what *would have* happened under a different exposure — a comparison that is never directly observable. The entire architecture of epidemiologic study design is an attempt to construct a credible version of that counterfactual comparison. Randomized controlled trials do this by design: random assignment means the exposed and unexposed groups are exchangeable, so the control group's outcomes genuinely represent what the treatment group would have experienced had they not been treated. The problem is that most exposures of interest — poverty, pollution, smoking, diet, childhood adversity — cannot be ethically or practically randomized. Natural experiments are the epidemiologist's way of finding the randomization that the world occasionally provides for free.

A **natural experiment** exploits a source of **exogenous variation** — variation in exposure that is driven by forces external to the individuals being studied and unrelated to their underlying health or risk profile. The classic example is John Snow's cholera investigation: households on different sides of a street happened to receive water from different suppliers (the Southwark and Vauxhall company vs. the Lambeth company), based on historical infrastructure decisions that predated any knowledge of cholera's transmission. That historical accident functioned like random assignment. More recent examples include policy cutoffs (individuals on either side of an income threshold that determines program eligibility), geographic boundaries (counties on either side of a state border with different policies), weather shocks (droughts or floods affecting crop prices), and lottery assignments (military draft lotteries, housing lottery assignments).

The validity of a natural experiment rests on a key assumption: the assignment mechanism is **as-good-as-random** with respect to confounders. This is usually argued, not proven — you assess whether observable characteristics are balanced across exposure groups (as you would after randomization), examine the plausibility of the assignment mechanism, and look for violations like sorting of individuals in anticipation of the policy. A **regression discontinuity design** exploits a sharp threshold: people just below a cutoff serve as the counterfactual for people just above it, on the assumption that just-below and just-above groups are essentially identical except for their exposure status. A **difference-in-differences** design compares changes over time in exposed versus unexposed groups, assuming that in the absence of the exposure, trends would have been parallel. Each design has a specific identifying assumption that can be interrogated.

What natural experiments can and cannot tell you is shaped by the nature of the exogenous variation. Because the variation is often local and specific — a particular policy change, in a particular place, at a particular time — the **external validity** of natural experiment findings may be limited. The effect you estimate may be specific to the population near the threshold, or to the magnitude of the policy change, rather than generalizable to the full range of exposures. This is the **local average treatment effect (LATE)** problem in instrumental variable contexts: the estimated effect pertains to the subpopulation whose exposure was actually changed by the instrument, which may not be representative. Interpreting natural experiment results requires being explicit about what population and what contrast the design is actually estimating.

Natural experiments have produced some of the most influential findings in social epidemiology and health policy precisely because they credibly address confounding in settings where experiments are impossible. The Barker hypothesis about developmental origins of disease, the effect of folic acid fortification on neural tube defects, the long-term effects of early childhood interventions, the health effects of unemployment — all have been illuminated by natural experiments. Their power lies in the fact that the world sometimes creates, through policy accidents, geographic quirks, or natural disasters, the separation of exposure and confounders that experimenters create by design.

