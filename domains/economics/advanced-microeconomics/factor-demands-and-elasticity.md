---
id: factor-demands-and-elasticity
title: Factor Demands and Substitution Elasticity
domain: economics
course: advanced-microeconomics
prerequisites:
- id: cost-minimization-duality
  type: hard
- id: production-function-microeconomics
  type: hard
tags:
- producer-theory
- factor-markets
- elasticity
stage: advanced
status: draft
---

# Factor Demands and Substitution Elasticity

## Core Idea
Factor demands show how optimal input quantities respond to factor prices and output levels. The Allen partial elasticity of substitution measures the percentage change in factor ratio from a one percent increase in relative factor prices. Higher substitution elasticity implies greater flexibility in adjusting input mix when relative prices change.

## Explainer

From cost minimization and duality, you know that a profit-maximizing firm chooses its input mix to minimize the cost of producing any given output level, and that this problem has a dual relationship with the production function. From your study of production functions, you know how inputs combine to produce output. **Factor demand functions** are the solution to the cost-minimization problem — they tell you the optimal quantity of each input (labor, capital, materials) as a function of input prices and the desired output level.

Consider a firm using two inputs, labor (L) and capital (K), with prices w and r. The cost-minimization condition requires that the ratio of marginal products equals the ratio of input prices: MP_L / MP_K = w / r. This tangency condition, combined with the output constraint, yields the **conditional factor demand functions** L*(w, r, q) and K*(w, r, q). These functions have intuitive properties: factor demand is decreasing in its own price (if wages rise, the firm uses less labor), increasing in the price of substitutes (if capital becomes expensive, the firm shifts toward labor), and generally increasing in output.

The **elasticity of substitution** quantifies how easily the firm can swap between inputs when relative prices change. Formally, it measures the percentage change in the capital-labor ratio (K/L) in response to a one percent change in the relative price of labor to capital (w/r). If σ is high, the firm can readily shift between inputs — think of a factory that can automate tasks when wages rise. If σ is near zero, inputs must be used in nearly fixed proportions — like a pilot and a plane, where adding pilots without planes does not help. The Cobb-Douglas production function has σ = 1 everywhere; the Leontief (fixed-proportions) has σ = 0; the CES (constant elasticity of substitution) production function lets σ take any positive value, making it a flexible workhorse for empirical work.

The elasticity of substitution matters enormously for policy. When governments raise the minimum wage, the employment effect depends critically on how substitutable labor is for capital and other inputs. If σ is high, firms can easily automate, and employment falls significantly. If σ is low, firms have little choice but to continue using labor, and the employment effect is small. Similarly, the incidence of a tax on capital income depends on how easily firms can shift toward labor — high substitution elasticity means capital bears less of the tax burden because it can "flee" to labor-intensive production methods. The factor demand framework turns these qualitative intuitions into precise, quantifiable predictions that can be estimated from data on input usage and prices.

When there are more than two inputs, the **Allen partial elasticity of substitution** generalizes the concept by measuring pairwise substitutability while holding other input quantities at their optimal levels. Two inputs are **substitutes** if raising the price of one increases demand for the other (σ > 0) and **complements** if it decreases demand (σ < 0). For example, skilled labor and computers might be complements (firms that invest in technology also hire more skilled workers), while unskilled labor and machines might be substitutes. These cross-elasticities, derived from the firm's cost function via Shephard's lemma, are the empirical backbone of labor economics and public finance.
