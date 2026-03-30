---
id: mediation-analysis-social
title: Mediation and Indirect Effects Analysis
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: linear-regression-social-science
  type: hard
- id: research-design-advanced
  type: soft
- id: matrices-intro
  type: soft
- id: linear-regression
  type: soft
- id: partial-derivatives-basics
  type: soft
- id: partial-derivatives
  type: soft
builds-toward:
- conditional-indirect-effects
- dynamic-mediation-models
tags:
- mechanisms
- indirect-effects
- pathways
- causal-process
stage: advanced
status: validated
---

# Mediation and Indirect Effects Analysis

## Core Idea
Mediation analysis decomposes a causal effect into direct effects (X→Y) and indirect effects operating through a mediator (X→M→Y). Understanding mechanisms requires identifying the causal pathway through which an independent variable influences an outcome. Modern mediation analysis uses causal inference frameworks: the natural indirect effect (NIE) and direct effect (NDE) are defined under counterfactual logic, accounting for treatment-mediator interactions and sequential ignorability assumptions.

## Questions

```yaml
- question: "A researcher uses observational data to show that college attendance (X) increases lifetime earnings (Y), and that college-developed skills (M) mediate this relationship. She concludes that M causally explains the income gap. What is the most important methodological problem?"
  type: multiple-choice
  options:
    - "She should have used structural equation modeling rather than regression to compute the indirect effect"
    - "Sequential ignorability is unlikely to hold — unmeasured confounders of M→Y (e.g., unobserved ability) could bias the indirect effect estimate and make it non-causal"
    - "Mediation analysis cannot be applied to observational data under any circumstances"
    - "The product-of-coefficients method always overestimates indirect effects compared to counterfactual approaches"
  answer: 1
  explanation: "Causal mediation requires sequential ignorability: no unmeasured confounders of X→Y, AND no unmeasured confounders of M→Y conditional on X. In observational research, this second assumption is almost never satisfied. Unobserved variables (like underlying ability or motivation) may jointly cause both M (skills acquired) and Y (earnings), producing a spurious indirect effect. Demonstrating a statistically significant indirect effect in observational data does not establish that M causally mediates — it establishes that the data are consistent with mediation, conditional on strong untestable assumptions."

- question: "A researcher finds that the indirect effect of X on Y through M is statistically significant, but the direct effect of X on Y is zero (complete mediation). What can she most accurately conclude?"
  type: multiple-choice
  options:
    - "X causes Y entirely through M, and M is the causal mechanism"
    - "Full mediation is established, eliminating the need to consider other mediators"
    - "The data are consistent with complete mediation, but causal claims require sequential ignorability assumptions that must be stated explicitly and probed with sensitivity analyses"
    - "A zero direct effect means the model is misspecified — direct effects can never truly be zero"
  answer: 2
  explanation: "Statistical significance of the indirect effect and a zero direct effect are consistent with complete mediation — but 'consistent with' is not the same as 'establishes.' Causal language requires the sequential ignorability assumptions to hold. In observational data, the pattern could also result from unmeasured confounding. The correct posture is to report the finding, state the assumptions, and probe their plausibility with sensitivity analyses rather than asserting causal mediation. Options A and B use causal language ('causes,' 'established') that is not warranted by observational evidence alone."

- question: "When the effect of M on Y differs depending on the level of X (an X×M interaction exists), the simple product-of-coefficients formula for the indirect effect can give misleading results."
  type: true-false
  answer: true
  explanation: "The product-of-coefficients formula (indirect effect = a×b, where a is the X→M effect and b is the M→Y effect) assumes these paths are independent of X's value. When X moderates the M→Y relationship, this formula is incorrect. The counterfactual definitions of the natural indirect effect (NIE) and natural direct effect (NDE) correctly handle this case by integrating over the distribution of X, but they require more complex estimation (bootstrapping for confidence intervals, testing interaction terms). Ignoring X×M interactions when they exist produces biased decompositions."

- question: "Demonstrating a statistically significant indirect effect (X→M→Y) in a well-powered observational study is sufficient to conclude that M causally mediates the relationship between X and Y."
  type: true-false
  answer: false
  explanation: "Statistical significance addresses sampling error, not confounding. A significant indirect effect means the estimated indirect path is unlikely to be zero by chance — but it says nothing about whether unmeasured confounders are producing a spurious pattern. Causal mediation requires sequential ignorability: effective randomization of both X and M (conditional on X). In observational data, neither condition is easily satisfied, which is why mediation claims should be accompanied by explicit assumption statements and sensitivity analyses, not asserted as established mechanisms."

- question: "What is sequential ignorability in mediation analysis, and why does its violation mean that mediation findings from observational data should be interpreted cautiously?"
  type: short-answer
  answer: "Sequential ignorability requires two conditions: (1) no unmeasured confounders of the X→Y relationship (X is effectively randomized), and (2) no unmeasured confounders of the M→Y relationship conditional on X (M is effectively randomized given X). If either condition fails, the estimated indirect effect may be biased by variables that jointly cause M and Y or X and Y. In observational research, unmeasured factors like ability, motivation, or socioeconomic background routinely violate these assumptions, making it impossible to distinguish a true causal indirect effect from spurious correlation through a third variable."
  explanation: "This is why mediation claims from purely observational data are often overstated. The statistical machinery of mediation analysis runs correctly and produces a significant indirect effect — but the causal interpretation requires assumptions the data cannot verify. Sensitivity analyses (e.g., how strong would an unmeasured confounder need to be to explain away the indirect effect?) are the responsible way to probe these assumptions. When possible, experimental manipulation of X or M provides much stronger grounds for causal mediation claims."
```

