---
id: signaling-games-and-pooling-separating
title: 'Signaling Games: Separating and Pooling Equilibria'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games-and-incomplete-information
  type: hard
- id: adverse-selection-screening
  type: soft
builds-toward:
- labor-market-signaling
tags:
- game-theory
- information-asymmetry
stage: advanced
status: draft
---

# Signaling Games: Separating and Pooling Equilibria

## Core Idea
In signaling games, the informed player moves first with an action (signal) that communicates private information. Separating equilibria have different types taking different actions; pooling equilibria have all types taking the same action. The Intuitive Criterion eliminates equilibria depending on unreasonable out-of-equilibrium beliefs, selecting among multiple equilibria.

## Explainer

From your study of adverse selection and screening, you know that information asymmetry creates problems: when one side of a market knows more than the other, uninformed parties cannot distinguish good types from bad. In screening models, the uninformed party moves first, designing a menu of contracts to sort the informed party. **Signaling games** flip this structure — here the informed party moves first, taking a costly action that conveys information about their type. The classic example is Spence's job market signaling: a worker knows their own productivity, and they choose how much education to get before an employer makes a wage offer. Education may or may not improve productivity directly — what matters is that it is differentially costly across types, allowing it to function as a credible signal.

A **separating equilibrium** is one where different types choose different signals, fully revealing their private information. In the education example, high-ability workers get a degree while low-ability workers do not. This works when the signal is costly enough that low types would not want to mimic high types, even for the higher wage. The condition is called the **single-crossing property**: the marginal cost of the signal must differ across types so that indifference curves of different types cross only once in signal-wage space. High-ability workers find education less costly (in effort, time, or difficulty), so they are willing to invest in a level of education that low-ability workers would find prohibitively expensive. The employer, observing the education level, correctly infers the worker's type and pays accordingly.

A **pooling equilibrium** is one where all types choose the same signal, so no information is transmitted. If all workers get the same education level regardless of ability, the employer learns nothing and pays the average-productivity wage. Pooling equilibria can be sustained when the signal cost is high enough that no type finds it worthwhile to deviate — or when beliefs about deviators are pessimistic enough that deviating is not rewarded. This multiplicity of equilibria is a characteristic feature of signaling games: for many parameter values, both separating and pooling equilibria exist, along with partial-pooling equilibria where some types separate and others pool.

The **Intuitive Criterion**, introduced by Cho and Kreps, is the standard refinement for selecting among these equilibria. The idea is to eliminate equilibria that are sustained only by unreasonable beliefs about off-equilibrium actions. If a particular deviation from the equilibrium strategy could only conceivably benefit a high type (because a low type would lose money even with the most optimistic belief about the employer's response), then the employer should infer that any deviator is a high type. Formally, if a signal is **equilibrium dominated** for one type — meaning that type would never benefit from sending it regardless of how the receiver responds — then the receiver should not attribute that signal to that type. Applying this criterion typically eliminates pooling equilibria and many partial-pooling equilibria, selecting the most efficient separating equilibrium as the unique prediction. This refinement is widely applied in industrial organization, finance (firms signaling quality through dividends or debt), and political economy (candidates signaling competence through policy positions).
