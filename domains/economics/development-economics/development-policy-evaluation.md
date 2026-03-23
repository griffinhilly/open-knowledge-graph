---
id: development-policy-evaluation
title: Development Policy Evaluation and Impact Assessment
domain: economics
course: development-economics
prerequisites:
- id: randomized-experiments-development-economics
  type: hard
- id: causal-inference-econometrics
  type: soft
tags:
- impact evaluation
- policy assessment
- methodology
- evidence
stage: expert
status: draft
---

# Development Policy Evaluation and Impact Assessment

## Core Idea
Evaluating development policies requires isolating causal effects through RCTs, regression discontinuity, instrumental variables, or difference-in-differences. Each has strengths and limitations. Evidence-based development now requires rigorous evaluation, shifting policy from intuition toward empirical demonstration of what works, for whom, and at what cost.

## Questions

```yaml
- question: "A government cash transfer program targets households with a poverty score below 50 on a 0–100 index. A researcher wants to estimate the causal effect of the transfer on child school enrollment. Which method best exploits this design?"
  type: multiple-choice
  options:
    - "A randomized controlled trial, randomly reassigning households above and below the threshold"
    - "Difference-in-differences, comparing enrolled children before and after the program"
    - "Regression discontinuity, comparing households just above and just below the score-50 threshold"
    - "Instrumental variables, using household income as an instrument for treatment status"
  answer: 2
  explanation: "The arbitrary score threshold creates a natural experiment: households just above 50 and just below 50 are nearly identical in all observable and unobservable characteristics, but one group receives the transfer and the other does not. Regression discontinuity exploits this sharp discontinuity to estimate the causal effect at the threshold. A new RCT would require randomly re-enrolling some ineligible households (ethically problematic). DID requires a clean pre-period. IV requires a separate instrument."

- question: "An RCT in rural Kenya finds that a microfinance program raises household income by 15%. A policymaker plans to scale it to urban Bangladesh, expecting similar effects. What is the primary methodological concern?"
  type: multiple-choice
  options:
    - "Internal validity — the randomization may have been compromised"
    - "Statistical power — the sample was too small to detect real effects"
    - "External validity — effects measured in one context may not generalize to a different population and setting"
    - "Attrition bias — households that left the study may have had higher incomes"
  answer: 2
  explanation: "External validity (generalizability) is the core concern. An RCT in rural Kenya measures the average treatment effect for that specific population, at that time, with that implementation. Urban Bangladesh may differ in financial infrastructure, social norms, credit markets, and economic shocks. What works in one context may have no effect, or even a negative effect, in another. This is not a flaw in the RCT's internal validity — within Kenya the estimate is credible — but a fundamental limit of any single-site evaluation."

- question: "A well-designed randomized controlled trial always provides more credible causal estimates than a quasi-experimental method such as regression discontinuity or instrumental variables."
  type: true-false
  answer: false
  explanation: "Method quality depends on execution and assumptions, not on the method label. A poorly implemented RCT — with high attrition, contamination between treatment and control, or compliance problems — can produce less credible estimates than a well-designed regression discontinuity that cleanly exploits a sharp, arbitrary cutoff. The evaluator's job is to match the method to the question and defend the identifying assumptions. No method is automatically superior."

- question: "The fundamental challenge in development policy evaluation is that we can never directly observe what would have happened to program participants had they not received the intervention."
  type: true-false
  answer: true
  explanation: "This is the counterfactual problem — the core challenge of causal inference. We observe the same person either treated or untreated, never both simultaneously. All evaluation methods (RCT, RD, DID, IV) are strategies for constructing a credible counterfactual by identifying a comparison group that represents what the treated group would have looked like without treatment. The method only changes how the counterfactual is constructed; the underlying problem is always the same."

- question: "Why is reporting that 'a program worked' insufficient for scaling decisions, and what additional information do policymakers need from an impact evaluation?"
  type: short-answer
  answer: "Policymakers need to know for whom the program worked (heterogeneous treatment effects across subgroups), at what cost (cost-effectiveness), under what conditions (implementation context, institutional capacity), and with what magnitude (effect size, not just statistical significance). A program that works for urban women but not rural men, costs $500 per beneficiary, and requires a trained NGO to implement cannot simply be scaled nationally in the same form."
  explanation: "Average treatment effects aggregate across a heterogeneous population. A positive average could hide null or negative effects for subgroups who should be excluded. Cost-effectiveness determines whether the same resources could produce more impact elsewhere. Implementation context determines whether the program can actually be replicated — many RCTs use NGOs with exceptional management capacity that governments cannot match. All of these details are required for a policy decision about scaling, modification, or abandonment."
```

## Explainer

From your work on randomized experiments in development economics, you know the gold standard for causal inference: randomly assign a program to some people and not others, then compare outcomes. But policy evaluation in development is broader than any single method. The core question is always the same — **what would have happened without the intervention?** — and the challenge is that we can never directly observe this counterfactual. Every evaluation method is a different strategy for constructing a credible comparison group.

**Randomized controlled trials (RCTs)** solve the comparison problem by design: random assignment ensures that treatment and control groups are statistically identical before the intervention, so any subsequent difference is caused by the program. But RCTs have real limitations. They are expensive and slow. They may not be ethical when the intervention is a basic right (you cannot randomly deny children vaccines). They measure average effects in a specific context, and what works in rural Kenya may not work in urban Bangladesh — this is the **external validity** problem. And some questions simply cannot be randomized: you cannot randomly assign countries to have different trade policies or institutional structures.

When randomization is impossible, economists turn to **quasi-experimental methods** that exploit natural variation. **Regression discontinuity** uses arbitrary cutoffs — a poverty program that serves households below a specific income threshold creates a natural experiment around that threshold, since households just above and just below are nearly identical. **Difference-in-differences** compares changes over time between a group affected by a policy and a group that was not, controlling for common trends. **Instrumental variables** use a source of variation that affects the treatment but has no direct effect on the outcome — for example, using distance to a school as an instrument for years of education. Each method requires specific assumptions, and the evaluator must argue convincingly that those assumptions hold.

The shift toward evidence-based policy has transformed development practice. Organizations like the World Bank and USAID now require impact evaluations for major programs. The key insight is not that RCTs are always best, but that **every policy claim implies a causal story**, and that story must be tested against data with an appropriate method. A well-designed quasi-experiment can be more informative than a poorly executed RCT. The evaluator's job is to match the method to the question, be transparent about assumptions, and report not just whether a program "worked" but **for whom, at what cost, and under what conditions** — because those details determine whether the program should be scaled, modified, or abandoned.
