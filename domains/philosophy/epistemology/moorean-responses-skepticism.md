---
id: moorean-responses-skepticism
title: Moore's Methods and Responses to Skepticism
domain: philosophy
course: epistemology
prerequisites:
- id: cartesian-skepticism
  type: hard
- id: external-world-skepticism
  type: hard
- id: closure-principles-knowledge
  type: soft
tags:
- moorean
- skepticism
- closure
- methodology
stage: formal-systems
status: draft
---

# Moore's Methods and Responses to Skepticism

## Core Idea
G.E. Moore famously responded to skepticism by insisting that he knows ordinary propositions like 'here is a hand' more certainly than he knows the premises of skeptical arguments. Moorean responses deny closure principles or contextualize standards rather than accepting skeptical conclusions. This approach privileges commonsense knowledge and shifts the burden of proof to skeptics.

## How It's Best Learned
Examine Moore's specific argument form: assuming P and closure would entail absurdity, so either closure fails or the skeptical premise is false. Understand the intuitive appeal: why shouldn't we trust ordinary perception over abstract skeptical reasoning? But also grasp skeptical responses: why closure and skeptical premises seem rationally unavoidable.

## Common Misconceptions
- Moore's position isn't a simple appeal to intuition; it uses inference to the best explanation about which principles to trust. - Moorean responses typically require modifications to closure or contextualism; they don't simply accept knowledge while rejecting closure. - The approach doesn't prevent skeptical scenarios from being genuine possibilities; it just denies they're relevant alternatives.

## Questions

```yaml
- question: "A philosopher presents this valid argument: (1) You cannot rule out being a brain in a vat. (2) If you cannot rule out being a brain in a vat, you cannot know you have hands. (3) Therefore, you do not know you have hands. A Moorean response would most likely:"
  type: multiple-choice
  options:
    - "Accept the conclusion and seek comfort in the fact that we act as if we have hands even without knowledge"
    - "Deny the argument is valid and show that premises (1) and (2) do not logically entail (3)"
    - "Run the argument in reverse: 'I know I have hands' gives stronger grounds to deny premise (1) or (2) than the skeptical premises give to accept (3)"
    - "Argue that brains in vats cannot have genuine beliefs, so the skeptical scenario is self-defeating"
  answer: 2
  explanation: "The Moorean move — 'tollensing the ponens' — runs the argument backwards. Instead of: P1, P2 → ¬Knowledge, Moore says: Knowledge, P2 → ¬P1. Which direction you run the argument depends on which you trust more: the skeptical premises, or your ordinary perceptual knowledge. Moore's claim is that 'I know I have hands' has higher epistemic standing than any abstract philosophical premise, so the monstrous conclusion (no knowledge of hands) gives us grounds to reject a premise."

- question: "Nozick's tracking theory supports denying closure in response to skepticism. Which best states the key claim?"
  type: multiple-choice
  options:
    - "You know 'I have hands' because this belief is justified by coherent sensory experience, but justification doesn't extend to skeptical scenarios"
    - "You know 'I have hands' because your belief tracks the truth — you believe it when true and wouldn't if false — but you cannot track 'I am not a brain in a vat' because in that scenario you'd still believe you're not"
    - "You know 'I have hands' because the probability of being a brain in a vat is negligibly small"
    - "You know 'I have hands' because ordinary language doesn't require ruling out remote possibilities like brains in vats"
  answer: 1
  explanation: "Nozick's tracking theory: you know P if your belief tracks its truth — you believe it when true, and wouldn't believe it if it were false. You track 'I have hands' perfectly: if you didn't have hands, your experience would be different. But 'I am not a brain in a vat' fails: if you were a brain in a vat, you'd still believe you're not. So you don't know this — without that undermining your hand knowledge. This is how closure fails: knowledge doesn't transmit across all known entailments."

- question: "Moore's response to skepticism is simply an appeal to common sense — he says 'I just know I have hands' without providing any philosophical reasoning."
  type: true-false
  answer: false
  explanation: "This is a common misreading. Moore's position uses a genuine philosophical argument structure: he runs the skeptical argument in reverse (tollensing the ponens) and makes the substantive epistemological claim that ordinary knowledge has higher epistemic standing than abstract philosophical premises. As the Common Misconceptions note: 'Moore's position isn't a simple appeal to intuition; it uses inference to the best explanation about which principles to trust.'"

- question: "According to contextualism, both the skeptic and Moore can be correct — each is making a knowledge claim that is true relative to different conversational standards."
  type: true-false
  answer: true
  explanation: "Contextualism holds that standards for 'knowing' vary with conversational context. In everyday life, relevant alternatives to 'I have hands' are things like bandages or prostheses — easily ruled out. In a philosophy seminar where brains-in-vats are explicitly under discussion, those remote alternatives become relevant, raising the standards. On this view, 'I know I have hands' is true in the ordinary context and potentially false in the philosophical context — neither speaker is simply wrong."

- question: "Explain what 'tollensing the ponens' means in the context of Moore's response to skepticism, and why it is a philosophically legitimate move rather than a logical error."
  type: short-answer
  answer: "Tollensing the ponens means running a modus ponens argument backwards as modus tollens. The skeptic argues: P1, P2, therefore ¬K. Moore argues: K, P2, therefore ¬P1. Both are valid argument forms. Which direction to run the argument depends on which premise you have stronger reason to accept. Moore's claim is that 'I know I have hands' (K) has higher epistemic standing than the skeptic's abstract premise P1 — so the obviously false conclusion is grounds to reject the premise."
  explanation: "Logical validity is symmetric: if an argument is valid, both modus ponens and modus tollens are valid inferences from the same premises. A valid argument whose conclusion seems obviously false provides evidence against one of its premises — this is how mathematics works too (reductio ad absurdum). Moore applies this same logic to skepticism: the monstrous conclusion that I don't know I have hands is evidence against a premise, not an invitation to accept the monstrosity."
```

