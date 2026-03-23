---
id: price-discrimination-strategies
title: Price Discrimination Strategies and Welfare Effects
domain: economics
course: microeconomics
prerequisites:
- id: monopoly-output-and-pricing
  type: hard
tags:
- monopoly
- pricing
- discrimination
stage: formal-systems
status: validated
---

# Price Discrimination Strategies and Welfare Effects

## Core Idea
First-degree (perfect) discrimination charges each consumer their reservation price; second-degree discriminates by quantity (bulk discounts); third-degree separates markets and charges different prices. Perfect discrimination maximizes firm profit while eliminating deadweight loss but is rarely feasible. Second-degree discrimination occurs through nonlinear pricing; third-degree requires market segmentation. Discrimination can increase total output compared to uniform monopoly pricing but typically extracts consumer surplus.

## Questions

```yaml
- question: "An airline charges business travelers $800 and students $200 for the same route. The profit-maximizing reason to charge business travelers more is that:"
  type: multiple-choice
  options:
    - "Business travelers have higher incomes, so they should pay more"
    - "Business travelers have less price-elastic demand — they need to fly regardless of price, so the firm maximizes revenue by charging more where consumers are least responsive to price changes"
    - "Students are a protected class entitled to discounts under anti-discrimination law"
    - "Business travelers consume more airline resources per flight"
  answer: 1
  explanation: "Third-degree price discrimination's profit-maximizing condition is that marginal revenue be equalized across market segments, which means charging more in markets with less price-elastic demand. Business travelers typically must fly for meetings on specific dates — their demand is inelastic. Students have more flexibility (elastic demand) and will substitute away if prices rise. Option A is tempting but wrong: ability to pay is not the criterion; price sensitivity (elasticity) is. A market with inelastic demand — however rich or poor — gets charged more. A market with elastic demand — however affluent — gets a lower price."

- question: "Under perfect (first-degree) price discrimination, what happens to deadweight loss and consumer surplus compared to uniform monopoly pricing?"
  type: multiple-choice
  options:
    - "Deadweight loss is eliminated and consumer surplus is preserved — both buyers and sellers benefit"
    - "Deadweight loss is eliminated because output expands to the competitive level, but all consumer surplus is captured by the firm as profit"
    - "Deadweight loss increases because the firm now restricts output to only the highest-value buyers"
    - "Deadweight loss and consumer surplus are both unchanged because total output is fixed"
  answer: 1
  explanation: "Under perfect discrimination, the firm charges each consumer exactly their reservation price, so every consumer willing to pay at least marginal cost is served — output expands to the competitive level, and the efficiency loss (deadweight loss) disappears. But every consumer pays exactly their maximum willingness to pay, so no one gets a bargain: all consumer surplus is transferred to the firm as profit. This is efficient but deeply redistributive. Option A is the common error: students learn 'deadweight loss disappears' and conclude everyone benefits — in fact, buyers pay exactly what they would have been willing to pay rather than the lower competitive price."

- question: "Price discrimination always reduces consumer welfare relative to what consumers would experience under uniform monopoly pricing."
  type: true-false
  answer: false
  explanation: "Welfare effects are ambiguous and depend on what type of discrimination is practiced and how output changes. Third-degree discrimination often increases total output: consumers previously priced out of the market (those whose willingness to pay was below the uniform monopoly price but above marginal cost) may now be served at a lower discriminatory price. Those consumers gain welfare they wouldn't have had under uniform pricing. Whether total welfare rises depends on whether the output-expanding effect outweighs the consumer-surplus extraction. Some previously-served consumers pay more and are worse off; some new consumers buy and are better off."

- question: "Second-degree price discrimination requires the firm to know each individual buyer's reservation price in advance."
  type: true-false
  answer: false
  explanation: "This confuses second-degree with first-degree discrimination. First-degree (perfect) discrimination requires knowing each consumer's reservation price — which is why it is rarely feasible in practice. Second-degree discrimination works without any knowledge of individual identities: the firm designs a menu of product versions or quantity bundles, and consumers self-select into the tier designed for them. Airline economy/business/first-class cabins, software editions (student/professional/enterprise), utility tiered pricing — all work through self-selection. The firm uses product design (degrading lower tiers enough that high-value buyers choose the premium tier) rather than individual information."

- question: "In third-degree price discrimination, what condition must hold for a firm to maximize profit across market segments, and why?"
  type: short-answer
  answer: "The firm must equalize marginal revenue across all market segments. If marginal revenue is higher in segment A than segment B, the firm should shift output from B to A — sell more where each additional unit adds more revenue and less where it adds less — until marginal revenues are equalized. This means charging a higher price in the segment with less elastic demand (where consumers are less responsive to price changes, so raising price extracts more revenue) and a lower price in the more elastic segment."
  explanation: "The intuition is that a profit-maximizing firm directs output toward where it generates the most revenue at the margin. If MR_A > MR_B, moving one unit from B to A increases total revenue. This reallocation continues until MR_A = MR_B — an arbitrage condition. Because less elastic markets have higher marginal revenue at any given quantity (the demand curve is steeper), the profit-maximizing price in the inelastic market is higher. Business vs. leisure travelers, domestic vs. international markets, or geographic pricing all reflect this logic."
```

## Explainer

You've studied how a monopolist with a single price creates deadweight loss — it charges a price above marginal cost, restricts output, and leaves gains from trade on the table. **Price discrimination** is the monopolist's attempt to recapture those gains by charging different prices to different buyers or for different quantities. The three degrees of discrimination describe different ways this can be done, depending on the information the firm possesses and its ability to prevent resale.

**First-degree (perfect) discrimination** is the theoretical benchmark. The firm knows each consumer's **reservation price** — the maximum they'd pay — and charges exactly that. Every consumer pays a different price equal to what they'd be willing to pay rather than go without. The demand curve becomes the marginal revenue curve because each additional unit is sold to a buyer whose willingness to pay is exactly the price received. Output expands to the competitive level, and deadweight loss disappears entirely. But all consumer surplus is transferred to the firm as profit — no buyer gets a bargain. Perfect discrimination is rarely feasible in practice because firms don't know individual reservation prices and because buyers could otherwise collude or resell to arbitrage the price differences.

**Second-degree discrimination** works without knowing individual identities — the firm discriminates by quantity or product version, and consumers self-select. Utility companies charge lower rates per kilowatt-hour for high-volume users; airlines offer economy, business, and first class; software vendors offer student, professional, and enterprise licenses at different price-feature bundles. The firm designs a **menu of options** so that each consumer type chooses the option targeted at them. This is nonlinear pricing: the total price is not simply proportional to quantity. The key challenge is preventing high-willingness-to-pay buyers from mimicking low types to get the cheaper option — so product bundles are designed with just enough degradation in the low-tier option to make the high tier worth its premium to those who value it most.

**Third-degree discrimination** requires **market segmentation**: the firm splits buyers into identifiable groups and charges each group a different uniform price. Senior citizen discounts, student fares, geographic pricing, and airline revenue management all work this way. The condition for profit maximization across segments is that marginal revenue be equalized across markets — the firm charges more in the less price-elastic market (where consumers are less sensitive to price changes) and less in the more elastic market. A student market with elastic demand gets a lower price; a business traveler market with inelastic demand gets a higher price. Welfare effects are ambiguous: output typically increases relative to single-price monopoly (some previously excluded consumers now buy), but consumer surplus is redistributed toward the firm, and whether total welfare rises depends on whether the output effect outweighs the distributional loss.


