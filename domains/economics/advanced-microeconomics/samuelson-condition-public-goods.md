---
id: samuelson-condition-public-goods
title: Efficient Provision of Public Goods (Samuelson Condition and Lindahl Equilibrium)
domain: economics
course: advanced-microeconomics
prerequisites:
- id: public-goods-and-common-resources
  type: hard
- id: pareto-efficiency-and-optimality
  type: hard
- id: marginal-rate-substitution-indifference
  type: soft
- id: nash-equilibrium-microeconomics
  type: soft
builds-toward:
- vcg-auction-mechanism
tags:
- public goods
- Samuelson condition
- Lindahl equilibrium
- free rider
- vertical summation
- public economics
stage: expert
status: validated
---

# Efficient Provision of Public Goods (Samuelson Condition and Lindahl Equilibrium)

## Core Idea
A pure public good is consumed by everyone at once, so one unit benefits every person. Paul Samuelson showed in 1954 that Pareto-efficient provision requires the sum of all individuals' marginal rates of substitution between the public good and a private good to equal the marginal rate of transformation, Σᵢ MRSᵢ = MRT. For a private good, by contrast, each person's MRS equals the MRT separately. When people contribute voluntarily, each one compares only their own marginal benefit with the cost, so the Nash equilibrium supplies too little. Lindahl equilibrium, with personalized prices that sum to marginal cost, reaches the efficient level but relies on people reporting their benefits truthfully.

## How It's Best Learned
Use a small town with three residents and linear marginal-benefit schedules for a public park. Sum the schedules vertically, because every resident uses the same park, and set the sum equal to marginal cost. Then compute what would be built if residents contributed on their own, and finally find Lindahl prices. The gap between the voluntary and efficient levels makes the free-rider problem quantitative.

## Common Misconceptions
- Market demand for a public good is found by adding individual demands horizontally, as for private goods. (Each unit is shared by all, so willingness to pay is added vertically at each quantity.)
- Efficient provision means producing until each person's marginal benefit equals marginal cost. (That rule underprovides; efficiency requires the sum of marginal benefits to equal marginal cost.)
- Lindahl prices solve the free-rider problem. (They describe an efficient allocation, but because each person's price depends on their stated benefit, people have an incentive to understate it.)

## Questions

```yaml
- question: "Three identical residents each have marginal benefit MB = 10 − G from G units of a public good. The marginal cost of the good is constant at 6. What is the efficient quantity?"
  type: multiple-choice
  options: ["4", "6", "8", "10"]
  answer: 2
  explanation: "The sum of marginal benefits is 3(10 − G) = 30 − 3G. Setting 30 − 3G = 6 gives G = 8."
- question: "In the same town, if residents contribute voluntarily and each takes others' contributions as given, how much is provided in total?"
  type: multiple-choice
  options: ["0", "4", "8", "12"]
  answer: 1
  explanation: "In a Nash equilibrium, a resident adds to the total only while their own MB exceeds 6. Own MB equals 6 at G = 4, so no one adds beyond 4 in total. The town gets 4 units instead of the efficient 8."
- question: "In a Lindahl equilibrium, every person faces the same price per unit of the public good."
  type: true-false
  answer: false
  explanation: "Each person pays a personalized price equal to their own marginal benefit at the efficient quantity, and these prices sum to marginal cost. In the identical-resident example each pays 2 per unit, but with different preferences the prices differ."
- question: "Explain why the efficiency condition for a public good involves the sum of marginal rates of substitution, while for a private good it involves each person's MRS separately."
  type: short-answer
  answer: "A unit of a private good can be consumed by only one person, so efficiency requires that each person's willingness to give up other goods for one more unit equal its production cost. A unit of a public good is consumed by everyone simultaneously, so its total value to society is the sum of everyone's willingness to pay. Efficiency then requires that sum to equal the marginal rate of transformation."
  explanation: "This is the Samuelson condition. It explains why demand for public goods is summed vertically."
```

## Explainer
You know that a pure public good is non-rival and non-excludable: one person's use does not reduce what others get, and no one can easily be kept out. National defense and a lighthouse are textbook cases. The question here is how much of such a good an efficient economy should produce.

Start with a private good. If an extra apple goes to Ana, nobody else eats it. At a Pareto-efficient allocation, Ana's marginal rate of substitution between apples and other goods must equal the rate at which the economy can transform other goods into apples, the MRT. The same holds for every consumer separately.

A public good differs because an extra unit is enjoyed by everyone. Its value to society is the sum of what each person would give up for it. Paul Samuelson's 1954 paper "The Pure Theory of Public Expenditure" stated the condition: provide the public good up to the point where Σᵢ MRSᵢ = MRT. In money terms, the sum of individual marginal benefits equals marginal cost. Graphically, individual demand curves are added vertically, not horizontally.

Take three identical residents, each with marginal benefit 10 − G, and a marginal cost of 6. The vertical sum is 30 − 3G, so the efficient quantity is 8.

Now let residents contribute on their own. Each one gains only their own marginal benefit from an extra unit but pays its full cost. So each stops contributing once their own MB reaches 6, at G = 4. If the total were below 4, someone would add more; above 4, nobody would. Voluntary provision gives 4, half the efficient amount. Each resident free-rides on the others' contributions. This underprovision is a general result of private provision of public goods.

The Swedish economist Erik Lindahl described an allocation that fixes the problem in principle. Each person pays a **personalized price** per unit equal to their own marginal benefit at the efficient quantity, and these prices sum to marginal cost. In the example each resident pays 2 per unit. At a price of 2, each resident's demand is 10 − G = 2, or G = 8, so all agree on the efficient quantity and costs are covered.

The difficulty is information. Lindahl prices depend on preferences that only individuals know, and a person who understates their benefit pays less while still enjoying the good. Mechanism design asks whether any procedure can get people to reveal their values; the Vickrey-Clarke-Groves mechanism is one answer, at a cost in budget balance.
