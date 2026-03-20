---
id: tax-incidence-and-elasticity
title: Tax Incidence and Elasticity
domain: economics
course: microeconomics
prerequisites:
- id: market-equilibrium
  type: hard
- id: price-elasticity-of-demand
  type: hard
- id: price-elasticity-of-supply
  type: hard
builds-toward:
- price-controls-and-deadweight-loss
- externalities-and-market-failure
tags:
- tax incidence
- burden
- elasticity
- wedge
stage: formal-systems
status: validated
---

# Tax Incidence and Elasticity

## Core Idea
Tax incidence refers to who ultimately bears the economic burden of a tax, regardless of who legally pays it. The burden is shared between buyers and sellers, and the split is determined by relative elasticities: the more inelastic side bears a larger share of the tax. A per-unit tax creates a wedge between the price buyers pay and the price sellers receive, reducing the equilibrium quantity and generating deadweight loss. The legal incidence (who sends the check to the government) is irrelevant to the economic incidence.

## How It's Best Learned
Draw supply-and-demand diagrams showing the tax wedge, then verify algebraically. Compare a tax on buyers vs. a tax on sellers to demonstrate that the economic outcome — and burden sharing — is identical regardless of legal incidence.

## Common Misconceptions
- Students frequently assume that whoever pays the tax to the government bears all the burden; this ignores behavioral responses.
- When demand is perfectly inelastic, buyers bear 100% of the tax — students find this counterintuitive and need worked examples to internalize it.

## Explainer

You know from your study of market equilibrium that price is determined by supply and demand, not by legislation. Tax incidence exploits this insight: the government can legally require *sellers* to remit a per-unit tax, but economic forces determine how much of that burden actually falls on sellers versus buyers. The mechanism is the **tax wedge** — a fixed gap driven between the price buyers pay (P_b) and the price sellers receive (P_s), with P_b − P_s = t (the tax per unit). The equilibrium is found by asking: at what quantity does the demand curve (evaluated at P_b) equal the supply curve (evaluated at P_s), with the wedge t between them?

The key insight is that whoever is more **inelastic** — less able or willing to adjust quantity in response to price changes — bears more of the burden. Imagine demand is perfectly inelastic: buyers need exactly Q* units regardless of price (insulin is the classic example). When a tax raises the price buyers pay, quantity doesn't fall. Sellers still sell Q*, just at a price t higher. The entire tax burden lands on buyers because they have no option to exit the market. Contrast this with perfectly elastic demand: buyers will buy any amount at the original price P* but nothing above it. A tax that raises the buyer's price above P* causes all buyers to leave. To prevent this, sellers must absorb the entire tax, keeping the buyer price at P* by accepting P* − t for themselves. The burden shifts entirely to sellers.

The precise formula captures this logic: buyers bear a fraction e_S / (e_S + |e_D|) of the tax, and sellers bear e_D / (e_S + |e_D|), where e_S is the price elasticity of supply and |e_D| is the absolute value of the price elasticity of demand. When supply is relatively elastic and demand is relatively inelastic (as with many necessities), buyers bear most of the burden. When demand is relatively elastic (luxury goods with close substitutes) and supply is inelastic (specialized factors), sellers bear most.

A crucial and often surprising result is that **legal incidence is irrelevant to economic incidence**. Whether the tax is formally collected from buyers or sellers, the equilibrium price wedge — and the burden split — is identical. If a $5 gas tax is levied on gas stations rather than drivers, gas stations will raise pump prices by close to the same amount as if the tax had been levied directly on drivers. The supply and demand curves haven't changed; only who writes the check to the government has changed. This symmetry is counterintuitive but follows directly from equilibrium logic: any per-unit tax creates the same wedge regardless of who formally remits it. The policy implication is significant — designing a tax to fall "on corporations" instead of consumers may change the optics without changing who actually bears the burden.
