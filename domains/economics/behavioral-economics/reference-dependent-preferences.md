---
id: reference-dependent-preferences
title: Reference-Dependent Preferences
domain: economics
course: behavioral-economics
prerequisites:
- id: prospect-theory
  type: hard
- id: loss-aversion
  type: hard
tags:
- reference-points
- expectations
- Koszegi-Rabin
- gain-loss-utility
stage: expert
status: validated
---

# Reference-Dependent Preferences

## Core Idea
Reference-dependent preferences formalize the insight from prospect theory that people evaluate outcomes as gains or losses relative to a reference point rather than as absolute levels. Koszegi and Rabin (2006) developed the most influential model, proposing that utility has two components: consumption utility (standard utility from the outcome itself) and gain-loss utility (additional utility or disutility depending on whether the outcome exceeds or falls short of a reference point, typically rational expectations). This model generates predictions about labor supply (taxi drivers work less on high-wage days), consumer behavior (demand patterns respond to reference prices), and risk attitudes (which depend on the stochastic properties of expectations). Reference-dependence is now a core building block of behavioral economic theory, extending prospect theory from static laboratory gambles to dynamic economic settings.

## Questions

```yaml
- question: "In the Koszegi-Rabin model, the reference point is determined by..."
  type: multiple-choice
  options:
    - "An arbitrary anchor provided by the experimenter"
    - "The person's rational expectations about outcomes, formed before the decision"
    - "The highest outcome the person has ever experienced"
    - "A fixed biological set point"
  answer: 1
  explanation: "Koszegi and Rabin's key innovation was to endogenize the reference point as rational expectations. Rather than assuming the reference point is the status quo or some arbitrary value, their model proposes that people form expectations about what they will receive (based on available information) and then evaluate actual outcomes relative to those expectations. This makes the reference point endogenous to the economic environment — it responds to information, prices, and probabilities — while preserving the gain-loss evaluation framework from prospect theory."

- question: "Reference-dependent preferences predict that consumers will be more price-sensitive when a price increase exceeds their expectations than when the same high price has always been the norm."
  type: true-false
  answer: true
  explanation: "If the reference point is expectations, a consumer who expects to pay $5 and encounters a $7 price experiences a $2 loss relative to the reference point — activating loss aversion and reducing demand more than the price change alone would predict. A consumer who always expected $7 has no loss relative to expectations and responds based on standard price sensitivity alone. This asymmetry between expected and unexpected price changes is a distinctive prediction of reference-dependent models and has been confirmed in field data."

- question: "How does reference-dependence explain the finding that New York City taxi drivers work fewer hours on high-wage days?"
  type: short-answer
  answer: "Camerer et al. found that taxi drivers set a daily income target (reference point) and stop working once they reach it. On high-fare days (rainy, busy), they reach the target quickly and quit early; on low-fare days, they work longer to approach the target. This is the opposite of the standard labor supply prediction (work more when wages are high) but consistent with reference-dependent preferences: once income exceeds the reference point, additional earnings provide diminishing gain-loss utility, reducing the incentive to continue."
  explanation: "This finding has been debated — Farber argues that measurement issues and selection effects complicate the original analysis — but the theoretical point stands: reference-dependent preferences can produce 'target earning' behavior where labor supply slopes negatively with the daily wage. The Koszegi-Rabin model would predict this if the reference point is a daily income expectation, because surpassing the expectation provides diminishing marginal gain-loss utility while falling short of it produces steep marginal loss."
```

## Explainer

Prospect theory demonstrated that people evaluate outcomes relative to reference points, but it left a critical question unanswered: what determines the reference point? In the original laboratory experiments, the reference point was usually the status quo or an experimentally controlled endowment. But in dynamic economic settings — labor supply, consumption, investment — the reference point is not fixed or obvious. Reference-dependent preference models, particularly Koszegi and Rabin's, address this gap by providing a systematic theory of reference point formation.

Koszegi and Rabin proposed that the reference point is determined by the person's rational expectations about outcomes. If you expect to earn $200 today, earning $250 generates gain-loss utility from the $50 gain relative to expectations, while earning $150 generates loss-related disutility from the $50 shortfall. The total utility has two components: standard consumption utility (you enjoy spending $250 more than $150) and gain-loss utility (the pleasant surprise of exceeding expectations or the painful disappointment of falling short). Loss aversion means that the disutility of falling $50 short exceeds the utility of exceeding expectations by $50.

This seemingly simple modification has rich implications. In consumer demand, it predicts that price increases from an expected level reduce demand more than equivalent price decreases increase demand — an asymmetric demand response around the reference price. This has been confirmed in field data: consumers respond more strongly to price increases than to price decreases of the same magnitude, controlling for the price level. In labor markets, it predicts target-earning behavior when workers have daily income reference points — they work fewer hours when wages are high because they reach their target faster, and more hours when wages are low because reaching the target requires more effort.

The expectations-based reference point also explains patterns in risk attitudes. If you expect a certain outcome, any risk relative to that expectation involves potential losses as well as potential gains — and loss aversion makes the downside loom larger. This produces risk aversion around the expected outcome. But if you already expect a risky outcome (a gamble), your reference point incorporates the distribution of possible outcomes, and loss aversion is partially pre-digested into expectations. This means that risk attitudes depend not just on the gamble itself but on whether the risk was anticipated — a prediction that standard expected utility cannot make.

The broader significance of reference-dependent preferences is that they bring prospect theory into general equilibrium analysis. Original prospect theory was a theory of isolated gambles in laboratories. Koszegi and Rabin's framework makes it applicable to any economic setting where agents form expectations — which is essentially every setting. Labor supply, consumption-savings, portfolio choice, bargaining, and industrial organization can all be analyzed with reference-dependent preferences, generating predictions that differ from standard models in specific, testable ways. This has made reference-dependence a working model in applied microeconomics, not just a behavioral psychology curiosity.
