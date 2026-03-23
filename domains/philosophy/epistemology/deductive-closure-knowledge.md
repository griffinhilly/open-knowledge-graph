---
id: deductive-closure-knowledge
title: Deductive Closure and Knowledge
domain: philosophy
course: epistemology
prerequisites:
- id: epistemic-closure
  type: hard
- id: what-is-knowledge
  type: soft
builds-toward:
- skeptical-scenarios-knowledge-closure
tags:
- knowledge
- closure
- deduction
- entailment
stage: formal-systems
status: validated
---

# Deductive Closure and Knowledge

## Core Idea
The closure principle asserts that knowledge is closed under known entailment: if you know that P, and you know that P entails Q, then you know Q (at least absent defeating conditions). This principle faces pressure from skeptical scenarios where you know ordinary propositions but arguably don't know skeptical scenarios are false, yet the latter follows from the former. Debates over closure reveal tensions between our intuitions about knowledge and about skepticism.

## How It's Best Learned
Test closure with examples: you know your car is in the driveway, you know this entails the driveway exists, so do you know the driveway exists? Examine skeptical challenges to closure and alternative closure principles.

## Common Misconceptions
- Thinking closure means you can know any logical consequence of known propositions.
- Confusing closure-under-entailment with closure-under-known-entailment.
- Assuming closure is necessary for any adequate account of knowledge.

## Questions

```yaml
- question: "The brain-in-a-vat scenario creates a problem for deductive closure because:"
  type: multiple-choice
  options:
    - "It shows that 'I am sitting reading' does not actually entail 'I am not a brain in a vat'"
    - "It suggests we know ordinary things but cannot know skeptical hypotheses are false, even though ordinary knowledge entails this"
    - "It demonstrates that knowledge requires certainty, which we lack for ordinary beliefs"
    - "It shows that deductive inference is unreliable when applied to philosophical scenarios"
  answer: 1
  explanation: "The structure of the problem is: (1) you know ordinary proposition P ('I am sitting reading'); (2) P entails Q ('I am not a brain in a vat'); (3) by closure, you know Q. But there is strong intuition that you cannot know Q — your evidence doesn't distinguish the real situation from the vat scenario. Something has to give: closure, ordinary knowledge, or the claim that you can't know Q. Option A is wrong because the entailment holds — being a brain in a vat would mean you are not actually sitting reading. Option C mischaracterizes the problem, which is about closure, not about certainty."

- question: "A philosopher accepts deductive closure and also accepts that you know ordinary things (your car is in the driveway, your hands are before you). What must they conclude about skeptical hypotheses?"
  type: multiple-choice
  options:
    - "Skepticism is correct — we know nothing, because all knowledge depends on ruling out skeptical alternatives"
    - "We do know that skeptical hypotheses are false — closure requires it, given that ordinary knowledge entails this"
    - "Closure only applies to analytic entailments, not to contingent propositions about external reality"
    - "Knowledge of ordinary things and knowledge of skeptical hypotheses are logically independent"
  answer: 1
  explanation: "This is the forced conclusion of accepting both closure and ordinary knowledge. If you know P (ordinary facts) and P entails Q (not-brain-in-a-vat), then by closure you know Q. You cannot consistently accept closure, accept ordinary knowledge, and deny that you know skeptical hypotheses are false. This seems counterintuitive — and that's the puzzle. Option A accepts closure but rejects ordinary knowledge (the skeptic's position). Option B is the position you must hold if you keep both closure and common sense."

- question: "Nozick's tracking account of knowledge accepts deductive closure but adds extra conditions to restrict what follows from known propositions."
  type: true-false
  answer: false
  explanation: "Nozick's tracking account is precisely one of the main ways to DENY closure. On the tracking view, knowledge requires that your belief be sensitive to the truth: if P were false, you would not believe P. You can track the truth of 'my car is in the driveway' (if it weren't, you'd see an empty driveway), but you cannot track the falsehood of 'I am a brain in a vat' (your experiences would be identical in both worlds). So tracking knowledge of ordinary P does not extend to tracking the negation of skeptical hypotheses — closure fails."

- question: "Accepting deductive closure forces philosophers to adopt skepticism, since no one can know that skeptical scenarios are false."
  type: true-false
  answer: false
  explanation: "This is only one of three responses available. Skeptics do accept closure and deny ordinary knowledge. But a second option is to accept both closure AND ordinary knowledge — and conclude that we DO know skeptical hypotheses are false (even if this seems surprising). A third option is contextualism: in ordinary conversational contexts the standards are low and we know everyday facts; in skeptical contexts the standards rise. Closure does not force skepticism; it creates a trilemma where each horn has costs."

- question: "What is the trilemma generated by applying deductive closure to skeptical scenarios? What must any response to the problem sacrifice?"
  type: short-answer
  answer: "The trilemma: (1) accept closure + accept ordinary knowledge → must accept we know skeptical hypotheses are false (counterintuitive); (2) accept closure + accept that we can't know skeptical hypotheses are false → must deny ordinary knowledge (skepticism); (3) deny closure → can hold ordinary knowledge + cannot know skeptical hypotheses are false, but must explain why a seemingly obvious logical principle fails. Every response sacrifices something: either the denial of skeptical hypotheses, ordinary knowledge, or closure itself."
  explanation: "This trilemma is what makes deductive closure philosophically important rather than merely technical. It shows that three prima facie plausible commitments — closure, common-sense knowledge, and the inexplicability of skeptical scenarios — are jointly inconsistent. Any adequate epistemology must resolve the tension, and the different schools (closure-deniers like Nozick, contextualists like Cohen, common-sense epistemologists like Moore) each pay a different price for their resolution."
```

## Explainer

From your study of epistemic closure, you have the basic principle in hand: knowledge can "close" under certain operations. **Deductive closure** makes this precise for the operation of known entailment. The principle says: if you know P, and you know that P entails Q, then you know Q. This seems almost trivially obvious — how could you know a fact and know what follows from it, yet fail to know what follows? If you know the bank is open on Saturday, and you know that "the bank is open on Saturday" entails "the bank is open on some day this weekend," surely you know the bank is open some day this weekend.

The trouble begins when you apply the principle to **skeptical scenarios**. Here is the standard puzzle. You believe — and seem to know — that you are sitting in a room reading. You also know that "I am sitting in a room reading" entails "I am not a brain in a vat being fed experiences of sitting and reading." By closure, you therefore know that you are not a brain in a vat. But wait: do you actually know that? The whole point of the skeptical scenario is that if you were a brain in a vat, everything would look exactly the same to you. Your evidence does not distinguish between the two situations. Many philosophers, following Descartes, have the strong intuition that you *cannot* know you are not a brain in a vat. But if closure is true, and you *do* know ordinary things, then you must know the skeptical hypothesis is false. Something has to give.

This generates three main responses. **Skeptics** accept closure and deny that you know ordinary propositions: since you can't know you're not a brain in a vat, you can't know much of anything. **Closure deniers** (like Dretske and Nozick) reject the closure principle itself — they argue that knowledge requires that your belief *track* the truth in the actual world, and ordinary beliefs can track truth without your belief-forming process being sensitive to exotic skeptical scenarios. On this view, you can know your car is in the driveway without being able to rule out every far-fetched alternative. **Contextualists** take yet another path: they argue that the word "know" is context-sensitive, and in ordinary conversational contexts the standards are low enough that you know everyday facts, but in skeptical philosophical contexts the standards rise and you no longer "know" anything. None of these responses is without cost, which is what makes deductive closure one of epistemology's central pressure points: it forces you to choose between closure, common-sense knowledge, and the intelligibility of skepticism.
