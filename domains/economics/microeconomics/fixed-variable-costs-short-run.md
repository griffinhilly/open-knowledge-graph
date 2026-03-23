---
id: fixed-variable-costs-short-run
title: Fixed and Variable Costs in the Short Run
domain: economics
course: microeconomics
prerequisites:
- id: short-run-costs
  type: hard
builds-toward:
- average-and-marginal-cost-curves
tags:
- costs
- short-run
- cost-structure
stage: formal-systems
status: validated
---

# Fixed and Variable Costs in the Short Run

## Core Idea
In the short run, some inputs (capital, premises) are fixed, while others (labor, materials) are variable. Total Cost = Fixed Cost + Variable Cost. Fixed costs don't change with output; variable costs rise as production increases. This distinction explains why firms face different cost structures in the short run (constrained) versus long run (flexible).

## How It's Best Learned
Examine a firm's budget: rent is fixed, wages and materials are variable. See how total cost = fixed cost (unchanged) + variable cost (rising with output).

## Questions

```yaml
- question: "A restaurant has $10,000/month in rent (fixed) and $8,000/month in food and labor costs (variable). It earns $9,000/month in revenue. What should it do in the short run?"
  type: multiple-choice
  options:
    - "Shut down immediately — it's losing $9,000 per month"
    - "Continue operating — revenue exceeds variable costs, so operating recovers some fixed cost"
    - "Continue operating only if it can negotiate a rent reduction"
    - "Shut down — total costs exceed revenue, so every unit produced makes the loss worse"
  answer: 1
  explanation: "The restaurant's total cost is $18,000 and revenue is $9,000, so it loses $9,000/month. But the shutdown decision in the short run only compares revenue to variable costs ($8,000). Revenue ($9,000) exceeds variable costs ($8,000) by $1,000, meaning the restaurant recovers $1,000 of its fixed rent by staying open. If it shuts down, it still owes the full $10,000 rent and loses $10,000. Operating loses $9,000 — which is better. The fixed cost is irrelevant to the operating decision because it is owed regardless. Shut down only when revenue falls below variable costs."

- question: "Which of the following best explains why fixed costs are described as 'sunk' in the short run?"
  type: multiple-choice
  options:
    - "Fixed costs are always larger than variable costs in the short run"
    - "Fixed costs cannot be recovered by producing less or shutting down — they are owed no matter what the firm does"
    - "Fixed costs represent past investments that were poorly planned"
    - "Fixed costs eventually become variable costs as the firm grows"
  answer: 1
  explanation: "A cost is 'sunk' in the short run if it cannot be avoided by changing the production decision. Because fixed costs — rent, loan payments, contracted salaries — are owed whether the firm produces zero or a million units, they do not factor into the rational production decision. They are committed regardless of output. This is not about poor planning (option C), nor about scale (option D). The sunk nature of fixed costs is exactly why a firm can rationally continue operating even while losing money overall — the question is whether operating recovers any of those unavoidable costs."

- question: "A firm's total cost includes both fixed and variable components, so both types of cost should factor into the short-run decision of whether to keep producing."
  type: true-false
  answer: false
  explanation: "This is the central misconception the FC/VC distinction corrects. Fixed costs are irrelevant to the short-run production decision because they are unavoidable — the firm owes them whether it produces or not. The only relevant comparison is between revenue and variable costs. If price exceeds average variable cost, continuing to operate is better than shutting down, even if the firm is losing money overall. Only variable costs change with the shutdown decision, so only they should influence it."

- question: "In the short run, a firm's fixed costs remain constant at every level of output, including zero."
  type: true-false
  answer: true
  explanation: "This is the defining feature of fixed costs — they do not vary with output. Whether the firm produces 0 units or 10,000 units, fixed costs (rent, equipment payments, salaried management) remain the same. Graphically, the fixed cost curve is a horizontal line at the same height across all output levels. This is precisely why shutting down does not eliminate fixed costs: output = 0 is just another point on the horizontal line. Fixed costs only disappear in the long run, when all commitments can be renegotiated or exited."

- question: "Why are fixed costs irrelevant to the short-run shutdown decision, and what cost is actually relevant? Explain the reasoning."
  type: short-answer
  answer: "Fixed costs are irrelevant because they must be paid whether or not the firm operates — they are sunk in the short run. Shutting down does not make them go away. The relevant comparison is between revenue and variable costs. If revenue exceeds variable costs, operating is better than shutting down because it recovers at least part of the fixed cost. The shutdown condition is: shut down when price falls below average variable cost (P < AVC), because below that point, operating doesn't even cover the costs that vary with production."
  explanation: "This reasoning reveals the core logic: a decision should only respond to costs that change with that decision. Since fixed costs don't change whether you produce or not, they are genuinely irrelevant to the produce-vs-shutdown comparison. The variable cost is the one that changes when you shut down (it falls to zero), so it is the relevant cost. This is a direct application of the marginal thinking principle: only consider costs that differ between the two options being compared."
```

## Explainer

From your study of short-run costs, you know that the short run is defined not by calendar time but by the presence of at least one **fixed input** — an input whose quantity cannot be adjusted regardless of how much the firm produces. The cost of those fixed inputs is the **fixed cost (FC)**: rent on a factory, interest payments on equipment loans, the salary of a permanently contracted manager. These costs do not move whether the firm produces zero units or ten thousand. They are sunk in the short run.

**Variable costs (VC)**, by contrast, move directly with output. If a bakery makes more loaves, it needs more flour, more electricity, more hours from part-time staff. These inputs can be adjusted quickly. Total cost is simply their sum: TC = FC + VC. The graphical implication is stark — on a TC curve plotted against output, the TC curve starts at FC (where VC = 0) and rises as output increases, while the FC curve is a horizontal line at that same height throughout.

The distinction matters most when a firm is deciding whether to keep operating in the short run. Since fixed costs cannot be avoided by shutting down — they are owed regardless — they are **irrelevant to the production decision**. The relevant comparison is whether revenue covers variable costs. A firm should continue operating as long as price exceeds average variable cost (AVC), even if it is making a loss overall, because operating at least recovers some of the fixed cost. If it shuts down, it still owes the full fixed cost. This is the shutdown condition, and it rests entirely on the FC/VC distinction.

In the long run, the distinction collapses: all inputs become variable, all costs become variable. A firm can exit an industry, renegotiate leases, sell equipment, or redesign its entire production process. The short-run constraint — being locked into a fixed cost — is precisely what creates the asymmetry in behavior between short-run and long-run supply curves and explains why industries adjust sluggishly to demand shocks. The cost structure you inherit in the short run shapes every output, shutdown, and pricing decision until those fixed commitments expire.
