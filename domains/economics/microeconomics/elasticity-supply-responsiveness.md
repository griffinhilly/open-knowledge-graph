---
id: elasticity-supply-responsiveness
title: Price Elasticity of Supply
domain: economics
course: microeconomics
prerequisites:
- id: supply-and-demand-basics
  type: hard
builds-toward:
- tax-incidence-and-elasticity
- supply-curve-individual-firm
tags:
- elasticity
- supply
- producer-responsiveness
stage: formal-systems
status: draft
---

# Price Elasticity of Supply

## Core Idea
Price elasticity of supply measures how responsively quantity supplied changes when price changes, calculated as the percentage change in quantity supplied divided by the percentage change in price. Elastic supply (ε > 1) indicates firms can readily adjust production; inelastic supply (ε < 1) indicates production constraints. Supply elasticity depends on input availability, production time, and technological flexibility.

## How It's Best Learned
Compare elasticity across different industries and time horizons (short-run vs. long-run). Examine agricultural products (seasonal constraints on supply elasticity) against manufactured goods.

## Common Misconceptions
- Assuming all goods have the same supply elasticity—elasticity varies widely based on production flexibility.
- Confusing supply elasticity with the slope of the supply curve.
- Ignoring time horizons—supply is generally more elastic in the long run.

## Questions

```yaml
- question: "A price increase of 10% causes quantity supplied to increase by 4%. What is the price elasticity of supply, and how is it classified?"
  type: multiple-choice
  options:
    - "PES = 2.5; elastic supply"
    - "PES = 0.4; inelastic supply"
    - "PES = 0.4; elastic supply"
    - "PES = 6.0; perfectly elastic supply"
  answer: 1
  explanation: "PES = (%ΔQs) / (%ΔP) = 4% / 10% = 0.4. Since PES < 1, supply is inelastic — producers increase quantity by a smaller proportion than the price increase. A PES of 0.4 indicates significant constraints on production expansion, such as limited inputs, fixed capacity, or biological production limits. The classification threshold is PES = 1 (unit elastic): above 1 is elastic, below 1 is inelastic."

- question: "Two supply curves pass through the same market equilibrium point. Curve A is steeper than Curve B. Which statement correctly distinguishes their elasticities?"
  type: multiple-choice
  options:
    - "Curve A is more elastic because a steeper slope signals stronger producer willingness to supply"
    - "Both curves have the same elasticity at the equilibrium point since they pass through the same price-quantity combination"
    - "Curve B is more elastic because a given price change produces a larger percentage change in quantity supplied"
    - "Elasticity cannot be compared without knowing whether the curves are linear"
  answer: 2
  explanation: "Slope and elasticity are related but not equivalent. Slope measures absolute changes (ΔP/ΔQ); elasticity measures proportional changes (%ΔQs/%ΔP). At the same price-quantity point, a steeper supply curve (smaller ΔQs for a given ΔP) implies a lower percentage change in quantity for a given percentage price change — making it less elastic. A flatter curve (Curve B) allows more quantity response per unit price change, making it more elastic at that point."

- question: "In most industries, supply is more elastic in the long run than in the short run."
  type: true-false
  answer: true
  explanation: "Time horizon is the dominant determinant of supply elasticity. In the short run, firms are constrained by fixed capital — you cannot build a new factory in a week, and existing capacity is a hard limit on output. In the long run, firms can build new plants, hire more workers, and new firms can enter the industry, making total supply much more responsive to price changes. Housing is the canonical example: in the short run supply is very inelastic (construction takes time), but over years, supply expands substantially in response to sustained high prices."

- question: "If a good has inelastic supply, a large increase in demand will raise its price only slightly, because producers cannot expand output easily."
  type: true-false
  answer: false
  explanation: "This reverses the relationship. Inelastic supply means producers *cannot* quickly expand output — they have limited capacity, specialized inputs, or biological constraints. When demand surges and supply cannot respond proportionally, the price increase is *larger*, not smaller. A market with elastic supply can absorb a demand shock by expanding output, keeping prices relatively stable. It is elastic supply that limits price increases; inelastic supply amplifies them."

- question: "Why does the time horizon matter so much for supply elasticity? Use a real-world example to illustrate how the same good can have very different supply elasticities depending on the time frame."
  type: short-answer
  answer: "Time horizon matters because supply elasticity depends on how quickly firms can adjust their production capacity — and capital adjustments take time. In the short run, firms work with fixed plant, equipment, and sometimes fixed inputs (like farmland or licensed venues), so output cannot change much regardless of price. In the long run, new plants can be built, new firms can enter, and input constraints can be resolved. Housing illustrates this clearly: in the short run, a city's housing supply is nearly fixed (construction takes 1-3 years), so a sudden demand surge drives prices up sharply. Over 5-10 years, developers respond to those high prices with new construction, and supply expands — the same market that was inelastic in the short run becomes moderately elastic over a decade."
  explanation: "The same good, same market, but two very different elasticities at different time scales. This is why economists distinguish short-run and long-run supply curves, and why policy effects look very different depending on the time horizon being analyzed."
```

## Explainer

You already know that supply curves slope upward — higher prices bring more quantity supplied. But the supply curve alone doesn't tell you how much more. A steep supply curve and a shallow one both slope upward, yet they represent very different realities. **Price elasticity of supply** (PES) gives the proportional answer: if price rises by 1%, by what percentage does quantity supplied change? The formula is PES = (% change in Qs) / (% change in P). A PES of 2 means a 10% price increase brings a 20% increase in quantity supplied — **elastic supply**. A PES of 0.4 means the same price increase only brings a 4% increase — **inelastic supply**.

The distinction matters because it tells you how markets actually respond to shocks. Imagine a drought destroys half the wheat crop. Supply shifts left, pushing prices up. If wheat supply is elastic in the long run, the high prices quickly pull new land into cultivation and attract more farmers — prices come back down. If supply is inelastic (fixed farmland, long growing seasons), prices stay elevated for years. Whether a market self-corrects quickly or stays disrupted depends entirely on supply elasticity.

Three determinants drive supply elasticity. First, **input availability**: if a firm can hire workers, buy materials, and rent machines on short notice, it can scale output quickly — elastic supply. If inputs are specialized or scarce, expansion is slow and costly. Second, **production time**: agricultural goods face biological constraints — you can't harvest corn faster by paying more. Manufactured goods can usually be produced in more flexible quantities. Third, **spare capacity**: a factory running at 50% capacity can easily raise output if prices rise; one running at 98% cannot.

**Time horizon** is the dominant determinant for most industries. In the short run, firms work with fixed capital — you can't build a new plant in a week. Short-run supply is relatively inelastic. In the long run, new plants can be built, new firms can enter, and the entire industry expands. Long-run supply is more elastic. Housing is the classic example: in the short run, you can't create new housing stock quickly, so a demand surge sends prices up sharply. Over years, developers respond, new construction materializes, and prices moderate. The same market, the same concept, two very different elasticities at different time scales.
