---
id: cost-effectiveness-analysis
title: Cost-Effectiveness Analysis in Policy Research
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: research-design-advanced
  type: hard
- id: linear-regression-social-science
  type: soft
- id: linear-programming
  type: soft
tags:
- policy
- evaluation
- economics
- efficiency
stage: advanced
status: validated
---

# Cost-Effectiveness Analysis in Policy Research

## Core Idea
Cost-effectiveness analysis (CEA) compares the costs and health or social benefits of interventions. The cost-effectiveness ratio divides cost by benefit (e.g., cost per QALY gained); interventions are ranked by efficiency. CEA informs resource allocation but requires defining what counts as a benefit and willingness-to-pay thresholds. Unlike randomized trials, CEA is observational and depends on assumptions about cost attribution and benefit measurement. CEA is widely used in public health, education, and social policy.

## Questions

```yaml
- question: "Program A costs $200,000 and produces 50 QALYs. Program B costs $100,000 and produces 20 QALYs. A policymaker funds Program B because it costs less. What error in cost-effectiveness reasoning is this?"
  type: multiple-choice
  options:
    - "No error — lower total cost always indicates better cost-effectiveness"
    - "Confusing cost-effectiveness with cost-minimization — Program A produces more benefit per dollar ($4,000/QALY vs. $5,000/QALY)"
    - "Failing to apply the willingness-to-pay threshold — without it, neither program can be ranked"
    - "Using QALYs inappropriately — cost minimization requires a different benefit metric"
  answer: 1
  explanation: "Cost-effectiveness is measured by the cost-effectiveness ratio: total cost divided by total benefit. Program A: $200,000 / 50 QALYs = $4,000/QALY. Program B: $100,000 / 20 QALYs = $5,000/QALY. Program A is more cost-effective despite costing more in absolute terms. The policymaker is conflating cost minimization with cost-effectiveness — funding the cheaper program without asking how much benefit each dollar buys misses the entire point of CEA."

- question: "A CEA concludes a new education program costs $8,000 per additional year of schooling completed. A critic argues this finding is meaningless without a willingness-to-pay (WTP) threshold. The critic is:"
  type: multiple-choice
  options:
    - "Wrong — a lower CER is always preferable regardless of WTP"
    - "Wrong — WTP thresholds only apply to healthcare CEA, not education"
    - "Right — whether $8,000 per year-of-schooling represents good value depends on how much society is willing to spend per unit of that outcome"
    - "Partly right — WTP only matters when the program costs more than existing alternatives"
  answer: 2
  explanation: "The CER tells you the price per outcome unit, but not whether that price is worth paying. That judgment requires a WTP threshold — a policy choice about how much society will spend per unit of benefit. $8,000/year-of-schooling could be excellent value (if the threshold is $20,000) or poor value (if it is $3,000). The threshold is 'itself a policy choice, not a mathematical fact.' WTP thresholds apply across all CEA domains, not just healthcare."

- question: "The choice of benefit metric in a CEA — whether to use QALYs, earnings gains, or crime reduction — embeds value judgments that the analysis itself cannot resolve."
  type: true-false
  answer: true
  explanation: "Defining and measuring 'benefit' requires normative choices. QALY calculations require judgments about health-state quality weights. Educational CEA must decide whether the relevant benefit is earnings, test scores, social mobility, or civic participation. These choices privilege certain values over others. CEA can quantify tradeoffs rigorously once a metric is chosen, but cannot determine which metric is right — that requires ethical and political reasoning outside the model."

- question: "The most cost-effective intervention is typically the one with the lowest total program cost."
  type: true-false
  answer: false
  explanation: "Cost-effectiveness is measured by the cost-effectiveness ratio (total cost / total benefit), not total cost alone. A more expensive program that produces proportionally more benefit can be more cost-effective than a cheaper one. Cost minimization and cost-effectiveness are fundamentally different objectives. Confusing them — funding the cheapest option regardless of how much benefit it produces — is one of the most common errors in policy evaluation."

- question: "Why is sensitivity analysis essential to an honest cost-effectiveness analysis, and what does it reveal about the nature of CEA conclusions?"
  type: short-answer
  answer: "CEA conclusions depend on assumptions about cost attribution, benefit measurement, discount rates, and counterfactual comparisons. Sensitivity analysis varies these assumptions to show how much the CER changes — revealing which assumptions are load-bearing. A finding cost-effective only under optimistic assumptions is fundamentally less credible than one that holds across a wide range of reasonable values."
  explanation: "Because CEA typically uses observational data rather than randomized experiments, the causal assumptions in the underlying models do real work. Sensitivity analysis makes those assumptions visible and testable rather than buried. A conclusion that survives many different reasonable assumptions is more robust than one that hinges on a single favorable parameter choice. Sensitivity analysis doesn't undermine CEA — it is what makes it scientifically honest rather than advocacy dressed as analysis."
```

## Explainer

You know from your advanced research design background that not all interventions produce equal outcomes, and from regression that we can model relationships between variables. Cost-effectiveness analysis asks a harder question: given limited resources, which interventions produce the most benefit per dollar spent? It is the tool that forces a comparison that policy debates often avoid — not "does this program work?" but "does it work well enough given what it costs, relative to alternatives?"

The core calculation is the **cost-effectiveness ratio (CER)**: total program cost divided by total units of benefit produced. In health care, the standard benefit unit is the **Quality-Adjusted Life Year (QALY)** — one year lived in perfect health, with health states below perfect health assigned fractional weights. An intervention costing $50,000 that produces 5 QALYs has a CER of $10,000 per QALY. Whether that is "good" depends on the **willingness-to-pay threshold**: the maximum a payer is willing to spend per unit of benefit. UK health authorities use roughly £20,000–30,000 per QALY; interventions below the threshold are typically funded, those above face scrutiny. The threshold is itself a policy choice, not a mathematical fact.

The deeper challenge is defining and measuring the benefit unit. QALY calculations require judgments about the quality weight assigned to health states — living with diabetes counts as less than a full QALY per year, but how much less? These weights are elicited through surveys and involve normative assumptions about which lives are worth how much. In social policy (education, crime prevention, workforce training), defining a comparable unit is even harder. What is the "benefit unit" for a literacy program? Lifetime earnings? Crime reduction? Social mobility? The choice of benefit metric embeds value judgments that CEA cannot resolve on its own.

Your regression skills are directly relevant to CEA's empirical side. Program costs are rarely simple line items — analysts must attribute overhead, estimate counterfactual costs, and control for unmeasured confounders in outcomes. CEA typically relies on observational data rather than randomized trials, which means the causal assumptions in your regression models are doing real work. **Sensitivity analyses** — varying the key assumptions to see how much the CER changes — are essential to honest CEA. A conclusion that a program is cost-effective is only as credible as its most consequential assumptions, and transparent sensitivity analysis is how analysts signal where the real uncertainty lies.
