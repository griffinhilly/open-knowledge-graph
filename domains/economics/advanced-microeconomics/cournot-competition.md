---
id: cournot-competition
title: 'Cournot Competition: Quantity Competition in Oligopoly'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: oligopoly-and-strategic-behavior
  type: hard
- id: profit-maximization-microeconomics
  type: soft
- id: constrained-optimization
  type: soft
- id: optimization-multivariable-basics
  type: soft
builds-toward:
- bertrand-competition
- stackelberg-competition
tags:
- industrial-organization
- oligopoly
stage: advanced
status: draft
---

# Cournot Competition: Quantity Competition in Oligopoly

## Core Idea
Firms simultaneously choose quantities of a homogeneous product; price clears the market. Each firm's profit depends on its output and rivals' outputs. Cournot-Nash equilibrium occurs where each firm optimizes given rivals' quantities. As competitors increase, equilibrium price approaches marginal cost. Cournot yields prices between monopoly and perfect competition.

## Explainer

From oligopoly theory, you know that a small number of firms interact strategically — each firm's optimal decision depends on what rivals do. Cournot competition gives this intuition its first precise mathematical formulation. The setup is clean: two or more firms produce an identical product, each simultaneously chooses how much to produce, and the market price is determined by total industry output through a downward-sloping demand curve. Each firm's profit equals price times its own quantity minus its costs — but since price depends on everyone's combined output, each firm must anticipate what rivals will produce.

The key analytical tool is the **best-response function** (also called the reaction function). For each possible quantity that firm 2 might produce, firm 1 calculates its profit-maximizing quantity by setting marginal revenue equal to marginal cost — the same profit-maximization logic from basic microeconomics, except that marginal revenue now depends on the rival's output. With linear demand and constant marginal costs, the best-response function is a downward-sloping line: when firm 2 produces more, the residual demand facing firm 1 shrinks, so firm 1 optimally produces less. Firm 2's best-response function is symmetric. The **Cournot-Nash equilibrium** is the intersection of these two reaction functions — the pair of quantities where each firm is best-responding to the other, and neither wants to change.

Consider a concrete example. Suppose market demand is P = 100 − Q (where Q is total quantity), both firms have marginal cost of 10, and there are no fixed costs. A monopolist would produce 45 units at a price of 55, earning profit of 2,025. In the Cournot duopoly, each firm produces 30 units (total 60), price falls to 40, and each earns profit of 900 — industry profit is 1,800, less than the monopoly profit of 2,025. The competitive outcome would be Q = 90, P = 10, with zero profit. Cournot sits between these extremes. Each firm restricts output relative to the competitive level (earning positive profit) but produces more than the joint-monopoly quantity (because each firm ignores the negative externality its output imposes on the rival's revenue).

This framework scales naturally. With N identical firms, each produces less individually but the industry produces more in total. As N grows, the Cournot equilibrium converges smoothly to the perfectly competitive outcome — price approaches marginal cost and individual market shares shrink toward zero. This convergence result is powerful: it shows perfect competition as the limiting case of oligopoly rather than a separate model. Cournot competition also provides the foundation for richer models: Stackelberg competition adds sequential timing, Bertrand competition switches the strategic variable to prices, and collusion models ask whether firms can sustain the joint monopoly outcome through repeated interaction.
