---
id: counterfactual-framework
title: Counterfactual Framework and Potential Outcomes
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: directed-acyclic-graphs
  type: hard
- id: epidemiology-foundations
  type: soft
builds-toward:
- sensitivity-analysis-epidemiology
tags:
- causal-inference
- potential-outcomes
- rubin-causal-model
stage: expert
status: validated
---

# Counterfactual Framework and Potential Outcomes

## Core Idea
The counterfactual framework defines causal effects as contrasts between potential outcomes under different exposure levels, observed for the same individual in hypothetical scenarios. The fundamental problem of causal inference is that only one potential outcome is observed per person; valid causal inference requires assumptions about missing counterfactuals (e.g., consistency, positivity, exchangeability).

## Questions

```yaml
- question: "A study finds that patients who voluntarily chose to take a new medication had better outcomes than those who did not. The researchers conclude the medication caused the improvement. Which assumption, if violated, most directly undermines this causal claim?"
  type: multiple-choice
  options:
    - "Positivity — some patient subgroups had zero probability of receiving the medication"
    - "Consistency — there are multiple formulations of the medication with different effects"
    - "Exchangeability — patients who chose the medication may have been systematically healthier or more health-conscious, making the groups incomparable in their potential outcomes"
    - "The sample was too small to estimate the average treatment effect with precision"
  answer: 2
  explanation: "In an observational study where patients self-select into treatment, the most immediate threat is confounding — a violation of exchangeability. Patients who voluntarily take a medication may differ systematically from those who don't (more health-conscious, fewer comorbidities, better access to care). Their potential outcomes under no treatment may already be better, making it impossible to attribute the outcome difference to the medication. Randomization solves this mechanically; observational studies must address it through design and statistical adjustment."

- question: "Why can't individual causal effects — Y(1) − Y(0) — be directly measured for any single person?"
  type: multiple-choice
  options:
    - "IRB regulations prohibit collecting the same outcome measurement twice from the same participant"
    - "Each person experiences only one treatment condition, so one potential outcome is never realized and remains permanently unobserved"
    - "The subtraction Y(1) − Y(0) is mathematically undefined when the outcome is a binary variable"
    - "Individual effects are too small to detect; only population-level averages are large enough to measure reliably"
  answer: 1
  explanation: "This is the fundamental problem of causal inference: potential outcomes are mutually exclusive in reality. If someone takes the drug, we observe Y(1) and Y(0) — what would have happened without it — is forever unobserved (the counterfactual). If they don't take it, Y(0) is observed and Y(1) is unknown. We cannot run the same person through both conditions simultaneously while holding everything else constant. This is why causal inference requires assumptions about missing potential outcomes — we impute the counterfactual from comparable people, not measure it directly."

- question: "Randomized controlled trials solve the fundamental problem of causal inference by allowing researchers to observe both potential outcomes Y(1) and Y(0) for the same individual."
  type: true-false
  answer: false
  explanation: "RCTs do not allow observation of both potential outcomes for the same person — the fundamental problem persists. What RCTs accomplish is different: random assignment creates groups that are exchangeable in expectation, so the control group's observed Y(0) is a valid stand-in for the treatment group's counterfactual Y(0). We still observe only one potential outcome per person; we just have a valid design for estimating the average treatment effect without controlling for confounders, because randomization balances both measured and unmeasured variables."

- question: "Exchangeability requires that, conditional on measured covariates, the distribution of potential outcomes is the same across treatment groups — meaning no unmeasured common cause of treatment assignment and outcome remains."
  type: true-false
  answer: true
  explanation: "Exchangeability (no unmeasured confounding) is the most demanding and least testable of the three key assumptions. It means that after conditioning on measured covariates, treatment assignment is independent of the potential outcomes — the groups are interchangeable in the sense that each could stand in for the other's counterfactual. In DAG terms, this requires that conditioning on measured covariates blocks all backdoor paths. Unlike positivity (detectable from data distributions), exchangeability is a claim about unmeasured variables and cannot be verified from data alone."

- question: "Explain why the potential outcomes framework defines a causal effect as a contrast between Y(1) and Y(0) rather than as a statistical association between treatment and outcome."
  type: short-answer
  answer: "Statistical association conflates causation with confounding and selection bias — two variables can correlate strongly because they share a common cause, not because one causes the other. The counterfactual definition forces precision: the causal effect is the difference between what happened under one treatment and what would have happened under the alternative, within the same individual (or population average across individuals). This 'hold everything else constant' requirement is what separates a causal claim from a mere association."
  explanation: "The framework's power is that it makes explicit what a causal claim requires: a comparison between observed fact and a hypothetical counterfactual. By writing the target estimand as E[Y(1) − Y(0)], we can precisely characterize when observational data can validly estimate it (when the three assumptions hold) and when it cannot. This explicitness is what separates modern causal inference from the older tradition of treating association as a proxy for causation."
```

