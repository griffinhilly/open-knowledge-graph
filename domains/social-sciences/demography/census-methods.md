---
id: census-methods
title: Census Methods
domain: social-sciences
course: demography
prerequisites:
- id: population-dynamics
  type: hard
- id: survey-sampling-methods
  type: soft
builds-toward:
- vital-registration-systems
- demographic-estimation-techniques
tags:
- census
- enumeration
- de-jure
- de-facto
- coverage
stage: advanced
status: validated
---

# Census Methods

## Core Idea
A population census is a complete enumeration of all persons in a defined territory at a specific point in time. Censuses provide the denominator for virtually all demographic rates and the baseline for population estimates and projections between census years. Key methodological choices include de facto (counting people where they are on census night) versus de jure (counting people at their usual residence), individual versus household-based enumeration, and the trade-off between census frequency and cost. Census errors include under-coverage (missing people, particularly marginalized populations), over-coverage (counting people twice), content error (inaccurate responses), and processing error. Post-enumeration surveys estimate coverage rates, and census data are adjusted for known biases before use. Modern census alternatives include register-based censuses (using administrative records) and rolling surveys, adopted by some countries to reduce cost.

## How It's Best Learned
Examine the questionnaire and methodology documentation for a real census (e.g., US Census 2020 or a country with published methodology). Identify the decisions made about enumeration type, question design, and coverage evaluation. Then compare coverage estimates across demographic groups to see which populations are hardest to count.

## Common Misconceptions
- A census is not a survey — it aims to count every person, not a sample. However, some census systems use sampling for detailed questions (the "long form") while enumerating everyone with basic questions (the "short form").
- Census under-counts are not random — they systematically miss young men, minorities, homeless populations, undocumented migrants, and people in remote areas, introducing bias into the demographic data derived from census denominators.

## Questions

```yaml
- question: "What is the primary difference between a de facto and a de jure census, and when would you prefer each approach?"
  type: multiple-choice
  options:
    - "De facto counts people at their usual residence; de jure counts them where they are on census night"
    - "De facto counts people where they are on census night; de jure counts them at their usual residence — de facto is simpler operationally but de jure is preferred for calculating demographic rates at the usual place of residence"
    - "There is no practical difference; both methods produce identical results"
    - "De facto only counts citizens; de jure counts all persons including non-citizens"
  answer: 1
  explanation: "De facto enumeration records people wherever they happen to be at the moment of enumeration — simple to implement because it avoids determining 'usual residence.' De jure enumeration assigns people to their usual place of residence, which is more useful for computing local demographic rates (since it matches people with the area where they normally live, work, and use services). The choice matters for populations with high mobility: de facto counts will over-represent tourist destinations and under-represent areas with temporary outmigration."

- question: "Census under-coverage affects all demographic groups equally, so it does not bias demographic rates."
  type: true-false
  answer: false
  explanation: "Census under-coverage is systematically biased by age, sex, race/ethnicity, socioeconomic status, and housing situation. Young men, racial minorities, homeless populations, and undocumented immigrants are consistently under-counted in most censuses. This differential under-coverage biases demographic rates: if the denominator (population) is too low for a group, rates derived from that denominator (death rates, birth rates) will be too high. Post-enumeration surveys allow statistical adjustment, but the corrections themselves carry uncertainty."

- question: "Explain what a post-enumeration survey (PES) is and why it is considered essential to modern census practice."
  type: short-answer
  answer: "A post-enumeration survey (PES) is an independent survey conducted shortly after the census in a sample of areas, using a different enumeration team. It independently lists and interviews residents, then matches results against the census records to estimate how many people the census missed (under-coverage) and how many were counted more than once (over-coverage). The PES is essential because no census achieves perfect coverage, and the pattern of coverage errors is not random — it is systematically biased toward missing certain groups. Without a PES, users of census data cannot know the magnitude or direction of coverage errors, and demographic rates derived from census denominators may be misleading."
  explanation: "The dual-system estimation method used in PES applications is a demographic version of capture-recapture from ecology. The census is one 'capture' and the PES is another; the overlap between them estimates the total population. The method assumes independence between the two captures — an assumption that is never perfectly met but provides a workable approximation for coverage estimation."
```

## Explainer

Every demographic rate you have studied — crude birth rates, crude death rates, age-specific rates, dependency ratios — requires a **denominator**: the population at risk. That denominator ultimately comes from the population **census**, the most fundamental data collection operation in demography. Without census counts, the entire architecture of demographic measurement collapses into numerators without denominators.

A census aims to **enumerate every person** in a defined territory at a specific point in time. This distinguishes it from a survey, which draws a sample. The complete enumeration principle means a census can provide data for small geographic areas and small population subgroups that surveys cannot — a property essential for electoral apportionment, service planning, and resource allocation.

Two fundamental approaches exist. In a **de facto** census, enumerators count people wherever they are found on census night. This is operationally simple — you count the person in the dwelling where they sleep — but it places visitors and travelers in the wrong geographic unit. In a **de jure** census, people are assigned to their usual place of residence, regardless of where they are on census night. This produces better denominators for local demographic rates but requires more complex enumeration (determining each person's usual residence, handling people with multiple residences, tracing people who are temporarily away).

No census achieves perfect coverage. **Under-coverage** — missing people entirely — is the most serious error because it systematically affects certain groups: young men (who may be transient or avoiding enumeration), racial and ethnic minorities, homeless populations, undocumented immigrants, and people in remote or conflict-affected areas. **Over-coverage** — counting people more than once — can occur when people with multiple residences are enumerated at each one. The **post-enumeration survey** (PES) estimates these errors through an independent re-enumeration of a sample of areas, using capture-recapture logic: if the census found 95% of the people that the PES independently found, then the census missed approximately 5%. These estimates allow statistical adjustment of census totals.

Modern alternatives to the traditional census are emerging. Several Nordic countries now conduct **register-based censuses** using administrative records (population registers, tax records, property databases) instead of direct enumeration, dramatically reducing cost and respondent burden. France replaced its traditional decennial census with a **rolling survey** that covers the entire country over five-year cycles. These innovations reflect the tension between the census ideal (complete enumeration) and its practical limitations (enormous cost, declining response rates, and the inherent difficulty of counting mobile, complex populations).
