---
id: statistical-power-and-effect-size-determination
title: Statistical Power, Effect Size, and Sample Size Planning
domain: psychology
course: research-methods-psychology
prerequisites:
- id: variable-definition-and-operational-measurement
  type: hard
- id: population-sampling-representativeness
  type: hard
- id: effect-size-and-power
  type: hard
- id: normal-distribution
  type: soft
- id: standard-normal-z-scores-theory
  type: hard
builds-toward:
- statistical-inference-significance-testing
tags:
- statistical-power
- effect-size
- sample-size
- design-planning
stage: formal-systems
status: draft
---

# Statistical Power, Effect Size, and Sample Size Planning

## Core Idea
Statistical power is the probability of detecting a true effect. It increases with sample size, effect size magnitude, and alpha level. Effect size quantifies the magnitude of an effect independent of sample size. A-priori power analysis plans sample size to achieve adequate power (typically 0.80). Underpowered studies risk Type II error (missing true effects); overpowered studies waste resources.

## How It's Best Learned
Use power analysis software (G*Power) to compute required sample sizes for typical effect sizes and power levels. Review published papers reporting effect sizes and power. Discuss why small-sample studies are common in psychology and their implications.

## Common Misconceptions
- Statistical significance proves practical significance; - All effect sizes worth studying are large; - Power analysis is only needed for rare or expensive studies; - Larger samples automatically mean valid inferences.

## Questions

```yaml
- question: "Study A (n = 10,000) finds a drug reduces headache severity by 0.1 points on a 100-point scale (p < 0.001). Study B (n = 50) finds a 15-point reduction (p = 0.04). Which conclusion is most accurate?"
  type: multiple-choice
  options:
    - "Study A's finding is more important because p < 0.001 is far more significant than p = 0.04"
    - "Study B likely demonstrates a more practically meaningful effect, even though Study A is more statistically significant"
    - "Neither study is meaningful without pre-registration"
    - "Study A is definitive because large samples eliminate statistical uncertainty"
  answer: 1
  explanation: "Statistical significance reflects how unlikely the observed result is under the null hypothesis — it is heavily influenced by sample size. With n = 10,000, even a trivially small effect (0.1 points on a 100-point scale) becomes highly significant. Study B's 15-point reduction is far larger in magnitude and likely clinically meaningful, even though its p-value is less extreme. Effect size (the magnitude of the difference) is the relevant metric for practical significance; p-values should not be used as a proxy for importance."

- question: "A researcher wants 80% power to detect a small effect (Cohen's d = 0.2) at α = .05. Compared to detecting a large effect (d = 0.8) with the same power and alpha, how does the required sample size compare?"
  type: multiple-choice
  options:
    - "About the same — sample size requirements don't vary much with effect size"
    - "Much larger — smaller effects are harder to distinguish from noise and require more data"
    - "Smaller — small effects are more common in nature, making them easier to detect"
    - "The answer depends entirely on the specific alpha level chosen"
  answer: 1
  explanation: "Effect size and required sample size have an inverse relationship for fixed power and alpha. For d = 0.2, you need approximately 197 participants per group; for d = 0.8, only about 26 per group (using standard power formulas). Smaller effects produce smaller differences in sample distributions, making them harder to distinguish from random variation — which requires more observations to accumulate sufficient evidence. Effect prevalence in nature is irrelevant to how difficult the effect is to detect statistically."

- question: "A statistically significant result (p < .05) from a study with only 20% power is strong evidence that a real effect exists."
  type: true-false
  answer: false
  explanation: "An underpowered study that achieves statistical significance is actually suspect, not reassuring. With only 20% power, the study had a high base rate of failing to detect true effects. The studies that 'succeed' despite low power are disproportionately those that observed inflated effects by chance sampling — a phenomenon called the 'winner's curse.' These inflated estimates tend not to replicate. High power matters not just for detecting effects but for producing stable, accurate effect size estimates."

- question: "Effect size is a standardized measure of the magnitude of an effect that does not depend on sample size."
  type: true-false
  answer: true
  explanation: "This is the defining feature that makes effect sizes valuable. Unlike p-values, which decrease (become more significant) as sample size increases for any fixed true effect, Cohen's d, r, η², and related measures quantify the size of an effect in scale-free units that remain constant regardless of how many participants were tested. This is why effect sizes are required for meta-analyses — they allow combining results across studies with different sample sizes."

- question: "Why do researchers conduct a-priori power analyses before collecting data? What goes wrong scientifically when this step is skipped?"
  type: short-answer
  answer: "A-priori power analysis determines the sample size needed to detect your expected effect with adequate probability (typically 80%), given your significance threshold. Skipping it leads to underpowered studies: if the true effect exists but is modest, an underpowered study will usually miss it (Type II error), wasting resources. Worse, researchers who lack a pre-specified sample size often collect data until p < .05 appears — a practice called 'optional stopping' — which inflates the false positive rate well above the nominal alpha level. Pre-specifying sample size (and ideally pre-registering hypotheses) ensures that a significant result reflects a planned, adequately powered test rather than sampling until luck produces significance."
  explanation: "The replication crisis in psychology was partly caused by widespread underpowered studies combined with flexible stopping rules. Understanding power analysis reveals exactly why this is problematic: the tools for rigorous inference require commitment before observing data. Power analysis is not bureaucratic overhead; it's the mechanism that connects sampling precision to the strength of scientific claims."
```

## Explainer

You've already encountered the concept that statistical significance depends on both the size of an effect and the precision of your estimate. **Statistical power** and **effect size** formalize this relationship and turn it into a design tool. Power is the probability that your study will detect a true effect when one exists — in other words, the probability of *not* making a Type II error (false negative). Power depends on three things under your control as a researcher: the effect size you're trying to detect, the sample size you collect, and the significance threshold you set.

**Effect size** is the metric that links statistical results to scientific meaning. It quantifies the magnitude of a difference or relationship in a scale-free way. Common effect size metrics include **Cohen's d** (for mean differences — a d of 0.5 means the group means are half a standard deviation apart), **r** (the correlation coefficient, which is its own effect size measure), and **η²** (proportion of variance explained in ANOVA). Cohen's benchmark guidelines — small (.2), medium (.5), large (.8) for d — are rough calibrations, not laws. What counts as a meaningful effect depends entirely on the domain: a d of 0.2 might be clinically important for a serious disease intervention but trivial for an attitude measure. Effect size connects your result to the world outside the p-value, which is why reporting it is now required by most journals.

**A-priori power analysis** is the practice of calculating required sample size *before* collecting data, given your target power (typically .80), your chosen alpha (.05), and your expected effect size. The mechanics work like this: power increases as sample size increases, because larger samples reduce sampling error, making it easier to distinguish real effects from noise. If you expect a small effect (d = 0.2), you need a much larger sample to reliably detect it than if you expect a large effect (d = 0.8). Underpowered studies — those with power below .80 — not only fail to detect true effects; they also produce unstable effect size estimates, because small samples vary widely. A study with 30% power that happens to find p < .05 likely observed an inflated effect by chance, which then fails to replicate.

The replication crisis in psychology was partly caused by widespread use of underpowered studies with flexible stopping rules — collecting data until p < .05 emerged. Understanding power helps you see exactly why this is problematic: if you stop when you first cross the significance threshold, you've created an implicit multiple-comparison problem (the more you look, the higher the false positive rate) and you've exploited sampling variability rather than estimated a true effect. The remedy is to commit to a sample size before you start, justify it with a power analysis, and pre-register your hypotheses. Power analysis is not a bureaucratic requirement — it is the tool that connects the precision of your measurement to the scientific claims you're entitled to make.
