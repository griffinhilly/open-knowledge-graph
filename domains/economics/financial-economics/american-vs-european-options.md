---
id: american-vs-european-options
title: American versus European Options
domain: economics
course: financial-economics
prerequisites:
- id: options-basics-financial
  type: hard
- id: options-payoff-diagrams
  type: hard
builds-toward:
- option-trading-strategies
tags:
- options
- american
- european
- early-exercise
stage: formal-systems
status: draft
---

# American versus European Options

## Core Idea
European options can only be exercised at maturity, while American options can be exercised at any time before expiration. The early exercise feature gives American options greater value, especially calls on dividend-paying stocks and puts when interest rates are high. Closed-form pricing exists only for Europeans; Americans require numerical methods.

## How It's Best Learned
Compare American and European option prices on the same underlying using approximation formulas or binomial trees. Examine when early exercise is optimal (typically just before dividend payments for calls).
