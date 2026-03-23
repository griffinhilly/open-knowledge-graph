---
id: conjoint-analysis-preferences
title: Conjoint Analysis and Stated Preference Methods
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: survey-design-advanced
  type: hard
- id: logistic-regression-binary-outcomes
  type: soft
- id: combinations
  type: soft
builds-toward:
- discrete-choice-modeling
- experimental-design-survey
tags:
- preferences
- survey
- experimental
- choice-modeling
stage: expert
status: draft
---

# Conjoint Analysis and Stated Preference Methods

## Core Idea
Conjoint analysis presents respondents with combinations of attributes (e.g., policy options with different costs and benefits) and asks them to rank, rate, or choose. Analysis decomposes choices into attribute importance and part-worth utilities. Conjoint experiments reveal trade-offs respondents make; for example, voters' trade-offs between security, liberty, and cost. Advantages include realism and efficiency; disadvantages include hypothetical bias and cognitive burden. Conjoint analysis is widely used in political science, marketing, and policy research.

## Questions

```yaml
- question: "Respondents are asked 'How important is environmental sustainability to your product choices?' 92% rate it 8 or higher out of 10. The same respondents complete a conjoint survey choosing between products with varying sustainability and price levels; the results show price matters three times as much as sustainability. What does this reveal?"
  type: multiple-choice
  options:
    - "The conjoint survey was poorly designed and should be discarded"
    - "Respondents lied in the direct rating because they wanted to appear virtuous"
    - "Direct ratings inflate the importance of every positive attribute; conjoint reveals actual trade-offs through forced choice"
    - "Sustainability genuinely matters more, but the conjoint profiles were priced unrealistically"
  answer: 2
  explanation: "This is the core problem conjoint analysis solves: when asked directly, people over-report how much they care about any positively-framed attribute. There is no cognitive pressure to make trade-offs, so every good thing gets rated highly. Conjoint forces respondents to choose between profiles where gaining more of one attribute requires accepting less of another — mirroring real decisions. The resulting part-worth utilities reveal relative importance through behavior, not self-report. Option B (lying) implies intent to deceive; the inflated ratings are typically a genuine measurement artifact of the direct-rating method, not conscious dishonesty."

- question: "In a conjoint experiment, each respondent makes a series of choices between pairs of policy profiles varying on cost, privacy protection, and response time. What is the statistical role of logistic regression in analyzing these responses?"
  type: multiple-choice
  options:
    - "It estimates what percentage of respondents prefer each attribute level in isolation"
    - "It models each binary choice as a function of the attribute levels of each profile and estimates how much each level increases the probability of being chosen"
    - "It determines the optimal number of attributes and levels for the conjoint design"
    - "It corrects for hypothetical bias by comparing stated choices to revealed preferences"
  answer: 1
  explanation: "Each choice observation is a binary outcome (chose profile A or profile B), and the attribute levels of each profile are the predictors. Logistic regression estimates coefficients — part-worth utilities — that indicate how much each attribute level increases the log-odds of a profile being chosen. This framing makes it straightforward to extend: interactions between attributes, heterogeneous preferences across subgroups, and predictions about hypothetical profiles not included in the original design can all be handled within the same framework. Option A describes a simpler frequency analysis, not regression."

- question: "Hypothetical bias is a genuine validity threat in conjoint analysis because respondents' stated choices in a survey context may systematically differ from how they would behave with real stakes."
  type: true-false
  answer: true
  explanation: "Hypothetical bias occurs when the absence of real consequences allows respondents to choose more idealistically than they would act in practice. A voter might choose a more expensive green-energy policy profile in a conjoint survey but not support it in an actual referendum where they would pay the tax. This threat is particularly acute for politically sensitive topics where social desirability pressure influences stated choices. Mitigation strategies include incentivizing truthful responses, validating survey conjoint results against real-world data where available, and being cautious about extrapolating from the hypothetical context."

- question: "The main methodological advantage of conjoint analysis over direct attribute ratings is that conjoint reduces cognitive burden on respondents by simplifying what they need to evaluate."
  type: true-false
  answer: false
  explanation: "Conjoint analysis often increases cognitive burden relative to direct ratings: respondents must evaluate bundles of multiple attributes simultaneously, and realistic profiles can be complex. The advantage of conjoint is not simplicity — it is validity. Forced choices between multi-attribute profiles mirror how real decisions are made, revealing the relative importance of attributes through actual trade-offs rather than self-reported importance. Direct ratings are simpler to complete but systematically over-estimate the importance of every positive attribute. Conjoint trades cognitive simplicity for measurement accuracy."

- question: "Why do conjoint experiments produce more valid estimates of attribute importance than directly asking respondents to rate how much they care about each attribute? Explain the core methodological logic."
  type: short-answer
  answer: "When asked directly, people over-report the importance of every positive attribute because there is no cost to saying everything matters. Real decisions require trade-offs — choosing more of one thing means accepting less of another. Conjoint analysis mimics this by presenting profiles where attributes are bundled: respondents can only get the high-privacy option if they also accept the high-cost option. By analyzing the pattern of choices across many such trade-off decisions, the method decomposes which attributes actually drove choices — revealing relative importance through revealed choice behavior rather than self-report. Part-worth utilities express how much preference shifts as each attribute changes, accounting for the trade-offs respondents were actually forced to make."
  explanation: "The logic mirrors the distinction between stated and revealed preferences in economics. Direct ratings produce stated importance, which is subject to social desirability and the absence of trade-off pressure. Conjoint produces a behavioral analog of revealed importance: what the respondent's choices imply about relative valuation. This is why conjoint is particularly valuable for politically or socially sensitive attributes — respondents cannot simply rate everything highly because the design forces them to give something up for every gain."
```

