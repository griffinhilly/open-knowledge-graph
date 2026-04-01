---
id: causal-inference-ml
title: Causal Inference in Machine Learning
domain: computer-science
course: machine-learning-theory
prerequisites:
- id: probabilistic-graphical-models
  type: hard
- id: bayesian-inference-intro
  type: hard
tags:
- causal-inference
- causal-graphs
- treatment-effects
- confounding
- intervention
stage: expert
status: validated
---

# Causal Inference in Machine Learning

## Core Idea
Causal inference in machine learning goes beyond correlation to identify cause-effect relationships: "If we intervene to change X, how will Y change?" This is formalized through causal graphs (directed acyclic graphs representing causal assumptions), do-calculus (Pearl's framework for computing interventional distributions), and randomized experiments (gold standard but often infeasible). Machine learning approaches use observational data with causal assumptions to estimate causal effects, addressing confounding (variables that influence both cause and effect), selection bias, and unobserved confounders. Applications include treatment effect estimation, policy evaluation, and counterfactual prediction.

## Questions

```yaml
- question: "What is the key difference between correlation and causation, and why does standard ML (which learns correlations) fail to capture causation?"
  type: short-answer
  answer: "Correlation describes association: P(Y|X) is high if X and Y co-occur frequently. Causation describes intervention: P(Y|do(X)) is the probability of Y if we intervene to set X to a value. The difference emerges when confounders (variables that influence both X and Y) exist. For example, ice cream sales and drowning deaths are correlated (both increase in summer), but neither causes the other; summer weather is a confounder. Standard ML learns correlations from data, but confounders break the causal interpretation: increasing ice cream sales does not save lives. Causal inference requires additional assumptions (causal graphs specifying confounders, randomization) and specialized methods to estimate P(Y|do(X)) from observational data."
  explanation: "The correlation-causation distinction is fundamental. ML practitioners must recognize when they are estimating correlation vs. causation and choose methods accordingly. Causal inference is necessary for policy/treatment decisions where we care about intervention effects, not just prediction."

- question: "In causal graphs, a confounder is a variable that influences both the treatment and outcome. How does confounding bias causal effect estimates from observational data?"
  type: multiple-choice
  options:
    - "Confounders have no effect on causal estimates; they are irrelevant to do-calculus"
    - "Confounders induce spurious correlation between treatment and outcome, biasing effect estimates if not controlled for"
    - "Confounders always increase the estimated effect size, never decrease it"
    - "Confounders are automatically handled by any regression model"
  answer: 1
  explanation: "Confounders create non-causal association between treatment and outcome. If a confounder C influences both T (treatment) and Y (outcome), then P(Y|T) will be inflated: T and Y are correlated partly due to C, not (only) due to a causal effect of T on Y. For example, in health studies, age is a confounder: older patients are both more likely to receive treatment (physicians prescribe more for elderly) and more likely to have adverse outcomes (age-related decline). Comparing outcomes between treated and untreated without controlling for age conflates the treatment effect with age effects. Causal methods (matching, stratification, inverse probability weighting) condition on confounders to isolate the causal effect."

- question: "Pearl's do-calculus provides rules for computing interventional distributions P(Y|do(X)) from observational distributions P(Y|X). In what situation can you compute the causal effect from observational data alone?"
  type: multiple-choice
  options:
    - "Never — causal effects always require randomized experiments"
    - "When all confounders are measured and the causal graph is known, satisfying the 'backdoor criterion'; then causal effects can be estimated by conditioning on confounders"
    - "When X has no confounders; then P(Y|do(X)) = P(Y|X)"
    - "When sample size is large; large data is sufficient to infer causation"
  answer: 1
  explanation: "The backdoor criterion, developed by Pearl, specifies when causal effects are identifiable from observational data: if all confounders are measured and the causal graph is correctly specified, you can estimate the causal effect by conditioning on confounders. For example, if age is the only confounder of treatment-outcome, stratifying by age removes confounding, and the treatment effect is estimable. If unmeasured confounders exist, even perfect data and a known graph will not identify the causal effect; you need additional assumptions (instrumental variables, regression discontinuity) or experiments."

- question: "Inverse Probability Weighting (IPW) is a method for estimating causal effects from observational data. The weights are typically inverse propensity scores. Why reweight rather than just condition?"
  type: true-false
  answer: true
  explanation: "IPW and conditioning (stratification) both control for confounders but have different properties. Conditioning (matching on confounders) is intuitive but can lead to sparse data in high-dimensional confounders. IPW reweights observations: units with low propensity score for their observed treatment are upweighted, creating a pseudo-population where treatment is independent of confounders (by design). IPW is efficient for high-dimensional confounders but can be unstable if propensity scores are extreme (some units have very low probability of their observed treatment). Doubly robust methods combine both, improving efficiency and robustness."
```

## Explainer

Causal inference is the science of learning cause-effect relationships from data. In machine learning, this emerges as a critical challenge: when you train a model on observational data, are you learning correlation or causation? This distinction is crucial for applications like medical treatment (does this drug help patients?), policy evaluation (does this intervention improve outcomes?), and counterfactual reasoning (what would happen if we changed a decision?).

**The Causal Graph Framework**: Pearl's causal framework represents causal assumptions as directed acyclic graphs (DAGs). Nodes are variables; directed edges represent causal influences. For example, a treatment T causes outcome Y, and a confounder C causes both T and Y. The graph encodes the causal structure and enables formal reasoning about which variables must be controlled to isolate causal effects.

**Do-Calculus**: Pearl's do-calculus provides rules for computing interventional distributions P(Y|do(X)) — the probability of Y if we intervene to set X — from observational distributions P(Y|X). The do-operator is key: P(Y|do(X)=x) differs from P(Y|X=x) when confounders exist. Do-calculus formalizes three rules:
1. **Ignore observations**: P(Y|do(X), Z, W) = P(Y|do(X), W) if Z is not a descendant of X.
2. **Ignore interventions**: P(Y|do(X), do(Z), W) = P(Y|do(X), W) if there is no causal path from Z to Y given X.
3. **Ignore interventions and observations**: Complex rule for ignoring variables when confounding is broken.

These rules allow converting do-expressions to observation-based quantities, enabling estimation from observational data.

**Confounding and Bias**: A confounder is a variable that influences both treatment and outcome. Confounders induce spurious correlation: if C causes both T and Y, then T and Y are correlated even without a causal effect of T on Y. Causal methods address confounding through:
- **Conditioning**: Stratify by confounder value, isolating the causal effect within strata.
- **Matching**: Create matched pairs of treated/untreated units with similar confounder values.
- **Regression**: Include confounders as covariates (works for linear models and some non-linear settings).
- **Inverse Probability Weighting**: Reweight observations by inverse propensity score, creating a pseudo-population where treatment is independent of confounders.
- **Doubly Robust Methods**: Combine regression and weighting for robustness.

**Identifiability**: A causal effect is identifiable if it can be computed from the observational distribution and the causal graph. The **backdoor criterion** (Pearl) provides a sufficient condition: the causal effect of T on Y is identifiable if there exists a set of confounders C such that (1) C blocks all non-causal paths from T to Y (backdoor paths), and (2) no element of C is a descendant of T. If the backdoor criterion is satisfied, the causal effect is identifiable by conditioning on C.

**Unobserved Confounding**: If unmeasured confounders exist, the causal effect is not identifiable from observational data alone, even with a known causal graph. Alternative strategies:
- **Instrumental Variables**: Variables that affect treatment but only through treatment's effect on outcome, enabling causal effect estimation without measuring confounders.
- **Regression Discontinuity**: When treatment assignment has a threshold, the discontinuity at the threshold identifies causal effects near the threshold.
- **Synthetic Controls**: Construct control units from pre-intervention outcomes to estimate counterfactual outcomes.
- **Sensitivity Analysis**: Explore how conclusions change under different levels of unmeasured confounding.

**Machine Learning Integration**: Modern causal ML combines machine learning with causal inference:
- **Heterogeneous Treatment Effects**: Use ML to learn how treatment effects vary across subgroups (e.g., which patients benefit from a drug?).
- **Causal Discovery**: Use algorithms to learn causal structure from data (challenging; requires strong assumptions and often fails without sufficient data or domain knowledge).
- **Double ML**: Combine machine learning for nuisance parameter estimation (e.g., propensity scores) with causal inference for treatment effects.
- **Causal Forests**: Ensemble methods that estimate heterogeneous causal effects by splitting data on causal effect heterogeneity.

**Practical Challenges**:
- Causal assumptions (the causal graph) are usually not known and must be justified based on domain knowledge.
- Unmeasured confounders are always possible in observational studies.
- Estimating causal effects requires careful balance of bias and variance; naive estimators can be biased or inefficient.
- Causal effects in complex domains (social systems, economics) are often heterogeneous and context-dependent.

**Applications**:
- Medicine: Estimating treatment effects from observational patient data.
- Economics: Evaluating policy interventions (minimum wage, education programs).
- Recommendation Systems: Understanding causal effects of recommendations on user outcomes (vs. just correlation).
- Marketing: Measuring incremental impact of campaigns while controlling for confounding.

Causal inference is an increasingly critical capability as ML systems move from prediction (does X predict Y?) to decision-making (if we do X, what happens to Y?). Practitioners must understand both the power and limitations of causal methods.