## Explainer

From your study of directed acyclic graphs (DAGs), you already understand that causation has a direction and that confounding arises when common causes of both exposure and outcome distort an observed association. The **counterfactual framework** takes this further: it defines what a causal effect actually *means* for a single individual. The claim "smoking caused her lung cancer" is a counterfactual claim — it asserts that if, contrary to fact, she had not smoked, she would not have developed cancer. Causation is always a comparison between what happened and what *would have happened* under a different world.

The formal notation makes this precise. Write **Y(1)** for the outcome a person would experience if exposed (treatment = 1) and **Y(0)** for the outcome they would experience if unexposed (treatment = 0). These are called **potential outcomes** — not observed outcomes, but outcomes that would be realized under each possible treatment state. The **individual causal effect** is Y(1) − Y(0): did the treatment change this person's outcome? This is the exact quantity we care about. But here is the inescapable problem: every person receives one treatment. If a patient takes the drug, we observe Y(1) and never learn Y(0). If they don't take it, we observe Y(0) and never learn Y(1). One of the two potential outcomes is always a **counterfactual** — literally counter to the observed fact. This is the **fundamental problem of causal inference**.

Because we cannot observe both potential outcomes for the same person, we cannot directly measure individual causal effects. The solution is to shift the estimand: instead of the individual effect, we target the **average treatment effect (ATE)** — E[Y(1) − Y(0)] — averaged across a population. This is estimable if the treated and untreated groups are *exchangeable*: statistically comparable in their potential outcomes, so that the untreated group's observed Y(0) can stand in for the treated group's counterfactual Y(0). Randomization achieves this mechanically; observational studies must achieve it through design and modeling.

Three key assumptions underpin valid counterfactual inference. **Consistency** requires that the potential outcome Y(a) for treatment a is precisely what you observe when treatment a is received — there is one well-defined version of each treatment level, not ambiguous variations. **Positivity** (also called the overlap assumption) requires that every subgroup defined by measured covariates has some positive probability of receiving each treatment level; if certain people *never* receive the treatment, we cannot estimate the effect for them. **Exchangeability** (no unmeasured confounding) is the most demanding: it requires that, conditional on measured covariates, treatment assignment is independent of the potential outcomes — no hidden common causes remain.

The connection to your DAG prerequisite is direct. A DAG encodes the assumed causal structure of the data-generating process. Exchangeability conditional on covariates Z translates to the DAG condition that blocking all backdoor paths from exposure to outcome is achievable by conditioning on Z. The three assumptions are not mere statistical niceties; they are substantive claims about the world that must be justified on scientific grounds. Sensitivity analysis — the topic this builds toward — is specifically the practice of asking how badly your conclusions break down if exchangeability is violated.

## How It's Best Learned
Work through simple numerical examples: two identical people who differ only in treatment received, calculate what the ATE would be if you could observe both potential outcomes, then see how the naive observational comparison can diverge. This makes the fundamental problem concrete and the need for assumptions intuitive.
