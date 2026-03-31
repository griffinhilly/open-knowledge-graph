---
id: willingness-to-pay-health
title: Willingness to Pay in Health Economics
domain: health-and-human-development
course: health-economics
prerequisites:
- id: cost-effectiveness-analysis
  type: hard
- id: cost-benefit-analysis-health
  type: soft
builds-toward: []
tags:
- WTP
- threshold
- contingent-valuation
- discrete-choice
- value-of-health
stage: advanced
status: validated
---

# Willingness to Pay in Health Economics

## Core Idea
Willingness to pay (WTP) in health economics refers to the maximum amount an individual or society would pay for a unit of health improvement (typically a QALY). At the individual level, WTP is elicited through stated preference methods (contingent valuation surveys, discrete choice experiments) to value specific health states or interventions. At the societal level, the WTP threshold is the cost-effectiveness benchmark that determines which interventions are funded — interventions with ICERs below the threshold are considered good value for money. The threshold is sometimes derived empirically (from observed past decisions, displaced spending analysis) or set normatively (reflecting what society should be willing to pay). The appropriate level of the WTP threshold is one of the most consequential and debated parameters in health economics — it determines the boundary between funded and unfunded healthcare.

## Questions

```yaml
- question: "Country A sets its cost-effectiveness threshold at $50,000/QALY. Country B, with five times the GDP per capita, sets its threshold at $150,000/QALY. Is this difference justified?"
  type: multiple-choice
  options:
    - "No — a QALY has the same intrinsic value everywhere, so the threshold should be universal"
    - "Yes — the threshold reflects the opportunity cost of healthcare spending, which depends on the country's wealth and health budget. A richer country can afford to fund less cost-effective interventions because its marginal spending displaces less valuable care"
    - "The threshold should equal GDP per capita in all countries"
    - "Thresholds are arbitrary and should be abolished"
  answer: 1
  explanation: "The threshold represents the opportunity cost — the health forgone by other patients when resources are allocated to the new intervention. In a wealthier country with a larger health budget, the next best use of funds may already be quite effective (high opportunity cost), while in a poorer country, there may be highly cost-effective interventions still unfunded. The threshold should ideally reflect the marginal cost-effectiveness of current spending — the health gained by the last intervention currently funded. This varies by country wealth and health system efficiency."

- question: "A contingent valuation survey asks people: 'What is the maximum you would pay per month for a treatment that reduces your risk of a heart attack by 50%?' The average response is $200/month. This estimate reliably reflects the true value people place on heart attack prevention."
  type: true-false
  answer: false
  explanation: "Contingent valuation (CV) is subject to well-documented biases: hypothetical bias (people state higher WTP than they would actually pay), starting-point bias (anchoring to initial suggested amounts), scope insensitivity (WTP does not scale proportionally with the magnitude of benefit), and strategic bias (overstating WTP to influence policy). CV estimates should be interpreted cautiously and validated against revealed preferences where possible. Discrete choice experiments, which ask respondents to choose between defined alternatives rather than state a dollar amount, partially mitigate some of these biases."

- question: "Explain why setting the WTP threshold too high wastes resources and setting it too low denies patients beneficial care."
  type: short-answer
  answer: "A threshold that is too high approves interventions whose cost per QALY exceeds the health that could be produced if the same money were spent on other patients (opportunity cost exceeds benefit). This displaces more cost-effective care, reducing total population health. A threshold that is too low rejects interventions that produce genuine health benefits at a cost below the opportunity cost of current spending — denying patients access to care that would improve their health without harming others. The optimal threshold equals the marginal cost-effectiveness of current spending: the ICER of the least cost-effective intervention currently funded."
  explanation: "In practice, thresholds are imprecise. The UK's £20,000-30,000/QALY range was originally based on precedent and expert judgment. Recent research (Claxton et al., 2015) estimated the actual opportunity cost in the NHS at approximately £13,000/QALY — suggesting the threshold may be too high, and some currently funded interventions are displacing more cost-effective care. This finding illustrates the real-world stakes of threshold-setting: it determines who gets treated and who does not."
```

## Explainer

Every time a health system funds an intervention, it implicitly or explicitly decides how much a unit of health is worth. A system that approves a drug costing $200,000 per QALY is saying "we are willing to pay $200,000 for one year of perfect health." A system that rejects it is saying "we are not." The **willingness-to-pay threshold** makes this judgment explicit, transforming a vague value statement into a decision rule.

At the **individual level**, WTP for health improvements can be elicited through surveys. **Contingent valuation** asks directly: "How much would you pay for X?" **Discrete choice experiments** present pairs of alternatives with different attributes (cost, effectiveness, side effects, convenience) and ask which they prefer, inferring WTP from the pattern of choices. These methods are used to value health states, inform benefit-package design, and calibrate societal thresholds. However, stated preferences are prone to biases — people say they would pay more than they actually would, and their responses are sensitive to framing, question order, and anchoring.

At the **societal level**, the WTP threshold determines the boundary of the benefits package. The WHO previously suggested 1-3 times GDP per capita as a threshold, but this approach has been criticized as too permissive — many countries cannot afford to fund all interventions below 3× GDP per capita. More sophisticated approaches estimate the **opportunity cost** of health spending: the health that would be gained if the money were spent on the next-best alternative. If funding a new cancer drug at $150,000/QALY means withdrawing resources from a prevention program that produces QALYs at $15,000 each, the net effect is a loss of population health. The threshold should equal the cost-effectiveness of the marginal intervention — the last thing currently funded.

The empirical evidence suggests many countries' thresholds are too high relative to their opportunity costs. Claxton and colleagues estimated the marginal productivity of NHS spending at approximately £13,000/QALY — well below the NICE threshold of £20,000-30,000. This implies that some interventions currently funded by NICE are displacing more productive spending elsewhere in the NHS, reducing total population health. Getting the threshold right is not an academic exercise — it determines how hundreds of billions of dollars in health spending are allocated, and small changes affect millions of patients' access to care.
