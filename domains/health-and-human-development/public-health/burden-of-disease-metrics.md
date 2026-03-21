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

## Questions

```yaml
- question: "Disease A kills 1,000 people at age 70 (contributing roughly 12 YLL each). Disease B causes 50,000 people to live 20 years with a disability weight of 0.5. Which disease contributes more DALYs, and what does this reveal about burden of disease analysis?"
  type: multiple-choice
  options:
    - "Disease A, because mortality is always weighted more heavily than disability in the DALY formula"
    - "Disease B, because its YLD (50,000 × 20 × 0.5 = 500,000) vastly outweighs Disease A's YLL (1,000 × 12 = 12,000)"
    - "They contribute equally, since DALY converts both death and disability to a common scale"
    - "Cannot be determined without knowing the discount rate applied to future years"
  answer: 1
  explanation: "Disease B contributes 500,000 YLD versus Disease A's 12,000 YLL — more than 40 times as much. This reveals a crucial insight: widespread chronic non-fatal conditions often dominate DALY calculations even when their mortality is low. This is why the global epidemiological transition (falling infectious mortality, rising chronic non-communicable disease) has shifted DALY rankings dramatically — depression, back pain, and diabetes generate enormous YLD despite causing fewer deaths than historic infectious diseases."

- question: "A health economist uses QALYs rather than DALYs to evaluate whether a new cancer drug should be funded by a national health system. What is the most important reason for choosing QALYs in this context?"
  type: multiple-choice
  options:
    - "QALYs measure functional impairment more accurately than DALYs"
    - "DALYs cannot be applied to chronic diseases, only to acute infectious conditions"
    - "QALYs enable calculation of the incremental cost-effectiveness ratio (ICER), directly answering whether the drug provides sufficient health gain per dollar spent"
    - "QALYs are free from value judgments, unlike DALYs, which embed disability weights set by expert panels"
  answer: 2
  explanation: "QALYs are designed for cost-effectiveness analysis: dividing intervention cost by QALYs gained yields the ICER, which is then compared to a threshold (e.g., £30,000 per QALY in UK NICE assessments) to decide funding. DALYs are designed for population-level burden comparison and priority-setting, not cost-effectiveness evaluation. Option D is false — both metrics embed value judgments, just in different ways."

- question: "A country's DALY burden estimates remain the same regardless of whether analysts use a 3% annual discount rate or a 0% discount rate."
  type: true-false
  answer: false
  explanation: "Discount rates reduce the value of future health years — at 3%, a DALY averted 20 years from now is worth less than one averted today. This disproportionately affects diseases whose harms materialize decades later and interventions (like childhood vaccination) whose benefits accrue over a lifetime. A 0% discount rate treats future and present health equally, which substantially changes relative burden rankings and intervention priorities."

- question: "Within the DALY framework, assigning a disability weight to a health condition inherently reflects value judgments about how much worse it is to live with that condition than to live in perfect health."
  type: true-false
  answer: true
  explanation: "Disability weights (between 0 = perfect health and 1 = equivalent to death) embed normative assumptions about the value of different health states. Disability rights advocates note that people living with conditions like limb amputation or deafness often report high quality of life, yet are assigned substantial disability weights by external expert panels. This reveals that DALYs are not purely objective measures — they encode societal values about which ways of living count as 'reduced' health."

- question: "Why do disability rights advocates critique the use of disability weights in DALY calculations, and what does this critique reveal about the nature of burden of disease metrics?"
  type: short-answer
  answer: "Disability weights assume that living with a given condition constitutes a fixed fractional loss of a healthy year — but this judgment is made by expert panels or general-population surveys, not necessarily by people living with those conditions. People with disabilities often adapt to and value their lives highly, yet are assigned substantial weights by external raters. The critique reveals that DALYs are not purely descriptive measurements: they embed normative claims about which ways of living are 'healthy,' and those claims determine which diseases are counted as burdensome and which interventions get prioritized."
  explanation: "This isn't a fatal flaw in the DALY framework — all metrics embed values — but it means burden of disease analysis is a political as well as technical exercise. The design choices (discount rates, age weights, how disability weights are elicited) determine whose suffering gets counted and how much, shaping global health funding priorities accordingly."
```

## Explainer

From your study of epidemiology, you can count cases, calculate rates, and measure how common diseases are across populations. But raw frequency doesn't tell you everything: a condition that kills people young versus one that causes decades of disability are very different burdens, even if they affect the same number of people. Burden of disease metrics were developed precisely to answer the follow-up question: across all the conditions affecting a population, which ones matter most in aggregate, and how do we weigh premature death against years lived with impairment?

The **DALY (disability-adjusted life year)** is the foundational metric of global burden of disease analysis. One DALY equals one year of healthy life lost — either through premature death or through living with disability. It has two components. **YLL (years of life lost to premature mortality)** counts the gap between age at death and expected age of death from a reference life table — a 25-year-old dying loses roughly 57 YLL, while a 75-year-old dying loses about 12. **YLD (years lived with disability)** multiplies the duration of living with a condition by a **disability weight** between 0 (perfect health) and 1 (equivalent to death). A person living 10 years with moderate depression (disability weight ≈ 0.4) contributes 4 YLD. DALY = YLL + YLD. This additive structure means a chronic non-fatal condition creating decades of moderate impairment can dominate the burden calculation even if its mortality is low — which is exactly the epidemiological transition pattern seen globally as infectious disease mortality falls and non-communicable disease disability rises.

The **QALY (quality-adjusted life year)** is the health economic parallel. One QALY is one year of life in perfect health. It is used to evaluate interventions: an intervention producing 5 QALYs at a cost of $50,000 has an **incremental cost-effectiveness ratio (ICER)** of $10,000 per QALY. Most high-income healthcare systems use a threshold (commonly $50,000–$100,000 per QALY in the US, £20,000–30,000 per QALY in the UK's NICE assessments) to determine whether a treatment provides sufficient value. Unlike DALYs, QALYs are typically elicited from patients or the public through preference surveys (time trade-off, standard gamble) — you ask people how many years of life in a health state they would trade for fewer years in perfect health. The difference from disability weights is subtle but important: DALYs use weights set by expert panels and are meant to represent societal values consistently across the GBD study; QALYs can use weights elicited from the patients actually experiencing a condition, potentially capturing their adaptation to illness.

Both metrics embed explicit value judgments that are worth examining critically. Disability weights assume that living with a given condition is worse than perfect health by a fixed factor — but whether an amputee experiencing a full life should be counted as "losing" 0.3 of each year lived is philosophically contested, particularly within disability rights frameworks. Discount rates (which reduce the value of future health years, typically at 3% annually) deprioritize conditions affecting the young relative to those affecting the middle-aged, and conditions whose harms materialize decades later. Age-weighting, used in earlier DALY formulations, explicitly valued a year of life in young adulthood more than a year in childhood or old age. These aren't bugs in the methodology — they're design choices with enormous implications for which conditions rank as global priorities and which interventions get funded. Reading burden of disease data critically means understanding not just the numbers, but the architecture of values embedded in how they were produced.
