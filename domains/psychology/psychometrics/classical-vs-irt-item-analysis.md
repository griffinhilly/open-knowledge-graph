---
id: classical-vs-irt-item-analysis
title: Classical and IRT-Based Item Analysis Compared
domain: psychology
course: psychometrics
prerequisites:
- id: item-difficulty-discrimination
  type: hard
- id: item-response-theory-assumptions
  type: hard
builds-toward:
- multiple-choice-distractor-analysis
tags:
- item-analysis
- classical-test-theory
- irt
- comparison
stage: advanced
status: draft
---

# Classical and IRT-Based Item Analysis Compared

## Core Idea
Classical item analysis examines difficulty (p-value) and discrimination (point-biserial correlation) but these statistics depend on ability distribution and test length. IRT analysis yields ability-independent estimates modeling full response curves. Classical methods are simpler and don't require unidimensionality; IRT is more precise and informative but computationally demanding.

## Questions

```yaml
- question: "A test item has a p-value of 0.85 when administered to a sample of college graduates. The same item has a p-value of 0.52 when given to a sample of high school students. The best interpretation is:"
  type: multiple-choice
  options:
    - "The item was scored incorrectly for one of the groups"
    - "This demonstrates that p-value is a sample-dependent statistic, not a fixed property of the item"
    - "The item discriminates poorly because its difficulty appears to change across groups"
    - "The high school students received a flawed test administration"
  answer: 1
  explanation: "The p-value (proportion answering correctly) reflects both item properties and the ability distribution of the sample. A more able group will always produce a higher p-value on the same item — not because the item changed, but because CTT statistics conflate item and sample. This is the central limitation of classical test theory: you cannot determine whether a difference between groups reflects the item or the examinees. IRT addresses this by estimating item parameters that are theoretically invariant across populations."

- question: "A testing company needs to build an item bank and compare scores across different test forms administered to different cohorts each year. Which measurement approach is most appropriate?"
  type: multiple-choice
  options:
    - "Classical test theory, because p-values and point-biserials are simpler to compute and interpret"
    - "IRT, because item parameter estimates are theoretically invariant across populations, enabling score equating across different forms and cohorts"
    - "Classical test theory, because point-biserial correlations capture the same information as IRT discrimination parameters"
    - "Either approach works equally well for equating scores across test forms"
  answer: 1
  explanation: "Score equating — placing scores from different test forms on a common scale — requires that item properties remain constant across administrations. CTT item statistics are sample-dependent, so a p-value from one cohort cannot directly inform interpretation in another. IRT item parameters (difficulty b, discrimination a) are calibrated to be population-invariant, allowing the test developer to treat item properties as fixed. This is why virtually all large-scale standardized testing programs use IRT rather than CTT for equating."

- question: "A CTT p-value of 0.80 indicates that the item has moderate difficulty, regardless of which population is tested."
  type: true-false
  answer: false
  explanation: "A p-value of 0.80 means 80% of the tested sample answered correctly — but that number depends entirely on the ability level of the sample. The same item might have p = 0.95 with a highly able group and p = 0.40 with a struggling group. CTT p-values describe the item-in-context, not the item alone. The statement would be approximately true only if you always test the same population, which is rarely the case. This sample-dependence is the fundamental limitation CTT cannot escape."

- question: "IRT item parameter estimates allow test developers to place items from different test forms onto a common scale and compare their properties, even if those forms were administered to different groups."
  type: true-false
  answer: true
  explanation: "This is the key practical advantage of IRT over CTT. Because IRT item parameters are theoretically invariant across populations (conditional on good model fit), a difficulty parameter estimated from one cohort should apply to other cohorts. This parameter invariance makes score equating and item banking possible: a calibrated item difficulty can be used to predict performance in new groups without re-administering the item to a full new sample. Large-scale adaptive testing systems depend entirely on this property."

- question: "What is the fundamental limitation of classical test theory item statistics, and how does IRT address it?"
  type: short-answer
  answer: "CTT statistics (p-value, point-biserial) conflate item properties with sample properties — the same item appears easier or harder depending on who takes the test, making CTT statistics not portable across populations. IRT models the probability of a correct response as a function of both examinee ability and item-specific parameters estimated separately. Once calibrated, IRT item parameters are theoretically invariant across populations, separating what is in the item from what is in the examinees."
  explanation: "The sample-dependence of CTT is not merely a technical inconvenience — it means CTT statistics cannot be meaningfully compared across testing occasions unless the same population is tested each time. This makes CTT unsuitable for item banking, score equating, and computerized adaptive testing. IRT solves this by defining items in terms of the ability scale (theta) rather than the proportion correct in a particular sample, trading computational simplicity for measurement precision and portability across contexts."
```

## Explainer

You already know from your study of item difficulty and discrimination that classical test theory (CTT) characterizes each item by two numbers: its **p-value** (the proportion of examinees who answered correctly) and its **point-biserial correlation** (how strongly getting the item right correlates with total score). These statistics are intuitive and easy to compute, which is why CTT has dominated practical test development for a century. But there is a deep problem built into both numbers: they describe the item and the sample jointly, not the item alone. An item that 80% of honors students answer correctly might be answered correctly by only 30% of a remedial class — the "difficulty" of the item appears to change, but the item itself has not changed at all.

This **sample-dependence** is the central limitation that IRT addresses. From your prerequisite study of IRT assumptions, you know that IRT models the probability of a correct response as a mathematical function of two things: the examinee's ability (θ) and the item's parameters. The Rasch (1PL) model uses a single parameter — item difficulty (b) — defined as the ability level at which an examinee has a 50% chance of answering correctly. The 2PL adds a discrimination parameter (a), and the 3PL adds a guessing parameter (c). The critical feature is that once these item parameters are estimated from a calibration sample, they are theoretically **invariant across populations**: the difficulty parameter of a well-fitting item should be the same whether estimated from a high-ability group or a low-ability group (though the estimated values may differ more in practice due to estimation error).

The practical consequence is that CTT and IRT give you different lenses on the same data. CTT's p-value and point-biserial are quick diagnostics for flagging problems: an item with p=0.95 is probably too easy; a point-biserial below 0.10 suggests the item discriminates poorly or is flawed. IRT's **item characteristic curve (ICC)** shows the full relationship between ability and probability of correct response across the entire ability spectrum. An item that is highly discriminating will produce a steep S-shaped ICC; a poorly discriminating item produces a flat one. The ICC reveals something p-values cannot: whether an item performs differently at different ability levels. An item might have a satisfactory average discrimination while actually functioning well only for mid-range examinees.

The choice between methods is not merely technical — it reflects what you need from your analysis. CTT works well when you are analyzing a test administered to a reasonably similar group each time, when computational resources are limited, or when items do not form a clean unidimensional scale. IRT is essential when you need to **equate** scores across different test forms (essential for standardized licensure exams administered repeatedly), when you are building **item banks** and need to know an item's properties independently of which other items it appeared with, or when you need precise measurement across a wide range of abilities. IRT's requirement of unidimensionality — that a single underlying trait drives all item responses — is a strong assumption that must be tested, and violating it produces biased parameter estimates.

A useful synthesis: CTT item statistics are roughly interpretable as summaries of what IRT estimates more precisely. The p-value approximates the difficulty parameter's implied percent-correct for the tested population; the point-biserial approximates discrimination. But CTT conflates what is in the item with what is in the sample, while IRT attempts to surgically separate them. Skilled psychometricians often use both: CTT for fast initial screening and IRT for final calibration and equating. Understanding both traditions lets you read legacy test development documentation (typically CTT-based) and modern adaptive testing frameworks (typically IRT-based) with equal fluency.

