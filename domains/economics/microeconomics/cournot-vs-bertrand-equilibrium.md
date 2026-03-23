---
id: cournot-vs-bertrand-equilibrium
title: Cournot versus Bertrand Competition Models
domain: economics
course: microeconomics
prerequisites:
- id: cournot-competition
  type: hard
- id: bertrand-competition
  type: hard
tags:
- oligopoly
- game theory
- competition models
stage: advanced
status: validated
---

# Cournot versus Bertrand Competition Models

## Core Idea
Cournot equilibrium (quantity competition) yields prices above marginal cost and positive profit even in long run, with convergence to competition as firm numbers increase. Bertrand equilibrium (price competition) yields P = MC and zero profit with as few as two firms if goods are homogeneous; differentiated goods allow positive profit. The empirical relevance depends on strategic variable (capacity vs. price setting) and product nature.

## Questions

```yaml
- question: "Two firms produce identical products in an oligopoly. A student argues: 'With only two sellers, each has substantial market power — prices should settle well above marginal cost.' Under which competition model is the student's intuition correct?"
  type: multiple-choice
  options:
    - "Bertrand competition with homogeneous goods"
    - "Bertrand competition with differentiated goods only"
    - "Cournot competition — both firms produce positive profit even with two competitors"
    - "Neither — two firms always drive prices to marginal cost"
  answer: 2
  explanation: "In Cournot competition, firms choose quantities simultaneously, and the resulting equilibrium price is above marginal cost even with just two firms. The student's intuition about market power is correct *for Cournot*. Under Bertrand competition with homogeneous goods, however, the student is wrong: two price-setting firms with unlimited capacity are sufficient to drive price to marginal cost (the Bertrand paradox). The distinction between models matters enormously for the policy and welfare analysis of oligopoly."

- question: "Two airlines fly the same route, offering identical service and matching each other's prices in real time. Neither has capacity constraints. Based on the Cournot vs. Bertrand framework, what equilibrium do we expect?"
  type: multiple-choice
  options:
    - "Prices stabilize at the Cournot level — slightly above marginal cost"
    - "Prices fall to marginal cost and economic profits approach zero"
    - "The airlines collude implicitly, maintaining prices near the monopoly level"
    - "The larger airline sets prices and the smaller one follows"
  answer: 1
  explanation: "This scenario fits Bertrand competition: homogeneous goods (identical service), simultaneous price-setting, and no capacity constraints. The Bertrand logic applies — either airline can steal the entire market by undercutting by a penny. The race to the bottom continues until P ≈ MC. Collusion (option C) is a separate equilibrium requiring coordination mechanisms; the Bertrand framework predicts competitive pricing absent coordination. Cournot would apply if the airlines competed by choosing flight frequency or capacity rather than price."

- question: "In Bertrand competition with homogeneous goods, two firms produce the same equilibrium outcome as a perfectly competitive market: price equals marginal cost and economic profits are zero."
  type: true-false
  answer: true
  explanation: "This is the Bertrand paradox — the counterintuitive result that duopoly (two firms) can yield the competitive outcome when firms set prices for identical goods. The logic is airtight: as long as both firms price above MC, either can profitably undercut and capture the whole market. This mutual incentive continues until P = MC, at which point no profitable undercutting is possible. The 'paradox' is that it seems like two firms should have more market power than a competitive fringe with many firms — but under Bertrand price competition with homogeneous goods, they do not."

- question: "As the number of firms in a Cournot oligopoly increases toward infinity, equilibrium price remains above marginal cost because each firm individually retains some market power."
  type: true-false
  answer: false
  explanation: "As the number of Cournot competitors grows, each firm's output share falls and its individual market power diminishes. In the limit as N → ∞, Cournot equilibrium converges to the perfectly competitive outcome: price approaches marginal cost and economic profit approaches zero. The Cournot model thus interpolates between monopoly (N = 1) and perfect competition (N → ∞), with market power declining continuously with more firms. The claim that price 'remains above MC' regardless of firm count is incorrect."

- question: "Explain the Kreps-Scheinkman theorem and what it reveals about why the distinction between Cournot and Bertrand competition ultimately depends on the *timing* of strategic commitments rather than on whether firms technically 'set prices' or 'set quantities.'"
  type: short-answer
  answer: "The Kreps-Scheinkman theorem shows that if firms first choose capacity (a quantity commitment) and then compete on price, the equilibrium outcome matches Cournot — not Bertrand. Capacity is costly and slow to change, so it acts as a commitment device. Once capacity is set, a firm cannot profitably undercut to steal the whole market because it cannot serve it. The Bertrand undercutting logic breaks down when firms are capacity-constrained. The deeper insight is that the equilibrium depends on which commitment comes first in the game's timing: capacity commitments made before price-setting produce Cournot outcomes, while pure simultaneous price competition without capacity constraints produces Bertrand outcomes."
  explanation: "The Kreps-Scheinkman result is important because real industries often involve both kinds of competition — firms invest in capacity long-run and then price short-run. The theorem explains why industries that 'seem' to compete on price (Bertrand) can still maintain positive profits: the capacity decisions made earlier effectively constrain the subsequent pricing game. This is why identifying the *first-mover commitment* (capacity, contracts, inventory) is the key empirical question when applying these models."
```

## Explainer

You've now studied Cournot and Bertrand as separate models. The deeper question is: why do they produce such radically different predictions, and how do you know which to apply in a given industry? The answer lies in what firms actually compete over and how quickly they can respond to rivals.

In Cournot competition, firms choose **quantities** and the market price emerges from total supply. When you choose output, you're implicitly committing to a production run before knowing what your rival will produce — think of firms that must build factories or hire workers before the selling season. Your best response to a rival's output is to produce less if they produce more (the best-response functions slope downward), and the equilibrium lands where both are best-responding simultaneously. The result is a price *above* marginal cost: both firms exercise some market power, and both earn economic profit. Crucially, this profit doesn't disappear as you add firms — it shrinks, but the logic remains. With two Cournot firms, price is well above MC; with ten, you're close to competitive; with infinitely many, you reach the competitive outcome. Cournot is the theory of capacity-constrained industries where commitments are made before prices are set.

In Bertrand competition, firms choose **prices** simultaneously, and consumers buy from whichever firm charges less. This transforms the strategic landscape completely. Suppose both firms charge above MC. Either firm can steal the entire market by undercutting by a penny — and if it can serve the whole market, that's profitable. So the rival undercuts back. This race to the bottom continues until *P = MC*, at which point neither firm can profitably undercut further. **The Bertrand paradox** is the result: two firms are sufficient to eliminate all market power and drive profit to zero, the same outcome as perfect competition. The paradox dissolves as soon as you add product differentiation — if your product isn't identical to the rival's, undercutting doesn't steal the whole market, and equilibrium price rises above MC.

The practical question is which model fits an industry. Bertrand tends to apply when: goods are homogeneous (or close), capacity is unlimited, and firms can match prices quickly. Commodity exchanges, airline pricing in overlapping routes, and gasoline retail near competitors are all closer to Bertrand dynamics. Cournot tends to apply when: capacity is costly and slow to adjust, firms make production commitments in advance, and quantity decisions are more visible than price decisions. Steel production, crude oil extraction, and pharmaceutical manufacturing are closer to Cournot. The **Kreps-Scheinkman theorem** formalizes this intuition: if firms first choose capacity (Cournot style) and then compete on price (Bertrand style), the equilibrium outcome matches Cournot — because capacity constraints prevent the Bertrand undercutting race from reaching MC. This is why the strategic variable that matters most is whichever commitment comes *first* in the game's timing.
