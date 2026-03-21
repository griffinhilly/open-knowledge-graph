---
id: natural-experiments-identification-strategy
title: 'Natural Experiments: Quasi-Random Assignment for Causal Identification'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: causal-inference-from-observation
  type: hard
- id: natural-experiments-design
  type: soft
- id: conditional-probability
  type: soft
builds-toward:
- regression-discontinuity-sharp-fuzzy
tags:
- natural-experiments
- quasi-random
- causal-identification
stage: advanced
status: draft
---

# Natural Experiments: Quasi-Random Assignment for Causal Identification

## Core Idea
Natural experiments exploit quasi-random variation in treatment assignment from policy changes or institutional rules. When assignment is plausibly independent of unmeasured confounders, they identify causal effects. Credibility depends on the plausibility of independence.

## Questions

```yaml
- question: "Researchers use geographic proximity to a job training center as a natural experiment to study the effect of training on earnings. Participants near the center are more likely to enroll. What is the key threat to validity they must address?"
  type: multiple-choice
  options:
    - "Proximity is invalid as an instrument because it was not randomly assigned by the researchers"
    - "Proximity may affect earnings through channels other than training — for example, people near job centers may have better commute options or different social networks — violating the exclusion restriction"
    - "The study should have used a randomized control trial instead of a natural experiment"
    - "Geographic proximity can only be used in regression discontinuity designs, not as an instrument"
  answer: 1
  explanation: "The exclusion restriction requires that the assignment variable (here, proximity) affects outcomes ONLY through the treatment channel (training enrollment), not through any other pathway. But proximity to a job center plausibly correlates with urban density, transportation access, and local labor markets — all of which affect earnings independently of training. If so, proximity is not a clean instrument even if it predicts enrollment. This is the most common and serious threat to natural experiment credibility: the assignment mechanism leaking into the outcome through other routes."

- question: "What is the main advantage of a well-designed natural experiment over a traditional observational study with careful statistical controls?"
  type: multiple-choice
  options:
    - "Natural experiments require smaller sample sizes because quasi-random assignment is statistically more efficient"
    - "Natural experiments eliminate both observable and unobservable confounders through quasi-random assignment, whereas statistical controls only address observed confounders"
    - "Natural experiments allow researchers to directly manipulate and vary the treatment of interest"
    - "Natural experiments produce more generalizable results because they always use representative population samples"
  answer: 1
  explanation: "This is the fundamental advantage. In observational studies, even with extensive controls, unmeasured confounders can bias estimates — you can only control what you measured. When assignment is quasi-random (as in the Vietnam draft lottery), treatment and control groups should be balanced on ALL pre-treatment characteristics, measured or not, because the assignment mechanism was independent of them. This eliminates confounding from unobservables — something no statistical control procedure can do. The cost is that valid natural experiments are rare and require substantive institutional arguments."

- question: "In the Vietnam draft lottery study, men with low lottery numbers (who were more likely to serve) and men with high lottery numbers should have had statistically similar pre-lottery characteristics — and researchers verify this as a check on the design's validity."
  type: true-false
  answer: true
  explanation: "Balance tests on pre-treatment covariates are a standard validity check for natural experiments, analogous to what you would check after randomization. If lottery number assignment truly was independent of background characteristics (as it should be, given it was a literal lottery), men with low and high numbers should look similar on average across education, income, geography, and other variables measured before the lottery. Finding imbalance would suggest the lottery wasn't fully independent of these characteristics, threatening the design."

- question: "Demonstrating statistical balance on observed pre-treatment covariates is sufficient to establish the credibility of a natural experiment's identification strategy."
  type: true-false
  answer: false
  explanation: "Balance on observable covariates is necessary but not sufficient. The harder requirement is the exclusion restriction: the quasi-random assignment must affect outcomes only through the treatment, not through any other pathway. This cannot be tested statistically — it requires a substantive argument about the assignment mechanism itself. For instance, if draft lottery numbers had correlated with birth month and birth month affects health (via seasonal effects), balance on standard demographics wouldn't catch it. The identification strategy must be defended on institutional and logical grounds, not just statistical ones."

- question: "What is the exclusion restriction, and why does a natural experiment live or die by it?"
  type: short-answer
  answer: "The exclusion restriction requires that the quasi-random assignment variable affects the outcome only through the treatment channel being studied, not through any other pathway. A natural experiment's causal claim rests entirely on this: if the assignment mechanism has other routes to the outcome, the estimated effect conflates the treatment's impact with those other influences, and causal identification fails. Satisfying this restriction requires a substantive argument about the specific institutional or chance mechanism, not just statistical balance."
  explanation: "Consider the draft lottery: lottery number assignment must affect later earnings only through military service. If low lottery numbers also correlated with geography, and geography affects earnings through local labor markets, the design is compromised even if lottery numbers predicted service. The exclusion restriction is what makes natural experiments a distinct methodology from observation with controls — it's a claim about the world (this mechanism is clean), not just a statistical property (these variables are balanced)."
```

## Explainer

From causal inference with observational data, you know the core problem: treatment and control groups in naturally occurring data usually differ in ways that are correlated with outcomes, making it impossible to isolate the effect of the treatment. Natural experiments don't solve this by randomizing — a researcher didn't design them. Instead, they find situations where the world, through chance or administrative rule, *effectively* randomized treatment. The causal credibility of the study rides entirely on the plausibility of that claim.

The canonical example is the Vietnam-era draft lottery. To study the effects of military service on later-life earnings, economists couldn't randomly assign men to serve — that happened decades ago. But the draft lottery in 1969 literally randomized eligibility by birth date. Men born on dates randomly drawn early were much more likely to serve than those drawn late. This lottery assignment is a natural experiment: men with low lottery numbers didn't choose to have low lottery numbers, so their pre-lottery characteristics should be statistically indistinguishable from men with high lottery numbers. Any difference in later outcomes can be attributed to the difference in military service exposure. The economist Joshua Angrist used exactly this design to estimate the earnings effect of Vietnam service.

What makes a natural experiment credible isn't just that assignment *happened* to look quasi-random — you have to argue it *was* quasi-random for reasons that don't also affect the outcome through other paths. This is the **exclusion restriction**: the quasi-random assignment affects outcomes *only through* the treatment channel you're studying. If lottery numbers had been correlated with geography, and geography affected earnings through other mechanisms, the design would be compromised. Researchers document this by showing that pre-treatment characteristics are balanced across treatment and control groups — exactly as you'd check in a randomized experiment.

Several institutional patterns reliably generate natural experiments. **Cutoff rules** — age eligibility for programs, test score thresholds for selective schools, income limits for benefits — create sharp discontinuities where people just above and just below a threshold are nearly identical except for treatment status. This is the logic of **regression discontinuity design**: estimate the treatment effect by comparing outcomes in a narrow band around the cutoff, where assignment is as good as random. **Policy rollouts** that are phased in across regions or time create quasi-experimental variation: regions treated earlier can be compared to those treated later on observable outcomes. **Geographic boundaries** sometimes generate natural experiments when similar populations face different policies on either side of a border.

The key distinction from standard observational analysis is that in a natural experiment you are not primarily controlling for observable confounders through regression — you are arguing that the quasi-random assignment mechanism has already eliminated confounding, observable and unobservable alike. This is a much stronger claim, and it requires a much more specific argument about the particular institutional or chance mechanism that generated the variation. The credibility of the identification strategy is the thing being defended, and it must be defended substantively, not just statistically. Strong natural experiments are rare and valuable precisely because the conditions for quasi-random assignment are hard to find in real social processes.
