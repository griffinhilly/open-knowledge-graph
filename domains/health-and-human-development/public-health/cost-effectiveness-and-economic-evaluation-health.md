---
id: cost-effectiveness-and-economic-evaluation-health
title: Cost-Effectiveness Analysis and Economic Evaluation of Health Interventions
domain: health-and-human-development
course: public-health
prerequisites:
- id: cost-benefit-analysis-epidemiology
  type: hard
- id: burden-of-disease-and-comparative-health-assessment
  type: soft
tags:
- economic-evaluation
- cost-effectiveness
- program-evaluation
stage: abstract-reasoning
status: draft
---

# Cost-Effectiveness Analysis and Economic Evaluation of Health Interventions

## Core Idea
Cost-effectiveness analysis compares intervention costs to health benefits (measured in QALYs or DALYs averted) to estimate the cost per unit health gain. Analyses require careful definition of perspective (individual, healthcare system, societal), identification of all relevant costs and benefits, and sensitivity analysis on key assumptions. Willingness-to-pay thresholds (often set as 1-3× GDP per capita) guide policy decisions.

## How It's Best Learned
Build a cost-effectiveness model for an intervention (vaccination, screening, treatment) comparing costs and health outcomes against a comparator.

## Common Misconceptions
- Cost-effectiveness analysis is objective; it requires value judgments about perspective, what outcomes to count, and what threshold is acceptable.
- Dominated interventions (more costly and less effective) should never be used; some dominated options are preferred for equity reasons.

## Explainer

From your study of cost-benefit analysis in epidemiology and burden-of-disease measurement, you know that health resources are finite and that interventions have measurable effects on health outcomes. **Cost-effectiveness analysis (CEA)** is the method health economists use to formalize the tradeoff: given a fixed budget, which interventions produce the most health for the money spent? Unlike a simple cost-benefit analysis that converts everything to dollars, CEA keeps health gains in natural units — most commonly **quality-adjusted life years (QALYs)** (life years weighted by health-related quality of life) or **disability-adjusted life years (DALYs)** averted.

The central output of a CEA is the **incremental cost-effectiveness ratio (ICER)**: the additional cost divided by the additional health benefit of the new intervention compared to the current standard of care. If a new vaccine costs $5 million more per year than the existing approach and prevents 1,000 additional DALYs, its ICER is $5,000 per DALY averted. Whether this represents good value depends on the **willingness-to-pay (WTP) threshold** — the maximum a payer is willing to spend for one additional unit of health gain. The World Health Organization has historically suggested 1–3× a country's GDP per capita as a reasonable threshold; richer countries use higher thresholds (the UK's NICE uses roughly £20,000–30,000 per QALY). Interventions with ICERs below the threshold are considered cost-effective; those above it are not — though "cost-effective" never means "affordable" or "recommended."

The **perspective** of analysis is one of the most consequential methodological choices. A healthcare system perspective counts only medical costs and health outcomes; a societal perspective adds productivity losses, informal caregiver costs, and downstream economic effects. These can differ dramatically: a mental health intervention might appear only modestly cost-effective from a healthcare perspective (it uses expensive clinical resources) but highly cost-effective from a societal perspective (it prevents years of lost work and reduces criminal justice costs). Analysts must declare their perspective explicitly, because changing it can flip a conclusion from "not cost-effective" to "highly cost-effective."

Because every model rests on assumptions — about disease incidence, intervention effectiveness, quality-of-life weights, discount rates — **sensitivity analysis** is not optional; it is the core of honest economic evaluation. One-way sensitivity analyses vary each input individually; probabilistic sensitivity analyses vary all inputs simultaneously using Monte Carlo simulation, producing a distribution of ICER estimates rather than a single point. A policy decision based on a single ICER without sensitivity analysis is fragile. The final nuance — captured in the Common Misconceptions — is that the cost-effectiveness threshold is itself a value judgment, not a scientific finding. Societies routinely fund interventions above the threshold for equity reasons (rare diseases, pediatric conditions) and sometimes defund effective interventions below the threshold for budget reasons. CEA is a decision aid, not a decision rule.
