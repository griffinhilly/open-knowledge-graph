---
id: collusion-cartel-stability
title: Collusion, Cartels, and Stability
domain: economics
course: advanced-microeconomics
prerequisites:
- id: cournot-quantity-competition
  type: hard
- id: nash-equilibrium-microeconomics
  type: hard
tags:
- industrial-organization
- collusion
- repeated-games
stage: advanced
status: draft
---

# Collusion, Cartels, and Stability

## Core Idea
Cartels are agreements among competitors to restrict output and elevate price toward monopoly levels, sharing monopoly profit. Collusion is unstable because each firm has incentive to cheat by undercutting the agreed price. Sustainability requires credible punishment (grim trigger: permanent reversion to Cournot) and sufficient future profit weight, with higher discount rates destabilizing collusion.

## Explainer

From Cournot competition, you know that oligopolists who independently choose quantities end up at a Nash equilibrium where industry profits are lower than monopoly profits — competition dissipates some of the surplus. This creates an obvious temptation: what if firms agree to collectively restrict output to the monopoly level and split the larger pie? This is the logic behind **cartels**, and it immediately raises the central question of this topic: why don't all oligopolists collude, and why do cartels so often fall apart?

The instability comes directly from the structure of the Cournot game. Suppose two firms agree to each produce half the monopoly quantity. At this restricted output, the market price is high. But each firm, taking the other's restricted output as given, finds it profitable to **cheat** — to secretly produce more than its agreed share. The cheating firm captures extra sales at a still-high price (since the other firm is still restricting output), earning more than its share of monopoly profits. This is the same logic as the prisoner's dilemma: mutual cooperation (collusion) is jointly optimal, but individual defection is privately optimal. In a one-shot game, cheating is the dominant strategy and collusion unravels.

The resolution lies in **repeated interaction**. If firms compete period after period indefinitely, they can sustain collusion using **trigger strategies**: cooperate as long as everyone cooperates, but if anyone cheats, revert permanently to the Cournot-Nash equilibrium (the **grim trigger**). The cheater gains a one-period windfall from extra output but loses the stream of future collusive profits, receiving only Cournot profits forever after. Whether collusion holds depends on the **discount factor** (δ). The critical condition is that the present value of continued collusive profits must exceed the one-time cheating gain plus the discounted stream of punishment profits. This yields a minimum discount factor below which collusion is unsustainable — impatient firms (high discount rates, low δ) cannot maintain cartels because the immediate temptation outweighs distant future losses.

Several real-world factors map onto this framework. More firms make collusion harder — each firm's share of monopoly profit shrinks while the temptation to cheat remains large. Demand fluctuations create problems because firms cannot easily distinguish a rival's cheating from a genuine demand decline (the **Green-Porter** model of imperfect monitoring). Asymmetric costs make agreement on output shares contentious. Antitrust enforcement raises the cost of collusion by adding legal penalties. OPEC illustrates every element: members periodically agree to output quotas, individual members regularly exceed them, and the cartel's effectiveness varies with how patient members are and how well they can monitor each other's production.
