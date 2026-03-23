---
id: synthetic-control-methods-epidemiology
title: Synthetic Control and Comparative Case Studies
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: natural-experiments
  type: hard
- id: difference-in-differences
  type: soft
builds-toward:
- interrupted-time-series-analysis
tags:
- quasi-experimental
- policy-evaluation
- case-study
stage: expert
status: draft
---

# Synthetic Control and Comparative Case Studies

## Core Idea
Synthetic control methods construct a weighted combination of unexposed units to match pre-intervention characteristics of an exposed unit. Comparing the exposed unit's post-intervention trajectory to the synthetic control estimates the intervention effect. This approach is useful when few units are exposed and historical data are limited.

## Questions

```yaml
- question: "A researcher applies synthetic control to evaluate a California smoking prevention policy. The synthetic control closely tracks California's smoking rate for 15 years before the policy, then diverges sharply downward after implementation. The most important feature of this result for making a causal inference is:"
  type: multiple-choice
  options:
    - "The post-intervention gap is large in absolute terms"
    - "The pre-intervention fit is close, meaning the synthetic control was a valid counterfactual before the policy"
    - "The donor pool includes many states with similar demographics to California"
    - "The analysis was conducted using a least-squares minimization algorithm"
  answer: 1
  explanation: "The validity of the causal inference rests on the pre-intervention fit. If the synthetic control closely tracked the treated unit before the intervention, we have good reason to believe it represents a credible counterfactual — what would have happened absent the policy. The post-intervention divergence then estimates the treatment effect. A large gap means little without a credible pre-period match; the pre-period fit is the foundation of the method's logic."

- question: "Why are standard frequentist hypothesis tests (p-values based on assumed sampling distributions) inappropriate for synthetic control analyses with a single treated unit?"
  type: multiple-choice
  options:
    - "Synthetic control estimates are always biased, making hypothesis tests invalid"
    - "With only one treated unit, there is no sampling distribution from which p-values can be derived in the standard sense"
    - "Synthetic control requires Bayesian inference because it uses prior information"
    - "Standard tests require normally distributed outcomes, which smoking rates violate"
  answer: 1
  explanation: "Standard frequentist inference imagines drawing many samples from a population. With a single treated unit (one state, one country), there is no such sampling distribution — we have one observation of the treatment effect, not many. This is why synthetic control uses permutation-based placebo tests instead: apply the same method to each untreated unit as if it were treated, generate a distribution of 'effects,' and compare the real treated unit's effect to this null distribution. This is honest about the small-sample nature of the analysis."

- question: "The quality of a synthetic control analysis depends critically on how well the weighted combination of donor pool units matches the treated unit's pre-intervention trajectory."
  type: true-false
  answer: true
  explanation: "This is the core validity requirement of synthetic control. The synthetic control is only a credible counterfactual if it reproduces the treated unit's pre-intervention behavior. Poor pre-period fit means the synthetic control is not tracking the same underlying trends, and post-intervention divergence cannot be attributed to the intervention. Researchers should report pre-period fit explicitly as a quality check."

- question: "Synthetic control requires finding a single donor pool unit that closely resembles the treated unit across all relevant characteristics."
  type: true-false
  answer: false
  explanation: "This is precisely what synthetic control improves upon compared to simple comparison methods. No single unit needs to resemble the treated unit — the method finds a weighted combination (the 'synthetic' control) that matches as a composite. For example, synthetic California might be 40% Texas + 35% Florida + 15% Ohio + 10% Pennsylvania. The composite does the matching work even when no individual unit is a good match alone."

- question: "Describe the placebo test used for inference in synthetic control and explain what it establishes about the estimated treatment effect."
  type: short-answer
  answer: "A placebo test applies the synthetic control procedure to each unexposed unit in the donor pool as if it were treated — estimating a 'placebo effect' for each. These placebo effects form a reference distribution. The researcher then asks: is the actual treated unit's post-intervention gap unusually large relative to this distribution? If the real effect is in the extreme tail of the placebo distribution, that constitutes evidence against the null hypothesis of no effect. The test is honest because it uses the same small-sample data structure instead of invoking asymptotic assumptions."
  explanation: "With only one treated unit, there is no frequentist sampling distribution to appeal to. Permutation inference — shuffling the 'treatment label' across units — generates an empirical null distribution using the actual data structure. This is why synthetic control inference is both more credible and more limited than large-sample methods: it makes honest use of what is actually available."
```

## Explainer

From your study of natural experiments and difference-in-differences (DiD), you know that quasi-experimental methods try to approximate the counterfactual: what would have happened to the treated unit if it had not received the intervention? Difference-in-differences achieves this by finding a control group with parallel pre-intervention trends and assuming those trends would have continued. But DiD requires multiple unexposed units that share a common trend with the treated unit — and it struggles when you have only a single treated unit (one city, one country, one hospital) and a heterogeneous pool of potential controls with diverging pre-treatment trends.

**Synthetic control** was developed precisely for this setting. The core idea is intuitive: rather than picking a single control unit that resembles the treated unit, why not build a tailor-made composite? You select a **donor pool** of unexposed units and find the weighted combination of those units — the synthetic control — that best reproduces the treated unit's pre-intervention trajectory across a vector of outcome and covariate values. The algorithm minimizes the distance between the treated unit and the weighted combination during the **pre-period**. If California is the treated unit (which implemented a policy), the synthetic control might be 40% Texas + 35% Florida + 15% Ohio + 10% Pennsylvania — whatever mix best matches California's pre-intervention smoking rates, demographics, and economic indicators. No single state needs to look like California; the composite does.

After the intervention, you simply compare the treated unit's actual post-intervention trajectory to what the synthetic control would have predicted. The gap between the two trajectories is your estimate of the **treatment effect**. The visual logic is compelling: if the synthetic control tracked the treated unit closely for ten years before the policy change and then diverged sharply afterward, the divergence is hard to attribute to anything other than the policy. This is an extension of the DiD intuition — instead of assuming parallel trends between real groups, you construct a control group whose trends are guaranteed to match by construction.

Inference in synthetic control is non-standard because you typically have very few treated units (often one) and standard frequentist assumptions break down. The conventional approach uses **placebo tests**: apply the synthetic control method to each unit in the donor pool as if it were treated, estimate its "placebo effect," and compare the treated unit's actual effect to the distribution of placebo effects. If the treated unit's post-intervention gap is large relative to the placebo gaps, that constitutes evidence against the null hypothesis. This permutation-based inference is honest about the small-sample nature of the analysis. The method has important limitations: it requires a rich pre-period for the matching algorithm to work; it cannot handle multiple treated units without extensions; and when the treated unit is an outlier that the donor pool cannot match well in the pre-period, the synthetic control is unreliable and that failure should be reported explicitly as a quality check.