## Explainer

From your linear regression background, you know that regression estimates the average relationship between a predictor and an outcome while holding other variables constant. Mediation analysis takes the next step: instead of just asking *whether* X affects Y, it asks *how* — through what pathway does the effect travel? This distinction between "does it work?" and "how does it work?" is the difference between establishing an effect and understanding a mechanism.

The basic setup has three variables. You have an independent variable X (a treatment, policy, or cause), an outcome Y, and a **mediator** M — an intermediate variable that lies on the causal path from X to Y. For example: does attending college increase lifetime earnings (X→Y)? Part of that effect might operate directly (employers value degrees per se), and part might operate through the skills and networks college develops (X→M→Y). Mediation analysis partitions the total effect into these pieces. The **direct effect** is the effect of X on Y that does not go through M. The **indirect effect** is the portion that travels through M. The two sum to the total effect.

The classical approach (Baron and Kenny's "causal steps" procedure) estimated these pieces using a series of regression equations: regress M on X, regress Y on X and M, and interpret coefficients. The indirect effect equals the product of two coefficients — the effect of X on M and the effect of M on Y controlling for X. This product-of-coefficients approach is still the core computational intuition. But modern mediation analysis, built on the **counterfactual framework** you may recognize from causal inference, is considerably more demanding. It requires **sequential ignorability**: X must be effectively randomized (no unmeasured confounders of X→Y), and M must also be effectively randomized conditional on X (no unmeasured confounders of M→Y). In observational research, neither assumption is easily satisfied, which is why mediation claims from purely observational data are often overstated.

The modern definitions of the **natural direct effect** (NDE) and **natural indirect effect** (NIE) handle the case where X modifies the effect of M on Y — that is, when the pathway through M works differently depending on the value of X. In this interaction case, the simple product-of-coefficients formula gives misleading results; counterfactual definitions correctly partition the total effect. In practice, this means testing for X×M interactions and using bootstrapping to construct confidence intervals for indirect effects, since the product of two regression coefficients doesn't follow a simple known distribution. The upshot for applied research: mediation analysis is a powerful tool for investigating mechanisms, but its causal interpretation requires strong assumptions that should be stated explicitly and probed with sensitivity analyses rather than assumed away.
