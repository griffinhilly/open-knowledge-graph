---
id: cancer-epidemiology
title: Cancer Epidemiology
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiologic-study-designs
  type: hard
- id: chronic-disease-epidemiology
  type: hard
- id: measurement-error-epidemiology
  type: soft
tags:
- cancer-control
- risk-factors
- prevention-screening
stage: expert
status: validated
---

# Cancer Epidemiology

## Core Idea
Cancer epidemiology addresses distinct methodological challenges: long latency periods between exposure and disease onset, multiple etiological pathways for each histology, and substantial heterogeneity across cancer types. Study designs emphasize large prospective cohorts with biomarkers for exposure and outcome ascertainment. Analyses focus on absolute lifetime risk, attributable fractions of risk, and stage-specific survival to inform prevention and screening priorities. Temporal trends, geographic variation, and comparison across cancer types reveal modifiable risk factors and health inequities.

## Questions

```yaml
- question: "A carcinogen has a relative risk of 4.0 for a rare cancer affecting 0.01% of the population. A second exposure has a relative risk of 1.5 for a common cancer affecting 30% of the population. Which exposure has the larger population attributable fraction?"
  type: multiple-choice
  options:
    - "The first exposure, because a relative risk of 4.0 is more than twice the second exposure's relative risk"
    - "The second exposure, because prevalence is high enough that even a modest relative risk produces a large attributable fraction"
    - "They are equal, because relative risk and prevalence cancel out"
    - "Cannot be determined without knowing the absolute incidence rates"
  answer: 1
  explanation: "Population attributable fraction (PAF) depends on BOTH relative risk and the prevalence of the exposure. A very high relative risk applied to a rare exposure produces little preventable burden; a modest relative risk applied to a ubiquitous exposure may dominate. This is why physical inactivity and poor diet often rank ahead of rarer toxins in cancer prevention priority — they are everywhere. Relative risk alone does not answer the policy question."

- question: "A cancer type is rare in Japan but rises to match American rates among Japanese migrants to the United States within one to two generations. What does this pattern most strongly indicate?"
  type: multiple-choice
  options:
    - "Japanese genetic variants protect against this cancer type in their homeland"
    - "The genetic background of this population is highly susceptible to American dietary patterns"
    - "Environmental or behavioral factors, not genetic factors, are the primary drivers of this cancer risk"
    - "The Japanese healthcare system underdiagnoses this cancer, creating an artificial rate difference"
  answer: 2
  explanation: "In migrant studies, the genetic background of the population remains constant while the environment changes. If cancer rates shift within one or two generations to match those of the host country, the change must be driven by modifiable exposures — diet, lifestyle, environmental toxins — not by genes. This logic was foundational to identifying diet and caloric intake as likely contributors to colorectal and breast cancer risk decades before randomized trial evidence was available."

- question: "Cross-sectional study designs are poorly suited for cancer epidemiology because of the long latency between exposure and disease onset."
  type: true-false
  answer: true
  explanation: "The latency between a carcinogenic exposure and detectable disease can span 20–40 years. A cross-sectional snapshot therefore captures exposure status and disease status at the same point in time, but the relevant exposure may have occurred decades earlier — making it nearly impossible to establish temporal precedence or to accurately recall past exposures. This is why large prospective cohorts (Nurses' Health Study, UK Biobank) that collect exposure data before disease onset are the backbone of cancer epidemiology."

- question: "Demonstrating a strong relative risk between an exposure and a cancer type is sufficient to make that exposure a high-priority cancer prevention target."
  type: true-false
  answer: false
  explanation: "Relative risk establishes that an association is real and causal, but prevention priority requires population attributable fraction (PAF) — which incorporates how prevalent the exposure is. An exposure with a relative risk of 10 but a 0.001% prevalence has a negligible PAF. Prioritizing cancer prevention requires understanding both the strength of the causal relationship and how many people carry the exposure. Without prevalence data, relative risk alone can misdirect prevention resources."

- question: "Why do major cancer cohort studies collect biological specimens and exposure data prospectively rather than relying on recalled exposure data collected after a cancer diagnosis?"
  type: short-answer
  answer: "Recalled exposure data collected after diagnosis is subject to recall bias — participants who develop cancer may remember or report past exposures differently from those who remain healthy. More fundamentally, if the relevant exposures occurred 20–40 years before diagnosis, memory is unreliable and the data inaccurate. Prospective collection captures exposures before any disease develops, eliminating recall bias and allowing biomarkers to objectively document what participants were actually exposed to, rather than what they remember."
  explanation: "This connects two concepts: the latency problem (exposures precede diagnosis by decades) and measurement error (recalled data is systematically biased in case-control settings). Prospective design solves both: exposure data is complete, contemporaneous, and equally accurate across cases and controls because disease status is unknown at collection. This is the core methodological reason why large cohort studies are expensive but irreplaceable in cancer epidemiology."
```

## Explainer

Cancer epidemiology applies the study designs and methods you learned in general epidemiology and chronic disease epidemiology, but the unique biology of cancer introduces methodological challenges that require specific adaptations. The most fundamental challenge is **latency**: the gap between a causative exposure and the development of detectable cancer can span two to four decades. A woman who develops breast cancer at age 60 may have had her key exposures — hormonal, dietary, environmental — at ages 20–40. This means that recalled exposure data is unreliable (measuring a past exposure is the measurement error problem you have already studied), cross-sectional designs are nearly useless, and cohort studies must follow participants for extraordinarily long periods. The large prospective cohorts that anchor cancer epidemiology — the Nurses' Health Study, UK Biobank, EPIC — were designed precisely to collect exposure data prospectively so that it can be linked to cancer outcomes that may not manifest for decades.

A second defining challenge is **heterogeneity**: "cancer" is not one disease but hundreds of distinct conditions that happen to share the property of uncontrolled cell division. Lung squamous cell carcinoma, lung adenocarcinoma, and small cell lung cancer have different epidemiological risk factors, natural histories, and responses to treatment, even though all three occur in the lung. Aggregating them inflates exposure misclassification and dilutes associations. Modern cancer epidemiology increasingly analyzes cancers by histological subtype, molecular marker, and tumor characteristics rather than anatomical site alone. This shift requires larger sample sizes but produces more precise etiological insights — which is why biobanking (collecting biological specimens for later genomic or proteomic analysis) is now standard in major cancer cohorts.

**Migrant studies** and **ecological analyses** of geographic variation are two powerful tools for identifying modifiable causes. If a cancer is rare in Japan but rises among Japanese migrants to the United States within one or two generations, this strongly implicates environmental or behavioral factors over genetic ones — because the genetic background remained constant while the environment changed. This logic identified dietary fat and caloric intake as likely contributors to colorectal and breast cancer risk decades before randomized evidence was available. Conversely, if cancer rates track closely with ethnicity even after migration, genetic or early-life factors are implicated. Combining migrant data with family and twin studies allows researchers to partition risk between nature and nurture.

The key analytical outputs for prevention and policy are **absolute lifetime risk** and **population attributable fraction (PAF)**. Relative risks are important for establishing causation, but they do not directly answer "how much would cancer burden decrease if this exposure were eliminated?" The PAF estimates exactly this: the proportion of cancer cases in a population that are attributable to a specific risk factor, accounting for how prevalent the risk factor is. If smoking has a high relative risk for lung cancer *and* high prevalence, its PAF will be large. If a toxin has an equally high relative risk but is rare, its PAF will be small. Prioritizing cancer prevention efforts requires both relative and absolute reasoning — understanding which exposures are most causal *and* most prevalent in the target population.
