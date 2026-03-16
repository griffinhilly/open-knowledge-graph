---
id: response-time-analysis-in-testing
title: Response Time Analysis in Psychometric Testing
domain: psychology
course: psychometrics
prerequisites:
- id: item-response-functions
  type: hard
- id: classical-test-theory
  type: soft
tags:
- response-times
- item-analysis
- test-behavior
- speed-accuracy
- guessing
stage: advanced
status: draft
---

# Response Time Analysis in Psychometric Testing

## Core Idea
Response times provide additional information about test performance beyond accuracy alone. Unusually fast responses may indicate guessing, random responding, or careless errors; unusually slow responses suggest processing difficulty or uncertainty. Joint modeling of accuracy and speed via hierarchical response models can improve ability estimation, detect problematic response patterns, and identify test difficulty calibration issues.

## Explainer

From item response theory (IRT), you know that an item response function (IRF) characterizes the probability of a correct response as a function of a person's latent ability. This model uses only one piece of information per item: whether the person got it right. But in a computer-administered test, you also know *when* they got it right. Response time is a second data channel that carries information IRT's accuracy-only model cannot see — and it carries information about fundamentally different aspects of test behavior.

The central intuition is the **speed-accuracy tradeoff**: people can generally go faster by accepting more errors, or go slower to achieve greater accuracy. Under normal testing conditions, examinees make an implicit judgment about where to sit on this tradeoff. When you observe someone answering in 2 seconds on items that typically take 30 seconds, that unusual speed is a signal. It could mean they already knew the answer instantly (genuine mastery), or it could mean they were not engaging — guessing, selecting randomly, or clicking through. These two explanations have opposite implications for what their score means.

The **log-normal model for response times** is the most common measurement approach. Response times are right-skewed (most responses cluster near the mode, with a long tail of slow responses), and taking the log of response time produces an approximately normal distribution that can be modeled using familiar linear methods. In this framework, each person has a latent **speed parameter** (their general pace of responding) and each item has a **time intensity parameter** (how long it typically takes). Just as IRT models person ability and item difficulty on a common scale, hierarchical RT models place person speed and item time intensity on a common scale, allowing the two to be compared.

The diagnostic power emerges when you combine the accuracy model and the response time model. Consider four cells: fast-correct (mastery or lucky guess?), fast-incorrect (careless or random?), slow-correct (difficult but worked through), slow-incorrect (struggled and failed). IRT can distinguish some of these cases using item difficulty and ability estimates, but the RT information sharpens those distinctions considerably. A person who consistently answers fast-incorrect on hard items is almost certainly guessing; their accuracy-only IRT ability estimate is biased upward. Filtering out or downweighting aberrant response patterns before final ability estimation can meaningfully reduce that bias.

Response time analysis also has direct applications in test security. **Pre-knowledge** — when examinees have seen the items beforehand — produces a characteristic signature: faster-than-expected responses and higher-than-expected accuracy, particularly on items that are objectively difficult. A pattern of fast, correct responses on hard items is unlikely under honest test-taking and can flag potential item exposure. Similarly, **rapid guessing** on a subset of items (often near the end of a timed test) can be detected by identifying the transition point where an examinee's response times drop sharply, allowing their scores to be separated into engaged and disengaged response phases for more accurate scoring.
