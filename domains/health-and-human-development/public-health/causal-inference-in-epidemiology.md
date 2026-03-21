---
id: causal-inference-in-epidemiology
title: Causal Inference in Epidemiology
domain: health-and-human-development
course: public-health
prerequisites:
- id: epidemiology-foundations
  type: hard
- id: confounding-epidemiology
  type: hard
builds-toward:
- mediation-analysis-epidemiology
- instrumental-variables-epidemiology
tags:
- causal-inference
- confounding
- dags
- bias-adjustment
- identification
stage: advanced
status: draft
---

# Causal Inference in Epidemiology

## Core Idea
Causal inference in epidemiology moves beyond identifying associations to establishing causal relationships using directed acyclic graphs (DAGs), confounding adjustment, and identification strategies. Hill's criteria provide a framework for evaluating causality from observational data when randomized experiments are infeasible or unethical. Understanding counterfactual thinking and potential outcomes frameworks is essential for valid causal conclusions.

## How It's Best Learned
Work through real epidemiologic studies to identify confounders, draw DAGs, and interpret adjusted versus unadjusted analyses. Practice using sensitivity analysis to test robustness of causal conclusions to residual confounding.

## Common Misconceptions
Assuming all confounding is eliminated through statistical adjustment. Believing correlation proves causation just because confounding is ruled out. Confusing confounding with effect modification.

## Questions

```yaml
- question: "A researcher studying exercise's effect on cardiovascular disease adjusts for resting heart rate in their model. Resting heart rate is actually on the causal pathway from exercise to CVD — lower resting heart rate is one mechanism through which exercise reduces CVD risk. What is the consequence of this adjustment?"
  type: multiple-choice
  options:
    - "The analysis becomes more accurate by removing a confounder that distorted the estimate"
    - "The analysis introduces selection bias by restricting to a specific subgroup"
    - "The estimated effect of exercise is attenuated, underestimating the total causal effect of exercise on CVD"
    - "No consequence — adjusting for any variable associated with both exposure and outcome improves causal estimates"
  answer: 2
  explanation: "Resting heart rate is a mediator — a variable on the causal pathway from exercise to cardiovascular outcomes. Adjusting for a mediator blocks part of the causal effect you are trying to estimate. The remaining estimate captures only the portion of exercise's effect that does not operate through resting heart rate, underestimating the total causal effect. DAGs make this pitfall explicit: conditioning on a node on the directed path from exposure to outcome removes that path from the analysis. Adjusting for all variables associated with both exposure and outcome is not a safe rule — the DAG-based approach requires distinguishing confounders (should be adjusted) from mediators (should not, for total effect estimation) and colliders (must not be adjusted)."

- question: "In a DAG, a researcher conditions on a collider — a variable with arrows pointing INTO it from both the exposure and the outcome. What happens to the exposure-outcome association?"
  type: multiple-choice
  options:
    - "A spurious association between the exposure and outcome is introduced where none previously existed"
    - "The analysis is improved because conditioning on a collider blocks a non-causal backdoor path"
    - "The association is unchanged — colliders have no effect on estimates when conditioned on"
    - "The true causal association is revealed more clearly by removing the collider's distorting effect"
  answer: 0
  explanation: "Conditioning on a collider opens a path between its causes — in this case, the exposure and outcome. If the exposure and outcome both independently cause the collider, then knowing the collider's value makes the exposure and outcome statistically dependent even if they have no causal relationship. This 'collider stratification bias' is the opposite of what most researchers intuit: unlike confounders (which should be adjusted) and mediators (which usually should not), colliders must NOT be conditioned on to obtain unbiased causal estimates. DAGs are the primary tool for identifying colliders and recognizing when conditioning introduces rather than removes bias."

- question: "Adjusting for all measured variables that are associated with both the exposure and outcome will eliminate confounding and yield an unbiased causal estimate."
  type: true-false
  answer: false
  explanation: "This is a common and dangerous misconception. Adjusting for all associated variables will inadvertently include mediators (attenuating causal effects) and colliders (introducing spurious associations where none existed). Furthermore, even perfect adjustment for measured confounders cannot address unmeasured confounding, and residual confounding from measurement error can leave substantial bias. The DAG-based approach requires reasoning about the causal structure first, then selecting a valid adjustment set based on the backdoor criterion — not mechanically adjusting for everything associated with exposure and outcome."

- question: "Temporality — the requirement that a cause precede its effect — is the only one of Hill's criteria that is logically necessary for a causal interpretation."
  type: true-false
  answer: true
  explanation: "The other Hill criteria (strength, consistency, specificity, biological gradient, plausibility, coherence, experimental evidence, analogy) increase or decrease confidence in a causal interpretation but none is logically necessary — a causal relationship could be weak, inconsistent across studies, or biologically unexplained and still be causal. Temporality is the exception: by definition, a cause cannot follow its effect. If the outcome is shown to precede the putative exposure, the hypothesized causal direction is ruled out. This is why longitudinal study design — which establishes exposure measurement before outcome — is methodologically fundamental in epidemiology."

- question: "In the counterfactual framework, why can an observational study never directly answer a causal question in the same way a randomized controlled trial can?"
  type: short-answer
  answer: "The counterfactual definition of causation asks: what would have happened to this person had they not been exposed? For any individual, we can only observe one state — exposed or unexposed — never both simultaneously. In an RCT, random assignment makes exposed and unexposed groups identical in expectation on all other variables, so the unexposed group serves as a valid counterfactual for the exposed group at the population level. In an observational study, people who are exposed differ from those who are not in ways often related to the outcome (confounding, selection), so the unexposed group is not a valid counterfactual. All observational causal inference methods — regression adjustment, instrumental variables, matching — are attempts to construct a valid counterfactual comparison, but they depend on untestable assumptions that RCT randomization satisfies by design."
  explanation: "This is why epidemiologic causal inference is described as making the observational comparison 'as if randomized' through analytical means — it is an approximation to the counterfactual, not the counterfactual itself. The strength of a causal claim from observational data depends on the plausibility of the assumptions underlying the approximation, which is why DAGs, sensitivity analyses, and explicit assumption-naming are essential rather than optional."
```

