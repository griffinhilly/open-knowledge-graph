---
id: burden-of-proof
title: Burden of Proof and the Presumption Principle
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: argument-structure
  type: hard
- id: burden-of-proof-evaluation
  type: soft
builds-toward:
- principle-of-charity
- evaluating-evidence
tags:
- burden-of-proof
- presumption
- assertion
- epistemology
stage: formal-systems
status: validated
---
# Burden of Proof and the Presumption Principle

## Core Idea
The burden of proof is the obligation to provide evidence for a claim, falling on whoever makes the positive assertion. 'Extraordinary claims require extraordinary evidence' (Sagan's principle) captures that the strength of evidence required scales with how surprising the claim is relative to background knowledge. Failing to meet the burden of proof — especially by demanding others disprove a claim — is the fallacy of appeal to ignorance (argumentum ad ignorantiam): 'You can't prove it doesn't exist, so it does.' Correctly allocating the burden is foundational to structured debate.

## How It's Best Learned
In each argumentative exchange you analyze, ask: who is making the positive claim? What evidence have they provided? Does the evidence scale appropriately with the claim's scope? Practice detecting when burden-shifting is occurring.

## Common Misconceptions
- Thinking absence of disproof constitutes positive evidence — the burden stays with the positive claimant.
- Applying the burden principle mechanically without considering that sometimes the default presumption should be questioned (e.g., in science, the null hypothesis).

## Questions

```yaml
- question: "A health blogger claims that a herbal supplement cures anxiety. When a skeptic asks for evidence, the blogger replies: 'You can't prove it doesn't work. Millions of people use it.' What is wrong with this response?"
  type: multiple-choice
  options:
    - "The response is valid — if no one has disproved the claim, it is reasonable to accept it provisionally"
    - "The blogger is shifting the burden of proof to the skeptic, but the obligation to provide evidence rests on the positive claimant"
    - "The response is too emotional to count as a logical argument"
    - "Popularity of use is a strong form of empirical evidence and should count in the blogger's favor"
  answer: 1
  explanation: "This is the appeal to ignorance fallacy (argumentum ad ignorantiam): reasoning that because a claim hasn't been disproved, it must be true. The burden of proof falls on whoever makes the positive assertion — that the supplement works. Absence of disproof is not positive evidence. The blogger has made a claim and must supply supporting premises; the skeptic is not obligated to disprove it first."

- question: "A researcher claims to have discovered a simple plant extract that reverses late-stage Alzheimer's disease. A critic says this claim requires far more evidence than a claim that a plant extract improves mild sleep quality. Why is the critic correct?"
  type: multiple-choice
  options:
    - "The critic is applying a double standard — all claims require the same type and amount of evidence"
    - "Because the Alzheimer's claim is more expensive to test, it requires a higher evidentiary bar"
    - "The threshold of evidence required scales with how surprising a claim is relative to existing background knowledge"
    - "Late-stage disease claims require clinical trials while mild condition claims do not"
  answer: 2
  explanation: "Sagan's principle — 'extraordinary claims require extraordinary evidence' — reflects Bayesian logic: the prior probability of a claim affects how much evidence is needed to update belief in it. A claim that contradicts well-established medical knowledge (that late-stage Alzheimer's can be reversed) carries a very low prior, so evidence must overcome that. The sleep quality claim is modest and consistent with background knowledge. This is not a double standard — it is proportionality, calibrating evidential demands to the probability of the claim."

- question: "If you cannot disprove a claim, that constitutes positive evidence that the claim is true."
  type: true-false
  answer: false
  explanation: "This is the appeal to ignorance fallacy. Absence of disproof is not the same as positive evidence. We lack disproof of infinitely many contradictory things simultaneously — if undisprovedeness were evidence, we would be forced to believe them all. The absence of evidence for X is only weak evidence against X when we would expect evidence to exist if X were true. The burden of proof principle holds that positive assertions require positive evidence, not mere absence of counter-evidence."

- question: "The burden of proof falls on the person making the positive assertion, not on those who are skeptical of it."
  type: true-false
  answer: true
  explanation: "This is the foundational principle of rational discourse. We begin from a baseline of not believing things for which no evidence exists, and we shift belief only when warranted by evidence. This asymmetry is not bias — it is necessary to avoid simultaneously believing infinitely many unverified claims. The positive claimant introduces a new belief candidate; they must supply the premises that justify its adoption. Skeptics are not obligated to disprove claims — that reverses the entire structure of evidence-based reasoning."

- question: "Why does absence of disproof not constitute evidence that a claim is true? Use the structure of rational discourse to explain."
  type: short-answer
  answer: "Absence of disproof tells us nothing about a claim's truth — it only tells us no one has yet found a counter-example or disproving argument. If undisprovedeness were treated as positive evidence, we would be logically committed to believing an infinite number of unverified claims simultaneously (since most claims have never been disproved). Rational discourse begins from the baseline of not believing claims until evidence supports them; the positive claimant must provide premises that justify belief, not wait for others to eliminate all alternatives."
  explanation: "The principle connects to the basic structure of argument: premises provide positive grounds for a conclusion. 'No one has disproved X' provides no premise about X's truth — it only makes a claim about the history of argumentation. The Sagan/Bayesian framing adds precision: prior probability matters. Absence of evidence is weak evidence of absence only when we would expect evidence to have appeared if the claim were true. This threshold varies by claim, which is why extraordinary claims require extraordinary evidence."
```

## Explainer

From your study of argument structure, you know that arguments consist of premises offered in support of a conclusion. The burden of proof assigns an obligation: whoever makes a claim in an argument must supply premises that support it. This sounds obvious until you notice how often it gets reversed in practice — and how much epistemic mischief that reversal causes.

The basic rule is that **the burden of proof falls on the positive claimant**: the person who asserts that something exists, occurred, or is true. The burden does not fall on the audience to disprove it. If someone asserts that a particular cure works, they must present evidence; it is not your obligation to demonstrate that it does not work. This asymmetry reflects the structure of rational discourse. We begin from a baseline of not believing things for which no evidence exists, and we add beliefs only when evidence warrants them. The alternative — believing everything until disproven — would require believing an indefinite number of contradictory things simultaneously.

Carl Sagan's formulation — **"extraordinary claims require extraordinary evidence"** — adds a calibration principle to the basic burden rule. The threshold of evidence required scales with how surprising the claim is relative to background knowledge. A claim that a common herb causes mild drowsiness requires modest support. A claim that a herb can reverse terminal cancer requires substantially more, because it contradicts accumulated medical knowledge. This proportionality requirement is not mere skeptical bias; it reflects Bayesian logic — the prior probability of a claim is part of what evidence must overcome.

The fallacy that violates the burden principle is **appeal to ignorance** (argumentum ad ignorantiam): reasoning that because a claim has not been disproven, it must be true (or, symmetrically, because it hasn't been proven, it must be false). "No one has ever proved that ghosts don't exist, so they must exist" is the classic form. The error is treating absence of disproof as positive evidence. The absence of evidence is only weak evidence of absence when we would expect to have found evidence if the thing existed. In science, the analogous structure is the **null hypothesis**: by default, we assume no effect until evidence rejects that assumption. The null hypothesis can itself be questioned when the default presumption isn't neutral, but the underlying logic of requiring positive evidence to shift belief remains constant.

