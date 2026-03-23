---
id: game-theory-strategic-behavior-nash
title: 'Game Theory: Strategic Behavior and Nash Equilibrium'
domain: economics
course: microeconomics
prerequisites:
- id: game-theory-basics-microeconomics
  type: hard
- id: nash-equilibrium-microeconomics
  type: hard
builds-toward:
- cournot-competition
- bertrand-competition
tags:
- game-theory
- strategic-interaction
- equilibrium
stage: advanced
status: validated
---

# Game Theory: Strategic Behavior and Nash Equilibrium

## Core Idea
Game theory models strategic interaction when each player's outcome depends on others' actions. A Nash equilibrium is a strategy profile where no player can improve by unilateral deviation. In oligopolies, firms choose quantities (Cournot) or prices (Bertrand), leading to different equilibrium outcomes. Game theory explains why oligopolists earn profits between competition and monopoly levels.

## How It's Best Learned
Solve simple games (2×2 matrices). Find dominant strategies, Nash equilibria. Compare equilibrium outcomes to monopoly and competition benchmarks.

## Common Misconceptions
- Nash equilibrium is optimal for society (it's individually rational but may be collectively suboptimal; e.g., prisoner's dilemma).
- There is always a unique Nash equilibrium (some games have multiple equilibria or none in pure strategies).

## Questions

```yaml
- question: "Two competing firms in an oligopoly each earn $10M if both restrict output, $15M if one defects while the other restricts, and $6M if both defect. What is the Nash equilibrium?"
  type: multiple-choice
  options:
    - "Both firms restrict output, earning $10M each — collusion is stable because both earn more"
    - "One firm restricts and the other defects, since the defecting firm earns the most"
    - "Both firms defect, earning $6M each — each firm prefers to defect regardless of what the rival does"
    - "Firms alternate between restricting and defecting to maximize long-run profits"
  answer: 2
  explanation: "This is the prisoner's dilemma structure. Check both firms' incentives: if Firm B restricts, Firm A earns $15M by defecting vs. $10M by restricting — defect. If Firm B defects, Firm A earns $6M by defecting vs. nothing by restricting alone — defect. Defecting is a dominant strategy for both firms. The Nash equilibrium (both defect, $6M each) is individually stable — neither firm can unilaterally improve by switching — but collectively inferior to the ($10M, $10M) cooperative outcome. This is precisely why cartels are unstable: each member has a unilateral incentive to cheat."

- question: "In a market for identical products with constant marginal costs, two firms compete on price rather than quantity. What is the Nash equilibrium price?"
  type: multiple-choice
  options:
    - "Above marginal cost, since with only two firms each has market power and can charge a markup"
    - "Equal to marginal cost, with both firms earning zero economic profit — the competitive outcome"
    - "Below marginal cost temporarily, until one firm exits and the survivor raises price"
    - "The same as the Cournot outcome, since market power depends on the number of firms, not the strategy variable"
  answer: 1
  explanation: "This is the Bertrand paradox. With homogeneous products, any price above marginal cost is not a Nash equilibrium: whichever firm charges a tiny bit less captures the entire market. Each firm undercuts the other until both hit marginal cost, where further undercutting would mean selling at a loss. Just two firms competing on price with identical goods produce the competitive outcome — zero economic profit. This contrasts sharply with Cournot, where two firms earn positive markups. The strategy variable (price vs. quantity) fundamentally shapes outcomes."

- question: "A Nash equilibrium requires that the outcome be efficient — meaning no player could be made better off without making another player worse off."
  type: true-false
  answer: false
  explanation: "Nash equilibrium requires only that no *single* player can improve by unilateral deviation, given what others are doing. It says nothing about efficiency. The prisoner's dilemma Nash equilibrium leaves both players worse off than the cooperative outcome — it is inefficient. Oligopoly Nash equilibria produce less output than the competitive outcome, creating deadweight loss. Nash equilibrium is a stability concept (self-enforcing), not an optimality concept (welfare-maximizing)."

- question: "A price-fixing cartel agreement where all firms produce the monopoly-level output collectively is not a Nash equilibrium of the one-shot game, because each firm has a unilateral incentive to expand output beyond its cartel quota."
  type: true-false
  answer: true
  explanation: "Correct. At the monopoly output level, the market price is above each firm's marginal cost, so any single firm can increase profit by slightly expanding output and selling more units at a price still above MC. Since every firm faces this same incentive, the monopoly output allocation is not self-enforcing — no firm is playing a best response. The Nash equilibrium (e.g., Cournot) involves more total output than the monopoly optimum, which is why cartels require binding enforcement mechanisms or repeated-game cooperation to be sustained."

- question: "Why do two firms competing on price with identical products earn zero economic profit at Nash equilibrium, while two firms competing on quantity earn positive profits?"
  type: short-answer
  answer: "In Bertrand competition, any price above marginal cost invites the rival to undercut by a penny and capture the entire market. This undercutting continues until both firms price at marginal cost, where no further profitable undercutting is possible. In Cournot competition, firms commit to quantities and price adjusts to clear the market — each firm's best response is to produce less than the competitive quantity, and at the Nash equilibrium both are earning markups. The strategy variable changes the nature of the undercutting dynamic: price competition eliminates all rents with just two firms, while quantity competition preserves partial market power."
  explanation: "This is the Bertrand paradox: market structure (two firms) does not guarantee market power if the competition is in prices. The key is that price competition is fundamentally more aggressive — a small price cut captures the entire market discontinuously, while a small quantity increase does not. Understanding which variable firms effectively commit to (capacity, production runs, or listed price) is crucial for predicting whether real-world industries look more Cournot or Bertrand."
```

