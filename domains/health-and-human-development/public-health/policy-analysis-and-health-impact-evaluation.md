---
id: policy-analysis-and-health-impact-evaluation
title: Policy Analysis and Health Impact Evaluation
domain: health-and-human-development
course: public-health
prerequisites:
- id: health-policy-and-advocacy
  type: hard
- id: health-systems-and-financing
  type: soft
builds-toward:
- cost-effectiveness-and-economic-evaluation-health
tags:
- policy
- impact-evaluation
- health-outcomes
stage: advanced
status: draft
---

# Policy Analysis and Health Impact Evaluation

## Core Idea
Policy impact evaluation estimates how policy changes (taxation, regulation, subsidies) affect health outcomes. Methods include natural experiments (leveraging policy discontinuities), difference-in-differences (comparing jurisdictions before/after policy), and interrupted time-series (assessing trend changes at policy implementation). Policy analysis requires understanding both intended direct effects and unintended indirect effects.

## How It's Best Learned
Evaluate a real health policy using natural variation (e.g., state-level variation in Medicaid expansion, local taxes on sugary beverages) and estimate effect sizes on health outcomes.

## Common Misconceptions
- Policies always affect health in intended directions; unintended consequences (behavioral adaptation, substitution) are common.
- Policy effects are uniform; heterogeneous effects across subgroups are typical and often reveal equity implications.

## Explainer

From your health policy prerequisite, you understand how policy is made — the political and institutional processes by which governments adopt regulations, taxes, or programs. Policy impact evaluation is the analytical complement: it answers the question, "Did this policy actually work, and by how much?" This is harder than it sounds, because health outcomes change continuously for many reasons unrelated to any single intervention. Isolating the causal contribution of a policy requires a credible **counterfactual** — a rigorous answer to the question, what would have happened in this population's absence of the policy?

The fundamental challenge is that we cannot observe both potential outcomes simultaneously. We cannot watch New York City both implement and not implement a soda tax at the same time. The solution is to find a comparison group that was similar in all relevant ways before the policy and serves as a stand-in for the treated group's counterfactual trajectory. **Difference-in-differences (DiD)** exploits this logic: compare the change in outcomes in a jurisdiction that adopted a policy against the change in outcomes in a comparable jurisdiction that did not, over the same time period. If both were on similar trends before the policy — the **parallel trends assumption** — then the difference in their post-policy trajectories is the estimated treatment effect. Medicaid expansion under the Affordable Care Act is a textbook DiD case: states adopted expansion at different times or not at all, creating comparison groups that researchers have used to estimate effects on insurance coverage, healthcare utilization, and mortality.

**Natural experiments** arise when policy variation is driven by circumstances effectively random from the researcher's perspective — a legislative deadline, a close election, a geographic boundary, an arbitrary eligibility cutoff. These create quasi-experimental comparisons without requiring the researcher to assign anyone to a condition. A state border where eligibility for a program changes discontinuously becomes a **regression discontinuity**: people just above and just below the cutoff are likely similar in background characteristics, so comparing their outcomes estimates the treatment effect. **Interrupted time-series (ITS)** takes a different approach: it uses a single jurisdiction as its own control by modeling the pre-policy trend and testing whether the post-policy trajectory deviates from the projected continuation. A clean ITS shows a smooth pre-policy trend, then a change in level or slope at the policy implementation date.

What makes health policy evaluation genuinely difficult — and practically important — is **heterogeneous treatment effects**. A sugary drink tax reduces consumption on average, but its effect is larger in low-income populations (who spend a higher income fraction on these beverages) and may be smaller in high-income populations where modest price increases do not change purchasing behavior. These subgroup differences are not noise to average away — they are substantively important for equity analysis. A tax that concentrates financial burden in lower-income households while delivering most health benefit to middle-income households is an instrument with real distributional consequences. Similarly, **substitution effects** — people switching to other sugary drinks not covered by the tax, or purchasing in adjacent jurisdictions — can attenuate intended effects. Understanding where the policy works, for whom, and at what cost is the full scope of policy evaluation, and it requires moving beyond the average treatment effect to characterize the heterogeneous reality underneath it.
