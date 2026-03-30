---
id: epidemiology-foundations
title: Foundations of Epidemiology
domain: health-and-human-development
course: public-health
prerequisites:
- id: infectious-disease-epidemiology
  type: soft
- id: population-ecology-intro
  type: soft
builds-toward:
- disease-frequency-measures
- epidemiologic-study-designs
- outbreak-investigation
tags:
- epidemiology
- public-health
- foundations
stage: formal-systems
status: validated
---

# Foundations of Epidemiology

## Core Idea
Epidemiology is the study of how disease and health outcomes are distributed across populations and what factors influence that distribution. The field asks three core questions: Who gets sick? Where and when does illness occur? Why does it occur? Epidemiologists use systematic observation, natural experiments, and controlled studies to identify causes of disease and inform interventions. The discipline bridges basic science and public health policy by translating population-level patterns into actionable guidance.

## How It's Best Learned
Start with classic case studies like John Snow's cholera investigation, which illustrates the core logic of mapping disease distribution to identify causes. Practice distinguishing person, place, and time variables, and discuss how each informs a different type of public health intervention.

## Common Misconceptions
- Epidemiology is not just statistics; it requires causal reasoning about biology, behavior, and environment.
- 'Risk' in epidemiology is a probability over a defined population and time window, not an individual-level guarantee.
- Correlation in epidemiologic data does not establish causation without application of criteria like Bradford Hill.

## Questions

```yaml
- question: "John Snow's cholera investigation is a foundational example in epidemiology. What was the core reasoning that identified the Broad Street pump as the source?"
  type: multiple-choice
  options: ["He ran a randomized controlled trial comparing pump water to river water", "He mapped disease distribution across persons and places and traced cases back to a common exposure", "He applied Bradford Hill criteria to a large administrative dataset", "He identified the Vibrio cholerae bacterium under a microscope"]
  answer: 1
  explanation: "Snow mapped who got sick and where they lived, revealing that cases clustered around the Broad Street pump. This is pure epidemiologic logic: using the distribution of disease across person, place, and time to identify a likely cause. He didn't know the pathogen — his reasoning was distributional and causal, not microbiological."

- question: "A study finds that people who carry lighters have higher rates of lung cancer. This correlation alone is sufficient to conclude that carrying lighters causes lung cancer."
  type: true-false
  answer: false
  explanation: "Correlation does not establish causation. Carrying lighters is associated with smoking, which causes lung cancer — a classic confounding relationship. Epidemiology uses criteria like Bradford Hill (strength, consistency, temporality, plausibility, dose-response) to evaluate whether an association is likely causal, not correlation alone."

- question: "Why does epidemiology define 'risk' at the population level rather than as a prediction for a specific individual?"
  type: short-answer
  answer: "Risk is a probability estimated from observed rates in a defined population over a defined time window. It cannot tell you whether a specific individual will develop a disease — only that a person with certain characteristics faces a given probability. Individual outcomes are influenced by factors unmeasured in any study."
  explanation: "Epidemiologic risk is an aggregate measure: the proportion of a population that develops disease given exposure. Translating population risk to individual prediction requires strong assumptions and additional information. Conflating population risk with individual fate is a frequent misapplication of epidemiologic findings."
```

## Explainer

Epidemiology asks a deceptively simple question: why do some people get sick and others don't? To answer it systematically, the field developed a framework built around three axes of description — **person** (who gets sick?), **place** (where does illness cluster?), and **time** (when does it occur and how does it change?). Every epidemiologic investigation starts by mapping a health outcome along these dimensions. Patterns that emerge — a spike in cases among factory workers, a geographic cluster near a water source, an outbreak that follows a point exposure — generate hypotheses about causes.

John Snow's 1854 cholera investigation in London is the classic demonstration. Snow didn't know what caused cholera; germ theory didn't yet exist. But he mapped cases onto a street grid and noticed they clustered around the Broad Street pump. By removing the pump handle, he stopped the outbreak. His reasoning was entirely epidemiologic: distribution of disease → hypothesis about exposure → intervention → test. The lesson isn't that Snow was lucky — it's that the distributional logic works even without knowledge of the underlying mechanism.

The distinction between **correlation and causation** is where epidemiology gets rigorous. Finding that coffee drinkers have lower rates of Parkinson's disease doesn't mean coffee is protective — it might reflect that people with early Parkinson's symptoms give up coffee first (reverse causation), or that some third factor explains both. The Bradford Hill criteria — including strength of association, consistency across studies, biological plausibility, dose-response relationship, and above all *temporality* (cause must precede effect) — provide a framework for evaluating whether an association is likely causal.

**Risk** in epidemiology is a population-level probability: if 40 out of 1,000 exposed people develop a disease, the risk is 4%. This is not a statement about any individual — it can't tell you whether *you* will get sick. Risk estimates come from measured rates in defined populations during defined time windows, and they always carry uncertainty. Conflating population risk with individual destiny is one of the most common ways epidemiologic findings are misused in public communication.

From here, the field branches into study designs — cohort studies, case-control studies, randomized trials, cross-sectional surveys — each suited to different questions and each with characteristic strengths and biases. Epidemiology is simultaneously a quantitative discipline and a causal reasoning discipline; mastering it requires both statistical fluency and the ability to reason about how diseases actually propagate through populations.
