---
id: randomized-controlled-trials-development
title: Randomized Trials in Development Economics
domain: economics
course: development-economics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: hypothesis-testing-framework
  type: soft
tags:
- RCT
- evaluation
- methodology
stage: advanced
status: draft
---

# Randomized Trials in Development Economics

## Core Idea
RCTs isolate causal effects of development interventions by random assignment to treatment/control. Pioneered by Banerjee and Duflo, RCTs have evaluated microfinance, school fee elimination, health campaigns, and more. Results often surprise: negative or modest impacts on measures expected to respond. RCTs are expensive and cannot be done at scale or for all questions, but they have reshaped development practice by demanding evidence.

## Explainer

From your study of causal inference, you know the fundamental problem: we never observe what would have happened to a unit had it received the other treatment. The RCT's solution is elegant — if you randomly assign who gets the intervention, then on average the treatment and control groups are identical in every observable and unobservable way before the program begins. Any subsequent difference in outcomes must therefore be caused by the intervention. Random assignment transforms a selection problem into a simple comparison of means.

The power of this approach becomes clear when you consider what observational data cannot tell you. Suppose a development NGO gives microloans to a village and finds that loan recipients have higher incomes afterward. Did the loans cause higher incomes — or did the NGO target the most entrepreneurial households in the first place? **Selection bias** — the systematic difference between who chooses to participate and who doesn't — makes it impossible to know. An RCT bypasses this entirely by making participation a matter of chance, like a lottery. Now the group that won the lottery and the group that lost it are, in expectation, identical twins before the program starts.

The findings from major development RCTs have repeatedly surprised policymakers. Microfinance, long celebrated as a poverty-alleviation tool, showed modest or mixed effects on consumption and income in rigorous RCTs across India, Morocco, Bosnia, and Ethiopia — despite widespread belief in its transformative power. Deworming programs in Kenya, by contrast, showed large effects on school attendance at very low cost. The key lesson is that **external validity** — whether results from one context generalize to another — is always in question. An RCT tells you what worked in *this* population at *this* time with *this* implementation. Replication across contexts is required before drawing broad policy conclusions.

RCTs also have genuine limitations. Many important policy questions cannot be randomized — you cannot randomly assign countries to different institutions, or assign individuals to be born into poverty. Ethical constraints prevent randomizing access to essential services. **Spillover effects** (where control units are affected by the treatment through social networks or markets) violate the **SUTVA assumption** (Stable Unit Treatment Value Assumption) that underpins the causal interpretation. And because RCTs require large samples and careful logistics, they are expensive and slow — ill-suited to rapidly evolving policy environments. The hypothesis-testing framework you know provides the formal machinery: power calculations before the trial determine how large the sample must be to detect an effect of a given size, and the balance test after randomization checks whether treatment and control groups are indeed statistically comparable on baseline characteristics. Together these tools define the rigorous standards that have made RCTs the gold standard — and sparked ongoing debate about whether that gold standard crowds out other valuable forms of evidence.
