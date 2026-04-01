---
id: intertemporal-choice-behavioral
title: Intertemporal Choice in Behavioral Economics
domain: economics
course: behavioral-economics
prerequisites:
- id: hyperbolic-discounting
  type: hard
- id: present-bias
  type: hard
- id: prospect-theory-behavioral
  type: soft
tags:
- intertemporal-choice
- quasi-hyperbolic
- beta-delta
- commitment-devices
- time-inconsistency
stage: advanced
status: validated
---

# Intertemporal Choice in Behavioral Economics

## Core Idea
Behavioral models of intertemporal choice study how people actually make tradeoffs between costs and benefits occurring at different times, departing sharply from the exponential discounting assumed in standard economics. The central finding is that people are time-inconsistent: they discount the near future much more steeply than the distant future, leading to preference reversals (preferring $100 today over $110 tomorrow, but $110 in 31 days over $100 in 30 days). The quasi-hyperbolic (beta-delta) model formalizes this with a present-bias parameter (beta < 1) that captures the extra weight placed on immediate outcomes. Time-inconsistency creates demand for commitment devices — mechanisms that restrict future choices to prevent the future self from succumbing to temptation — and has profound implications for savings, health behavior, addiction, and the design of default options in retirement plans.

## Questions

```yaml
- question: "A person prefers $100 today over $110 tomorrow, but also prefers $110 in 31 days over $100 in 30 days. This preference pattern is best explained by..."
  type: multiple-choice
  options:
    - "Standard exponential discounting with a high discount rate"
    - "Hyperbolic or quasi-hyperbolic discounting, which produces present bias and preference reversals"
    - "Risk aversion — the person is uncertain about future payments"
    - "Loss aversion — the person views delay as a loss"
  answer: 1
  explanation: "Exponential discounting cannot produce this reversal — if you prefer $100 today over $110 tomorrow, exponential discounting requires that you also prefer $100 in 30 days over $110 in 31 days, because the ratio of discount factors between consecutive days is constant. Hyperbolic and quasi-hyperbolic discounting produce steeper discounting for near-future delays than distant-future delays, so the one-day delay looms much larger when it is imminent (today vs. tomorrow) than when it is remote (day 30 vs. day 31). This preference reversal is the hallmark of present bias."

- question: "In the quasi-hyperbolic (beta-delta) model, a sophisticated agent who knows they have present bias will behave identically to a naive agent who is unaware of their bias."
  type: true-false
  answer: false
  explanation: "Sophisticates and naifs behave differently because sophisticates anticipate their future self-control problems. A sophisticated present-biased agent knows that their future self will over-discount, so they may seek commitment devices (automatic savings enrollment, gym contracts with penalties, deadlines) to constrain future behavior. A naive agent falsely believes they will follow through on plans, so they do not seek commitment and are repeatedly surprised by their own procrastination or impulsive behavior. The distinction between sophistication and naivete has major implications for policy design — commitment devices help sophisticates but may be ignored or avoided by naifs."

- question: "What is a commitment device, and why does the existence of demand for commitment devices provide evidence against exponential discounting?"
  type: short-answer
  answer: "A commitment device is a mechanism that restricts a person's future choices — such as automatic payroll deductions into a savings account, a gym contract with cancellation penalties, or Odysseus binding himself to the mast. Under exponential discounting, preferences are time-consistent, so there is no reason to constrain your future self — your future self will want exactly what your current self plans. Demand for commitment devices implies that people anticipate their preferences will change in ways they currently consider suboptimal, which is precisely what present bias and time inconsistency predict."
  explanation: "The revealed preference for commitment is among the strongest evidence for time inconsistency. Products like Save More Tomorrow (Thaler and Benartzi), where employees pre-commit to allocating future raises to savings, exploit the fact that people can plan wisely for the distant future but cannot execute those plans when the future becomes the present. The demand for such products is economically irrational under exponential discounting but perfectly rational under quasi-hyperbolic discounting with sophistication."

- question: "How does the beta parameter in the quasi-hyperbolic model relate to present bias?"
  type: short-answer
  answer: "The beta parameter (0 < beta <= 1) captures the degree of present bias. When beta = 1, the model reduces to standard exponential discounting with no present bias. As beta decreases below 1, the agent places increasingly disproportionate weight on immediate payoffs relative to all future payoffs. Empirical estimates typically place beta between 0.6 and 0.9, meaning people treat the present as 10-40% more valuable than even the very near future, over and above the normal time preference captured by delta."
  explanation: "The beta-delta model (Laibson, 1997) elegantly separates two distinct aspects of time preference: delta captures the standard long-run patience (how much you discount one period against the next in the future), while beta captures the additional pull of the present moment. This two-parameter structure is both tractable and empirically powerful — it generates time-inconsistent behavior with a minimal departure from the standard exponential model, which is why it has become the workhorse model in behavioral economics applications to savings, procrastination, and addiction."
```

