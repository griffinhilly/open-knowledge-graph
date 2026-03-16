---
id: guessing-pseudo-guessing-irt-models
title: The Guessing Parameter and Three-Parameter IRT Models
domain: psychology
course: psychometrics
prerequisites:
- id: three-parameter-logistic-model
  type: hard
- id: item-information-function-test-precision
  type: soft
builds-toward:
- differential-item-functioning-analysis
tags:
- 3pl-model
- guessing
- irt
- pseudo-guessing
stage: advanced
status: draft
---

# The Guessing Parameter and Three-Parameter IRT Models

## Core Idea
The three-parameter logistic model adds guessing parameter (c), representing probability of correct response when ability is very low. This asymptote captures lucky guesses on multiple-choice items and improves fit with substantial guessing. However, c is difficult to estimate reliably, often requiring informative priors. Empirical testing determines necessity.

## Explainer

From the two-parameter logistic (2PL) model, you know that every item's **item characteristic curve (ICC)** is fully described by discrimination (*a*) and difficulty (*b*): discrimination controls how steeply the curve rises around the inflection point, and difficulty controls where that inflection falls on the ability scale. The 2PL assumes that as ability approaches negative infinity, the probability of a correct response approaches zero. That assumption is reasonable for many item types — a free-response item, for instance, cannot be answered correctly by guessing. But multiple-choice items break that assumption. A four-option item gives even the least knowledgeable examinee a 25% chance of selecting the correct answer by random choice.

The **three-parameter logistic (3PL) model** introduces a lower asymptote parameter, typically denoted *c*, to capture this floor. The ICC never descends all the way to zero; instead, it levels off at *c* as ability decreases. A test developer designing a four-choice item might expect *c* ≈ 0.25, though in practice estimated values are often lower — around 0.10–0.20 — because low-ability examinees are not choosing randomly across all options. Distractor quality matters: well-constructed distractors attract systematic wrong responses, so low-ability examinees cluster below the floor rather than distributing uniformly. This is why the parameter is called **pseudo-guessing** rather than simply guessing: it represents the combined effect of random guessing and differential distractor attraction, not pure chance.

The practical consequence of ignoring guessing in a 2PL model is that difficulty estimates become inflated for multiple-choice items: the item looks harder than it is because the model tries to fit the lower plateau by pushing the inflection point upward. The 3PL corrects this by modeling the asymptote directly. In terms of test information, items with high *c* values contribute less information at low ability levels because the ICC's slope is shallower in that region — there is less signal distinguishing ability levels when everyone has a ~20% baseline chance of success.

The difficulty with the 3PL is estimation. The *c* parameter is weakly identified from the data alone — you need a very large sample and items where guessing is genuinely present for the likelihood surface to be sharp around *c*. In practice, researchers routinely place **informative priors** on *c* (commonly a beta distribution centered around the reciprocal of the number of options) to stabilize estimates. Without priors, *c* estimates are highly variable across samples and can produce ICC crossings and other pathologies. This is one reason many operational testing programs that use IRT favor the 3PL only for low-stakes, speeded, or highly multiple-choice contexts, and retain the 2PL or even Rasch (1PL) models elsewhere: the added complexity of the 3PL is only worth the estimation cost when guessing is a substantial, systematic feature of the data. Empirical model comparison — using fit statistics like M2 or RMSEA, or information criteria — is the proper way to decide whether the guessing parameter earns its place in a given application.
