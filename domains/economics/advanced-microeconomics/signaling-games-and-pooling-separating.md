---
id: signaling-games-and-pooling-separating
title: 'Signaling Games: Separating and Pooling Equilibria'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: bayesian-games
  type: hard
- id: adverse-selection-screening
  type: soft
builds-toward:
- labor-market-signaling
tags:
- game-theory
- information-asymmetry
stage: expert
status: validated
---

# Signaling Games: Separating and Pooling Equilibria

## Core Idea
In signaling games, the informed player moves first with an action (signal) that communicates private information. Separating equilibria have different types taking different actions; pooling equilibria have all types taking the same action. The Intuitive Criterion eliminates equilibria depending on unreasonable out-of-equilibrium beliefs, selecting among multiple equilibria.

## Questions

```yaml
- question: "In a job market signaling model, all workers — regardless of ability — choose the same level of education. What type of equilibrium is this, and what does an employer learn by observing the education level?"
  type: multiple-choice
  options:
    - "A separating equilibrium — the employer infers ability from how easily each worker obtained the degree"
    - "A pooling equilibrium — the employer learns nothing about individual ability from observing education"
    - "A separating equilibrium — different abilities choose the same signal but for different internal reasons"
    - "A pooling equilibrium — the employer infers average productivity and pays accordingly, revealing type information"
  answer: 1
  explanation: "When all types choose the same action, the signal contains no information — it does not distinguish types. An employer observing a common education level cannot update their beliefs about any individual worker's ability beyond the prior. This is the defining feature of a pooling equilibrium: the signal is uninformative because it is not differentially costly. Note that option D is partially correct about wages (the employer pays expected average-productivity wages) but wrong that this reveals type — pooling means types are hidden, not revealed."

- question: "In Spence's job market signaling model, education functions as a credible signal of worker ability even when education provides no direct productivity improvement. Why?"
  type: multiple-choice
  options:
    - "Employers observe credentials and assume all degree holders are productive regardless of effort"
    - "Education is differentially costly across ability types: high-ability workers bear lower costs, making it rational for them to signal while low-ability workers find mimicry too expensive"
    - "High-ability workers intrinsically prefer education regardless of its cost"
    - "Government regulations require credentialing for skilled positions, so education signals compliance rather than ability"
  answer: 1
  explanation: "The signaling logic depends entirely on cost differences, not on education's direct effect. If education were equally costly for all types, low-ability workers could mimic high-ability workers and the signal would be uninformative. The single-crossing property — that high-ability workers have lower marginal signaling cost — means there exists an education threshold high enough that low-ability workers rationally decline to reach it. High-ability workers signal not because they love education, but because for them the cost of the credential is less than the wage premium it commands."

- question: "In a separating equilibrium, the employer's beliefs about a worker's type after observing their signal are the same as the employer's prior beliefs before any signal was sent."
  type: true-false
  answer: false
  explanation: "In a separating equilibrium, different types choose different signals, so observing the signal fully reveals the worker's type. The employer's posterior beliefs after seeing the signal concentrate entirely on the type that would rationally choose that signal — a dramatic update from the prior. If prior beliefs were 50% high-ability and 50% low-ability, observing a separating signal of 'high education' shifts the posterior to nearly 100% high-ability. This is precisely the point of a separating equilibrium: information is fully transmitted."

- question: "The Intuitive Criterion eliminates pooling equilibria that are sustained only by the belief that any worker who deviates from the pooling action must be the least productive type."
  type: true-false
  answer: true
  explanation: "This is the core logic of the Intuitive Criterion. A pooling equilibrium can be sustained if the employer responds to any deviation with pessimistic beliefs (assuming the deviator is low-type). But if the deviation would never benefit a low-type worker regardless of employer response — it is 'equilibrium dominated' for low types — then it is unreasonable to attribute the deviation to them. The employer should infer the deviator is high-type, which makes the deviation profitable and unravels the pooling equilibrium. The criterion asks: are the supporting beliefs reasonable given who would plausibly benefit from deviating?"

- question: "What is the 'single-crossing property' in signaling games, and why is it a necessary condition for a separating equilibrium to exist?"
  type: short-answer
  answer: "The single-crossing property means that the indifference curves of different types cross exactly once in the signal-wage space, with high types having flatter curves (lower marginal cost of the signal). This ensures that if a high-type worker is indifferent between a given signal level and no signal, a low-type worker strictly prefers no signal at that level. Without single-crossing, a low-type worker could always find it beneficial to mimic whatever signal a high-type sends, preventing any signal from being credibly informative. Single-crossing is what makes separation self-enforcing: each type's optimal choice differs because their cost-benefit tradeoffs differ fundamentally."
  explanation: "Single-crossing is the knife's edge that makes signaling work. If cost differences between types are too small (violating single-crossing), mimicry is always rational for low types, and only pooling equilibria exist. If cost differences are large enough (satisfying single-crossing), there exists a signal threshold that high types clear and low types rationally avoid."
```

## Explainer

From your study of adverse selection and screening, you know that information asymmetry creates problems: when one side of a market knows more than the other, uninformed parties cannot distinguish good types from bad. In screening models, the uninformed party moves first, designing a menu of contracts to sort the informed party. **Signaling games** flip this structure — here the informed party moves first, taking a costly action that conveys information about their type. The classic example is Spence's job market signaling: a worker knows their own productivity, and they choose how much education to get before an employer makes a wage offer. Education may or may not improve productivity directly — what matters is that it is differentially costly across types, allowing it to function as a credible signal.

A **separating equilibrium** is one where different types choose different signals, fully revealing their private information. In the education example, high-ability workers get a degree while low-ability workers do not. This works when the signal is costly enough that low types would not want to mimic high types, even for the higher wage. The condition is called the **single-crossing property**: the marginal cost of the signal must differ across types so that indifference curves of different types cross only once in signal-wage space. High-ability workers find education less costly (in effort, time, or difficulty), so they are willing to invest in a level of education that low-ability workers would find prohibitively expensive. The employer, observing the education level, correctly infers the worker's type and pays accordingly.

A **pooling equilibrium** is one where all types choose the same signal, so no information is transmitted. If all workers get the same education level regardless of ability, the employer learns nothing and pays the average-productivity wage. Pooling equilibria can be sustained when the signal cost is high enough that no type finds it worthwhile to deviate — or when beliefs about deviators are pessimistic enough that deviating is not rewarded. This multiplicity of equilibria is a characteristic feature of signaling games: for many parameter values, both separating and pooling equilibria exist, along with partial-pooling equilibria where some types separate and others pool.

The **Intuitive Criterion**, introduced by Cho and Kreps, is the standard refinement for selecting among these equilibria. The idea is to eliminate equilibria that are sustained only by unreasonable beliefs about off-equilibrium actions. If a particular deviation from the equilibrium strategy could only conceivably benefit a high type (because a low type would lose money even with the most optimistic belief about the employer's response), then the employer should infer that any deviator is a high type. Formally, if a signal is **equilibrium dominated** for one type — meaning that type would never benefit from sending it regardless of how the receiver responds — then the receiver should not attribute that signal to that type. Applying this criterion typically eliminates pooling equilibria and many partial-pooling equilibria, selecting the most efficient separating equilibrium as the unique prediction. This refinement is widely applied in industrial organization, finance (firms signaling quality through dividends or debt), and political economy (candidates signaling competence through policy positions).
