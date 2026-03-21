---
id: evaluating-inductive-evidence
title: Evaluating Evidence in Inductive Arguments
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: inductive-reasoning
  type: hard
- id: inductive-strength-and-weakness
  type: hard
builds-toward:
- probabilistic-reasoning
- evaluating-evidence
tags:
- inductive-reasoning
- evidence-evaluation
- critical-thinking
stage: formal-systems
status: draft
---

# Evaluating Evidence in Inductive Arguments

## Core Idea
Evaluating inductive evidence requires assessing whether premises provide good support for conclusions. Key considerations: Is the sample representative? Is the sample size adequate? Are there alternative explanations? Systematic evaluation prevents accepting weak inductive arguments simply because conclusions feel plausible.

## Questions

```yaml
- question: "A polling organization surveys 10,000 people by calling landline telephone numbers and finds 65% support a policy. A student concludes: 'This is a very strong inductive argument — 10,000 is a huge sample.' What is the critical flaw in this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct; 10,000 is a reliable sample size for any population"
    - "The sample is large but systematically biased — landline users skew older and wealthier, so the procedure misrepresents the general population regardless of sample size"
    - "Telephone polling always produces weak evidence because people lie on the phone"
    - "65% support is too large a figure; any result above 60% should be treated with suspicion"
  answer: 1
  explanation: "This is the core insight: size cannot fix a biased sampling procedure. Landline-only polling systematically excludes mobile-only users, who tend to be younger, more urban, and less affluent — creating a directional error that grows larger with more data, not smaller. Representativeness is more fundamental than sample size. The law of large numbers reduces random error; it does nothing about systematic bias."

- question: "Researchers find a strong positive correlation between time spent on social media and depression rates. To support the causal claim that social media causes depression, the most persuasive additional evidence would be:"
  type: multiple-choice
  options:
    - "A larger study with 100,000 participants that replicates the same correlation"
    - "Testimonials from psychiatrists who believe social media harms mental health"
    - "A randomized experiment where participants are assigned to different social media usage levels, ruling out confounding variables"
    - "A meta-analysis averaging results from 50 correlation studies"
  answer: 2
  explanation: "Correlation studies — no matter how large or how many — cannot rule out confounding variables such as pre-existing depression, personality traits, or socioeconomic factors. Only random assignment to conditions allows researchers to isolate the effect of social media from confounds. Options A and D add more correlation data but not causal evidence. Option B is anecdotal, not systematic evidence."

- question: "A small but genuinely random sample can provide stronger inductive evidence than a large sample drawn from a biased sampling procedure."
  type: true-false
  answer: true
  explanation: "Representativeness is more fundamental than size. A random sample distributes sampling errors randomly, so they tend to cancel out across observations and the sample converges on the true population value with more data. A biased sample consistently overrepresents some groups, and adding more data from the same biased procedure just reinforces the same directional error. Size matters for reducing random variation; only an unbiased procedure can eliminate systematic error."

- question: "If a sample size is large enough, a biased sampling procedure will eventually produce representative results, because the law of large numbers guarantees convergence to the true population value."
  type: true-false
  answer: false
  explanation: "The law of large numbers guarantees convergence to the true mean when samples are drawn randomly. It does not apply to systematically biased procedures. A phone survey that calls only landlines consistently excludes mobile-only users — adding more calls just collects more data from the same skewed pool. No amount of data from a broken procedure repairs the procedure. The distinction between random error (reducible by more data) and systematic bias (not reducible by more data) is fundamental to understanding when sample size matters."

- question: "Explain the difference between random error and systematic bias in sampling, and why this distinction is fundamental to evaluating inductive evidence."
  type: short-answer
  answer: "Random error is variation that occurs by chance — any given sample might accidentally include slightly too many or too few members of a subgroup, but these errors vary in different directions across samples and tend to cancel out with more data. Systematic bias is a directional error built into the sampling procedure itself: it consistently overrepresents some groups and underrepresents others in the same direction every time. Because it is directional, it does not average out with larger samples. A phone survey that calls only landlines systematically excludes younger, more mobile-reliant populations no matter how many calls are made. This distinction matters because it determines what can fix the problem: random error is reduced by more data; systematic bias requires fixing the sampling procedure itself."
  explanation: "Students often assume that bigger samples are always better evidence. This is true only for random error. The harder and more practically important skill is recognizing when the sampling procedure itself introduces a directional distortion — which is the most common failure mode in real-world inductive arguments such as polls, studies, and surveys."
```

## Explainer

You already know that inductive arguments are not truth-preserving in the way deductive arguments are — even a strong inductive argument could have true premises and a false conclusion. And you know what it means for an inductive argument to be strong or weak: the premises either do or do not provide substantial support for the conclusion. What you are now learning is a practical toolkit for making that judgment systematically, case by case.

The first and most important question is **representativeness**: does the evidence reflect the population you are generalizing about? Suppose you survey 500 university students about political attitudes and draw conclusions about the general public. Your sample is large, but it's drawn from a narrow demographic with unusual characteristics — young, educated, mostly urban. The size of the sample doesn't matter if the sample systematically misrepresents the population. Representativeness failures are often invisible because the sample seems "normal" from inside the sampling process. This is why statisticians use random sampling: it distributes sampling errors randomly rather than systematically in one direction.

**Sample size** is the second consideration, and it interacts with representativeness. A small but genuinely random sample can give strong evidence; a large but biased sample remains weak evidence. The key insight is that sample size matters for reducing random variation — more data points reduce the chance that you happened to get an unusual cluster. But more data points cannot fix a systematically biased sampling procedure. There is also a point of diminishing returns: doubling your sample from 1,000 to 2,000 provides less additional confidence than doubling from 10 to 20, because the random error is already small. The question "is the sample big enough?" only makes sense after asking "is the sampling procedure sound?"

The third consideration is **alternative explanations**. Even a well-gathered sample can support multiple interpretations. A correlation between ice cream sales and drowning rates is real and reliable — but the right explanation is not that ice cream causes drowning. Both are explained by a common cause: hot weather drives both. **Confounding variables** are factors that correlate with both the proposed cause and the proposed effect, making a spurious association look causal. Strong inductive evidence for a causal claim requires ruling out the most plausible confounds — ideally through experimental control or statistical adjustment. Evidence that has not been tested against alternative explanations is considerably weaker than evidence that has survived such tests.

A useful practical habit is to evaluate evidence against a three-part checklist: (1) Is the evidence **relevant** — does it bear on the conclusion at all? (2) Is the evidence **sufficient** — does its quantity and distribution meet the burden required? (3) Is the evidence **uncontaminated** — has it been gathered and reported without systematic bias or motivated reasoning? Advertisements and advocacy documents routinely pass the first test and fail the second and third. Scientific peer review is partly a system for enforcing the second and third conditions. When you encounter an inductive argument in the wild — in journalism, policy debates, or everyday reasoning — these three questions will expose most of the significant weaknesses.
