---
id: analogy-strength-evaluation
title: 'Analogical Arguments: Strength and Weakness'
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: analogical-reasoning
  type: hard
- id: inductive-reasoning
  type: soft
builds-toward:
- informal-fallacies-intro
tags:
- analogies
- induction
- argument-evaluation
stage: formal-systems
status: draft
---

# Analogical Arguments: Strength and Weakness

## Core Idea
An analogical argument reasons: 'A and B are similar in respects X, Y, and Z. A has property P. Therefore, B likely has property P.' The strength of the analogy depends on the number of relevant shared properties, how similar the objects are overall, the irrelevance of known differences, and how direct the connection is between shared properties and the target property.

## How It's Best Learned
Compare strong vs. weak analogies (e.g., 'Planets orbit stars like electrons orbit nuclei' works for some purposes but fails for others). Identify relevant similarities and irrelevant differences. Show how same analogy can be strong or weak depending on context.

## Common Misconceptions
Thinking analogies must be perfect or point-for-point to be useful. Not recognizing that analogies argue for probability, not certainty. Missing that relevance of similarities depends on what we're trying to conclude.

## Questions

```yaml
- question: "The analogy 'the eye is like a camera' is used to support two conclusions: (1) that both form inverted images on a light-sensitive surface, and (2) that both can be repaired when damaged. How does the analogy's strength differ?"
  type: multiple-choice
  options:
    - "The analogy is equally strong for both conclusions because the number of similarities is the same"
    - "Strong for (1) because the shared optical properties directly explain image formation; weak for (2) because eyes heal biologically and cameras don't — a directly relevant difference"
    - "Weak for both because eyes and cameras are too different at the molecular level"
    - "Analogy strength cannot be evaluated without counting all shared properties"
  answer: 1
  explanation: "Analogy strength is conclusion-dependent. For image formation, the structural parallels (lens, inverted projection, light-sensitive surface) are causally relevant to how images form — the shared properties explain the target claim. For repair, there is a directly relevant difference: biological tissues heal through cellular regeneration while cameras have no such mechanism. A relevant difference in the domain of the conclusion undermines the analogy even when many other similarities exist."

- question: "Which factor most directly weakens an analogical argument, even if the two things being compared share many properties?"
  type: multiple-choice
  options:
    - "The objects come from different categories (e.g., biological vs. mechanical)"
    - "There are more than ten observable differences between the objects"
    - "A difference in a property that is directly relevant to the specific conclusion being drawn"
    - "The analogy is based on a single source case rather than multiple cases"
  answer: 2
  explanation: "A relevant difference — one that specifically bears on the conclusion — is the most potent weakener of an analogy. Category differences (option A) and sheer number of differences (option B) don't automatically weaken an analogy if those differences don't connect to the conclusion. Option D (single source) is a real weakener but less decisive than a relevant difference. The question is always: does this difference matter for *this specific claim*?"

- question: "An analogical argument that draws on multiple independent source cases is generally stronger than one based on a single source case."
  type: true-false
  answer: true
  explanation: "Sample diversity strengthens analogical arguments. If a pattern holds across varied, independent cases, it is less likely to be a fluke specific to one context. An argument that sleep improves athletic performance is stronger if it holds for basketball, football, swimming, and endurance sports than if it is based only on basketball data — the pattern's persistence across diverse cases provides inductive support that it is genuine rather than context-specific."

- question: "The more properties two things share, the stronger any analogy between them, regardless of which conclusion is being drawn."
  type: true-false
  answer: false
  explanation: "This is the central misconception about analogical reasoning. Shared properties strengthen an analogy only when they are relevant to the specific conclusion. Irrelevant similarities — however numerous — do not strengthen the argument. A human and a rock share many properties (both are material, both exist in time, both have mass), but this does nothing to support conclusions about cognition. Relevance is what matters, not the raw count of shared features."

- question: "Why must you specify the conclusion before you can judge whether an analogy is strong or weak?"
  type: short-answer
  answer: "Analogy strength is not a fixed property of the analogy itself — it is relative to the conclusion being drawn. The same shared properties may be highly relevant to one conclusion and irrelevant to another. To evaluate whether the similarities outweigh the differences, you need to know which similarities and differences are relevant — and relevance is defined by the conclusion. Without knowing what claim the analogy is supposed to support, you cannot determine which shared features count toward or against it."
  explanation: "The 'eye is like a camera' analogy is excellent for optics pedagogy and poor for biomedical repair reasoning — the same analogy, evaluated against different conclusions, has different strength. Evaluating an analogy always requires first asking: for *this conclusion*, do the relevant similarities between these cases outweigh the relevant differences? That question cannot be answered until the conclusion is specified."
```

## Explainer

From analogical reasoning and inductive logic, you already know the basic form: two things share some properties, so they probably share another. But knowing that analogies are inductive — probabilistic rather than certain — is only the beginning. The hard skill is diagnosing *how strong* a given analogy actually is. **Analogical argument strength** is not all-or-nothing; it lies on a spectrum determined by several independent factors that can pull in different directions.

The first factor is the **number and depth of relevant similarities**. An analogy gains strength from shared properties that are specifically connected to the conclusion you're drawing. The classic analogy "the eye is like a camera" supports conclusions about image formation but is weak for conclusions about repair, since eyes heal and cameras don't. Listing shared properties is not enough — you need shared properties that are relevant to the target claim. A second and equally important factor is the **absence of relevant differences**. If the two things being compared differ in a way that directly bears on what you're concluding, the analogy loses force even if the similarities are extensive. The eye-camera analogy is undermined for evolutionary conclusions precisely because cameras are designed and eyes were not.

A third factor is **sample diversity**: if the analogy draws on multiple independent source cases (not just one), it becomes stronger. "Professional athletes in basketball, football, and soccer all show improved performance after specific sleep interventions — so professional cyclists probably will too" is stronger than an analogy based on a single sport, because the pattern held across varied cases. A fourth factor is **directness of connection** — whether the shared properties are causally or constitutively related to the target property, or merely correlated with it. Shared body temperature between mammals and birds might support analogies about metabolic regulation (direct connection) but would be weak for analogies about social behavior (more indirect).

The deepest lesson is that **the same analogy can be strong or weak depending on the conclusion**. "Planets orbit stars like electrons orbit nuclei" was historically useful for generating predictions about electron shells, but it breaks down for wave-particle duality, quantum superposition, and orbital shape. When you encounter an analogical argument, the right question is not "is this analogy good or bad?" but rather "for this specific conclusion, do the relevant similarities outweigh the relevant differences?" That question requires knowing which similarities and differences are relevant — which in turn requires understanding the mechanisms involved, not just surface features.
