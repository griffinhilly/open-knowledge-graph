---
id: oligopoly-and-strategic-behavior
title: Oligopoly and Strategic Behavior
domain: economics
course: microeconomics
prerequisites:
- id: monopoly-microeconomics
  type: hard
- id: monopolistic-competition
  type: soft
builds-toward:
- game-theory-basics-microeconomics
- nash-equilibrium-microeconomics
tags:
- oligopoly
- interdependence
- Cournot
- Bertrand
- collusion
- cartel
stage: formal-systems
status: validated
---

# Oligopoly and Strategic Behavior

## Core Idea
An oligopoly is a market with few firms, where each firm's decisions affect others. Strategic interdependence distinguishes oligopoly from other market structures: the optimal decision for one firm depends on what rivals do. Cartel agreements (like OPEC) can push outcomes toward the monopoly solution, but they are unstable because each member has an incentive to cheat. Cournot competition (firms choose quantities simultaneously) and Bertrand competition (firms choose prices) yield different equilibrium outcomes, illustrating how the mode of competition matters.

## How It's Best Learned
Start with the kinked demand curve as an informal model, then develop Cournot duopoly reaction functions algebraically. The contrast between cartel and Cournot outcomes motivates game theory.

## Common Misconceptions
- Oligopoly is not synonymous with collusion; many oligopolies compete vigorously.
- Students confuse Cournot (quantity) and Bertrand (price) competition; Bertrand with identical goods drives price to MC even with two firms.

## Questions

```yaml
- question: "An OPEC member country is assigned a production quota in a cartel agreement that sets oil output below the competitive level to support a high price. What incentive does each member individually face?"
  type: multiple-choice
  options:
    - "To produce less than their quota, since lower supply increases the cartel price further"
    - "To produce exactly their quota, since deviating would trigger automatic price collapse"
    - "To produce more than their quota, since at the high cartel price each additional unit sold is profitable"
    - "To exit the cartel entirely, since independent producers earn higher profits than cartel members"
  answer: 2
  explanation: "At the elevated cartel price, the marginal revenue from producing one more unit exceeds marginal cost — so each member has a private incentive to expand output beyond their quota. If all members act on this incentive, total output rises and the cartel price collapses. This is the fundamental instability of cartels: the cooperative outcome is profitable collectively but individually defecting is profitable for each member unilaterally. The cartel only survives if members can monitor and punish cheating, or if some enforcement mechanism exists."

- question: "Two firms sell identical products with the same constant marginal cost and compete by setting prices (Bertrand competition). What is the equilibrium outcome?"
  type: multiple-choice
  options:
    - "Both firms split the market equally and price at the monopoly level"
    - "Both firms price at marginal cost — the same outcome as perfect competition"
    - "Firms coordinate on the Cournot equilibrium price to avoid a price war"
    - "The larger firm sets price above MC and the smaller firm follows"
  answer: 1
  explanation: "The Bertrand paradox: if firm A prices above MC, firm B can capture the entire market by undercutting by a penny. Firm A responds by undercutting firm B, and so on until both price at MC. At any price above MC, there is always a profitable deviation — undercut the rival. At MC, neither firm can profitably undercut further (that would mean selling at a loss). The result is the competitive outcome with just two firms, which surprises students who expect oligopoly to sustain prices above MC. This result breaks down with capacity constraints, product differentiation, or switching costs."

- question: "In Cournot competition, adding more firms to the market pushes the equilibrium price toward the competitive level, approaching marginal cost as the number of firms grows large."
  type: true-false
  answer: true
  explanation: "In the Cournot model, each firm's reaction function accounts for rivals' output. With n firms, each firm's market share shrinks, and the total output across all firms increases toward the competitive level as n grows. With two Cournot firms, price is between the monopoly price and MC. With three firms, it falls further. In the limit as n → ∞, the Cournot equilibrium converges to perfect competition. This makes Cournot a useful benchmark for thinking about how industry concentration affects market outcomes."

- question: "Oligopolies always tend toward collusion because collective coordination to restrict output and raise prices is the dominant strategy for every firm in the market."
  type: true-false
  answer: false
  explanation: "Collusion is collectively rational but individually unstable — it is not a dominant strategy for each firm. Each member of a cartel has a private incentive to cheat by producing above their quota at the high cartel price. If all members act on this incentive, the cartel collapses. Many oligopolies compete vigorously rather than colluding; oligopoly is not synonymous with collusion. Strategic interdependence means each firm must consider rivals' responses, but those responses can lead to competitive or cooperative equilibria depending on the mode of competition, the ability to monitor behavior, and whether the game is repeated."

- question: "Why is cartel agreement inherently unstable, and what structural incentive undermines it even when all members prefer the cartel outcome to the competitive one?"
  type: short-answer
  answer: "A cartel elevates price above the competitive level by restricting total output. At that high price, each member's marginal revenue from producing an additional unit exceeds their marginal cost — so each member individually gains by secretly expanding output beyond their quota. But if all members act on this incentive, total output rises and the cartel price falls back toward the competitive level, erasing the collective gain. The cartel is a collective action problem: the individually rational choice (cheat) produces the collectively worst outcome (cartel collapse). It persists only when cheating can be detected and punished."
  explanation: "This is the Prisoners' Dilemma structure applied to oligopoly. Each firm prefers the cartel outcome to competition, but each firm also prefers to cheat while others comply — and compliance while being cheated on is the worst outcome. Absent enforcement, the dominant strategy for each firm is to cheat, producing the competitive equilibrium even though all prefer the monopoly outcome."
```

