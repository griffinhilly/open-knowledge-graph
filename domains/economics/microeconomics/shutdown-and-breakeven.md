---
id: shutdown-and-breakeven
title: Shutdown and Breakeven Decisions
domain: economics
course: microeconomics
prerequisites:
- id: profit-maximization-microeconomics
  type: hard
- id: perfect-competition
  type: soft
builds-toward:
- monopoly-microeconomics
tags:
- shutdown
- breakeven
- sunk cost
- short run
- long run
stage: formal-systems
status: validated
---
# Shutdown and Breakeven Decisions

## Core Idea
A firm shuts down in the short run when price falls below average variable cost (P < AVC), because it cannot cover operating costs; it is better to produce nothing and lose only fixed costs. The breakeven point is where P = ATC, meaning the firm earns zero economic profit. In the long run, the shutdown condition becomes P < LRAC since all costs are variable. Fixed costs are sunk in the short run and should not influence the shutdown decision — only variable costs and revenue matter for that choice.

## How It's Best Learned
Use the three-region diagram (P above ATC, between AVC and ATC, below AVC) and practice classifying firm decisions at each price level. Reinforce sunk cost irrelevance by contrasting with popular but incorrect reasoning.

## Common Misconceptions
- Students often say a firm should shut down whenever it is losing money (profit < 0); but it should operate as long as P ≥ AVC, since fixed costs are lost either way.
- Confusing the short-run shutdown condition (P < AVC) with the long-run exit condition (P < LRAC).

## Questions

```yaml
- question: "A firm's price is $8, its AVC is $6, and its ATC is $10. What should the firm do in the short run?"
  type: multiple-choice
  options:
    - "Shut down, because the firm is earning negative economic profit"
    - "Continue operating, because it covers variable costs and contributes something toward fixed costs"
    - "Shut down, because the firm cannot cover its average total cost"
    - "Continue operating only if it can raise its price above ATC"
  answer: 1
  explanation: "P ($8) > AVC ($6), so the firm covers its variable costs and earns $2 per unit toward fixed costs. Even though P < ATC means the firm is losing money, it loses less by operating than by shutting down. If it shuts down, it still loses all its fixed costs with zero revenue — a larger loss. The shutdown rule is P < AVC, not P < ATC."

- question: "In the short run, a firm with P < ATC but P > AVC is best described as:"
  type: multiple-choice
  options:
    - "At breakeven — it covers all costs and earns zero economic profit"
    - "Operating at a loss but producing, because variable costs are covered"
    - "Indifferent between operating and shutting down"
    - "Violating the profit-maximization condition by continuing to produce"
  answer: 1
  explanation: "This is the 'operating loss' zone — between the shutdown point (P = AVC) and breakeven (P = ATC). The firm is losing money but should still produce because it covers variable costs and contributes something toward fixed costs. Fixed costs are sunk and will be lost regardless, so the operating loss is smaller than the shutdown loss. Only at P = ATC does the firm break even (zero economic profit)."

- question: "A firm should shut down in the short run whenever its economic profit is negative."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about shutdown decisions. A firm with negative profit should still operate as long as P ≥ AVC. Fixed costs are sunk in the short run — they cannot be recovered by shutting down. If the firm operates, it covers variable costs and offsets some fixed costs, making the loss smaller than if it simply produced nothing. The shutdown rule is P < AVC, not 'profit < 0.'"

- question: "In the long run, the shutdown condition changes from P < AVC to P < LRAC because there are no fixed costs in the long run."
  type: true-false
  answer: true
  explanation: "In the long run, a firm can exit the industry and recover all resources for alternative uses — no costs are sunk. Any cost that isn't covered is a genuine avoidable loss. The long-run exit condition is therefore P < LRAC (long-run average cost). The short-run condition P < AVC exists only because fixed costs are already committed; in the long run that asymmetry disappears."

- question: "Explain why fixed costs are irrelevant to the short-run shutdown decision."
  type: short-answer
  answer: "Fixed costs are sunk in the short run — already committed and unavoidable whether the firm produces or not. If the firm shuts down, it loses all its fixed costs with zero revenue. If it operates, it pays fixed costs plus variable costs but also earns revenue. As long as revenue exceeds variable costs (P > AVC), operating produces a smaller total loss than shutting down. Since fixed costs are identical in both scenarios, they cancel out of the comparison and have no bearing on the decision."
  explanation: "The sunk cost principle applies directly: a cost that is identical across all choices should be ignored when making that choice. The shutdown comparison reduces to: does operating revenue exceed variable costs? Fixed costs appear on both sides of the comparison and cancel. What determines the outcome is solely whether P ≥ AVC."
```

## Explainer

You already know from profit maximization that a firm produces where MR = MC — specifically, P = MC for a perfectly competitive firm. But that rule only tells you the *best output to produce given you're producing at all*. Shutdown and breakeven analysis asks the prior question: should the firm be producing anything at all?

The answer turns on a concept you may not have formalized before: the distinction between **fixed costs** and **variable costs**, and specifically the irreversibility of fixed costs in the short run. Suppose you run a bakery. Your lease payment is due whether you bake anything or not. Your flour and labor costs only arise if you actually bake. Fixed costs are **sunk** in the short run — already committed, not recoverable by shutting down. Variable costs are avoidable — you don't incur them if you produce zero.

This asymmetry drives the shutdown decision. If a firm shuts down, its revenue is zero and its loss equals its fixed costs. If it operates, its revenue is P × Q and its loss (if any) is P × Q − TC = P × Q − TVC − TFC. The firm prefers to operate when its operating loss is smaller than its shutdown loss — that is, when P × Q > TVC, or equivalently when P > AVC. The firm covers its variable costs and contributes something toward fixed costs. Even losing money is better than losing *more* money. The **short-run shutdown point** is therefore P = AVC (minimum of the AVC curve). Below this price, the firm cannot even cover operating costs and is better off idle.

The **breakeven point** is a separate condition: P = ATC (minimum of the ATC curve). At this price, total revenue exactly equals total cost, including fixed costs. Economic profit is zero. Above this price, the firm earns positive economic profit; below it (but above AVC), the firm is operating at a loss but still better off than shutting down. This creates three distinct regions: (1) P > ATC — operate profitably; (2) AVC < P < ATC — operate at a loss, but it beats shutting down; (3) P < AVC — shut down.

The long-run version is cleaner because there are no sunk costs. In the long run, a firm can exit the industry entirely, recovering all resources for alternative uses. There are no fixed costs to absorb. The exit condition becomes simply P < LRAC: if the firm cannot cover all costs, it should exit. The distinction between short-run shutdown (comparing to AVC) and long-run exit (comparing to LRAC) explains why you sometimes observe firms operating at a loss in the short run — they are waiting to see if prices recover before committing to the irreversible decision to exit. Airlines during downturns and farms during low commodity price cycles are classic examples of firms in the AVC < P < ATC zone, consciously losing money because operating losses beat shutdown losses.
