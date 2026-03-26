---
id: cost-minimization-and-factor-demand
title: Cost Minimization and Conditional Factor Demand
domain: economics
course: advanced-microeconomics
prerequisites:
- id: production-function-microeconomics
  type: hard
- id: long-run-costs-economies-of-scale
  type: soft
- id: lagrange-multipliers
  type: hard
- id: partial-derivatives
  type: soft
builds-toward:
- dual-production-and-profit-functions
tags:
- producer-theory
- costs
- optimization
stage: expert
status: validated
---

# Cost Minimization and Conditional Factor Demand

## Core Idea
Firms minimize cost for any target output by equating the marginal rate of technical substitution to the input price ratio. Conditional factor demands depend on output and input prices and are derived from the cost function using Shephard's lemma: ∂C/∂w_i = conditional demand for input i. This mirrors the consumer duality problem and is essential for understanding production technology.

## Questions

```yaml
- question: "A firm currently uses inputs such that the MRTS (the rate at which it can substitute input 2 for input 1 while maintaining output) equals 3, but the price ratio w₁/w₂ = 2. What should the firm do to minimize costs for its current output level?"
  type: multiple-choice
  options:
    - "Increase use of both inputs to produce more output at lower average cost"
    - "Use more of input 1 and less of input 2 — the firm is getting more output per dollar from input 1"
    - "Use more of input 2 and less of input 1 — the MRTS exceeds the price ratio, so substituting toward input 2 reduces cost while maintaining output"
    - "The firm is already at the cost minimum because any MRTS with positive inputs satisfies optimality"
  answer: 2
  explanation: "MRTS = 3 means the firm could give up 3 units of input 2 in exchange for 1 unit of input 1 and maintain output. But the price ratio w₁/w₂ = 2 means buying 1 unit of input 1 costs twice what 1 unit of input 2 costs. So by substituting: save 3 units of input 2 (saving 3w₂) and buy 1 unit of input 1 (spending w₁ = 2w₂) — net saving = w₂ per substitution. The firm should keep substituting toward input 2 until MRTS falls to equal the price ratio. The cost minimum requires MRTS = w₁/w₂."

- question: "Shephard's lemma states that the conditional demand for input i can be obtained by:"
  type: multiple-choice
  options:
    - "Setting the marginal product of input i equal to its price"
    - "Differentiating the cost function with respect to the price of input i"
    - "Differentiating the production function with respect to input i and dividing by output"
    - "Solving the cost-minimization Lagrangian specifically for x_i while holding all other inputs fixed"
  answer: 1
  explanation: "Shephard's lemma says ∂C/∂w_i = x_i*, the conditional demand for input i. This is an application of the envelope theorem: the partial derivative of the minimized cost function with respect to an input price directly recovers the optimal quantity of that input. Its power is that once you have the cost function, you can derive all conditional factor demands by differentiation without re-solving the optimization. This mirrors the consumer side, where differentiating the expenditure function with respect to a good's price yields the Hicksian (compensated) demand."

- question: "The cost-minimizing input combination occurs where the isoquant is tangent to the isocost line — that is, where the marginal rate of technical substitution equals the input price ratio."
  type: true-false
  answer: true
  explanation: "This tangency condition is the geometric statement of the optimality condition MRTS = w₁/w₂. At the tangency point, the rate at which the production technology allows substitution between inputs (MRTS) exactly equals the rate at which the market allows substitution between inputs (price ratio). If they differ, the firm can maintain output while spending less by substituting toward the relatively cheaper input. The tangency is the unique point where no further cost-saving substitution is possible."

- question: "To minimize production costs, a firm should typically allocate more resources to the input with the highest marginal product, since that input generates the most output per unit used."
  type: true-false
  answer: false
  explanation: "Cost minimization depends on marginal product relative to input price, not marginal product alone. The correct condition is MP₁/w₁ = MP₂/w₂ (equivalently, MRTS = w₁/w₂): the marginal product per dollar must be equal across all inputs. If input 1 has a very high marginal product but also a very high price, it may be less cost-effective than input 2. A firm that ignored prices and simply hired more of the highest-MP input could easily be spending more than necessary to achieve its output target."

- question: "What are 'conditional' factor demands, and why are they described as conditional rather than unconditional?"
  type: short-answer
  answer: "Conditional factor demands x_i*(w₁, w₂, q) give the cost-minimizing quantity of each input as a function of input prices and a fixed output target q. They are 'conditional' because the target output level q is held fixed — the firm is asking 'given that I must produce exactly q units, how much of each input minimizes my cost?' This contrasts with unconditional factor demands, which emerge from profit maximization where the firm chooses both inputs and output simultaneously. Conditional factor demands depend on output and input prices; their relationship to output level encodes how the firm's input mix changes as scale changes, which is essential for understanding returns to scale and the structure of the cost function."
  explanation: "The distinction matters because the two types of factor demand answer different questions. Conditional demands answer 'cheapest way to produce a given output?' — relevant for understanding production efficiency. Unconditional demands answer 'what inputs maximize profit?' — relevant for understanding market behavior. Shephard's lemma operates on the conditional cost function to yield conditional demands."
```

## Explainer

You already know from production theory that a firm transforms inputs into output according to a production function f(x₁, x₂). From your work with Lagrange multipliers, you know how to optimize a function subject to a constraint. Cost minimization brings these together: given input prices w₁ and w₂ and a target output level q, the firm chooses input quantities to minimize total cost w₁x₁ + w₂x₂ subject to f(x₁, x₂) = q. This is the producer's analog of the consumer's expenditure minimization problem.

The optimality condition has an intuitive interpretation. Setting up the Lagrangian and taking first-order conditions yields the rule that the **marginal rate of technical substitution** (MRTS) — the rate at which the firm can substitute one input for another while maintaining output — must equal the input price ratio w₁/w₂. Graphically, this is the point where an **isoquant** (constant-output curve) is tangent to an **isocost line** (constant-cost line). If the MRTS exceeds the price ratio, the firm is using too much of input 2 relative to input 1: it could maintain the same output at lower cost by substituting toward the cheaper input. The tangency condition ensures no further cost-saving substitution is possible.

Solving the cost minimization problem for all output levels produces two key objects. The **conditional factor demands** x_i*(w₁, w₂, q) tell you how much of each input the firm uses as a function of input prices and target output — they are "conditional" because output is held fixed rather than being chosen optimally. The **cost function** C(w₁, w₂, q) = w₁x₁* + w₂x₂* gives the minimized cost as a function of prices and output. This cost function encodes everything about the firm's technology in a compact, tractable form.

The connection between the cost function and factor demands is captured by **Shephard's lemma**: ∂C/∂w_i = x_i*. Differentiating the cost function with respect to an input price directly recovers the conditional demand for that input. This result, which parallels the envelope theorem from your optimization background, is powerful because it means you can derive factor demands from the cost function without re-solving the optimization problem. The entire framework mirrors consumer duality — expenditure function maps to cost function, Hicksian demands map to conditional factor demands, and Shephard's lemma works identically on both sides. Recognizing this parallel deepens your understanding of both producer and consumer theory.
