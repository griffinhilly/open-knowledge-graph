---
id: sampling-in-psychology
title: Sampling and Populations in Psychological Research
domain: psychology
course: research-methods-psychology
prerequisites:
- id: scientific-method-psychology
  type: hard
- id: sample-vs-population
  type: soft
- id: sampling-methods
  type: soft
builds-toward:
- descriptive-research-methods
- survey-research-methods
- inferential-statistics-psychology
tags:
- sampling
- population
- generalizability
- WEIRD
- random-sampling
stage: abstract-reasoning
status: validated
---

# Sampling and Populations in Psychological Research

## Core Idea
A population is the full group a researcher wants to understand; a sample is the subset actually studied. Sampling methods — random, stratified, convenience, snowball — differ in how well they produce representative samples, which determines the external validity of findings. A major criticism of psychology research is over-reliance on WEIRD samples (Western, Educated, Industrialized, Rich, Democratic), limiting generalizability. Sample size affects both the precision of estimates and statistical power.

## How It's Best Learned
Compare the same research question studied with a convenience sample versus a nationally representative sample. Predict how conclusions might differ and why.

## Common Misconceptions
- A large sample is not automatically representative — a large biased sample still yields biased conclusions.
- Random sampling (who is selected) is different from random assignment (who gets which condition).

## Questions

```yaml
- question: "A psychology study recruits 500 participants exclusively from introductory psychology courses at a U.S. university. The study finds that social comparison increases anxiety. What is the primary threat to the study's external validity?"
  type: multiple-choice
  options: ["The sample size is too small to detect true effects", "The sample is a convenience sample that may not represent the broader population", "The study lacks random assignment to conditions", "The anxiety measure may not be reliable"]
  answer: 1
  explanation: "The core issue is that the sample is drawn from a narrow, self-selected pool — undergraduate psychology students at a U.S. university — who differ systematically from the general population in age, education, cultural background, and many psychological characteristics. This threatens external validity (the ability to generalize findings). The other options address power, internal validity, and measurement reliability — real concerns, but secondary to the representativeness issue here."

- question: "A researcher surveys 50,000 people using an online opt-in panel. Because the sample is very large, the results can be generalized to the general population with confidence."
  type: true-false
  answer: false
  explanation: "Sample size and sample representativeness are independent. A 50,000-person opt-in online panel is a convenience sample biased toward people who are online, willing to take surveys, and aware of the platform — all of which correlate with many psychological variables. The famous 1936 Literary Digest poll predicted Roosevelt would lose using 2.4 million respondents; he won by a landslide. Systematic bias in who is sampled cannot be corrected by collecting more of the same biased data."

- question: "What is the WEIRD problem in psychology research, and why does it matter for the field?"
  type: short-answer
  answer: "WEIRD stands for Western, Educated, Industrialized, Rich, Democratic — the narrow slice of humanity that most psychology studies sample from. It matters because findings from WEIRD samples are often assumed to be universal but may not replicate across cultures."
  explanation: "Henrich, Heine, and Norenzayan (2010) showed that the typical psychology sample — North American undergraduates — is a statistical outlier on many cognitive, social, and perceptual variables, not a representative human. Studies on visual perception, fairness norms, individualism/collectivism, and many other topics show large cross-cultural variation. Treating WEIRD findings as universal laws of human psychology risks exporting cultural particulars as scientific universals."
```

## Explainer

Every empirical psychology study begins with an implicit or explicit claim: "here is something true about people." But the people actually studied are almost never "people in general" — they are a specific subset, a sample, drawn from a larger population the researcher cares about. Understanding sampling means understanding the chain between the people in your study and the people you want to say something about.

The ideal is a probability sample — one in which every member of the target population has a known, nonzero chance of being selected. A simple random sample (like drawing names from a hat) achieves this for a defined list. A stratified random sample divides the population into subgroups (strata) and samples randomly within each, ensuring minority groups are adequately represented. These methods are expensive and logistically difficult, which is why most psychology research instead uses convenience samples: whoever is available. In practice, this usually means introductory psychology students, who participate for course credit. Such samples are fast and cheap but structurally unrepresentative.

The WEIRD problem names the systematic bias that results. Henrich, Heine, and Norenzayan documented that the typical psychology participant is Western, Educated, Industrialized, Rich, and Democratic — characteristics that correlate with unusual patterns on perceptual tasks, fairness judgments, and social cognition relative to the rest of the world. Research built on WEIRD samples generates findings that may be specific to that cultural context but are framed as universal. Recognizing this is not a condemnation of all prior research — it is a call to replicate studies across cultures before assuming universality.

There is also a critical distinction between random sampling and random assignment. Random sampling concerns who is recruited into a study — it affects external validity and generalizability. Random assignment concerns who receives which experimental condition — it affects internal validity and causal inference. A study can have one without the other. A nationally representative survey has excellent random sampling but no random assignment; a tightly controlled lab experiment might have perfect random assignment but only a student convenience sample. Both matter, but they answer different questions.

Finally, sample size and sample quality are not the same thing. A large sample from a biased sampling frame is still a biased sample. Power analysis determines how large a sample you need to detect an effect of a given size — but it assumes you have a reasonably representative sample. Before worrying about sample size, you need to worry about whether the people in your study resemble the people you want to draw conclusions about.
