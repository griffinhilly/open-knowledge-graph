---
id: nominal-rigidities-sticky-prices
title: Nominal Rigidities and Sticky Prices
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: monopolistic-competition
  type: hard
builds-toward:
- calvo-pricing-model
tags:
- price-adjustment
- frictions
- monetary-non-neutrality
stage: expert
status: draft
---

# Nominal Rigidities and Sticky Prices

## Core Idea
Nominal price rigidities—including explicit contracts, menu costs, information constraints, and coordination frictions—prevent prices from adjusting instantly to changes in demand or costs. When prices are sticky, monetary shocks cannot be fully offset by proportional price increases, allowing money to have real short-run effects on output and employment. Understanding the sources, magnitude, and duration of price adjustment frictions is central to New Keynesian models and monetary policy analysis.

## Questions

```yaml
- question: "A central bank unexpectedly increases the money supply by 5%. If all prices in the economy were perfectly flexible, what would happen to real output?"
  type: multiple-choice
  options:
    - "Real output would rise by 5% in the short run as firms produce more to meet higher nominal demand"
    - "Real output would not change — all prices would rise proportionally, leaving relative prices and real purchasing power unaffected"
    - "Real output would fall because higher prices reduce consumer purchasing power"
    - "Real output would rise permanently as higher nominal demand creates new productive capacity"
  answer: 1
  explanation: "With perfectly flexible prices, a 5% increase in money supply triggers a 5% rise in all nominal prices. Firms see higher nominal revenue but face proportionally higher nominal costs; consumers have 5% more money but everything costs 5% more. Real variables — quantities produced, relative prices, real wages — are unchanged. This is monetary neutrality. Sticky prices break this symmetry: when firms leave prices unchanged, the increase in nominal spending translates into higher real demand and output."

- question: "A restaurant's optimal profit-maximizing price is $12.00. The restaurant faces a $0.50 menu cost to update its prices. Following a mild demand shock, the optimal price shifts to $12.40. Why might the restaurant rationally choose NOT to reprice, even though $0.40 is left on the table?"
  type: multiple-choice
  options:
    - "Because restaurants typically have long-term contracts that prohibit mid-year repricing"
    - "Because near the profit-maximizing price, the firm's profit loss from being $0.40 off-optimal is second-order (tiny), making a $0.50 cost sufficient to deter adjustment"
    - "Because customers will switch to competitors if the restaurant raises prices at all"
    - "Because the $0.40 improvement in price is less than the cost of $0.50, making repricing clearly unprofitable"
  answer: 1
  explanation: "This is the Mankiw/Akerlof-Yellen insight: the profit function is very flat near its maximum. Being $0.40 below optimal costs the restaurant far less than $0.40 in lost profit — profit loss is second-order in the deviation from optimal price. So a small menu cost of $0.50 easily exceeds the tiny private profit gain from adjusting. But macroeconomically, when thousands of firms make this same rational calculation, prices across the economy are sticky, and monetary shocks produce real output effects — a first-order social consequence from individually tiny private costs."

- question: "Nominal wage contracts are a source of nominal rigidity because they fix the nominal wage; but goods prices, being set by market forces, adjust immediately to changes in money supply."
  type: true-false
  answer: false
  explanation: "Both wages and goods prices exhibit nominal rigidity through different mechanisms. Goods prices face menu costs, coordination failures, and information frictions. Wages are sticky due to explicit annual contracts, implicit contracts, efficiency wage considerations, and the asymmetric impact of nominal wage cuts on worker morale. The assumption that wages are sticky while goods prices are flexible (or vice versa) is too simple; New Keynesian models typically incorporate both."

- question: "Sticky prices allow monetary policy to have real short-run effects on output because nominal spending increases cannot be absorbed by proportional price increases when prices are rigid."
  type: true-false
  answer: true
  explanation: "This is the central mechanism of New Keynesian macroeconomics. When the central bank increases money supply, if prices were flexible all prices would rise proportionally — monetary neutrality. But with sticky prices, many firms leave their nominal prices unchanged. Households have more money to spend, firms see higher real demand at prevailing prices, and they respond by increasing output and employment. The real effect persists until prices gradually adjust — the speed of that adjustment determines the duration and magnitude of monetary policy's impact on real variables."

- question: "Explain the 'second-order private cost, first-order social cost' insight from menu cost theory and why it is crucial for understanding the real effects of monetary policy."
  type: short-answer
  answer: "Near the profit-maximizing price, a small deviation from optimal causes a negligible private profit loss (second-order, because the profit function is flat at its maximum). Even a trivially small menu cost can therefore deter a firm from repricing. But the macroeconomic consequence of widespread price stickiness is first-order: when most firms decline to adjust their prices after a monetary shock, aggregate nominal spending increases translate into real output and employment changes rather than being absorbed by proportional price increases. The small private disincentive to adjust produces a large collective failure to clear markets through price adjustment."
  explanation: "This explains why monetary policy is non-neutral in the short run even though each individual firm's failure to reprice costs it almost nothing. It is an externality of pricing inaction: each firm's benefit from not repricing is roughly zero in profit terms, but collectively their stickiness is what gives the central bank power to affect real output. The implication is that monetary policy effectiveness depends critically on the degree of price stickiness in the economy."
```

