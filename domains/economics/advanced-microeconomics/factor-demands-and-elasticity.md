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
stage: expert
status: draft
---

# Factor Demands and Substitution Elasticity

## Core Idea
Factor demands show how optimal input quantities respond to factor prices and output levels. The Allen partial elasticity of substitution measures the percentage change in factor ratio from a one percent increase in relative factor prices. Higher substitution elasticity implies greater flexibility in adjusting input mix when relative prices change.

## Questions

```yaml
- question: "A government raises the minimum wage by 20%. A manufacturing firm uses labor and automated machinery as inputs. If the elasticity of substitution between labor and capital is high (σ ≈ 2), what is the most likely outcome?"
  type: multiple-choice
  options:
    - "Employment falls sharply as the firm substitutes toward capital, since high σ means inputs are easily swapped"
    - "Employment is largely unchanged because high σ means the firm is already using the optimal mix"
    - "Employment rises as higher wages attract more productive workers, increasing output"
    - "Employment falls slightly because high σ means the firm is locked into its current input mix"
  answer: 0
  explanation: "High substitution elasticity means the firm can readily swap between inputs when relative prices change. When wages rise, the price of labor increases relative to capital, so a firm with high σ responds by substituting toward capital — automating tasks, reducing headcount. The higher σ is, the more dramatic this shift. The common misconception is option D, which gets the direction backwards: high σ implies flexibility and large substitution responses, not rigidity."

- question: "A Leontief production function describes inputs that must be used in strictly fixed proportions (like a pilot and a plane). What is the elasticity of substitution for this technology?"
  type: multiple-choice
  options:
    - "σ = 1, because cost-minimizing firms always adjust input ratios proportionally to price ratios"
    - "σ = ∞, because the firm can always hire more pilots without needing more planes"
    - "σ = 0, because no matter how wages or rental costs change, the firm cannot alter its capital-labor ratio"
    - "σ > 1, because complementary inputs are more substitutable than independent inputs"
  answer: 2
  explanation: "The Leontief technology requires inputs in a fixed ratio — adding more of one input without the other yields no additional output. Therefore, even if wages rise dramatically, the firm cannot substitute capital for labor; it must continue using inputs in the same proportions. This corresponds to σ = 0. The Cobb-Douglas function, by contrast, has σ = 1 (constant unit elasticity of substitution), and the CES production function generalizes to any σ ≥ 0."

- question: "A Cobb-Douglas production function always has an elasticity of substitution equal to one, meaning a 10% increase in the wage-rental ratio causes exactly a 10% increase in the capital-labor ratio."
  type: true-false
  answer: true
  explanation: "This is the defining property of the Cobb-Douglas technology. The cost shares of labor and capital are constant (equal to the output elasticities α and 1−α), and the capital-labor ratio responds proportionally to changes in relative factor prices. This makes Cobb-Douglas a useful benchmark: σ = 1 everywhere, regardless of the level of output or input prices."

- question: "If the elasticity of substitution between labor and capital is near zero, a large increase in the minimum wage will cause a large reduction in employment."
  type: true-false
  answer: false
  explanation: "Near-zero substitution elasticity means the firm has almost no ability to swap between inputs — it must use them in nearly fixed proportions. When wages rise, a firm with σ ≈ 0 cannot easily replace workers with machines, so the employment effect is small. Large employment effects from wage increases require high substitution elasticity (σ >> 0), where firms can readily automate. This is why empirical estimates of σ are central to predicting minimum wage employment impacts."

- question: "A tax is imposed on capital income. Using the concept of substitution elasticity, explain how the ability to substitute between capital and labor determines who ultimately bears the burden of this tax."
  type: short-answer
  answer: "If substitution elasticity is high, capital can effectively 'flee' the tax by shifting production toward labor-intensive methods. As capital becomes more expensive, firms substitute toward labor, reducing demand for capital and shifting the burden partly onto labor (via lower wages) and onto consumers. With high σ, capital bears less of the tax because it can escape via substitution. With low σ, capital cannot substitute away, so it bears more of the burden. In the extreme Leontief case (σ = 0), capital and labor are used in fixed proportions, so the tax burden stays on capital with minimal shifting."
  explanation: "The incidence of any factor tax depends on how mobile and substitutable the taxed factor is. High substitution elasticity gives capital 'mobility' across production methods — even without moving geographically, firms reduce their capital intensity in response to higher capital costs. This reduces the effective tax burden on capital and spreads it to other factors. Low elasticity traps capital in its current use and forces it to absorb the full tax."
```

## Explainer

From cost minimization and duality, you know that a profit-maximizing firm chooses its input mix to minimize the cost of producing any given output level, and that this problem has a dual relationship with the production function. From your study of production functions, you know how inputs combine to produce output. **Factor demand functions** are the solution to the cost-minimization problem — they tell you the optimal quantity of each input (labor, capital, materials) as a function of input prices and the desired output level.

Consider a firm using two inputs, labor (L) and capital (K), with prices w and r. The cost-minimization condition requires that the ratio of marginal products equals the ratio of input prices: MP_L / MP_K = w / r. This tangency condition, combined with the output constraint, yields the **conditional factor demand functions** L*(w, r, q) and K*(w, r, q). These functions have intuitive properties: factor demand is decreasing in its own price (if wages rise, the firm uses less labor), increasing in the price of substitutes (if capital becomes expensive, the firm shifts toward labor), and generally increasing in output.

The **elasticity of substitution** quantifies how easily the firm can swap between inputs when relative prices change. Formally, it measures the percentage change in the capital-labor ratio (K/L) in response to a one percent change in the relative price of labor to capital (w/r). If σ is high, the firm can readily shift between inputs — think of a factory that can automate tasks when wages rise. If σ is near zero, inputs must be used in nearly fixed proportions — like a pilot and a plane, where adding pilots without planes does not help. The Cobb-Douglas production function has σ = 1 everywhere; the Leontief (fixed-proportions) has σ = 0; the CES (constant elasticity of substitution) production function lets σ take any positive value, making it a flexible workhorse for empirical work.

The elasticity of substitution matters enormously for policy. When governments raise the minimum wage, the employment effect depends critically on how substitutable labor is for capital and other inputs. If σ is high, firms can easily automate, and employment falls significantly. If σ is low, firms have little choice but to continue using labor, and the employment effect is small. Similarly, the incidence of a tax on capital income depends on how easily firms can shift toward labor — high substitution elasticity means capital bears less of the tax burden because it can "flee" to labor-intensive production methods. The factor demand framework turns these qualitative intuitions into precise, quantifiable predictions that can be estimated from data on input usage and prices.

When there are more than two inputs, the **Allen partial elasticity of substitution** generalizes the concept by measuring pairwise substitutability while holding other input quantities at their optimal levels. Two inputs are **substitutes** if raising the price of one increases demand for the other (σ > 0) and **complements** if it decreases demand (σ < 0). For example, skilled labor and computers might be complements (firms that invest in technology also hire more skilled workers), while unskilled labor and machines might be substitutes. These cross-elasticities, derived from the firm's cost function via Shephard's lemma, are the empirical backbone of labor economics and public finance.
