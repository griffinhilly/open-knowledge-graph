---
id: indexical-contextualism-epistemology
title: Contextualism as Indexicalism in Epistemology
domain: philosophy
course: epistemology
prerequisites:
- id: contextualism-in-epistemology
  type: hard
- id: indexicals-context-sensitivity
  type: hard
- id: contextualism-content-sensitivity
  type: soft
- id: relevant-alternatives-semantics
  type: soft
builds-toward:
- margin-error-semantics
tags:
- contextualism
- indexicals
- knowledge
- semantics
- pragmatics
stage: formal-systems
status: validated
---
# Contextualism as Indexicalism in Epistemology

## Core Idea
Contextualism treats knowledge ascriptions as context-indexed: the truth value of 'S knows that P' depends on standards of knowledge relevant in the speaker's context, not the subject's context. Knowledge-denials and knowledge-attributions can both be true when different conversational standards are operative, explaining apparent disagreements about knowledge without relativism.

## Questions

```yaml
- question: "A philosopher in a seminar raises skeptical possibilities about Hannah's car, then says 'Hannah doesn't know her car is in the lot.' Hannah's friend, outside the seminar, says 'Of course Hannah knows where her car is.' According to indexical contextualism, which of the following is correct?"
  type: multiple-choice
  options:
    - "Hannah's friend is simply wrong — the philosopher's higher standards are objectively correct and override ordinary claims"
    - "Both are making errors because knowledge is an all-or-nothing matter unaffected by conversational context"
    - "Both utterances can be true simultaneously, because 'knows' picks up different epistemic standards from each speaker's context"
    - "The dispute is merely verbal and has no substantive content about Hannah's epistemic state"
  answer: 2
  explanation: "The indexical contextualist's key move is that 'knows' shifts its standard with the speaker's context, just as 'I' shifts its referent. In the philosophical seminar, high standards are operative; outside it, low standards are operative. Each speaker's utterance is evaluated against their own context — both can be true because they express different propositions. This explains apparent disagreement without ruling anyone wrong and without collapsing into relativism."

- question: "What is the crucial feature that makes indexical contextualism specifically *indexical* rather than merely a form of relativism about knowledge?"
  type: multiple-choice
  options:
    - "Indexical contextualism holds that knowledge claims are always false, since standards vary"
    - "Indexical contextualism preserves objective truth conditions for each context — the sentence expresses a fixed proposition in each context, with a determinate truth value"
    - "Indexical contextualism holds that the subject's context, not the speaker's, determines the knowledge standard"
    - "Indexical contextualism avoids relativism by denying that context affects the meaning of 'knows'"
  answer: 1
  explanation: "The indexical model preserves objectivity: in context C1, 'S knows P' expresses the determinate proposition 'S meets standard-1 for P' — which is either true or false. In context C2, it expresses a different proposition — also with a fixed truth value. What varies is which proposition is expressed, not whether propositions have truth values. Simple relativism would say truth itself varies with context; indexical contextualism says which proposition is expressed varies, while each proposition has objective truth conditions."

- question: "On the indexical contextualist view, the truth of 'S knows that P' is determined by the epistemic standards operative in the *speaker's* context, not the subject's context."
  type: true-false
  answer: true
  explanation: "This is the defining structural feature of indexical contextualism. Just as 'I' refers to whoever is speaking (not whoever is being discussed), 'knows' picks up standards from the conversational context of the attributor. When you say 'Hannah knows X,' your context — your current conversational standards — determines whether that attribution is true, not Hannah's situation. This is what enables the dissolution of skeptical puzzles: the skeptic operates in a high-standard context; ordinary speakers operate in a low-standard context."

- question: "Indexical contextualism is a form of relativism because whether 'S knows P' is true depends on who is speaking, making truth relative to individuals."
  type: true-false
  answer: false
  explanation: "Indexical contextualism is specifically designed to avoid relativism. On the indexical model, 'S knows P' expresses a fully determinate proposition in any given context — one with a fixed, objective truth value. What differs across contexts is which proposition gets expressed. Compare: 'I am here' is not relativistic — it expresses a specific, objectively true or false proposition whenever uttered. The truth-conditions are context-indexed, but each indexed proposition is either true or false without further qualification."

- question: "Why does the indexical contextualist locate the relevant epistemic standards in the *speaker's* context rather than the *subject's* context? What problem would arise if it were the subject's context instead?"
  type: short-answer
  answer: "If standards were fixed by the subject's context, then raising skeptical possibilities in a seminar would never produce true knowledge-denials — because the subject (Hannah) is not in the seminar and her context remains unchanged. The skeptic's argument would always fail as a conversation-starter, which seems wrong: philosophers can genuinely shift what it takes to count as knowledge by introducing new considerations. Locating standards in the speaker's context also matches the indexical parallel: 'I' refers to the speaker, not the person being discussed."
  explanation: "Subject-sensitive invariantism (a competitor view) does locate standards partly in the subject's context — specifically in what's at stake for the subject. The debate between these views is active. Contextualism's advantage is that it explains why the same knowledge claim sounds true to Hannah's friend and false to the philosopher, without requiring that Hannah's epistemic situation has actually changed during the seminar."
```

## Explainer

You know from your work on **indexicals** that some expressions get their reference fixed by the context of utterance rather than by a fixed meaning. "I" always refers to the speaker; "here" always refers to the location of utterance; "now" always refers to the time of utterance. The expression is constant but its referent shifts with who speaks, where, and when. **Indexical contextualism** applies exactly this model to knowledge ascriptions: "knows" is treated as a kind of indexical whose semantic content — specifically, the standard of justification it invokes — shifts with the context of the person doing the attributing.

The key move is locating the relevant context in the **speaker**, not the **subject**. When someone says "S knows that P," the truth of that statement is determined by the epistemic standards operative in the *speaker's* conversational context, not by the standards S herself is subject to. This is the indexical parallel: just as "I" refers to the speaker rather than to the person being discussed, "knows" picks up standards from the attributor's context rather than from the subject's. Suppose you're in a casual conversation and I say "Hannah knows her car is in the lot." That claim is evaluated against my current context — probably low standards, since nothing is at stake. If a philosopher enters and raises far-fetched possibilities (maybe the car was towed in the last five minutes), the context shifts, the standards rise, and now the very same sentence, spoken by me in this new context, may express a falsehood.

This framework dissolves a puzzling asymmetry in skeptical arguments. The skeptic seems to prove that nobody ever knows anything, which contradicts our ordinary practice of attributing knowledge constantly. The indexical contextualist says: both are right, but in different contexts. The skeptic's arguments succeed in raising the epistemic standards within the philosophical discussion to a level at which ordinary beliefs fail. Outside that discussion, those extreme standards aren't in play. There is no contradiction — just two utterances of "knows" in contexts that fix different standards, the way "I am here" is true when you say it and false when I say it.

What makes this specifically **indexical** (rather than merely relativist) is that the truth conditions are still objective. The sentence "S knows that P" has a determinate truth value in every context — it is not vague or subjective. What varies is which proposition the sentence expresses. In context C1, "S knows that P" expresses the proposition that S meets standard-1 for P; in context C2 it expresses the proposition that S meets standard-2. Both propositions have fixed truth values. This lets the contextualist preserve the idea that knowledge claims are genuinely true or false — a significant advantage over simpler forms of relativism that make truth context-dependent rather than context-indexed.
