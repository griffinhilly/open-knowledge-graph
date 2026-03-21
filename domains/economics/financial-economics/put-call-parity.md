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

## Questions

```yaml
- question: "You observe that C − P > S − PV(K) for a European option pair with the same strike and expiration. What is the correct arbitrage response?"
  type: multiple-choice
  options:
    - "Buy the call and sell the put — the call is underpriced relative to the put"
    - "Sell the call, buy the put, buy the stock, and borrow PV(K) — sell the expensive portfolio, buy the cheap one"
    - "Do nothing — small deviations from parity are always within the no-arbitrage band"
    - "Buy the put and sell the call — the put is underpriced"
  answer: 1
  explanation: "If C − P > S − PV(K), then C + PV(K) > S + P: Portfolio A (call + bond) costs more than Portfolio B (stock + put), but both have identical payoffs. The arbitrage is to sell the expensive portfolio A (sell the call, borrow PV(K)) and buy the cheap portfolio B (buy the stock, buy the put). This locks in a riskless profit equal to the parity gap. Competition among arbitrageurs drives prices back toward equality."

- question: "Why does put-call parity hold exactly for European options but only approximately for American options?"
  type: multiple-choice
  options:
    - "American options have larger bid-ask spreads, introducing pricing errors"
    - "European options can be exercised at any time; American options can only be exercised at expiration"
    - "American put options may have value from early exercise that is not captured by the European parity formula"
    - "Put-call parity applies equally to both — the distinction is only theoretical"
  answer: 2
  explanation: "American options can be exercised before expiration. An American put may be worth exercising early — particularly when the stock has fallen sharply and the time value of waiting is costly. This early-exercise premium adds value to the American put beyond what European parity predicts, breaking the equality. The no-arbitrage portfolios underlying parity assume the option is held to expiration; early exercise invalidates that assumption. Note also that option B has the direction of European vs. American backwards — European options can only be exercised at expiration."

- question: "If two portfolios produce identical cash flows in every possible future state, they must have the same price today."
  type: true-false
  answer: true
  explanation: "This is the law of one price — the foundation of no-arbitrage pricing. If the portfolios had different prices, you could buy the cheaper one and sell the more expensive one, earning a riskless profit today with zero net future obligation. Such an arbitrage opportunity cannot persist in a rational market. Put-call parity is derived directly from this principle: Portfolio A (call + bond) and Portfolio B (stock + put) both pay max(S_T, K) at expiration, so they must cost the same to construct today."

- question: "Put-call parity implies that a call and a put with the same strike and expiration must have the same price."
  type: true-false
  answer: false
  explanation: "Put-call parity states C − P = S − PV(K), not C = P. Calls and puts have equal prices only in the special case where S = PV(K) — roughly when the stock price equals the discounted strike, which can occur for at-the-money options with very short time to expiration. In general, a call (which profits from price increases) and a put (which profits from price decreases) have different prices. Parity constrains their relationship, not their equality."

- question: "Explain the no-arbitrage logic behind put-call parity: why must C − P equal S − PV(K)?"
  type: short-answer
  answer: "Construct two portfolios: (A) buy a call + invest PV(K) in risk-free bonds; (B) buy the stock + buy a put. Portfolio A pays max(S_T, K) at expiration in all states: if S_T > K, exercise the call; if S_T ≤ K, the bond pays K. Portfolio B also pays max(S_T, K): if S_T > K, hold the stock; if S_T ≤ K, exercise the put. Identical payoffs in all states require identical prices: C + PV(K) = S + P, which rearranges to C − P = S − PV(K)."
  explanation: "The derivation requires no assumptions about how stock prices move — only the no-arbitrage condition. This makes put-call parity a model-free result. Any deviation from parity reveals an explicit arbitrage: buy the cheap portfolio, sell the expensive one, and collect a riskless profit at construction. The parity relationship also enables synthetic replication: knowing any three of {C, P, S, PV(K)}, you can determine the fourth."
```

## Explainer

You've spent time with options payoff diagrams and the basics of how puts and calls work. Put-call parity makes a striking claim: knowing the price of a call option, the stock price, the strike price, and the risk-free rate, you can determine exactly what the put option must be worth — no assumptions about return distributions needed. The relationship C - P = S - PV(K) holds by **no-arbitrage**: if two portfolios have identical payoffs in every possible future state, they must have the same price today. If they didn't, you could buy the cheap one and sell the expensive one, locking in a riskless profit.

To see why C - P = S - PV(K), construct two portfolios and compare their payoffs at expiration. **Portfolio A**: buy a call (cost C) and invest PV(K) in risk-free bonds (which grow to K at expiration). If S_T > K, you exercise the call for a gain of S_T - K and collect K from the bond, ending with S_T. If S_T ≤ K, the call expires worthless but you still hold K from the bond. In both cases, Portfolio A pays max(S_T, K). **Portfolio B**: buy the stock (cost S) and buy a put (cost P). If S_T > K, the put expires worthless and you hold stock worth S_T. If S_T ≤ K, you exercise the put, selling the stock for K. Portfolio B also pays max(S_T, K). Since both portfolios deliver identical payoffs in every state, no-arbitrage requires C + PV(K) = S + P, which rearranges to C - P = S - PV(K).

The practical implications are significant. Put-call parity lets you **synthetically replicate** any of the four instruments using the other three. Want to own a put without buying one? Buy a call, invest PV(K) in bonds, and short the stock. Want to replicate a call? Buy the stock, buy a put, and borrow PV(K). Traders use these synthetic positions when one leg is mispriced or unavailable. More broadly, put-call parity defines the fair relationship between put and call prices: a significant deviation in real market quotes immediately reveals the arbitrage trade.

Deviations from exact parity do occur in practice, and understanding why is illuminating. The relationship holds exactly only for **European options** on non-dividend-paying stocks. For **American options**, the right to early exercise adds value to puts in ways that break the equality — put-call parity becomes an inequality for American options. Dividends also matter: when the stock pays a dividend before expiration, the stock price falls on the ex-dividend date, benefiting puts and hurting calls, which shifts the parity relationship. Transaction costs and bid-ask spreads create a band around the theoretical parity within which small deviations are not profitably arbitrageable. These nuances — dividends, early exercise, and frictions — are exactly what more advanced options pricing models must handle beyond the basic parity relationship.
