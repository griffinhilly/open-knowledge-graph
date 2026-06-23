---
id: price-discrimination
title: Price Discrimination
domain: economics
course: microeconomics
prerequisites:
- id: monopoly-microeconomics
  type: hard
- id: consumer-surplus-microeconomics
  type: hard
- id: monopoly-market-power-barriers
  type: soft
- id: monopoly-output-and-pricing
  type: hard
builds-toward:
- welfare-analysis-microeconomics
tags:
- price discrimination
- first degree
- second degree
- third degree
- consumer surplus
stage: formal-systems
status: validated
---

# Price Discrimination

## Core Idea
Price discrimination occurs when a firm charges different prices to different customers for the same product, based on their willingness to pay. First-degree (perfect) price discrimination extracts all consumer surplus, eliminates deadweight loss, but transfers all gains to the producer. Second-degree discrimination uses quantity discounts or versioning; third-degree separates markets by observable characteristics (e.g., student discounts). Price discrimination requires market power, the ability to prevent resale, and identifiable differences in willingness to pay.

## How It's Best Learned
Compare the profit and welfare outcomes of standard monopoly pricing vs. each type of price discrimination graphically. The key insight is that first-degree discrimination is efficient (no DWL) but maximally inequitable.

## Common Misconceptions
- Price discrimination is not inherently illegal or harmful — in some cases (e.g., Ramsey pricing) it can increase efficiency and output.
- Third-degree price discrimination does not always result in higher profits than uniform pricing; it depends on whether the firm can fully separate demand segments.

## Questions

```yaml
- question: "A software company charges $200/month to businesses and $10/month to verified students for identical software. To maximize profit, the company should set prices so that:"
  type: multiple-choice
  options:
    - "The price difference equals the marginal cost of serving each group"
    - "Marginal revenue equals marginal cost within each market segment separately"
    - "Each group pays exactly its average willingness to pay"
    - "The higher-income group is always charged a price above the profit-maximizing monopoly price"
  answer: 1
  explanation: "This is third-degree price discrimination: the firm separates two identifiable segments (students vs. businesses) and sets MR = MC within each. Since MR = P(1 − 1/|ε|), the less price-elastic segment (businesses) faces a higher price. Option C describes first-degree discrimination, which requires knowing every individual's exact willingness to pay — impossible here. Option D is wrong; the price in each segment is determined by that segment's demand, not by a comparison to a uniform monopoly price."

- question: "Under perfect (first-degree) price discrimination, compared to a single-price monopoly, which outcome holds?"
  type: multiple-choice
  options:
    - "Total output increases, consumer surplus is positive, and deadweight loss falls"
    - "Deadweight loss is eliminated and all consumer surplus is transferred to the producer"
    - "Both total output and consumer surplus increase relative to the monopoly outcome"
    - "The firm earns the same profit but achieves a more equitable distribution"
  answer: 1
  explanation: "Perfect discrimination charges each buyer exactly their willingness to pay, so every unit where value exceeds marginal cost is sold — no deadweight loss. But consumer surplus is entirely extracted: every buyer pays their maximum, leaving them no better off than not buying. The social total surplus equals the competitive outcome, but it flows entirely to the producer. Option A is wrong because consumer surplus is zero, not positive. Option C is wrong because consumers are not better off — they pay their full reservation price."

- question: "Price discrimination usually harms consumers relative to what they would experience under single-price monopoly."
  type: true-false
  answer: false
  explanation: "Under a single-price monopoly, price-sensitive consumers are priced out entirely. If third-degree discrimination leads the firm to serve those consumers at a lower price (because it can now charge the inelastic segment more), those price-sensitive buyers are better off than under uniform monopoly pricing. Whether discrimination harms consumers on net depends on whether it expands or contracts total output and which groups face higher vs. lower prices."

- question: "Successful price discrimination requires market power, the ability to prevent resale between buyer groups, and some mechanism to identify or induce separation of buyer types."
  type: true-false
  answer: true
  explanation: "All three conditions are necessary. Without market power, competitors undercut the high price, eliminating the discrimination. Without preventing resale, low-price buyers resell to high-price buyers, arbitraging away the price gap. Without separating buyer types (through observable characteristics or self-selection mechanisms), the firm cannot charge different prices to different buyers. Remove any one condition and discrimination collapses."

- question: "Why does first-degree price discrimination eliminate deadweight loss even though it exploits consumers maximally?"
  type: short-answer
  answer: "Deadweight loss under single-price monopoly arises because consumers whose willingness to pay exceeds marginal cost are priced out — mutually beneficial trades don't happen. Under perfect discrimination, the firm charges each consumer exactly their willingness to pay, so every consumer with WTP ≥ MC makes a purchase. No beneficial trade is foregone, so deadweight loss is zero. The exploitation lies in how the gains are distributed — all surplus goes to the producer — not in whether the efficient quantity is traded."
  explanation: "Efficiency is about whether all mutually beneficial trades occur, not about distribution. Perfect discrimination achieves the competitive quantity (efficient) while capturing all surplus (maximally inequitable). This is why economists describe it as 'efficient but not equitable' — the total pie is as large as possible, but the consumer's slice is zero."
```

## Explainer

A standard monopolist faces an inherent dilemma: any single price leaves money on the table. Charge high and you lose price-sensitive buyers who would have paid something. Charge low and you give a discount to buyers who would have happily paid more. From your study of consumer surplus, you know this gap — the difference between willingness to pay and the actual price — is a transfer from the monopolist to buyers. **Price discrimination** is the strategy of recovering that lost revenue by charging different prices to different buyers based on their willingness to pay. It requires market power (otherwise competitors undercut the price differences), the ability to prevent resale between groups, and some way to identify or induce separation of buyer types.

**First-degree (perfect) price discrimination** is the theoretical extreme: the firm knows every buyer's exact reservation price and charges each one precisely that amount. The demand curve and the marginal revenue curve become identical, because each unit is sold at its own maximum price — there is no need to lower the price on prior units to sell more. The result is efficient: every unit where value exceeds cost is sold, so deadweight loss disappears entirely. But every dollar of consumer surplus is extracted. The social total surplus equals the competitive outcome; it just flows entirely to the producer. Perfect price discrimination is rarely achievable because individual willingness to pay is unobservable, though personalized algorithms and targeted pricing are increasingly close approximations.

**Second-degree discrimination** doesn't require knowing individual buyer types — instead it uses **self-selection mechanisms** that induce buyers to reveal their type through their choices. Quantity discounts (bulk pricing), versioning (economy vs. business class, software editions), and tiered subscription menus are all examples. The firm designs a menu of options where each consumer type prefers the option targeted at them, not the option meant for someone else. This is an information design problem: the firm must ensure the higher-valuation option isn't so attractive that low-valuation buyers choose it, while keeping the lower-valuation option genuinely appealing to low-valuation buyers. The firm does not need to identify who you are; your choices do the identification for it.

**Third-degree discrimination** uses observable group characteristics — student status, age, geography, time of purchase — to segment markets directly. The profit-maximizing rule in each segment is the same: set MR equal to MC within that segment. Since MR = P(1 − 1/|ε|), the segment with less elastic demand faces a higher price. Airlines charging business travelers more than leisure travelers, and software companies charging educational institutions less than corporations, both follow this logic: the price-sensitive segment gets a lower price, the inelastic segment pays more, and total profit exceeds what any single price could achieve. The efficiency consequences depend on whether the discrimination expands total output; sometimes it does (by serving price-sensitive buyers who would be priced out under uniform monopoly pricing), sometimes it does not.
