---
id: perfect-competition-firm-and-industry
title: 'Perfect Competition: Firm Behavior and Industry Equilibrium'
domain: economics
course: microeconomics
prerequisites:
- id: perfect-competition
  type: hard
- id: profit-maximization-microeconomics
  type: hard
- id: average-and-marginal-cost-curves
  type: hard
- id: economies-of-scale-long-run
  type: soft
builds-toward:
- market-equilibrium
tags:
- perfect-competition
- firm
- industry
- equilibrium
stage: formal-systems
status: validated
---

# Perfect Competition: Firm Behavior and Industry Equilibrium

## Core Idea
In perfect competition, firms are price-takers facing a horizontal demand curve at the market price. Each firm maximizes profit where MR = P = MC. In long-run equilibrium, free entry/exit drives price down to minimum ATC, so economic profit = 0. The industry's long-run supply curve is determined by how factor prices change as industry output expands (constant-, increasing-, or decreasing-cost industries).

## How It's Best Learned
Compare short-run (firms earn economic profit, losses possible) to long-run (zero economic profit, entry/exit adjusts). Graph individual firm and market simultaneously to see how entry shifts market supply.

## Common Misconceptions
- Perfect competition means firms do well (zero economic profit means firms earn only normal return on capital).
- Free entry eliminates differences between firms (it equalizes returns, but firms may have different scales or costs).

## Questions

```yaml
- question: "A competitive industry is in long-run equilibrium. A consultant reports 'all firms in this industry earn zero profit.' An economist's correct interpretation is:"
  type: multiple-choice
  options:
    - "The industry is in crisis — firms are on the verge of bankruptcy"
    - "Firms are earning exactly the competitive return on capital — what they could earn elsewhere"
    - "Firms have no revenue because prices have been driven to zero"
    - "The industry is characterized by natural monopoly and should be regulated"
  answer: 1
  explanation: "Zero economic profit means firms earn exactly the opportunity cost of capital — no more, no less. This is the normal competitive return, not a sign of crisis. Accountants would record these same firms as profitable (positive accounting profit), because accounting profit doesn't subtract the opportunity cost of capital. The economist's 'zero profit' means 'no economic rent above the competitive return.' This is the long-run equilibrium benchmark of a well-functioning competitive market."

- question: "A profitable new firm enters a perfectly competitive industry. The long-run effect on the market price is:"
  type: multiple-choice
  options:
    - "Price rises as existing firms raise prices to protect margins"
    - "Price falls as entry increases industry supply, until economic profit = 0 for all firms"
    - "Nothing — a price-taker firm cannot affect the market price regardless of entry"
    - "Price is indeterminate because each firm sets its own price"
  answer: 1
  explanation: "Positive economic profit signals that capital is earning above its opportunity cost, attracting new entrants. Each new firm adds to market supply, shifting the supply curve rightward and pushing the market price down. The process continues until price falls to minimum ATC, at which point economic profit = 0 and the incentive for further entry disappears. Each individual firm is a price-taker, but collective entry affects the market supply curve and thereby the equilibrium price."

- question: "In a perfectly competitive market, a firm that shuts down in the short run earns zero profit."
  type: true-false
  answer: false
  explanation: "A firm that shuts down in the short run still owes its fixed costs — rent, equipment leases, contractual obligations — which it cannot escape in the short run. Its profit is negative: it earns zero revenue but loses its total fixed costs. The shutdown decision compares this certain loss (fixed costs) against the loss from operating. A firm operates as long as P > AVC, because earning some contribution above variable costs reduces the fixed-cost loss. The floor from shutdown is negative fixed costs, not zero."

- question: "Long-run equilibrium in perfect competition occurs at the minimum of the average total cost curve because that is the only point where P = MC = ATC simultaneously."
  type: true-false
  answer: true
  explanation: "Correct. Three conditions must hold simultaneously in long-run equilibrium: (1) P = MC (profit maximization); (2) P = ATC (zero economic profit); (3) P = MR (price-taking). These can only hold at the point where MC crosses ATC at its minimum — because MC = ATC only at the minimum of ATC (when MC is below ATC, ATC is falling; when MC is above ATC, ATC is rising). Long-run equilibrium requires operating at exactly that point."

- question: "Why does zero economic profit in long-run competitive equilibrium not mean that successful firms in the industry are doing something wrong or should exit?"
  type: short-answer
  answer: "Economic profit is measured after subtracting the opportunity cost of all resources, including capital. A firm earning 'zero economic profit' is earning exactly what its capital could earn in the next best investment — the market rate of return. Owners have no incentive to exit because they are not doing worse than they would elsewhere. Accountants measure profit differently and don't subtract opportunity costs, so the same firm shows positive accounting profit. Zero economic profit is the efficiency benchmark, not a sign of failure."
  explanation: "This distinction is one of the most important in microeconomics. 'Normal profit' is what accountants call profit; 'zero economic profit' is what economists call the same thing, once opportunity costs are properly accounted for. Economic profit above zero is an efficiency signal: it means a sector is earning above the competitive return, so more capital should flow there. Economic profit below zero is the exit signal. Long-run equilibrium at zero economic profit means the sector is neither over- nor under-supplied."
```

