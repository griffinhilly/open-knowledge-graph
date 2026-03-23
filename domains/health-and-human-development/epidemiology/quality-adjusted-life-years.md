---
id: quality-adjusted-life-years
title: Quality-Adjusted Life Years (QALYs)
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: global-burden-of-disease
  type: soft
- id: health-systems-and-financing
  type: soft
builds-toward:
- cost-effectiveness-analysis-epidemiology
tags:
- health-economics
- preference-based-measures
- utility-assessment
stage: expert
status: validated
---

# Quality-Adjusted Life Years (QALYs)

## Core Idea
QALYs measure health benefit by combining quantity of life (years lived) with quality of life (health-related quality of life or utility). QALY = years × utility weight, where utility reflects individual or population preferences for health states on a 0-1 scale (0 = death, 1 = perfect health). QALYs enable cost-effectiveness analysis by quantifying willingness-to-pay trade-offs. Different methods elicit utility weights (time trade-off, visual analog scale, preference-based instruments like EQ-5D), which substantially affect QALY calculations and cost-effectiveness conclusions.

## Questions

```yaml
- question: "A patient living with a chronic condition would trade 7 years in their current health state for 5 years in perfect health (and no more). Using the time trade-off method, what is their utility weight for this health state?"
  type: multiple-choice
  options:
    - "0.71, calculated as 5/7"
    - "0.40, calculated as (7 − 5)/5"
    - "2.00, calculated as 7/5 − 1"
    - "Cannot be determined without knowing the patient's age"
  answer: 0
  explanation: "In the time trade-off method, utility = (years in perfect health the patient accepts) / (years in current health state). If the patient is indifferent between 7 years in their current state and 5 years in perfect health, their utility is 5/7 ≈ 0.71. Option B reverses the logic, and option C is nonsensical. Age is irrelevant to the TTO calculation — it captures preference strength at the point of indifference, not absolute time remaining."

- question: "A new treatment costs $80,000 more than standard care and generates 1 QALY (2 years of life extension at utility 0.5). A second analyst reruns the calculation using EQ-5D tariffs instead of TTO weights and arrives at a utility of 0.3 for the same health state. What happens to the ICER?"
  type: multiple-choice
  options:
    - "The ICER remains $80,000/QALY because QALYs measure objective health improvement"
    - "The ICER rises to approximately $133,333/QALY because fewer QALYs are generated under the EQ-5D estimate"
    - "The ICER is unchanged because both methods measure the same underlying utility"
    - "The ICER falls because EQ-5D instruments are more precise than TTO"
  answer: 1
  explanation: "QALY = years × utility. Under TTO: 2 × 0.5 = 1 QALY → ICER = $80,000/QALY. Under EQ-5D: 2 × 0.3 = 0.6 QALYs → ICER = $80,000 / 0.6 ≈ $133,333/QALY. This is precisely why measurement method matters: different elicitation instruments assign different utility weights to the same health state, producing different ICER estimates — which can flip a coverage decision relative to a willingness-to-pay threshold."

- question: "A treatment that generates QALYs entirely by improving quality of life (utility) is treated identically in cost-effectiveness analysis to one that generates the same number of QALYs by extending lifespan."
  type: true-false
  answer: true
  explanation: "The QALY formula, years × utility, is agnostic about whether QALYs come from life extension or quality improvement. A treatment that adds 2 years at utility 0.5 (= 1 QALY) is treated identically to one that improves utility from 0.6 to 0.8 over 5 years (= 1 QALY increment). This equivalence is central to the QALY framework's power — and also a source of ethical controversy, since some argue that the route to health gain matters morally."

- question: "The disability paradox refers to the finding that people with disabilities consistently report lower quality of life than healthy populations predict, confirming that QALY estimates from patient reports accurately capture the burden of their condition."
  type: true-false
  answer: false
  explanation: "The disability paradox is the opposite finding: many people living with serious disabilities rate their quality of life as good or excellent — *higher* than healthy people imagining the same state would predict. This means population-based utility tariffs (derived from surveys of healthy respondents imagining disability) may *underestimate* the utility that adapted patients actually experience. Patient-reported utilities are often higher than tariff-based ones, complicating which source to use in ICER calculations."

- question: "Why does the method used to elicit utility weights (TTO, standard gamble, or EQ-5D tariff) matter for health policy decisions, rather than simply reflecting measurement error that averages out?"
  type: short-answer
  answer: "Each method captures a conceptually different quantity. TTO measures willingness to trade life-years; standard gamble measures tolerance of mortality risk; EQ-5D tariffs are derived from population surveys that may not reflect the preferences of people actually living with the condition. These are not interchangeable proxies for a single underlying utility — they can give systematically different values for the same health state. Because ICER = ΔCost / ΔQALY, even moderate differences in utility weight translate into large differences in ICER, potentially moving a treatment from cost-effective to unacceptable relative to a willingness-to-pay threshold."
  explanation: "The divergence between TTO and EQ-5D estimates introduces systematic, not random, error. A drug clearing a $50,000/QALY threshold using TTO weights might exceed $150,000/QALY using EQ-5D tariffs. Policymakers must be explicit about which method was used and what its limitations are — the choice is a substantive policy decision, not merely a statistical one."
```