## Explainer

Your prerequisite on monopoly showed how a single firm with market power chooses output where MR = MC, setting price above marginal cost and generating deadweight loss. Competitive markets sit at the other extreme — price equals MC and DWL disappears. **Oligopoly** occupies the space in between: a market with so few firms that each firm's output or pricing decision materially affects the market price, and therefore affects what rivals will do. This mutual awareness — **strategic interdependence** — is what makes oligopoly different from both monopoly and competition, and why it requires game-theoretic thinking rather than just optimization.

The simplest model is **Cournot duopoly**: two firms each independently choose a quantity to produce, and the market price is then determined by the total quantity supplied. Each firm has a **reaction function** — the profit-maximizing quantity for firm 1 given firm 2's output, and vice versa. The Cournot equilibrium is where the two reaction functions intersect: both firms are simultaneously best-responding to each other. This equilibrium lies between the monopoly outcome (total output too low, price too high) and the competitive outcome (price equals MC). The more firms are added to the Cournot model, the closer the outcome approaches perfect competition — a useful benchmark for thinking about industry structure.

**Bertrand competition** changes only one thing: firms compete on price rather than quantity. The result is dramatic. If two firms sell identical products and have the same constant marginal cost, each has an incentive to undercut the other by a penny to capture the whole market. This undercutting continues until both firms price at marginal cost — the competitive outcome, achieved with just two firms. The "Bertrand paradox" (two firms are enough for competition) resolves in practice because real-world Bertrand competitors have capacity constraints, differentiated products, or switching costs, all of which soften the race to the bottom.

**Cartels** represent the cooperative alternative: firms agree to act collectively as a monopolist, restricting total output and splitting the monopoly profit. An OPEC-style cartel sets production quotas to push price toward the monopoly level. The cartel is self-defeating, however, because each member faces an incentive to produce slightly more than their quota — at the cartel price, selling one extra unit is profitable. If all members cheat, output expands and the cartel collapses. This instability is a recurring feature of oligopoly markets and explains why cartels require enforcement mechanisms (side payments, punishment strategies, or legal backing) to persist. The cartel's internal logic will become the foundation for studying repeated games and cooperation when you reach game theory.
