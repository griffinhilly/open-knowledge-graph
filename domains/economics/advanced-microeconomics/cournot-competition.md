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
stage: expert
status: draft
---

# Cournot Competition: Quantity Competition in Oligopoly

## Core Idea
Firms simultaneously choose quantities of a homogeneous product; price clears the market. Each firm's profit depends on its output and rivals' outputs. Cournot-Nash equilibrium occurs where each firm optimizes given rivals' quantities. As competitors increase, equilibrium price approaches marginal cost. Cournot yields prices between monopoly and perfect competition.

## Questions

```yaml
- question: "In a Cournot duopoly, each firm produces more than its share of the joint-monopoly output. Why doesn't each firm simply cut back to the monopoly level to maximize industry profits?"
  type: multiple-choice
  options:
    - "Firms are legally prohibited from coordinating production decisions"
    - "Each firm, taking the rival's output as given, finds that increasing its own output raises its individual profit — it ignores the negative externality its extra output imposes on the rival's revenue, so individual rationality leads each firm to overproduce relative to the joint optimum"
    - "The Cournot equilibrium quantity is actually less than the monopoly quantity, not more"
    - "Firms would cut back, but the Cournot model assumes they cannot observe each other's output"
  answer: 1
  explanation: "This is the core insight of Cournot competition. The joint monopoly outcome requires each firm to internalize the harm its output inflicts on the rival's price — but in a non-cooperative game, each firm only cares about its own profit. From firm 1's perspective, producing more than its 'monopoly share' increases its own revenue (selling more units, even at a slightly lower price), and the price reduction also hurts firm 2 — which firm 1 ignores. This externality is why the Cournot equilibrium produces more total output and lower prices than a monopoly, even without any legal prohibition on coordination."

- question: "As the number of identical Cournot competitors in a market increases from 2 to a large number N, what happens to the equilibrium price?"
  type: multiple-choice
  options:
    - "It rises toward the monopoly price, since more firms coordinate more effectively"
    - "It remains constant, since each firm adjusts output proportionally to maintain price"
    - "It falls toward marginal cost — the competitive outcome — as each firm's market power shrinks"
    - "It falls to zero because firms engage in price wars to capture market share"
  answer: 2
  explanation: "With N identical Cournot firms, each firm produces (a − c)/[(N+1)b] where P = a − bQ and c is marginal cost. As N → ∞, individual output shrinks but total industry output Q = N(a−c)/[(N+1)b] → (a−c)/b, which is the competitive quantity. Price converges to marginal cost. This convergence result is powerful because it shows perfect competition as the limiting case of Cournot oligopoly as market structure approaches atomistic — the two models are not separate but connected by N."

- question: "In Cournot competition, a firm's best-response quantity decreases when it expects its rival to produce more output."
  type: true-false
  answer: true
  explanation: "The best-response (reaction) function is downward sloping: if the rival increases output, total supply rises, driving down market price. This shrinks the residual demand facing our firm, lowering the profit-maximizing quantity for our firm. Setting MR = MC with higher rival output yields a lower optimal own-output. This strategic substitutability — where rivals' quantities and own quantities move in opposite directions — is the defining feature of Cournot-style quantity competition. (Contrast with Bertrand competition, where strategies are also substitutes, but in price space.)"

- question: "Cournot competition and perfect competition are completely separate theoretical models with no mathematical relationship between them."
  type: true-false
  answer: false
  explanation: "The Cournot model converges to the perfectly competitive outcome as the number of competitors grows large. With N firms, each producing (a−c)/[(N+1)b], the equilibrium price approaches marginal cost as N → ∞, and each firm's individual market share shrinks toward zero. This convergence means perfect competition is the limiting case of Cournot oligopoly — not a separate model. Understanding this relationship reveals why market structure matters: duopoly, tight oligopoly, and competitive markets differ in degree, not in kind."

- question: "In Cournot competition, why does each firm restrict output below the competitive level (earning positive profit), yet still produce more than its share of the joint-monopoly output? What game-theoretic logic drives this specific outcome?"
  type: short-answer
  answer: "Each firm restricts output below the competitive level because at the competitive quantity, price equals marginal cost and profit is zero — producing slightly less raises price above MC and generates positive profit margin. But each firm also produces more than the monopoly share because the monopoly outcome requires internalizing the harm your output inflicts on the rival's revenue — something a non-cooperative firm has no incentive to do. Each firm's best response to the rival's output is to produce the quantity that maximizes its own profit given that rival output, ignoring the external cost it imposes. The Nash equilibrium — where both best-response functions intersect — sits between these extremes because both forces operate simultaneously."
  explanation: "The positive-profit side: competitive markets earn zero because P = MC; any quantity restriction from that level creates a positive margin. The over-production-relative-to-monopoly side: the joint optimum requires each firm to act as if it were a monopolist over the whole market, which means restricting output to the point where it would actually benefit the rival more than itself. Without binding commitment or communication, each firm defects from this joint optimum — the classic prisoner's dilemma structure of oligopoly."
```

## Explainer

From oligopoly theory, you know that a small number of firms interact strategically — each firm's optimal decision depends on what rivals do. Cournot competition gives this intuition its first precise mathematical formulation. The setup is clean: two or more firms produce an identical product, each simultaneously chooses how much to produce, and the market price is determined by total industry output through a downward-sloping demand curve. Each firm's profit equals price times its own quantity minus its costs — but since price depends on everyone's combined output, each firm must anticipate what rivals will produce.

The key analytical tool is the **best-response function** (also called the reaction function). For each possible quantity that firm 2 might produce, firm 1 calculates its profit-maximizing quantity by setting marginal revenue equal to marginal cost — the same profit-maximization logic from basic microeconomics, except that marginal revenue now depends on the rival's output. With linear demand and constant marginal costs, the best-response function is a downward-sloping line: when firm 2 produces more, the residual demand facing firm 1 shrinks, so firm 1 optimally produces less. Firm 2's best-response function is symmetric. The **Cournot-Nash equilibrium** is the intersection of these two reaction functions — the pair of quantities where each firm is best-responding to the other, and neither wants to change.

Consider a concrete example. Suppose market demand is P = 100 − Q (where Q is total quantity), both firms have marginal cost of 10, and there are no fixed costs. A monopolist would produce 45 units at a price of 55, earning profit of 2,025. In the Cournot duopoly, each firm produces 30 units (total 60), price falls to 40, and each earns profit of 900 — industry profit is 1,800, less than the monopoly profit of 2,025. The competitive outcome would be Q = 90, P = 10, with zero profit. Cournot sits between these extremes. Each firm restricts output relative to the competitive level (earning positive profit) but produces more than the joint-monopoly quantity (because each firm ignores the negative externality its output imposes on the rival's revenue).

This framework scales naturally. With N identical firms, each produces less individually but the industry produces more in total. As N grows, the Cournot equilibrium converges smoothly to the perfectly competitive outcome — price approaches marginal cost and individual market shares shrink toward zero. This convergence result is powerful: it shows perfect competition as the limiting case of oligopoly rather than a separate model. Cournot competition also provides the foundation for richer models: Stackelberg competition adds sequential timing, Bertrand competition switches the strategic variable to prices, and collusion models ask whether firms can sustain the joint monopoly outcome through repeated interaction.