## Explainer

From your study of epidemiology foundations and confounding, you already understand that an observed association between an exposure and outcome may be distorted by third variables — confounders that are related to both. Causal inference takes the next step: given that you have measured an association and controlled for confounders, how do you decide whether the relationship is actually causal? This question cannot be answered by statistical analysis alone. It requires a conceptual framework for what causation means and what evidence pattern would distinguish a genuine cause from a spurious or confounded relationship.

The **counterfactual framework** provides the clearest definition of causation in epidemiology. A cause is something whose presence changes an outcome relative to what would have happened in its absence — the counterfactual. "Would this person have developed disease if they had not been exposed?" is the causal question. In a randomized trial, random assignment ensures the exposed and unexposed groups are comparable on all other factors, so the counterfactual can be approximated by comparing outcomes across arms. In observational data, we can never directly observe both states (exposed and unexposed) for the same person at the same time — we must construct a comparison group that resembles the counterfactual. This is precisely why confounding and selection bias are so pernicious: they corrupt the comparison group, making it non-representative of what would have happened under the counterfactual condition.

**Directed acyclic graphs (DAGs)** are the primary tool for reasoning clearly about confounding, mediation, and selection bias. A DAG represents variables as nodes and causal relationships as directed arrows — you draw what you believe about the causal structure, then use graph rules to identify which variables must be adjusted for to block non-causal paths. The key insight is that not all associated variables should be adjusted: adjusting for a **mediator** (a variable on the causal pathway from exposure to outcome) removes part of the causal effect you are trying to measure, and adjusting for a **collider** (a variable with arrows from both exposure and outcome pointing into it) can *introduce* spurious associations that did not previously exist. DAGs make these pitfalls explicit by allowing you to trace paths between variables and apply the **backdoor criterion** to identify valid adjustment sets.

**Hill's criteria** — proposed by Austin Bradford Hill in 1965 and still used to evaluate causal claims from observational data — list nine features that strengthen a causal inference: strength of association, consistency across studies, specificity, temporality (cause precedes effect), biological gradient (dose-response), plausibility, coherence with existing knowledge, experimental evidence where available, and analogy. Temporality is the only criterion that is logically necessary — a cause cannot follow its effect — but the others increase or decrease confidence in causal interpretation. Applying them rigorously reveals why even a large, consistent, biologically plausible association (like early evidence linking smoking to lung cancer) required sustained accumulation across multiple lines of evidence before the causal claim was accepted. Causal inference is ultimately a judgment about the totality of evidence, not a single statistical threshold — and learning to make that judgment explicitly, rather than collapsing it into a p-value, is what distinguishes epidemiologic thinking from mere pattern detection.
