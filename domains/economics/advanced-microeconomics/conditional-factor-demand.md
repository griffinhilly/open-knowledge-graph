---
id: conditional-factor-demand
title: Conditional Factor Demand
domain: economics
course: advanced-microeconomics
prerequisites:
- id: cost-function-duality
  type: hard
tags:
- producer-theory
- demand
- cost-minimization
stage: formal-systems
status: draft
---

# Conditional Factor Demand

## Core Idea
Conditional (or derived) factor demand x(w, y) gives the quantity of input used when minimizing costs for output level y at input prices w. By Shephard's lemma, ∂c(w,y)/∂w_i = x_i(w,y). These demands depend on output level, unlike Marshallian input demand which conditions on revenue. Conditional demands are crucial for understanding production and technological change.

## Explainer

From cost function duality, you know that the cost function c(w, y) encodes everything about a firm's technology and input choices. **Conditional factor demand** is the bridge between that cost function and the actual quantities of inputs (labor, capital, materials) a firm uses. The word "conditional" means we are asking: given that the firm wants to produce exactly y units of output, how much of each input should it use to minimize cost?

Think of a bakery that needs to produce 1,000 loaves of bread per day. It can use more labor with less capital (hand-kneading) or more capital with less labor (automated mixers). The conditional factor demands x(w, y) tell you exactly how many worker-hours and how many machine-hours the bakery should employ, given the wage rate, the rental rate of capital, and the target output of 1,000 loaves. If wages rise, the bakery substitutes toward capital — the conditional demand for labor falls and the conditional demand for capital rises, all while holding output fixed.

The mathematical elegance comes from **Shephard's lemma**: the conditional demand for input i is simply the partial derivative of the cost function with respect to input price w_i. This is the producer-theory analog of the relationship you saw in consumer duality, where Hicksian demand equals the derivative of the expenditure function with respect to price. The parallel is exact — cost minimization for a target output level mirrors expenditure minimization for a target utility level. Just as the expenditure function fully characterizes consumer behavior, the cost function fully characterizes the firm's input choices, and Shephard's lemma is the tool for extracting those choices.

Conditional factor demands have important properties inherited from the cost function. They are **homogeneous of degree zero** in input prices — if all prices double, the cost-minimizing input mix does not change, because relative prices are unchanged. The matrix of substitution effects (how demand for input i responds to the price of input j) is symmetric and negative semidefinite, mirroring the Slutsky matrix in consumer theory. These properties are not assumptions but consequences of optimization, which means they can be tested empirically. If estimated factor demands violate these restrictions, the data are inconsistent with cost-minimizing behavior — a powerful diagnostic for understanding firm behavior and technological structure.
