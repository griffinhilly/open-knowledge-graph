---
id: causal-vs-evidential-decision-theory
title: "Causal vs. Evidential Decision Theory"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: newcombs-problem
    type: hard
  - id: expected-value-decision-making
    type: hard
tags: ["decision-theory", "causation", "evidence", "rationality", "philosophy"]
stage: advanced
status: validated
---

## Core Idea

Causal decision theory (CDT) says to choose the action that causes the best expected outcome — evaluating each action by its causal consequences. Evidential decision theory (EDT) says to choose the action such that, conditional on performing it, you expect the best outcome — evaluating each action by what it tells you about the world. In most real-world cases they agree, but in Newcomb-like problems they diverge. CDT two-boxes because taking both boxes cannot cause the opaque box to be empty. EDT one-boxes because one-boxing is evidence that the box is full. The Rationalist community has explored extensions including functional decision theory (FDT), which evaluates actions by the consequences of the abstract computation that produces them. The debate reveals that the seemingly simple concept of "acting rationally" requires specifying what counts as a consequence of your action.

## How It's Best Learned

Work through Newcomb's problem under both frameworks and verify that they give different recommendations. Then try the Smoking Lesion problem (EDT says don't smoke because smoking is evidence of the lesion, CDT says the lesion is the cause, not the smoking) to see where EDT fails. Consider what framework you implicitly use in everyday decisions.

## Common Misconceptions

- CDT and EDT are not competing 'religions' — they are formal frameworks that make precise, testable predictions about which choices are rational.
- CDT does not always recommend selfish behavior — it recommends the action with the best causal consequences, which can include cooperation and altruism.

## Explainer

From Newcomb's problem, you learned that a nearly perfect predictor can create a situation where two apparently sound reasoning strategies -- "take the dominant action" and "take the action correlated with the best outcome" -- give opposite advice. Causal vs. evidential decision theory formalizes this split into two competing frameworks for rational choice, each with a precise account of what it means for an action to be "the right one."

**Causal decision theory (CDT)** says you should choose the action whose causal consequences produce the best expected outcome. It evaluates each option by asking: "If I were to intervene and perform this action, what would happen?" In Newcomb's problem, CDT two-boxes because taking both boxes cannot causally reach backward in time to change what the predictor already placed inside. The box contents are fixed; adding Box A to whatever is in Box B always gets you $1,000 more. The correlation between one-boxing and the million dollars is real but non-causal -- and CDT insists that only causal consequences of your action count.

**Evidential decision theory (EDT)** says you should choose the action such that, conditional on performing it, you expect the best outcome. It evaluates each option by asking: "Given that I observe myself choosing this action, what do I expect the world to look like?" EDT one-boxes because one-boxing is strong evidence that the predictor predicted one-boxing, which means the box almost certainly contains $1,000,000. EDT does not care that the action does not causally change the box -- it cares about what the action tells you about the state of the world.

The Smoking Lesion problem exposes where EDT stumbles. Suppose a genetic lesion causes both a desire to smoke and cancer, but smoking itself does not cause cancer. EDT recommends not smoking, because observing yourself smoke is evidence you have the lesion (and thus cancer), even though the smoking does not cause the cancer. CDT correctly says: the lesion either exists or it does not; choosing not to smoke cannot change your genetic state, so you should smoke if you enjoy it. This case makes EDT look like it confuses correlation with causation. Yet in Newcomb's problem, one-boxers (following EDT) empirically walk away richer than two-boxers (following CDT). The Rationalist community has explored extensions like **functional decision theory (FDT)**, which evaluates actions by the consequences of the abstract decision procedure that generates them -- arguing that being the kind of agent who one-boxes is what causes the predictor to fill the box. Whether FDT resolves the debate remains an open question, but the existence of the debate reveals something important: the seemingly simple concept of "acting rationally" requires specifying what counts as a consequence of your action.

## Questions

