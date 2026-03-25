---
id: newcombs-problem
title: Newcomb's Problem
domain: philosophy
course: applied-rationality
prerequisites:
- id: expected-value-decision-making
  type: hard
- id: rational-choice-and-ethics
  type: soft
- id: sunk-cost-recognition
  type: soft
builds-toward:
- causal-vs-evidential-decision-theory
tags:
- decision-theory
- thought-experiment
- newcomb
- rationality
stage: advanced
status: validated
---
## Core Idea

Newcomb's problem presents a choice: take both boxes (getting $1,000 plus whatever a nearly perfect predictor placed in the opaque box) or take only the opaque box (getting $1,000,000 if the predictor predicted you would one-box, $0 if it predicted you would two-box). The predictor has been right 99% of the time with previous players. One-boxing gets you $1,000,000 almost certainly; two-boxing gets you $1,000 almost certainly (the predictor foresaw your greed and left the box empty). This simple setup reveals a deep split in decision theory: causal decision theory says to two-box (your choice cannot causally change what is already in the box), while evidential decision theory says to one-box (one-boxing is strong evidence that the box contains $1,000,000). The problem has no consensus solution and illuminates fundamental questions about the relationship between choice, causation, and rationality.

## How It's Best Learned

First understand both arguments fully — the two-boxing argument from causal reasoning and the one-boxing argument from expected payoffs. Then examine variants: what if the predictor is only 51% accurate? What if you can randomize? Each variant tests the boundaries of different decision theories. The value is not in solving the problem but in understanding what makes it hard.

## Explainer

From expected value decision-making, you know that rational choices should maximize probability-weighted outcomes. Newcomb's problem is the thought experiment that reveals a crack in this seemingly straightforward principle -- a case where two apparently valid forms of expected-value reasoning give opposite answers, and neither can be easily dismissed.

Here is the setup. A nearly perfect predictor -- right 99% of the time -- has placed money in two boxes. Box A is transparent and contains $1,000. Box B is opaque and contains either $1,000,000 or nothing, depending on what the predictor predicted you would do. If the predictor predicted you would take only Box B, it placed $1,000,000 inside. If it predicted you would take both boxes, it placed nothing. The boxes are sealed; the prediction is already made. You choose: take both boxes, or take only Box B?

The **two-boxing argument** is elegant. Whatever the predictor placed in Box B is already there -- your choice now cannot reach backward in time to change it. If Box B contains $1,000,000, taking both boxes gets you $1,001,000 (better than $1,000,000). If Box B contains $0, taking both boxes gets you $1,000 (better than $0). In every possible state of the world, taking both boxes gets you $1,000 more. This is called a dominant strategy, and it seems like the bedrock of rational choice. The **one-boxing argument** is equally compelling. The predictor is right 99% of the time. One-boxers almost always find $1,000,000 in Box B; two-boxers almost always find it empty. The expected value of one-boxing is roughly $990,000; the expected value of two-boxing is roughly $11,000. One-boxers walk away rich; two-boxers walk away with pocket change. How can a "rational" strategy reliably produce worse outcomes?

The problem has no consensus solution because the two arguments rely on different decision theories, and the problem is designed to pull them apart. Causal decision theory backs two-boxing; evidential decision theory backs one-boxing. What makes Newcomb's problem philosophically valuable is not that it needs to be "solved" but that it forces you to commit to a framework for what "acting rationally" means. Does rationality mean choosing the action with the best causal consequences from the point of decision? Or does it mean choosing the action most correlated with the best outcome? These usually agree, but Newcomb's problem is the knife-edge case where they diverge -- and your answer reveals which theory of rationality you implicitly hold.

## Questions

