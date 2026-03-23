---
id: extraordinary-claims-and-evidence-scaling
title: "Extraordinary Claims Require Extraordinary Evidence"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: bayesian-thinking-in-practice
    type: hard
  - id: absence-of-evidence
    type: soft
builds-toward:
  - likelihood-ratios-and-belief-updates
tags: ["bayesian", "evidence", "prior-probability", "sagan-standard"]
stage: advanced
status: validated
---

## Core Idea

Carl Sagan's maxim is a direct consequence of Bayes' theorem. A claim with a very low prior probability requires evidence with a very high likelihood ratio to shift the posterior to a meaningful level. If your prior for a claim is 1 in a million, even evidence that is 100 times more likely under the hypothesis than under the alternative only brings the posterior to about 1 in 10,000 — still very unlikely. This is not a bias against unusual claims; it is a mathematical consequence of how evidence and priors interact. The practical lesson: calibrate the strength of evidence needed to the extremity of the claim, and be suspicious when extraordinary claims are supported only by ordinary evidence.

## How It's Best Learned

Calculate concrete examples: if a friend claims to have seen a UFO (prior ~1 in 100,000 for an actual alien craft), how strong would the evidence need to be to make you believe? Work out the likelihood ratios. Compare with mundane claims ("it rained yesterday") where even modest evidence suffices because the prior is already high.

## Common Misconceptions

- This principle does not mean extraordinary claims should be dismissed without investigation — it means the bar for evidence is proportional to the claim's prior improbability.
- "Extraordinary" does not mean "surprising to me personally" — it means having a low prior probability given existing knowledge.

## Explainer

Carl Sagan's famous maxim -- "extraordinary claims require extraordinary evidence" -- sounds like a heuristic or a rhetorical device, but it is actually a direct mathematical consequence of Bayes' theorem. Understanding why makes the principle precise, quantitative, and much more useful than the slogan alone.

Bayesian updating works by multiplying your prior odds by the likelihood ratio of the evidence: posterior odds = prior odds x (P(evidence | claim true) / P(evidence | claim false)). A claim with a very low prior probability has very low prior odds. To bring the posterior to a meaningful level -- say, 50% -- the likelihood ratio must be large enough to compensate. If your prior for a claim is 1 in a million, you need evidence with a likelihood ratio of roughly a million to reach 50% posterior probability. Evidence with a likelihood ratio of 50 -- which would be decisive for a claim with moderate prior probability -- barely moves the needle, bringing a 1-in-a-million prior to only about 1 in 20,000. The math is unforgiving: the more extreme the prior, the stronger the evidence must be.

This is why the same type of evidence can be sufficient for one claim and woefully insufficient for another. If a friend tells you "it rained in Seattle yesterday," that testimony easily suffices -- the prior probability of rain in Seattle is high, and even modest evidence pushes you to near certainty. But if the same friend tells you they saw an alien spacecraft, their testimony carries the same likelihood ratio as before, yet it is applied to a prior of perhaps 1 in 100,000 for genuine alien craft. The result: the posterior barely budges. You would need evidence that is overwhelmingly more likely under "real alien craft" than under all mundane explanations combined -- multiple independent sensors, physical artifacts, convergent testimony from unconnected witnesses -- to produce the enormous likelihood ratio that the low prior demands.

Crucially, the Sagan standard does not mean extraordinary claims should be dismissed without investigation. It specifies how strong the evidence must be, not that evidence should not be sought. A scientist who refuses to investigate an extraordinary claim because "the prior is too low" has misunderstood Bayesian reasoning just as badly as one who accepts it on weak evidence. The principle is a calibration tool: it tells you what to expect from the evidence before you commit to a conclusion, and it warns you when the evidence presented is orders of magnitude weaker than what the claim requires. Applied honestly, it is a guard against both credulity (accepting extraordinary claims on ordinary evidence) and closed-mindedness (refusing to update even when extraordinary evidence is presented).

## Questions

