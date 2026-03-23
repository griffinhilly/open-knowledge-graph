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
stage: expert
status: validated
---

# Policy Analysis and Health Impact Evaluation

## Core Idea
Policy impact evaluation estimates how policy changes (taxation, regulation, subsidies) affect health outcomes. Methods include natural experiments (leveraging policy discontinuities), difference-in-differences (comparing jurisdictions before/after policy), and interrupted time-series (assessing trend changes at policy implementation). Policy analysis requires understanding both intended direct effects and unintended indirect effects.

## How It's Best Learned
Evaluate a real health policy using natural variation (e.g., state-level variation in Medicaid expansion, local taxes on sugary beverages) and estimate effect sizes on health outcomes.

## Common Misconceptions
- Policies always affect health in intended directions; unintended consequences (behavioral adaptation, substitution) are common.
- Policy effects are uniform; heterogeneous effects across subgroups are typical and often reveal equity implications.

## Questions

```yaml
- question: "A city implements a sugar-sweetened beverage tax in 2018. A researcher compares average soda consumption in that city in 2019 to consumption in 2017 and finds a 15% decline, concluding the tax was effective. What is the primary threat to validity in this analysis?"
  type: multiple-choice
  options:
    - "The researcher should have used a larger sample to achieve adequate statistical power"
    - "Without a comparison group, there is no way to separate the effect of the tax from other concurrent trends — declining soda consumption nationally, health campaigns, or economic changes — that would have occurred anyway"
    - "A 15% decline is too small to be practically meaningful for public health purposes"
    - "The analysis should have measured sugar intake rather than soda consumption specifically"
  answer: 1
  explanation: "The core problem is the missing counterfactual: what would consumption have been in 2019 without the tax? A pre-post comparison within one jurisdiction cannot answer this. National trends, media campaigns, or changing demographics could all reduce consumption independently of the tax. Difference-in-differences addresses this by using a comparable untreated jurisdiction to estimate the counterfactual trajectory."

- question: "A difference-in-differences study compares Medicaid expansion states to non-expansion states before and after the ACA. What is the central identifying assumption that must hold for the DiD estimate to be a valid causal effect?"
  type: multiple-choice
  options:
    - "Expansion and non-expansion states must have identical pre-policy healthcare utilization rates"
    - "In the absence of Medicaid expansion, the treated states would have followed the same outcome trend as the control states (parallel trends assumption)"
    - "The policy must have been assigned randomly to states rather than through state legislative choices"
    - "The sample must be large enough that any pre-existing differences between states become statistically negligible"
  answer: 1
  explanation: "DiD does not require identical pre-policy levels — states can differ in baseline outcomes. What it requires is that both groups would have moved in parallel over time without the intervention. If expansion states were on a steeper improving trajectory before the policy (perhaps because they had more liberal health policies generally), DiD would overestimate the Medicaid expansion effect. Researchers test this by examining pre-policy trends; significant divergence before the policy weakens the parallel trends assumption."

- question: "Natural experiments can provide credible causal estimates of policy effects without random assignment, because variation in policy exposure driven by factors unrelated to the outcome serves as a quasi-random instrument."
  type: true-false
  answer: true
  explanation: "When a policy is implemented based on circumstances independent of the health outcomes being studied — a legislative deadline, a close election, a geographic boundary, an eligibility cutoff — this 'as-if random' variation allows researchers to estimate causal effects. The logic is the same as in randomized trials: if assignment to the 'treatment' (policy exposure) is unrelated to background characteristics, differences in outcomes can be attributed to the policy. The credibility of the causal claim depends on the plausibility that the assignment mechanism was truly independent of confounders."

- question: "A well-designed difference-in-differences study establishes causal policy effects without any identifying assumptions, because comparing the same population before and after a policy controls for all pre-existing differences."
  type: true-false
  answer: false
  explanation: "DiD always rests on the parallel trends assumption: that in the absence of the policy, treated and control groups would have followed the same trajectory. This assumption is empirically testable (by examining pre-policy trends) but cannot be proven — it is a claim about the counterfactual. A pre-post comparison of the treated group alone would be even weaker; using a control group addresses time trends but only under the parallel trends assumption. No observational study design eliminates identifying assumptions entirely."

- question: "Why do evaluators need to go beyond the average treatment effect when assessing health policy impacts? What does heterogeneity in treatment effects reveal that the average cannot?"
  type: short-answer
  answer: "The average treatment effect answers 'did this policy work on average?' but conceals who benefits, who is burdened, and whether the policy is equitable. A sugar tax that reduces consumption by 8% on average may have a 15% effect in low-income households (who spend a higher income fraction on these beverages) and a 2% effect in high-income households. If those same low-income households bear most of the financial burden while receiving less health benefit, the policy is regressive. Heterogeneous effects also reveal substitution patterns — switching to untaxed alternatives — that the average masks. Equity analysis requires characterizing the distribution of effects across income, race, and geography."
  explanation: "The practical implication is that policy evaluation should not stop at the headline average effect. Equity and efficiency both require understanding heterogeneity: the policy may be achieving its goals for some subgroups while failing or harming others. Interaction terms, subgroup analyses, and distributional measures are methodological tools for uncovering this structure."
```

