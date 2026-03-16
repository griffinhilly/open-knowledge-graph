---
id: randomized-experiments-development-economics
title: Randomized Controlled Trials and Causal Inference in Development
domain: economics
course: development-economics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: difference-in-differences
  type: soft
- id: probability-spaces-measure-theoretic
  type: soft
- id: conditional-probability
  type: soft
- id: sampling-distributions
  type: soft
builds-toward:
- development-policy-evaluation
tags:
- RCT
- causal inference
- experimentation
- impact evaluation
stage: advanced
status: draft
---

# Randomized Controlled Trials and Causal Inference in Development

## Core Idea
Randomized controlled trials (RCTs) in development, pioneered by Banerjee and Duflo, randomly assign program access to communities to isolate causal effects. This avoids selection bias where beneficiaries differ systematically. RCTs are expensive and raise ethical questions but have revealed surprising findings and become central to evidence-based policy.

## Explainer

From your study of causal inference in econometrics, you know the fundamental problem: we want to know what would have happened to the treated group if they had not received treatment, but we can never observe this counterfactual directly. Observational methods like difference-in-differences construct plausible counterfactuals using assumptions about parallel trends or selection. **Randomized controlled trials (RCTs)** solve the problem more directly: by randomly assigning who receives a program and who does not, randomization ensures that the treatment and control groups are statistically identical in expectation on every dimension — observed and unobserved. Any subsequent difference in outcomes can be attributed to the program itself.

The logic is identical to clinical drug trials, but the application to development economics was revolutionary when Abhijit Banerjee, Esther Duflo, and Michael Kremer began conducting field experiments in the late 1990s. Consider a concrete example: does providing free bed nets reduce malaria more effectively than selling them at subsidized prices? The intuition that charging a small price ensures only motivated users get nets (and therefore use them) seems reasonable. But when Jessica Cohen and Pascaline Dupas ran an RCT in Kenya, randomly varying the price of bed nets across clinics, they found that even small charges drastically reduced take-up with no improvement in usage rates among those who obtained nets. Free distribution was simply more effective. This finding, which contradicted the prevailing policy consensus, would have been nearly impossible to establish convincingly without randomization.

RCTs in development typically work at the community or group level. Researchers partner with an NGO or government rolling out a program — school meals, deworming treatment, microfinance access, teacher incentives — and randomly select which villages, schools, or households receive the program first. The randomization creates the control group. After enough time has passed, researchers compare outcomes (test scores, health indicators, income) between treatment and control groups. Because randomization balanced all pre-existing differences, the average difference in outcomes is an unbiased estimate of the **average treatment effect**.

However, RCTs have important limitations that any practitioner must understand. They are expensive and logistically demanding — maintaining random assignment in the field, preventing contamination between treatment and control groups, and tracking participants over time all require substantial resources. They raise **ethical concerns**: is it acceptable to deliberately withhold a potentially beneficial program from some communities? They answer narrow questions ("did this specific program in this specific context have an effect?") but generalizing to other settings — the problem of **external validity** — requires additional assumptions. And they are best suited to evaluating discrete interventions, not the large-scale institutional or macroeconomic changes (trade policy, governance reform) that may matter most for development. Despite these limitations, RCTs have fundamentally raised the evidentiary bar in development economics and reshaped how donors, governments, and NGOs evaluate what works.
