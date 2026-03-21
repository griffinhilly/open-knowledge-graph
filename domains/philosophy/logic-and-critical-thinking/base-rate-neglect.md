---
id: base-rate-neglect
title: Base Rate Neglect
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: inductive-reasoning
  type: hard
- id: evaluating-evidence
  type: soft
tags:
- base-rate
- probability
- cognitive-bias
- reasoning
stage: formal-systems
status: draft
---

# Base Rate Neglect

## Core Idea
Base rate neglect is the tendency to ignore prior probabilities (how common something is in the population) when evaluating specific evidence. The classic example is medical testing: a test that is 99% accurate sounds highly reliable, but if the disease affects only 1 in 10,000 people, a positive result is far more likely to be a false positive than a true positive. The prosecutor's fallacy commits the same error in legal contexts, confusing the probability of the evidence given innocence with the probability of innocence given the evidence. Correcting for base rates requires combining prior probability with the strength of new evidence — the core logic behind Bayes' theorem.

## How It's Best Learned
Work through the medical testing example with actual numbers: if 10,000 people are tested, how many true positives and false positives result? Visual aids like natural frequency trees make the math intuitive. Then apply the same reasoning to legal, security screening, and everyday probability scenarios.

## Common Misconceptions
- Thinking that a highly accurate test guarantees a correct diagnosis — accuracy must be weighed against how rare the condition is.
- Believing base rate neglect is a 'math problem' rather than a reasoning problem; the error arises from intuitive judgment, not from inability to do arithmetic.

## Questions

```yaml
- question: "A disease affects 1 in 10,000 people. A test for it is 99% sensitive (correctly detects the disease) and 99% specific (correctly rules it out). You test positive. Roughly what is the probability you actually have the disease?"
  type: multiple-choice
  options:
    - "About 99%, because the test is 99% accurate"
    - "About 50%, because a positive result is equally likely to be true or false"
    - "About 1%, because false positives vastly outnumber true positives given the disease's rarity"
    - "About 0.01%, because only 1 in 10,000 people have the disease"
  answer: 2
  explanation: "In 10,000 people: ~1 has the disease, detected correctly (true positive). Of the 9,999 healthy people, 1% — about 100 — test positive (false positives). So ~101 total positives, only 1 of which is a true positive: probability ≈ 1/101 ≈ 1%. The test is highly accurate, yet the positive predictive value is very low because the disease is so rare. The intuitive answer (option A) is the base rate neglect error — ignoring how rare the condition is."

- question: "A prosecutor argues: 'The probability of a random person having the same DNA profile as the crime scene sample is 1 in 1,000,000. Therefore the defendant is almost certainly guilty.' What is wrong with this argument?"
  type: multiple-choice
  options:
    - "Nothing — a 1-in-a-million probability of an innocent match is overwhelming evidence of guilt"
    - "It confuses P(DNA match | innocent) with P(innocent | DNA match), ignoring the base rate of how many people could match"
    - "DNA evidence is never reliable enough to use in court"
    - "The argument is valid only if the defendant had no alibi"
  answer: 1
  explanation: "This is the prosecutor's fallacy. P(DNA match | innocent) = 1/1,000,000 is the probability of finding this evidence if the person is innocent — not the probability of innocence given the evidence. To compute P(innocent | DNA match), you need Bayes' theorem, which requires knowing the base rate: in a city of 1 million people, roughly 1 person besides the perpetrator matches by chance. The posterior probability of guilt is far lower than the 'overwhelming' 999,999/1,000,000 the argument implies."

- question: "A test that is 95% accurate will correctly diagnose 95% of people who test positive."
  type: true-false
  answer: false
  explanation: "'95% accurate' typically means 95% sensitivity and/or specificity — the probability the test correctly identifies those who have or don't have the condition. The probability that a positive test result is correct (positive predictive value) depends also on the base rate of the condition. When the condition is rare (say, 1 in 10,000), even a 95% accurate test will generate far more false positives than true positives, and the chance that a positive result is correct can be well below 95%."

- question: "The base rate of a condition in the relevant population affects how much weight you should give to a positive test result for that condition."
  type: true-false
  answer: true
  explanation: "This is the core lesson of base rate reasoning. Bayes' theorem formalizes it: the posterior probability of a hypothesis depends on both the prior probability (the base rate) and the likelihood ratio of the evidence. A low base rate can dramatically reduce the posterior probability even when evidence is strong. Ignoring the base rate — treating only the test's accuracy as relevant — is the defining error of base rate neglect."

- question: "Explain why a highly accurate test can still produce mostly false positives, and what factor is responsible."
  type: short-answer
  answer: "Test accuracy describes performance at the individual level — how often the test is correct given whether someone has the condition. But when a condition is rare in the population, the vast majority of people tested are healthy. Even a small false positive rate (say 1%) applied to a large pool of healthy people generates many false positives, while the true positive rate (say 99%) applied to the tiny group with the condition generates few true positives. The ratio of false to true positives is determined by the base rate: the rarer the condition, the more false positives overwhelm true positives, regardless of test accuracy."
  explanation: "The responsible factor is the prior probability — how common the condition is before the test is applied. High test accuracy only guarantees correct results conditional on knowing who has the condition. When the prior is low, Bayes' theorem tells us the posterior probability of disease remains low even after a positive test."
```

## Explainer

From your work on inductive reasoning, you know that strong inductive arguments are those where the premises make the conclusion probable. Base rate neglect is a systematic failure of this principle — a way of reasoning that *feels* inductively strong but is actually weak because a crucial premise (the prior probability) has been ignored. The specific evidence grabs attention; the background frequency of the phenomenon quietly disappears from the calculation.

The canonical example makes the structure vivid. Suppose a disease affects 1 person in 10,000. A test for it is 99% accurate: if you have the disease, the test detects it 99% of the time; if you don't, the test is positive only 1% of the time (a false positive). You test positive. How worried should you be? Intuition says "very worried — the test is 99% accurate." But consider 10,000 people: about 1 has the disease, correctly identified by the test. Of the 9,999 healthy people, 1% — roughly 100 — also test positive. So out of approximately 101 positive results, only 1 is a true positive. The probability you actually have the disease given a positive result is roughly 1%. The test is highly accurate; you are almost certainly still healthy. This counterintuitive result is entirely driven by the **prior probability** — how rare the disease is before the test is applied.

The formal structure here is **Bayes' theorem**: the probability of a hypothesis given evidence depends on three things — the prior probability of the hypothesis (how common the disease is), the likelihood of the evidence given the hypothesis (the true positive rate), and the likelihood of the evidence overall (including false positives). Base rate neglect is the failure to weight by the prior. The evidence — a positive test — gets all the reasoning power, and the rarity of the disease gets none. When the prior is very low, even highly diagnostic evidence can barely shift the posterior probability.

The **prosecutor's fallacy** applies the same mistake in legal reasoning. A prosecutor might argue: "The probability of finding this DNA match if the defendant is innocent is 1 in a million — therefore the defendant is almost certainly guilty." But this substitutes P(evidence | innocent) for P(guilty | evidence). The latter requires knowing the base rate of the relevant profile in the population — how many people could have produced a matching sample. In a large city, even a 1-in-a-million coincidental match probability means another person might match by chance, and the posterior probability of guilt can be far lower than 1-in-a-million suggests. Recognizing base rate neglect means habitually asking: before seeing this evidence, how probable was the hypothesis? The answer always matters.
