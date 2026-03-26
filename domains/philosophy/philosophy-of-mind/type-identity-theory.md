---
id: type-identity-theory
title: Type Identity Theory
domain: philosophy
course: philosophy-of-mind
prerequisites:
- id: identity-theory
  type: hard
- id: physicalism-about-mind
  type: hard
- id: token-identity-theory
  type: soft
builds-toward:
- token-identity-theory
- multiple-realizability
tags:
- identity
- physicalism
- mental-states
- ontology
stage: formal-systems
status: validated
---
# Type Identity Theory

## Core Idea
Type identity theory claims that mental state types are identical to physical state types—pain is literally C-fiber stimulation, not just correlated with it. This stronger claim differs from token identity, which allows individual instances of pain to be realized in different physical systems.

## How It's Best Learned
Start with specific examples (pain as C-fiber firing) and compare to token identity to see the difference. Then consider cases where type identity seems to break down across different species.

## Common Misconceptions
Thinking type identity is the same as token identity; confusing neural correlates with identity; assuming that if type identity fails, all physicalism fails.

## Questions

```yaml
- question: "Pain in humans involves C-fibers, pain in octopuses involves entirely different neural structures, and a hypothetical Martian experiences pain through hydraulic pressure networks. What does this show about type identity theory?"
  type: multiple-choice
  options:
    - "It supports type identity theory, since each species has its own distinct pain type"
    - "It is irrelevant, since type identity theory was only ever claimed to apply to human minds"
    - "It refutes type identity theory: if pain-the-type = C-fiber-stimulation-the-type, then octopus and Martian pain would be definitionally impossible — but that seems clearly wrong"
    - "It shows that all forms of physicalism about the mind are false"
  answer: 2
  explanation: "This is Hilary Putnam's multiple realizability objection, the standard refutation of type identity theory. If pain is identical to C-fiber stimulation at the type level, then anything without C-fibers cannot have pain by definition. But octopuses, Martians, and presumably silicon-based systems could all be in functional states that play the same causal role as pain — caused by tissue damage, producing avoidance behavior — without sharing the same physical substrate. Type identity theory predicts this is impossible; multiple realizability shows it is plausible. Option A misunderstands the theory: type identity says there is one physical type for one mental type, not one per species. Option D is the critical error to avoid — multiple realizability defeats type identity but leaves token identity and functionalism intact."

- question: "Which correctly states the difference between type identity theory and token identity theory?"
  type: multiple-choice
  options:
    - "Type identity says mental events are caused by brain events; token identity says they are identical to brain events"
    - "Type identity says individual mental event instances are physical; token identity makes no claims about individuals"
    - "Type identity says the category 'pain' is identical to the category 'C-fiber stimulation'; token identity says each individual instance of pain is identical to some physical event, but different instances can be physically different"
    - "Type identity and token identity are the same position described at different levels of abstraction"
  answer: 2
  explanation: "The type/token distinction is the critical one. A *type* is a category (the mental state kind 'pain'); a *token* is a particular instance of that category (this episode of pain happening right now in this person). Type identity makes the stronger claim: the entire category pain = the entire category C-fiber stimulation, so every token of pain must be a token of C-fiber stimulation. Token identity makes only the weaker claim: each individual mental event token is identical to some physical event token — but different tokens of the same mental type can correspond to different physical types. Token identity is compatible with multiple realizability; type identity is not."

- question: "Hilary Putnam's multiple realizability objection targets type identity theory specifically — not token identity or functionalism."
  type: true-false
  answer: true
  explanation: "Multiple realizability directly challenges the type-level identification. If pain-the-type = C-fiber-stimulation-the-type, then any creature without C-fibers cannot have pain — but this seems to wrongly exclude octopuses, Martians, and future AI. Token identity avoids this: each individual pain token is some physical token, but different creatures' pain tokens can be physically different. Functionalism avoids it differently: pain is identified with a functional role (caused by tissue damage, produces avoidance) that can be realized by different physical systems. The multiple realizability objection is specifically lethal to the type-level identification, not to physicalism as such."

- question: "If type identity theory is false, then physicalism about the mind should also be false."
  type: true-false
  answer: false
  explanation: "This is the critical error to avoid. Type identity theory is the strongest, most specific physicalist claim — that mental types are identical to physical types. Its falsity leaves many other physicalist positions untouched. Token identity theory (each mental event token = some physical event token) is compatible with multiple realizability and remains viable. Functionalism identifies mental states with functional roles rather than specific physical substrates — also a physicalist position, also compatible with multiple realizability. Type identity theory's failure narrows the physicalist's options but doesn't foreclose them."

- question: "Explain in your own words why multiple realizability is a problem for type identity theory but not necessarily for token identity theory."
  type: short-answer
  answer: "Type identity theory claims that pain-as-a-category is identical to C-fiber-stimulation-as-a-category. If true, every instance of pain everywhere must be an instance of C-fiber stimulation. Multiple realizability shows that pain-like states can be realized by different physical systems (neurons in humans, different neurons in octopuses, hydraulics in Martians), making the type-level equation untenable. Token identity only claims that each individual pain event is some physical event — it doesn't say which physical type. Different tokens of 'pain' can correspond to different physical types, so multiple realizability poses no threat to token identity."
  explanation: "The key is the difference between 'all tokens of mental type M must be tokens of physical type P' (type identity, blocked by multiple realizability) and 'each token of M is identical to some physical token' (token identity, compatible with different tokens being different physical types). Type identity requires a fixed physical correlate for each mental category; token identity doesn't. Understanding this distinction is essential for understanding why multiple realizability is a targeted objection, not a wholesale refutation of physicalism."
```

## Explainer

You already know from identity theory and physicalism-about-mind that physicalists want to explain mental phenomena in physical terms. Type identity theory makes the boldest possible version of that claim: mental state *types* — the categories we use (pain, belief, desire) — are literally identical to physical state types. Not just correlated with them, not just realized by them, but *the same thing*. Pain doesn't just happen to involve C-fiber stimulation; pain *is* C-fiber stimulation, in the same way that water *is* H₂O.

The **type/token distinction** is crucial here. A *type* is a category (the word "cat"). A *token* is a particular instance of that category (this printed instance of "cat"). Token identity theory says each individual mental event is identical to some physical event, but different tokens of the same mental type can correspond to different physical types. Type identity goes further: it says pain-the-type is identical to C-fiber-stimulation-the-type, so every token of pain must be a token of C-fiber stimulation. This makes type identity a much stronger and riskier claim.

The standard objection, which you can appreciate given your understanding of physicalism, is **multiple realizability**. Consider that pain in a human involves C-fibers, pain in an octopus involves different neural structures, and a Martian might experience pain through hydraulic pressure networks. If pain-the-type = C-fiber-stimulation-the-type, then octopus pain and Martian pain would be impossible by definition — they don't have C-fibers. But that seems wrong. Pain seems to be a functional state (something that plays a certain causal role: caused by tissue damage, causing avoidance behavior) rather than a specific physical substrate.

This is why multiple realizability, developed by Hilary Putnam, is widely seen as refuting type identity theory. But notice what doesn't follow: that *all* physicalism fails. Token identity remains available. So does functionalism, which identifies mental states with their functional roles rather than specific physical realizers. Type identity theory thus serves as an important foil — understanding exactly where it goes wrong illuminates what a more defensible physicalism must look like, and why the mind-body problem cannot be dissolved by a simple identification of mental categories with neural categories.
