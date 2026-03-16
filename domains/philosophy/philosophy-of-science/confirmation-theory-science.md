---
id: confirmation-theory-science
title: Confirmation and Evidence
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: problem-of-induction-hume
  type: hard
- id: inductive-reasoning
  type: hard
- id: first-order-logic-syntax
  type: soft
builds-toward:
- bayesian-confirmation-science
- logical-positivism
tags:
- confirmation
- evidence
- support
- hypothesis
stage: advanced
status: draft
---

# Confirmation and Evidence

## Core Idea
Confirmation theory asks: When does evidence support or confirm a hypothesis? What makes one piece of evidence more confirmatory than another? Scientists intuitively assess evidence quality, but formalizing these judgments is philosophically challenging. Logical positivists sought deductive models, while modern approaches use probability theory and Bayesian inference to quantify how observation updates belief in hypotheses.

## Explainer

From your study of Hume's problem of induction, you know that no finite set of observations logically entails a universal generalization. No number of observed black ravens proves "all ravens are black." But science clearly works by gathering evidence, and some evidence genuinely supports hypotheses more than others. Confirmation theory is the attempt to make this intuition precise: to give a formal account of when and how much an observation supports a hypothesis. The difficulty is that our intuitions about evidential support, when pressed, generate genuine paradoxes.

The most famous is Carl Hempel's **ravens paradox**. Consider the hypothesis H: "All ravens are black." Observing a black raven seems to confirm it. Now consider the logically equivalent statement H': "All non-black things are non-ravens." A green apple is a non-black non-raven — it satisfies H'. Since H and H' say exactly the same thing (they are logically equivalent), and the green apple confirms H', it must also confirm H. But this seems absurd: you can sit in your living room collecting green apples and thereby (trivially) confirm the hypothesis about ravens. Hempel's response was to bite the bullet and accept that the apple does weakly confirm H — the counterintuitiveness reflects a pragmatic point about where we expect evidence to come from, not a logical error. But this answer is unsatisfying.

The Bayesian approach offers a cleaner resolution. **Bayesian confirmation** defines "E confirms H" as: the probability of H given E is higher than the prior probability of H. Formally, E confirms H if P(H|E) > P(H), which is equivalent to saying that E is more probable given H than given ¬H: P(E|H) > P(E|¬H). On this account, the green apple does confirm "all ravens are black" — but only infinitesimally. Before seeing the apple, almost all physical objects were non-black non-ravens; seeing one more doesn't update H much at all. Observing a black raven, by contrast, provides significantly more confirmation because ravens are much rarer than non-black things, making the raven observation more informative. The Bayesian framework explains why the apple confirmation feels trivial without denying it.

What the Bayesian approach reveals is that **confirmation is gradational and context-sensitive** — it is not a binary on/off relation but a matter of degree, governed by prior probabilities and the likelihood ratio P(E|H)/P(E|¬H). Evidence is more confirmatory when it was more likely to occur if the hypothesis is true and less likely if the hypothesis is false. This connects directly to your understanding of inductive reasoning: induction is not a single monolithic rule but a probabilistic updating process, and its strength depends on the specific evidential situation. The apparent paradoxes of confirmation largely dissolve once we shift from seeking a simple logical relation between statement and evidence to thinking in terms of probability updating — which is why Bayesian confirmation theory is the foundation of the more advanced framework you'll study next.
