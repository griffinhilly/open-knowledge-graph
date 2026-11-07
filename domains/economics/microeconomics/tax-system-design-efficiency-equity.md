---
id: tax-system-design-efficiency-equity
title: 'Designing a Tax System: Efficiency and Equity'
domain: economics
course: microeconomics
prerequisites:
- id: tax-incidence-and-elasticity
  type: hard
- id: consumer-surplus-deadweight-loss-policy
  type: hard
- id: price-elasticity-of-demand
  type: soft
- id: tax-brackets-marginal-rates
  type: soft
builds-toward:
- social-welfare-optimization
- automatic-stabilizers-fiscal-tools
tags:
- taxation
- progressive tax
- regressive tax
- marginal tax rate
- average tax rate
- vertical equity
- horizontal equity
- lump-sum tax
stage: formal-systems
status: validated
---

# Designing a Tax System: Efficiency and Equity

## Core Idea
A good tax system raises revenue at a low cost to society and shares the burden fairly. Efficiency concerns two costs beyond the tax paid: the deadweight loss from changed behavior, which depends on the marginal tax rate, and the administrative burden of complying. Equity has two principles: the benefits principle (pay according to benefits received) and the ability-to-pay principle, which splits into vertical equity (people with more ability pay more) and horizontal equity (people in similar situations pay similar amounts). A tax is progressive, proportional, or regressive depending on whether the average tax rate rises, stays constant, or falls as income rises.

## How It's Best Learned
Start with a two-bracket income tax and compute average and marginal rates for several incomes, so students see why the two rates differ. Then compare a lump-sum tax with an income tax that raises the same revenue and ask which changes behavior at the margin. Finish by classifying real taxes, such as a flat payroll tax with a cap, by how the average rate moves with income.

## Common Misconceptions
- Moving into a higher tax bracket can lower your after-tax income. (In a bracket system, the higher rate applies only to income above the threshold, so earning more always leaves you with more after tax.)
- A tax is progressive if rich people pay more dollars. (Progressivity is defined by the average tax rate rising with income; a proportional tax also takes more dollars from higher earners.)
- The legal taxpayer bears the burden. (Incidence depends on elasticities of supply and demand, so the burden can fall largely on the other side of the market.)

## Questions

```yaml
- question: "An income tax charges 10% on the first $20,000 of income and 30% on income above $20,000. For a person earning $50,000, what are the average and marginal tax rates?"
  type: multiple-choice
  options: ["Average 30%, marginal 30%", "Average 22%, marginal 30%", "Average 20%, marginal 10%", "Average 10%, marginal 22%"]
  answer: 1
  explanation: "Tax owed is 0.10 × 20,000 + 0.30 × 30,000 = 2,000 + 9,000 = 11,000. The average rate is 11,000 / 50,000 = 22%. The marginal rate, the rate on the next dollar earned, is 30%."
- question: "Why does a lump-sum tax, a fixed amount owed by every person whatever they do, create no deadweight loss?"
  type: multiple-choice
  options: ["Because it raises no revenue", "Because the marginal tax rate is zero, so it does not change the reward from working or buying one more unit", "Because it falls only on high-income people", "Because it is collected by the central bank"]
  answer: 1
  explanation: "Deadweight loss arises when a tax changes choices at the margin. A lump-sum tax takes the same amount whatever a person earns or buys, so extra effort or purchases are not taxed. It is efficient but widely seen as unfair, because it takes the same amount from rich and poor."
- question: "A payroll tax that takes 6% of all wages up to a cap and nothing on wages above the cap is regressive at incomes above the cap."
  type: true-false
  answer: true
  explanation: "Above the cap, the tax paid stays fixed while income keeps rising, so the average tax rate falls as income rises. A falling average rate is the definition of regressive."
- question: "Explain the difference between vertical and horizontal equity and give an example of a tax rule that could violate horizontal equity."
  type: short-answer
  answer: "Vertical equity says people with greater ability to pay should pay more. Horizontal equity says people with similar ability to pay should pay similar amounts. A deduction available only to homeowners could violate horizontal equity, because a renter and a homeowner with the same income would pay different taxes."
  explanation: "Both are applications of the ability-to-pay principle. Vertical equity concerns comparisons across income levels; horizontal equity concerns comparisons among people at the same level."
```

## Explainer
Governments need revenue for roads, defense, schools, and transfers. The question is how to raise it. Economists judge a tax system by two standards: efficiency and equity.

**Efficiency** asks how much a tax costs society beyond the money collected. From your study of deadweight loss, you know that a tax drives a wedge between what buyers pay and what sellers receive, so some trades that would have benefited both sides do not happen. The size of that loss depends on how much behavior changes, which depends on elasticities and on the **marginal tax rate**, the tax on one more dollar of income or one more unit bought. With linear supply and demand, the deadweight loss grows with the square of the tax rate, so doubling a tax roughly quadruples its deadweight loss. The second efficiency cost is administrative burden: time spent on records and forms, and money spent on tax advice and enforcement.

The most efficient tax in theory is a **lump-sum tax**, the same fixed amount for everyone. Because it does not depend on anything a person does, its marginal rate is zero, and it creates no deadweight loss. Few governments rely on it, because it takes the same amount from a poor family as from a rich one.

That brings in **equity**. The **benefits principle** says people should pay according to the benefits they receive from government, as with a gasoline tax that funds roads. The **ability-to-pay principle** says people should pay according to how well they can bear the burden. It has two parts. **Vertical equity** says those with more ability should pay more. **Horizontal equity** says people with similar ability should pay similar amounts.

Taxes are classified by the **average tax rate**, total tax divided by income. If the average rate rises with income, the tax is **progressive**; if it stays the same, **proportional**; if it falls, **regressive**. In a bracket system the two rates differ. With 10% on the first $20,000 and 30% above, a person earning $50,000 owes $11,000. The average rate is 22%, but the marginal rate is 30%. Efficiency depends on the marginal rate, while progressivity is about the average rate.

The two goals often conflict. Higher marginal rates on high earners raise vertical equity but increase deadweight loss. Deciding how to balance them involves value judgments as well as economics.
