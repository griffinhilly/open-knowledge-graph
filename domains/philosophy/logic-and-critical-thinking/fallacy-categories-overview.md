---
id: fallacy-categories-overview
title: Categories of Logical Fallacies
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: arguments-premises-and-conclusions
  type: hard
builds-toward:
- formal-logical-fallacies
- informal-fallacies-intro
tags:
- fallacies
- reasoning-errors
- argument-evaluation
stage: abstract-reasoning
status: draft
---

# Categories of Logical Fallacies

## Core Idea
Fallacies are reasoning errors—arguments appearing plausible that fail to support conclusions. Major categories: fallacies of relevance (premises don't address the conclusion), fallacies of weak induction (premises insufficiently support conclusion), and fallacies of ambiguity (unclear language masks failed reasoning).

## Questions

```yaml
- question: "A senator argues: 'My opponent has been accused of financial misconduct, so his healthcare reform proposal must be flawed.' Which fallacy category does this commit, and why?"
  type: multiple-choice
  options:
    - "Fallacy of weak induction — the financial misconduct is relevant but insufficient evidence about policy quality"
    - "Fallacy of relevance — attacking the person's character is irrelevant to whether the policy argument is sound"
    - "Fallacy of ambiguity — 'flawed' is used ambiguously to mean both ethically suspect and logically incorrect"
    - "No fallacy — a person's character and judgment are relevant evidence about the quality of their policy proposals"
  answer: 1
  explanation: "This is an ad hominem — a fallacy of relevance. The senator's financial misconduct, even if true, does not bear on the logical or empirical merits of the healthcare proposal. The premise (misconduct) doesn't address the conclusion (policy is flawed) — it changes the subject to the person instead. Option D is the tempting wrong answer: character can be relevant in some contexts (e.g., assessing trustworthiness), but it doesn't determine the logical validity or policy soundness of a specific proposal."

- question: "'We gave this new medication to eight patients and all of them reported improvement. Therefore, it is effective for treating this condition.' Which fallacy does this commit?"
  type: multiple-choice
  options:
    - "Fallacy of relevance — patient outcomes are irrelevant to drug efficacy claims"
    - "Fallacy of ambiguity — 'improvement' could mean different things across patients"
    - "Fallacy of weak induction — the evidence is relevant but eight patients is far too small a sample to support a general efficacy claim"
    - "No fallacy — positive outcomes are direct evidence of effectiveness"
  answer: 2
  explanation: "This is hasty generalization — a fallacy of weak induction. The premise (eight patients improved) is genuinely relevant to the conclusion (the drug is effective) — that's what makes this a weak induction fallacy rather than a relevance fallacy. But the evidence is woefully insufficient: eight patients is far too small a sample to rule out placebo effect, natural recovery, selection bias, or chance. Relevance is necessary but not sufficient; the premises must also provide adequate support."

- question: "An ad hominem attack is a fallacy of weak induction because personal character provides weak — but still relevant — evidence about the quality of someone's argument."
  type: true-false
  answer: false
  explanation: "Ad hominem is a fallacy of RELEVANCE, not weak induction. The distinction matters: in a relevance fallacy, the premises don't address the conclusion at all — they change the subject. A person's character or motives are irrelevant to whether their premises are true and their reasoning is valid. Weak induction fallacies have premises that are genuinely related to the conclusion but provide insufficient support. The diagnostic question: 'Does attacking the person's character address the argument itself?' — the answer is no, making it a relevance failure."

- question: "The diagnostic test for fallacies of ambiguity is to ask: if I assign a single, consistent meaning to each key term throughout the argument, does the argument still go through?"
  type: true-false
  answer: true
  explanation: "Ambiguity fallacies like equivocation work by using a word in two different senses — one sense in the premises, another in the conclusion — making an invalid inference appear valid. When you pin down a single meaning and hold it constant, the hidden shift becomes visible and the argument falls apart. For example: 'Laws of nature never fail; the laws of economics are laws; therefore, the laws of economics never fail.' If 'laws' consistently means 'physical laws,' the second premise is false. If it consistently means 'generalizations,' the first is false. Only by shifting between meanings does the argument seem to work."

- question: "What is the difference between a fallacy of relevance and a fallacy of weak induction? Why does the distinction matter for evaluating arguments?"
  type: short-answer
  answer: "A fallacy of relevance occurs when the premises don't address the conclusion at all — they change the subject to something easier to attack or emotionally compelling, but logically beside the point (e.g., attacking the speaker instead of the argument). A fallacy of weak induction occurs when the premises are genuinely related to the conclusion but don't provide sufficient support — the inferential step is too big for the evidence (e.g., generalizing from a tiny sample). The distinction matters because the appropriate response differs: a relevance fallacy requires pointing out that the premise is off-topic; a weak induction fallacy requires showing that the premise, while relevant, doesn't establish enough."
  explanation: "This distinction also shapes what a good rebuttal looks like. Against a relevance fallacy, you say: 'Even if that's true, it doesn't address the question.' Against a weak induction fallacy, you say: 'That evidence is relevant, but it's not nearly strong enough to support that conclusion.' Confusing the two leads to ineffective rebuttals — for instance, trying to dispute the facts of an ad hominem (which grants that the facts matter) rather than rejecting the premise as irrelevant."
```

## Explainer

You already know from arguments-premises-and-conclusions that a good argument has two requirements: the premises must be relevant to the conclusion, and they must provide adequate support for it. The taxonomy of fallacies maps directly onto these requirements. When an argument fails because its premises are irrelevant — they don't address the conclusion at all — it commits a **fallacy of relevance**. When the premises are related to the conclusion but don't provide enough support for it — the inference is too weak — it commits a **fallacy of weak induction**. A third category, **fallacies of ambiguity**, captures failures where unclear or shifting language creates the illusion of valid reasoning.

Fallacies of relevance are often emotionally compelling even though they're logically beside the point. The *ad hominem* attacks the person making the argument rather than the argument itself — the speaker's character or motives are irrelevant to whether their premises are true. The *appeal to inappropriate authority* cites an impressive-sounding source that lacks expertise on the specific question at hand. The *straw man* attacks a distorted, weakened version of the opponent's position — it looks like refutation, but the actual position has not been engaged. The diagnostic question for relevance fallacies is always: do the premises actually address the conclusion, or are they changing the subject to something easier to attack?

Fallacies of weak induction have premises that are genuinely relevant to the conclusion but don't do enough evidential work. *Hasty generalization* draws a broad conclusion from too small or unrepresentative a sample — the premises do connect to the conclusion, but the evidence is insufficient. *False cause* (post hoc, ergo propter hoc) infers causation from temporal succession alone — correlation is relevant evidence of causation, but correlation alone is far from sufficient. *Appeal to ignorance* treats the absence of disconfirming evidence as positive evidence — the connection to the conclusion is real but the support is too thin. Recognizing weak induction requires shifting from the question "does this connect?" to "how much support does this actually provide?"

Fallacies of ambiguity exploit multiple meanings or grammatical vagueness in the premises. *Equivocation* uses the same word in two different senses across the argument, making an invalid inference appear valid — for example, using "law" to mean both "physical law" and "legal statute" within a single argument. *Amphiboly* arises from structural ambiguity in a sentence that makes the premise's meaning indeterminate. These are particularly insidious because the argument may be formally valid if the meaning stays fixed — the failure is that the meaning quietly shifts. Spotting ambiguity fallacies requires asking: if I pin down a single, consistent meaning for each key term, does the argument still go through?
