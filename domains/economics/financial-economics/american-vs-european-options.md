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
status: draft
---

# American versus European Options

## Core Idea
European options can only be exercised at maturity, while American options can be exercised at any time before expiration. The early exercise feature gives American options greater value, especially calls on dividend-paying stocks and puts when interest rates are high. Closed-form pricing exists only for Europeans; Americans require numerical methods.

## How It's Best Learned
Compare American and European option prices on the same underlying using approximation formulas or binomial trees. Examine when early exercise is optimal (typically just before dividend payments for calls).

## Explainer

From your work on option basics and payoff diagrams, you know that a call option gives the right to buy an asset at the strike price K, and a put gives the right to sell. The key new question here is: does it ever make sense to use that right early, before the option expires? European options remove this choice entirely — you can only exercise at maturity. American options preserve it. Understanding when early exercise is optimal is the heart of this topic.

For a **call option on a non-dividend-paying stock**, the surprising answer is that early exercise is never optimal. Here's the intuition from your knowledge of time value: if you exercise early, you pay K today and receive the stock. But you could instead keep the option alive, let the stock price develop, and only pay K at maturity. By waiting, you retain **optionality** (protection against the stock falling below K) and keep K invested (earning the risk-free rate). A live option is always worth at least as much as its intrinsic value (S − K) for a call. So for non-dividend-paying stocks, American and European calls have the same price — the early exercise feature has zero value.

Dividends change this calculus. When a stock pays a dividend, its price typically drops by roughly the dividend amount on the ex-dividend date. If you hold the option through the dividend date, you miss the dividend payment while the stock price falls, reducing your intrinsic value. An American call holder might rationally exercise just before the ex-dividend date to capture the dividend. This is the primary scenario where early exercise of calls is optimal — the dividend received must exceed the time value sacrificed by exercising early.

For **put options**, early exercise can be rational even without dividends. If the underlying stock crashes to near zero, your put's intrinsic value is approximately K (you can sell a nearly worthless stock for K). Waiting adds risk that intrinsic value could decline if the stock somehow recovers, and costs you the interest you could earn on K if received today. When the interest rate is high and the option is deep in the money, receiving K now is worth more than the residual optionality. This is why American puts are always worth at least as much as European puts, and the premium (the difference) grows with interest rates. Pricing American options requires numerical methods — like binomial trees — because you must evaluate at each node whether immediate exercise beats continuation, a calculation that cannot collapse into a simple closed-form formula.
