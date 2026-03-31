---
id: hyperbolic-discounting
title: Hyperbolic Discounting
domain: economics
course: behavioral-economics
prerequisites:
- id: bounded-rationality
  type: soft
tags:
- time-preferences
- discounting
- self-control
- time-inconsistency
stage: advanced
status: validated
---

# Hyperbolic Discounting

## Core Idea
Hyperbolic discounting describes the empirical finding that people discount future rewards at rates that decrease over time, rather than at the constant rate assumed by standard exponential discounting. This produces time-inconsistent preferences: a person may prefer $110 in 31 days over $100 in 30 days when both are far away, but prefer $100 today over $110 tomorrow when the immediate option is now available. The key feature is a disproportionate preference for immediate rewards — a "present bias" that leads to procrastination, undersaving, overconsumption, and difficulty following through on long-term plans. Hyperbolic discounting is formally modeled by Laibson's quasi-hyperbolic (beta-delta) model, where beta (<1) captures the immediate-future discount and delta captures the per-period discount thereafter.

## Questions

```yaml
- question: "A person prefers to receive $100 today over $110 tomorrow but also prefers $110 in 31 days over $100 in 30 days. This pattern of preferences is..."
  type: multiple-choice
  options:
    - "Consistent with exponential discounting because the person values earlier payments"
    - "Time-inconsistent — the person's discount rate is higher for immediate trade-offs than for distant ones, which exponential discounting cannot produce"
    - "Random and uninterpretable"
    - "Consistent with risk aversion but not discounting"
  answer: 1
  explanation: "Exponential discounting applies the same discount rate to all adjacent periods, so if $100 now is preferred to $110 tomorrow (a 10% premium is insufficient for one day's wait), then $100 in 30 days should also be preferred to $110 in 31 days (the same one-day wait). The reversal reveals that the discount rate between today and tomorrow is higher than between day 30 and day 31 — a declining discount rate that is the hallmark of hyperbolic discounting and the source of time inconsistency."

- question: "Hyperbolic discounting implies that people always make poor decisions about the future."
  type: true-false
  answer: false
  explanation: "Hyperbolic discounting describes a systematic pattern in preferences, not necessarily poor outcomes in all cases. When present bias causes problems (undersaving, procrastination, unhealthy choices), people can and do adopt commitment devices — pre-commitment strategies that restrict their future choice set to counteract anticipated present bias. Automatic payroll deductions for savings, deadlines for projects, and gym membership contracts are all commitment devices that reflect sophisticated awareness of one's own time inconsistency. The problem is real but not inescapable."

- question: "What is a commitment device, and why does its existence provide evidence for hyperbolic discounting?"
  type: short-answer
  answer: "A commitment device is a voluntary restriction on one's own future choices — like automatic savings deductions, prepaid gym memberships, or self-imposed deadlines — designed to prevent future temptation from overriding current intentions. Commitment devices provide evidence for hyperbolic discounting because a time-consistent agent (exponential discounter) would never pay to restrict their future options — they would simply execute their plan when the time comes. Only a person who anticipates that their future self will have different preferences (present bias) would rationally constrain that future self."
  explanation: "The demand for commitment is a revealed preference for self-control. Odysseus binding himself to the mast to resist the Sirens is the classic metaphor. In modern life, people who delete social media apps before exams, ask friends to hold them accountable for diet goals, or use apps that lock them out of their phone at bedtime are all demonstrating awareness of time-inconsistent preferences and using pre-commitment to manage them. An exponential discounter would have no need for such devices."
```

## Explainer

Standard economic models assume that people discount the future exponentially — applying the same proportional discount rate to each period into the future. If you discount next year by 5%, you discount the year after by another 5%, producing a smooth, consistent decline in present value. Under exponential discounting, plans made today for future actions will still be optimal when the future arrives, because the relative valuation of adjacent periods never changes. This is time-consistency, and it makes exponential discounting the workhorse model for everything from savings behavior to climate policy.

The problem is that people do not discount exponentially. Experimental evidence overwhelmingly shows that discount rates decline over time. People apply very high discount rates to immediate trade-offs (today vs. tomorrow) and much lower rates to distant trade-offs (one year vs. one year and one day). This pattern looks more like a hyperbola than an exponential, hence the name. The practical consequence is time inconsistency: preferences reverse as the moment of choice approaches. You plan to start your diet on Monday, but when Monday arrives, you push it to next Monday. You plan to save the bonus, but when it arrives, you spend it. Your planning self and your experiencing self have different discount rates.

The quasi-hyperbolic (beta-delta) model, proposed by Laibson (1997), captures this elegantly with just one extra parameter. The standard exponential model discounts period-t utility by delta^t. The beta-delta model discounts it by beta * delta^t, where beta < 1 represents the extra discount applied to any future period relative to the present. When beta = 1, the model reduces to standard exponential discounting. When beta < 1, there is a discrete drop in valuation between "now" and "any future period," producing present bias. Typical estimates of beta range from 0.5 to 0.8, meaning people value immediate rewards at 1.25x to 2x what they would value the same reward if it were delayed by even a short period.

The behavioral consequences of present bias are pervasive. Undersaving for retirement is perhaps the most economically consequential: people intend to save more "starting next month" but consistently fail to follow through because next month's self faces the same present bias. Procrastination follows the same logic — the cost of effort is immediate while the benefits are delayed, so present-biased agents perpetually defer. Health behaviors (exercise, diet, medical checkups) involve immediate costs and delayed benefits, making them systematically undermined by present bias. Addiction involves immediate rewards and delayed costs, making it systematically reinforced.

The recognition of present bias has transformed policy design. The "Save More Tomorrow" program (Thaler and Benartzi) asks employees to commit now to increasing their savings rate with each future raise — a commitment device that exploits present bias by making the savings increase coincide with a pay increase (no perceived loss) and by requiring action to opt out rather than opt in. Default enrollment in retirement savings plans similarly exploits inertia and present bias. These interventions do not change preferences — they work with the grain of hyperbolic discounting rather than against it, producing better long-term outcomes without requiring willpower that present bias systematically erodes.
