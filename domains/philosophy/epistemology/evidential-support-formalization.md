---
id: evidential-support-formalization
title: Evidential Support and Confirmation Formalization
domain: philosophy
course: epistemology
prerequisites:
- id: conditionalization-and-bayesian-updating
  type: hard
- id: bayesian-confirmation-science
  type: soft
- id: first-order-logic-syntax
  type: soft
tags:
- evidence
- confirmation
- support
- hypothesis
stage: advanced
status: draft
---

# Evidential Support and Confirmation Formalization

## Core Idea
Evidential support can be formalized in Bayesian terms: evidence e supports hypothesis h if P(h|e) > P(h), i.e., learning e raises the probability of h. The degree of support is captured by the likelihood ratio P(e|h) / P(e|¬h): how much more probable the evidence is given h versus not-h. This framework unifies intuitions about confirmation, explains why evidence can be misleading (when prior probabilities are skewed), and reveals logical relationships between different kinds of supporting evidence.

## Explainer

From conditionalization and Bayesian updating, you know the core mechanics: you start with a prior probability P(h), observe evidence e, and update to a posterior P(h|e) using Bayes' theorem: P(h|e) = P(e|h) × P(h) / P(e). What evidential support formalization adds is a principled way to measure *how much* evidence matters — not just "did my belief change?" but "how strongly does this evidence favor this hypothesis over its alternatives?"

The basic confirmation relation is simple: **e confirms h** if and only if P(h|e) > P(h). Observing e raises your credence in h, so e is evidence for h. Conversely, e *disconfirms* h if P(h|e) < P(h). This fits the intuitive notion that a positive test result for a disease is evidence you have it, while a negative result is evidence against. The Bayesian framework turns this intuition into a precise inequality and connects it directly to the updating rule you already know.

The richer measure is the **likelihood ratio**: P(e|h) / P(e|¬h). This ratio asks how much more probable the evidence is under h than under its negation. A likelihood ratio of 10 means the evidence is ten times more expected if h is true than if h is false — strong support. A ratio near 1 means the evidence is roughly as probable either way — weak or no support. The power of this measure is that it isolates the *discriminating force* of the evidence, independent of your priors. Two investigators with different prior beliefs about h will update differently from the same evidence, but they will agree on the likelihood ratio — it is an objective feature of the evidence's relationship to the competing hypotheses.

This framework also illuminates when evidence can be **misleading** — the case where your posterior is high but you are nonetheless wrong. Suppose h is very improbable a priori (say, P(h) = 0.001), and you observe e with a likelihood ratio of 100. A ratio of 100 is substantial — but starting from 0.001, even multiplying by 100 leaves P(h|e) well below 50%. The evidence genuinely supports h (it moved the probability up), but the posterior is still low because the prior was so extreme. This shows why strong evidence is not sufficient for justified belief if the hypothesis was implausible to begin with. Misleading evidence can also occur in the other direction: a single confirming observation against a flood of disconfirming prior evidence may not produce a credence worth acting on.

A key application is understanding how **multiple pieces of evidence combine**. If observations are conditionally independent given h (knowing one tells you nothing about the others, beyond what h already tells you), their likelihood ratios multiply. Observing both e1 and e2, each with a likelihood ratio of 10, gives a combined ratio of 100. But if e1 and e2 are not independent — if they both measure the same underlying thing — their combined force is less than their product. Formalizing evidential support forces you to be explicit about these dependence assumptions, which are often hidden in informal reasoning. This is one of the ways Bayesian epistemology makes implicit inferential commitments visible and assessable.
