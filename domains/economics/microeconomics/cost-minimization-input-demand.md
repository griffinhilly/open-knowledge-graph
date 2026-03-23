---
id: cost-minimization-input-demand
title: Cost Minimization and Conditional Input Demand
domain: economics
course: microeconomics
prerequisites:
- id: production-technology-and-isoquants
  type: hard
- id: lagrange-multipliers
  type: soft
builds-toward:
- returns-to-scale-analysis
- long-run-cost-structure
tags:
- producer theory
- costs
- optimization
- factor demand
stage: formal-systems
status: validated
---

# Cost Minimization and Conditional Input Demand

## Core Idea
Firms minimize the cost of producing a target output by choosing input quantities where the price ratio equals the marginal rate of technical substitution (w/r = MRTS). Conditional input demands x*(w,r,y) show how many inputs to use at given prices and output. The cost function c(w,r,y) gives minimum cost for each output level; its properties (homogeneity, concavity) derive from technology.

## Questions

```yaml
- question: "A firm is currently using inputs where MP_L/MP_K = 3, the wage w = 4, and the rental rate r = 8. Is the firm minimizing cost, and if not, what should it do?"
  type: multiple-choice
  options:
    - "Yes — the firm is cost-minimizing because it is using positive quantities of both inputs"
    - "No — MRTS = 3 exceeds w/r = 0.5, so labor generates more output per dollar than capital; the firm should use more labor and less capital"
    - "No — MRTS = 3 exceeds w/r = 0.5, so capital is underused; the firm should substitute toward more capital"
    - "No — the firm should equalize MP_L and MP_K by adjusting quantities, regardless of input prices"
  answer: 1
  explanation: "At the cost-minimizing point, MRTS = w/r. Here MRTS = MP_L/MP_K = 3 and w/r = 4/8 = 0.5, so MRTS > w/r. This means MP_L/w > MP_K/r — each dollar spent on labor buys more output than each dollar spent on capital. The firm can reduce cost while maintaining output by shifting toward more labor and less capital. As labor increases and capital decreases, diminishing returns drive MRTS down toward 0.5. Option C is a common error: students see MRTS > w/r and mistakenly conclude capital is the underused input, when it's actually overused."

- question: "Shephard's lemma states that ∂c(w,r,y)/∂w = L*(w,r,y). What is the practical significance of this result?"
  type: multiple-choice
  options:
    - "It shows that cost functions are always linear in input prices, making estimation straightforward"
    - "It allows the conditional input demand functions to be recovered by differentiating the cost function, without resolving the optimization problem from scratch"
    - "It proves that a wage increase always reduces labor demand, confirming the law of factor demand"
    - "It tells us the marginal cost of producing one additional unit of output"
  answer: 1
  explanation: "Shephard's lemma is a powerful duality result: if you know the cost function c(w,r,y), you can recover how much of each input the firm uses at any prices and output level simply by differentiating. This means you can estimate conditional input demands from data on costs and prices without directly observing the optimization. Option D describes the Lagrange multiplier λ (= marginal cost), not Shephard's lemma. Option C is a consequence that can be derived from the lemma but is not what the lemma states."

- question: "At the cost-minimizing input bundle, the last dollar spent on labor and the last dollar spent on capital produce the same marginal output."
  type: true-false
  answer: true
  explanation: "The cost-minimization condition MRTS = w/r is equivalent to MP_L/w = MP_K/r. Both ratios express 'marginal product per dollar of expenditure.' At the optimum, these are equal for all inputs. If they were not equal, the firm could reduce cost by reallocating a dollar from the lower-productivity input to the higher-productivity one, producing the same output more cheaply. The tangency condition is the mathematical expression of this no-gain-from-reallocation requirement."

- question: "The conditional input demand function L*(w,r,y) tells a firm how much labor to hire to maximize profits at any given wage, holding capital fixed."
  type: true-false
  answer: false
  explanation: "Conditional input demands are derived from cost *minimization* for a given output target y, not from profit maximization. The word 'conditional' means conditional on producing output y — the firm is asking 'given that I must produce y units, what input mix minimizes cost?' Capital is not held fixed; both inputs are optimized jointly. Unconditional (profit-maximizing) input demands come from the second stage of the firm's problem, where the output level itself is chosen to maximize profit."

- question: "What does the tangency condition MRTS = w/r mean economically? Why is this the cost-minimizing point rather than just any point on the isoquant?"
  type: short-answer
  answer: "MRTS = w/r means the rate at which the firm can technically substitute one input for another (while holding output constant) equals the rate at which the market allows the firm to substitute one input for another (while holding cost constant). At any other point on the isoquant, one input delivers more output per dollar than the other — so the firm could reduce total cost by shifting spending toward the more productive input. Only at the tangency is there no profitable reallocation: every input bundle on the same isocost line that keeps output constant has already been used as efficiently as possible."
  explanation: "The intuition is an equimarginal principle: at the optimum, all marginal returns per dollar are equal. This is the producer analog of the consumer's utility-maximizing condition MRS = p_x/p_y. The isoquant-isocost tangency is where you've extracted the maximum output from a given budget — or equivalently, minimized the cost of hitting a given output. Moving along the isoquant from this point either puts you on a higher isocost line (more expensive) or keeps you on the same one (same cost) but never on a lower one."
```

## Explainer

From your study of isoquants, you know that an isoquant is a curve showing all input combinations — say, labor L and capital K — that produce the same quantity of output. The slope of an isoquant at any point is the **marginal rate of technical substitution** (MRTS), the rate at which you can substitute one input for another while holding output constant. MRTS equals the ratio of the marginal products: MRTS = MP_L / MP_K. Cost minimization is about finding the right point on an isoquant — the one that costs the least.

The cost of an input bundle (L, K) at wage w and rental rate r is simply wL + rK. If you set this equal to a fixed budget, you get an **isocost line**: L = C/w − (r/w)K. The slope of the isocost line is −r/w (or −w/r when expressed in the conventional orientation). The cost-minimizing input bundle is where an isocost line is tangent to the target isoquant. At this tangency point, the slopes are equal: MRTS = w/r. This tangency condition has an intuitive interpretation: at the optimum, the last dollar spent on labor buys as much output as the last dollar spent on capital — if it didn't, you could reallocate spending between inputs and produce the same output more cheaply.

This optimality condition defines the **conditional input demands** — the functions L*(w, r, y) and K*(w, r, y) that tell the firm how much of each input to hire to produce output y at minimum cost, given prices w and r. They are "conditional" because they depend on the output target y, not on the profit motive directly. Plugging these back into the cost expression gives the **cost function** c(w, r, y) = wL* + rK*, which summarizes everything about the firm's production technology. The cost function is homogeneous of degree one in input prices — doubling both w and r doubles costs without changing optimal input ratios — and it is concave in input prices, reflecting the firm's ability to substitute toward cheaper inputs when prices change.

If you have studied Lagrange multipliers, you can derive the same result formally: minimize wL + rK subject to the constraint f(L, K) = y. The first-order conditions yield w = λ · MP_L and r = λ · MP_K, where λ is the Lagrange multiplier (here, the **marginal cost** of output). Dividing one condition by the other gives MP_L / MP_K = w/r, confirming the tangency condition. The Lagrange multiplier λ plays a central role in producer theory: it is the shadow price of relaxing the output constraint by one unit — that is, the marginal cost of production. Shephard's lemma then tells us that the derivative of the cost function with respect to an input price equals the conditional demand for that input: ∂c/∂w = L*(w, r, y). This powerful result means you can recover input demands from the cost function without solving the optimization problem again.
