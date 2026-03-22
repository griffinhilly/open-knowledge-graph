---
id: calibration-training
title: "Calibration Training"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: bayesian-thinking-in-practice
    type: hard
  - id: likelihood-ratios-and-belief-updates
    type: soft
  - id: the-lens-that-sees-its-flaws
    type: hard
  - id: overconfidence-metacognitive-illusions
    type: soft
builds-toward:
  - reference-class-forecasting
  - the-planning-fallacy
  - intellectual-humility-and-calibrated-uncertainty
tags: ["calibration", "forecasting", "metacognition", "probability"]
stage: advanced
status: draft
---

## Core Idea

A calibrated reasoner's stated confidence matches their empirical accuracy: when they say they are 70% confident, they are right about 70% of the time. Most people are systematically overconfident — their 90% confidence predictions come true only 60-70% of the time. Calibration training closes this gap through deliberate practice: making explicit probability estimates, tracking accuracy, and adjusting. Research shows that calibration improves with feedback and practice — professional forecasters like those in the Good Judgment Project achieve near-perfect calibration. Calibration is not about being uncertain about everything; it is about having uncertainty that matches reality.

## How It's Best Learned

Use calibration training apps or exercises: estimate probabilities for trivia questions, then check your accuracy at each confidence level. Plot a calibration curve (stated confidence vs. actual accuracy). Identify your typical bias (overconfidence or underconfidence) and consciously adjust. Practice regularly — calibration is a skill that improves with repetition, like any other.

## Common Misconceptions

- Calibration is not the same as accuracy — a calibrated person may be uncertain about many things, but their uncertainty is well-matched to their knowledge.
- Perfect calibration does not mean predicting 50% for everything — it means using the full range of probabilities and being right at the rate you predict.
- Calibration training is not about math — it is about developing an honest internal sense of how much you actually know.

## Explainer

From your prerequisites, you know that Bayesian thinking means treating beliefs as probabilities and updating on evidence, and that the lens of rationality can examine its own flaws. Calibration training is where these ideas become empirically testable. The core question is simple: when you say you are 70% confident, are you right about 70% of the time? If the answer is yes, you are calibrated. If you are right only 50% of the time at stated 70% confidence, you are overconfident -- and research consistently shows that most people are.

The overconfidence gap is remarkably robust. Studies across domains -- trivia, forecasting, medical diagnosis, legal judgment -- find that people's 90% confidence intervals contain the true answer only 50-70% of the time. This is not a minor miscalibration; it means that events people consider near-certain regularly fail to occur. The Good Judgment Project, a large-scale forecasting tournament, demonstrated that this gap is closable: forecasters who received regular feedback on their calibration improved dramatically, achieving near-perfect calibration over time. The key was not raw intelligence or domain expertise but the feedback loop -- making predictions, checking results, and adjusting the internal sense of certainty.

The practical mechanics are straightforward. You make explicit probability estimates for questions where you can later check the answer: trivia questions, project completion dates, weather predictions, election outcomes. You record your estimates, sorted by confidence level, and after enough predictions you plot a calibration curve -- stated confidence on one axis, actual accuracy on the other. Perfect calibration is a 45-degree line; most people's curves reveal overconfidence (the accuracy line sits below the confidence line). Once you see your curve, you know which direction to adjust: if your 90% predictions come true only 70% of the time, you learn to mentally downgrade what feels like 90% to roughly 70%.

Calibration is distinct from accuracy, and this distinction matters. A person who says "50% confident" on every question and gets half right is perfectly calibrated but not very useful -- they are not discriminating between what they know and what they do not. A well-calibrated expert uses the full range of probabilities: 95% for well-established facts, 60% for educated guesses, 30% for things they think are probably wrong. The goal is not uniform uncertainty but honest probability estimation -- being as confident as the evidence warrants, no more and no less. This is why calibration training is foundational to the entire applied rationality project: it converts abstract commitment to "proportioning belief to evidence" into a measurable, improvable skill.

## Questions

