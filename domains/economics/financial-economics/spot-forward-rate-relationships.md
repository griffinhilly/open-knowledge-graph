---
id: spot-forward-rate-relationships
title: Spot Rates, Forward Rates, and No-Arbitrage Relationships
domain: economics
course: financial-economics
prerequisites:
- id: interest-rate-term-structure
  type: hard
- id: present-value-and-discounting
  type: soft
builds-toward:
- interest-rate-swaps-mechanics
- covered-and-uncovered-interest-parity
tags:
- interest-rates
- arbitrage
- forward-contracts
- no-arbitrage
stage: formal-systems
status: draft
---

# Spot Rates, Forward Rates, and No-Arbitrage Relationships

## Core Idea
Spot rates are today's interest rates for lending over specified periods, while forward rates are implicit rates for future lending periods derived from the term structure. No-arbitrage relationships lock in mathematical connections: forward rates must be consistent with spot rates to prevent riskless profit opportunities. These relationships form the foundation for pricing all fixed-income instruments.

## Questions

```yaml
- question: "The 1-year spot rate is 4% and the 2-year spot rate is 5%. What is the implied 1-year forward rate starting in one year, f(1,2)?"
  type: multiple-choice
  options:
    - "Approximately 6%, derived from (1.05)² / (1.04) - 1"
    - "4.5%, which is the simple average of the two spot rates"
    - "5%, because the 2-year rate already reflects expectations for year 2"
    - "1%, which is the spread between the two spot rates"
  answer: 0
  explanation: "The no-arbitrage condition requires (1 + s₂)² = (1 + s₁)(1 + f(1,2)). Solving: f(1,2) = (1.05)²/(1.04) - 1 = 1.1025/1.04 - 1 ≈ 6.01%. The intuition is that lending for two years at 5% must produce the same terminal value as lending for one year at 4% and rolling over at the forward rate. If f were only 4.5% (the average), an arbitrageur could exploit the gap by borrowing at the low side and lending at the high side. Option B is the most tempting wrong answer — averaging spot rates is a natural impulse but incorrect because compounding is multiplicative, not additive."

- question: "An investor observes that the implied 1-year forward rate starting in year 1 is 7%, but a broker is offering a one-year loan starting in one year at 8%. Assuming no transaction costs, what should the investor do?"
  type: multiple-choice
  options:
    - "Borrow at the 8% forward contract and lend synthetically using spot rates to lock in a riskless profit"
    - "Lend at the 8% forward contract and borrow synthetically using spot rates to lock in a riskless profit"
    - "Do nothing — forward rates and spot rates can diverge without creating arbitrage"
    - "Invest in the 2-year spot bond since it implies higher total returns"
  answer: 1
  explanation: "When a forward rate in the market (8%) exceeds the no-arbitrage forward rate (7%), you should lend at the high rate and borrow synthetically. Strategy: lend at the offered 8% forward; simultaneously borrow for 2 years at the 2-year spot rate and lend for 1 year at the 1-year spot rate — this synthetic short position costs 7% implied. The difference (8% - 7%) is riskless profit. No-arbitrage logic says this gap cannot persist: arbitrageurs will lend at 8%, driving that rate down until parity is restored. Option C is wrong precisely because the no-arbitrage condition is not merely a tendency — it is an enforced equality in liquid markets."

- question: "Forward rates represent the financial market's unbiased prediction of what future spot rates will actually be."
  type: true-false
  answer: false
  explanation: "False. Forward rates embed expected future spot rates *plus* term premia (compensation for bearing the risk of holding longer-duration instruments) plus convexity adjustments. An upward-sloping yield curve does imply that forward rates exceed current short rates, but this does not mean rates are expected to rise by that full amount — part of the difference compensates for duration risk. Disentangling pure expectations from term premia requires a term structure model with additional assumptions. Using forward rates as pure forecasts systematically overpredicts future short rates in most historical periods precisely because term premia are persistently positive."

- question: "If the 2-year spot rate exceeds the 1-year spot rate, the implied 1-year forward rate starting in year 1 must exceed the 2-year spot rate."
  type: true-false
  answer: true
  explanation: "True. From (1 + s₂)² = (1 + s₁)(1 + f(1,2)), if s₂ > s₁ then the left side grows faster than (1 + s₁)², which forces f(1,2) > s₂. Intuitively: if you earn more by lending for 2 years than 1 year, the implied rate for the second year must be even higher than the 2-year average — otherwise the 2-year advantage wouldn't exist. An upward-sloping spot curve therefore implies forward rates that are above and more steeply rising than the spot curve itself. This is why forward curves always 'overshoot' the spot curve when the yield curve is upward sloping."

- question: "Explain the no-arbitrage condition that ties forward rates to spot rates, and why this relationship must hold in liquid markets."
  type: short-answer
  answer: "The no-arbitrage condition states that lending for n years at the n-year spot rate must produce the same terminal value as a sequence of shorter loans at the corresponding spot and forward rates. For example, lending for 2 years at s₂ must equal lending for 1 year at s₁, then rolling over for a second year at f(1,2): (1+s₂)² = (1+s₁)(1+f(1,2)). If this equality fails, two strategies with identical payoffs have different costs — a free lunch that arbitrageurs would immediately exploit."
  explanation: "In practice, if the forward rate implied by spot rates were lower than an available forward contract, traders would borrow synthetically (via spot rates) at the cheap implied rate and lend at the expensive contract rate, earning riskless profit. This trading pressure pushes prices back toward parity. The key insight is that forward rates are not independently determined — they are fully pinned by spot rates through this compounding relationship. The relationship is mathematically exact, not approximate, which is what makes it a no-arbitrage condition rather than a tendency or approximation."
```

