---
id: cost-effectiveness-analysis-health-econ
title: Cost-Effectiveness Analysis
domain: health-and-human-development
course: health-economics
prerequisites:
- id: healthcare-market-structure
  type: soft
- id: healthcare-financing
  type: soft
builds-toward:
- cost-utility-analysis
- health-technology-assessment
- economic-evaluation-methods
tags:
- CEA
- ICER
- threshold
- dominance
- cost-effectiveness-plane
stage: advanced
status: validated
---

# Cost-Effectiveness Analysis

## Core Idea
Cost-effectiveness analysis (CEA) compares the costs and health outcomes of alternative interventions by computing the incremental cost-effectiveness ratio (ICER): the additional cost per additional unit of health outcome (e.g., life-year gained, infection prevented, blood pressure point reduced). ICER = (Cost_new - Cost_comparator) / (Effect_new - Effect_comparator). An intervention is cost-effective if its ICER falls below a decision threshold representing the maximum amount society is willing to pay for one unit of health outcome. CEA informs resource allocation by identifying which interventions produce the most health per dollar spent, enabling comparison across different diseases and treatment areas. It explicitly does not tell you what to do — it provides information about tradeoffs that decision-makers must weigh alongside equity, political feasibility, and other values.

## Questions

```yaml
- question: "Drug A costs $50,000 more than Drug B per patient and produces 0.5 additional life-years. The ICER is $100,000 per life-year gained. If the willingness-to-pay threshold is $50,000 per life-year, is Drug A cost-effective?"
  type: multiple-choice
  options:
    - "Yes — $100,000 per life-year is a reasonable price for saving lives"
    - "No — the ICER of $100,000 exceeds the willingness-to-pay threshold of $50,000, so Drug A does not provide sufficient health benefit relative to its additional cost"
    - "It depends on whether Drug A is for cancer or heart disease"
    - "The ICER is meaningless without knowing the total budget"
  answer: 1
  explanation: "At an ICER of $100,000 per life-year and a threshold of $50,000, Drug A costs twice as much per life-year as society is willing to pay. The same $50,000 spent elsewhere in the health system could produce one full life-year, whereas spending it on Drug A produces only half a life-year. Drug A is not cost-effective at this threshold — which does not mean it is ineffective, only that its incremental benefit does not justify its incremental cost relative to other uses of healthcare resources."

- question: "An intervention that is both cheaper and more effective than the comparator is said to 'dominate' the comparator. In this case, no ICER calculation is needed."
  type: true-false
  answer: true
  explanation: "Dominance means the new intervention is better on both dimensions — it costs less AND produces better outcomes. There is no tradeoff to evaluate: the dominant intervention is unambiguously preferred. The ICER is only meaningful when there is a tradeoff — more effective but more costly (the usual case) or less effective but cheaper. When dominance exists, the dominated strategy should be eliminated from consideration."

- question: "A public health official must choose between three programs: a vaccination campaign (ICER = $5,000/QALY), a screening program (ICER = $25,000/QALY), and a drug treatment (ICER = $150,000/QALY). With a fixed budget, what is the economically efficient allocation strategy?"
  type: short-answer
  answer: "Fund programs in order of their cost-effectiveness ratio, starting with the lowest ICER. First fund the vaccination campaign ($5,000/QALY), then the screening program ($25,000/QALY), and finally the drug treatment ($150,000/QALY) only if budget remains. This maximizes total health produced from the fixed budget. However, cost-effectiveness is one input to the decision — equity considerations (who benefits), severity of illness, and political feasibility also matter and may justify funding a less cost-effective program that serves a disadvantaged population."
  explanation: "This is the league table approach to priority setting. By ranking all interventions by ICER and funding from the top down until the budget is exhausted, the health system maximizes QALYs (or whatever outcome metric is used). The threshold willingness-to-pay is implicitly defined by where the budget runs out — the ICER of the last funded intervention. In practice, most countries use explicit thresholds (£20,000-30,000/QALY in the UK, roughly $50,000-150,000/QALY in the US) rather than strict league-table rationing."
```

## Explainer

Healthcare resources are finite, but health needs are effectively unlimited — there will always be more beneficial interventions than money to fund them. **Cost-effectiveness analysis** provides a systematic framework for making allocation decisions by comparing what you get (health outcomes) to what you give up (resources that could be used elsewhere). It does not determine whether an intervention is "worth it" in some absolute sense — it compares alternatives and identifies which provides the best value.

The **ICER** is the workhorse metric. For two interventions A and B, ICER = (Cost_A - Cost_B) / (Effect_A - Effect_B). This represents the additional cost per additional unit of health outcome when choosing A over B. If A costs $100,000 more and produces 2 additional life-years, the ICER is $50,000 per life-year. The ICER is meaningful only when the new intervention is both more effective and more costly — a tradeoff exists. If the new intervention is more effective and cheaper, it **dominates** and should be chosen without further analysis.

The ICER is compared to a **willingness-to-pay threshold** — the maximum amount society considers acceptable for one unit of health gain. The UK's NICE uses £20,000-30,000 per QALY as its threshold. The WHO has suggested 1-3 times GDP per capita as a benchmark. The US does not use an official threshold but implicit thresholds range from $50,000 to $200,000 per QALY depending on the context. If the ICER falls below the threshold, the intervention is considered cost-effective — the health benefit justifies the cost.

CEA has important limitations. The **perspective** matters: a societal perspective includes all costs (direct medical, patient time, productivity losses), while a healthcare system perspective includes only direct medical costs. Different perspectives can lead to different conclusions. **Discounting** (reducing the value of future costs and benefits) is standard practice, typically at 3% annually, because a dollar today is worth more than a dollar in ten years. **Sensitivity analysis** tests whether the conclusion changes under different assumptions about uncertain parameters (treatment effect, costs, time horizon). And CEA says nothing about **equity** — a cost-effective intervention that benefits the wealthy may be less socially valuable than a less cost-effective one that benefits the poor. These are reasons CEA informs but does not replace decision-making.
