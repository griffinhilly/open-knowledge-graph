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
stage: advanced
status: draft
---

# Mediation Analysis and Pathways

## Core Idea
Mediation analysis decomposes a total causal effect into natural direct effects (paths not operating through the mediator) and natural indirect effects (pathways operating through a mediator). Understanding mediation requires carefully specifying the causal pathway and assumes no unmeasured confounding of the mediator-outcome relationship. Modern mediation methods can handle interactions between exposure and mediator, mediator-outcome confounding, and cross-level interactions.

## How It's Best Learned
Draw DAGs for exposure → mediator → outcome; calculate controlled and natural direct/indirect effects using counterfactual definitions.

## Common Misconceptions
Mediation analysis is simply about statistical association and regression adjustment. The indirect effect is always smaller than the total effect (with interactions it can exceed the total).

## Explainer

Your prerequisite in directed acyclic graphs (DAGs) gave you a visual language for causal structure: nodes for variables, directed edges for causal relationships, and formal rules for identifying confounding paths, colliders, and valid adjustment sets. Your counterfactual framework formalized the idea of a causal effect as a comparison between potential outcomes under different exposure levels. Mediation analysis brings these two tools together to answer a more refined question: not just whether an exposure causes an outcome, but *how* — through which intermediate variables does the effect operate? This decomposition has direct practical consequences, because an intervention that blocks only one pathway will succeed or fail depending on how much of the total effect runs through that pathway.

The foundational distinction is between the **natural direct effect (NDE)** and the **natural indirect effect (NIE)**. Consider a DAG with exposure X → mediator M → outcome Y, plus the direct path X → Y (bypassing M). The NDE is the effect of X on Y that does *not* operate through M — formally, the contrast E[Y(x, M(x*))] − E[Y(x*, M(x*))] where M is fixed at the value it would take under the reference exposure level x*. The NIE is the effect that operates through M — formally, E[Y(x, M(x))] − E[Y(x, M(x*))], where X is held fixed at the active level while M is allowed to vary between what it would be under x versus x*. Under no interaction between X and M, the total effect equals NDE + NIE. The fraction mediated — NIE / Total effect — answers "how much of this effect runs through this pathway?"

The counterfactual definitions make clear why mediation is not simply about adding M to a regression model and comparing coefficients. The definitions involve **cross-world counterfactuals**: Y(x, M(x*)) imagines an individual simultaneously exposed to x but with a mediator value as if they received x* — a scenario that cannot be directly observed. This matters because regression-based "product of coefficients" approaches implicitly assume no interaction and no confounding of the mediator-outcome relationship, assumptions that are often violated. Because randomization of the exposure X does not automatically randomize M, the mediator-outcome relationship can be confounded even in a randomized trial. Modern mediation methods require explicitly assuming (and ideally checking) no unmeasured confounding of the M→Y pathway after adjusting for baseline covariates.

When the exposure and mediator **interact** — when the effect of M on Y depends on the level of X, or vice versa — the mediation decomposition becomes richer and the policy implications change. VanderWeele's **four-way decomposition** separates the total effect into components due to mediation alone, interaction alone, both mediation and interaction (the mediated interaction), and neither. Interaction matters practically: if exercise reduces cardiovascular risk partly through BMI reduction, but the BMI effect is substantially larger among people who exercise (an interaction), then an intervention targeting BMI without changing exercise will underperform predictions based on a simple additive mediation model. Conversely, the **indirect effect can exceed the total effect** when there is masking — when the direct effect and indirect effect operate in opposite directions. Understanding mediation correctly requires the full causal infrastructure your prerequisites built: the DAG to specify the pathway structure, and the counterfactual framework to define effects precisely enough to distinguish mediation from mere statistical association.