## Explainer

You already know that firms maximize profit where MR = MC, and you know the shapes of average and marginal cost curves. Perfect competition wires these tools together into a complete theory of how markets self-regulate through entry and exit. The most important result — zero long-run economic profit — seems paradoxical at first, but it follows inevitably from the logic of free entry.

Start with the short run. Each firm is a **price-taker**: it faces a horizontal demand curve at the market price P, so MR = P for every unit. The firm produces where P = MC and earns economic profit if P > ATC at that output, or takes a loss if P < ATC. Notice that short-run losses don't force immediate exit — a firm stays open as long as P > AVC, because it's better to cover variable costs and lose only fixed costs than to shut down and lose all fixed costs. This is the **shutdown rule** from profit maximization theory, now in context: exit is about comparing price to AVC, not ATC.

Now run the entry-exit machine. If price is above minimum ATC, firms earn positive economic profit. This is the signal that attracts new entrants — capital is earning above its opportunity cost here. Entry increases market supply, which pushes the market price down. Entry continues until price falls to minimum ATC, at which point economic profit = 0 and there's no incentive for further entry. The reverse operates for losses: price below minimum ATC drives exit, supply contracts, price rises, and exit stops at zero profit. The **long-run equilibrium** is therefore always at the bottom of the ATC curve: P = minimum ATC = MC. This is a remarkable result — competitive pressure forces efficiency.

The **long-run industry supply curve** captures how this adjustment plays out as industry output expands. In a **constant-cost industry**, new entry doesn't change input prices (the industry is small relative to input markets), so minimum ATC stays constant and the long-run supply curve is horizontal. In an **increasing-cost industry**, expansion bids up input prices (land, specialized labor), raising ATC and the long-run equilibrium price — the supply curve slopes upward. In a **decreasing-cost industry**, expansion generates economies in input production (economies of scale in supplying inputs), so ATC falls as the industry grows — the long-run supply curve slopes downward. These aren't exotic special cases; they're the mechanism by which industry expansion feeds back into costs.

Zero economic profit does not mean firms are barely surviving. **Economic profit** is profit above the opportunity cost of capital — the return the firm's owners could have earned in their best alternative investment. Zero economic profit means the firm earns exactly that competitive return. Accountants may record a healthy profit; economists net out the opportunity cost and call it zero. This distinction explains why competitive industries can be full of profitable, well-run firms in accounting terms while economists correctly say there's no economic rent being earned. The signal function of economic profit — "come here, capital is earning above its opportunity cost" — is precisely what drives the entry mechanism that makes competition self-regulating.
