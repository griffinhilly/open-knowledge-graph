---
id: input-substitution-elasticity
title: Elasticity of Substitution Between Inputs
domain: economics
course: microeconomics
prerequisites:
- id: production-technology-and-isoquants
  type: hard
builds-toward:
- factor-demands-and-elasticity
tags:
- producer theory
- elasticity
- substitution
stage: formal-systems
status: validated
---

# Elasticity of Substitution Between Inputs

## Core Idea
The elasticity of substitution σ measures how easily a firm can substitute between inputs when their price ratio changes. It quantifies the percentage change in input ratio relative to percentage change in price ratio. σ = 0 means inputs are complements (no substitution), σ = 1 for Cobb-Douglas, σ = ∞ for perfect substitutes. Higher elasticity means firms have more flexibility in factor adjustment.

## Questions

```yaml
- question: "Wages rise sharply in an economy where σ (the elasticity of substitution between labor and capital) is close to zero. What happens to labor's share of total income?"
  type: multiple-choice
  options:
    - "Labor's share falls, because firms substitute toward capital and employ fewer workers"
    - "Labor's share is unchanged, because σ = 1 guarantees constant factor shares"
    - "Labor's share rises, because firms cannot substitute away from labor so they pay the higher wage with little reduction in employment"
    - "Labor's share falls, because higher wages make production unprofitable and firms exit the market"
  answer: 2
  explanation: "When σ is low (near zero), inputs are near-complements — the firm cannot easily replace labor with capital even when wages spike. So the firm continues using roughly the same amount of labor, paying the now-higher wage. Labor's income share (wL/pY) rises because w goes up while L barely changes. This is the counterintuitive income-distribution result: the factor that is harder to substitute away from actually gains income share when its price rises. With σ = 1 (Cobb-Douglas), factor shares are constant. With σ > 1, firms substitute so aggressively that labor's share falls when wages rise."

- question: "What does the shape of the isoquant reveal about the elasticity of substitution σ?"
  type: multiple-choice
  options:
    - "Steeper isoquants indicate higher σ because they show a larger MRTS"
    - "More curved (L-shaped) isoquants indicate lower σ because inputs are harder to substitute; flatter (nearly straight) isoquants indicate higher σ"
    - "The shape of the isoquant is unrelated to σ; only the position of the isoquant matters"
    - "A right-angled isoquant corresponds to σ = ∞ because inputs are perfect complements"
  answer: 1
  explanation: "Isoquant curvature directly measures how quickly the MRTS changes as you move along the isoquant — that is, how readily you can trade one input for another while holding output fixed. A sharply curved (L-shaped, Leontief) isoquant means the MRTS changes abruptly: a small move along the isoquant requires a large change in the input ratio, so inputs are poor substitutes (σ ≈ 0). A nearly straight isoquant means the MRTS barely changes: inputs can be freely swapped at a nearly constant rate (σ → ∞). σ = 1 (Cobb-Douglas) produces the intermediate smoothly curved shape where factor shares remain constant."

- question: "A higher elasticity of substitution means firms can more easily replace one input with another when their relative prices change."
  type: true-false
  answer: true
  explanation: "This is the direct interpretation of σ: it measures the percentage change in the input ratio (K/L) per one percent change in the input price ratio (w/r). High σ means a small relative price change induces a large rebalancing of the input mix — firms substitute freely. Low σ means the input mix barely changes despite large price swings — firms are locked into a fixed ratio. This sensitivity has major implications for how wage increases or capital cost changes transmit into production costs, employment levels, and income distribution."

- question: "In a Cobb-Douglas economy (σ = 1), if wages rise while the rental rate of capital stays constant, labor's share of national income increases."
  type: true-false
  answer: false
  explanation: "The defining property of Cobb-Douglas production (σ = 1) is that factor shares are constant regardless of input prices. When wages rise, firms substitute toward capital enough to keep wL/pY unchanged — employment falls proportionally with the wage increase, so the total wage bill stays the same share of output. This constancy of factor shares was a major reason Cobb-Douglas became the workhorse of macroeconomics: Kaldor's stylized facts observed roughly stable labor shares over long periods, consistent with σ ≈ 1 in aggregate."

- question: "Why does a low elasticity of substitution (σ < 1) imply that a wage increase raises labor's share of national income, even though higher wages make labor more expensive?"
  type: short-answer
  answer: "When σ is low, firms cannot easily replace labor with capital — the isoquants are highly curved (near-Leontief). Even as wages rise, the firm must continue using roughly the same amount of labor to maintain output. The quantity of labor (L) decreases only slightly. Since labor's income share is wL/pY, and w rises while L barely falls, the numerator (wL) increases and so does labor's share. The wage increase cannot be 'absorbed' by substitution, so it flows directly into a larger share of income going to workers."
  explanation: "This result is often counterintuitive: we expect expensive inputs to lose ground, but in a low-substitution world, losing ground requires substitution, and substitution is precisely what's unavailable. The economic story is about market power of a factor: when you cannot be replaced, your price increases translate into income gains. This has policy implications — in sectors where labor and capital are poor substitutes (low σ), minimum wage increases may raise labor's income share without large employment losses."
```

## Explainer

From your study of isoquants, you know that the slope of an isoquant at any point — the **marginal rate of technical substitution** (MRTS) — tells you how many units of one input a firm can trade for one unit of another while keeping output constant. A steeply curved isoquant means the MRTS changes quickly as you move along it: inputs are hard to substitute. A gently curved isoquant (nearly straight) means the MRTS stays roughly constant: inputs are nearly perfect substitutes. The **elasticity of substitution** σ turns that geometric intuition into a number.

Formally, σ = % change in (K/L) ÷ % change in (w/r), where w is the wage and r is the rental rate of capital. It asks: if the relative price of labor rises by 1%, how much do firms shift their input mix away from labor and toward capital? A high σ means firms respond aggressively — they substitute readily. A low σ means firms are stuck using roughly the same mix no matter what prices do. The formula connects isoquant curvature to observed factor demand behavior: flatter isoquants → less curvature → higher σ → more substitution.

The three benchmark cases illuminate the range. When σ = 0, the isoquants are **right-angled (Leontief)**: inputs must be used in fixed proportions like two tires per bicycle axle. No amount of price change induces substitution because the inputs are perfect complements. When σ = ∞, the isoquants are **straight lines**: inputs are perfect substitutes and the firm uses entirely whichever is cheaper, switching completely if the price ratio crosses a threshold. The **Cobb-Douglas** case at σ = 1 sits in between: factor shares of income (wL/pY and rK/pY) remain constant as input prices change, a prediction that has been historically useful for modeling aggregate production.

Why does σ matter economically? When σ is high, labor and capital markets are tightly linked: a wage increase can be substantially offset by substituting toward capital (automation). When σ is low, wage increases translate more directly into higher costs, because the firm has little flexibility to rebalance. For policy analysis, σ governs how income is distributed between workers and capital owners as factor prices change: with Cobb-Douglas (σ = 1), factor shares are fixed; with σ < 1, the relatively more expensive factor sees its share *rise* (because quantity can't adjust much); with σ > 1, the more expensive factor sees its share *fall* as firms successfully substitute away from it.
