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

## Explainer

You already know from profit maximization that a firm produces where MR = MC — specifically, P = MC for a perfectly competitive firm. But that rule only tells you the *best output to produce given you're producing at all*. Shutdown and breakeven analysis asks the prior question: should the firm be producing anything at all?

The answer turns on a concept you may not have formalized before: the distinction between **fixed costs** and **variable costs**, and specifically the irreversibility of fixed costs in the short run. Suppose you run a bakery. Your lease payment is due whether you bake anything or not. Your flour and labor costs only arise if you actually bake. Fixed costs are **sunk** in the short run — already committed, not recoverable by shutting down. Variable costs are avoidable — you don't incur them if you produce zero.

This asymmetry drives the shutdown decision. If a firm shuts down, its revenue is zero and its loss equals its fixed costs. If it operates, its revenue is P × Q and its loss (if any) is P × Q − TC = P × Q − TVC − TFC. The firm prefers to operate when its operating loss is smaller than its shutdown loss — that is, when P × Q > TVC, or equivalently when P > AVC. The firm covers its variable costs and contributes something toward fixed costs. Even losing money is better than losing *more* money. The **short-run shutdown point** is therefore P = AVC (minimum of the AVC curve). Below this price, the firm cannot even cover operating costs and is better off idle.

The **breakeven point** is a separate condition: P = ATC (minimum of the ATC curve). At this price, total revenue exactly equals total cost, including fixed costs. Economic profit is zero. Above this price, the firm earns positive economic profit; below it (but above AVC), the firm is operating at a loss but still better off than shutting down. This creates three distinct regions: (1) P > ATC — operate profitably; (2) AVC < P < ATC — operate at a loss, but it beats shutting down; (3) P < AVC — shut down.

The long-run version is cleaner because there are no sunk costs. In the long run, a firm can exit the industry entirely, recovering all resources for alternative uses. There are no fixed costs to absorb. The exit condition becomes simply P < LRAC: if the firm cannot cover all costs, it should exit. The distinction between short-run shutdown (comparing to AVC) and long-run exit (comparing to LRAC) explains why you sometimes observe firms operating at a loss in the short run — they are waiting to see if prices recover before committing to the irreversible decision to exit. Airlines during downturns and farms during low commodity price cycles are classic examples of firms in the AVC < P < ATC zone, consciously losing money because operating losses beat shutdown losses.
