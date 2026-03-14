---
id: arbitrage-pricing-theory
title: Arbitrage Pricing Theory (APT) and Factor Models
domain: economics
course: financial-economics
prerequisites:
- id: capital-asset-pricing-model
  type: hard
- id: multiple-regression-model
  type: soft
builds-toward:
- risk-adjusted-performance-measures
tags:
- apt
- factor-models
- fama-french
- multi-factor
- arbitrage
stage: formal-systems
status: validated
---

# Arbitrage Pricing Theory (APT) and Factor Models

## Core Idea
Arbitrage Pricing Theory (APT), developed by Stephen Ross, generalizes CAPM by allowing multiple systematic risk factors to drive expected returns: E[rᵢ] = rₓ + β₁λ₁ + β₂λ₂ + … + βₖλₖ, where each βⱼ is the factor loading and λⱼ is the associated risk premium. APT is derived purely from the no-arbitrage condition — if expected returns were not proportional to factor exposures, investors could construct a zero-investment, zero-risk portfolio with positive expected return, which cannot persist. Empirical implementations include the Fama-French three-factor model (market, size, value) and the Carhart four-factor model (adding momentum), which substantially outperform one-factor CAPM in explaining cross-sectional return variation.

## How It's Best Learned
Understand the no-arbitrage derivation: if a diversified portfolio with zero factor exposure has positive expected return, it is an arbitrage opportunity that rational investors immediately exploit. Estimate a three-factor regression for a mutual fund to decompose its performance into factor exposures and true alpha.

## Common Misconceptions
- APT does not specify which factors to use — factor identification is purely empirical, leaving the theory open-ended in a way that can be misused.
- APT does not render CAPM obsolete — CAPM is the special one-factor case of APT; they share the same logical foundation.
