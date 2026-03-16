---
id: item-response-theory-assumptions
title: 'Item Response Theory: Assumptions and Fundamentals'
domain: psychology
course: psychometrics
prerequisites:
- id: item-response-functions
  type: hard
- id: classical-test-theory
  type: hard
- id: probability-density-functions-theory
  type: soft
- id: normal-distribution
  type: soft
- id: probability-mass-functions
  type: hard
- id: probability-axioms
  type: hard
builds-toward:
- ability-parameter-estimation-theta-estimation
- classical-vs-irt-item-analysis
tags:
- irt
- assumptions
- unidimensionality
- local-independence
stage: advanced
status: draft
---

# Item Response Theory: Assumptions and Fundamentals

## Core Idea
IRT assumes unidimensionality (one latent ability drives responses), local independence (responses independent given ability), and monotonic item response functions. These assumptions are more restrictive than classical test theory but enable item-level precision and ability-independent item statistics. Testing assumptions is essential before IRT application.

## How It's Best Learned
Fit IRT models to real datasets and examine residuals and goodness-of-fit indices. Use dimensionality tests and compare unidimensional vs. multidimensional models.

## Common Misconceptions
- Assuming unidimensionality requires perfect homogeneity (acceptable even with small secondary factors)
- Local independence is violated when content is highly related (it means independence GIVEN ability, not necessarily in raw data)

## Explainer

Classical test theory (CTT), which you have already studied, treats a test as a whole — every statistic (reliability, item difficulty, item discrimination) is computed relative to the specific sample and the specific test. Swap the sample, and item statistics change. Shorten the test, and reliability estimates change. IRT was developed to escape this sample-and-test dependency, but doing so requires stronger assumptions about the structure of the data. Understanding those assumptions is not optional overhead — it is the key to understanding why IRT works when it works, and why it fails when it fails.

The first and most fundamental assumption is **unidimensionality**: all items in the test are measuring a single underlying latent ability or trait, denoted θ. This does not mean items must be identical — a math test can have geometry and algebra items that differ in content — but it does mean that one common factor accounts for all the covariation among responses. In practice, perfect unidimensionality is never achieved; most tests have dominant factors with minor secondary ones. The working standard is that IRT is robust to minor multidimensionality but breaks down when secondary factors are substantial. Confirmatory factor analysis and parallel analysis are the standard tools for evaluating this assumption before fitting IRT models.

The second assumption is **local independence**: given a person's true ability level θ, knowing their response to one item provides no additional information about their response to any other item. This is the conditional independence assumption from your probability prerequisites — mathematically, P(X_i, X_j | θ) = P(X_i | θ) × P(X_j | θ). Local independence is not the same as saying items are uncorrelated in raw data; highly correlated items can still satisfy local independence if the correlation is fully explained by the shared latent ability. Local independence is violated, for example, when two items share a reading passage, so that reading skill for that passage creates an item-cluster effect beyond general ability. Violations inflate item information and produce artificially high reliability estimates.

The third assumption is a **monotone item response function**: higher ability must always be associated with a higher (or equal) probability of correct response. No IRT model tolerates items where very high-ability people are *less* likely to answer correctly than moderate-ability people (which would indicate item flaws like implausible distractors that trap sophisticated test-takers). Together, these three assumptions define the measurement model that IRT requires. When they hold, IRT delivers **parameter invariance** — the great payoff that item difficulty parameters estimated in one sample apply to others, and ability parameters estimated from one set of items apply when different items are used. This invariance is what enables item banking, CAT, and test equating — applications that CTT cannot support.
