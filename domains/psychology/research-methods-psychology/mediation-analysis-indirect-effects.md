---
id: mediation-analysis-indirect-effects
title: Mediation Analysis and Indirect Effects in Causal Pathways
domain: psychology
course: research-methods-psychology
prerequisites:
- id: correlational-research-design
  type: soft
- id: inferential-statistics-psychology
  type: hard
- id: longitudinal-designs-temporal-change-patterns
  type: soft
- id: linear-regression
  type: soft
- id: correlation-coefficient
  type: hard
builds-toward:
- moderation-analysis-interaction-effects
- exploratory-vs-confirmatory-analysis-strategies
tags:
- analysis
- mediation
- indirect-effects
- mechanisms
stage: formal-systems
status: draft
---

# Mediation Analysis and Indirect Effects in Causal Pathways

## Core Idea
Mediation analysis examines the mechanisms through which an independent variable affects a dependent variable by identifying intermediate variables (mediators) that transmit the effect. For example, socioeconomic status may affect academic achievement through mediators of parental involvement and home resources. Mediation requires establishing: (1) effect of IV on DV, (2) effect of IV on mediator, (3) effect of mediator on DV, and (4) reduced direct effect of IV on DV when mediator is included. Mediation analysis can be conducted with experimental or observational data using regression, structural equation modeling, or multilevel approaches.

## How It's Best Learned
Identify a psychological effect you find interesting and theorize about potential mediators, then examine whether existing data supports the mediation model.

## Common Misconceptions
Correlation between variables implies mediation (actually, the specific pattern of indirect effects through a mediator defines mediation). Mediation proves the mechanism (actually, mediation analysis is consistent with a mechanism but cannot definitively prove causation from observational data).

## Questions

```yaml
- question: "A study finds that exercise (X) predicts lower depression (Y), that exercise predicts reduced inflammation (M), and that reduced inflammation predicts lower depression. A researcher claims inflammation mediates the exercise-depression link. What is the minimum additional analysis required to establish mediation?"
  type: multiple-choice
  options:
    - "Confirming that all three correlations are statistically significant"
    - "Showing that the direct effect of exercise on depression becomes non-significant when inflammation is controlled"
    - "Estimating and testing whether the indirect effect (a × b, the product of the X→M and M→Y paths) differs significantly from zero"
    - "Establishing that exercise was measured before depression in the study design"
  answer: 2
  explanation: "Showing that three pairwise correlations exist does not establish mediation — it only shows that the variables are related. Mediation requires specifically testing the *indirect effect*, the product of the a path (X→M) and the b path (M→Y controlling for X). This product captures whether the influence of X on Y actually flows *through* M. Modern practice uses bootstrapping to test whether the indirect effect's confidence interval excludes zero. The direct effect becoming non-significant (full mediation) is a possible outcome, but partial mediation is also valid — the indirect effect test is the core requirement either way."

- question: "A researcher uses observational data to show that number of books at home (M) fully mediates the relationship between parental education (X) and children's reading scores (Y). She concludes she has identified the causal mechanism. Which limitation applies most critically?"
  type: multiple-choice
  options:
    - "The analysis requires experimental data — observational mediation requires at least 1,000 participants"
    - "She should have used the Sobel test rather than bootstrapping for more accurate inference"
    - "Observational mediation cannot rule out unmeasured confounders — a third variable causing both M and Y would produce the same statistical pattern without genuine mediation"
    - "Mediation analysis only applies when the mediator is a continuous variable"
  answer: 2
  explanation: "This is the fundamental limitation of observational mediation. A confounder — say, parental reading habits — could cause both more books in the home (M) and higher reading scores (Y) independently, producing a significant indirect effect even if books do not causally transmit the effect of parental education. The mediation model is statistically consistent with a causal mechanism but cannot distinguish it from confounding without experimental control. Experimental designs (manipulating both X and M in a 2×2 factorial) or at least longitudinal designs establishing temporal order are needed for stronger causal claims."

- question: "Finding that X is correlated with M and M is correlated with Y is sufficient to establish that M mediates the X-Y relationship."
  type: true-false
  answer: false
  explanation: "Three pairwise correlations are a necessary but not sufficient condition for mediation. The specific requirement is that the *indirect effect* (a × b) is significant — that the influence of X on Y specifically flows through M. For example, all three correlations could exist if M is simply a common correlate of both X and Y with no mediating role. Testing mediation requires the product of the a and b paths and bootstrapped confidence intervals to determine whether that product is reliably nonzero."

- question: "In mediation analysis, the indirect effect is computed as the product of the a path (X→M) and the b path (M→Y while controlling for X)."
  type: true-false
  answer: true
  explanation: "The a path quantifies how much M changes per unit of X. The b path quantifies how much Y changes per unit of M, holding X constant (to isolate M's contribution net of any direct effect of X on Y). The product a × b represents the portion of X's total effect on Y that passes through M — the indirect effect. Baron and Kenny's original steps described mediation in terms of regression coefficients, and this product is now tested directly using bootstrapping rather than the Sobel test, which assumes a normal sampling distribution that often does not hold for products of coefficients."

- question: "Why is experimental manipulation of both X and M stronger evidence of mediation than finding the same statistical pattern in observational data? What would an ideal experimental test of mediation look like?"
  type: short-answer
  answer: "In observational data, any pattern consistent with X→M→Y could equally reflect confounding — unmeasured variables that affect both M and Y — making it impossible to conclude that M causally transmits X's effect. An ideal experimental test uses a 2×2 factorial design: X is randomly assigned (e.g., stress vs. no stress), and M is also manipulated independently (e.g., rumination induced vs. blocked). If the effect of X on Y is eliminated when M is blocked, and reintroduced when M is activated, this provides direct evidence that M is the causal mechanism — confounders are controlled by randomization and the mediating role is tested directly rather than inferred from correlations."
  explanation: "Experimental mediation designs (attributed to Spencer, Zanna, and Fong) provide what observational mediation cannot: causal identification. The logic is similar to surgical dissection — by manipulating the proposed mechanism directly, you can confirm or disconfirm that it is genuinely necessary for the X→Y effect. When full experiments are not possible, longitudinal designs at least establish temporal order (X before M, M before Y), which is a necessary if not sufficient condition for the causal chain."
```

