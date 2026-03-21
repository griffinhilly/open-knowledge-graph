---
id: long-run-costs-economies-of-scale
title: Long-Run Costs and Economies of Scale
domain: economics
course: microeconomics
prerequisites:
- id: short-run-costs
  type: hard
- id: production-function-microeconomics
  type: hard
builds-toward:
- profit-maximization-microeconomics
- perfect-competition
- natural-monopoly
tags:
- long-run average cost
- LRAC
- economies of scale
- minimum efficient scale
stage: formal-systems
status: validated
---

# Long-Run Costs and Economies of Scale

## Core Idea
In the long run, all inputs are variable, so firms can choose plant size to minimize cost for any output level. The long-run average cost (LRAC) curve is the envelope of all short-run ATC curves. Economies of scale exist where LRAC falls with output, diseconomies where it rises, and constant returns to scale where it is flat. The minimum efficient scale (MES) is the lowest output at which LRAC reaches its minimum. Industries with large economies of scale relative to market demand tend toward natural monopoly.

## How It's Best Learned
Derive the LRAC envelope graphically by drawing multiple SRATC curves for different plant sizes and tracing the outer lower boundary. Then connect MES to industry structure (competitive vs. oligopolistic vs. natural monopoly).

## Common Misconceptions
- Economies of scale are a long-run concept (all inputs variable); students confuse them with diminishing returns, which is a short-run concept.
- The LRAC is not simply the lowest SRATC curve; it is the envelope, which can lie below every individual SRATC curve except at the tangency points.

## Questions

```yaml
- question: "A firm can choose among several possible plant sizes, each with its own U-shaped short-run average total cost (SRATC) curve. The long-run average cost (LRAC) at any output level represents:"
  type: multiple-choice
  options:
    - "The arithmetic average of all SRATC curves at that output level"
    - "The minimum cost achievable at that output level by selecting the optimal plant size"
    - "The single lowest SRATC curve, since the firm would always build the cheapest plant"
    - "The SRATC curve for the plant size designed to produce exactly that output most efficiently"
  answer: 1
  explanation: "The LRAC is the envelope of all SRATC curves — the minimum cost achievable at each output level across all possible plant sizes. At any given output, the firm selects the plant size that minimizes average cost, and the LRAC records that minimum. Option C is the classic misconception: the LRAC lies below every individual SRATC at most outputs, not equal to any single one of them. Each SRATC is cheapest only near its designed capacity; for other output levels, a different plant size would be cheaper. The envelope captures this by selecting the optimal plant separately at each output level."

- question: "An industry's minimum efficient scale (MES) equals approximately 70% of total market demand. What market structure is this industry most likely to exhibit?"
  type: multiple-choice
  options:
    - "Perfect competition with many small firms each well below MES"
    - "Natural monopoly or tight duopoly, since only one or two firms can operate at minimum cost"
    - "Monopolistic competition, since high MES encourages product differentiation"
    - "The market structure depends entirely on demand elasticity, not on MES relative to demand"
  answer: 1
  explanation: "When MES is large relative to market demand, only one or two firms can simultaneously operate at minimum efficient scale. A second entrant would face much higher average costs than the incumbent, creating an insurmountable cost disadvantage. This is the defining condition for natural monopoly: economies of scale are so large that the market can only support one firm efficiently. Water utilities, power transmission networks, and railroad infrastructure are classic examples. When MES is small relative to demand, many firms can each reach minimum cost, enabling competitive market structure."

- question: "The long-run average cost curve is the envelope of all short-run average total cost curves, meaning it can lie below every individual SRATC curve at most output levels."
  type: true-false
  answer: true
  explanation: "This is precisely the definition of an envelope curve. The LRAC records the minimum of all SRATC values achievable by choosing the optimal plant size at each output level. Since each SRATC curve is only at its own minimum near its designed capacity, the LRAC lies below (or touches) each SRATC for most output levels — it is never above any SRATC and touches a particular SRATC only at one tangency point. Students often assume the LRAC simply is the lowest SRATC, but it is a new curve constructed by optimizing plant choice separately at every output."

- question: "Diminishing marginal returns and diseconomies of scale are essentially the same economic concept — both describe rising costs as output increases."
  type: true-false
  answer: false
  explanation: "These are distinct concepts applying to different time horizons. Diminishing marginal returns is short-run: with at least one fixed input (typically capital), adding more of the variable input (labor) eventually yields smaller output increments, raising marginal and average variable costs. Diseconomies of scale is long-run: when all inputs are variable and the firm expands every input proportionally, average costs eventually rise due to coordination failures and bureaucratic inefficiency at very large scale. Confusing the two leads to incorrect analysis — a firm can exhibit diminishing returns in the short run while still enjoying economies of scale at larger plant sizes in the long run."

- question: "Explain the difference between the short-run concept of diminishing marginal returns and the long-run concept of diseconomies of scale, including what defines each time horizon."
  type: short-answer
  answer: "The short run is defined as the period when at least one input is fixed (typically capital). Diminishing marginal returns occurs because adding more of a variable input (labor) to a fixed capital stock eventually yields smaller output increments, driving up marginal cost. The long run is defined as the period when all inputs are variable — the firm can choose its plant size freely. Diseconomies of scale occur when expanding all inputs proportionally leads to rising average costs, typically due to coordination costs and management inefficiencies at very large scale. The key distinction: diminishing returns results from a fixed-input constraint; diseconomies of scale result from organizational problems that arise even when all inputs can be freely adjusted."
  explanation: "This distinction matters practically. A firm experiencing diminishing returns in the short run might solve the problem by expanding its plant in the long run — getting onto a lower SRATC curve. But if the long-run LRAC is also rising at that scale, expanding the plant won't help. Understanding which time horizon applies is essential for diagnosing whether rising costs are a short-run capacity constraint (solvable by investing in more capital) or a long-run structural problem (requiring a fundamentally different scale or organizational approach)."
```

