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
status: draft
---

# Field Experiments and Real-World Randomization

## Core Idea
Field experiments implement randomized treatments in real-world settings—organizations, schools, communities—avoiding laboratory artificiality. Challenges unique to field experiments include recruitment and attrition, partial compliance, spillovers (treated units affect untreated), general equilibrium effects (policy-wide impacts), and contextual heterogeneity. Solutions include intention-to-treat analysis, instrumental variables for compliance, and structural modeling. Field experiments have generated policy-relevant evidence in development, education, labor, and public health.

## Explainer

You already know from experimental design that random assignment to treatment and control groups is the gold standard for isolating causal effects — it neutralizes confounders by making groups statistically equivalent before the treatment begins. Field experiments preserve this logic but move it out of the controlled laboratory and into schools, villages, hospitals, or workplaces. The payoff is **external validity**: you are measuring effects on real populations facing real stakes, not college students in a lab answering hypothetical questions. The cost is that the world is messier than a lab, and a field experimenter must manage threats to validity that never arise in controlled settings.

The most fundamental challenge is **partial compliance**: the researcher assigns people to conditions, but not everyone assigned to treatment actually receives it, and some in the control group may find their way to the treatment anyway. Imagine a job training program randomized across neighborhoods — some eligible participants never show up; some ineligible participants find similar training elsewhere. If you simply compare outcomes by actual treatment receipt, you reintroduce self-selection bias, exactly what randomization was meant to eliminate. The solution is **intention-to-treat (ITT) analysis**: compare groups based on assignment, not receipt. ITT gives you a conservative estimate of impact — diluted by non-compliers — but preserves the causal integrity of randomization. When you want the effect for compliers specifically, instrumental variables (using assignment as an instrument for receipt) recover a **Local Average Treatment Effect (LATE)**.

**Spillovers** are a second complication absent from laboratory settings. When a treated unit affects neighboring untreated units — say, a vaccination campaign in treated villages reduces disease in nearby untreated villages through herd immunity — the control group is no longer a clean counterfactual. Your estimate of the treatment effect is deflated because controls also benefit. Researchers handle spillovers by randomizing at a larger unit (entire villages rather than households), by explicitly modeling diffusion, or by constructing buffers between treatment and control clusters. The spillover problem also connects to **general equilibrium effects**: a job training program might help individual participants but, if scaled economy-wide, could affect wages for everyone. Field experiments capture local treatment effects; they can systematically miss what happens when a program runs at full scale.

**Attrition** — participants dropping out of the study before measurement — is particularly dangerous if dropout is related to the treatment. If the most discouraged participants leave a job-training intervention early, you end up measuring outcomes only for those who persisted, introducing selection bias even in an originally randomized study. Researchers check for differential attrition by testing whether dropout rates differ across arms, use bounding analysis (assuming best-case or worst-case outcomes for attriters), and design protocols to minimize dropout. Across all these challenges, the connecting thread is your ethics prerequisite: field experiments involve real people in real situations, and the obligation to obtain informed consent, minimize harm, and treat participants equitably shapes every design choice — from the randomization procedure to when it is ethical to withhold a promising treatment from the control group.
