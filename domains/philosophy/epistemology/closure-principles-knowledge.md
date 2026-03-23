---
id: closure-principles-knowledge
title: Epistemic Closure and Logical Closure Principles
domain: philosophy
course: epistemology
prerequisites:
- id: epistemic-closure
  type: hard
- id: logical-form
  type: hard
builds-toward:
- moorean-responses-skepticism
tags:
- closure
- knowledge
- logical-properties
- skepticism
stage: formal-systems
status: validated
---

# Epistemic Closure and Logical Closure Principles

## Core Idea
Epistemic closure principles specify how knowledge properties transmit through logical operations. The most discussed principle is closure under known entailment: if you know P and know that P entails Q, you know Q. Skeptical arguments exploit supposed failures of closure to argue that we lack knowledge of ordinary external world propositions. Understanding formal closure principles is essential for assessing these arguments.

## Questions

```yaml
- question: "You know you have hands (P). You know that having hands entails you are not a handless brain in a vat (P → ~BIV). A student applies CKE and concludes: 'Therefore I know I'm not a brain in a vat.' What is philosophically significant about this conclusion?"
  type: multiple-choice
  options:
    - "It is a straightforward valid inference — CKE is uncontroversially true and the conclusion follows trivially"
    - "The conclusion (~BIV) seems epistemically inaccessible from the inside, creating pressure either to deny ordinary hand knowledge or to deny CKE itself"
    - "It commits an informal fallacy by conflating direct knowledge with inferred knowledge"
    - "It proves that BIV skepticism is false, since the conclusion is clearly available to ordinary reasoners"
  answer: 1
  explanation: "The philosophical tension is that ~BIV seems like a 'heavyweight' claim you cannot verify from the inside — you would have the same experiences whether or not you were a BIV. So the CKE inference forces a choice: either accept you know ~BIV (the Moorean response), or run the argument backward: since you don't know ~BIV, and CKE says knowing P requires knowing its entailments, you don't know you have hands. Neither horn is comfortable, which is what makes CKE philosophically central."

- question: "Dretske and Nozick deny closure under known entailment. On their tracking theory, which of the following best explains why you might know you have hands without knowing you are not a brain in a vat?"
  type: multiple-choice
  options:
    - "Ordinary perceptual knowledge is infallible, but BIV knowledge requires a higher epistemic standard"
    - "You track 'I have hands' because you would not believe it if it were false (you'd lack the perceptual experience), but you do not track 'I am not a BIV' because you would still believe it even if you were a BIV"
    - "The BIV scenario is logically impossible, so the entailment from hands to ~BIV does not hold"
    - "CKE only fails for highly technical philosophical claims, not for ordinary knowledge like having hands"
  answer: 1
  explanation: "The tracking theory defines knowledge as a counterfactual sensitivity: you know P iff you wouldn't believe P if P were false. You track 'I have hands' because if you lacked hands, you'd lack the relevant perceptual experience. But if you were a BIV, you'd still believe you weren't one — the BIV scenario is designed to fool you. So you don't track ~BIV even though you (supposedly) know P. This is exactly what Dretske and Nozick use to motivate closure denial: the perceptual connection that gives you ordinary knowledge doesn't extend to ruling out remote skeptical possibilities."

- question: "The skeptical argument about brains in vats uses modus tollens on CKE: if knowing P requires knowing ~BIV (by CKE), but you don't know ~BIV, then you don't know P."
  type: true-false
  answer: true
  explanation: "This is precisely the logical form of the skeptical argument. CKE says: K(P) ∧ K(P → Q) → K(Q). Contraposing: ¬K(Q) → ¬K(P) ∨ ¬K(P → Q). Since you plausibly know the entailment from having hands to not being a BIV, the skeptic runs: ¬K(~BIV) → ¬K(hands). The skeptic assumes CKE is true and uses your inability to know ~BIV to undermine ordinary knowledge."

- question: "Epistemic closure under known entailment is universally accepted by epistemologists as correct and unproblematic."
  type: true-false
  answer: false
  explanation: "CKE is explicitly contested. Philosophers Fred Dretske and Robert Nozick denied closure as part of their tracking theory responses to skepticism. While closure is intuitively compelling, its interaction with skeptical scenarios generates significant controversy. The debate is not merely academic: different theories of knowledge (tracking, safety, contextualism, relevant alternatives) make different predictions about whether and when CKE holds."

- question: "What is the 'odd result' that defenders of epistemic closure level against Dretske and Nozick's closure-denial view?"
  type: short-answer
  answer: "If closure denial is correct, a competent logician who explicitly deduces Q from known premises (knowing P and P → Q, then inferring Q) would thereby know less than an equally situated non-logician who never made the deduction. The non-logician, having never formed the belief Q, avoids the 'untracked' claim and retains knowledge of P. But the logician, by performing valid reasoning, arrives at a belief Q that they don't 'track' — undermining their knowledge of P by CKE's contrapositive. This seems backwards: logical reasoning should not reduce knowledge. Closure defenders argue this consequence makes the tracking theory epistemologically untenable."
  explanation: "This objection, pressed especially by John Hawthorne, captures why closure denial has a high philosophical cost even if it avoids skepticism. The alternative — Moorean responses that simply accept we know ~BIV — carries its own costs, but at least preserves the intuition that deduction is epistemically safe."
```

