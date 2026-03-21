---
id: price-elasticity-of-supply
title: Price Elasticity of Supply
domain: economics
course: microeconomics
prerequisites:
- id: supply-and-demand-basics
  type: hard
- id: price-elasticity-of-demand
  type: soft
builds-toward:
- tax-incidence-and-elasticity
- price-controls-and-deadweight-loss
tags:
- elasticity
- supply
- responsiveness
- time horizon
stage: formal-systems
status: validated
---

# Price Elasticity of Supply

## Core Idea
Price elasticity of supply (PES) measures how responsive quantity supplied is to a price change: PES = (% change in Qs) / (% change in P). Supply tends to be more elastic in the long run than the short run because firms have more time to adjust capacity, enter or exit, and change input usage. Perfectly inelastic supply (vertical curve) occurs when output cannot change regardless of price, as with land in a fixed location.

## How It's Best Learned
Compare short-run and long-run supply responses in the same market (e.g., housing). Work through numerical problems and graphical cases including perfectly elastic and perfectly inelastic extremes.

## Common Misconceptions
- Students often assume supply is always elastic or always inelastic rather than recognizing it depends on time horizon and the nature of the good.
- PES is always non-negative (positive sign), unlike PED which is negative — students sometimes apply the absolute-value convention incorrectly.

## Questions

```yaml
- question: "In 2022, a sudden surge in demand for microchips drove prices sharply higher but barely increased chip output. Two years later, new chip factories came online and output expanded substantially. Which statement best explains this pattern?"
  type: multiple-choice
  options:
    - "Microchip supply is perfectly inelastic in both the short and long run, so prices always absorb demand surges"
    - "The demand surge was temporary, which is what causes short-run supply to appear inelastic"
    - "Short-run supply was highly inelastic (limited by fixed capacity), but long-run supply became more elastic as firms expanded production"
    - "Long-run supply is always perfectly elastic in manufacturing, so prices must return to their original level"
  answer: 2
  explanation: "Time horizon is the single most important determinant of supply elasticity. In the short run, chip production was constrained by existing factory capacity and established supply chains — output could not respond meaningfully to higher prices. Over two years, firms invested in new fabs, hired workers, and expanded capacity, allowing a much larger supply response to the same price signals. This is the core lesson: the same market can behave like an inelastic supplier in the short run and an elastic supplier in the long run."

- question: "A government imposes a $10 per-unit tax on a good with perfectly inelastic supply (a vertical supply curve). How is the tax burden distributed between buyers and sellers?"
  type: multiple-choice
  options:
    - "Buyers and sellers each absorb $5 — the tax is always split equally"
    - "Buyers absorb the full $10 because higher costs are always passed on through higher prices"
    - "Sellers absorb the full $10 — the price buyers pay is unchanged, but sellers receive $10 less per unit"
    - "The burden is split in proportion to the ratio of supply elasticity to demand elasticity"
  answer: 2
  explanation: "With perfectly inelastic supply (vertical curve), sellers cannot reduce quantity to avoid the tax — they must sell the same amount regardless of the net price they receive. The market equilibrium quantity is fixed by supply. The pre-tax buyer price is determined by where that fixed quantity meets demand; a tax on sellers shifts their net receipts down by the full $10 without changing the buyer price. Sellers bear the entire burden. This is the extreme case of the general principle: the more inelastic side bears more of the tax. Option D states the general rule, which reduces to option C in this extreme case."

- question: "Price elasticity of supply is always a positive number, unlike price elasticity of demand which is typically negative."
  type: true-false
  answer: true
  explanation: "Supply curves slope upward — as price rises, quantity supplied increases. This means the numerator (% change in quantity supplied) and denominator (% change in price) always have the same sign, making PES always positive or zero. In contrast, demand curves slope downward, so PED is typically negative (though it is often reported as an absolute value). The sign difference reflects the fundamental behavioral difference: higher prices attract more supply but deter more demand."

- question: "A price elasticity of supply of 2.5 means that a 10% price increase causes a 25% decrease in quantity supplied."
  type: true-false
  answer: false
  explanation: "PES = (% change in quantity supplied) / (% change in price). Since supply curves slope upward, a price increase causes an *increase* in quantity supplied, not a decrease. PES = 2.5 means a 10% price increase causes a 25% *increase* in quantity supplied — supply is elastic (responds more than proportionally). A negative PES would imply a backward-bending supply curve, which is not the standard case. This confusion often arises from over-applying the absolute-value convention from price elasticity of demand."

- question: "Explain why the same market can have very different supply elasticities over different time horizons, using a specific example."
  type: short-answer
  answer: "In the short run, firms are constrained by fixed capital — they cannot quickly build new factories, hire and train workers, or secure new supply contracts. So when prices rise, output can only increase within existing capacity, making supply inelastic. In the long run, firms can expand capacity, new firms can enter, and the entire industry can scale up. Housing is a clear example: a demand surge in a desirable city raises prices sharply in the short run (construction is slow, permitting takes time) but eventually triggers new development, making long-run supply more elastic. The same city, the same market — but very different supply responses at different time horizons."
  explanation: "The time-horizon insight generalizes beyond manufacturing. It applies to agricultural goods (planting decisions take seasons), natural resources (oil production requires years of investment), and services (training professionals takes years). In policy terms, this means price controls or taxes have different effects in the short run than the long run — a market that absorbs a policy shock with price changes in the short run may absorb it with quantity changes once supply adjusts."
```

## Explainer

You've already learned price elasticity of demand — how sensitively buyers respond to price changes. Price elasticity of supply is the mirror concept on the seller's side. The formula has the same structure: **PES = (% change in quantity supplied) / (% change in price)**. If price rises 10% and quantity supplied rises 15%, PES = 1.5, meaning supply is **elastic** — producers respond more than proportionally. If quantity supplied only rises 5%, PES = 0.5 and supply is **inelastic**. Unlike PED, PES carries no negative sign: supply curves slope upward, so price and quantity always move together.

The extreme cases anchor your intuition. **Perfectly inelastic supply** (PES = 0) produces a vertical supply curve — quantity is fixed regardless of price. The classic example is land in a specific location: no matter how much you pay, you cannot create more beachfront in Malibu. A sold-out event has perfectly inelastic supply in the short run — no extra tickets exist. At the other extreme, **perfectly elastic supply** (PES = ∞) produces a horizontal supply curve — firms will supply any quantity at exactly the going price, but none below it. This approximates competitive industries where firms are identical and inputs are unlimited.

Time horizon is the single most important determinant of supply elasticity. Consider oil: in the short run, refineries run at capacity and crude oil production can barely change — supply is highly inelastic, so demand spikes translate almost entirely into price spikes. Over years, new drilling projects come online, refinery capacity expands, and alternative fuels develop — supply becomes much more elastic. Housing follows the same pattern: a demand surge in a desirable city sends prices up sharply in the short run (inelastic supply), but eventually triggers new construction that partially absorbs demand (more elastic supply). The same market at two time horizons behaves like two different markets.

PES has a direct application you'll develop in the tax incidence topic: when a tax is imposed on a market, the burden is shared between buyers and sellers in proportion to their relative elasticities. **The more inelastic side bears more of the tax.** If supply is perfectly inelastic (vertical curve), sellers bear the entire tax — they receive a lower net price and can't reduce quantity to avoid it. If supply is perfectly elastic (horizontal curve), sellers pass the entire tax to buyers. Most real markets lie between these extremes, and calculating the precise split requires knowing both PES and PED — another reason why understanding supply elasticity is foundational to policy analysis.
