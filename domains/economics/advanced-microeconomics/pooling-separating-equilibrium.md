---
id: pooling-separating-equilibrium
title: Pooling and Separating Equilibria
domain: economics
course: advanced-microeconomics
prerequisites:
- id: adverse-selection-signaling
  type: hard
- id: bayesian-games-incomplete-info
  type: hard
tags:
- contract-theory
- information-asymmetry
- equilibrium
stage: advanced
status: draft
---

# Pooling and Separating Equilibria

## Core Idea
In signaling games, a separating equilibrium is one where different types take different actions, fully revealing types. A pooling equilibrium is one where all types take identical action, revealing no information. Market unraveling can occur when high-quality types find pooling equilibrium pay too low relative to signaling cost, causing them to exit, degrading average quality.

## Explainer

From signaling theory, you know that an informed party can take costly actions to credibly communicate their private type to an uninformed party. From Bayesian games, you know how to model situations where players have private information and update beliefs about others using Bayes' rule. **Pooling and separating equilibria** describe the two polar outcomes that can emerge: either the signal perfectly reveals type, or it reveals nothing at all.

In a **separating equilibrium**, different types choose different signals, and the uninformed party can perfectly infer type from the observed action. The classic example is Spence's job market signaling model: high-ability workers get college degrees, low-ability workers do not, and employers pay accordingly. The mechanism works because signaling must be **differentially costly** — education must be cheaper (in effort, time, or psychic cost) for high-ability types than for low-ability types. In equilibrium, high types choose a level of education that is worth the cost given the wage premium it earns, while low types find that same level of education too costly relative to the payoff. The **single-crossing condition** — the requirement that different types have different marginal costs of signaling — is what makes separation possible. Without it, low types would simply mimic high types and the signal would be uninformative.

In a **pooling equilibrium**, all types choose the same signal, and the uninformed party learns nothing beyond their prior beliefs. In the education example, this would mean all workers get the same level of education (possibly none), and employers pay everyone the average-quality wage. Pooling equilibria can be sustained when the signaling cost is too high for the benefit, or when the proportion of high types is large enough that the pooling wage is acceptable to them. But pooling equilibria are often fragile — they can unravel when high-quality types deviate. If a high-type worker can acquire slightly more education at a cost that is less than the wage increase from being recognized as high-type, the pooling equilibrium breaks down.

The choice between pooling and separating outcomes has profound implications for **market efficiency**. In a separating equilibrium, information is revealed but at a real resource cost — education is consumed purely as a signal, not because it increases productivity. Society bears a deadweight loss from the signaling activity itself. In a pooling equilibrium, signaling costs are avoided, but high-quality types are underpaid (receiving the average wage rather than their marginal product), which may cause them to exit the market or reduce effort. **Semi-separating** (or partial pooling) equilibria can also exist, where some types mix between signals and the uninformed party updates beliefs but does not achieve full type separation. The framework applies far beyond labor markets: warranty terms signal product quality, dividend policy signals firm profitability, and insurance contract menus screen for risk types. In each case, the central question is the same — does the equilibrium fully separate, fully pool, or achieve some intermediate level of information revelation?