```yaml
- question: "A causal decision theorist is shown the following argument: 'One-boxers walk away with $1,000,000 nearly every time; two-boxers walk away with $1,000 nearly every time. Therefore you should one-box.' How does the causal decision theorist respond?"
  type: multiple-choice
  options:
    - "The argument is valid — expected value calculations are the correct basis for rational choice"
    - "The correlation between one-boxing and the large prize is spurious, caused by the predictor's method, not by the player's choice"
    - "At the moment of your choice, the contents of the opaque box are already fixed — taking both boxes always yields $1,000 more than taking one, regardless of what is in it"
    - "The argument would be valid only if the predictor's accuracy were 100%; at 99%, two-boxing has higher expected value"
  answer: 2
  explanation: "The causal decision theorist's core move is to note that at decision time, the box contents are already set — the predictor acted in the past. Since the content of the opaque box is causally independent of your present choice, taking both boxes dominates: you get whatever is in the opaque box PLUS $1,000. The observed correlation between one-boxing and the $1M is real, but correlation does not establish that your choice causes what's already in the box. This is the causal dominance argument."

- question: "A player reasons: 'I am the kind of person who one-boxes. The predictor is nearly perfect. Therefore the box almost certainly contains $1,000,000.' This reasoning exemplifies:"
  type: multiple-choice
  options:
    - "Causal decision theory — the player correctly identifies that choosing to one-box causes the $1M to be placed"
    - "Evidential decision theory — the player treats one-boxing as strong evidence that the box contains $1M, regardless of whether the choice causally affects the contents"
    - "A logical fallacy — past correlations among other players cannot predict what is in this player's box"
    - "Bayesian updating — the player correctly calculates a posterior probability conditional on the predictor's past accuracy"
  answer: 1
  explanation: "Evidential decision theory (EDT) recommends the action that is best correlated with good outcomes, using conditional expected value: E[outcome | one-box] ≈ $1,000,000 × 0.99 = $990,000 vs. E[outcome | two-box] ≈ $1,000 × 0.99 = ~$1,000. EDT one-boxes. This contrasts with causal decision theory (CDT), which conditions on the causal structure: since your choice does not cause what is already in the box, CDT two-boxes. The disagreement is genuine — neither framework is obviously wrong."

- question: "The two-boxing argument in Newcomb's problem rests on the observation that, at the moment of choice, the contents of the opaque box are already determined and cannot be causally changed by your decision."
  type: true-false
  answer: true
  explanation: "This is the exact foundation of the causal dominance argument. Whatever the opaque box contains — $0 or $1,000,000 — taking both boxes yields $1,000 more than taking only the opaque box. If the contents are fixed, two-boxing weakly dominates one-boxing. The causal decision theorist accepts this and two-boxes. The evidential decision theorist rejects this reasoning by focusing on the correlation rather than the causal structure."

- question: "Newcomb's problem has a single correct answer — one-boxing — because the expected monetary value of one-boxing ($990,000) clearly exceeds the expected value of two-boxing (~$11,000) given the predictor's 99% accuracy."
  type: true-false
  answer: false
  explanation: "This is the most common misconception: treating evidential expected value as the uniquely correct decision criterion. Causal decision theory also has a coherent expected-value calculation — it conditions on the causal structure and finds that two-boxing always yields $1,000 more. Newcomb's problem has no universally accepted solution precisely because both arguments are internally valid under their respective frameworks. The problem's value is diagnostic: it reveals that causal and evidential decision theories can recommend different actions, forcing us to decide which framework is correct."

- question: "Why doesn't Newcomb's problem have a universally accepted correct answer, and what makes it philosophically valuable despite this?"
  type: short-answer
  answer: "The problem has no consensus answer because two internally coherent decision theories — causal decision theory and evidential decision theory — give opposite recommendations. CDT says two-box (the contents are fixed; dominance reasoning applies). EDT says one-box (the choice is evidentially correlated with the $1M prize). Neither can be dismissed as simply wrong. The philosophical value lies precisely in this impasse: Newcomb's problem serves as a diagnostic that separates the theories, revealing that our intuitions about rational choice are inconsistent. It forces explicit commitment to a framework rather than allowing vague appeals to 'rationality.'"
  explanation: "Note also that the problem is not about free will or determinism — it arises even for libertarian free will, since the predictor is empirically accurate rather than metaphysically certain. The predictor need not 'see the future'; it may simply model your decision-making process better than you do. This is what makes the problem unsettling and durable."
```

## Common Misconceptions

- There is no universally accepted 'right answer' — Newcomb's problem is a diagnostic for competing theories of rational choice, not a puzzle with a hidden solution.
- The problem is not about free will or determinism — it arises even if you believe in libertarian free will, because the predictor is empirically accurate.
