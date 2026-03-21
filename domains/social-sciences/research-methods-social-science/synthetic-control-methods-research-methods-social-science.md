---
id: synthetic-control-methods-research-methods-social-science
title: Synthetic Control Methods
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: natural-experiments-identification-strategy
  type: hard
- id: time-series-cross-section
  type: soft
- id: linear-regression
  type: soft
builds-toward:
- generalized-synthetic-control
- augmented-synthetic-control
tags:
- causal-inference
- comparative
- counterfactual
- policy-evaluation
stage: advanced
status: draft
---

# Synthetic Control Methods

## Core Idea
Synthetic control constructs a counterfactual for a treated unit by taking a weighted combination of untreated units. When a single unit (country, region, organization) experiences an intervention, its pre-intervention trends may not match any single control unit, but a weighted average may. The method estimates the treatment effect as the post-intervention difference between the treated unit and its synthetic control. It is particularly useful for policy evaluation when aggregate data is available but individual randomization is infeasible.

## Questions

```yaml
- question: "A researcher uses synthetic control to evaluate a minimum wage increase in one state. The synthetic control tracks the treated state's pre-intervention employment trend almost exactly over 12 years. After the wage increase, employment runs 3 percentage points below the synthetic control. Placebo tests on each donor state produce gaps of 0.2–0.8 percentage points. What should the researcher conclude?"
  type: multiple-choice
  options:
    - "The result is statistically significant at p < 0.05 by standard regression criteria"
    - "The estimate is implausibly large and likely reflects overfitting to the pre-intervention period"
    - "The post-intervention gap is large relative to placebo estimates, providing evidence that the policy had a real effect"
    - "The result is inconclusive because only one state was treated, making any inference impossible"
  answer: 2
  explanation: "In synthetic control, inference is done via permutation tests: applying the method to each untreated donor unit reveals the distribution of placebo 'effects.' If the treated state's 3-percentage-point gap far exceeds all placebo gaps (0.2–0.8 pp), that result would be extremely unlikely if the policy had no effect — constituting strong inferential evidence. This is not asymptotic inference; it is a ranking-based permutation test appropriate for a single treated unit. The excellent pre-intervention fit strengthens, not undermines, the estimate's credibility."

- question: "What is the primary advantage synthetic control offers over standard regression-based difference-in-differences when evaluating a policy affecting a single aggregate unit?"
  type: multiple-choice
  options:
    - "Synthetic control does not require a pre-intervention period, making it usable when historical data is unavailable"
    - "The counterfactual is explicitly constructed as a weighted combination of donor units, and its pre-intervention fit is directly verifiable, making identification assumptions transparent"
    - "Synthetic control eliminates the need for any control group, relying solely on the treated unit's own time series"
    - "Synthetic control produces smaller standard errors than difference-in-differences by incorporating more comparison units"
  answer: 1
  explanation: "The defining advantage is transparency: the researcher explicitly constructs the counterfactual (showing which donor units receive which weights) and verifies it by plotting pre-intervention trajectories. If the synthetic control diverges from the treated unit in the pre-period, the counterfactual is not credible — and this failure is immediately visible. In standard regression DiD, the counterfactual is implicit in the regression coefficients, making it much harder to inspect. Synthetic control makes the 'what would have happened without treatment' question concrete and directly checkable."

- question: "In synthetic control, inference about whether an observed post-intervention gap is real uses classical standard errors computed from the pre-intervention regression fit."
  type: true-false
  answer: false
  explanation: "Synthetic control uses permutation-based inference (placebo tests), not classical standard errors. Classical asymptotic inference requires a large number of treated units, but synthetic control has only one. Instead, the researcher applies the method to each untreated donor unit, treating each as if it had received the treatment, and observes the distribution of resulting 'effects.' The actual estimated effect is then ranked within this placebo distribution. Standard errors from regression are not appropriate for this single-treated-unit setting and would produce misleading precision."

- question: "One weakness of synthetic control is that a poor pre-intervention fit between the treated unit and its synthetic control is hidden from view and can only be detected through auxiliary diagnostic tests."
  type: true-false
  answer: false
  explanation: "This is precisely the opposite of the truth — and is one of the method's key strengths. A poor pre-intervention fit is immediately visible when the researcher plots the treated unit's trajectory alongside the synthetic control over the pre-intervention period. If the two series diverge before the treatment, the researcher knows the synthetic control is not a credible counterfactual. This transparency distinguishes synthetic control from regression-based approaches where the counterfactual is implicit. The method cannot hide a bad fit; it displays it prominently."

- question: "Why is a long pre-intervention period important for synthetic control, and what does it allow you to verify that a short pre-intervention window cannot?"
  type: short-answer
  answer: "A long pre-intervention period serves two purposes. First, it provides more data points over which to construct the synthetic control, reducing the risk that the weights are fit to noise rather than stable structural similarities. Second, and more importantly, a long window allows the researcher to verify that the synthetic control tracks the treated unit's trajectory through multiple economic cycles, external shocks, and policy environments — establishing that the match reflects genuine underlying similarity rather than a coincidental alignment on a few recent observations. With a short pre-intervention window, the synthetic control might fit by accident (overfitting), and the researcher cannot tell whether the good fit reflects stable structural comparability or a fragile coincidence that would break down post-intervention."
  explanation: "The pre-intervention fit is the entire basis for trusting the post-intervention counterfactual. A longer validation period makes that trust more credible, because it is much harder for an artificial match to coincidentally track the treated unit through many years of diverse conditions than through just a few years."
```