## Explainer

A simple regression tells you whether X predicts Y. Mediation analysis asks a more specific question: *through what pathway* does X affect Y? The basic structure is a chain: X influences M (the **mediator**), and M in turn influences Y. The interest lies in the **indirect effect** — the portion of X's influence on Y that operates through M — rather than (or in addition to) the **direct effect**, which is X's remaining influence on Y after M is accounted for. Understanding this distinction requires you to mentally decompose the total relationship between X and Y into its constituent causal steps.

The most intuitive way to see this is with an example. Suppose you find that socioeconomic status (X) predicts academic achievement (Y). The correlation is real, but it does not reveal the mechanism. Mediation analysis might ask whether parental involvement (M) is the pathway: children from higher-SES families receive more homework support and educational enrichment, which then produces higher achievement. The **a path** is the effect of SES on parental involvement; the **b path** is the effect of parental involvement on achievement while controlling for SES. The indirect effect is the product of these two paths: a × b. If this product is significant and confidence intervals from bootstrapping exclude zero, the evidence is consistent with mediation. The direct effect (c') tells you how much SES still predicts achievement *beyond* the mediation pathway — whether partial or full mediation has occurred.

From your regression background, you can see that each path is estimated by a standard regression coefficient. What makes mediation analysis more than two regressions run separately is the focus on the **product of coefficients** (a × b) and the need to test whether that product differs significantly from zero. Classical approaches used the Sobel test for this, but the Sobel test assumes a normal sampling distribution for the product, which is often violated. Modern practice uses **bootstrapping**: resample the data thousands of times, compute the indirect effect in each resample, and derive confidence intervals from the empirical distribution. This approach makes no assumption about the shape of the sampling distribution and is strongly preferred.

The most important limitation of mediation analysis is causal: demonstrating that X → M → Y fits your data does not prove it is the mechanism unless you have experimental control. In observational data, the M–Y relationship could reflect confounding — a third variable that causes both M and Y could produce the same statistical signature as genuine mediation. Experimental mediation designs, where both X and M are manipulated in a 2×2 design, provide stronger causal leverage. When experimental manipulation is not possible, longitudinal designs with X measured before M, and M measured before Y, at least establish the temporal order required by causal claims. Mediation analysis is best understood as a tool for *testing the plausibility* of a theorized mechanism, not as a method that establishes causal processes from correlational data alone.
