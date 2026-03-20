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

## Explainer

From your study of inductive arguments, you know that inductive strength depends on how well evidence supports a conclusion — not just whether evidence exists, but how much there is, how representative it is, and how reliable the measurement is. **Statistical reasoning** makes those criteria precise. Statistics provides the formal tools for asking: how confident should I be that a pattern in my sample reflects the real world?

The foundational concept is the difference between a **sample** and a **population**. A population is every instance of whatever you're studying; a sample is the subset you actually observe. Conclusions about populations based on samples are always uncertain — the question is how much. **Sample size** directly affects this uncertainty. Larger samples reduce **sampling error**, the random variation between your sample result and the true population value. A poll of 100 voters might have a margin of error of ±10 percentage points; a poll of 1,000 might have ±3. But size is only half the story.

**Representativeness** is equally important and harder to guarantee. A sample of 1 million people who all volunteered to participate tells you less about a general population than a well-drawn random sample of 1,000. This is why **selection bias** can make large samples worse than useless — they give false confidence. The famous 1936 Literary Digest poll that predicted a Landon landslide was based on 10 million responses but surveyed primarily car owners and telephone subscribers, missing the very voters who elected Roosevelt. Size cannot fix bias.

The concept your prerequisite work prepared you for is applying **base rates**. When evaluating a statistical claim, always ask: what's the background frequency? If a medical test is 99% accurate but the disease affects 1 in 10,000 people, a positive test result is still more likely a false positive than a true positive. This is the **base rate neglect** error — ignoring the prior probability and focusing only on the test's accuracy. Statistical significance works the same way: a finding is "significant" at p < 0.05 means you'd expect it to happen by chance once in twenty experiments — but if researchers run hundreds of tests and only publish the significant ones, you should expect false positives to dominate the literature. Evaluating statistical evidence requires asking not just "what did this study find?" but "what's the context that determines how much this finding should update my beliefs?"
