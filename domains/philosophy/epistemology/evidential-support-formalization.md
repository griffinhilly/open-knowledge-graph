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
stage: formal-systems
status: draft
---

# Evidential Support and Confirmation Formalization

## Core Idea
Evidential support can be formalized in Bayesian terms: evidence e supports hypothesis h if P(h|e) > P(h), i.e., learning e raises the probability of h. The degree of support is captured by the likelihood ratio P(e|h) / P(e|¬h): how much more probable the evidence is given h versus not-h. This framework unifies intuitions about confirmation, explains why evidence can be misleading (when prior probabilities are skewed), and reveals logical relationships between different kinds of supporting evidence.

## Questions

```yaml
- question: "A disease affects 1 in 1,000 people. A diagnostic test has a likelihood ratio of 50 (it is 50× more likely to return positive if the patient has the disease). You test positive. What is approximately your posterior probability of having the disease?"
  type: multiple-choice
  options:
    - "About 98% — a likelihood ratio of 50 is very strong evidence"
    - "About 50% — the likelihood ratio balances the prior uncertainty"
    - "About 5% — the extreme rarity of the disease still dominates after updating"
    - "Cannot be determined without knowing the false positive rate exactly"
  answer: 2
  explanation: "Using Bayes' theorem: P(disease|+) ≈ (0.001 × 50) / (0.001 × 50 + 0.999 × 1) ≈ 0.05 / 1.05 ≈ 4.8%. A likelihood ratio of 50 is genuinely strong evidence — it moves the probability from 0.1% to about 5%. But the prior was so extreme (1 in 1,000) that even strong evidence leaves the posterior well below 50%. This illustrates why strong evidence is not sufficient for confident belief when the prior is extreme. Option A is the classic base-rate neglect error."

- question: "What does a likelihood ratio P(e|h) / P(e|¬h) close to 1 tell you about the evidence e?"
  type: multiple-choice
  options:
    - "The evidence strongly confirms h, because both h and ¬h predict it equally"
    - "The evidence is equally probable under h and under ¬h — it provides little discriminating force"
    - "The posterior probability of h equals the prior probability of h after seeing e"
    - "Both B and C — a likelihood ratio of 1 means the evidence leaves credences unchanged"
  answer: 3
  explanation: "Options B and C are both correct, making D the right answer. A likelihood ratio of exactly 1 means P(e|h) = P(e|¬h) — the evidence is no more expected under h than under its negation. By Bayes' theorem, this means the posterior equals the prior: the evidence provides zero discriminating force and leaves belief unchanged. This is why the likelihood ratio is the right measure of evidential strength — it isolates whether the evidence preferentially supports h over ¬h, independent of prior probabilities."

- question: "Two investigators studying the same hypothesis start with very different prior probabilities but observe the same evidence. They will assign the same likelihood ratio to that evidence."
  type: true-false
  answer: true
  explanation: "The likelihood ratio P(e|h) / P(e|¬h) depends only on the hypothesis h and the evidence e — specifically, on how probable each makes the evidence. It does not depend on the investigators' prior probabilities for h. This is what makes the likelihood ratio an 'objective' measure of evidential strength: two people can rationally disagree about how probable h is while fully agreeing on how much this particular evidence supports h over ¬h."

- question: "If evidence e confirms hypothesis h — that is, P(h|e) > P(h) — then observing e is sufficient justification to believe h."
  type: true-false
  answer: false
  explanation: "Confirmation (raising probability) is necessary but not sufficient for justified belief. If P(h) = 0.001 and evidence with a likelihood ratio of 10 raises P(h|e) to about 1%, the evidence genuinely confirms h but the posterior is still far too low to justify belief. Justification requires the posterior to exceed some threshold (context-dependent, but typically well above 50% for action). Strong evidence that confirms h can still leave a rational agent doubting h when the prior is sufficiently low."

- question: "Two confirming observations e1 and e2 each have a likelihood ratio of 20. Explain under what condition their combined likelihood ratio equals 400, and why this condition often fails in practice."
  type: short-answer
  answer: "The combined likelihood ratio equals LR1 × LR2 = 400 only when e1 and e2 are conditionally independent given h — that is, knowing e1 tells you nothing about e2 beyond what h already tells you, and similarly for ¬h. In that case, P(e1,e2|h) = P(e1|h)P(e2|h), and the ratios multiply. This often fails in practice because many pieces of evidence are correlated: two eyewitness reports of the same event share a common cause (the actual event) and may also share common biases, so they are not independent given h. Treating correlated evidence as independent inflates the combined likelihood ratio and overstates how much the evidence supports h."
  explanation: "This is one of the main ways Bayesian epistemology reveals hidden assumptions in ordinary reasoning. Informal arguments that 'we have lots of evidence for h' can be undermined if all that evidence traces to the same underlying source. The Bayesian framework forces explicitness about dependence structure, preventing double-counting of correlated observations."
```

## Explainer

From conditionalization and Bayesian updating, you know the core mechanics: you start with a prior probability P(h), observe evidence e, and update to a posterior P(h|e) using Bayes' theorem: P(h|e) = P(e|h) × P(h) / P(e). What evidential support formalization adds is a principled way to measure *how much* evidence matters — not just "did my belief change?" but "how strongly does this evidence favor this hypothesis over its alternatives?"

The basic confirmation relation is simple: **e confirms h** if and only if P(h|e) > P(h). Observing e raises your credence in h, so e is evidence for h. Conversely, e *disconfirms* h if P(h|e) < P(h). This fits the intuitive notion that a positive test result for a disease is evidence you have it, while a negative result is evidence against. The Bayesian framework turns this intuition into a precise inequality and connects it directly to the updating rule you already know.

The richer measure is the **likelihood ratio**: P(e|h) / P(e|¬h). This ratio asks how much more probable the evidence is under h than under its negation. A likelihood ratio of 10 means the evidence is ten times more expected if h is true than if h is false — strong support. A ratio near 1 means the evidence is roughly as probable either way — weak or no support. The power of this measure is that it isolates the *discriminating force* of the evidence, independent of your priors. Two investigators with different prior beliefs about h will update differently from the same evidence, but they will agree on the likelihood ratio — it is an objective feature of the evidence's relationship to the competing hypotheses.

This framework also illuminates when evidence can be **misleading** — the case where your posterior is high but you are nonetheless wrong. Suppose h is very improbable a priori (say, P(h) = 0.001), and you observe e with a likelihood ratio of 100. A ratio of 100 is substantial — but starting from 0.001, even multiplying by 100 leaves P(h|e) well below 50%. The evidence genuinely supports h (it moved the probability up), but the posterior is still low because the prior was so extreme. This shows why strong evidence is not sufficient for justified belief if the hypothesis was implausible to begin with. Misleading evidence can also occur in the other direction: a single confirming observation against a flood of disconfirming prior evidence may not produce a credence worth acting on.

A key application is understanding how **multiple pieces of evidence combine**. If observations are conditionally independent given h (knowing one tells you nothing about the others, beyond what h already tells you), their likelihood ratios multiply. Observing both e1 and e2, each with a likelihood ratio of 10, gives a combined ratio of 100. But if e1 and e2 are not independent — if they both measure the same underlying thing — their combined force is less than their product. Formalizing evidential support forces you to be explicit about these dependence assumptions, which are often hidden in informal reasoning. This is one of the ways Bayesian epistemology makes implicit inferential commitments visible and assessable.
