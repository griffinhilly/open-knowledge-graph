---
id: absence-of-evidence
title: "Absence of Evidence Is Evidence of Absence"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: bayesian-thinking-in-practice
    type: hard
  - id: conservation-of-expected-evidence
    type: soft
builds-toward:
  - extraordinary-claims-and-evidence-scaling
tags: ["bayesian", "evidence", "probability", "reasoning"]
stage: advanced
status: validated
---

## Core Idea

The saying "absence of evidence is not evidence of absence" is probabilistically wrong. If a hypothesis predicts that we should observe certain evidence, and we look and do not find it, that observation is evidence against the hypothesis — exactly to the degree that the hypothesis predicted we would find it. If a drug works, we expect clinical trials to show positive results; if trials show nothing, that is evidence the drug does not work. The strength of the evidence depends on the likelihood ratio: how much more likely is the absence of evidence under "hypothesis false" versus "hypothesis true"? When the hypothesis strongly predicts observable consequences, failing to observe them is strong evidence against it.

## How It's Best Learned

Work through the Bayesian math explicitly: if P(observe evidence | H true) = 0.9 and P(observe evidence | H false) = 0.1, then not observing the evidence gives a likelihood ratio of 0.1/0.9 ≈ 0.11, a strong update against H. Practice identifying real-world cases where absence of expected evidence should update beliefs: the dog that did not bark, the study that found no effect, the prediction that did not come true.

## Common Misconceptions

- This does not mean any absence of evidence disproves a claim — the strength depends on how strongly the claim predicted observable consequences.
- The original saying has a grain of truth in informal contexts: sometimes we simply have not looked hard enough. But once we have looked and found nothing, that is informative.

## Explainer

The common saying "absence of evidence is not evidence of absence" sounds wise, but it is probabilistically wrong in most contexts where it gets invoked. If a hypothesis predicts that certain evidence should be observable, and you look carefully and do not find it, that failure to observe is genuine evidence against the hypothesis. The strength of this evidence depends on a precise quantity: how much more likely is the absence under "hypothesis false" compared to "hypothesis true"? When the hypothesis strongly predicts observable consequences, failing to observe them is a powerful update against it.

Consider a concrete case. A pharmaceutical company claims its drug reduces blood pressure. Researchers run a large, well-powered clinical trial and find no statistically significant effect. The company protests: "You haven't proven it doesn't work -- absence of evidence is not evidence of absence." But this defense confuses logical proof with probabilistic evidence. If the drug actually worked, a well-designed trial would detect the effect with high probability -- say 90%. The null result is therefore much more likely if the drug is ineffective than if it is effective. By Bayes' theorem, that null result genuinely shifts probability toward "the drug does not work." The trial did not prove absence with certainty, but it provided substantial evidence of absence.

The Bayesian math makes this precise. If P(evidence | H true) = 0.9 and P(evidence | H false) = 0.1, then not observing the evidence gives a likelihood ratio of P(no evidence | H false) / P(no evidence | H true) = 0.9 / 0.1 = 9, a strong update against H. Sherlock Holmes captured this intuitively with "the dog that did not bark in the night" -- if the dog would reliably bark at an intruder and the dog was silent, the silence is strong evidence that no intruder came. If the dog only sometimes barks, silence is weak evidence. The evidential weight of absence scales with how confidently the hypothesis predicts the evidence's presence.

The original saying retains a grain of truth in one specific case: when you have not actually looked. If you never ran the trial, never searched the house, never checked the data, then the absence of evidence in your possession tells you nothing -- you simply have not gathered information yet. But once you have looked carefully and found nothing, that observation is informative. The distinction between "we haven't looked" and "we looked and found nothing" is the difference between ignorance and evidence. Practical Bayesian thinking requires honoring that distinction rather than hiding behind a comforting aphorism.

## Questions

