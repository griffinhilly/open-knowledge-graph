---
id: american-vs-european-options
title: American versus European Options
domain: economics
course: financial-economics
prerequisites:
- id: options-basics-financial
  type: hard
- id: options-payoff-diagrams
  type: hard
builds-toward:
- option-trading-strategies
tags:
- options
- american
- european
- early-exercise
stage: formal-systems
status: validated
---

# American versus European Options

## Core Idea
European options can only be exercised at maturity, while American options can be exercised at any time before expiration. The early exercise feature gives American options greater value, especially calls on dividend-paying stocks and puts when interest rates are high. Closed-form pricing exists only for Europeans; Americans require numerical methods.

## How It's Best Learned
Compare American and European option prices on the same underlying using approximation formulas or binomial trees. Examine when early exercise is optimal (typically just before dividend payments for calls).

## Questions

```yaml
- question: "An American call option on a non-dividend-paying stock has a market price of $5 and intrinsic value (S − K) = $3. An investor exercises immediately to capture the $3. Is this rational?"
  type: multiple-choice
  options:
    - "Yes — capturing certain intrinsic value is always better than holding a risky option"
    - "No — the option trades at $5, so exercising early destroys $2 of value relative to simply selling the option"
    - "Yes — once intrinsic value exceeds the premium originally paid, early exercise is optimal"
    - "No — American calls on non-dividend stocks cannot be exercised early by regulation"
  answer: 1
  explanation: "Early exercise is irrational here because the option is worth more alive ($5) than its intrinsic value ($3). Exercising gives you $3 of value; selling gives you $5. The extra $2 reflects the option's time value — the optionality (protection if the stock falls) plus the time value of delaying the payment of K. The common misconception is conflating 'has intrinsic value' with 'should be exercised.' For non-dividend-paying stocks, an American call is always worth at least its intrinsic value on the open market, making early exercise dominated."

- question: "Under what circumstances is early exercise of an American put option potentially rational, even on a non-dividend-paying stock?"
  type: multiple-choice
  options:
    - "Never — put options should always be held to expiration to maximize optionality"
    - "When the option is deep in the money and interest rates are high, so receiving K now is worth more than the remaining optionality"
    - "When the stock price is rising, to lock in the profit before it reverses"
    - "Only when the put is exactly at-the-money"
  answer: 1
  explanation: "For a deep-in-the-money put, the stock is near zero and intrinsic value is approximately K. At this point, further downside is limited (the stock can't fall below zero), but receiving K immediately earns interest. When interest rates are high, the present value of K received now versus at expiration is significant. The residual optionality (the stock recovering) is worth little since recovery from near-zero is unlikely. The rational investor weighs interest earned against optionality sacrificed."

- question: "An American call option on a non-dividend-paying stock is always worth more than an otherwise identical European call, because the early exercise feature has positive value."
  type: true-false
  answer: false
  explanation: "For non-dividend-paying stocks, early exercise of an American call is never optimal — you always do better by selling the option than by exercising it. Therefore, the early exercise feature has zero value, and American and European calls on non-dividend stocks are priced identically. This is the key insight: having a right that you should never use adds nothing to the option's value."

- question: "American options are always at least as valuable as otherwise identical European options."
  type: true-false
  answer: true
  explanation: "An American option has all the same rights as a European option plus the additional right to exercise early. Having more flexibility cannot decrease value. In cases where early exercise is never optimal (e.g., calls on non-dividend stocks), American and European options are equal in price. In cases where early exercise is sometimes optimal (puts, calls on dividend stocks), the American option is strictly more valuable."

- question: "Explain intuitively why early exercise of a call option on a non-dividend-paying stock is never optimal."
  type: short-answer
  answer: "Exercising early costs you two things: (1) optionality — if the stock later falls below K, holding the option limits your loss to the premium, whereas exercising and owning the stock exposes you to full downside; (2) time value of money — paying K now rather than at expiration forfeits the interest K could have earned. Since both benefits of waiting are lost upon exercise and neither is recovered, a rational investor always prefers to sell the option rather than exercise it. The live option is always worth at least its intrinsic value (S − K) in the market."
  explanation: "The formal proof uses the put-call parity relation to show C ≥ S − Ke^{−rT} > S − K for r > 0. Intuitively: the option gives everything owning the stock gives (upside), plus protection the stock doesn't (limited downside), plus deferred payment of K. Exercising discards the protection and acceleration payment without compensation."
```

## Explainer

From your work on option basics and payoff diagrams, you know that a call option gives the right to buy an asset at the strike price K, and a put gives the right to sell. The key new question here is: does it ever make sense to use that right early, before the option expires? European options remove this choice entirely — you can only exercise at maturity. American options preserve it. Understanding when early exercise is optimal is the heart of this topic.

For a **call option on a non-dividend-paying stock**, the surprising answer is that early exercise is never optimal. Here's the intuition from your knowledge of time value: if you exercise early, you pay K today and receive the stock. But you could instead keep the option alive, let the stock price develop, and only pay K at maturity. By waiting, you retain **optionality** (protection against the stock falling below K) and keep K invested (earning the risk-free rate). A live option is always worth at least as much as its intrinsic value (S − K) for a call. So for non-dividend-paying stocks, American and European calls have the same price — the early exercise feature has zero value.

Dividends change this calculus. When a stock pays a dividend, its price typically drops by roughly the dividend amount on the ex-dividend date. If you hold the option through the dividend date, you miss the dividend payment while the stock price falls, reducing your intrinsic value. An American call holder might rationally exercise just before the ex-dividend date to capture the dividend. This is the primary scenario where early exercise of calls is optimal — the dividend received must exceed the time value sacrificed by exercising early.

For **put options**, early exercise can be rational even without dividends. If the underlying stock crashes to near zero, your put's intrinsic value is approximately K (you can sell a nearly worthless stock for K). Waiting adds risk that intrinsic value could decline if the stock somehow recovers, and costs you the interest you could earn on K if received today. When the interest rate is high and the option is deep in the money, receiving K now is worth more than the residual optionality. This is why American puts are always worth at least as much as European puts, and the premium (the difference) grows with interest rates. Pricing American options requires numerical methods — like binomial trees — because you must evaluate at each node whether immediate exercise beats continuation, a calculation that cannot collapse into a simple closed-form formula.
