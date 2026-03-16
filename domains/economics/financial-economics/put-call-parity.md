---
id: put-call-parity
title: Put-Call Parity
domain: economics
course: financial-economics
prerequisites:
- id: options-basics-financial
  type: hard
- id: options-payoff-diagrams
  type: hard
builds-toward:
- option-greeks-and-sensitivity
- option-trading-strategies
tags:
- options
- parity
- arbitrage
stage: formal-systems
status: draft
---

# Put-Call Parity

## Core Idea
Put-call parity is the fundamental relationship stating that for European options: C - P = S - PV(K), where C is the call price, P is the put price, S is the stock price, and K is the strike price. This relationship prevents arbitrage and is essential for option pricing, synthetic replication, and understanding the relative values of puts and calls.

## How It's Best Learned
Verify put-call parity with real option quotes on the same underlying and strike, identifying when deviations occur and what arbitrage transactions would exploit them.

## Common Misconceptions
- Put-call parity holds for American options (it only holds exactly for European options; Americans have additional value from early exercise).
- The parity relationship is always perfectly observed (transaction costs, bid-ask spreads, and dividend timing create small deviations).

## Explainer

You've spent time with options payoff diagrams and the basics of how puts and calls work. Put-call parity makes a striking claim: knowing the price of a call option, the stock price, the strike price, and the risk-free rate, you can determine exactly what the put option must be worth — no assumptions about return distributions needed. The relationship C - P = S - PV(K) holds by **no-arbitrage**: if two portfolios have identical payoffs in every possible future state, they must have the same price today. If they didn't, you could buy the cheap one and sell the expensive one, locking in a riskless profit.

To see why C - P = S - PV(K), construct two portfolios and compare their payoffs at expiration. **Portfolio A**: buy a call (cost C) and invest PV(K) in risk-free bonds (which grow to K at expiration). If S_T > K, you exercise the call for a gain of S_T - K and collect K from the bond, ending with S_T. If S_T ≤ K, the call expires worthless but you still hold K from the bond. In both cases, Portfolio A pays max(S_T, K). **Portfolio B**: buy the stock (cost S) and buy a put (cost P). If S_T > K, the put expires worthless and you hold stock worth S_T. If S_T ≤ K, you exercise the put, selling the stock for K. Portfolio B also pays max(S_T, K). Since both portfolios deliver identical payoffs in every state, no-arbitrage requires C + PV(K) = S + P, which rearranges to C - P = S - PV(K).

The practical implications are significant. Put-call parity lets you **synthetically replicate** any of the four instruments using the other three. Want to own a put without buying one? Buy a call, invest PV(K) in bonds, and short the stock. Want to replicate a call? Buy the stock, buy a put, and borrow PV(K). Traders use these synthetic positions when one leg is mispriced or unavailable. More broadly, put-call parity defines the fair relationship between put and call prices: a significant deviation in real market quotes immediately reveals the arbitrage trade.

Deviations from exact parity do occur in practice, and understanding why is illuminating. The relationship holds exactly only for **European options** on non-dividend-paying stocks. For **American options**, the right to early exercise adds value to puts in ways that break the equality — put-call parity becomes an inequality for American options. Dividends also matter: when the stock pays a dividend before expiration, the stock price falls on the ex-dividend date, benefiting puts and hurting calls, which shifts the parity relationship. Transaction costs and bid-ask spreads create a band around the theoretical parity within which small deviations are not profitably arbitrageable. These nuances — dividends, early exercise, and frictions — are exactly what more advanced options pricing models must handle beyond the basic parity relationship.