## Explainer

When a health system or insurer must decide whether to fund a new treatment, it faces a fundamental comparison problem: how do you weigh a treatment that adds two years of life in perfect health against one that adds five years with significant disability? A simple "years of life" metric can't answer this. **Quality-Adjusted Life Years (QALYs)** address it by attaching a **utility weight** to each year lived — a number between 0 (equivalent to death) and 1 (perfect health) — and multiplying: QALY = years × utility. A person who lives 10 years with a utility of 0.6 (say, moderate chronic pain limiting activity) accumulates 6 QALYs. A treatment that raises that utility to 0.8 while extending life by 2 years would generate (12 × 0.8) − (10 × 0.6) = 9.6 − 6 = 3.6 incremental QALYs.

The most contested part of QALY calculation is how utility weights are derived. Three main methods are used. The **visual analog scale (VAS)** asks patients to mark their current health state on a line from 0 to 100 — quick but considered less reliable because it doesn't require trade-offs. The **time trade-off (TTO)** method asks: "How many years in your current health state would you trade for X years in perfect health?" If someone would trade 8 years in their current state for 6 years in perfect health, their utility is 6/8 = 0.75. The **standard gamble** method offers a choice between certain life in the current state versus a gamble with probability p of perfect health and (1−p) of immediate death; the utility equals the probability p at which the person is indifferent. TTO and standard gamble are preference-based and grounded in expected utility theory; VAS is not. Standardized instruments like the **EQ-5D** convert responses to pre-measured utility tariffs from population surveys, allowing consistent comparison across studies.

The QALY framework becomes powerful when combined with cost data in **cost-effectiveness analysis**. The key metric is the **incremental cost-effectiveness ratio (ICER)**: ICER = ΔCost / ΔQALY. If a new cancer drug costs $200,000 more than standard care and generates 2 more QALYs, its ICER is $100,000/QALY. Decision-makers then compare this to a **willingness-to-pay threshold** — in the UK's NICE, roughly £20,000–30,000/QALY; in the US, commonly cited as $50,000–$150,000/QALY. Treatments below the threshold are considered cost-effective; those above require special justification or negotiation.

Despite their utility, QALYs carry important limitations. Utility weights vary across populations: a patient who has adapted to disability may rate their utility higher than a healthy person imagining that state (**disability paradox**). QALYs also treat all years equally regardless of age, which raises equity concerns — a QALY gained by a child effectively counts the same as one gained at age 80. And measurement method matters: TTO, standard gamble, and EQ-5D tariffs for the same health state can differ substantially, producing different ICERs and different funding decisions. Understanding these limitations is essential for critically interpreting cost-effectiveness analyses in health policy discussions.
