---
id: cost-effectiveness-analysis
title: Cost-Effectiveness Analysis in Policy Research
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: research-design-advanced
  type: hard
- id: linear-regression-social-science
  type: soft
- id: linear-programming
  type: soft
builds-toward:
- health-economic-evaluation
- return-on-investment-analysis
tags:
- policy
- evaluation
- economics
- efficiency
stage: advanced
status: draft
---

# Cost-Effectiveness Analysis in Policy Research

## Core Idea
Cost-effectiveness analysis (CEA) compares the costs and health or social benefits of interventions. The cost-effectiveness ratio divides cost by benefit (e.g., cost per QALY gained); interventions are ranked by efficiency. CEA informs resource allocation but requires defining what counts as a benefit and willingness-to-pay thresholds. Unlike randomized trials, CEA is observational and depends on assumptions about cost attribution and benefit measurement. CEA is widely used in public health, education, and social policy.

## Explainer

You know from your advanced research design background that not all interventions produce equal outcomes, and from regression that we can model relationships between variables. Cost-effectiveness analysis asks a harder question: given limited resources, which interventions produce the most benefit per dollar spent? It is the tool that forces a comparison that policy debates often avoid — not "does this program work?" but "does it work well enough given what it costs, relative to alternatives?"

The core calculation is the **cost-effectiveness ratio (CER)**: total program cost divided by total units of benefit produced. In health care, the standard benefit unit is the **Quality-Adjusted Life Year (QALY)** — one year lived in perfect health, with health states below perfect health assigned fractional weights. An intervention costing $50,000 that produces 5 QALYs has a CER of $10,000 per QALY. Whether that is "good" depends on the **willingness-to-pay threshold**: the maximum a payer is willing to spend per unit of benefit. UK health authorities use roughly £20,000–30,000 per QALY; interventions below the threshold are typically funded, those above face scrutiny. The threshold is itself a policy choice, not a mathematical fact.

The deeper challenge is defining and measuring the benefit unit. QALY calculations require judgments about the quality weight assigned to health states — living with diabetes counts as less than a full QALY per year, but how much less? These weights are elicited through surveys and involve normative assumptions about which lives are worth how much. In social policy (education, crime prevention, workforce training), defining a comparable unit is even harder. What is the "benefit unit" for a literacy program? Lifetime earnings? Crime reduction? Social mobility? The choice of benefit metric embeds value judgments that CEA cannot resolve on its own.

Your regression skills are directly relevant to CEA's empirical side. Program costs are rarely simple line items — analysts must attribute overhead, estimate counterfactual costs, and control for unmeasured confounders in outcomes. CEA typically relies on observational data rather than randomized trials, which means the causal assumptions in your regression models are doing real work. **Sensitivity analyses** — varying the key assumptions to see how much the CER changes — are essential to honest CEA. A conclusion that a program is cost-effective is only as credible as its most consequential assumptions, and transparent sensitivity analysis is how analysts signal where the real uncertainty lies.