## Explainer

In the short run — which you've already studied — at least one input is fixed. A firm with a given factory is stuck with that capital stock regardless of output. It can hire more workers, but it can't instantly resize the plant. That fixed input creates the U-shaped short-run average total cost (SRATC) curve: output is cheap near the plant's designed capacity and expensive at the extremes. Different plant sizes produce different SRATC curves, each U-shaped and shifted relative to the others.

In the **long run**, all inputs are variable. The firm can choose its plant size optimally for any output level it wants to produce. This freedom to optimize plant scale is what generates the **long-run average cost (LRAC)** curve. Imagine drawing five SRATC curves, one for each possible plant size. The LRAC curve is the **envelope** of these curves — the outer lower boundary tracing the minimum cost achievable for each output level across all possible plant configurations. At any given output, the firm picks the plant size that minimizes average cost, and the LRAC records that minimum. The envelope lies on or below every individual SRATC curve, touching each at exactly one point (the tangency).

**Economies of scale** describe the slope of the LRAC. When LRAC falls as output rises, production exhibits economies of scale — doubling output costs less than double to produce. This happens because of indivisibilities (a single manager can oversee ten workers or fifty), specialization (larger plants can use specialized equipment and labor), and purchasing power. When LRAC rises with output, production exhibits **diseconomies of scale** — coordination costs, communication failures, and bureaucratic inefficiency raise average costs at very large scales. The **minimum efficient scale (MES)** is the lowest output at which LRAC reaches its minimum — the smallest plant that achieves the full economies of scale available in that technology.

MES connects costs to market structure. If MES is small relative to market demand, many firms can coexist at minimum cost, and the industry is likely competitive. If MES is large relative to market demand — meaning one or two firms at MES can serve the whole market — the industry tends toward natural monopoly. A water utility with enormous fixed infrastructure costs and low marginal delivery costs has an LRAC that falls continuously over the relevant range of output. A second firm duplicating that infrastructure would have much higher average costs than the incumbent. This is why natural monopolies exist and why their regulation requires distinct policy tools. Understanding economies of scale thus bridges microeconomic cost theory to the structure of entire industries.