## Explainer

From your study of monopolistic competition, you know that firms set their own prices rather than taking a market price as given. Each firm faces a downward-sloping demand curve and chooses the price that maximizes its profit, balancing higher margins against lower sales volume. This market structure is the prerequisite for understanding sticky prices because it explains why firms have pricing discretion in the first place—and therefore why the decision of when and how to change prices becomes economically meaningful.

In a perfectly competitive market, prices adjust automatically to clear supply and demand; no individual firm makes a pricing decision. But monopolistically competitive firms must actively decide to change their prices, and this decision involves costs. **Menu costs** are the most concrete example: the literal expense of printing new catalogs, updating websites, reprogramming registers, and renegotiating contracts. These costs are typically small for any individual price change—perhaps a few hundred dollars for a restaurant reprinting its menu. The puzzle is how such small costs can have large macroeconomic consequences. The answer lies in a key insight from Mankiw (1985) and Akerlof and Yellen (1985): near the profit-maximizing price, the firm's profit function is very flat. A small deviation from the optimal price costs the firm almost nothing in lost profit (second-order loss), so even a tiny menu cost can make it rational to leave the price unchanged. But the macroeconomic consequences of unchanged prices are first-order—when many firms fail to adjust prices after a monetary shock, aggregate demand changes translate into output changes rather than being absorbed by price movements.

Beyond menu costs, several other mechanisms generate nominal rigidity. **Contracts** fix prices for specified periods—wages are typically renegotiated annually, rental agreements lock in rates for years, and supply contracts specify prices for months. **Information frictions** mean firms may not immediately observe changes in demand or costs, and even when they do, they face uncertainty about whether changes are temporary or permanent. **Coordination failures** arise because each firm's optimal price depends on what other firms charge; if a firm expects competitors to hold prices steady, it may rationally do the same, creating a self-reinforcing equilibrium of price stickiness. These mechanisms interact and amplify one another: a firm facing menu costs, contractual obligations, and uncertainty about competitor behavior has strong reasons to delay price adjustment.

The macroeconomic consequence of sticky prices is that monetary policy has real effects in the short run. If the central bank increases the money supply and prices were perfectly flexible, all prices would rise proportionally and nothing real would change—monetary neutrality would hold. But with sticky prices, many firms leave their prices unchanged in the short run. The increase in nominal spending translates into higher real demand at prevailing prices, firms respond by producing more, and output and employment rise. This is the core mechanism of **New Keynesian economics**: nominal rigidities provide the friction that allows monetary policy to affect real economic activity. The duration and magnitude of these real effects depend on how quickly and how completely prices eventually adjust—questions that the Calvo pricing model and its alternatives formalize by specifying the stochastic process governing price changes.
