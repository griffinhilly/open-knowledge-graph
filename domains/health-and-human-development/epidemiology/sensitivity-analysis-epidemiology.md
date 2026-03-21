---
id: sensitivity-analysis-epidemiology
title: Sensitivity Analysis for Unmeasured Confounding
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: counterfactual-framework
  type: hard
- id: confounding-epidemiology
  type: hard
tags:
- unmeasured-confounding
- bias-analysis
- robustness
stage: advanced
status: draft
---

# Sensitivity Analysis for Unmeasured Confounding

## Core Idea
Sensitivity analysis assesses whether conclusions remain robust under violations of unmeasured confounding. Methods (e.g., E-value, Rotnitzky-Robins bounds) quantify the minimum strength of unmeasured confounding needed to reverse or nullify an observed association. Sensitivity analysis supplements point estimates with assessments of hidden bias.

## Questions

```yaml
- question: "An observational study reports a risk ratio of 2.5 for the association between exposure X and outcome Y. A critic says, 'This could be explained by unmeasured confounding.' What does a sensitivity analysis using the E-value actually provide?"
  type: multiple-choice
  options:
    - "Proof that unmeasured confounding is absent if the E-value is large"
    - "The minimum association strength that an unmeasured confounder would need with both the exposure and the outcome to fully explain away the observed RR"
    - "A statistical test of whether unmeasured confounding is present"
    - "An adjusted effect estimate that accounts for unmeasured confounders"
  answer: 1
  explanation: "The E-value does not prove that confounding is absent and does not adjust the estimate — it quantifies the minimum strength of a specific confounding scenario. A critic asserting 'there might be confounding' must now name a specific confounder with at least E-value-sized associations with both the exposure and the outcome simultaneously. This shifts the debate from a logical impossibility (proving no confounding) to an empirical claim (is any such confounder plausible?). Options A and D represent common misunderstandings of what sensitivity analysis accomplishes."

- question: "An observational study finds RR = 1.1 with a correspondingly small E-value of approximately 1.2. Which conclusion is best supported?"
  type: multiple-choice
  options:
    - "The finding is robust because the association is statistically significant"
    - "The finding is fragile — a confounder with only modest associations with exposure and outcome could explain it away"
    - "The finding is robust because a twofold confounder would be required"
    - "No conclusion about robustness is possible without knowing the confounder's prevalence"
  answer: 1
  explanation: "A small E-value (here about 1.2) means that even a confounder with weak associations (1.2-fold with both exposure and outcome) could fully explain the observed result. This makes the finding fragile — a common, mild confounder easily provides the required association. Statistical significance does not imply robustness to confounding; a large, well-powered study can produce significant but confounded results. Option C mischaracterizes the E-value — 1.2 is far from twofold."

- question: "Sensitivity analysis for unmeasured confounding can establish that an observational finding is free from bias, given a sufficiently large E-value."
  type: true-false
  answer: false
  explanation: "Sensitivity analysis can never establish the absence of unmeasured confounding — it does not eliminate the assumption, it quantifies the robustness to violations of it. A large E-value means confounding would have to be implausibly extreme to explain away the finding, making the causal claim more defensible. But it does not prove bias is absent. The value of the E-value is that it replaces 'there might be confounding' with 'name a specific confounder of this magnitude.'"

- question: "A high E-value for an observed association makes it harder for critics to dismiss the finding by simply asserting the possibility of unmeasured confounding."
  type: true-false
  answer: true
  explanation: "This is the practical payoff of sensitivity analysis. Before the E-value, a critic could always say 'some unmeasured confounder might explain this' — a logically unfalsifiable claim. After computing the E-value, the critic must identify a specific unmeasured variable with associations of at least E-value magnitude with both the exposure and the outcome simultaneously. For strong findings with large E-values, this is a much harder scientific bar to meet."

- question: "How does sensitivity analysis convert the untestable assumption of 'no unmeasured confounding' into a tractable empirical question?"
  type: short-answer
  answer: "Rather than asking whether unmeasured confounding exists (unanswerable), sensitivity analysis asks: how strong would unmeasured confounding need to be to explain away the observed association? The E-value gives a specific numerical threshold. Critics must then identify a plausible confounder that meets that threshold — a testable, domain-specific claim rather than an abstract logical possibility. The question is no longer whether confounding could exist, but whether any known risk factor has the required magnitude of association with both exposure and outcome simultaneously."
  explanation: "The key move is quantification: instead of a binary (confounded/not confounded), sensitivity analysis produces a continuous parameter (the E-value) describing the minimum confounding required. This makes 'there could be confounding' into 'there could be confounding of this specific magnitude' — a claim that domain experts can evaluate."
```

## Explainer

From the counterfactual framework, you know that valid causal inference from observational data requires **exchangeability**: conditional on measured covariates, the exposed and unexposed groups must be comparable in their potential outcomes. This is the assumption of no unmeasured confounding. In a randomized trial, it holds by design. In observational studies, it is always an untestable assumption — you cannot rule out that some unmeasured variable simultaneously predicts both who gets exposed and who gets the outcome. Sensitivity analysis does not test this assumption; it asks a sharper question: **how strongly would unmeasured confounding have to act to explain away your finding?**

The **E-value** (introduced by VanderWeele and Ding) is the most widely used tool for this purpose. It answers: what is the minimum strength, on the risk ratio scale, that an unmeasured confounder would need to have with *both* the exposure and the outcome — simultaneously — to fully explain away the observed association? If you observe a risk ratio of 3.0, the E-value tells you precisely how large the confounder-exposure and confounder-outcome associations would each need to be. The calculation is simple: E-value = RR + √(RR × (RR − 1)). For an RR of 3.0, E-value ≈ 5.2. This means any unmeasured confounder would need associations of at least 5.2-fold with both the exposure and the outcome to explain the result away. You then ask: is there any plausible confounder with that magnitude of association? If the strongest known predictors of the outcome all have associations below 5.2, the result is robust.

**Rotnitzky-Robins bounds** (and related **Cornfield conditions**) approach the same problem differently — they impose parameter constraints on what a confounding variable would have to look like (its prevalence, its association with exposure and outcome) and derive bounds on the true causal effect under those constraints. Rather than a single threshold, bounds analysis yields an interval: the true effect could be anywhere from [lower bound] to [upper bound] if unmeasured confounding exists at a specified level. This is more informative than a point estimate when uncertainty about confounding is substantial.

The practical workflow is to report the E-value alongside every point estimate in an observational study. A large E-value provides a degree of protection: you are saying "for this finding to be spurious, confounding would need to be implausibly extreme." A small E-value is a warning: the finding is fragile and could easily be explained by modest unmeasured confounding. Critics cannot simply assert "there might be confounding" — they must propose a specific confounder with the required magnitude, which is a much harder scientific argument to make. Sensitivity analysis thus converts a logical impossibility (proving the absence of unmeasured confounding) into a tractable empirical question (is there anything plausible with that effect size?), and in doing so it disciplines the rhetoric around causal claims from observational data.

## How It's Best Learned
Calculate E-values for published observational findings across a range of reported effect sizes, and evaluate whether plausible unmeasured confounders could meet the threshold. This trains the intuition for what "robust" actually means quantitatively.
