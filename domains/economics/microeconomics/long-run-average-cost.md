---
id: long-run-average-cost
title: Long-Run Average Cost and Economies of Scale
domain: economics
course: microeconomics
prerequisites:
- id: short-run-cost-fixed-variable
  type: hard
- id: economies-of-scale-long-run
  type: soft
- id: long-run-cost-structure
  type: soft
builds-toward:
- profit-maximization-output-level
- equilibrium-perfect-competition
tags:
- long-run
- average-cost
- economies-of-scale
- minimum-efficient-scale
stage: formal-systems
status: validated
---
# Long-Run Average Cost and Economies of Scale

## Core Idea
In the long run, all inputs are variable, so firms can choose their optimal scale of production. The long-run average cost curve (LAC) is the envelope of short-run average cost curves at different scales. Economies of scale occur when long-run average cost declines as output increases (due to specialization, bulk discounts, etc.). Diseconomies of scale occur when LAC rises with output (due to management complexity, coordination problems, etc.). The minimum point of the LAC defines the minimum efficient scale—the smallest output level at which a firm achieves lowest average cost.

## How It's Best Learned
Compare short-run and long-run cost curves, observing how firms can lower costs by adjusting all inputs in the long run. Examine industry structures and relate them to the shape of the LAC curve.

## Common Misconceptions
- Thinking economies of scale apply to all firms—they depend on specific production technologies and industry characteristics.
- Confusing economies of scale with increasing returns to scale in production—they're related but distinct concepts.

## Questions

```yaml
- question: "A water utility company requires enormous infrastructure investment and can supply a city more cheaply the more customers it serves. What market structure does this cost structure predict?"
  type: multiple-choice
  options:
    - "Perfect competition — low average costs attract many entrants who compete prices down"
    - "A natural monopoly tendency — the minimum efficient scale is so large that only one firm can operate at lowest cost within the market"
    - "An oligopoly — a few large firms share the infrastructure costs equally"
    - "Monopolistic competition — product differentiation allows many firms with high fixed costs to coexist"
  answer: 1
  explanation: "When minimum efficient scale (MES) — the output level at which average costs are minimized — is large relative to total market demand, only one or a few firms can operate at efficient scale. A water utility's MES may be so large that building a second competing network would drive both above minimum average cost, making one supplier more efficient than two. This is the definition of a natural monopoly tendency. The key insight is that industry structure (how many firms) is shaped by where MES falls relative to market size — the LAC curve is doing explanatory work about market organization."

- question: "A firm doubles its output and finds that its total cost increases by 80% (less than double). This firm is experiencing:"
  type: multiple-choice
  options:
    - "Diseconomies of scale — total costs increased, so average costs must be rising"
    - "Economies of scale — average cost fell because total cost rose by less than output"
    - "Constant returns to scale — the cost increase of 80% is close enough to 100% to be considered constant"
    - "Diminishing returns — in the long run all inputs are variable, so costs should double exactly"
  answer: 1
  explanation: "Economies of scale means that average cost decreases as output increases — equivalently, a doubling of output costs less than a doubling of total cost. If output doubles (100% increase) but total cost only rises 80%, then cost per unit has fallen. Average cost = total cost / output. Before doubling: TC/Q. After: 1.8·TC / 2Q = 0.9·TC/Q — average cost fell to 90% of its original value. This is economies of scale. Option A confuses 'total cost increased' with 'average cost increased' — these are different. Option C misidentifies the threshold: constant returns to scale requires total cost to double exactly when output doubles."

- question: "If a firm doubles its output and total cost also exactly doubles, it is experiencing economies of scale."
  type: true-false
  answer: false
  explanation: "When output doubles and total cost also exactly doubles, average cost (TC/Q) is unchanged — this is constant returns to scale, not economies of scale. Economies of scale occur when long-run average cost *falls* as output increases, meaning total cost rises by *less* than proportionally with output. A common error is conflating 'scale is increasing' (output is growing) with 'economies of scale' (average cost is falling). The relevant question is always: when output increases by X%, does total cost increase by more than X% (diseconomies), equal to X% (constant), or less than X% (economies)?"

- question: "The long-run average cost (LAC) curve lies at or below every short-run average cost curve because the firm has more flexibility in the long run."
  type: true-false
  answer: true
  explanation: "In the short run, at least one input is fixed, constraining the firm's ability to minimize cost for a given output level. In the long run, all inputs are variable, so the firm can choose the optimal scale for any output. The LAC is constructed as the envelope of all possible short-run curves — at each output level, the firm selects the plant size (short-run cost curve) that minimizes average cost for that output. Having more choices can never make outcomes worse, so LAC ≤ SRAC for any output level. This is why the LAC is sometimes called the 'planning curve': it represents costs available to a firm that can redesign its entire operation."

- question: "Why is the long-run average cost curve called the 'envelope' of the short-run average cost curves, and what does this imply about the relationship between long-run and short-run average costs?"
  type: short-answer
  answer: "The LAC is the envelope of short-run curves because it is constructed by taking, at each output level, the minimum average cost achievable across all possible plant sizes (each plant size has its own short-run average cost curve). The LAC traces the lower boundary that 'wraps around' the family of short-run curves from below. This implies that long-run average cost is always equal to or less than any particular short-run average cost: the firm in the long run can always do at least as well as it does when constrained to a fixed plant size, and usually better for most output levels."
  explanation: "The envelope relationship captures the value of flexibility. In the short run, a firm is 'stuck' with its plant size — if demand changes, it either overuses or underuses capacity, raising average cost. In the long run, it can right-size. For a given output level, the optimal short-run plant size achieves exactly the same average cost as the LAC; for all other output levels, that plant size is suboptimal and its short-run curve lies above the LAC. The envelope metaphor is apt: if you drew every possible short-run curve on one graph, the LAC would hug their lowest points from below like a tight envelope around them."
```

## Explainer

In the short run, at least one input is fixed—your factory size, your lease, your equipment. Your prerequisite on short-run costs shows how this creates the familiar U-shaped average cost curve: spreading fixed costs over more units initially lowers average cost, but eventually diminishing returns to the variable input drive it back up. The **long run** is different: it is the planning horizon over which a firm can adjust *everything*—build a bigger or smaller factory, renegotiate leases, adopt new technology. There are no fixed inputs in the long run.

Because the firm can choose any scale in the long run, the **long-run average cost (LAC) curve** is constructed as an envelope of short-run curves. Imagine every possible factory size, each with its own short-run average cost curve. For each output level, the firm chooses the factory size that minimizes cost for that output. Connecting those minimum-cost points traces out the LAC. The LAC lies at or below any individual short-run curve—long-run flexibility can only expand your options, never reduce them.

The shape of the LAC curve reveals the nature of **scale economies**. When the LAC is falling, the firm experiences **economies of scale**: doubling output costs less than double. This happens because of specialization (workers focus on narrower tasks), bulk purchasing discounts, spreading indivisible fixed costs like R&D over more units, and network effects. When the LAC is rising, the firm faces **diseconomies of scale**: the coordination and management challenges of a large organization push average costs up. Between these regions, the LAC may be flat, reflecting **constant returns to scale**.

The bottom of the LAC curve marks the **minimum efficient scale (MES)**—the smallest output level at which average costs are minimized. MES shapes industry structure: if MES is small relative to market demand, many small firms can coexist (restaurants, hair salons). If MES is large relative to market demand, only one or a few firms can operate efficiently—a natural tendency toward monopoly (water utilities, rail networks). Reading a market's industry structure often starts by asking what the LAC curve looks like and where MES falls.
