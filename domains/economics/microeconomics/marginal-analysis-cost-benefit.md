---
id: marginal-analysis-cost-benefit
title: Marginal Analysis and Cost-Benefit Decisions
domain: economics
course: microeconomics
prerequisites:
- id: opportunity-cost-concept
  type: hard
- id: scarcity-and-opportunity-cost
  type: soft
builds-toward:
- profit-maximization-output-level
- marginal-utility-and-consumer-choice
- externalities-and-market-failure
- sunk-cost-fallacy
tags:
- marginal analysis
- cost-benefit analysis
- marginal benefit
- marginal cost
- decision rule
stage: formal-systems
status: validated
---

# Marginal Analysis and Cost-Benefit Decisions

## Core Idea
Most economic choices are about how much of an activity to do, and they are made one unit at a time. Marginal benefit (MB) is the extra benefit from one more unit; marginal cost (MC) is the extra cost, measured as opportunity cost. A decision-maker should keep expanding an activity while MB is at least as large as MC and stop where the two meet. Costs already paid and impossible to recover do not change MB or MC, so they should not affect the choice.

## How It's Best Learned
Build a table for a simple activity, such as hours of study before an exam, with columns for total benefit, marginal benefit, and marginal cost. Ask students to find the best number of hours using totals and then using marginals, and show that both give the same answer. Then add a sunk cost to the story and show that the marginal columns do not change.

## Common Misconceptions
- The best choice is the one that maximizes total benefit. (The best choice maximizes net benefit, total benefit minus total cost, which occurs where MB equals MC, usually before total benefit peaks.)
- Money already spent should influence whether to continue. (Sunk costs cannot be recovered whatever you do next, so they drop out of the comparison of future benefits and costs.)
- Marginal cost only counts money paid out. (It includes the value of the next-best use of time and resources, the opportunity cost.)

## Questions

```yaml
- question: "A student's marginal benefit from each extra hour of study is 10, 8, 6, 4, and 2 points for hours 1 to 5. The marginal cost of each hour is a constant 5. How many hours should the student study to maximize net benefit?"
  type: multiple-choice
  options: ["1 hour", "3 hours", "4 hours", "5 hours"]
  answer: 1
  explanation: "Hours 1 to 3 each add more benefit (10, 8, 6) than cost (5), so they raise net benefit. Hour 4 adds 4 but costs 5, so it lowers net benefit. The student should stop at 3 hours."
- question: "A firm has already spent $2 million, which it cannot recover, on a project. Finishing will cost $1 million more and yield $1.5 million in revenue. Should the firm finish?"
  type: multiple-choice
  options: ["No, because total spending of $3 million exceeds revenue of $1.5 million", "Yes, because the extra $1.5 million in revenue exceeds the extra $1 million in cost", "No, because the project has already lost money", "It depends only on how much has already been spent"]
  answer: 1
  explanation: "The $2 million is sunk and is lost whether or not the firm finishes. The decision compares only future values: finishing adds $1.5 million of benefit for $1 million of cost, a gain of $0.5 million. Comparing total spending to revenue mixes in the sunk cost."
- question: "At the quantity that maximizes net benefit, total benefit is also at its maximum."
  type: true-false
  answer: false
  explanation: "Total benefit keeps rising as long as marginal benefit is positive. Net benefit peaks earlier, where marginal benefit falls to equal marginal cost. Doing more beyond that point still adds some benefit but adds more cost."
- question: "Why does the rule 'expand an activity until marginal benefit equals marginal cost' give the same answer as comparing net benefit at every possible quantity?"
  type: short-answer
  answer: "Net benefit changes by MB minus MC with each additional unit. While MB exceeds MC, each unit raises net benefit; once MC exceeds MB, each unit lowers it. So net benefit is highest at the point where MB stops exceeding MC."
  explanation: "The marginal rule is a shortcut for the total comparison. It works because the change in a total is the sum of the marginal changes."
```

## Explainer
You already know that every choice has an opportunity cost: the value of the best alternative you give up. Marginal analysis applies that idea to a very common kind of choice. Most decisions are not all-or-nothing. They are about how much: how many hours to work, how many workers to hire, how much pollution to clean up. Such choices are easiest to make one unit at a time.

**Marginal benefit** is the additional benefit from one more unit of an activity. **Marginal cost** is the additional cost of that unit, including the opportunity cost of the time or resources it uses. The decision rule is simple. If the next unit's marginal benefit exceeds its marginal cost, do it, because it raises your net benefit. If its marginal cost exceeds its marginal benefit, stop, because it would lower your net benefit. The best quantity is where the two are equal, or, with whole units, the last unit for which MB is still at least MC.

Consider studying. The first hour is very useful, because you review the main ideas. Later hours add less, because you are going over material you already know. This falling marginal benefit is typical. Suppose the marginal benefits of five hours are 10, 8, 6, 4, and 2, and each hour costs you 5 in forgone sleep or work. Hours 1, 2, and 3 pass the test. Hour 4 does not. You should study three hours. Notice that total benefit would keep rising through hour 5. Maximizing total benefit and maximizing net benefit are different goals, and only the second makes sense when doing more is costly.

Marginal thinking also explains why **sunk costs** should be ignored. A sunk cost has already been paid and cannot be recovered. Because it is the same whatever you choose next, it does not change the marginal benefit or marginal cost of any future option. A firm that has spent $2 million on an unfinished project should ask only whether finishing adds more revenue than it costs from here. People often find this hard and keep going "so the money is not wasted," which behavioral economists call the sunk cost fallacy.

The same rule reappears throughout microeconomics. A consumer buys a good until its marginal benefit per dollar matches other goods. A firm produces until marginal revenue equals marginal cost. A society should reduce pollution until the marginal benefit of cleaner air equals the marginal cost of cleanup.
