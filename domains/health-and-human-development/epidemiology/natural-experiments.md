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
stage: expert
status: validated
---

# Natural Experiments and Quasi-Experimental Design

## Core Idea
Natural experiments leverage exogenous (policy-driven, geographic, or temporal) variation in exposure that is not controlled by individuals or affected by their underlying risk. When assignment is essentially random or unrelated to confounders, natural experiments provide causal evidence comparable to randomized trials despite their observational nature.

## Questions

```yaml
- question: "A researcher studies the effect of air pollution on childhood asthma by comparing children living near a highway to those living far away. A colleague argues this is confounded. Which of the following would best approximate a natural experiment?"
  type: multiple-choice
  options:
    - "Randomly assign children to neighborhoods near or far from a highway"
    - "Compare children near highways built after a zoning change made for traffic reasons unrelated to neighborhood health"
    - "Match children on socioeconomic status before comparing pollution exposure"
    - "Use a very large sample to reduce confounding through statistical averaging"
  answer: 1
  explanation: "A natural experiment requires exogenous variation — assignment driven by forces unrelated to individual health characteristics. A zoning change made for traffic or political reasons (not health reasons) creates variation in highway proximity that mimics random assignment: children near the new highway were not there because of health-related factors. Option A would be a randomized trial. Matching and large samples reduce but do not eliminate confounding from unmeasured factors."

- question: "A regression discontinuity design uses an income threshold: households just below receive a health subsidy; those just above do not. The validity of this design rests on which assumption?"
  type: multiple-choice
  options:
    - "Households on both sides of the threshold were randomly selected from the population"
    - "Households just below and just above the threshold are similar in all other health-relevant characteristics"
    - "The threshold was set without knowledge of household income levels"
    - "The same households appear on both sides of the threshold at different time points"
  answer: 1
  explanation: "A regression discontinuity exploits the assumption that households just below and just above the threshold are essentially identical in all characteristics except their eligibility status. Far from the threshold, many confounders differ between groups. Near the threshold (e.g., $30,100 vs. $29,900 income), the comparison approaches the cleanliness of random assignment. This 'local similarity' is the identifying assumption — it must be argued from context and tested with observable characteristics, not proven."

- question: "Natural experiments can provide causal evidence comparable to randomized controlled trials when the source of exposure variation is exogenous and unrelated to individual risk factors."
  type: true-false
  answer: true
  explanation: "This is the core logic of natural experiments. When exposure is determined by forces external to individuals — policy cutoffs, geographic accidents, weather shocks, lottery assignments — the exposed and unexposed groups are comparable in the way that random assignment creates comparability. The key is that individuals did not select into exposure based on their own characteristics, so the exposure-outcome comparison is not confounded by self-selection."

- question: "Because natural experiments exploit exogenous variation rather than self-selection, their causal estimates automatically generalize to the full population of interest."
  type: true-false
  answer: false
  explanation: "Natural experiments often estimate a Local Average Treatment Effect (LATE) — a causal effect specific to the subpopulation whose exposure was actually changed by the exogenous variation. A policy cutoff provides causal evidence about people near the threshold, not necessarily those far from it. External validity — whether results generalize beyond the specific setting, population, and magnitude of the intervention — is a separate question that requires its own argument."

- question: "What does 'exogenous variation' mean in the context of natural experiments, and why is it the key requirement for supporting causal inference?"
  type: short-answer
  answer: "Exogenous variation is variation in exposure driven by forces external to the individuals being studied — forces unrelated to their health status, behaviors, or risk factors. Policy decisions, geographic boundaries, weather events, and historical infrastructure choices are examples. It is the key requirement because causal inference requires comparing otherwise-identical groups that differ only in their exposure. When exposure is chosen by individuals (endogenous variation), exposed and unexposed groups systematically differ in ways that confound the relationship. Exogenous variation breaks this link: the exposure was determined by something outside the individuals, so it is not systematically related to their characteristics, approximating the exchangeability that randomization creates."
  explanation: "John Snow's cholera study illustrates this: which water supplier a household had was determined by historical infrastructure decisions made before cholera's transmission was understood — not by household health behavior. That historical accident created exogenous variation in water quality, making the comparison between supplier customers nearly as clean as a randomized comparison."
```

## Explainer

You know from the counterfactual framework that causal inference requires comparing what actually happened to what *would have* happened under a different exposure — a comparison that is never directly observable. The entire architecture of epidemiologic study design is an attempt to construct a credible version of that counterfactual comparison. Randomized controlled trials do this by design: random assignment means the exposed and unexposed groups are exchangeable, so the control group's outcomes genuinely represent what the treatment group would have experienced had they not been treated. The problem is that most exposures of interest — poverty, pollution, smoking, diet, childhood adversity — cannot be ethically or practically randomized. Natural experiments are the epidemiologist's way of finding the randomization that the world occasionally provides for free.

A **natural experiment** exploits a source of **exogenous variation** — variation in exposure that is driven by forces external to the individuals being studied and unrelated to their underlying health or risk profile. The classic example is John Snow's cholera investigation: households on different sides of a street happened to receive water from different suppliers (the Southwark and Vauxhall company vs. the Lambeth company), based on historical infrastructure decisions that predated any knowledge of cholera's transmission. That historical accident functioned like random assignment. More recent examples include policy cutoffs (individuals on either side of an income threshold that determines program eligibility), geographic boundaries (counties on either side of a state border with different policies), weather shocks (droughts or floods affecting crop prices), and lottery assignments (military draft lotteries, housing lottery assignments).

The validity of a natural experiment rests on a key assumption: the assignment mechanism is **as-good-as-random** with respect to confounders. This is usually argued, not proven — you assess whether observable characteristics are balanced across exposure groups (as you would after randomization), examine the plausibility of the assignment mechanism, and look for violations like sorting of individuals in anticipation of the policy. A **regression discontinuity design** exploits a sharp threshold: people just below a cutoff serve as the counterfactual for people just above it, on the assumption that just-below and just-above groups are essentially identical except for their exposure status. A **difference-in-differences** design compares changes over time in exposed versus unexposed groups, assuming that in the absence of the exposure, trends would have been parallel. Each design has a specific identifying assumption that can be interrogated.

What natural experiments can and cannot tell you is shaped by the nature of the exogenous variation. Because the variation is often local and specific — a particular policy change, in a particular place, at a particular time — the **external validity** of natural experiment findings may be limited. The effect you estimate may be specific to the population near the threshold, or to the magnitude of the policy change, rather than generalizable to the full range of exposures. This is the **local average treatment effect (LATE)** problem in instrumental variable contexts: the estimated effect pertains to the subpopulation whose exposure was actually changed by the instrument, which may not be representative. Interpreting natural experiment results requires being explicit about what population and what contrast the design is actually estimating.

Natural experiments have produced some of the most influential findings in social epidemiology and health policy precisely because they credibly address confounding in settings where experiments are impossible. The Barker hypothesis about developmental origins of disease, the effect of folic acid fortification on neural tube defects, the long-term effects of early childhood interventions, the health effects of unemployment — all have been illuminated by natural experiments. Their power lies in the fact that the world sometimes creates, through policy accidents, geographic quirks, or natural disasters, the separation of exposure and confounders that experimenters create by design.

