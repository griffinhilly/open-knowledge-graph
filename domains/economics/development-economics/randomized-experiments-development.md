---
id: randomized-experiments-development
title: Randomized Experiments in Development Economics
domain: economics
course: development-economics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: hypothesis-testing-regression
  type: soft
- id: probability-theory
  type: hard
- id: sampling-distributions-theory
  type: hard
builds-toward:
- conditional-cash-transfers-cct
tags:
- RCT
- experimental-design
stage: advanced
status: draft
---

# Randomized Experiments in Development Economics

## Core Idea
Randomized Controlled Trials randomly assign treatment (a development program) to some communities and not others, generating credible causal impact estimates. Banerjee and Duflo pioneered this approach in development economics, studying microfinance, education, and health programs. RCTs address selection bias and reverse causality but raise questions about generalizability and policy scalability.

## Explainer

From causal inference, you know the fundamental problem: we want to know what would have happened to treated individuals had they not been treated, but we can never observe both states for the same person. From probability theory and sampling distributions, you understand that random assignment across a large enough sample ensures that treatment and control groups are statistically equivalent in expectation — any difference in outcomes can be attributed to the treatment itself. **Randomized Controlled Trials** (RCTs) in development economics apply this experimental logic to real-world programs, bringing the rigor of clinical trials to questions like whether deworming pills improve school attendance or whether microloans reduce poverty.

The core mechanics are straightforward. Researchers identify a population — say, 200 villages eligible for a new school-feeding program. They randomly assign half the villages to receive the program (treatment group) and half to continue without it (control group). After a specified period, they measure outcomes in both groups: test scores, attendance rates, nutritional status. Because assignment was random, any systematic difference between the groups at the end is the **average treatment effect** of the program. This eliminates **selection bias**, the problem that plagues observational studies. Without randomization, villages that receive feeding programs might be wealthier, better-governed, or more motivated — and any improvement in outcomes could reflect those pre-existing advantages rather than the program itself.

Abhijit Banerjee and Esther Duflo, along with collaborators at the Abdul Latif Jameel Poverty Action Lab (J-PAL), pioneered the systematic use of RCTs in development economics, winning the 2019 Nobel Prize for this work. Their studies produced surprising and policy-relevant findings. Providing free bed nets for malaria prevention was more effective than charging even small amounts, overturning the intuition that cost-sharing increases usage. Adding a second teacher to a classroom had little effect on learning, but hiring a contract teacher accountable to parents did. These results challenged development orthodoxies and shifted billions of dollars in aid allocation toward evidence-backed programs.

RCTs are not without limitations, and understanding them is essential for interpreting results responsibly. **External validity** — whether findings from one context generalize to another — is a persistent concern. A deworming program that raised attendance in Kenya may not work the same way in a Bolivian highland community with different health burdens and school systems. **Scalability** is related: a small, carefully managed pilot may succeed because of intensive researcher oversight that a national rollout cannot replicate. There are also ethical questions — is it acceptable to withhold a potentially beneficial program from the control group? — and practical constraints, since randomization requires the cooperation of governments and NGOs willing to let a coin flip determine who receives services. Despite these limitations, RCTs have fundamentally raised the evidentiary standard in development economics, shifting the field from ideological debates about what should work toward empirical evidence about what actually does.
