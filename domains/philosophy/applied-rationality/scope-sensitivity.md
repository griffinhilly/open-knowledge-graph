---
id: scope-sensitivity
title: "Scope Sensitivity"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: debiasing-techniques
    type: hard
  - id: expected-value
    type: soft
builds-toward:
  - expected-value-decision-making
  - effective-altruism-and-scope
tags: ["debiasing", "scope", "scale", "quantitative-reasoning", "altruism"]
stage: advanced
status: validated
---

## Core Idea

Scope insensitivity is the tendency to respond with similar emotional intensity to problems of vastly different scale. In a famous study, people were willing to pay roughly the same amount to save 2,000 birds, 20,000 birds, or 200,000 birds from oil spills. The emotional response is driven by the prototype (one oil-soaked bird) rather than by the quantity. Scope sensitivity training means learning to multiply — to consciously scale your concern, effort, and resources in proportion to the actual magnitude of the problem. This is foundational to effective altruism and rational prioritization: if intervention A saves 10 lives and intervention B saves 10,000, the second is 1,000 times more valuable, even if both evoke similar emotional concern.

## How It's Best Learned

When evaluating a problem, explicitly estimate its scale before forming an emotional response. Practice with charitable giving: compare the cost-effectiveness of different interventions using metrics like QALYs or lives saved per dollar. Notice when your emotional reaction does not match the quantitative scale.

## Common Misconceptions

- Scope sensitivity is not about suppressing emotions — it is about ensuring that the scale of your response matches the scale of the problem.
- Being scope-sensitive does not mean only caring about the largest problems — it means being proportionate in your concern across problems of different sizes.

## Explainer

From debiasing techniques, you know that specific procedural countermeasures are needed to correct cognitive biases, and that awareness alone is insufficient. Scope insensitivity is one of the most consequential biases to address, because it distorts decisions about resource allocation, charitable giving, risk assessment, and policy -- anywhere the magnitude of a problem should influence the magnitude of the response.

The canonical demonstration comes from a study on willingness to pay for environmental protection. Researchers asked three groups how much they would pay to save migratory birds from drowning in oil ponds: 2,000 birds, 20,000 birds, or 200,000 birds. Willingness to pay was roughly the same across all three conditions -- about $80. A 100x difference in the scale of the problem produced almost no difference in the response. The explanation is that people's emotional reaction is driven by a **prototype** -- a vivid mental image of a single oil-soaked bird -- rather than by the quantity. The prototype is the same whether 2,000 or 200,000 birds are affected, so the emotional response (and the willingness to act) is the same. The numbers are not processed as magnitudes; they are processed as interchangeable labels on the same emotional experience.

Scope sensitivity training means learning to **multiply** -- to consciously scale your concern, effort, and resources in proportion to the actual magnitude of the problem. This does not mean suppressing emotions; it means ensuring that emotional motivation is calibrated to quantitative reality. If intervention A saves 10 lives per $10,000 and intervention B saves 10,000 lives per $10,000, intervention B is 1,000 times more valuable. Scope sensitivity demands that this 1,000x difference actually influence your behavior -- not just your intellectual acknowledgment. The practical technique is to estimate the scale of a problem explicitly before forming an emotional response, and then to check whether your response is proportionate.

Scope insensitivity is foundational to effective altruism because it is the primary mechanism by which donors systematically misallocate resources. Charitable giving is dominated by emotional resonance -- identifiable victims, compelling narratives, personal connections -- none of which scale with the magnitude of the problem. A donor who gives $10,000 to a local cause that produces modest benefits and $0 to a global health intervention that could save two lives is not failing at generosity; they are failing at scope. The same emotional impulse that makes them generous in the first place would, if calibrated to magnitude, direct their resources where the impact is orders of magnitude larger. This is what makes scope sensitivity not just a cognitive curiosity but a moral imperative for anyone who wants their concern for others to actually translate into proportionate action.

## Questions

```yaml
- question: "In a famous study, people were asked how much they would pay to fund cleanup of an oil spill affecting either 2,000, 20,000, or 200,000 birds. Willingness to pay barely changed across conditions. What best explains this finding?"
  type: multiple-choice
  options:
    - "Respondents rationally concluded that the marginal cost of saving additional birds was too high to justify more spending"
    - "Their willingness to pay was driven by a vivid image of a single oil-soaked bird rather than by the actual number of birds affected"
    - "Respondents lacked reliable information about bird population sizes and thus couldn't calibrate their responses"
    - "The monetary value of wildlife conservation is inherently fixed and does not scale with population size"
  answer: 1
  explanation: "This is the canonical demonstration of scope insensitivity. The emotional response is anchored to the prototype — a mental image of one suffering bird — not to the quantity. A 100x difference in scale produced almost no difference in willingness to pay. This reveals that intuitive concern responds to the identifiable victim or vivid prototype, not to numbers. Options A and C rationalize the finding rather than explaining the underlying cognitive mechanism."

- question: "From the standpoint of scope sensitivity, which approach to charitable giving is most rational?"
  type: multiple-choice
  options:
    - "Donating to causes you feel most emotionally connected to, since personal motivation improves follow-through and long-term commitment"
    - "Distributing donations equally across many causes to hedge against uncertainty about which interventions work"
    - "Comparing interventions by cost-effectiveness metrics such as lives saved per dollar and allocating resources accordingly"
    - "Prioritizing causes where your social network is already engaged, since collective action multiplies individual impact"
  answer: 2
  explanation: "Scope sensitivity means calibrating the scale of your response to the scale of the problem. If intervention A saves 10 lives per $1,000 and intervention B saves 10,000 lives per $1,000, the second is 1,000 times more valuable. Cost-effectiveness metrics (QALYs, lives saved per dollar) operationalize this proportionality. Options A and D anchor to emotional and social cues rather than magnitude; option B ignores effectiveness differences entirely."

- question: "Scope insensitivity is a problem of not caring — people who exhibit it simply don't value the welfare of birds or other beings."
  type: true-false
  answer: false
  explanation: "False. Scope insensitivity is not a lack of caring — people who show it may care intensely. The problem is that their level of concern fails to scale proportionally with the actual magnitude of the problem. Someone can feel genuine distress about 2,000 birds and essentially the same distress about 200,000 birds, while sincerely caring about both. The cognitive failure is in the scaling, not in the caring."

- question: "Correcting for scope insensitivity means learning to scale your concern, effort, and resources in proportion to the actual magnitude of the problem — not eliminating emotional responses."
  type: true-false
  answer: true
  explanation: "True. This is the explicit framing in the Common Misconceptions: scope sensitivity training is not about suppressing emotions. The goal is to ensure that the scale of your response matches the scale of the problem. Emotions remain useful as motivators; the correction is to multiply them by the numbers rather than let the numbers be irrelevant to the emotional response."

- question: "Why does scope insensitivity pose a particularly serious problem for effective altruism, rather than just being a general cognitive quirk?"
  type: short-answer
  answer: "Effective altruism explicitly aims to maximize the good done per unit of resource by comparing interventions across scale. Scope insensitivity directly undermines this: if donors give the same amount to save 10 lives as to save 10,000, the massive differences in cost-effectiveness that effective altruism relies on become invisible to intuitive decision-making. The cognitive bias collapses exactly the distinctions that effective prioritization depends on."
  explanation: "Most decisions affected by scope insensitivity involve small practical stakes. But in philanthropy, the differences in scale between interventions can be orders of magnitude — deworming programs vs. feel-good local projects, for example. When someone's emotional response doesn't scale with those orders of magnitude, they systematically underallocate to the most impactful interventions and overallocate to emotionally salient but less effective ones."
```
