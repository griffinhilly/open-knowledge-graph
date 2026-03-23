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
stage: expert
status: validated
---

# The Guessing Parameter and Three-Parameter IRT Models

## Core Idea
The three-parameter logistic model adds guessing parameter (c), representing probability of correct response when ability is very low. This asymptote captures lucky guesses on multiple-choice items and improves fit with substantial guessing. However, c is difficult to estimate reliably, often requiring informative priors. Empirical testing determines necessity.

## Questions

```yaml
- question: "A test developer expects the guessing parameter c for a 4-choice item to be approximately 0.25, but the estimated value is 0.13. The most likely explanation is:"
  type: multiple-choice
  options:
    - "The item is too easy, so even low-ability examinees answer correctly without guessing"
    - "Low-ability examinees are attracted to specific distractors rather than choosing randomly across all options"
    - "The item has poor discrimination, which reduces the lower asymptote"
    - "The sample was too small to estimate c accurately, so it shrank toward zero"
  answer: 1
  explanation: "The 'pseudo' in pseudo-guessing reflects the fact that low-ability examinees do not choose uniformly at random. Well-constructed distractors attract systematic wrong responses — certain wrong answers look more plausible than others — so low-ability examinees cluster on specific incorrect options rather than spreading evenly. This means the empirical lower asymptote is typically 0.10–0.20 for 4-choice items, well below the 0.25 that pure random guessing would predict. Option A describes a different problem (low difficulty), and option C confuses discrimination with the asymptote."

- question: "A psychometrician fits a 2PL model to multiple-choice data from a test with substantial guessing. What systematic bias should they expect in difficulty (b) estimates?"
  type: multiple-choice
  options:
    - "Difficulty will be deflated because the model attributes lucky guesses to the item being easy"
    - "Difficulty will be inflated because the model pushes the ICC's inflection point upward to fit the lower plateau"
    - "Difficulty will be unaffected — the discrimination parameter absorbs guessing behavior"
    - "Difficulty estimates will be random, since guessing is random by definition"
  answer: 1
  explanation: "The 2PL assumes the ICC descends all the way to zero as ability decreases. When there is a genuine lower plateau from guessing, the model tries to fit this floor by shifting the inflection point (b) upward — making the item look harder than it really is. The 3PL corrects this by modeling the asymptote directly with c, freeing b to reflect true difficulty. Option C is wrong because discrimination controls the slope, not the floor; the 2PL has no mechanism to absorb a non-zero lower asymptote."

- question: "For a four-option multiple-choice item, the 3PL pseudo-guessing parameter c will typically be estimated at approximately 0.25 in real test data."
  type: true-false
  answer: false
  explanation: "This is a common intuition — 1 in 4 options suggests 25% chance guessing — but empirical c estimates are typically 0.10–0.20, substantially lower. Low-ability examinees are not choosing randomly; they are systematically drawn to plausible distractors. The 0.25 value applies only if choices are uniformly random, which real test-taking behavior is not. This is exactly why the parameter is called 'pseudo-guessing' rather than 'guessing.'"

- question: "The added complexity of the 3PL model over the 2PL is only justified when guessing is a substantial, systematic feature of the data, and this should be determined by empirical model comparison."
  type: true-false
  answer: true
  explanation: "The c parameter is weakly identified from data alone — it requires large samples and items where guessing genuinely occurs, and even then it is estimated with high variance, often requiring informative priors to stabilize. Using the 3PL when guessing is minimal or absent adds estimation instability without improving fit. Many operational testing programs use 2PL or Rasch models for most items, reserving the 3PL for clearly multiple-choice contexts with known guessing. Empirical comparison using indices like M2, RMSEA, or information criteria is the principled way to decide."

- question: "Why is the lower asymptote parameter in the 3PL model called 'pseudo-guessing' rather than simply 'guessing'?"
  type: short-answer
  answer: "Because the parameter captures the combined effect of random guessing and differential distractor attraction, not pure chance. Low-ability examinees do not choose uniformly at random — well-constructed distractors attract systematic wrong responses, so examinees cluster on specific incorrect options. The empirical lower asymptote is therefore lower than 1/k (where k is the number of options) would predict from pure random guessing. 'Pseudo-guessing' acknowledges that the lower asymptote reflects distractor quality and test-taking strategy as well as chance."
  explanation: "The distinction matters practically: if c simply equaled 1/k, test developers would have no reason to invest in distractor quality. The pseudo-guessing framing reveals that good distractors — ones that attract low-ability examinees for conceptual reasons — actually reduce c below the chance baseline, giving the test more information-discriminating power at low ability levels. It also means that c is partly a property of the items (distractor quality) and not just a universal constant for multiple-choice formats."
```

## Explainer

From the two-parameter logistic (2PL) model, you know that every item's **item characteristic curve (ICC)** is fully described by discrimination (*a*) and difficulty (*b*): discrimination controls how steeply the curve rises around the inflection point, and difficulty controls where that inflection falls on the ability scale. The 2PL assumes that as ability approaches negative infinity, the probability of a correct response approaches zero. That assumption is reasonable for many item types — a free-response item, for instance, cannot be answered correctly by guessing. But multiple-choice items break that assumption. A four-option item gives even the least knowledgeable examinee a 25% chance of selecting the correct answer by random choice.

The **three-parameter logistic (3PL) model** introduces a lower asymptote parameter, typically denoted *c*, to capture this floor. The ICC never descends all the way to zero; instead, it levels off at *c* as ability decreases. A test developer designing a four-choice item might expect *c* ≈ 0.25, though in practice estimated values are often lower — around 0.10–0.20 — because low-ability examinees are not choosing randomly across all options. Distractor quality matters: well-constructed distractors attract systematic wrong responses, so low-ability examinees cluster below the floor rather than distributing uniformly. This is why the parameter is called **pseudo-guessing** rather than simply guessing: it represents the combined effect of random guessing and differential distractor attraction, not pure chance.

The practical consequence of ignoring guessing in a 2PL model is that difficulty estimates become inflated for multiple-choice items: the item looks harder than it is because the model tries to fit the lower plateau by pushing the inflection point upward. The 3PL corrects this by modeling the asymptote directly. In terms of test information, items with high *c* values contribute less information at low ability levels because the ICC's slope is shallower in that region — there is less signal distinguishing ability levels when everyone has a ~20% baseline chance of success.

The difficulty with the 3PL is estimation. The *c* parameter is weakly identified from the data alone — you need a very large sample and items where guessing is genuinely present for the likelihood surface to be sharp around *c*. In practice, researchers routinely place **informative priors** on *c* (commonly a beta distribution centered around the reciprocal of the number of options) to stabilize estimates. Without priors, *c* estimates are highly variable across samples and can produce ICC crossings and other pathologies. This is one reason many operational testing programs that use IRT favor the 3PL only for low-stakes, speeded, or highly multiple-choice contexts, and retain the 2PL or even Rasch (1PL) models elsewhere: the added complexity of the 3PL is only worth the estimation cost when guessing is a substantial, systematic feature of the data. Empirical model comparison — using fit statistics like M2 or RMSEA, or information criteria — is the proper way to decide whether the guessing parameter earns its place in a given application.
