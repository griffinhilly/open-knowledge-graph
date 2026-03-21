---
id: long-run-cost-structure
title: Long-Run Cost Curves and Scale Economies
domain: economics
course: microeconomics
prerequisites:
- id: cost-minimization-input-demand
  type: hard
- id: returns-to-scale-analysis
  type: hard
builds-toward:
- competitive-industry-long-run
tags:
- producer theory
- costs
- economies of scale
stage: formal-systems
status: draft
---

# Long-Run Cost Curves and Scale Economies

## Core Idea
Long-run average cost (LAC) reflects the firm's flexibility to adjust all inputs. LAC curves downward when increasing returns (economies of scale) allow spreading fixed costs, flat under constant returns, and upward with decreasing returns (diseconomies of scale). The envelope of short-run average cost curves forms the LAC. The minimum efficient scale is the smallest output at minimum LAC.

## Questions

```yaml
- question: "A manufacturing firm is producing 1,000 units per month. Its long-run average cost curve is steeply downward-sloping at this output level. What does this imply about the firm's technology?"
  type: multiple-choice
  options:
    - "The firm is experiencing diseconomies of scale and should reduce output"
    - "The firm has constant returns to scale — doubling inputs doubles output"
    - "The firm has increasing returns to scale — expanding production would lower per-unit costs"
    - "The firm has reached minimum efficient scale and further expansion raises average cost"
  answer: 2
  explanation: "A downward-sloping LAC means average cost falls as output increases — this is the definition of economies of scale, arising from increasing returns to scale. The firm produces each unit more cheaply by expanding. Diseconomies of scale (A) would cause an upward-sloping LAC. Constant returns to scale (B) produce a flat LAC. Minimum efficient scale (D) is the output where LAC reaches its minimum and stops declining — not where it is still steeply falling."

- question: "Which statement correctly describes the relationship between short-run average cost (SAC) curves and the long-run average cost (LAC) curve?"
  type: multiple-choice
  options:
    - "The LAC is the arithmetic average of all SAC curves at each output level"
    - "Each SAC curve lies on or above the LAC, touching it at exactly one point"
    - "The LAC coincides with the lowest SAC curve across all output levels"
    - "SAC curves shift downward to become the LAC when fixed costs become variable"
  answer: 1
  explanation: "The LAC is the lower envelope of all SAC curves. Because the long run offers full input flexibility — by definition the cost-minimizing option at every output — no SAC curve can lie below it. Each SAC curve corresponds to one specific capital stock; it is tangent to the LAC at the single output level for which that capital stock is optimal. At all other outputs, the fixed capital is suboptimal, making the SAC lie above the LAC. The LAC is not an average of SACs (A), nor does it coincide with any single SAC (C)."

- question: "The minimum efficient scale (MES) is the smallest output level at which a firm reaches its lowest long-run average cost."
  type: true-false
  answer: true
  explanation: "This is the precise definition of MES. It is the output where the LAC curve reaches its minimum and economies of scale are fully exhausted. Below MES, the firm has not captured all available economies of scale and produces at above-minimum average cost. MES also has industry-structure implications: if MES is large relative to total market demand, only a few firms can operate at minimum cost before the market is saturated, predicting concentration."

- question: "A firm can produce at a point below its long-run average cost curve by optimally adjusting all its inputs."
  type: true-false
  answer: false
  explanation: "This is impossible by construction. The LAC represents the minimum achievable average cost at each output level when all inputs are optimally chosen — it is the lower boundary of feasible average costs. No combination of input choices can yield lower cost than the LAC for any given output; that is what cost minimization means. Points below the LAC are not attainable. Points above it represent suboptimal input choices, as occurs in the short run when some inputs are fixed at non-optimal levels."

- question: "Explain why each short-run average cost curve is tangent to the long-run average cost curve at exactly one point."
  type: short-answer
  answer: "Each SAC curve is constructed for a specific capital stock K₀. At exactly one output level q₀, the capital K₀ is precisely optimal — the cost-minimizing amount for producing q₀. At that point, the firm is at its long-run optimum given this capital, so the SAC and LAC agree and are tangent. At any other output level, K₀ is either too much or too little capital, making production more expensive than it would be with flexibly chosen capital — so the SAC lies strictly above the LAC. The LAC stitches together one optimal point from each possible SAC into a smooth envelope."
  explanation: "This envelope relationship is not a coincidence — it is the mathematical definition of the LAC. Every point on the LAC is a tangency with some SAC, each representing the long-run optimum for a different capital level and its associated output quantity."
```

## Explainer

In the short run, some inputs are fixed — you cannot immediately expand factory floor space or install new capital equipment. From your study of cost minimization with fixed capital, you know this creates a U-shaped short-run average cost curve: at low output, fixed costs are spread over few units; at high output, diminishing marginal returns to variable inputs drive costs up. The long run changes everything: all inputs become variable, and the firm chooses the optimal scale for any output target.

Think of the **long-run average cost (LAC) curve** as the lower envelope of all the short-run average cost (SAC) curves, one for each possible capital level. For any given output quantity, the firm selects the capital stock that minimizes total cost for that quantity. Plotting those minimum cost points across all output levels traces out the LAC. No short-run curve can lie below the LAC — by definition, the long run offers maximum flexibility and therefore minimum cost at every output level. Each SAC curve is tangent to the LAC at exactly one point: the output level for which that capital stock is optimal.

The shape of the LAC reflects the technology's **returns to scale** you analyzed previously. When increasing all inputs by λ percent raises output by more than λ percent (increasing returns), the LAC slopes downward: **economies of scale** allow larger firms to produce each unit more cheaply. Classic sources include indivisibilities (a single large blast furnace is more efficient per ton than two small ones), specialization of labor and capital, and spreading fixed setup costs over larger runs. When inputs and output scale proportionally (constant returns), the LAC is flat. When scaling up becomes increasingly costly due to coordination problems or managerial diseconomies (decreasing returns), the LAC turns upward.

The **minimum efficient scale (MES)** is the smallest output level at which the firm reaches minimum LAC. It is an industry-structure concept as much as a firm concept. If MES is large relative to total market demand, only a few firms can operate at minimum cost before the market is saturated — a natural tendency toward concentration. If MES is small relative to demand, many firms can coexist efficiently, supporting a competitive structure. This is why the LAC shape matters beyond individual cost accounting: it tells you how many firms can efficiently serve a market, and therefore what market structure to expect.