## Explainer

The intuitive idea behind **epistemic closure** is that knowledge should be closed under reasoning: if you know something, and you validly reason from it to a conclusion, you should end up knowing the conclusion too. From your study of epistemic closure and logical form, you understand both what closure means informally and how logical entailment works. **Closure under known entailment** makes this precise: if you know P, and you know that P entails Q, then you know Q. Call this principle "CKE."

CKE seems almost trivially true at first. Suppose you know your car is in the parking lot (P). You know that if your car is in the parking lot, it hasn't been stolen (P entails Q). Surely you know your car hasn't been stolen (Q). But the philosophical action comes from applying CKE to **skeptical scenarios**. Consider: you know you have hands (P). You know that having hands entails you are not a handless brain in a vat (BIV) being fed false sensory experiences (P entails ~BIV). CKE then says you know you're not a BIV (~BIV). But wait — how could you possibly know you're not a BIV? You can't check from the inside. This creates pressure in both directions. Either you accept that you do know you're not a BIV (Moorean response), or you concede you don't know you're not a BIV and therefore, by reversing CKE, conclude you don't know you have hands (skeptical response).

The formal structure of the skeptical argument is a **modus tollens** on CKE: if knowing P entails knowing Q (CKE), but you don't know Q (not-BIV), then you don't know P (hands). This is why **closure denial** is one possible anti-skeptical strategy: philosophers like Fred Dretske and Robert Nozick argued that knowledge does NOT always transmit under known entailment — specifically, "heavyweight" implications like "I'm not a BIV" can be detached from ordinary knowledge without undermining it. On their accounts, you know you have hands through the right perceptual connection to the world, but this doesn't require eliminating remote possibilities like vat scenarios. The tracking theory of knowledge (know P iff you wouldn't believe P if P were false) predicts this: you wouldn't believe you had hands if you didn't have hands (counterfactual tracks), but you might still believe you're not a BIV even if you were one, so you don't "track" that claim.

Closure defenders like John Hawthorne respond that abandoning CKE is too high a price: if you genuinely know P, and you reason validly to Q, it would be epistemically irresponsible to claim you don't know Q. Closure denial also generates odd results — it seems to entail that a competent logician who deduces Q from known premises can know less than a non-logician who never made the deduction. Understanding the formal structure of CKE and its alternatives lets you see that the debate isn't really about closure as an abstract principle — it's about which theory of knowledge best handles the joint demands of ordinary knowledge attribution and skeptical vulnerability. The **formal properties** of closure (transitivity, whether it holds for disjunctions, whether it applies to single agents or communities) generate a rich technical literature that maps exactly where different theories of knowledge succeed and fail.
