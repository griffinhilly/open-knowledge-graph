---
id: burden-of-disease-metrics
title: Burden of Disease Metrics
domain: health-and-human-development
course: public-health
prerequisites:
- id: epidemiology-foundations
  type: hard
- id: disease-frequency-measures
  type: hard
builds-toward:
- global-burden-of-disease
tags:
- daly
- qaly
- health-burden
- priority-setting
- measurement
stage: advanced
status: draft
---

# Burden of Disease Metrics

## Core Idea
Disability-adjusted life years (DALYs) and quality-adjusted life years (QALYs) quantify disease burden as lost health from premature death and functional impairment, enabling comparison of disease burden across conditions and regions. These metrics require choices about disability weights, discount rates, and time horizons that reflect underlying values. Burden metrics support priority-setting to maximize population health gain with limited resources.

## How It's Best Learned
Calculate DALYs and QALYs for different diseases to compare burden across conditions. Examine how disability weights and discount rates affect priority ranking of interventions across scenarios.

## Common Misconceptions
DALY and QALY are identical measures. Ignoring distributional effects and who bears the burden across populations. Treating burden metrics as purely objective measures rather than value-laden choices with ethical implications.

## Explainer

From your study of epidemiology, you can count cases, calculate rates, and measure how common diseases are across populations. But raw frequency doesn't tell you everything: a condition that kills people young versus one that causes decades of disability are very different burdens, even if they affect the same number of people. Burden of disease metrics were developed precisely to answer the follow-up question: across all the conditions affecting a population, which ones matter most in aggregate, and how do we weigh premature death against years lived with impairment?

The **DALY (disability-adjusted life year)** is the foundational metric of global burden of disease analysis. One DALY equals one year of healthy life lost — either through premature death or through living with disability. It has two components. **YLL (years of life lost to premature mortality)** counts the gap between age at death and expected age of death from a reference life table — a 25-year-old dying loses roughly 57 YLL, while a 75-year-old dying loses about 12. **YLD (years lived with disability)** multiplies the duration of living with a condition by a **disability weight** between 0 (perfect health) and 1 (equivalent to death). A person living 10 years with moderate depression (disability weight ≈ 0.4) contributes 4 YLD. DALY = YLL + YLD. This additive structure means a chronic non-fatal condition creating decades of moderate impairment can dominate the burden calculation even if its mortality is low — which is exactly the epidemiological transition pattern seen globally as infectious disease mortality falls and non-communicable disease disability rises.

The **QALY (quality-adjusted life year)** is the health economic parallel. One QALY is one year of life in perfect health. It is used to evaluate interventions: an intervention producing 5 QALYs at a cost of $50,000 has an **incremental cost-effectiveness ratio (ICER)** of $10,000 per QALY. Most high-income healthcare systems use a threshold (commonly $50,000–$100,000 per QALY in the US, £20,000–30,000 per QALY in the UK's NICE assessments) to determine whether a treatment provides sufficient value. Unlike DALYs, QALYs are typically elicited from patients or the public through preference surveys (time trade-off, standard gamble) — you ask people how many years of life in a health state they would trade for fewer years in perfect health. The difference from disability weights is subtle but important: DALYs use weights set by expert panels and are meant to represent societal values consistently across the GBD study; QALYs can use weights elicited from the patients actually experiencing a condition, potentially capturing their adaptation to illness.

Both metrics embed explicit value judgments that are worth examining critically. Disability weights assume that living with a given condition is worse than perfect health by a fixed factor — but whether an amputee experiencing a full life should be counted as "losing" 0.3 of each year lived is philosophically contested, particularly within disability rights frameworks. Discount rates (which reduce the value of future health years, typically at 3% annually) deprioritize conditions affecting the young relative to those affecting the middle-aged, and conditions whose harms materialize decades later. Age-weighting, used in earlier DALY formulations, explicitly valued a year of life in young adulthood more than a year in childhood or old age. These aren't bugs in the methodology — they're design choices with enormous implications for which conditions rank as global priorities and which interventions get funded. Reading burden of disease data critically means understanding not just the numbers, but the architecture of values embedded in how they were produced.
