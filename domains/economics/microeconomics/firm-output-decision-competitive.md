---
id: firm-output-decision-competitive
title: Competitive Firm Output Decision and Supply
domain: economics
course: microeconomics
prerequisites:
- id: profit-maximization-microeconomics
  type: hard
- id: perfect-competition
  type: hard
builds-toward:
- supply-curve-individual-firm
- competitive-industry-long-run
tags:
- producer theory
- competition
- profit maximization
stage: formal-systems
status: validated
---

# Competitive Firm Output Decision and Supply

## Core Idea
A competitive firm facing a constant market price maximizes profit by producing where marginal cost equals price (P = MC). In the short run, the firm will shut down if price falls below minimum average variable cost. The firm's supply curve is its marginal cost curve above the shutdown point, showing how quantity supplied responds to price. Long-run supply requires price to cover average cost.

## Questions

```yaml
- question: "A competitive firm's average variable cost is $8 and its average total cost is $12. The market price is $10. What should the firm do in the short run?"
  type: multiple-choice
  options:
    - "Shut down immediately, since the price doesn't cover average total cost"
    - "Continue producing, since the price covers average variable cost and reduces losses compared to shutting down"
    - "Reduce output to zero and exit the industry"
    - "Raise its price to $12 to cover average total cost"
  answer: 1
  explanation: "In the short run, fixed costs are sunk — the firm pays them whether it operates or not. As long as price covers average variable cost (P ≥ min AVC), operating generates revenue that offsets at least some fixed costs. Here P = $10 > AVC = $8, so continuing to produce reduces the total loss. The firm should only shut down if P falls below min AVC — the shutdown point. Option A is the most tempting wrong answer because losing money feels like it should mean shutting down, but sunk fixed costs change the calculus."

- question: "Which portion of a competitive firm's cost curves defines its short-run supply curve?"
  type: multiple-choice
  options:
    - "The marginal cost curve above the minimum of average total cost"
    - "The average variable cost curve above its minimum"
    - "The marginal cost curve above the minimum of average variable cost"
    - "The entire marginal cost curve for all positive output levels"
  answer: 2
  explanation: "The firm produces where P = MC, but only operates when P ≥ min AVC (the shutdown point). Below min AVC, quantity supplied = 0. So the short-run supply curve traces the MC curve for all prices at or above the minimum of AVC. This is distinct from the long-run threshold (min ATC) — in the short run, fixed costs are sunk, so the relevant floor is AVC, not ATC."

- question: "A competitive firm that is earning an economic loss should usually shut down in the short run to minimize its losses."
  type: true-false
  answer: false
  explanation: "A loss-making firm should shut down only if price falls below minimum average variable cost. If P is between min AVC and min ATC, the firm is losing money but covers its variable costs — operating costs less than shutting down, because fixed costs must be paid regardless. Shutting down when P > min AVC means forfeiting revenue that would have partially offset unavoidable fixed costs. The shutdown rule is about variable costs, not total costs."

- question: "At the long-run competitive equilibrium, the market price equals both the firm's marginal cost and its minimum average total cost."
  type: true-false
  answer: true
  explanation: "This triple equality — P = MC = min ATC — is the defining condition of long-run competitive equilibrium. Free entry drives economic profits to zero, pushing price down to min ATC (the break-even point). Simultaneously, the P = MC condition holds because firms are profit-maximizing price-takers. This intersection is also where allocative efficiency (P = MC) and productive efficiency (min ATC) coincide — a benchmark against which other market structures are compared."

- question: "Explain why a competitive firm's short-run shutdown condition is P < min AVC rather than P < min ATC."
  type: short-answer
  answer: "In the short run, fixed costs are sunk — the firm pays them regardless of whether it operates. The decision to produce or not therefore depends only on whether revenue covers the costs that operating actually causes: variable costs. If P ≥ min AVC, the firm recovers its variable costs and contributes something toward the unavoidable fixed costs, making operating better than shutting down. Only when P < min AVC does every unit produced deepen the loss beyond the fixed costs alone — at that point, earning zero revenue from shutdown is actually better. In the long run, fixed costs become avoidable (the firm can exit), so the threshold shifts up to min ATC."
  explanation: "The key is distinguishing sunk costs (irrelevant to short-run decisions) from variable costs (the costs that operating actually creates). Short-run shutdown is about whether you're covering your avoidable costs, not your total costs."
```

## Explainer

A competitive firm is a **price-taker**: it sells into a market where the price is set by the intersection of all buyers and sellers, and its own output is too small to shift that price. From your study of perfect competition, you know this means the firm's demand curve is perfectly horizontal at the market price P — every unit it sells fetches P, neither more nor less. From your study of profit maximization, you know the general rule is MR = MC. For a price-taking firm, MR = P always (because selling one more unit adds exactly P to revenue). So the profit-maximizing rule simplifies to **P = MC**: keep expanding output as long as the price received exceeds the cost of producing one more unit, and stop when they're equal.

The **supply curve** of a competitive firm is derived directly from this logic. If the price rises from $10 to $12, the firm now finds it profitable to push output further up its rising marginal cost curve until MC again equals the new price. If price falls, the firm walks back down. The supply curve is therefore the MC curve itself — specifically, the portion of the MC curve above a critical threshold called the **shutdown point**. The shutdown point is the minimum of the **average variable cost** (AVC) curve. Here is why: even a loss-making firm should keep operating in the short run as long as it covers its variable costs, because fixed costs are sunk regardless. If P ≥ min AVC, operating loses less money than shutting down. If P < min AVC, every unit sold deepens the loss beyond the unavoidable fixed costs — better to produce nothing. So the short-run supply curve traces MC above min AVC and is zero below it.

The **long-run** adds another threshold. In the long run, fixed costs are no longer sunk — the firm can exit and avoid them entirely. The long-run shutdown condition is therefore tighter: the firm exits if price falls below **average total cost** (ATC), not just AVC. The long-run supply curve traces MC above min ATC. At the minimum of ATC, marginal cost and average total cost intersect — this is the **break-even point**, where economic profit is exactly zero. A competitive industry's long-run equilibrium lands here: free entry drives economic profit to zero, and each firm operates at efficient scale. The P = MC = min ATC condition characterizes this efficient competitive equilibrium and is the benchmark against which other market structures are compared. Monopoly, for instance, produces where MR = MC but P > MC — a wedge between the price charged and the cost of the last unit produced, representing deadweight loss.