## Explainer

The fundamental challenge conjoint analysis solves is this: if you ask someone "how much do you value privacy?" they'll say "a lot." If you ask "how much do you value security?" they'll say "a lot." People consistently over-report their preference for every positive attribute when asked directly. Conjoint analysis sidesteps this by forcing respondents to make **trade-offs** — just as real decisions do. By presenting profiles that bundle attributes together (high privacy but high cost; low privacy but high security), the method reveals preferences through choices rather than stated importance ratings. The result is a much more realistic picture of what people actually value relative to each other.

The mechanics connect directly to your survey design background. In a typical conjoint experiment, you construct a factorial design: you have several attributes (say, cost, privacy protection, and response time for a technology policy), each with several levels. Respondents see pairs of profiles drawn from this design and choose which they prefer, or rate each profile. The key mathematical operation is decomposition — working backward from the pattern of choices to estimate each attribute's contribution to overall preference. These contributions are called **part-worth utilities**, and they tell you how much a one-unit change in each attribute moves the average respondent's evaluation. An attribute with high variance in part-worths matters a lot to respondents; one with low variance barely moves the needle.

The statistical engine behind modern conjoint analysis is often logistic regression or its extensions — exactly the model you've studied. Each choice observation is a binary outcome (chose profile A or profile B), and the attribute levels of each profile are the predictors. The coefficients estimate how much each attribute level increases the log-odds of being chosen. This framing makes it easy to extend: you can include interactions between attributes (does cost matter more at high security than low?), allow heterogeneous preferences across respondent subgroups, or model preference shares for hypothetical product configurations not actually tested.

The main threats to conjoint validity are hypothetical bias and cognitive burden. **Hypothetical bias** means stated choices in a survey context may not match real behavior — respondents might claim to care deeply about environmental impact in a product choice but not act on it when paying with their own money. **Cognitive burden** refers to the fact that realistic conjoint profiles can be complex, and respondents simplify by ignoring some attributes, especially late in a long survey. Both threats call for careful design: keep the number of attributes manageable, randomize attribute order, and when possible, validate against real-world data. When those conditions are met, conjoint analysis is among the most powerful tools for measuring latent preferences at scale.
