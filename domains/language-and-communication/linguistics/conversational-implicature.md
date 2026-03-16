---
id: conversational-implicature
title: Conversational Implicature
domain: language-and-communication
course: linguistics
prerequisites:
- id: linguistic-pragmatics
  type: hard
- id: speech-act-theory
  type: soft
builds-toward:
- discourse-analysis
tags:
- Grice
- implicature
- maxims
- cooperation
- inference
- cancelability
stage: formal-systems
status: validated
---

# Conversational Implicature

## Core Idea
Grice's theory of conversational implicature explains how listeners routinely infer meanings that go beyond what is literally said. The Cooperative Principle holds that speakers generally make their contributions relevant, truthful, appropriately informative, and clear. When an utterance appears to violate one of Grice's four maxims (Quantity, Quality, Relation, Manner), listeners infer the speaker intends an additional meaning — a conversational implicature. Unlike entailments, implicatures are cancellable: they can be retracted without contradiction.

## How It's Best Learned
Work through classic implicature puzzles: 'Some students passed' implicates 'not all' — but why, and how is it cancellable? Practice distinguishing implicatures from entailments by testing whether the inference survives cancellation and negation.

## Common Misconceptions
- Implicatures are not lies or half-truths; they are rational inferences licensed by the assumption of cooperative communication.
- Not every inference is an implicature — entailments follow logically from sentence meaning regardless of context.
- Maxims are default assumptions about cooperative behavior, not rules that must be followed; flouting them deliberately is a common rhetorical device.

## Questions

```yaml
- question: "A speaker says 'Some of the students passed the exam.' According to Grice, why does this utterance implicate 'not all students passed'?"
  type: multiple-choice
  options:
    - "The word 'some' logically entails 'not all' by its semantic definition"
    - "The maxim of Quantity requires speakers to be as informative as needed; if all had passed, a cooperative speaker would have said so"
    - "The maxim of Quality prohibits making strong claims that might turn out to be false"
    - "The implicature arises because 'some' is ambiguous between 'a few' and 'most'"
  answer: 1
  explanation: "Saying 'some' when you know 'all' would be true violates the maxim of Quantity (be as informative as required). A hearer assumes the speaker is being cooperative, and since 'all' is a stronger and more informative claim, the speaker's choice of 'some' implicates they cannot honestly say 'all.' Note that 'some' does NOT logically entail 'not all' — 'some, and in fact all' is not a contradiction, which is exactly what makes this an implicature rather than an entailment."

- question: "Conversational implicatures are a type of logical entailment because, like entailments, they follow necessarily from the meaning of the sentence."
  type: true-false
  answer: false
  explanation: "The key difference is cancellability. Entailments cannot be retracted without contradiction: 'John's sister arrived, but he has no siblings' is incoherent. Implicatures can be cancelled without contradiction: 'Some students passed — in fact, all of them did' is perfectly coherent. Implicatures arise from reasoning about the speaker's communicative intentions in context, not from the logical content of the words alone."

- question: "What does it mean to say an implicature is 'cancellable,' and why is cancellability the key test for distinguishing implicatures from entailments? Give an example."
  type: short-answer
  answer: "Cancellability means the speaker can explicitly deny the implied meaning without creating a logical contradiction. For example, 'Some students passed — in fact, all of them did' cancels the 'not all' implicature that 'some' normally generates, yet the sentence is entirely coherent. By contrast, entailments cannot be cancelled: 'Mary stopped smoking, but she never smoked' is a contradiction because 'stopped smoking' logically entails prior smoking. Cancellability proves that the 'not all' inference was pragmatic (context-dependent reasoning) rather than semantic (part of the word's logical meaning)."
  explanation: "Cancellability is the diagnostic Grice identified to separate what is said (the literal semantic content, including entailments) from what is implicated (pragmatic inferences defeasible by context). This distinction is foundational for linguistic pragmatics because it explains why the same sentence can communicate very different things in different contexts."
```

## Explainer

You have already studied linguistic pragmatics — the study of how context shapes the interpretation of utterances beyond their literal meaning. Conversational implicature is the most influential single theory within pragmatics, developed by philosopher H. P. Grice in his 1975 paper "Logic and Conversation." It answers a deceptively simple question: how do speakers routinely communicate far more than they literally say?

Grice's starting point is the observation that conversation is not a random sequence of utterances — it is a cooperative activity. Speakers generally try to make their contributions serve the conversational purpose. He called this the Cooperative Principle, and he broke it into four maxims: Quantity (be as informative as required, but not more), Quality (don't say what you believe to be false), Relation (be relevant), and Manner (be clear, brief, and orderly). These are not rules people consciously follow — they are default assumptions listeners bring to any exchange. When a contribution appears to violate one of these maxims, the listener does not conclude the speaker is being incoherent; instead, they infer that the speaker must intend an additional meaning that reconciles the apparent violation. That inferred meaning is a conversational implicature.

The classic example is scalar implicature. If someone asks "Did all the students pass?" and you reply "Some did," you have said something literally true (if at least one student passed). But by choosing "some" rather than "all" — the stronger, more informative claim — you implicate that you cannot truthfully say "all." The listener reasons: if the cooperative speaker could have said "all" and didn't, there must be a reason; the most natural reason is that "all" is false. The implicature ("not all") arises not from the meaning of "some" but from the reasoning about what a cooperative speaker would say. This is why implicatures are pragmatic rather than semantic.

The single most important technical distinction in this theory is between implicatures and entailments. Entailments are logical consequences of what a sentence literally says — they hold in every context and cannot be cancelled without contradiction. Implicatures are defeasible: they can be cancelled without contradiction when context makes the cancellation natural. "Some students passed — in fact, all of them did" is coherent because the first clause is true (all is a subset of all) and the second explicitly cancels the implicature. "John stopped smoking, but he never smoked" is not coherent because "stopped smoking" logically entails prior smoking, and you cannot cancel an entailment. Cancellability is the diagnostic test.

A further insight from Grice is that maxims can be deliberately flouted — openly violated in a way the listener is expected to notice — to generate implicatures through irony, understatement, or rhetorical effect. When someone says "Oh yes, he's a brilliant scholar" about a notoriously incompetent colleague, the obvious violation of Quality (saying something you don't believe) signals irony; the listener infers the opposite of what was said. Understanding implicature thus explains not just ordinary conversation but the mechanics of sarcasm, politeness, hedging, and rhetorical indirection that characterize sophisticated language use.
