---
id: tariffs-and-import-quotas
title: Tariffs, Import Quotas, and the Welfare Effects of Trade Policy
domain: economics
course: microeconomics
prerequisites:
- id: comparative-advantage-and-trade
  type: hard
- id: consumer-surplus-deadweight-loss-policy
  type: hard
- id: market-equilibrium
  type: hard
- id: tax-incidence-and-elasticity
  type: soft
builds-toward:
- trade-and-development
tags:
- international trade
- tariffs
- import quotas
- protectionism
- deadweight loss
- world price
stage: formal-systems
status: validated
---

# Tariffs, Import Quotas, and the Welfare Effects of Trade Policy

## Core Idea
When a small country opens to trade, its domestic price moves to the world price, and it imports the gap between domestic demand and domestic supply. A tariff is a tax on imports. It raises the domestic price, so domestic producers sell more, consumers buy less, imports fall, and the government collects revenue. Consumers lose more surplus than producers and the government gain together, and the difference is a deadweight loss. An import quota limits the quantity of imports directly and has similar price effects, but the revenue goes to whoever holds the import licenses.

## How It's Best Learned
Draw domestic supply and demand with a horizontal world-price line below the domestic equilibrium. Label imports as the horizontal gap at the world price. Then raise the line by the tariff and shade four areas: the producer gain, the government revenue rectangle, and the two deadweight-loss triangles. Working one numerical example with linear curves fixes the areas in memory.

## Common Misconceptions
- A tariff is paid by foreign exporters. (In a small country facing a fixed world price, the domestic price rises by the full tariff, so domestic buyers bear it.)
- Protecting an industry with a tariff makes the country as a whole better off because jobs are saved. (Producer gains and tariff revenue are smaller than the loss to consumers; the net effect for a small country is a deadweight loss.)
- An import quota and a tariff that lead to the same import level have identical welfare effects. (Prices and quantities can match, but under a quota the rectangle that would have been tariff revenue goes to license holders, who may be foreign firms.)

## Questions

```yaml
- question: "Domestic demand for steel is Qd = 100 − P and domestic supply is Qs = P. The world price is 20. The country imposes a tariff of 10 per unit. How many units are imported after the tariff?"
  type: multiple-choice
  options: ["60", "50", "40", "30"]
  answer: 2
  explanation: "With the tariff the domestic price becomes 20 + 10 = 30. Demand is 100 − 30 = 70 and domestic supply is 30, so imports are 70 − 30 = 40. Before the tariff imports were 80 − 20 = 60."
- question: "In the same steel market, what is the deadweight loss from the tariff?"
  type: multiple-choice
  options: ["50", "100", "400", "750"]
  answer: 1
  explanation: "The production-side triangle is ½ × 10 × (30 − 20) = 50, from extra high-cost domestic output. The consumption-side triangle is ½ × 10 × (80 − 70) = 50, from purchases that no longer happen. Total deadweight loss is 100. As a check, consumers lose 750, producers gain 250, and the government collects 10 × 40 = 400, so the net loss is 750 − 250 − 400 = 100."
- question: "For a small country that cannot affect the world price, a tariff raises total surplus because it adds government revenue."
  type: true-false
  answer: false
  explanation: "The tariff revenue is a transfer from domestic consumers and adds no surplus of its own. Consumers lose more than the sum of producer gains and revenue, so total surplus falls by the deadweight loss."
- question: "Who receives the area that would have been tariff revenue when a country uses an import quota instead of a tariff, and why does that matter?"
  type: short-answer
  answer: "It goes to the holders of the import licenses, who can buy at the world price and sell at the higher domestic price. If the licenses are given to foreign exporters or domestic importers rather than auctioned, the government loses that revenue, so the country's net loss can be larger than under an equivalent tariff."
  explanation: "This gap between world and domestic prices times the quota quantity is called the quota rent. Auctioning licenses would make a quota and a tariff equivalent in welfare terms."
```

## Explainer
From comparative advantage you know that trade lets countries consume beyond their own production possibilities. Supply and demand show who wins and who loses inside one country. Suppose a small country can buy steel on the world market at a price of 20, and it cannot change that price. Domestic demand is Qd = 100 − P and domestic supply is Qs = P. Without trade the domestic price would be 50. With trade the domestic price falls to 20. Buyers want 80 units, domestic firms supply 20, and the country imports 60.

Now the government imposes a **tariff** of 10 per imported unit. Foreign steel now costs domestic buyers 30, and domestic firms can also charge 30. Four things happen. Domestic production rises from 20 to 30. Domestic consumption falls from 80 to 70. Imports shrink from 60 to 40. The government collects 10 on each of the 40 imported units, which is 400.

Consumer surplus falls by the area between the two prices out to the demand curve: the average of 80 and 70, times 10, is 750. Producer surplus rises by the matching area out to the supply curve: the average of 20 and 30, times 10, is 250. Adding producer gain and revenue gives 650, which is 100 less than the consumer loss. That 100 is the **deadweight loss**. It has two parts. One triangle, worth 50, comes from domestic firms producing units at a cost above the world price. The other triangle, also worth 50, comes from buyers who valued steel above 20 but no longer buy it at 30.

An **import quota** caps imports at a fixed amount, say 40 units. Domestic buyers then compete for limited foreign supply, and the domestic price rises until the gap between demand and domestic supply is 40, which again means a price of 30. Producers and consumers fare as under the tariff. The difference is the rectangle of 400. Under a quota it goes to whoever holds the right to import, called the quota rent. If those rights go to foreign firms, the country loses that area too.

Defenders of trade restrictions point to jobs in protected industries, national security, and helping young industries grow. Economists take some of these arguments seriously in particular cases. The basic small-country analysis still shows that a tariff transfers income from consumers to producers and the government, and destroys some surplus along the way.