## Explainer

From the term structure of interest rates you know that different maturities carry different yields — the yield curve slopes upward, downward, or lies flat depending on expectations and risk premia. From present value discounting you know how to value a single cash flow by dividing it by an appropriate discount factor. Spot and forward rates give precise names to the discount rates being used and show how they must logically relate to each other.

A **spot rate** s(t) is simply today's rate for lending or borrowing over a specific horizon from now until time t. The 2-year spot rate is the yield on a zero-coupon bond that pays $1 in two years; the 5-year spot rate is the same for five years. These rates are the fundamental building blocks — every coupon bond is priced by discounting each of its cash flows at the spot rate for that cash flow's specific maturity. The yield to maturity is a weighted average of these spot rates, which is why YTM changes even when the issuer's credit quality is unchanged but the shape of the spot curve shifts.

A **forward rate** f(t₁, t₂) is the interest rate agreed upon today for lending that will begin at time t₁ and end at time t₂ — it is a rate for a future period, locked in now. Forward rates are not directly observable in the market; they are *implied* by the relationship between spot rates. The key relationship is the **no-arbitrage condition**: lending for two years at the 2-year spot rate must produce the same terminal value as lending for one year at the 1-year spot rate and then reinvesting for a second year at the 1-year forward rate starting at year one. In formula form: (1 + s₂)² = (1 + s₁)(1 + f(1,2)). If this equality did not hold, an arbitrageur could borrow at the cheap side and lend at the expensive side to earn a riskless profit — the no-arbitrage logic forces the equation to hold exactly.

This connection is what makes forward rates useful for fixed-income pricing and monetary policy analysis. If the yield curve is upward-sloping, the implied forward rates are higher than the current short rate — the curve embeds the expectation (or compensation for risk) that short rates will rise. Central bankers and traders use forward rate curves extracted from Treasury yields to infer market expectations about the path of policy rates. An important caveat: forward rates are not pure forecasts of future spot rates. They bundle together expected future rates, **term premia** (compensation for the uncertainty of holding long-duration instruments), and convexity adjustments. Disentangling these components requires additional model assumptions, which is why interpreting forward curves is more art than arithmetic.