```yaml
- question: "In Newcomb's problem, a predictor has placed $1M in Box B if it predicted you'd take only Box B, or $0 if it predicted you'd take both. Both boxes are sealed. What does Causal Decision Theory recommend, and why?"
  type: multiple-choice
  options:
    - "Take only Box B, because the predictor is nearly always right and one-boxing correlates with $1M"
    - "Take both boxes, because your choice now cannot causally affect what the predictor placed in the box earlier"
    - "Take only Box B, because EDT and CDT always agree in well-defined decision problems"
    - "Refuse to choose — Newcomb's problem is logically incoherent and has no correct answer"
  answer: 1
  explanation: "CDT evaluates actions by their causal consequences: the intervention of choosing both boxes over one box. Since the boxes are already sealed, your current choice cannot travel backward in time to change what the predictor placed inside. Causally, adding Box A to whatever is in Box B is always strictly better — you get $1000 more regardless of Box B's contents. CDT two-boxes precisely because it ignores correlations that don't run through causal mechanisms. This is also why one-boxers (following EDT) statistically walk away richer: the predictor's accuracy means one-boxing is strong evidence that Box B is full."

- question: "In the Smoking Lesion problem, a genetic lesion causes both a desire to smoke and cancer; smoking itself does not cause cancer. What does Evidential Decision Theory recommend, and why is this considered a flaw?"
  type: multiple-choice
  options:
    - "EDT recommends smoking, because smoking removes evidence of the lesion by showing non-aversion behavior"
    - "EDT recommends not smoking, because observing yourself smoke is evidence that you have the lesion — and thus cancer — even though the smoking didn't cause it"
    - "EDT recommends smoking, because it causally reduces cancer risk by providing a psychological outlet"
    - "EDT and CDT agree in this case: both recommend not smoking because cancer is a bad outcome"
  answer: 1
  explanation: "EDT recommends the action with the best expected outcome conditional on performing it. Conditionally on smoking, you observe yourself as someone with a desire to smoke — which is evidence of the lesion — raising your expected probability of cancer. EDT therefore recommends not smoking, treating the correlation between smoking and cancer as decision-relevant even though the causal path runs through the lesion, not the cigarette. This is widely considered a failure of EDT: it recommends foregoing a pleasurable activity to 'manage the evidence' about a fait accompli genetic state. The lesion either exists or it doesn't; smoking cannot change it. CDT correctly recommends smoking (or not, based only on taste/cost), recognizing that the causal path to cancer bypasses the choice."

- question: "In Newcomb's problem, CDT recommends two-boxing even though one-boxers empirically walk away with more money."
  type: true-false
  answer: true
  explanation: "True, and this is the core tension that makes Newcomb's problem philosophically important. CDT's reasoning is impeccable within its own framework: at the moment of choice, the box contents are fixed, so taking both is causally dominant (it always adds $1000). Yet EDT one-boxers get $1M while CDT two-boxers get at most $1000. Does rationality require us to follow the causal argument even when it leads to worse outcomes? CDT says yes — the decision was already 'over' when the predictor acted. Critics reply that a decision theory that systematically produces worse outcomes for its adherents seems defective. This tension drives much of the research into functional decision theory and related frameworks."

- question: "CDT and EDT give different recommendations whenever a decision involves uncertainty about the state of the world."
  type: true-false
  answer: false
  explanation: "False. CDT and EDT agree in the vast majority of decisions, including most decisions involving uncertainty. They diverge specifically in Newcomb-like problems: situations where the agent's choice is correlated with a causally prior state of the world (like the predictor's prediction). In ordinary decisions — choosing an umbrella when it might rain, investing in uncertain stocks — the action doesn't correlate with the prior state of the world in a way that disconnects causal and evidential reasoning. The frameworks produce different verdicts only when there is a correlation between the action and the world state that does not run through a causal mechanism the agent can influence."

- question: "What structural feature distinguishes Newcomb-like problems — where CDT and EDT diverge — from ordinary decisions where they agree?"
  type: short-answer
  answer: "In Newcomb-like problems, the agent's action is correlated with a causally prior state of the world through a mechanism that the action cannot causally influence. In Newcomb's problem, the predictor's earlier placement of money in the box depends on a prediction of the agent's action — so choice and box contents are correlated, but the choice has no causal power over the already-fixed box contents. In ordinary decisions, either no such backward correlation exists, or the action does causally influence the relevant state. When causal and evidential relevance align, CDT and EDT agree; when they come apart — when 'acting as evidence' conflicts with 'acting as a cause' — they give different verdicts."
  explanation: "This is also why FDT (functional decision theory) was developed: it tries to evaluate actions based on the consequences of the decision procedure that produces them, which can sometimes thread the needle between CDT and EDT. The key insight is that being the kind of agent who one-boxes is different from taking a backward-causal action — FDT argues that the predictor predicts your decision procedure, so choosing to one-box is in some sense causally upstream of the predictor's action, even if temporally downstream. Whether this resolves the debate remains contested."
```
