---
id: mediation-analysis-epidemiology
title: Mediation Analysis and Pathways
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: counterfactual-framework
  type: hard
- id: directed-acyclic-graphs
  type: hard
tags:
- causal-pathways
- direct-indirect-effects
- mechanisms
stage: expert
status: draft
---

# Mediation Analysis and Pathways

## Core Idea
Mediation analysis decomposes a total causal effect into natural direct effects (paths not operating through the mediator) and natural indirect effects (pathways operating through a mediator). Understanding mediation requires carefully specifying the causal pathway and assumes no unmeasured confounding of the mediator-outcome relationship. Modern mediation methods can handle interactions between exposure and mediator, mediator-outcome confounding, and cross-level interactions.

## How It's Best Learned
Draw DAGs for exposure → mediator → outcome; calculate controlled and natural direct/indirect effects using counterfactual definitions.

## Common Misconceptions
Mediation analysis is simply about statistical association and regression adjustment. The indirect effect is always smaller than the total effect (with interactions it can exceed the total).

## Questions

```yaml
- question: "A researcher runs a randomized trial of a dietary intervention (X) on cardiovascular disease (Y), with BMI as a proposed mediator (M). A colleague suggests adding BMI to the regression to isolate the direct effect of X. Why is this approach insufficient for valid mediation analysis?"
  type: multiple-choice
  options:
    - "Randomization ensures there is no confounding of the M→Y relationship, so regression adjustment is valid"
    - "Adding M to the regression produces unbiased estimates only if there is no interaction between X and M"
    - "Randomization of X does not randomize M, so the M→Y relationship can still be confounded by baseline variables"
    - "The product-of-coefficients method fails only when the outcome is binary"
  answer: 2
  explanation: "Randomizing the exposure X ensures no confounding of X→Y overall, but it does not randomize the mediator M. Baseline characteristics that affect both BMI and cardiovascular disease (e.g., baseline fitness, diet quality before the trial) can confound the M→Y pathway even in a perfectly executed RCT. Valid mediation analysis requires explicitly assuming (and adjusting for) no unmeasured confounding of the mediator-outcome relationship — an assumption randomization alone cannot guarantee."

- question: "A mediation study reports that the natural indirect effect (NIE) of exposure X on outcome Y through mediator M is larger in magnitude than the total effect of X on Y. What is the most plausible interpretation?"
  type: multiple-choice
  options:
    - "There is a calculation error — the NIE can never exceed the total effect by definition"
    - "The direct effect and indirect effect operate in opposite directions, with the direct effect partially canceling the indirect effect"
    - "The mediator M fully accounts for all of X's effect on Y, leaving no direct pathway"
    - "The exposure has no causal effect on the outcome and all observed association is spurious"
  answer: 1
  explanation: "When a direct effect (NDE) and indirect effect (NIE) operate in opposite directions — one positive, one negative — they partially cancel, making the total effect smaller than either component alone. This is called masking or suppression. The NIE can legitimately exceed the total effect in this scenario: Total = NDE + NIE, so if NDE is negative and NIE is positive, NIE > Total. Thinking the NIE can never exceed the total is the classic misconception that assumes the additive decomposition involves only same-sign components."

- question: "In a properly randomized trial, the natural direct effect of exposure on outcome can be estimated without any additional assumptions about confounding."
  type: true-false
  answer: false
  explanation: "Randomization of the exposure eliminates confounding of the total exposure-outcome effect, but mediation analysis requires estimating the natural direct effect — which involves the counterfactual Y(x, M(x*)), fixing the mediator at the value it would take under the reference exposure. Because this cross-world counterfactual involves M, which was not randomized, confounding of the M→Y pathway remains a real threat. Estimating the NDE requires additional assumptions — specifically, no unmeasured confounding of mediator-outcome given baseline covariates — that the trial design does not automatically satisfy."

- question: "When there is an interaction between the exposure and the mediator, the total effect equals the natural direct effect plus the natural indirect effect."
  type: true-false
  answer: false
  explanation: "The simple additive decomposition Total = NDE + NIE holds only when there is no interaction between the exposure and the mediator. When interaction is present, VanderWeele's four-way decomposition is needed: the total effect separates into a component due to mediation alone, interaction alone, mediated interaction, and neither. Adding only NDE and NIE in the presence of interaction conflates the interaction component with one of the other parts, yielding an incorrect decomposition."

- question: "Why do counterfactual definitions of mediation involve 'cross-world' quantities, and why does this make regression-based product-of-coefficients approaches problematic?"
  type: short-answer
  answer: "The natural direct effect requires comparing Y(x, M(x*)) — the outcome when exposed to x but with the mediator at the value it would take under the reference x* — to Y(x*, M(x*)). These two potential outcomes fix the mediator at a value from a different exposure level, creating a 'cross-world' counterfactual that cannot be directly observed in any individual. Product-of-coefficients regression implicitly assumes no interaction and no mediator-outcome confounding; when these assumptions fail, the coefficients no longer correspond to the counterfactual quantities NDE and NIE."
  explanation: "Cross-world counterfactuals are unobservable because no individual can simultaneously be exposed to x and have a mediator value as if they received x*. This is why the identifying assumptions — no unmeasured confounding of X→Y, X→M, and M→Y — must be stated explicitly. Regression 'adjustment' for a mediator treats M as just another covariate, implicitly assuming these confounding conditions hold, without formally acknowledging them as assumptions that could be violated."
```

