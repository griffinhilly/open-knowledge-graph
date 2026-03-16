---
id: market-equilibrium
title: Market Equilibrium
domain: economics
course: microeconomics
prerequisites:
- id: supply-and-demand-basics
  type: hard
builds-toward:
- consumer-surplus-microeconomics
- price-controls-and-deadweight-loss
- comparative-statics
tags:
- equilibrium
- market clearing
- price
- surplus
- shortage
stage: abstract-reasoning
status: validated
---

# Market Equilibrium

## Core Idea
Market equilibrium is the price and quantity at which quantity demanded equals quantity supplied, so the market clears. At prices above equilibrium a surplus arises, putting downward pressure on price; at prices below equilibrium a shortage arises, putting upward pressure. The equilibrium price is the market's signal that coordinates decentralized decisions by buyers and sellers. Equilibrium is not static — changes in supply or demand shift it.

## How It's Best Learned
Solve for equilibrium algebraically with linear supply and demand functions, then verify graphically. Work through scenarios where either curve shifts and predict the new equilibrium price and quantity before drawing.

## Common Misconceptions
- Students often treat equilibrium as a permanent state rather than a tendency the market moves toward.
- 'Supply equals demand' is a common shorthand that conflates the curves with quantities — the correct statement is 'quantity supplied equals quantity demanded.'

## Questions

```yaml
- question: "The demand function is Q_d = 100 - 2P and the supply function is Q_s = 4P - 20. What is the equilibrium price?"
  type: multiple-choice
  options: ["$10", "$15", "$20", "$25"]
  answer: 2
  explanation: "Set Q_d = Q_s: 100 - 2P = 4P - 20, so 120 = 6P, giving P = 20. At P = 20, Q = 100 - 2(20) = 60, and Q_s = 4(20) - 20 = 60. Both sides equal 60, confirming the market clears. A common error is to set Q = 0 or to solve only one equation rather than equating both sides."

- question: "Once a market reaches equilibrium, it will remain at that price and quantity unless a government regulation changes the price."
  type: true-false
  answer: false
  explanation: "Equilibrium is a tendency the market moves toward, not a permanent fixed state. Any shift in supply or demand — from changes in consumer income, input costs, technology, tastes, prices of related goods, or expectations — shifts the relevant curve and changes the equilibrium price and quantity. Markets face constant real-world disturbances and are continuously adjusting toward a moving equilibrium."

- question: "Explain why a price above the equilibrium price creates downward pressure on price, using the logic of surpluses and seller incentives."
  type: short-answer
  answer: "At a price above equilibrium, quantity supplied exceeds quantity demanded — a surplus. Sellers cannot move all they have produced. To clear excess inventory, competing sellers cut prices. This downward adjustment continues until quantity supplied equals quantity demanded, driving the price back to equilibrium."
  explanation: "This self-correcting mechanism requires no central authority — it emerges from the decentralized decisions of competing sellers facing unsold goods. The symmetric case (price below equilibrium) creates a shortage, and competing buyers bid prices up. These two pressures converge on the single market-clearing price."
```

## Explainer

Supply and demand curves each represent one side of a market: the demand curve summarizes how much buyers are willing and able to purchase at each price, and the supply curve summarizes how much sellers are willing and able to offer. Market equilibrium is the price where these two schedules are consistent — where the price leads buyers to demand exactly what sellers want to supply, so the market clears. At that price every willing buyer finds a willing seller, and no unsatisfied parties remain.

To find equilibrium algebraically, set quantity demanded equal to quantity supplied and solve for price. With Q_d = 100 - 2P and Q_s = 4P - 20, setting them equal gives 100 - 2P = 4P - 20, so P = 20 and Q = 60. This is the market-clearing price and quantity. Algebraic methods are faster and more precise than reading a graph, and the technique generalizes directly to comparative statics — tracking how the equilibrium changes when a curve shifts.

The stability of equilibrium rests on the surplus-shortage mechanism. Above equilibrium, quantity supplied exceeds quantity demanded: sellers produce more than buyers want at that price, leaving unsold inventory. Competing sellers, unwilling to hold surplus stock, cut prices — driving the market back down. Below equilibrium, quantity demanded exceeds quantity supplied: buyers want more than sellers can provide, creating a shortage. Competing buyers offer higher prices to secure scarce goods, bidding the price back up. These two corrective pressures — downward from surpluses, upward from shortages — converge on the single price where the market clears. No coordination is needed; the mechanism is entirely decentralized.

The most important conceptual point is that equilibrium is a tendency, not a permanent state. Real markets face constant disturbances — shifts in consumer income, changes in input costs, technological improvements, new entrants, changes in the price of substitutes or complements. Each shift moves the equilibrium to a new price and quantity. Developing fluency with this comparative statics reasoning — predicting the direction and magnitude of equilibrium changes when a curve shifts — is the primary skill this topic builds toward.
