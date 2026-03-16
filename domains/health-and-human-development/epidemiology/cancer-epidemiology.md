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
stage: advanced
status: draft
---

# Cancer Epidemiology

## Core Idea
Cancer epidemiology addresses distinct methodological challenges: long latency periods between exposure and disease onset, multiple etiological pathways for each histology, and substantial heterogeneity across cancer types. Study designs emphasize large prospective cohorts with biomarkers for exposure and outcome ascertainment. Analyses focus on absolute lifetime risk, attributable fractions of risk, and stage-specific survival to inform prevention and screening priorities. Temporal trends, geographic variation, and comparison across cancer types reveal modifiable risk factors and health inequities.

## Explainer

Cancer epidemiology applies the study designs and methods you learned in general epidemiology and chronic disease epidemiology, but the unique biology of cancer introduces methodological challenges that require specific adaptations. The most fundamental challenge is **latency**: the gap between a causative exposure and the development of detectable cancer can span two to four decades. A woman who develops breast cancer at age 60 may have had her key exposures — hormonal, dietary, environmental — at ages 20–40. This means that recalled exposure data is unreliable (measuring a past exposure is the measurement error problem you have already studied), cross-sectional designs are nearly useless, and cohort studies must follow participants for extraordinarily long periods. The large prospective cohorts that anchor cancer epidemiology — the Nurses' Health Study, UK Biobank, EPIC — were designed precisely to collect exposure data prospectively so that it can be linked to cancer outcomes that may not manifest for decades.

A second defining challenge is **heterogeneity**: "cancer" is not one disease but hundreds of distinct conditions that happen to share the property of uncontrolled cell division. Lung squamous cell carcinoma, lung adenocarcinoma, and small cell lung cancer have different epidemiological risk factors, natural histories, and responses to treatment, even though all three occur in the lung. Aggregating them inflates exposure misclassification and dilutes associations. Modern cancer epidemiology increasingly analyzes cancers by histological subtype, molecular marker, and tumor characteristics rather than anatomical site alone. This shift requires larger sample sizes but produces more precise etiological insights — which is why biobanking (collecting biological specimens for later genomic or proteomic analysis) is now standard in major cancer cohorts.

**Migrant studies** and **ecological analyses** of geographic variation are two powerful tools for identifying modifiable causes. If a cancer is rare in Japan but rises among Japanese migrants to the United States within one or two generations, this strongly implicates environmental or behavioral factors over genetic ones — because the genetic background remained constant while the environment changed. This logic identified dietary fat and caloric intake as likely contributors to colorectal and breast cancer risk decades before randomized evidence was available. Conversely, if cancer rates track closely with ethnicity even after migration, genetic or early-life factors are implicated. Combining migrant data with family and twin studies allows researchers to partition risk between nature and nurture.

The key analytical outputs for prevention and policy are **absolute lifetime risk** and **population attributable fraction (PAF)**. Relative risks are important for establishing causation, but they do not directly answer "how much would cancer burden decrease if this exposure were eliminated?" The PAF estimates exactly this: the proportion of cancer cases in a population that are attributable to a specific risk factor, accounting for how prevalent the risk factor is. If smoking has a high relative risk for lung cancer *and* high prevalence, its PAF will be large. If a toxin has an equally high relative risk but is rare, its PAF will be small. Prioritizing cancer prevention efforts requires both relative and absolute reasoning — understanding which exposures are most causal *and* most prevalent in the target population.
