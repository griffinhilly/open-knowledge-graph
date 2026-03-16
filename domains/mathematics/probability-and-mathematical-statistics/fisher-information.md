---
id: fisher-information
title: Fisher Information
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: expectation-measure-theoretic
  type: hard
- id: distribution-functions-densities-rigorous
  type: hard
builds-toward:
- cramer-rao-lower-bound
- asymptotic-normality-mle
tags:
- fisher-information
- information-theory
- statistics
stage: advanced
status: draft
---

# Fisher Information

## Core Idea
The Fisher information is I(θ) = E[(∂log f(X|θ)/∂θ)²] = -E[∂²log f(X|θ)/∂θ²]. It quantifies how much information the data carries about θ: larger I means θ is more precisely estimable. For n i.i.d. observations, Iₙ(θ) = nI(θ). Fisher information appears in the Cramer-Rao bound and characterizes the asymptotic variance of MLEs.
