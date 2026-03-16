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
status: draft
---

# Epistemic Closure and Logical Closure Principles

## Core Idea
Epistemic closure principles specify how knowledge properties transmit through logical operations. The most discussed principle is closure under known entailment: if you know P and know that P entails Q, you know Q. Skeptical arguments exploit supposed failures of closure to argue that we lack knowledge of ordinary external world propositions. Understanding formal closure principles is essential for assessing these arguments.

## Explainer

The intuitive idea behind **epistemic closure** is that knowledge should be closed under reasoning: if you know something, and you validly reason from it to a conclusion, you should end up knowing the conclusion too. From your study of epistemic closure and logical form, you understand both what closure means informally and how logical entailment works. **Closure under known entailment** makes this precise: if you know P, and you know that P entails Q, then you know Q. Call this principle "CKE."

CKE seems almost trivially true at first. Suppose you know your car is in the parking lot (P). You know that if your car is in the parking lot, it hasn't been stolen (P entails Q). Surely you know your car hasn't been stolen (Q). But the philosophical action comes from applying CKE to **skeptical scenarios**. Consider: you know you have hands (P). You know that having hands entails you are not a handless brain in a vat (BIV) being fed false sensory experiences (P entails ~BIV). CKE then says you know you're not a BIV (~BIV). But wait — how could you possibly know you're not a BIV? You can't check from the inside. This creates pressure in both directions. Either you accept that you do know you're not a BIV (Moorean response), or you concede you don't know you're not a BIV and therefore, by reversing CKE, conclude you don't know you have hands (skeptical response).

The formal structure of the skeptical argument is a **modus tollens** on CKE: if knowing P entails knowing Q (CKE), but you don't know Q (not-BIV), then you don't know P (hands). This is why **closure denial** is one possible anti-skeptical strategy: philosophers like Fred Dretske and Robert Nozick argued that knowledge does NOT always transmit under known entailment — specifically, "heavyweight" implications like "I'm not a BIV" can be detached from ordinary knowledge without undermining it. On their accounts, you know you have hands through the right perceptual connection to the world, but this doesn't require eliminating remote possibilities like vat scenarios. The tracking theory of knowledge (know P iff you wouldn't believe P if P were false) predicts this: you wouldn't believe you had hands if you didn't have hands (counterfactual tracks), but you might still believe you're not a BIV even if you were one, so you don't "track" that claim.

Closure defenders like John Hawthorne respond that abandoning CKE is too high a price: if you genuinely know P, and you reason validly to Q, it would be epistemically irresponsible to claim you don't know Q. Closure denial also generates odd results — it seems to entail that a competent logician who deduces Q from known premises can know less than a non-logician who never made the deduction. Understanding the formal structure of CKE and its alternatives lets you see that the debate isn't really about closure as an abstract principle — it's about which theory of knowledge best handles the joint demands of ordinary knowledge attribution and skeptical vulnerability. The **formal properties** of closure (transitivity, whether it holds for disjunctions, whether it applies to single agents or communities) generate a rich technical literature that maps exactly where different theories of knowledge succeed and fail.