## Explainer

Game theory's central insight is that your best choice depends on what others do — and they know that, and you know they know that. This mutual dependency is what makes strategic situations fundamentally different from ordinary optimization. In a competitive market, each firm is so small it ignores rivals; but in an oligopoly with a few large firms, each firm's output decision directly affects the market price and therefore its rivals' profits. The framework for analyzing this is the **strategic game**: a set of players, a set of strategies available to each, and a payoff function mapping every combination of strategies to outcomes for each player.

A **Nash equilibrium** is a self-reinforcing outcome: given what everyone else is doing, no single player benefits from switching strategies unilaterally. It doesn't require communication — it's a state of mutual best responses. The prisoner's dilemma illustrates why Nash equilibrium is individually rational but potentially collectively inefficient. Two suspects, unable to communicate, each choose between confessing and staying silent. The Nash equilibrium (both confess) leaves both worse off than if they'd cooperated (both stayed silent), but it's stable because each player, taking the other's choice as fixed, strictly prefers to confess. This logic applies directly to oligopoly: firms would collectively earn more by colluding on monopoly output, but each firm has an individual incentive to undercut the cartel, pushing the equilibrium toward higher output and lower prices than the monopoly outcome.

In the **Cournot model**, firms simultaneously choose quantities. Each firm's **best response** is the profit-maximizing output given the rival's choice, yielding a best-response function. The Nash equilibrium is the intersection of these functions — the point where each firm is simultaneously on its own best-response curve. The Cournot outcome sits between competition (P = MC) and monopoly: firms exercise market power, but rivalry prevents full monopoly pricing. In the **Bertrand model**, firms compete on price with identical goods. The equilibrium is striking: with homogeneous products and constant marginal costs, both firms price at MC and earn zero economic profit — the competitive outcome emerges with just two firms, because any price above MC invites the rival to undercut by a penny and capture the entire market.

The Cournot vs. Bertrand distinction matters for real industries. When capacity is costly to change quickly (airlines, steel mills), quantity competition better describes behavior and Cournot predicts intermediate markups. When goods are homogeneous and prices adjust easily (retail, online markets), Bertrand's logic dominates and margins are thin. These two models show how the strategy variable firms compete on — quantity vs. price — fundamentally shapes market outcomes, even holding the number of firms fixed.