```yaml
- question: "A weather forecaster expresses '70% confidence of rain' on 100 different occasions. It actually rains on 72 of those days. How should we assess this forecaster's calibration?"
  type: multiple-choice
  options:
    - "Well-calibrated — 72% actual accuracy closely matches the stated 70% confidence"
    - "Overconfident — the forecaster should have said 72% to match reality exactly"
    - "Underconfident — since it rained more often than predicted, the forecaster was too conservative"
    - "Not calibrated, because calibration requires achieving 100% accuracy on confident predictions"
  answer: 0
  explanation: "A calibrated forecaster's stated confidence matches their empirical accuracy — when they say 70%, they should be right about 70% of the time. This forecaster said 70% and was right 72% of the time — an excellent match. Calibration is not about being right every time; it is about having stated confidence track actual accuracy across many predictions. The 2% gap is negligible over 100 predictions. Option B misunderstands calibration as requiring perfect post-hoc adjustment rather than prospective accuracy-matching."

- question: "A person states 90% confidence on 50 trivia questions and gets 32 correct (64%). This pattern most likely reflects:"
  type: multiple-choice
  options:
    - "Poor accuracy — they should study more before answering"
    - "Overconfidence — their stated confidence (90%) substantially exceeds their empirical accuracy (64%)"
    - "Good calibration — 90% confidence is an aspirational target, not a prediction"
    - "Underconfidence — they were being too modest about what they know"
  answer: 1
  explanation: "Overconfidence is the most common and well-documented calibration failure. When someone says they are 90% confident but is only right 64% of the time, their internal sense of certainty is systematically inflated relative to their actual knowledge. Research consistently shows that people's 90% confidence intervals contain the true answer only 50-70% of the time. This is not about accuracy per se — you can be low-accuracy but well-calibrated (saying 50% confidence when you're right 50% of the time). The problem here is the *gap* between stated confidence and actual accuracy."

- question: "A well-calibrated person who is uncertain about many things would express 50% confidence on questions they don't know, to signal that they're essentially guessing."
  type: true-false
  answer: false
  explanation: "This is a common misconception about calibration. Perfect calibration does not mean collapsing to 50% on uncertain questions — it means using the full probability range and having each stated level match reality. A calibrated person might say 55% when they lean slightly toward one answer, 75% when they have good reasons to be fairly confident, and 30% when they lean the other way. Saying 50% for everything would actually be poor calibration on questions where you have any relevant evidence. The goal is honest probability estimation, not uniform uncertainty."

- question: "Calibration is a learnable skill that improves with deliberate practice and feedback on the accuracy of your predictions."
  type: true-false
  answer: true
  explanation: "Research from forecasting tournaments (like the Good Judgment Project) and calibration training studies shows that calibration is trainable. Forecasters who receive regular feedback on their accuracy — especially structured feedback that shows their calibration curves — improve systematically over time. Making explicit probability estimates, tracking results by confidence level, and adjusting based on observed patterns is enough to close much of the overconfidence gap. This is in contrast to many cognitive biases that are highly resistant to training."

- question: "Why is calibration distinct from accuracy, and why does a calibrated but low-accuracy person still possess something valuable that an uncalibrated high-accuracy person lacks?"
  type: short-answer
  answer: "Accuracy measures how often you are right; calibration measures whether your stated confidence matches how often you are right. A calibrated but low-accuracy person knows what they don't know — they say 55% when they're 55% likely to be correct, 30% when they're probably wrong. This self-knowledge is valuable for decision-making: others can trust their uncertainty signals and make appropriate use of their estimates. An uncalibrated high-accuracy person may be right often, but expresses false certainty — saying 95% when they're right only 70% of the time — which leads others (and themselves) to over-rely on their judgments. Calibration is the reliability of uncertainty estimates, not the reliability of the estimates themselves."
  explanation: "The distinction matters most in collaborative and high-stakes contexts. When doctors, engineers, or analysts communicate confidence, decision-makers downstream use those signals to allocate caution, gather more data, or commit to a course of action. An uncalibrated expert who expresses 95% certainty when 70% is accurate will cause systematic over-commitment. A calibrated expert communicates actionable uncertainty even when their knowledge is limited."
```
