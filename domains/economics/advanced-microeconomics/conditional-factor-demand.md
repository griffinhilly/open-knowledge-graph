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
status: validated
---

# Conditional Factor Demand

## Core Idea
Conditional (or derived) factor demand x(w, y) gives the quantity of input used when minimizing costs for output level y at input prices w. By Shephard's lemma, ∂c(w,y)/∂w_i = x_i(w,y). These demands depend on output level, unlike Marshallian input demand which conditions on revenue. Conditional demands are crucial for understanding production and technological change.

## Questions

```yaml
- question: "A firm minimizes costs to produce exactly 500 units. If the wage rate rises while capital rental costs stay constant, what happens to the conditional demand for labor?"
  type: multiple-choice
  options:
    - "Labor demand increases because the firm must compensate for the higher cost by working inputs harder"
    - "Labor demand is unchanged because conditional demand depends only on output level, not input prices"
    - "Labor demand decreases as the firm substitutes toward relatively cheaper capital, holding output fixed"
    - "Labor demand decreases and output falls, as the firm can no longer afford to produce 500 units"
  answer: 2
  explanation: "Conditional factor demand holds output fixed (at 500 units here) and minimizes cost. When wages rise, capital becomes relatively cheaper, so the cost-minimizing input mix shifts toward capital and away from labor — substitution along an isoquant. Output does NOT change (that is the 'conditional' part). Option D confuses conditional factor demand (output fixed) with unconditional Marshallian demand (where output adjusts to maximize profit)."

- question: "Shephard's lemma states that the conditional demand for input i can be derived directly from the cost function. How?"
  type: multiple-choice
  options:
    - "It is the partial derivative of the cost function with respect to output y"
    - "It is the partial derivative of the cost function with respect to the input price w_i"
    - "It is the ratio of the cost function to the number of inputs"
    - "It is found by inverting the production function at the optimal input bundle"
  answer: 1
  explanation: "Shephard's lemma: x_i(w, y) = dc(w, y)/dw_i. This is the producer-theory analog of the Hicksian demand result in consumer theory (where compensated demand equals the derivative of the expenditure function with respect to price). The elegance is that once you have the cost function, all factor demands follow from differentiation — no need to re-solve the minimization problem for each input."

- question: "Conditional factor demand is homogeneous of degree zero in input prices — if all input prices double, the cost-minimizing input quantities do not change."
  type: true-false
  answer: true
  explanation: "When all input prices scale by the same factor, relative prices are unchanged, so the cost-minimizing input bundle (the tangency between the isocost line and the isoquant) is unchanged. Only the total cost doubles. This homogeneity property is a consequence of cost minimization, not an assumption — and it can be tested empirically to check whether firms behave as cost minimizers."

- question: "Conditional factor demand and Marshallian (unconditional) input demand answer the same question from different angles, so they usually give the same input quantities at the optimum."
  type: true-false
  answer: false
  explanation: "They answer different questions. Conditional factor demand asks: given that output is fixed at y, what inputs minimize cost? Marshallian input demand asks: given input and output prices, what inputs maximize profit, allowing output to adjust? They coincide only at the profit-maximizing output level. For any other output level, conditional demands reflect the cost-minimizing mix for that target while Marshallian demands reflect the full output-and-input optimization."

- question: "Why does the matrix of own- and cross-price substitution effects for conditional factor demands have to be symmetric and negative semidefinite? What guarantees these properties?"
  type: short-answer
  answer: "These properties are consequences of the cost function being concave in input prices, which results from cost minimization. Symmetry — the effect of w_j on x_i equals the effect of w_i on x_j — follows from Young's theorem applied to the cost function (mixed partial derivatives are equal). Negative semidefiniteness means own-price effects are non-positive: a higher price for an input can only reduce or maintain its conditional demand, never increase it at fixed output. These are mathematical implications of optimization, not behavioral assumptions, making them testable predictions about firm behavior."
  explanation: "The parallel to consumer theory is exact: the Slutsky matrix of compensated demand derivatives is also symmetric and negative semidefinite for the same reason (expenditure function concavity). Both results say that optimization imposes structure on how demands respond to prices."
```

## Explainer

From cost function duality, you know that the cost function c(w, y) encodes everything about a firm's technology and input choices. **Conditional factor demand** is the bridge between that cost function and the actual quantities of inputs (labor, capital, materials) a firm uses. The word "conditional" means we are asking: given that the firm wants to produce exactly y units of output, how much of each input should it use to minimize cost?

Think of a bakery that needs to produce 1,000 loaves of bread per day. It can use more labor with less capital (hand-kneading) or more capital with less labor (automated mixers). The conditional factor demands x(w, y) tell you exactly how many worker-hours and how many machine-hours the bakery should employ, given the wage rate, the rental rate of capital, and the target output of 1,000 loaves. If wages rise, the bakery substitutes toward capital — the conditional demand for labor falls and the conditional demand for capital rises, all while holding output fixed.

The mathematical elegance comes from **Shephard's lemma**: the conditional demand for input i is simply the partial derivative of the cost function with respect to input price w_i. This is the producer-theory analog of the relationship you saw in consumer duality, where Hicksian demand equals the derivative of the expenditure function with respect to price. The parallel is exact — cost minimization for a target output level mirrors expenditure minimization for a target utility level. Just as the expenditure function fully characterizes consumer behavior, the cost function fully characterizes the firm's input choices, and Shephard's lemma is the tool for extracting those choices.

Conditional factor demands have important properties inherited from the cost function. They are **homogeneous of degree zero** in input prices — if all prices double, the cost-minimizing input mix does not change, because relative prices are unchanged. The matrix of substitution effects (how demand for input i responds to the price of input j) is symmetric and negative semidefinite, mirroring the Slutsky matrix in consumer theory. These properties are not assumptions but consequences of optimization, which means they can be tested empirically. If estimated factor demands violate these restrictions, the data are inconsistent with cost-minimizing behavior — a powerful diagnostic for understanding firm behavior and technological structure.