## Explainer

From natural experiments, you know that causal identification requires a credible counterfactual: what would have happened to the treated unit if it had not been treated? The challenge in many policy contexts is that the unit of treatment is a whole country, state, or city — you cannot randomize, and no single comparison unit may look much like it. Synthetic control addresses exactly this problem by constructing an artificial comparison unit from a weighted combination of untreated units.

The canonical example is Abadie, Diamond, and Hainmueller's study of the effect of California's 1988 tobacco control program on per-capita cigarette sales. No single state looks quite like California in the pre-1988 period — not in terms of economic conditions, demographics, and pre-existing cigarette consumption trends. But a **synthetic California** — a weighted average of Colorado (58.9%), Utah (8.6%), Nevada (23.3%), and a few others — tracks California's pre-intervention trajectory extremely well over the prior 17 years. After 1988, observed California diverges below synthetic California. That gap is the estimated treatment effect.

The weights are chosen to minimize the discrepancy between the treated unit and the synthetic control on pre-intervention outcomes and predictors. This is a transparent, data-driven process: you see exactly which donor units contribute to the synthetic control and in what proportions. The pre-intervention fit is directly verifiable — you plot both series and inspect how closely they track. This is a significant advantage over regression-based approaches where the counterfactual is implicit. If the pre-intervention fit is poor, the synthetic control is not credible, and you know it.

Inference in synthetic control is done through **placebo tests** rather than classical standard errors. The idea: apply the same method to each untreated unit in the donor pool, pretending it received the treatment. Each untreated unit generates its own synthetic control and its own estimated "effect." The distribution of these placebo estimates tells you how unusual your actual estimated effect is. If California's post-intervention gap is much larger than any of the placebo gaps, that is evidence the effect is real. If many placebos show similar gaps, the California result is unexceptional. This permutation-based inference is appropriate because you have one treated unit — asymptotic theory is irrelevant.

The method has important limitations. It requires a reasonably long pre-intervention period to construct and validate the synthetic control. It requires a **donor pool** of untreated units that are genuinely comparable — if the treated unit is an outlier (e.g., the United States as a whole), there may be no good synthetic. It also assumes that the untreated donor units are not themselves affected by the intervention (the **stable unit treatment value assumption**). Despite these constraints, synthetic control has become a standard tool in comparative policy analysis precisely because it makes the counterfactual construction transparent and the credibility of the identification directly inspectable.