```yaml
- question: "A company claims its supplement boosts immune function. Researchers conduct a large, well-designed double-blind trial and find no statistically significant effect. The company responds: 'Absence of evidence is not evidence of absence — you just haven't proven it doesn't work.' What is the most accurate Bayesian reply?"
  type: multiple-choice
  options:
    - "The company is correct — a null result only means the study lacked statistical power"
    - "The null result does lower the probability that the supplement works, in proportion to how reliably a real effect would have been detected"
    - "Absence of evidence only matters if the study found positive evidence of harm"
    - "We cannot update our probability estimate in either direction from a null result"
  answer: 1
  explanation: "If the supplement works, a well-designed large trial should detect the effect with high probability. The null result is therefore more likely under 'supplement doesn't work' than under 'supplement works.' By Bayes' theorem, this shifts probability toward the hypothesis that the supplement doesn't work. The company's defense ('you haven't proved absence') conflates logical proof with probabilistic evidence. The null result is genuine evidence against efficacy — its strength depends on the trial's power to detect a real effect."

- question: "Hypothesis H predicts that observable event E will occur with probability 0.95 if H is true, and E occurs with probability 0.05 if H is false. You look for E and do not find it. How should you update your belief in H?"
  type: multiple-choice
  options:
    - "Do not update — absence of evidence is never informative"
    - "Update weakly against H — since E is expected, not finding it is only mildly surprising"
    - "Update strongly against H — the likelihood ratio of not-E is P(¬E|H false)/P(¬E|H true) = 0.95/0.05 = 19:1 in favor of ¬H"
    - "Update in favor of H — the rarity of not-E under H-false means H is more likely"
  answer: 2
  explanation: "The likelihood ratio for not-E is P(¬E | H false)/P(¬E | H true) = (1−0.05)/(1−0.95) = 0.95/0.05 = 19. This means observing ¬E is 19 times more likely if H is false than if H is true — a very strong update against H. When a hypothesis strongly predicts we should see evidence and we don't see it, that absence is powerful evidence against the hypothesis. This is the Bayesian cash-out of 'absence of evidence is evidence of absence.'"

- question: "If a hypothesis predicts observable consequences that we look for and fail to find, failing to find them is evidence against the hypothesis."
  type: true-false
  answer: true
  explanation: "This is the central claim. The strength of the evidence depends on the likelihood ratio: how much more probable is the absence of evidence if the hypothesis is false versus if it is true? When the hypothesis strongly predicts the evidence, a failure to find it is a large update against the hypothesis. The popular saying 'absence of evidence is not evidence of absence' is, in the probabilistic sense, simply wrong in this case."

- question: "The evidential weight of failing to find expected evidence is the same regardless of how thoroughly and carefully we searched."
  type: true-false
  answer: false
  explanation: "The strength of absence-as-evidence depends entirely on P(evidence | hypothesis true) — how likely we were to find the evidence if the hypothesis were actually true. A cursory search that would miss most evidence even if the hypothesis were true yields a weak update. A thorough search that would reliably detect evidence if the hypothesis were true yields a strong update. 'We looked under the couch' is weak absence-of-evidence for 'the keys aren't in this house.' A full building sweep is strong absence-of-evidence."

- question: "Under what conditions does failing to find evidence strongly support absence, and when does it barely matter? Explain using the concept of likelihood ratios."
  type: short-answer
  answer: "Absence of evidence strongly supports absence when the hypothesis predicts that observable evidence would appear with high probability — i.e., P(evidence | hypothesis true) is large. In that case, not finding the evidence gives a large likelihood ratio in favor of the hypothesis being false: P(¬E | H false)/P(¬E | H true) = (1 − P_base)/(1 − P_predicted). When the hypothesis makes a weak prediction — the evidence might not appear even if the hypothesis is true — not finding it barely updates us at all, because the likelihood ratio approaches 1."
  explanation: "The classic example is Sherlock Holmes's 'the dog that did not bark in the night.' If the dog would reliably bark at an intruder, and the dog did not bark, this is strong evidence no intruder came. If the dog only sometimes barks at intruders, silence is weak evidence. The evidential weight of absence scales with how confidently the hypothesis predicts the evidence's presence."
```
