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
status: draft
---

# Cournot versus Bertrand Competition Models

## Core Idea
Cournot equilibrium (quantity competition) yields prices above marginal cost and positive profit even in long run, with convergence to competition as firm numbers increase. Bertrand equilibrium (price competition) yields P = MC and zero profit with as few as two firms if goods are homogeneous; differentiated goods allow positive profit. The empirical relevance depends on strategic variable (capacity vs. price setting) and product nature.

## Explainer

You've now studied Cournot and Bertrand as separate models. The deeper question is: why do they produce such radically different predictions, and how do you know which to apply in a given industry? The answer lies in what firms actually compete over and how quickly they can respond to rivals.

In Cournot competition, firms choose **quantities** and the market price emerges from total supply. When you choose output, you're implicitly committing to a production run before knowing what your rival will produce — think of firms that must build factories or hire workers before the selling season. Your best response to a rival's output is to produce less if they produce more (the best-response functions slope downward), and the equilibrium lands where both are best-responding simultaneously. The result is a price *above* marginal cost: both firms exercise some market power, and both earn economic profit. Crucially, this profit doesn't disappear as you add firms — it shrinks, but the logic remains. With two Cournot firms, price is well above MC; with ten, you're close to competitive; with infinitely many, you reach the competitive outcome. Cournot is the theory of capacity-constrained industries where commitments are made before prices are set.

In Bertrand competition, firms choose **prices** simultaneously, and consumers buy from whichever firm charges less. This transforms the strategic landscape completely. Suppose both firms charge above MC. Either firm can steal the entire market by undercutting by a penny — and if it can serve the whole market, that's profitable. So the rival undercuts back. This race to the bottom continues until *P = MC*, at which point neither firm can profitably undercut further. **The Bertrand paradox** is the result: two firms are sufficient to eliminate all market power and drive profit to zero, the same outcome as perfect competition. The paradox dissolves as soon as you add product differentiation — if your product isn't identical to the rival's, undercutting doesn't steal the whole market, and equilibrium price rises above MC.

The practical question is which model fits an industry. Bertrand tends to apply when: goods are homogeneous (or close), capacity is unlimited, and firms can match prices quickly. Commodity exchanges, airline pricing in overlapping routes, and gasoline retail near competitors are all closer to Bertrand dynamics. Cournot tends to apply when: capacity is costly and slow to adjust, firms make production commitments in advance, and quantity decisions are more visible than price decisions. Steel production, crude oil extraction, and pharmaceutical manufacturing are closer to Cournot. The **Kreps-Scheinkman theorem** formalizes this intuition: if firms first choose capacity (Cournot style) and then compete on price (Bertrand style), the equilibrium outcome matches Cournot — because capacity constraints prevent the Bertrand undercutting race from reaching MC. This is why the strategic variable that matters most is whichever commitment comes *first* in the game's timing.