## Explainer

From your study of Cartesian and external-world skepticism, you are familiar with the structure of the skeptical argument: I cannot rule out that I am a brain in a vat (or a dreaming mind); if I cannot rule this out, I cannot know anything about the external world; therefore I know nothing about the external world. The argument seems valid. The premises seem plausible. And yet G.E. Moore looked down at his hands and said: that argument cannot be right, because I *know* I have hands — and I know this more certainly than I know the skeptic's abstract premises.

Moore's move is philosophically bold precisely because it reverses the normal direction of philosophical argument. Typically, you start from premises you are confident in and derive conclusions. Moore essentially runs the argument backwards: the conclusion of the skeptical argument (I don't know I have hands) is so obviously false that we should reject one of the premises that leads to it. This is sometimes called **"tollensing the ponens"** — where the skeptic runs "P1, P2, therefore ~K" (no knowledge), Moore runs "K, P2, therefore ~P1" (one of the skeptical premises must be wrong). Which direction you run the argument depends on which premise you trust more — the skeptical premises or your perceptual knowledge. Moore's claim is that ordinary knowledge has *higher epistemic standing* than abstract philosophical arguments.

The connection to **closure principles** (which you have studied) is crucial. Recall that epistemic closure says: if you know P, and you know that P entails Q, then you know Q. The skeptic uses closure to derive: if you know you have hands, and you know that having hands entails you are not a brain in a vat, then you know you are not a brain in a vat — but you don't know that, so you don't know you have hands. One Moorean response (developed by Fred Dretske and Robert Nozick) **denies closure**: knowledge does not transmit across all known entailments. Your knowledge of "I have hands" is grounded in perceptual experience of hands; that grounding does not extend to the remote possibility of brains in vats. The tracking theory of knowledge (Nozick) makes this precise: you know P if your belief tracks the truth of P (you believe it when it's true, don't when it's false). You track "I have hands" perfectly in ordinary circumstances, but you cannot track "I am not a brain in a vat" because in the skeptical scenario you would still believe you are not — your belief doesn't track that proposition.

A second Moorean strategy uses **contextualism**: the standards for "knowing" vary with conversational context. In the ordinary context of daily life, the relevant alternatives to "I have hands" are prostheses, bandages, optical illusions — none of which are present. In a philosophical seminar room where brains-in-vats are on the table, the relevant alternatives expand, and ordinary knowledge claims may fail. On this view, both the skeptic and Moore are right in their own contexts. Neither the skeptical conclusion nor the common-sense knowledge claim is absolutely true — each is true relative to the standards operative in a particular conversational setting. The lasting contribution of Moorean responses is to remind epistemologists that **certainty runs in both directions**: if an argument leads to a monstrous conclusion, that is evidence against the argument, not just an invitation to accept the monstrosity.


