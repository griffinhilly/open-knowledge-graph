---
id: information-value-and-exploration
title: "Value of Information and Exploration-Exploitation"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: expected-value-decision-making
    type: hard
  - id: bayesian-thinking-in-practice
    type: soft
tags: ["decision-theory", "information", "exploration", "exploitation", "VoI"]
stage: formal-systems
status: draft
---

## Core Idea

The value of information (VoI) is how much better you expect your decision to be if you acquire additional information before acting. If learning the answer to a question would not change your decision, that information has zero value regardless of how interesting it is. VoI analysis prevents both over-researching (gathering information that will not affect your choice) and under-researching (acting on insufficient information when cheap investigation is available). The exploration-exploitation tradeoff generalizes this: exploring (trying new options, gathering data) has information value but opportunity cost, while exploiting (acting on current best knowledge) captures immediate value but may miss better options. Optimal strategies explore more when uncertainty is high and time horizons are long, and exploit more as certainty increases or deadlines approach.

## How It's Best Learned

Before researching a decision, ask: what would I do if I could not get any more information? If the answer is clear, further research has low VoI. Apply the explore-exploit framework to everyday choices: restaurants (try new ones when you have many meals ahead, go to favorites when you want a reliable experience), career moves (explore early, exploit later).

## Common Misconceptions

- Value of information is not the same as interestingness — fascinating information that does not change any decision has zero practical VoI.
- The exploration-exploitation tradeoff does not have a universal solution — the optimal balance depends on time horizon, stakes, and current uncertainty.
