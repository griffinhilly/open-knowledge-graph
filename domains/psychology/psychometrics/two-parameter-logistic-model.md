---
id: two-parameter-logistic-model
title: Two-Parameter Logistic IRT Model (2PL)
domain: psychology
course: psychometrics
prerequisites:
- id: rasch-model
  type: hard
- id: maximum-likelihood-estimation-theory
  type: soft
builds-toward:
- three-parameter-logistic-model
- irt-model-fit-comparison
tags:
- 2pl
- item-response-theory
- discrimination
- difficulty
stage: advanced
status: draft
---

# Two-Parameter Logistic IRT Model (2PL)

## Core Idea
The 2PL model adds discrimination as an item parameter alongside difficulty, allowing items to vary in how steeply performance increases with ability. This provides better empirical fit to many real datasets compared to the Rasch model but requires larger sample sizes and more computational complexity.

## Explainer

Recall from the Rasch model that every item was described by a single parameter: its difficulty (b), which positions the item on the ability scale at the point where a test-taker has a 50% probability of a correct response. All Rasch item characteristic curves (ICCs) have the same shape — they are identical logistic curves, just shifted left or right along the ability axis. The Rasch model's elegant property is that this uniformity allows for specific objectivity: person and item parameters are separable, and the model's fit can be tested. The cost is that in practice, real test items often differ not just in difficulty but in how sharply they discriminate between high and low ability examinees.

The **2PL model** adds a second parameter, **discrimination** (a), which controls the slope of the item characteristic curve at the point of inflection. An item with a high discrimination parameter (a ≈ 2.0) has a steeply rising ICC — it sharply differentiates examinees near its difficulty level. An item with low discrimination (a ≈ 0.3) has a shallow, nearly flat ICC — it provides little information about ability regardless of where the examinee falls on the ability scale. The probability of a correct response for person i on item j is: P(X=1|θ) = 1 / (1 + exp(−a(θ − b))). When a is constrained to 1.0 for all items, the 2PL reduces to the Rasch model (scaled by a constant).

The practical consequence of this second parameter is that items vary in their **information function** — the contribution they make to ability estimation at different points on the theta scale. A high-discrimination item provides concentrated information near its difficulty value but little information far from it. A low-discrimination item provides diffuse, weak information everywhere. The **item information function** is a(squared) × P(θ)(1 − P(θ)), which peaks at θ = b and scales with a squared. This makes discrimination the single most important item parameter for the precision of a fixed-length test.

Compared to the Rasch model, the 2PL is more flexible and typically fits real data better, but that flexibility comes with costs. Estimating the additional discrimination parameter requires substantially larger calibration samples (typically 500+ versus 200 for Rasch). The loss of Rasch's specific objectivity means that comparisons between examinees depend on which items are administered — the elegant invariance property weakens. In practice, the 2PL is the standard model for many large-scale educational assessments precisely because discrimination varies systematically across items and ignoring that variation produces biased ability estimates. The decision between Rasch and 2PL is ultimately an empirical one, made by comparing model fit to the data at hand.