```yaml
- question: "A skeptic's prior probability for claim X is 1 in 10,000. A witness reports seeing X, and this type of testimony is 50 times more likely when X is true than when X is false (likelihood ratio = 50). What is the approximate posterior probability that X is true after hearing the testimony?"
  type: multiple-choice
  options:
    - "About 50% — a likelihood ratio of 50 makes the claim roughly equally likely to be true or false"
    - "About 0.5% — the low prior still dominates; even strong evidence barely moves the needle on a 1-in-10,000 claim"
    - "About 99% — a likelihood ratio of 50 is overwhelming evidence that almost always confirms the claim"
    - "It cannot be determined without knowing the base rate of the type of testimony"
  answer: 1
  explanation: "Using Bayes' theorem with prior odds of 1:9,999 and a likelihood ratio of 50: posterior odds = 50 × (1/9,999) ≈ 1:200, or about 0.5%. This is the mathematical heart of the Sagan standard. Even a likelihood ratio of 50 — which would be decisive for a claim with a moderate prior — barely moves the needle on a 1-in-10,000 claim. To reach 50% posterior probability from a 1-in-10,000 prior requires a likelihood ratio of approximately 10,000. The strength of evidence needed scales with the prior's extremity."

- question: "You are evaluating two claims: (A) 'It rained in Seattle yesterday' (prior ~80%) and (B) 'A homeopathic remedy cured stage 4 cancer' (prior ~0.001%). A credible eyewitness report has the same likelihood ratio for both claims. For which claim does the eyewitness report more dramatically change your absolute probability estimate?"
  type: multiple-choice
  options:
    - "Claim B, because any movement from near-zero requires proportionally larger updating"
    - "Both claims update by the same factor — the likelihood ratio is the same, so the multiplicative update is identical regardless of prior"
    - "Claim A, because the absolute change in probability will be larger given the high prior"
    - "Neither — eyewitness testimony has the same absolute effect regardless of the prior"
  answer: 2
  explanation: "The likelihood ratio multiplies the prior odds equally for both claims. But the *absolute* change in probability is much larger for Claim A because starting from 80%, a 50× likelihood ratio can move you to near certainty — a large absolute shift. Starting from 0.001%, the same 50× ratio only gets you to about 0.05% — a tiny absolute change. Claim A changes dramatically in absolute terms; Claim B barely moves. This is why ordinary evidence is sufficient for Claim A but woefully insufficient for Claim B — the prior's extremity sets how much evidence is needed to produce any meaningful absolute change."

- question: "'Extraordinary claims require extraordinary evidence' means that claims with low prior probability should be rejected outright rather than investigated."
  type: true-false
  answer: false
  explanation: "This is the most common misreading of the Sagan standard. The principle specifies how strong the evidence must be — it does not say skip the investigation. A 1-in-a-million prior claim can still become credible with sufficiently strong evidence (a likelihood ratio of millions). The principle is about calibrating the evidence threshold, not dismissing claims. A scientist who refuses to investigate an extraordinary claim because 'the prior is too low' has misunderstood Bayesian reasoning just as badly as the one who accepts it on weak evidence."

- question: "'Extraordinary' in 'extraordinary claims' means claims that are unusual, shocking, or surprising to the person evaluating them."
  type: true-false
  answer: false
  explanation: "The correct definition of 'extraordinary' here is objective, not subjective: a claim is extraordinary to the extent that it has a low prior probability given existing knowledge. A claim that is personally surprising to you might have a high prior in the reference class of well-informed people. Conversely, a mundane-sounding claim might be extraordinary if it conflicts with well-established science. 'Extraordinary' is not about emotional register — it is about location in probability space. This distinction matters because personal surprise is not a reliable guide to prior probability."

- question: "Explain why the Sagan standard ('extraordinary claims require extraordinary evidence') is not just a heuristic or bias against novelty, but a direct mathematical consequence of Bayes' theorem."
  type: short-answer
  answer: "Bayesian updating works by multiplying prior odds by the likelihood ratio: posterior odds = prior odds × (P(evidence|claim true) / P(evidence|claim false)). A claim with prior probability 1 in N has prior odds of approximately 1:N. To reach even 50% posterior probability requires a likelihood ratio of approximately N. So a claim with prior 1 in a million mathematically requires evidence with a likelihood ratio of roughly a million — evidence that is a million times more likely if the claim is true than if it is false. This is not a preference or a conservative bias; it is what the numbers demand. The more extreme the prior, the larger the likelihood ratio must be to achieve any given posterior probability."
  explanation: "The power of this framing is that it transforms a vague intuition into a precise quantitative claim. Instead of 'I'm skeptical of UFOs,' the Bayesian says: 'My prior is 10^-6; show me evidence with a likelihood ratio of at least 10^4 and I'll take it seriously.' This makes the standard transparent and improvable — if you can establish a higher prior or demonstrate a higher likelihood ratio, you have made genuine progress on the question."
```
