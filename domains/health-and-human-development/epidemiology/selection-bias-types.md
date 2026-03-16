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
stage: advanced
status: draft
---

# Selection Bias: Types and Sources in Epidemiologic Studies

## Core Idea
Selection bias arises when the process selecting study participants is related to both exposure and outcome, distorting the true association. Common types include Berkson's bias (in case-control hospital studies), loss-to-follow-up bias (cohort studies), and healthy worker effect. Selection bias is a threat to internal validity and cannot be controlled in analysis once it occurs.

## Explainer

Selection bias is about the gap between who you wanted to study and who you actually studied — and when that gap is systematically related to both the exposure and the outcome you're investigating. You already know from epidemiologic study designs that different designs have different sampling schemes: cohort studies enroll participants based on exposure status and follow them forward, while case-control studies sample based on outcome status. Each design has characteristic vulnerabilities to selection bias that flow directly from how participants enter the study.

The core mechanism is simple: selection bias occurs when the probability of being included in the study is not equal across all combinations of exposure and disease status. Write it this way: if P(selected | E=1, D=1) / P(selected | E=1, D=0) ≠ P(selected | E=0, D=1) / P(selected | E=0, D=0), then the observed odds ratio will not equal the true population odds ratio. The selection probabilities multiply through to distort the observed association. This is not a statistical problem solvable by larger samples or better analysis — the target population you want to make inferences about is not adequately represented in your sample.

**Berkson's bias** (or Berkson's fallacy) is the canonical selection bias in hospital-based case-control studies. When you recruit both cases and controls from hospitalized patients, you are sampling from people sick enough to be hospitalized — not from the general population. People with multiple conditions are disproportionately hospitalized. As a result, if your exposure (say, smoking) independently increases hospitalization risk, it will appear more commonly in both cases and controls than in the general population. If the control condition (say, appendicitis) is associated with smoking, you'll see artificially low odds ratios because smoking is inflated in the control group too. The bias flows entirely from the selection of controls from a non-representative hospital population.

**Loss-to-follow-up bias** strikes cohort studies when participants who drop out differ systematically from those who remain. If sicker participants are more likely to die or stop coming to clinic (informative censoring), and if their illness is related to the exposure, the remaining cohort is a healthier, non-representative subset. The classic example: workers in an occupational cohort who develop serious illness quit the workforce and are lost to follow-up; the remaining workers appear healthier than they truly are. This connects directly to the **healthy worker effect** — the observation that employed populations consistently show lower mortality than the general population in references tables, not because employment is protective but because severely ill people disproportionately don't work. Comparing a worker cohort to general population mortality tables therefore creates a systematic downward bias in estimated occupational hazard ratios.

The critical clinical and methodological lesson is that selection bias **cannot be corrected analytically** after the fact. Unlike confounding, which can sometimes be addressed by statistical adjustment if the confounders are measured, selection bias distorts the study sample itself — the data you have simply do not represent the target population in the relevant cells of the exposure-outcome table. The remedy must come at the design stage: community-based (rather than hospital-based) control recruitment, intensive follow-up to minimize loss, and explicit attention to what process selects participants into and out of the study and whether that process is related to exposure and outcome simultaneously.
