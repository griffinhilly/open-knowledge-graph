---
id: cost-benefit-analysis-health
title: Cost-Benefit Analysis in Health
domain: health-and-human-development
course: health-economics
prerequisites:
- id: cost-effectiveness-analysis
  type: hard
- id: cost-utility-analysis
  type: soft
builds-toward:
- willingness-to-pay-health
- economic-evaluation-methods
tags:
- CBA
- monetary-valuation
- VSL
- willingness-to-pay
- net-benefit
stage: advanced
status: validated
---

# Cost-Benefit Analysis in Health

## Core Idea
Cost-benefit analysis (CBA) in health converts both costs and health outcomes into monetary terms, enabling a direct comparison: if the monetized benefits exceed the costs, the intervention increases social welfare. Unlike CEA (which produces a ratio requiring a threshold for interpretation), CBA produces a net benefit in dollars — a positive net benefit means the intervention is worth doing. The key challenge is assigning a monetary value to health outcomes, particularly life itself. The Value of a Statistical Life (VSL) — derived from observed tradeoffs people make between money and mortality risk (wage-risk studies, consumer behavior) — is the standard approach, with current US estimates around $10-12 million. CBA is the standard framework in environmental and transportation policy but is controversial in health because of discomfort with explicitly pricing life and because the VSL varies with income, raising equity concerns.

## Questions

```yaml
- question: "An air quality regulation reduces annual mortality by 100 deaths at a cost of $500 million. Using a VSL of $10 million, what is the net benefit?"
  type: multiple-choice
  options:
    - "Net benefit = $500 million (the regulation pays for itself)"
    - "Net benefit = $500 million (100 lives × $10M - $500M = $500M)"
    - "Net benefit = -$500 million (the cost exceeds the number of deaths prevented)"
    - "Cannot be calculated without knowing who dies"
  answer: 1
  explanation: "Monetized benefit = 100 statistical lives × $10 million = $1 billion. Cost = $500 million. Net benefit = $1 billion - $500 million = $500 million. The regulation passes the CBA test. The VSL does not mean each life is 'worth' $10 million — it reflects the aggregate willingness of the affected population to pay for small reductions in mortality risk. The $10 million figure comes from observing that people accept approximately $1,000 in additional annual income for a 1/10,000 increase in annual mortality risk (1,000 × 10,000 = $10M)."

- question: "CBA's reliance on the VSL means that health interventions benefiting wealthier populations will always show larger net benefits, because higher-income individuals have higher VSL (they are willing to pay more for risk reduction)."
  type: true-false
  answer: true
  explanation: "This is the most serious equity critique of CBA in health. VSL is derived from willingness-to-pay, which is constrained by ability-to-pay. A wealthy person's VSL may be $15 million while a low-income person's is $5 million — not because the rich person's life is more valuable, but because they have more resources to trade for safety. Using income-differentiated VSLs would systematically favor interventions for the wealthy. Most regulatory agencies use a single VSL for all populations to avoid this inequity, but this is an ethical choice, not an economic one."

- question: "Explain why cost-effectiveness analysis is more commonly used than cost-benefit analysis for healthcare resource allocation decisions."
  type: short-answer
  answer: "CEA avoids the controversial step of placing a monetary value on health outcomes. It compares interventions using natural health units (QALYs, life-years) and a cost-effectiveness ratio, which is then judged against a threshold. CBA requires explicitly monetizing health, which raises ethical objections (commodifying life), methodological challenges (which valuation method? whose willingness to pay?), and equity concerns (VSL varies with income). CEA is also more intuitive for clinicians and health policymakers who think in terms of health outcomes rather than dollar values. However, CBA is standard in regulatory impact analysis (environmental, transportation) where health is one of many outcomes that must be compared on a common scale."
  explanation: "The threshold used in CEA (e.g., $50,000/QALY) implicitly places a monetary value on health — if society will pay up to $50,000 for one QALY, that is an implicit valuation. The difference is that CEA keeps this valuation implicit and allows different thresholds for different contexts, while CBA makes it explicit through the VSL. The implicit approach is considered more politically and ethically palatable in healthcare settings."
```

## Explainer

Cost-effectiveness analysis tells you which intervention produces the most health per dollar, but it cannot tell you whether the health gains are worth the cost in absolute terms — you need a threshold, and the threshold is ultimately a judgment call. **Cost-benefit analysis** resolves this by converting everything into dollars: if monetized benefits exceed costs, the intervention increases social welfare. This directness is both CBA's strength and the source of its controversy.

The central methodological challenge is **monetizing health outcomes**, especially life and death. The standard concept is the **Value of a Statistical Life** (VSL), which does not claim to price an identified individual's life. Instead, it measures the aggregate value of small reductions in mortality risk. If 10,000 people are each willing to pay $1,000 for a safety measure that reduces each person's annual mortality risk by 1/10,000, the implied VSL is $1,000 × 10,000 = $10 million. This is the value of one "statistical" life — the prevention of one expected death among a large group.

VSL estimates come from two sources. **Revealed preference** studies examine real-world tradeoffs: workers accepting higher wages for riskier jobs, consumers paying more for safer cars, or homebuyers paying premiums for homes away from pollution sources. **Stated preference** studies use surveys to elicit willingness-to-pay for hypothetical risk reductions. Current US regulatory estimates center around $10-12 million, though estimates vary by method, population, and type of risk.

The equity implications of CBA are its Achilles' heel in health applications. Because willingness-to-pay is constrained by ability-to-pay, VSL estimates are higher for wealthier populations. Using differentiated VSLs would mean that a policy saving 100 lives in a wealthy suburb generates more "benefit" than one saving 100 lives in a low-income neighborhood — a conclusion most societies find morally unacceptable. This is why healthcare resource allocation generally uses CEA with QALYs (which do not depend on income) rather than CBA with VSLs. CBA remains dominant in environmental and transportation regulation, where health impacts must be weighed against non-health costs and benefits on a common monetary scale.