## Explainer

Standard economics models intertemporal choice using exponential discounting: future utility is discounted at a constant rate per period, so the tradeoff between any two consecutive periods is always the same regardless of when those periods occur. This produces time-consistent preferences — a plan made today for future behavior will still be the preferred plan when the future arrives. Paul Samuelson introduced this framework in 1937 as a simplifying assumption, not as an empirical claim, but it became the default model in economics for decades. The behavioral economics of intertemporal choice begins with the observation that this assumption is systematically wrong.

The key empirical regularity is that people discount the near future much more steeply than the distant future. When choosing between a smaller-sooner reward and a larger-later reward, people are far more impatient when the smaller reward is available immediately than when both rewards are in the future. This produces preference reversals: a person who prefers $110 in 31 days over $100 in 30 days will reverse that preference as day 30 approaches and choose $100 immediately over $110 tomorrow. This pattern — called hyperbolic discounting — has been documented in humans and animals across hundreds of experiments. It means that plans made calmly in advance are systematically abandoned when the moment of temptation arrives.

The quasi-hyperbolic or beta-delta model, formalized by Laibson (1997) building on work by Phelps and Pollak (1968), captures this pattern with a minimal modification to the standard model. Instead of discounting period-t utility by delta^t, the model discounts it by beta * delta^t for all t > 0, where beta is between 0 and 1. The beta parameter creates an extra discount applied to all future periods relative to the present, generating the disproportionate pull of the present moment. When beta equals 1, the model reduces to standard exponential discounting. When beta is less than 1, the agent is present-biased: they overweight immediate gratification relative to what their "long-run self" would prefer. This creates an intrapersonal conflict — the person at time 0 and the person at time 1 effectively have different preferences, which is why the literature sometimes models intertemporal choice as a game between multiple selves.

The sophistication-naivete distinction is critical for applied work. A naive agent does not realize they are present-biased and makes plans they will not follow through on — they plan to start dieting tomorrow, saving next month, exercising next week, but tomorrow they postpone again. A sophisticated agent correctly anticipates their future self-control failure and takes strategic action: they use commitment devices to bind their future selves. The most celebrated application is the Save More Tomorrow program (Thaler and Benartzi, 2004), which invites employees to pre-commit to increasing their savings rate with each future raise. Because the commitment is made in advance (when beta does not distort the decision), employees agree — and because the increases coincide with raises (so take-home pay never falls), they follow through. Participation raised average savings rates from 3.5% to 13.6% over four years, a dramatic demonstration that small behavioral interventions can overcome the consequences of present bias.

The implications extend across nearly every domain where short-term costs and long-term benefits conflict: addiction (the immediate pleasure of a cigarette versus long-term health), procrastination (the immediate pleasure of avoiding an unpleasant task versus the long-term cost of delay), credit card debt (immediate consumption versus future interest payments), and exercise (immediate discomfort versus future health). In each case, the time-inconsistency framework explains both the self-destructive behavior and the demand for self-regulation strategies that would be unnecessary under exponential discounting.
