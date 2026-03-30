---
id: field-experiments-real-world
title: Field Experiments and Real-World Randomization
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: experimental-design-social
  type: hard
- id: research-ethics-human-subjects
  type: hard
builds-toward:
- policy-experiments-evaluation
- scaling-field-experiments
tags:
- experiments
- field
- policy
- randomized
stage: advanced
status: validated
---

# Field Experiments and Real-World Randomization

## Core Idea
Field experiments implement randomized treatments in real-world settings—organizations, schools, communities—avoiding laboratory artificiality. Challenges unique to field experiments include recruitment and attrition, partial compliance, spillovers (treated units affect untreated), general equilibrium effects (policy-wide impacts), and contextual heterogeneity. Solutions include intention-to-treat analysis, instrumental variables for compliance, and structural modeling. Field experiments have generated policy-relevant evidence in development, education, labor, and public health.

## Questions

```yaml
- question: "A randomized job-training program assigns 500 people to training and 500 to a control group. Only 60% of the treatment group attends. A researcher compares outcomes for actual attendees vs. the control group to estimate training's effect. This approach:"
  type: multiple-choice
  options:
    - "Is valid because randomization still holds for the subsample who chose to attend"
    - "Re-introduces self-selection bias, because attendees likely differ systematically from non-attendees in motivation or ability"
    - "Is conservative and will underestimate the true treatment effect for attendees"
    - "Is the most informative approach because it measures the effect on people who actually received training"
  answer: 1
  explanation: "This is the key mistake that intention-to-treat analysis is designed to prevent. People who chose to attend training differ from those who didn't — in motivation, circumstances, distance to the training site, and other factors correlated with outcomes. Comparing attendees to controls reintroduces exactly the self-selection bias that randomization eliminated. Option C is half-right (it might underestimate the effect), but the fundamental problem is bias, not just attenuation. Option D tempts because 'effect on those who actually received it' sounds like what we want, but it cannot be recovered by simple comparison of compliers vs. controls."

- question: "A vaccination field experiment randomizes villages to a high-coverage vaccination program or no program. After two years, disease rates fall in both treatment and control villages. The most likely explanation is:"
  type: multiple-choice
  options:
    - "Differential attrition — sicker people dropped out of the control group, making it look healthier"
    - "Spillovers — vaccination in treated villages reduced disease transmission to nearby control villages through herd immunity effects"
    - "Regression to the mean — disease rates in the control group were unusually high at baseline"
    - "General equilibrium effects — a government-wide vaccination campaign ran simultaneously"
  answer: 1
  explanation: "Spillovers occur when treatment in one unit affects neighboring untreated units — in this case, herd immunity reduces pathogen circulation across village boundaries. When this happens, the control group is no longer a clean counterfactual: controls benefit from the treatment, so the difference between treatment and control understates the true effect. The solution is to randomize at a larger unit (e.g., districts rather than villages) and to explicitly model or buffer against spillover. Option D (general equilibrium) is a different mechanism and would typically produce larger, nationwide effects."

- question: "Intention-to-treat analysis compares participants based on whether they actually received the treatment, to get the most precise estimate of the intervention's real-world impact."
  type: true-false
  answer: false
  explanation: "Intention-to-treat (ITT) analysis compares participants based on their *assigned* condition, not their actual receipt. ITT preserves the causal integrity of randomization by keeping the comparison groups as they were constituted by random assignment. Comparing by actual receipt re-introduces self-selection. The cost of ITT is that the estimated effect is diluted by non-compliers — it is a conservative estimate of the full treatment effect — but it is unbiased. The statement in the question describes the per-protocol analysis, which sacrifices causal validity for apparent precision."

- question: "In a randomized field experiment, if dropout from the study is unrelated to the experimental condition, attrition does not threaten the validity of causal inference."
  type: true-false
  answer: true
  explanation: "The danger of attrition is *differential* attrition — when dropout rates or dropout types differ between treatment and control groups, reintroducing selection bias into groups that were initially balanced by randomization. If attrition is random with respect to condition (equal rates and patterns across arms), the remaining samples are still comparable, and causal inference is preserved. Researchers test for differential attrition by checking whether dropout rates and baseline characteristics of dropouts differ across conditions."

- question: "What is intention-to-treat analysis, and why does it preserve causal validity even when many assigned participants don't comply with their condition?"
  type: short-answer
  answer: "Intention-to-treat (ITT) analysis estimates effects by comparing groups as defined by random assignment, regardless of whether participants actually received the treatment. Because randomization made the groups statistically equivalent before the study began, any outcome difference between assigned groups can be causally attributed to the assignment — even if many people didn't comply. Analyzing by actual receipt breaks this guarantee because compliers and non-compliers differ systematically, reintroducing confounding. ITT estimates are conservative (diluted by non-compliers) but unbiased."
  explanation: "The logic is that randomization is a valid instrument for treatment receipt: assignment is randomly determined, affects receipt, and affects outcomes only through receipt. This is the IV setup. ITT uses assignment directly; if you want the effect specifically for compliers, instrumental variables (using assignment as an instrument for receipt) recover a Local Average Treatment Effect (LATE). The choice between ITT and LATE depends on the policy question: ITT answers 'what happens when you roll out this program?' (realistic, since compliance will be imperfect); LATE answers 'what is the effect for those who actually take up the treatment when offered?'"
```

