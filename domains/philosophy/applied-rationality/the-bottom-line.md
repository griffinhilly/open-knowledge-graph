---
id: the-bottom-line
title: "The Bottom Line"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: motivated-reasoning
    type: hard
builds-toward:
  - considering-the-opposite
  - steelmanning
tags: ["rationality", "biases", "argument-evaluation", "motivated-cognition"]
stage: advanced
status: validated
---

## Core Idea

Imagine a sheet of paper where the bottom line — the conclusion — is written first, and then arguments are filled in above it. No matter how compelling those arguments look, they carry no evidential weight because they were selected to support a predetermined conclusion. This thought experiment from the Sequences illustrates why the order of operations in reasoning matters: evidence must be evaluated before reaching a conclusion, not gathered in service of one. Once you have written the bottom line, any further "reasoning" is rationalization. The practical test: if no possible evidence could change your conclusion, you are not reasoning — you are performing reasoning.

## How It's Best Learned

Before evaluating an argument, ask yourself: have I already decided what I think? Practice with political or social topics where you have strong priors. Try to specify in advance what evidence would change your mind — if you cannot, you may have already written the bottom line.

## Common Misconceptions

- Having a prior belief is not the same as having written the bottom line — Bayesian reasoning starts with priors but genuinely updates on evidence.
- The bottom line is not about arguments being invalid — the same argument can carry evidential weight when encountered honestly and zero weight when cherry-picked.

## Explainer

From motivated reasoning, you know that desires and identity can steer reasoning toward predetermined conclusions without the reasoner's awareness. The Bottom Line, a thought experiment from Eliezer Yudkowsky's Sequences, crystallizes this insight into a single vivid image that serves as a diagnostic for broken reasoning.

Imagine a sheet of paper with a conclusion written at the bottom -- the "bottom line." Above it, someone has filled in arguments, evidence, and reasoning that support the conclusion. The arguments may be individually valid. The evidence may be genuine. But none of it carries evidential weight, because it was selected specifically to support a conclusion that was already determined before the reasoning began. The order of operations is reversed: instead of evidence leading to a conclusion, the conclusion determined which evidence would be gathered. Any argument selected to support a fixed conclusion tells you nothing about whether the conclusion is true -- it tells you only that the person is skilled at finding supporting arguments, which is a different thing entirely.

The practical test for whether you have written the bottom line is deceptively simple: **what evidence would change your mind?** If you can specify, even roughly, what the world would have to look like for you to abandon your current conclusion, your belief is held in a way that can respond to reality. You have a prior, not a bottom line. But if you find that no conceivable evidence would change your conclusion -- or if every piece of contrary evidence gets reinterpreted as either flawed or secretly confirming -- you have written the bottom line, and all the reasoning above it is rationalization. The key distinction is between having a strong prior (legitimate -- Bayesian reasoning starts with priors and updates) and having a fixed conclusion (illegitimate -- the "updating" is performative).

Consider two people who both conclude that a controversial policy is correct. Alex decided the policy was correct first, then gathered five supporting arguments and ignored three counterarguments. Beth examined all eight arguments with genuine openness and concluded the policy was correct. The arguments Beth found are evidence about the policy; the arguments Alex found are evidence about Alex's ability to construct rationalizations. The output looks identical -- five arguments for the same conclusion -- but the epistemic value is completely different. This is why the order of operations matters so much in reasoning: the same argument can carry genuine evidential weight when encountered honestly and zero weight when cherry-picked. Detecting which process generated the arguments requires examining how they were found, not what they say -- which is exactly why motivated reasoning is so hard to catch from the outside and nearly impossible to catch from the inside without deliberate practices like specifying what would change your mind.

## Questions