## Explainer

From your health policy prerequisite, you understand how policy is made — the political and institutional processes by which governments adopt regulations, taxes, or programs. Policy impact evaluation is the analytical complement: it answers the question, "Did this policy actually work, and by how much?" This is harder than it sounds, because health outcomes change continuously for many reasons unrelated to any single intervention. Isolating the causal contribution of a policy requires a credible **counterfactual** — a rigorous answer to the question, what would have happened in this population's absence of the policy?

The fundamental challenge is that we cannot observe both potential outcomes simultaneously. We cannot watch New York City both implement and not implement a soda tax at the same time. The solution is to find a comparison group that was similar in all relevant ways before the policy and serves as a stand-in for the treated group's counterfactual trajectory. **Difference-in-differences (DiD)** exploits this logic: compare the change in outcomes in a jurisdiction that adopted a policy against the change in outcomes in a comparable jurisdiction that did not, over the same time period. If both were on similar trends before the policy — the **parallel trends assumption** — then the difference in their post-policy trajectories is the estimated treatment effect. Medicaid expansion under the Affordable Care Act is a textbook DiD case: states adopted expansion at different times or not at all, creating comparison groups that researchers have used to estimate effects on insurance coverage, healthcare utilization, and mortality.

**Natural experiments** arise when policy variation is driven by circumstances effectively random from the researcher's perspective — a legislative deadline, a close election, a geographic boundary, an arbitrary eligibility cutoff. These create quasi-experimental comparisons without requiring the researcher to assign anyone to a condition. A state border where eligibility for a program changes discontinuously becomes a **regression discontinuity**: people just above and just below the cutoff are likely similar in background characteristics, so comparing their outcomes estimates the treatment effect. **Interrupted time-series (ITS)** takes a different approach: it uses a single jurisdiction as its own control by modeling the pre-policy trend and testing whether the post-policy trajectory deviates from the projected continuation. A clean ITS shows a smooth pre-policy trend, then a change in level or slope at the policy implementation date.

What makes health policy evaluation genuinely difficult — and practically important — is **heterogeneous treatment effects**. A sugary drink tax reduces consumption on average, but its effect is larger in low-income populations (who spend a higher income fraction on these beverages) and may be smaller in high-income populations where modest price increases do not change purchasing behavior. These subgroup differences are not noise to average away — they are substantively important for equity analysis. A tax that concentrates financial burden in lower-income households while delivering most health benefit to middle-income households is an instrument with real distributional consequences. Similarly, **substitution effects** — people switching to other sugary drinks not covered by the tax, or purchasing in adjacent jurisdictions — can attenuate intended effects. Understanding where the policy works, for whom, and at what cost is the full scope of policy evaluation, and it requires moving beyond the average treatment effect to characterize the heterogeneous reality underneath it.
