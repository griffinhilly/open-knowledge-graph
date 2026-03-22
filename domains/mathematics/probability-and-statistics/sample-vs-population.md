---
id: sample-vs-population
title: Samples and Populations
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: mean-median-mode
  type: soft
- id: simple-probability
  type: soft
builds-toward:
- sampling-methods
- hypothesis-testing-fundamentals
- sampling-distributions
tags:
- statistics
- sampling
- population
- inference
- data-collection
stage: formal-systems
status: validated
---

# Samples and Populations

## Core Idea
A population is the entire group of interest in a study, while a sample is a subset of that population actually observed. Because populations are often too large or inaccessible to study in full, statistical inference uses sample data to draw conclusions about the population. The quality of those conclusions depends critically on how the sample was chosen — a biased sample produces misleading estimates no matter how large it is.

## How It's Best Learned
Ground the distinction in concrete scenarios: a Gallup poll samples ~1000 people to estimate opinions of millions. Have students identify populations and samples in news studies before moving to formal definitions. Discuss what makes a sample representative.

## Common Misconceptions
- Bigger is always better: a large but biased sample is worse than a smaller random one.
- Confusing the sample statistic (e.g., sample mean x̄) with the population parameter (μ).
- Assuming any sample is automatically representative.

## Explainer

The distinction between a **population** and a **sample** is the foundation of all statistical inference. The population is the entire group you want to understand — all registered voters in the United States, every lightbulb produced by a factory, the complete set of measurements a sensor could generate. The sample is the subset you actually observe. Because studying every member of a population is usually impossible (too expensive, too time-consuming, or physically inaccessible), statistics uses the sample to draw conclusions about the population. This leap from observed data to unobserved truth is what makes statistics both powerful and perilous.

The quality of any inference depends critically on **how the sample was selected**. A **random sample** gives every member of the population an equal (or known) chance of being included, so the sample's composition tends to reflect the population's. A **biased sample** systematically over-represents or under-represents certain subgroups, producing estimates that are consistently off in one direction. The classic cautionary tale is the 1936 Literary Digest poll, which surveyed 2.4 million people and predicted the wrong presidential winner. Its sampling frame — telephone directories and automobile registrations — over-represented wealthier households, introducing systematic bias that no amount of additional data could fix. A much smaller random sample by Gallup correctly predicted the outcome.

This illustrates a subtle but critical point: **sample size and sampling method solve different problems**. A larger sample reduces **sampling error** — the random fluctuation between any sample and the true population value. But it does nothing to reduce **bias** — the systematic distortion caused by a flawed selection method. Doubling the size of a biased sample just gives you a more precise estimate of the wrong thing. Conversely, a well-designed random sample of modest size can produce remarkably accurate estimates. National polls routinely estimate the opinions of hundreds of millions of people from samples of about 1,000 — and the mathematical framework of sampling distributions explains why this works.

The language of statistics formalizes the distinction with parallel notation. **Population parameters** — the true values you want to know — are denoted by Greek letters: μ for the population mean, σ for the population standard deviation, p for a population proportion. **Sample statistics** — the values you compute from observed data — are denoted by Roman letters: x̄ for the sample mean, s for the sample standard deviation, p̂ for a sample proportion. The entire enterprise of inferential statistics is about using sample statistics to estimate, test hypotheses about, and construct confidence intervals for the corresponding population parameters. Keeping the two conceptually separate — what you know (the sample) versus what you want to know (the population) — is the first discipline of statistical thinking.

## Questions

```yaml
- question: "A polling company calls 100,000 people using phone book listings to predict an election. A competitor polls 1,000 people selected by random digit dialing. Which poll is likely more accurate?"
  type: multiple-choice
  options:
    - "The 100,000-person poll — larger samples always produce more accurate estimates"
    - "The 1,000-person poll — random sampling eliminates the systematic bias that a phone-book list introduces"
    - "They are equally accurate — sample size is the only thing that matters for accuracy"
    - "The 100,000-person poll — once a sample is large enough, any sampling method works"
  answer: 1
  explanation: "This mirrors the famous 1936 Literary Digest poll, which surveyed 2.4 million people but still predicted the wrong winner because its list systematically over-represented wealthier, Republican-leaning households. A biased sampling frame produces systematically wrong estimates no matter how large the sample — you are just measuring the bias more precisely. Random sampling gives every member of the population an equal chance of selection, so the sample's composition reflects the population's. Size amplifies the quality of the method; it cannot fix a flawed one."

- question: "A researcher estimates the average American's height by surveying only members of an NBA fan forum. What is the primary flaw in this approach?"
  type: multiple-choice
  options:
    - "Sampling error — the natural variation that occurs between any sample and the population"
    - "Selection bias — systematically over-representing a non-representative subgroup of the population"
    - "Confounding — a third variable is interfering with the height measurements"
    - "Random error — unpredictable fluctuations in the measurement instrument"
  answer: 1
  explanation: "Selection bias occurs when the mechanism used to select the sample systematically excludes or over-represents certain groups. NBA fans skew male, younger, and — because NBA players are exceptionally tall — may be taller-than-average themselves. The sample is not drawn from the full population; it is drawn from a self-selected subset. This is distinct from sampling error, which is the unavoidable random variation even in a perfect random sample. Sampling error shrinks as n grows; selection bias does not — it is baked into the sampling method."

- question: "A sample of 10,000 people is always more representative of a population than a sample of 500 people."
  type: true-false
  answer: false
  explanation: "Sample size does not guarantee representativeness — the sampling method does. A 10,000-person sample drawn from phone book listings in one city will be less representative of the national population than a 500-person nationally stratified random sample. The Literary Digest's 2.4-million-person sample failed to predict FDR's landslide because of systematic selection bias. Bigger is better only when the sampling method is sound; more observations from a biased sample just give you a more precise estimate of the wrong thing."

- question: "Even a perfectly random sample will not exactly match the population — some difference between the sample statistic and the population parameter is always expected."
  type: true-false
  answer: true
  explanation: "This is sampling error (or sampling variability) — the unavoidable random fluctuation between a sample and the population it was drawn from. Even with perfect random sampling, you're observing a subset, and chance determines which individuals are selected. The sample mean x̄ will rarely equal the population mean μ exactly. This is why statistical inference exists: to quantify how much x̄ might differ from μ by chance, using tools like standard errors and confidence intervals. Sampling error shrinks as sample size grows, but it never reaches zero."

- question: "Why can a large biased sample lead to worse conclusions than a small random sample? Use a concrete example to illustrate."
  type: short-answer
  answer: "A biased sample systematically misrepresents the population in a specific direction. More observations from a biased sample just reinforce the same distortion with more false precision. A small random sample, by contrast, gives every population member an equal chance of selection, so it reflects the population's true diversity. Example: a 100,000-person survey of only urban residents would systematically underestimate rural support for a candidate, while a 500-person random national sample would capture rural and urban voters proportionally."
  explanation: "The key insight is that bias and sampling error are different problems. Sampling error is random — it averages out over many samples and shrinks with size. Bias is systematic — it does not average out and is not reduced by adding more biased observations. When you increase a biased sample, you increase your confidence in a wrong answer. This is why statisticians care so much about how samples are drawn, not just how large they are."
```
