---
id: statistical-reasoning-basics
title: Statistical Reasoning Basics
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: strength-of-inductive-arguments
  type: hard
builds-toward:
- correlation-and-causation-distinction
- reasoning-under-uncertainty
tags:
- statistics
- probability
- data-reasoning
stage: formal-systems
status: draft
---

# Statistical Reasoning Basics

## Core Idea
Sound statistical reasoning requires understanding concepts like sample size, distribution, representativeness, and margin of error. Misunderstanding these concepts leads to errors like overgeneralizing from small samples, ignoring base rates, or failing to account for natural variation. Statistics is not just mathematics; it is a tool for reasoning about evidence.

## How It's Best Learned
Work through concrete examples where sample size and representativeness vary. Calculate margins of error to see how sample size affects confidence. Compare polling errors, medical study results, and survey data to see statistical reasoning in practice.

## Common Misconceptions
Statistical significance means practical importance (a tiny effect can be statistically significant in large samples). A large sample guarantees accuracy (biased samples stay biased regardless of size). The average tells you about a typical case (averages can be misleading when distributions are skewed or multimodal).

## Questions

```yaml
- question: "A company surveys 500,000 customers via opt-in email and reports 88% satisfaction. A competitor surveys 2,000 randomly selected customers by phone and reports 71% satisfaction. Which survey more reliably estimates the true satisfaction level?"
  type: multiple-choice
  options:
    - "The company's survey, because 500,000 is a vastly larger sample"
    - "The competitor's survey, because random selection reduces selection bias more than raw sample size does"
    - "They are equally reliable since both used real customers"
    - "Neither can be reliable without knowing the full population size"
  answer: 1
  explanation: "Representativeness beats size when a sample is biased. The opt-in email survey systematically over-represents satisfied customers (dissatisfied ones are less likely to respond), so adding more biased observations just reinforces the wrong answer with greater precision. A well-drawn random sample of 2,000 gives each customer equal inclusion probability, producing an unbiased estimate. The 1936 Literary Digest poll (10 million responses, catastrophically wrong) is the canonical example of size failing to fix bias."

- question: "A medical test is 99% accurate. The disease it screens for affects 1 in 1,000 people. If a randomly selected person tests positive, approximately what is the probability they actually have the disease?"
  type: multiple-choice
  options:
    - "About 99%, since the test is 99% accurate"
    - "About 50%, since a test is either right or wrong"
    - "About 9%, because the low base rate means most positives are false positives"
    - "About 0.1%, equal to the disease prevalence"
  answer: 2
  explanation: "This is the base rate neglect problem. Out of 1,000 people: roughly 1 has the disease (true positive with 99% chance ≈ 1 person) and 999 do not (false positive rate of 1% ≈ 10 people). So about 11 people test positive, and only 1 of those ~11 actually has the disease — roughly 9%. The test's accuracy sounds impressive but is swamped by the rarity of the disease. Ignoring the base rate leads to wildly overestimating what a positive result means."

- question: "A study with 100,000 participants finds a statistically significant difference between two groups (p < 0.001). This means the difference is practically important."
  type: true-false
  answer: false
  explanation: "False — statistical significance only means the result is unlikely to have arisen by chance at the chosen threshold. With 100,000 participants, even a trivially small difference (say, a 0.01% improvement) can reach p < 0.001. The p-value says nothing about whether the effect is large enough to matter in the real world. Effect size — how big the difference actually is — determines practical importance. 'Significant' in statistics means 'detectable,' not 'meaningful.'"

- question: "A random sample of 1,000 people is generally more reliable than a convenience sample of 100,000 people for estimating a population proportion."
  type: true-false
  answer: true
  explanation: "True — a convenience sample systematically excludes or over-represents certain groups, producing a biased estimate regardless of size. Adding more observations from the same biased pool does not correct the bias; it reinforces it. A well-drawn random sample of 1,000 gives each population member equal inclusion probability, making it representative and its error quantifiable (margin of error ≈ 1/√1000 ≈ ±3%). Larger but biased samples give precise estimates of the wrong thing."

- question: "Explain why a biased sample of one million people may give worse results than a random sample of one thousand people."
  type: short-answer
  answer: "Bias is a systematic error — the sample consistently mis-represents the population regardless of size. Adding more biased observations doesn't reduce the error; it just makes you more confident in the wrong answer. A random sample of 1,000 has only random (unsystematic) sampling error, which averages out and is quantifiable via margins of error. The biased sample produces a precise estimate of the wrong quantity. Size reduces random error; it cannot fix systematic error."
  explanation: "The Literary Digest example illustrates this perfectly: 10 million responses from car and telephone owners in 1936 systematically missed the voters who actually elected Roosevelt. More data from the same biased pool just compounded the false confidence. Representativeness determines whether your sample asks the right question; size determines how precisely you answer it."
```

## Explainer

From your study of inductive arguments, you know that inductive strength depends on how well evidence supports a conclusion — not just whether evidence exists, but how much there is, how representative it is, and how reliable the measurement is. **Statistical reasoning** makes those criteria precise. Statistics provides the formal tools for asking: how confident should I be that a pattern in my sample reflects the real world?

The foundational concept is the difference between a **sample** and a **population**. A population is every instance of whatever you're studying; a sample is the subset you actually observe. Conclusions about populations based on samples are always uncertain — the question is how much. **Sample size** directly affects this uncertainty. Larger samples reduce **sampling error**, the random variation between your sample result and the true population value. A poll of 100 voters might have a margin of error of ±10 percentage points; a poll of 1,000 might have ±3. But size is only half the story.

**Representativeness** is equally important and harder to guarantee. A sample of 1 million people who all volunteered to participate tells you less about a general population than a well-drawn random sample of 1,000. This is why **selection bias** can make large samples worse than useless — they give false confidence. The famous 1936 Literary Digest poll that predicted a Landon landslide was based on 10 million responses but surveyed primarily car owners and telephone subscribers, missing the very voters who elected Roosevelt. Size cannot fix bias.

The concept your prerequisite work prepared you for is applying **base rates**. When evaluating a statistical claim, always ask: what's the background frequency? If a medical test is 99% accurate but the disease affects 1 in 10,000 people, a positive test result is still more likely a false positive than a true positive. This is the **base rate neglect** error — ignoring the prior probability and focusing only on the test's accuracy. Statistical significance works the same way: a finding is "significant" at p < 0.05 means you'd expect it to happen by chance once in twenty experiments — but if researchers run hundreds of tests and only publish the significant ones, you should expect false positives to dominate the literature. Evaluating statistical evidence requires asking not just "what did this study find?" but "what's the context that determines how much this finding should update my beliefs?"