## Explainer

Your prerequisite in directed acyclic graphs (DAGs) gave you a visual language for causal structure: nodes for variables, directed edges for causal relationships, and formal rules for identifying confounding paths, colliders, and valid adjustment sets. Your counterfactual framework formalized the idea of a causal effect as a comparison between potential outcomes under different exposure levels. Mediation analysis brings these two tools together to answer a more refined question: not just whether an exposure causes an outcome, but *how* — through which intermediate variables does the effect operate? This decomposition has direct practical consequences, because an intervention that blocks only one pathway will succeed or fail depending on how much of the total effect runs through that pathway.

The foundational distinction is between the **natural direct effect (NDE)** and the **natural indirect effect (NIE)**. Consider a DAG with exposure X → mediator M → outcome Y, plus the direct path X → Y (bypassing M). The NDE is the effect of X on Y that does *not* operate through M — formally, the contrast E[Y(x, M(x*))] − E[Y(x*, M(x*))] where M is fixed at the value it would take under the reference exposure level x*. The NIE is the effect that operates through M — formally, E[Y(x, M(x))] − E[Y(x, M(x*))], where X is held fixed at the active level while M is allowed to vary between what it would be under x versus x*. Under no interaction between X and M, the total effect equals NDE + NIE. The fraction mediated — NIE / Total effect — answers "how much of this effect runs through this pathway?"

The counterfactual definitions make clear why mediation is not simply about adding M to a regression model and comparing coefficients. The definitions involve **cross-world counterfactuals**: Y(x, M(x*)) imagines an individual simultaneously exposed to x but with a mediator value as if they received x* — a scenario that cannot be directly observed. This matters because regression-based "product of coefficients" approaches implicitly assume no interaction and no confounding of the mediator-outcome relationship, assumptions that are often violated. Because randomization of the exposure X does not automatically randomize M, the mediator-outcome relationship can be confounded even in a randomized trial. Modern mediation methods require explicitly assuming (and ideally checking) no unmeasured confounding of the M→Y pathway after adjusting for baseline covariates.

When the exposure and mediator **interact** — when the effect of M on Y depends on the level of X, or vice versa — the mediation decomposition becomes richer and the policy implications change. VanderWeele's **four-way decomposition** separates the total effect into components due to mediation alone, interaction alone, both mediation and interaction (the mediated interaction), and neither. Interaction matters practically: if exercise reduces cardiovascular risk partly through BMI reduction, but the BMI effect is substantially larger among people who exercise (an interaction), then an intervention targeting BMI without changing exercise will underperform predictions based on a simple additive mediation model. Conversely, the **indirect effect can exceed the total effect** when there is masking — when the direct effect and indirect effect operate in opposite directions. Understanding mediation correctly requires the full causal infrastructure your prerequisites built: the DAG to specify the pathway structure, and the counterfactual framework to define effects precisely enough to distinguish mediation from mere statistical association.
