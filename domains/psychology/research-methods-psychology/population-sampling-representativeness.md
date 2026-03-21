---
id: population-sampling-representativeness
title: Populations, Sampling Methods, and Representativeness
domain: psychology
course: research-methods-psychology
prerequisites:
- id: research-design-selection-and-matching
  type: hard
- id: sampling-distributions-theory
  type: soft
builds-toward:
- statistical-power-and-effect-size-determination
tags:
- sampling
- populations
- generalizability
- representativeness
stage: formal-systems
status: draft
---

# Populations, Sampling Methods, and Representativeness

## Core Idea
The population is the full set to which inferences are desired; the sample is the subset studied. Probability sampling (random, stratified, systematic) provides known inclusion probabilities and supports statistical inference. Non-probability sampling (convenience, purposive) sacrifices representativeness but is practical. Sample representativeness on key variables enhances generalizability; bias in sampling limits it.

## How It's Best Learned
Specify a research population and design probability and non-probability sampling schemes. Evaluate how different sampling methods affect validity and generalizability. Calculate what percentage of a population you've sampled.

## Common Misconceptions
- Random sampling equals representative sampling; - Large samples are always representative; - Non-probability samples are invalid; - Statistical inference requires perfect representativeness.

## Questions

```yaml
- question: "The 1936 Literary Digest poll surveyed 10 million people but predicted the wrong presidential winner by a wide margin. What was the primary cause of this failure?"
  type: multiple-choice
  options:
    - "The sample was too small to detect the true preferences of the electorate"
    - "The sampling frame (telephone and car registration lists) systematically oversampled wealthier, Republican-leaning voters"
    - "The poll was conducted too far in advance of the election"
    - "The questions used were ambiguously worded, confusing respondents"
  answer: 1
  explanation: "The Literary Digest failure is a textbook case of sampling bias, not sample size. With 10 million respondents, size was not the problem. The sampling frame — people with telephones and cars in 1936 — systematically excluded lower-income voters who favored Roosevelt. The bias in *who* was selected overwhelmed the precision gained from large numbers. This illustrates the core principle: representativeness is about selection method, not volume."

- question: "A researcher wants to estimate the average anxiety level of adults in a large city. Which approach provides the strongest statistical basis for inference to the full population?"
  type: multiple-choice
  options:
    - "Survey 5,000 volunteers who respond to a public Facebook post"
    - "Survey every patient at the city's three largest mental health clinics"
    - "Draw a simple random sample of 800 adults from city registration records"
    - "Survey 10,000 university students at local campuses"
  answer: 2
  explanation: "Simple random sampling from a complete sampling frame gives every adult a known, equal probability of inclusion — the condition required for standard inferential statistics to be valid. Options A and D are convenience samples with systematic biases (social media users, students). Option B oversamples people already seeking mental health treatment, severely biasing the estimate upward. A smaller random sample (800) outperforms a larger biased sample (5,000 or 10,000) for accurate population inference."

- question: "A convenience sample of 10,000 participants is necessarily more representative of the population than a random sample of 1,000 participants."
  type: true-false
  answer: false
  explanation: "Representativeness depends on *how* participants are selected, not *how many* are selected. A large convenience sample can be systematically biased — overrepresenting certain demographic groups — in ways that a smaller random sample avoids. The Literary Digest poll exemplifies this: 10 million biased respondents produced a worse estimate than a well-designed smaller random sample. Sample size increases precision (reduces sampling error) only if the sample is unbiased in the first place."

- question: "Non-probability sampling methods (e.g., convenience samples, purposive samples) can be appropriate and valid for some research purposes."
  type: true-false
  answer: true
  explanation: "Non-probability samples are not inherently invalid — they are inappropriate for making precise population-level statistical inferences, but they serve many legitimate research purposes. Exploratory research, hypothesis generation, studies of rare or hard-to-reach populations, qualitative research, and initial pilot testing often rely on purposive or convenience sampling. The key is honesty: results should be explicitly bounded to the sample or similar populations, rather than overgeneralized to groups not represented in the sample."

- question: "Why can a well-drawn random sample of 1,000 people produce more accurate population estimates than a convenience sample of 100,000 people?"
  type: short-answer
  answer: "A random sample gives every member of the population a known, equal chance of selection, so the resulting sample's statistics are unbiased estimates of population parameters. A convenience sample systematically over- or under-represents certain groups, introducing bias that does not shrink as sample size grows — more observations from a biased process just give a more precise estimate of the wrong thing."
  explanation: "Statistical inference theory assumes random selection: confidence intervals, significance tests, and sampling distributions are derived under the assumption that each observation is drawn randomly from the population. A convenience sample violates this assumption, so the inferential machinery doesn't apply. Large biased samples are like measuring with a miscalibrated ruler many times — you get more precise measurements, but they're all wrong in the same systematic direction. Randomization ensures the errors are unsystematic and average out."
```

## Explainer

Every empirical study begins with a fundamental question: who are we studying, and who do we want our conclusions to apply to? The **population** is the full set of individuals, events, or observations to which you want to generalize. The **sample** is the subset you actually study. The relationship between them — and how that relationship was constructed — determines the generalizability of everything you conclude.

**Probability sampling** methods give each member of the population a known, nonzero probability of being selected. **Simple random sampling** is the foundation: every individual has an equal chance of selection, which allows you to use standard inferential statistics — sampling distributions, confidence intervals, and significance tests — in their textbook form, because the theoretical assumptions underlying those tools require random selection. **Stratified sampling** divides the population into subgroups (strata such as age, gender, or region) and samples randomly within each, ensuring proportional representation of key variables even with moderate sample sizes. **Systematic sampling** selects every kth person from an ordered list — practical when a list exists and the ordering is unrelated to the outcome. All probability methods share a crucial property: selection is governed by chance, not judgment, so sample estimates are unbiased estimates of population parameters.

**Non-probability sampling** includes convenience samples (whomever is available and willing), purposive samples (selected for specific characteristics), and snowball samples (participants recruit others from their networks). These are common in psychology — undergraduate participant pools, clinic populations, online panels — and they are not inherently invalid. But they require honesty about generalizability limits. A convenience sample of university students may generalize well to similar populations but poorly to older adults, rural communities, non-Western cultures, or people with limited education. The now-famous WEIRD critique (Western, Educated, Industrialized, Rich, Democratic) of psychology's participant base is fundamentally a sampling argument: if most published research draws from a narrow slice of humanity, conclusions cannot be claimed to describe universal human psychology.

The most important misconception to overcome is confusing **large sample size** with **representativeness**. A famous historical example: the Literary Digest predicted a landslide win for Alf Landon in the 1936 US presidential election based on a survey of 10 million people — one of the largest polls ever conducted. Franklin Roosevelt won by the largest Electoral College margin in over a century. The poll failed not because it was too small but because it drew from telephone directories and car registration lists, systematically oversampling wealthy, Republican-leaning voters. Representativeness is a question of *who* is selected and how, not how many. A well-drawn random sample of 1,000 routinely outperforms a convenience sample of 1,000,000 for accurate population inference.
