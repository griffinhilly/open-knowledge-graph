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

## Explainer

A simple regression tells you whether X predicts Y. Mediation analysis asks a more specific question: *through what pathway* does X affect Y? The basic structure is a chain: X influences M (the **mediator**), and M in turn influences Y. The interest lies in the **indirect effect** — the portion of X's influence on Y that operates through M — rather than (or in addition to) the **direct effect**, which is X's remaining influence on Y after M is accounted for. Understanding this distinction requires you to mentally decompose the total relationship between X and Y into its constituent causal steps.

The most intuitive way to see this is with an example. Suppose you find that socioeconomic status (X) predicts academic achievement (Y). The correlation is real, but it does not reveal the mechanism. Mediation analysis might ask whether parental involvement (M) is the pathway: children from higher-SES families receive more homework support and educational enrichment, which then produces higher achievement. The **a path** is the effect of SES on parental involvement; the **b path** is the effect of parental involvement on achievement while controlling for SES. The indirect effect is the product of these two paths: a × b. If this product is significant and confidence intervals from bootstrapping exclude zero, the evidence is consistent with mediation. The direct effect (c') tells you how much SES still predicts achievement *beyond* the mediation pathway — whether partial or full mediation has occurred.

From your regression background, you can see that each path is estimated by a standard regression coefficient. What makes mediation analysis more than two regressions run separately is the focus on the **product of coefficients** (a × b) and the need to test whether that product differs significantly from zero. Classical approaches used the Sobel test for this, but the Sobel test assumes a normal sampling distribution for the product, which is often violated. Modern practice uses **bootstrapping**: resample the data thousands of times, compute the indirect effect in each resample, and derive confidence intervals from the empirical distribution. This approach makes no assumption about the shape of the sampling distribution and is strongly preferred.

The most important limitation of mediation analysis is causal: demonstrating that X → M → Y fits your data does not prove it is the mechanism unless you have experimental control. In observational data, the M–Y relationship could reflect confounding — a third variable that causes both M and Y could produce the same statistical signature as genuine mediation. Experimental mediation designs, where both X and M are manipulated in a 2×2 design, provide stronger causal leverage. When experimental manipulation is not possible, longitudinal designs with X measured before M, and M measured before Y, at least establish the temporal order required by causal claims. Mediation analysis is best understood as a tool for *testing the plausibility* of a theorized mechanism, not as a method that establishes causal processes from correlational data alone.