## Explainer

You already know from experimental design that random assignment to treatment and control groups is the gold standard for isolating causal effects — it neutralizes confounders by making groups statistically equivalent before the treatment begins. Field experiments preserve this logic but move it out of the controlled laboratory and into schools, villages, hospitals, or workplaces. The payoff is **external validity**: you are measuring effects on real populations facing real stakes, not college students in a lab answering hypothetical questions. The cost is that the world is messier than a lab, and a field experimenter must manage threats to validity that never arise in controlled settings.

The most fundamental challenge is **partial compliance**: the researcher assigns people to conditions, but not everyone assigned to treatment actually receives it, and some in the control group may find their way to the treatment anyway. Imagine a job training program randomized across neighborhoods — some eligible participants never show up; some ineligible participants find similar training elsewhere. If you simply compare outcomes by actual treatment receipt, you reintroduce self-selection bias, exactly what randomization was meant to eliminate. The solution is **intention-to-treat (ITT) analysis**: compare groups based on assignment, not receipt. ITT gives you a conservative estimate of impact — diluted by non-compliers — but preserves the causal integrity of randomization. When you want the effect for compliers specifically, instrumental variables (using assignment as an instrument for receipt) recover a **Local Average Treatment Effect (LATE)**.

**Spillovers** are a second complication absent from laboratory settings. When a treated unit affects neighboring untreated units — say, a vaccination campaign in treated villages reduces disease in nearby untreated villages through herd immunity — the control group is no longer a clean counterfactual. Your estimate of the treatment effect is deflated because controls also benefit. Researchers handle spillovers by randomizing at a larger unit (entire villages rather than households), by explicitly modeling diffusion, or by constructing buffers between treatment and control clusters. The spillover problem also connects to **general equilibrium effects**: a job training program might help individual participants but, if scaled economy-wide, could affect wages for everyone. Field experiments capture local treatment effects; they can systematically miss what happens when a program runs at full scale.

**Attrition** — participants dropping out of the study before measurement — is particularly dangerous if dropout is related to the treatment. If the most discouraged participants leave a job-training intervention early, you end up measuring outcomes only for those who persisted, introducing selection bias even in an originally randomized study. Researchers check for differential attrition by testing whether dropout rates differ across arms, use bounding analysis (assuming best-case or worst-case outcomes for attriters), and design protocols to minimize dropout. Across all these challenges, the connecting thread is your ethics prerequisite: field experiments involve real people in real situations, and the obligation to obtain informed consent, minimize harm, and treat participants equitably shapes every design choice — from the randomization procedure to when it is ethical to withhold a promising treatment from the control group.
