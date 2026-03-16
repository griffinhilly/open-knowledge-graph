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

## Explainer

You already know from your study of item difficulty and discrimination that classical test theory (CTT) characterizes each item by two numbers: its **p-value** (the proportion of examinees who answered correctly) and its **point-biserial correlation** (how strongly getting the item right correlates with total score). These statistics are intuitive and easy to compute, which is why CTT has dominated practical test development for a century. But there is a deep problem built into both numbers: they describe the item and the sample jointly, not the item alone. An item that 80% of honors students answer correctly might be answered correctly by only 30% of a remedial class — the "difficulty" of the item appears to change, but the item itself has not changed at all.

This **sample-dependence** is the central limitation that IRT addresses. From your prerequisite study of IRT assumptions, you know that IRT models the probability of a correct response as a mathematical function of two things: the examinee's ability (θ) and the item's parameters. The Rasch (1PL) model uses a single parameter — item difficulty (b) — defined as the ability level at which an examinee has a 50% chance of answering correctly. The 2PL adds a discrimination parameter (a), and the 3PL adds a guessing parameter (c). The critical feature is that once these item parameters are estimated from a calibration sample, they are theoretically **invariant across populations**: the difficulty parameter of a well-fitting item should be the same whether estimated from a high-ability group or a low-ability group (though the estimated values may differ more in practice due to estimation error).

The practical consequence is that CTT and IRT give you different lenses on the same data. CTT's p-value and point-biserial are quick diagnostics for flagging problems: an item with p=0.95 is probably too easy; a point-biserial below 0.10 suggests the item discriminates poorly or is flawed. IRT's **item characteristic curve (ICC)** shows the full relationship between ability and probability of correct response across the entire ability spectrum. An item that is highly discriminating will produce a steep S-shaped ICC; a poorly discriminating item produces a flat one. The ICC reveals something p-values cannot: whether an item performs differently at different ability levels. An item might have a satisfactory average discrimination while actually functioning well only for mid-range examinees.

The choice between methods is not merely technical — it reflects what you need from your analysis. CTT works well when you are analyzing a test administered to a reasonably similar group each time, when computational resources are limited, or when items do not form a clean unidimensional scale. IRT is essential when you need to **equate** scores across different test forms (essential for standardized licensure exams administered repeatedly), when you are building **item banks** and need to know an item's properties independently of which other items it appeared with, or when you need precise measurement across a wide range of abilities. IRT's requirement of unidimensionality — that a single underlying trait drives all item responses — is a strong assumption that must be tested, and violating it produces biased parameter estimates.

A useful synthesis: CTT item statistics are roughly interpretable as summaries of what IRT estimates more precisely. The p-value approximates the difficulty parameter's implied percent-correct for the tested population; the point-biserial approximates discrimination. But CTT conflates what is in the item with what is in the sample, while IRT attempts to surgically separate them. Skilled psychometricians often use both: CTT for fast initial screening and IRT for final calibration and equating. Understanding both traditions lets you read legacy test development documentation (typically CTT-based) and modern adaptive testing frameworks (typically IRT-based) with equal fluency.

