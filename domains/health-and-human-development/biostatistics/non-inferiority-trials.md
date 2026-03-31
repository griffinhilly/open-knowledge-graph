---
id: non-inferiority-trials
title: Non-Inferiority Trial Design
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: clinical-trial-design-intro
  type: hard
- id: power-and-sample-size
  type: hard
builds-toward: []
tags:
- non-inferiority
- equivalence
- margin
- active-control
- assay-sensitivity
stage: expert
status: validated
---

# Non-Inferiority Trial Design

## Core Idea
Non-inferiority trials test whether a new treatment is not meaningfully worse than an established active control, rather than whether it is better than placebo. The null hypothesis is that the new treatment is inferior by more than a pre-specified non-inferiority margin (delta); rejecting this null provides evidence that the new treatment preserves at least some of the active control's benefit. The non-inferiority margin represents the largest clinically acceptable loss of efficacy — often a fraction (e.g., 50%) of the active control's established effect over placebo. These trials are appropriate when placebo control is unethical (an effective treatment exists), and the new treatment offers advantages in safety, cost, convenience, or adherence. The per-protocol analysis is typically primary (unlike superiority trials where intention-to-treat is primary) because ITT analysis in non-inferiority trials is anti-conservative — non-compliance and treatment crossover bias toward finding non-inferiority.

## Questions

```yaml
- question: "A new antibiotic is tested against the standard treatment for pneumonia. The non-inferiority margin is set at 10 percentage points for cure rate. The study finds the new drug's cure rate is 5 percentage points lower, with a 95% confidence interval of [-9, -1]. Is non-inferiority demonstrated?"
  type: multiple-choice
  options:
    - "No — the new drug is 5 points worse, which proves inferiority"
    - "Yes — the entire 95% confidence interval lies above the non-inferiority margin of -10, so the new drug is not worse than the standard by more than 10 points"
    - "No — the confidence interval is entirely below zero, proving the new drug is inferior"
    - "The result is inconclusive because the interval includes negative values"
  answer: 1
  explanation: "Non-inferiority is demonstrated when the lower bound of the confidence interval for the treatment difference exceeds (is less negative than) the non-inferiority margin. Here, the lower bound is -9, which is above -10. We can conclude with 95% confidence that the new drug is not worse than the standard by more than 10 points. Note that the drug IS worse (the CI is entirely negative, so it would be declared inferior in a superiority test), but it is not worse enough to exceed the pre-specified acceptable margin. If the drug offers advantages (fewer side effects, oral instead of IV), this small efficacy loss may be acceptable."

- question: "In a non-inferiority trial, the intention-to-treat analysis is the primary analysis, just as in superiority trials."
  type: true-false
  answer: false
  explanation: "In superiority trials, ITT is conservative (non-compliance dilutes the treatment effect, making it harder to reject the null). In non-inferiority trials, this logic reverses: non-compliance, treatment crossover, and poor adherence make treatments appear more similar than they truly are, biasing TOWARD non-inferiority. The per-protocol analysis, which includes only patients who adhered to the assigned treatment, is the primary analysis because it provides a more honest comparison of the treatments as actually received. Both ITT and per-protocol should be reported, and non-inferiority should ideally be demonstrated in both."

- question: "Explain why choosing the non-inferiority margin is the most critical and controversial decision in non-inferiority trial design."
  type: short-answer
  answer: "The margin determines what counts as 'not meaningfully worse' and directly controls the clinical interpretation. Too large a margin allows clinically important efficacy losses to be declared non-inferior — the new drug could be substantially worse than the standard but still pass. Too small a margin requires enormous sample sizes and may be unachievable. The margin should be smaller than the active control's effect over placebo (otherwise the new drug could be no better than placebo and still pass) and should represent a loss of efficacy that preserves a clinically meaningful proportion of the active control's benefit. There is no statistical formula for choosing it — it requires clinical judgment and is often the subject of regulatory negotiation."
  explanation: "The margin is typically set at no more than 50% of the active control's historically demonstrated effect over placebo. This ensures the new drug retains at least 50% of the known benefit. But if the active control's effect has been measured imprecisely or has changed over time (assay sensitivity concerns), the margin may be based on outdated evidence. The FDA requires a thorough historical review (meta-analysis of prior placebo-controlled trials) to justify the margin — a process called 'constancy assumption' analysis."
```

## Explainer

Most clinical trials ask: "Is the new treatment better than placebo (or the current standard)?" But sometimes the relevant question is different: "Is the new treatment at least as good as what we already have?" If a new antibiotic has fewer side effects, costs less, or can be taken orally instead of intravenously, it would be valuable even if its cure rate were slightly lower — provided the difference is not clinically meaningful. **Non-inferiority trials** address this by testing whether the new treatment's efficacy falls within an acceptable margin of the active control.

The statistical setup inverts the usual null and alternative hypotheses. The **null hypothesis** is that the new treatment is inferior to the standard by more than the non-inferiority margin delta. The **alternative** is that the difference is within the margin. Non-inferiority is demonstrated when the confidence interval for the treatment difference excludes the margin — specifically, when the lower bound of the confidence interval (for a beneficial direction) is above -delta. This is a one-sided test: you are testing only for inferiority, not for superiority.

The **non-inferiority margin** is the single most important design parameter. It must satisfy two constraints. First, it should be clinically meaningful — a margin of 30 percentage points for a life-saving treatment is absurdly permissive, while 0.1 percentage points is impractically strict. Second, it should be small enough that a drug passing the non-inferiority test is still demonstrably better than placebo. This requires knowledge of the active control's effect over placebo from prior trials. If the active control reduces mortality by 10% versus placebo, a non-inferiority margin of 10% would allow the new drug to be equivalent to placebo — clearly unacceptable. Regulatory guidelines typically require the margin to preserve at least 50% of the active control's historical benefit.

A subtle but important feature of non-inferiority trials is the reversal of the ITT principle. In superiority trials, ITT analysis is conservative because treatment contamination and non-compliance dilute the true difference, making it harder to reject the null. In non-inferiority trials, dilution works the opposite way: it makes the treatments appear more similar, biasing toward a finding of non-inferiority. A trial where many patients in the new drug group switched to the standard treatment would appear non-inferior simply because the groups received similar treatments. For this reason, the **per-protocol analysis** (restricted to patients who complied with the protocol) is the primary analysis, and non-inferiority should ideally be demonstrated in both ITT and per-protocol populations.
