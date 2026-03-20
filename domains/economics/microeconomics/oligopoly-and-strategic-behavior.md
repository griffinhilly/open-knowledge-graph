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

## Explainer

Your prerequisite on monopoly showed how a single firm with market power chooses output where MR = MC, setting price above marginal cost and generating deadweight loss. Competitive markets sit at the other extreme — price equals MC and DWL disappears. **Oligopoly** occupies the space in between: a market with so few firms that each firm's output or pricing decision materially affects the market price, and therefore affects what rivals will do. This mutual awareness — **strategic interdependence** — is what makes oligopoly different from both monopoly and competition, and why it requires game-theoretic thinking rather than just optimization.

The simplest model is **Cournot duopoly**: two firms each independently choose a quantity to produce, and the market price is then determined by the total quantity supplied. Each firm has a **reaction function** — the profit-maximizing quantity for firm 1 given firm 2's output, and vice versa. The Cournot equilibrium is where the two reaction functions intersect: both firms are simultaneously best-responding to each other. This equilibrium lies between the monopoly outcome (total output too low, price too high) and the competitive outcome (price equals MC). The more firms are added to the Cournot model, the closer the outcome approaches perfect competition — a useful benchmark for thinking about industry structure.

**Bertrand competition** changes only one thing: firms compete on price rather than quantity. The result is dramatic. If two firms sell identical products and have the same constant marginal cost, each has an incentive to undercut the other by a penny to capture the whole market. This undercutting continues until both firms price at marginal cost — the competitive outcome, achieved with just two firms. The "Bertrand paradox" (two firms are enough for competition) resolves in practice because real-world Bertrand competitors have capacity constraints, differentiated products, or switching costs, all of which soften the race to the bottom.

**Cartels** represent the cooperative alternative: firms agree to act collectively as a monopolist, restricting total output and splitting the monopoly profit. An OPEC-style cartel sets production quotas to push price toward the monopoly level. The cartel is self-defeating, however, because each member faces an incentive to produce slightly more than their quota — at the cartel price, selling one extra unit is profitable. If all members cheat, output expands and the cartel collapses. This instability is a recurring feature of oligopoly markets and explains why cartels require enforcement mechanisms (side payments, punishment strategies, or legal backing) to persist. The cartel's internal logic will become the foundation for studying repeated games and cooperation when you reach game theory.
