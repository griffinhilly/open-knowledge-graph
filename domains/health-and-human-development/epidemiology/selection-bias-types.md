---
id: selection-bias-types
title: 'Selection Bias: Types and Sources in Epidemiologic Studies'
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiologic-study-designs
  type: hard
builds-toward:
- stratification-and-adjustment
- sensitivity-analysis-epidemiology
tags:
- selection-bias
- internal-validity
- study-design
stage: expert
status: draft
---

# Selection Bias: Types and Sources in Epidemiologic Studies

## Core Idea
Selection bias arises when the process selecting study participants is related to both exposure and outcome, distorting the true association. Common types include Berkson's bias (in case-control hospital studies), loss-to-follow-up bias (cohort studies), and healthy worker effect. Selection bias is a threat to internal validity and cannot be controlled in analysis once it occurs.

## Questions

```yaml
- question: "A hospital-based case-control study examines smoking as a risk factor for bladder cancer. Cases are bladder cancer patients; controls are hospitalized patients with appendicitis. Appendicitis is independently more common in smokers. Compared to the true odds ratio, what is the most likely result?"
  type: multiple-choice
  options:
    - "The odds ratio will be inflated because smoking is over-represented among cases"
    - "The odds ratio will be biased toward the null because smoking is also elevated in the control group, making cases and controls appear more similar than they truly are"
    - "There will be no bias because both groups are drawn from the same hospital"
    - "The odds ratio will be inflated because hospital patients are generally sicker and more likely to smoke"
  answer: 1
  explanation: "This is Berkson's bias. Controls are drawn from hospitalized patients with appendicitis — a condition independently associated with smoking. This inflates smoking prevalence in the control group, making it artificially similar to the cases. The result is a diluted (biased toward null) odds ratio for smoking-bladder cancer. Berkson's bias flows from selecting controls from a non-representative hospital population where multiple diseases and exposures cluster together."

- question: "An occupational cohort study compares mortality in chemical plant workers to national mortality tables and finds significantly lower death rates among workers. The most accurate interpretation is:"
  type: multiple-choice
  options:
    - "Chemical plant employment is likely protective against mortality"
    - "The healthy worker effect — severely ill people disproportionately do not work, making the employed cohort healthier at baseline than the general population"
    - "Loss-to-follow-up bias has inflated apparent worker survival"
    - "The national mortality tables are calibrated for a different age distribution"
  answer: 1
  explanation: "The healthy worker effect is a form of selection bias: the reference population (all people in national tables) includes severely ill people who cannot work, while the employed cohort systematically excludes them. The comparison group is therefore healthier at baseline, producing an apparent protective effect. This means occupational hazard ratios can be systematically underestimated when national mortality tables serve as reference — a design flaw, not a real protective effect."

- question: "Selection bias, unlike confounding, can be corrected through statistical adjustment during data analysis if sufficient covariate data are collected."
  type: true-false
  answer: false
  explanation: "This is the critical distinction. Confounding can sometimes be addressed analytically (via stratification, regression, matching) if confounders are measured, because the target population is represented in the data. Selection bias distorts the study sample itself — specific cells of the exposure-outcome table are under- or over-represented relative to the target population. No amount of statistical adjustment can recover information about people who were never properly included. The remedy must come at the design stage: community-based control sampling, intensive follow-up to minimize dropout."

- question: "Selection bias requires that the probability of study inclusion differs jointly across both exposure and disease status — differential inclusion based on exposure alone (without involving disease) is not sufficient to produce a biased association estimate."
  type: true-false
  answer: true
  explanation: "Precisely right. If selection depends only on exposure (say, exposed people are twice as likely to be recruited, regardless of disease status), the exposure-disease association is not distorted — the data are still internally valid, just externally generalizable to a restricted population. Selection bias occurs when the selection probabilities differ across the combined exposure-disease cells: P(selected|E=1,D=1)/P(selected|E=1,D=0) ≠ P(selected|E=0,D=1)/P(selected|E=0,D=0). This differential pattern is what distorts the observed odds ratio."

- question: "Explain why selection bias cannot be corrected through statistical analysis after data collection, unlike some forms of confounding."
  type: short-answer
  answer: "Selection bias distorts which people are in the study — the data collected do not adequately represent all cells of the exposure-outcome table in the target population. Because people with certain exposure-outcome combinations are systematically missing or over-represented, there is no data to adjust. Confounding, by contrast, involves a third variable present in the data that can be adjusted away statistically if measured. With selection bias, the problem is in the denominator of your study — who was never there — not in a measured variable you can control for."
  explanation: "The metaphor is instructive: confounding is a problem with the data you have (a covariate you can model); selection bias is a problem with the data you don't have (people who should have been sampled but weren't, or were sampled at wrong rates). You can't regress your way out of a sample that doesn't represent the population you want to study."
```

## Explainer

Selection bias is about the gap between who you wanted to study and who you actually studied — and when that gap is systematically related to both the exposure and the outcome you're investigating. You already know from epidemiologic study designs that different designs have different sampling schemes: cohort studies enroll participants based on exposure status and follow them forward, while case-control studies sample based on outcome status. Each design has characteristic vulnerabilities to selection bias that flow directly from how participants enter the study.

The core mechanism is simple: selection bias occurs when the probability of being included in the study is not equal across all combinations of exposure and disease status. Write it this way: if P(selected | E=1, D=1) / P(selected | E=1, D=0) ≠ P(selected | E=0, D=1) / P(selected | E=0, D=0), then the observed odds ratio will not equal the true population odds ratio. The selection probabilities multiply through to distort the observed association. This is not a statistical problem solvable by larger samples or better analysis — the target population you want to make inferences about is not adequately represented in your sample.

**Berkson's bias** (or Berkson's fallacy) is the canonical selection bias in hospital-based case-control studies. When you recruit both cases and controls from hospitalized patients, you are sampling from people sick enough to be hospitalized — not from the general population. People with multiple conditions are disproportionately hospitalized. As a result, if your exposure (say, smoking) independently increases hospitalization risk, it will appear more commonly in both cases and controls than in the general population. If the control condition (say, appendicitis) is associated with smoking, you'll see artificially low odds ratios because smoking is inflated in the control group too. The bias flows entirely from the selection of controls from a non-representative hospital population.

**Loss-to-follow-up bias** strikes cohort studies when participants who drop out differ systematically from those who remain. If sicker participants are more likely to die or stop coming to clinic (informative censoring), and if their illness is related to the exposure, the remaining cohort is a healthier, non-representative subset. The classic example: workers in an occupational cohort who develop serious illness quit the workforce and are lost to follow-up; the remaining workers appear healthier than they truly are. This connects directly to the **healthy worker effect** — the observation that employed populations consistently show lower mortality than the general population in references tables, not because employment is protective but because severely ill people disproportionately don't work. Comparing a worker cohort to general population mortality tables therefore creates a systematic downward bias in estimated occupational hazard ratios.

The critical clinical and methodological lesson is that selection bias **cannot be corrected analytically** after the fact. Unlike confounding, which can sometimes be addressed by statistical adjustment if the confounders are measured, selection bias distorts the study sample itself — the data you have simply do not represent the target population in the relevant cells of the exposure-outcome table. The remedy must come at the design stage: community-based (rather than hospital-based) control recruitment, intensive follow-up to minimize loss, and explicit attention to what process selects participants into and out of the study and whether that process is related to exposure and outcome simultaneously.
