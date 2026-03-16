---
id: comparative-statics
title: Comparative Statics
domain: economics
course: microeconomics
prerequisites:
- id: market-equilibrium
  type: hard
- id: implicit-differentiation
  type: soft
- id: partial-derivatives
  type: soft
builds-toward:
- price-elasticity-of-demand
- consumer-surplus-microeconomics
tags:
- comparative statics
- equilibrium shifts
- supply shifts
- demand shifts
stage: abstract-reasoning
status: validated
---

# Comparative Statics

## Core Idea
Comparative statics analyzes how an equilibrium outcome changes when an exogenous parameter changes, holding everything else constant. By shifting the supply or demand curve and comparing the new equilibrium to the old one, we can predict the direction of change in both price and quantity. When both curves shift simultaneously, the effect on one variable is determinate but the effect on the other is ambiguous without knowing the magnitudes. This method is one of the most widely used tools in applied economics.

## How It's Best Learned
Drill through scenarios systematically: single shift left, single shift right, double shifts in same and opposite directions. Practicing the 'ambiguous' cases — where you can determine price but not quantity or vice versa — solidifies the logic.

## Common Misconceptions
- Students often try to predict both price and quantity even in ambiguous double-shift cases.
- Forgetting that the ceteris paribus assumption applies: only one parameter changes at a time in a comparative-statics exercise.

## Explainer

Comparative statics is the economist's version of a controlled experiment on paper. You already know from market equilibrium that supply and demand intersect to determine a price and quantity. Comparative statics asks: if one exogenous condition changes — a tax, a new technology, a shift in consumer preferences — how does the equilibrium respond? The method is purely logical: hold everything else fixed (ceteris paribus), move the appropriate curve, and read off the new equilibrium.

The procedure for a single-curve shift is mechanical. Identify which curve is affected and in which direction. Demand shifts right when something makes buyers want more at every price — rising income for a normal good, a price increase in a substitute, favorable news. Supply shifts right when something makes production cheaper — lower input costs, better technology, a subsidy. Once the shift is drawn, the new intersection reveals unambiguous predictions: a rightward demand shift raises both price and quantity; a leftward supply shift raises price but lowers quantity. There are four single-shift cases, each deterministic.

The interesting complexity arises when both curves shift simultaneously. Here the **indeterminacy principle** becomes essential: when both supply and demand shift, you can always determine the sign of the change in one variable but not both, unless you know the relative magnitudes. For example, if demand rises and supply also rises, quantity certainly increases — both shifts push quantity up. But price is ambiguous: the demand increase pushes price up while the supply increase pushes it down; which effect dominates depends on the sizes. Drawing both possible outcomes (large demand shift vs. small demand shift) and noting that price is "ambiguous" is the correct answer, not an evasion.

The connection to calculus is direct for those with partial derivatives in their toolkit. If equilibrium price P* is determined implicitly by the condition Q^d(P, α) = Q^s(P, β) — where α is a demand parameter and β is a supply parameter — then dP*/dα equals the partial derivative of demand with respect to α divided by the net slope term. This is implicit differentiation applied to equilibrium conditions. But the intuition always precedes the algebra: draw the shift, identify what happens to the intersection, and only then formalize. The diagram is the argument; the math confirms it.