```yaml
- question: "Alex decides that Policy X is correct, then gathers and presents five strong supporting arguments. Beth evaluates the same five arguments before reaching any conclusion, and also ends up supporting Policy X. Whose arguments provide stronger evidence that Policy X is correct?"
  type: multiple-choice
  options:
    - "Alex's arguments are stronger because he has more conviction behind them"
    - "Both provide equal evidence — the logical validity of an argument doesn't depend on the order in which it was found"
    - "Beth's arguments provide stronger evidence, because Alex's were selected to support a conclusion already written, making them zero net evidence"
    - "Neither provides evidence — only empirical data, not arguments, can support a policy conclusion"
  answer: 2
  explanation: "The key insight is that evidential weight depends on the process by which arguments were found, not just their logical form. Alex wrote the bottom line first, then filled in supporting arguments above it. No matter how valid those arguments appear, they were chosen from a space of possible arguments precisely because they support X — so finding them tells us nothing about whether X is true. Beth's reasoning process could have led her anywhere; Alex's could not. The same argument, encountered honestly, carries information; encountered via rationalization, it carries none."

- question: "Which of the following is the clearest example of 'writing the bottom line'?"
  type: multiple-choice
  options:
    - "A scientist forms a hypothesis and then runs an experiment to test it, finding support for her hypothesis"
    - "A Bayesian reasoner starts with a strong prior that a drug is effective, then updates on clinical trial data that confirms it"
    - "A manager concludes before reviewing the data that the new product launch was a success, then selects metrics that show positive results to include in the report"
    - "A debater is assigned to argue one side of a topic and constructs the strongest possible case for that side"
  answer: 2
  explanation: "The manager wrote the bottom line — 'the launch was a success' — before examining evidence, then filtered the evidence through that conclusion. The hypothesis-testing scientist and Bayesian reasoner both have prior beliefs, but their process genuinely exposes them to contrary evidence that could change their conclusion. The debater is explicitly performing advocacy, not reasoning — both parties know the argument is one-sided, so no one is deceived about its evidential status."

- question: "An argument that is logically valid and supported by true premises carries the same evidential weight regardless of whether it was found before or after the reasoner committed to its conclusion."
  type: true-false
  answer: false
  explanation: "The bottom-line insight is precisely that evidential weight is process-dependent, not just structure-dependent. A valid argument found after committing to a conclusion was selected from all possible arguments because it supports that conclusion — the act of selection tells us nothing new about the world. If you looked for arguments on both sides and found this one was strongest, that's evidence. If you only looked for arguments supporting your predetermined conclusion, finding one is uninformative. The argument's internal structure is irrelevant to this epistemic point."

- question: "Having a strong prior belief about a conclusion is equivalent to having 'written the bottom line' — in both cases, your subsequent reasoning is rationalization."
  type: true-false
  answer: false
  explanation: "This is a critical distinction the topic explicitly addresses. A prior belief becomes the bottom line only when it is fixed — when no possible evidence could change it. Bayesian reasoning begins with priors and genuinely updates on evidence; the conclusion is not fixed in advance, even if the prior is strong. The test is counterfactual: could evidence change your mind? If yes, you are reasoning. If no possible evidence would move you, the conclusion was written before the reasoning started, and any subsequent 'evidence gathering' is rationalization."

- question: "What practical test can you apply to determine whether you have written the bottom line on a question, and what does the test reveal?"
  type: short-answer
  answer: "Specify in advance what evidence would change your conclusion. If you cannot name any such evidence — or if the evidence you name would have to be extraordinary while confirming evidence can be ordinary — you have likely written the bottom line. The test reveals whether your belief is held in a way that could, in principle, respond to the world."
  explanation: "The bottom-line problem is invisible from the inside — rationalization feels like reasoning. The test forces you to make your belief falsifiable in your own mind before evaluating evidence. If you find yourself unable to specify any conceivable evidence that would change your conclusion, that is a strong signal the conclusion is fixed and subsequent 'reasoning' is performance. A genuine reasoner can always describe, at least approximately, what the world would have to look like for them to be wrong."
```
