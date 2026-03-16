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
tags:
- cost-effectiveness
- cea
- economic-evaluation
- health-economics
- icer
stage: abstract-reasoning
status: draft
---

# Economic Evaluation of Health Interventions

## Core Idea
Economic evaluation methods—cost-effectiveness analysis, cost-benefit analysis, budget impact analysis—quantify the health gained per resource spent on interventions. These analyses support resource allocation decisions and justify public health investments to policymakers and funders. Cost-effectiveness depends on context and local prices; assessment requires transparency about perspective, assumptions, and uncertainty.

## How It's Best Learned
Conduct a simple cost-effectiveness analysis comparing two interventions in your local context. Perform sensitivity analysis to examine how assumptions about costs and effectiveness affect conclusions about cost-effectiveness.

## Common Misconceptions
Cost-effectiveness analysis is the only input to policy decisions rather than one evidence source. Cost-effectiveness analysis avoids value judgments when discount rates and perspective reflect values. Cheaper interventions are always more cost-effective than expensive interventions.

## Explainer

You've already studied burden-of-disease metrics like DALYs and QALYs, which quantify how much health is lost or preserved by disease and intervention. Economic evaluation is the next step: it connects those health measures to costs, answering the question that burden metrics alone cannot — given limited resources, which intervention produces the most health per dollar? This question is uncomfortable but unavoidable in health policy, and the analytical methods are designed to make the tradeoffs explicit rather than hidden.

The most common tool is **cost-effectiveness analysis (CEA)**, which divides the difference in costs between two interventions by the difference in health outcomes. The result — the **incremental cost-effectiveness ratio (ICER)** — expresses how much one additional unit of health (typically one QALY or one DALY averted) costs when choosing one intervention over its comparator. For example, if a new drug costs $100,000 more per patient per year and produces 2 additional QALYs over the patient's lifetime, the ICER is $50,000/QALY. The ICER is compared to a willingness-to-pay threshold — a political and ethical judgment about what society will spend for one QALY. In the United States this is informally around $100,000–$150,000/QALY; in the UK, NICE uses approximately £20,000–£30,000/QALY. Interventions below the threshold are considered "cost-effective"; above it, they are not cost-effective given current resource constraints.

**Cost-benefit analysis (CBA)** is conceptually different: it converts health outcomes directly into monetary units, allowing comparison of health spending against other social investments (infrastructure, education). The challenge is the ethical discomfort of putting a dollar value on a life or year of healthy life, which makes CBA less common in health policy than CEA. **Budget impact analysis** is a practical complement: even a cost-effective intervention may be unaffordable in Year 1 if it affects a large population. Budget impact analysis projects the short-term financial consequences of adoption, which matters for government budget cycles that cannot absorb sudden large expenditures regardless of long-run value.

Your biostatistics background is essential here: economic evaluations depend on effect sizes from clinical trials or observational studies, and those estimates carry uncertainty. A key technique is **sensitivity analysis** — systematically varying the model's assumptions (discount rate, assumed duration of effectiveness, cost of adverse events) to see whether the conclusion changes. If the ICER stays below the threshold under almost all plausible assumptions, the intervention is robustly cost-effective. If it crosses the threshold under many assumptions, decision-makers need more data or must accept uncertainty. The transparency of these assumptions is what distinguishes credible economic evaluation from advocacy dressed in numbers — a distinction you should apply critically when reading any cost-effectiveness claim.
