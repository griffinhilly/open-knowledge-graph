---
id: short-run-cost-fixed-variable
title: 'Short-Run Cost Structure: Fixed and Variable Costs'
domain: economics
course: microeconomics
prerequisites:
- id: factor-demand-input-cost
  type: hard
builds-toward:
- long-run-average-cost
- profit-maximization-output-level
tags:
- costs
- fixed-costs
- variable-costs
- short-run
- cost-structure
stage: formal-systems
status: validated
---

# Short-Run Cost Structure: Fixed and Variable Costs

## Core Idea
In the short run, some inputs (e.g., factory buildings) are fixed, while others (e.g., labor and raw materials) are variable. Total cost (TC) equals fixed costs (FC) plus variable costs (VC). Average total cost (ATC = TC/Q), average fixed cost (AFC = FC/Q), and average variable cost (AVC = VC/Q) all vary with output. Marginal cost (MC = ΔTC/ΔQ) is the cost of producing one more unit. The firm cannot avoid fixed costs even if it produces nothing in the short run.

## How It's Best Learned
Work with numerical examples calculating FC, VC, TC, AFC, AVC, ATC, and MC for different output levels. Graph the cost curves and observe their shapes and relationships.

## Common Misconceptions
- Confusing average cost with marginal cost—they are equal only at the minimum of average cost.
- Thinking fixed costs are irrelevant to production decisions—they're sunk in the short run but influence entry/exit decisions and the shutdown point.

## Questions

```yaml
- question: "A firm has fixed costs of $600 and produces 100 units with total variable costs of $400. It then produces one more unit (101st), bringing total variable costs to $412. What is the marginal cost of the 101st unit, and what is the average total cost at 100 units?"
  type: multiple-choice
  options:
    - "MC = $12; ATC = $10.00"
    - "MC = $4; ATC = $10.00"
    - "MC = $12; ATC = $4.00"
    - "MC = $6; ATC = $7.00"
  answer: 0
  explanation: "Marginal cost = ΔTCC/ΔQ = ($412+$600) - ($400+$600) / 1 = $12. Since ΔFC = 0, MC = ΔVC/ΔQ = $12 - $0 (the change in VC only) = $12. ATC at 100 units = TC/Q = ($600 + $400)/100 = $1000/100 = $10.00. This shows the key relationship: MC reflects only the change in variable costs, not the fixed overhead, while ATC includes both components divided by output."

- question: "At the minimum point of the average total cost (ATC) curve, which of the following must be true?"
  type: multiple-choice
  options:
    - "ATC equals average variable cost (AVC), since fixed costs are zero at the minimum"
    - "Marginal cost (MC) equals ATC, because when MC is below ATC it pulls the average down and when above it pulls the average up"
    - "MC is at its own minimum, since cost curves reach their lowest point simultaneously"
    - "ATC equals average fixed cost (AFC), as the overhead is fully spread at the minimum"
  answer: 1
  explanation: "The MC curve always passes through the minimum of the ATC curve — this is a mathematical identity, not a coincidence. When MC < ATC, adding one more unit costs less than the average, pulling ATC down. When MC > ATC, the additional unit costs more than average, pulling ATC up. They must be equal exactly at the minimum. The same logic applies to the AVC curve: MC passes through AVC's minimum too. MC and ATC do NOT reach their minima at the same output level — MC typically turns upward before ATC does."

- question: "An increase in a firm's fixed costs will raise its marginal cost curve."
  type: true-false
  answer: false
  explanation: "Marginal cost measures how total cost changes as output changes by one unit: MC = ΔTC/ΔQ = ΔVC/ΔQ (since ΔFC = 0). Fixed costs, by definition, do not change with output — so they contribute nothing to ΔTC. An increase in fixed costs shifts the ATC and AFC curves upward but leaves the MC curve and the AVC curve completely unchanged. This is why fixed costs are called 'sunk' in the short run — they don't influence how much it costs to produce one more unit."

- question: "Average fixed cost (AFC) declines continuously as output increases, because a fixed overhead cost is spread over more and more units."
  type: true-false
  answer: true
  explanation: "AFC = FC/Q. Since FC is a constant, dividing by larger and larger Q drives AFC toward zero — it falls throughout the entire output range and never turns upward. This is the 'spreading the overhead' effect. It is one reason ATC declines at first even when AVC is relatively stable — the falling AFC pulls ATC down. Eventually, as AVC starts rising (due to diminishing returns), AVC's increase more than offsets AFC's decline, and ATC reaches its minimum and then rises."

- question: "Why is MC = ΔVC/ΔQ even though TC = FC + VC? What does this tell you about the relationship between fixed costs and short-run production decisions?"
  type: short-answer
  answer: "Because fixed costs don't change with output, ΔFC = 0 for any change in quantity. So ΔTC = ΔFC + ΔVC = 0 + ΔVC = ΔVC. Therefore MC = ΔTC/ΔQ = ΔVC/ΔQ — marginal cost is determined entirely by variable costs. For short-run production decisions (should we produce this unit?), only variable costs matter because fixed costs are already paid regardless of output. A firm should produce as long as revenue covers variable costs; fixed costs only affect whether to stay in business long-run or exit."
  explanation: "This is a critical insight for profit maximization: a firm comparing revenue to cost at the margin compares price to MC, and MC is unaffected by fixed overhead. A factory that has already paid $1 million in rent should not let that sunk cost influence how many units to produce today — only the variable cost of production (materials, labor per unit) and the selling price should drive that decision. Fixed costs matter for entry/exit and investment decisions, but not for moment-to-moment output choices."
```

## Explainer

Your prerequisite work on factor demand established that firms hire inputs up to the point where their marginal product justifies their cost. Now we look at how those input costs aggregate into the cost curves that govern output decisions. The key structural distinction is between inputs the firm can and cannot adjust in the short run.

**Fixed costs (FC)** are costs that don't change with output — you pay them whether you produce zero units or a million. Think of the rent on a factory, a piece of capital equipment under a long-term lease, or a salaried manager. These are locked in because the input cannot be adjusted quickly. **Variable costs (VC)** respond to output — more production requires more labor hours, more raw materials, more energy. **Total cost (TC = FC + VC)** rises with output because variable inputs rise, but the fixed component means TC is strictly positive even at zero output.

Dividing each cost component by quantity gives three average curves that reveal the firm's per-unit economics. **Average fixed cost (AFC = FC/Q)** falls continuously as output rises — the fixed overhead is spread over more units, a phenomenon called "spreading the overhead." **Average variable cost (AVC = VC/Q)** typically falls at first (due to increasing returns to labor — more workers can specialize) and then rises (as the factory becomes congested and workers get in each other's way — diminishing marginal returns). **Average total cost (ATC = TC/Q = AFC + AVC)** is the vertical sum: it inherits both the declining AFC and the U-shape of AVC, producing its own U-shape, but its minimum occurs at higher output than AVC's minimum because AFC is still declining.

**Marginal cost (MC = ΔTC/ΔQ)** is the most important cost concept for decisions. Because fixed costs don't change with output, ΔFC = 0, so MC = ΔTCC/ΔQ = ΔVC/ΔQ — marginal cost is purely determined by how variable costs change. The MC curve passes through the minimum points of both AVC and ATC — this is a mathematical necessity, not a coincidence. When MC is below average cost, producing more pulls the average down; when MC is above average cost, producing more pulls the average up; they must be equal at the average's minimum. This relationship between marginal and average is the cornerstone of all the cost-curve geometry you'll use when studying profit maximization and market structure.
