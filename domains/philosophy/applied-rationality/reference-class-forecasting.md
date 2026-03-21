---
id: reference-class-forecasting
title: "Reference Class Forecasting"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: calibration-training
    type: hard
  - id: base-rate-neglect
    type: soft
builds-toward:
  - the-planning-fallacy
  - fermi-estimation
tags: ["forecasting", "base-rates", "planning", "statistics"]
stage: advanced
status: draft
---

## Core Idea

Reference class forecasting predicts the outcome of a specific case by looking at the base rate of similar cases — the "reference class." Instead of asking "how long will MY software project take?" (subject to optimism bias), ask "how long do software projects of this type and size typically take?" The outside view, as Kahneman calls it, anchors your estimate to empirical reality before you adjust for case-specific factors. Bent Flyvbjerg's research on infrastructure projects showed that reference class forecasting dramatically reduces cost overruns. The technique is simple: identify the reference class, find the distribution of outcomes, and use that as your starting point.

## How It's Best Learned

Apply reference class forecasting to a personal project: before estimating how long it will take, look up how long similar projects took for other people. Notice the gap between your inside-view estimate and the base rate. Practice identifying the right reference class — too broad loses specificity, too narrow loses statistical power.

## Common Misconceptions

- Reference class forecasting does not mean ignoring case-specific information — it means starting with the base rate and adjusting, rather than starting with your inside-view estimate.
- The technique is not limited to large projects — it applies to everyday estimates like commute times, cooking duration, or how long errands take.

## Questions

```yaml
- question: "A software engineer estimates her new feature will take 1 week based on careful analysis of the task. Historical data shows that similar features at her company take an average of 4 weeks. What does reference class forecasting recommend she do?"
  type: multiple-choice
  options:
    - "Use 1 week — she knows her own project best and her inside-view analysis is more specific"
    - "Use 4 weeks as the final estimate, ignoring all inside-view analysis"
    - "Start with the 4-week base rate as the anchor, then adjust modestly for any genuinely distinctive features of this project"
    - "Average the two estimates to get 2.5 weeks"
  answer: 2
  explanation: "Reference class forecasting prescribes starting with the outside view (base rate) as the anchor — not averaging it with the inside view, and not discarding it. The engineer can still adjust from 4 weeks if there are specific, concrete reasons this project is demonstrably different from the reference class (simpler technology, fewer dependencies, etc.). But the adjustment should be modest and explicit. Option A is the classic planning fallacy: most people believe their project is the exception, but the base rate reflects the aggregate of all such 'exceptions.' Option D (averaging) lacks principled justification and still underweights the base rate."

- question: "A researcher uses reference class forecasting to estimate the cost of a new bridge construction project. She identifies a reference class of 'large urban bridge projects in developed countries.' A colleague argues the class is too broad and insists on using only 'suspension bridges over 500 meters built in the last 10 years in the same country.' Which is correct?"
  type: multiple-choice
  options:
    - "The colleague is right — narrower reference classes are always more accurate because they are more specific"
    - "The researcher is right — broader classes always have more reliable statistics and should be preferred"
    - "The right choice involves a trade-off: too broad loses specificity, too narrow loses statistical power; the best reference class is narrow enough to be meaningfully similar but broad enough to include sufficient cases"
    - "Reference class forecasting should not be used for unique infrastructure projects because no two bridges are alike"
  answer: 2
  explanation: "Selecting the right reference class involves a genuine tension. Too broad (all construction projects) loses the specificity that makes the comparison meaningful. Too narrow (this exact type of project in this exact context) leaves you with too few data points to produce a reliable estimate — and risks cherry-picking comparisons that match your prior expectations. The goal is to find a class that is similar enough to be informative but large enough to provide statistical signal. This is one of the key practical skills in applying reference class forecasting: identifying the relevant peer group."

- question: "Reference class forecasting is most useful for projects where the forecaster has deep domain expertise, because expertise allows accurate identification of which features make a project exceptional."
  type: true-false
  answer: false
  explanation: "This is backwards. Reference class forecasting is especially valuable precisely because domain experts tend to over-rely on their inside view — believing their project is exceptional — and systematically underestimate time and cost. Kahneman's research (and Flyvbjerg's infrastructure data) shows that experts are often *more* overconfident than non-experts because they have more detailed inside-view information to construct optimistic narratives around. The outside view (base rate) is valuable as a corrective to this inside-view overconfidence. Expertise helps identify the reference class and make appropriate adjustments, but it should not override the base rate anchor."

- question: "Reference class forecasting requires ignoring what you know about your specific project in order to avoid contamination from the planning fallacy."
  type: true-false
  answer: false
  explanation: "This is a common misunderstanding of the technique. Reference class forecasting does not require ignoring case-specific information — it requires *sequencing* properly: start with the outside-view base rate as the anchor, then adjust for specific features. Flyvbjerg's method explicitly includes a step for 'adjusting for the specific case.' The problem with the inside view is not that case-specific information is irrelevant, but that people typically start from the inside view and anchor on it, then fail to sufficiently adjust toward the base rate. Reference class forecasting reverses the sequence: base rate first, specific adjustments second."

- question: "Explain why the 'outside view' (reference class base rate) tends to produce better forecasts than the 'inside view' (detailed analysis of the specific case), and under what conditions adjustments from the base rate are justified."
  type: short-answer
  answer: "The inside view focuses on the unique details of a specific plan — its stages, challenges, and contingencies — which creates optimistic scenarios that systematically underweight base-rate outcomes. People construct detailed mental models that anchor on best-case assumptions and underrepresent the long tail of delays, surprises, and failures that the reference class captures. The outside view bypasses this by asking what actually happened to similar projects, incorporating all the unexpected problems that forecasters routinely fail to imagine. Adjustments from the base rate are justified when there is concrete, verifiable evidence that this project differs from the reference class in ways that historically predict different outcomes — not just a feeling that 'this one is different.'"
  explanation: "Kahneman describes this as the tension between 'inside view' narrative (our project has a great team, a clear plan, and management support) versus 'outside view' statistics (most projects of this type overrun by 40%). The narrative feels compelling but the statistics are more reliable. Adjustments are warranted only for specific, falsifiable differences — not generic claims of exceptionalism, which every forecaster also claims."
```
