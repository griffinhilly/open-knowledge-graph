---
id: poverty-trap-mechanisms
title: Mechanisms of Poverty Traps
domain: economics
course: development-economics
prerequisites:
- id: poverty-trap-low-equilibrium
  type: hard
- id: differential-equations-intro
  type: hard
- id: fixed-point-iteration
  type: soft
builds-toward:
- human-capital-accumulation-development
- credit-constraints-poverty
tags:
- poverty-traps
- mechanisms
stage: advanced
status: draft
---

# Mechanisms of Poverty Traps

## Core Idea
Poverty traps operate through specific feedback loops: malnutrition reduces cognitive development and productivity (health-productivity loop), inability to borrow prevents education and business investment (credit constraints), and insufficient scale makes productive investments unprofitable (coordination failures). Identifying which mechanism dominates in a given context is essential for effective intervention design.

## Explainer

From your prerequisite on poverty traps, you understand that a low-income equilibrium is a stable fixed point — the economy tends to return there rather than escaping upward. But that model describes the shape of the trap without explaining why the curve bends the way it does. The mechanisms here are the micro-level feedback loops that generate the S-curve. Understanding them transforms the abstract fixed-point diagram into something concrete enough to intervene in.

The **health-productivity loop** is perhaps the most visceral mechanism. Insufficient nutrition impairs physical stamina, cognitive development, and immune function — all of which reduce productivity. Lower productivity means lower income, which means lower food expenditure, perpetuating the malnutrition. The key insight from differential equations is that this is a self-reinforcing dynamic: the derivative of income depends on current income through health. Below a threshold, the feedback is negative (conditions worsen), above it, positive (conditions improve). A farmer too malnourished to work full days cannot accumulate savings to improve their diet; the trap is not a preference but a biological constraint.

The **credit constraint mechanism** arises from information asymmetry in financial markets. High-return investments — education, business capital, land — require upfront payment. Without collateral or credit history, poor households cannot borrow at any interest rate, because lenders have no way to enforce repayment. So a small business owner who could double revenue with a $500 piece of equipment, but cannot pledge assets they don't own, remains stuck at a lower production level. This mechanism maps cleanly onto your fixed-point intuition: the investment function has a kink at the credit constraint, creating a threshold below which the household cannot move.

The **coordination failure mechanism** operates at the level of communities or regions, not just individuals. Some investments are only profitable if others also invest: a farmer won't irrigate fields if roads are too poor to transport produce to market; a transport company won't build roads if farms aren't productive enough to generate freight demand. Every agent's rational inaction makes everyone else's inaction rational too — a Nash equilibrium that is collectively suboptimal. This is a coordination trap, not just a low-income trap. The mathematical structure is one of multiple equilibria without any natural path from the bad equilibrium to the good one.

Distinguishing mechanisms matters for policy design. Health traps call for nutrition and public health interventions — in-kind transfers or conditional cash programs. Credit constraint traps suggest microfinance, collateral reform, or direct asset transfers to jump households over the threshold. Coordination failures require large coordinated interventions (the "big push") that bring multiple complementary investments online simultaneously — no single small intervention can succeed when the failure is systemic. A program well-matched to the wrong mechanism wastes resources; identifying the dominant mechanism is the first step in effective development policy.
