---
id: american-option-exercise-decisions
title: Optimal Exercise Decisions for American Options
domain: economics
course: financial-economics
prerequisites:
- id: american-vs-european-options
  type: hard
- id: option-intrinsic-and-time-value
  type: soft
builds-toward:
- options-greeks-trading-applications
tags:
- options
- exercise
- optimization
- american
stage: formal-systems
status: draft
---

# Optimal Exercise Decisions for American Options

## Core Idea
American options' early exercise feature has value when receiving the intrinsic value immediately dominates holding the option. For calls on non-dividend-paying stocks, early exercise is never optimal (time value exceeds intrinsic value). For puts, deep in-the-money puts may warrant early exercise. Dividend-paying stocks complicate decisions: large upcoming dividends can make early call exercise optimal.

## How It's Best Learned
Use binomial trees to solve the optimal exercise boundary and compare American and European option values under different scenarios.
