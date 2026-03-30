---
id: economic-evaluation-health-interventions
title: Economic Evaluation of Health Interventions
domain: health-and-human-development
course: public-health
prerequisites:
- id: biostatistics-in-public-health
  type: hard
- id: burden-of-disease-metrics
  type: hard
- id: cost-effectiveness-and-economic-evaluation-health
  type: soft
tags:
- cost-effectiveness
- cea
- economic-evaluation
- health-economics
- icer
stage: advanced
status: validated
---
# Economic Evaluation of Health Interventions

## Core Idea
Economic evaluation methods—cost-effectiveness analysis, cost-benefit analysis, budget impact analysis—quantify the health gained per resource spent on interventions. These analyses support resource allocation decisions and justify public health investments to policymakers and funders. Cost-effectiveness depends on context and local prices; assessment requires transparency about perspective, assumptions, and uncertainty.

## How It's Best Learned
Conduct a simple cost-effectiveness analysis comparing two interventions in your local context. Perform sensitivity analysis to examine how assumptions about costs and effectiveness affect conclusions about cost-effectiveness.

## Common Misconceptions
Cost-effectiveness analysis is the only input to policy decisions rather than one evidence source. Cost-effectiveness analysis avoids value judgments when discount rates and perspective reflect values. Cheaper interventions are always more cost-effective than expensive interventions.

## Questions

```yaml
- question: "Drug A costs $500 more than standard care and produces 0.01 additional QALYs per patient (ICER = $50,000/QALY). Drug B costs $50,000 more than standard care and produces 1 additional QALY per patient (ICER = $50,000/QALY). With a willingness-to-pay threshold of $100,000/QALY, which drug is more cost-effective?"
  type: multiple-choice
  options:
    - "Drug A — it is much cheaper, making it more affordable and therefore more cost-effective"
    - "Both are equally cost-effective — they have identical ICERs relative to the threshold"
    - "Drug B — it produces far greater absolute health benefit at the same ICER"
    - "Neither can be assessed without knowing the budget impact for each drug"
  answer: 1
  explanation: "Both drugs have identical ICERs of $50,000/QALY — both are equally cost-effective relative to the threshold. Cost-effectiveness is defined by the ratio of incremental cost to incremental health gain, not by absolute cost. This directly targets the common misconception that cheaper interventions are automatically more cost-effective. Drug A costs less in absolute terms, but Drug B produces 100 times more health at the same cost per QALY. The ICER is the relevant metric, not the price tag."

- question: "Which type of economic evaluation converts health outcomes into monetary units to allow comparison with non-health public investments such as road safety or education spending?"
  type: multiple-choice
  options:
    - "Cost-effectiveness analysis, using QALYs or DALYs as the health outcome"
    - "Budget impact analysis, projecting fiscal consequences over a time horizon"
    - "Cost-benefit analysis, assigning dollar values to health outcomes"
    - "Sensitivity analysis, testing assumptions about cost and effectiveness"
  answer: 2
  explanation: "Cost-benefit analysis (CBA) places monetary values on health outcomes (e.g., a statistical life or a healthy year), enabling comparisons between health spending and other social investments. This is philosophically distinct from CEA, which uses natural health units and compares within health. The Explainer notes that CBA is less common in health policy partly due to the ethical discomfort of monetizing life — but it is the only method that enables direct cross-sector resource comparison."

- question: "A cost-effectiveness analysis finding that a new intervention has an ICER below the willingness-to-pay threshold proves that governments should adopt the intervention immediately."
  type: true-false
  answer: false
  explanation: "Cost-effectiveness analysis is one input into policy decisions, not the sole determinant. Other relevant factors include budget impact (a cost-effective intervention affecting millions may cause a short-term fiscal crisis), equity considerations, uncertainty in model assumptions, and the political values embedded in the willingness-to-pay threshold itself. The Common Misconceptions explicitly warn against treating CEA as the only input to policy decisions."

- question: "The discount rate used in a cost-effectiveness model reflects a value judgment, not just a technical economic parameter."
  type: true-false
  answer: true
  explanation: "Discounting future health benefits at a positive rate implies that a QALY gained today is worth more than a QALY gained in the future — a value judgment about how society weighs present versus future welfare. The Explainer notes that discount rates and the choice of perspective (payer, patient, societal) embed values into the analysis. Two analysts using different discount rates for the same intervention can reach different conclusions about cost-effectiveness, which is why transparency about assumptions is essential."

- question: "Why must the ICER always be calculated relative to a specific comparator rather than expressed as an absolute number on its own?"
  type: short-answer
  answer: "The ICER is an incremental measure: it quantifies the additional cost per additional QALY gained by choosing one intervention over another. Without specifying the comparator, 'additional' is undefined — you cannot determine how much extra health the intervention produces or how much more it costs. An intervention that looks expensive compared to no treatment might look cost-effective compared to current standard of care, or vice versa. The ICER only makes sense as a relational measure between two alternatives."
  explanation: "Policy decisions are always choices between alternatives, so the cost-effectiveness of any intervention is inherently context-dependent on what it is being compared to. Reporting an ICER without naming the comparator — or comparing ICERs from different studies that used different comparators — is a common source of confusion in the health policy literature."
```

## Explainer

You've already studied burden-of-disease metrics like DALYs and QALYs, which quantify how much health is lost or preserved by disease and intervention. Economic evaluation is the next step: it connects those health measures to costs, answering the question that burden metrics alone cannot — given limited resources, which intervention produces the most health per dollar? This question is uncomfortable but unavoidable in health policy, and the analytical methods are designed to make the tradeoffs explicit rather than hidden.

The most common tool is **cost-effectiveness analysis (CEA)**, which divides the difference in costs between two interventions by the difference in health outcomes. The result — the **incremental cost-effectiveness ratio (ICER)** — expresses how much one additional unit of health (typically one QALY or one DALY averted) costs when choosing one intervention over its comparator. For example, if a new drug costs $100,000 more per patient per year and produces 2 additional QALYs over the patient's lifetime, the ICER is $50,000/QALY. The ICER is compared to a willingness-to-pay threshold — a political and ethical judgment about what society will spend for one QALY. In the United States this is informally around $100,000–$150,000/QALY; in the UK, NICE uses approximately £20,000–£30,000/QALY. Interventions below the threshold are considered "cost-effective"; above it, they are not cost-effective given current resource constraints.

**Cost-benefit analysis (CBA)** is conceptually different: it converts health outcomes directly into monetary units, allowing comparison of health spending against other social investments (infrastructure, education). The challenge is the ethical discomfort of putting a dollar value on a life or year of healthy life, which makes CBA less common in health policy than CEA. **Budget impact analysis** is a practical complement: even a cost-effective intervention may be unaffordable in Year 1 if it affects a large population. Budget impact analysis projects the short-term financial consequences of adoption, which matters for government budget cycles that cannot absorb sudden large expenditures regardless of long-run value.

Your biostatistics background is essential here: economic evaluations depend on effect sizes from clinical trials or observational studies, and those estimates carry uncertainty. A key technique is **sensitivity analysis** — systematically varying the model's assumptions (discount rate, assumed duration of effectiveness, cost of adverse events) to see whether the conclusion changes. If the ICER stays below the threshold under almost all plausible assumptions, the intervention is robustly cost-effective. If it crosses the threshold under many assumptions, decision-makers need more data or must accept uncertainty. The transparency of these assumptions is what distinguishes credible economic evaluation from advocacy dressed in numbers — a distinction you should apply critically when reading any cost-effectiveness claim.
