---
id: token-identity-theory-details
title: Token Identity and Physical Realizability
domain: philosophy
course: philosophy-of-mind
prerequisites:
- id: type-identity-theory
  type: hard
- id: multiple-realizability
  type: soft
builds-toward:
- substrate-independence-realization
tags:
- token-identity
- particulars
- realizability
stage: formal-systems
status: validated
---

# Token Identity and Physical Realizability

## Core Idea
Token identity theory holds that individual mental events are identical to individual physical events, even if mental types are not identical to physical types. This allows multiple realizability: the same mental type could be realized by different physical types in different creatures or systems.

## Questions

```yaml
- question: "A human feels pain. An octopus feels pain. A silicon robot (hypothetically) feels pain. Token identity theory says:"
  type: multiple-choice
  options:
    - "All three pains are identical to the same physical type (C-fiber firing), since pain is pain"
    - "Only the human pain is a physical event; the others are non-physical because they lack neurons"
    - "Each individual pain event is identical to some physical event in that system, but the physical types across systems may differ entirely"
    - "Pain cannot exist in non-biological systems, since token identity is limited to organisms with nervous systems"
  answer: 2
  explanation: "Token identity theory holds that each individual mental event token is identical to some physical event token, but does not require that all tokens of the same mental type (pain) be realized by the same physical type. The human's pain token is identical to some neural event; the octopus's pain token is identical to a completely different neural event using different architecture; the robot's pain token is identical to some computational state. What they all share is being physical events — not being physical events of the same kind. This is exactly the modification token identity makes over type identity to accommodate multiple realizability."

- question: "What is the key difference between type identity theory and token identity theory?"
  type: multiple-choice
  options:
    - "Type identity holds that mental events are physical; token identity denies that any mental events are physical"
    - "Type identity claims every mental KIND maps to a physical KIND; token identity claims every mental INSTANCE maps to some physical instance, but different instances of the same mental kind can be realized by different physical kinds"
    - "Token identity applies only to beliefs and desires; type identity covers all mental states"
    - "Type identity is compatible with multiple realizability; token identity is not"
  answer: 1
  explanation: "Type identity theory (e.g., pain = C-fiber firing as a general law) requires all tokens of a mental type to share a physical type. Multiple realizability refutes this because pain is realized by completely different physical mechanisms in different creatures. Token identity retreats to the claim that each individual mental event is identical to some physical event, without requiring the physical types to match across tokens. This preserves physicalism (every mental particular is a physical particular) while allowing the physical realization to vary. Reversing option D: type identity is NOT compatible with multiple realizability; token identity IS."

- question: "Token identity theory is compatible with the claim that a human and an octopus both experience pain even though their pain-realizing physical states share no physical properties."
  type: true-false
  answer: true
  explanation: "Token identity theory requires only that each individual pain event be identical to some physical event — not that all pain events share any physical property. The human's pain token is a neural event; the octopus's pain token is a different neural event using different neurotransmitters, different neural architecture, and different physical properties. They are both physical events, but they need have nothing physical in common beyond being physical. This is the theoretical advantage over type identity, which would require both pains to instantiate the same physical type."

- question: "Token identity theory implies that most instances of pain share some underlying physical property that makes them most count as pains."
  type: true-false
  answer: false
  explanation: "This is what type identity theory claims, not token identity theory. Token identity permits that every pain token is a physical event, without positing any common physical type across them. What unifies pains as pains, on the token identity view, is their functional role — what causes them and what they cause — not their physical constitution. This is why token identity naturally supports functionalism: the mental kind 'pain' is defined by its causal-functional role, and that role can be multiply realized in physically diverse substrates."

- question: "Explain why token identity theory counts as a form of physicalism even though it denies that mental types reduce to physical types."
  type: short-answer
  answer: "Token identity theory holds that every individual mental event is identical to some individual physical event — nothing mental occurs without a corresponding physical occurrence. This satisfies the core physicalist commitment: there is no 'extra' non-physical stuff. Mental events are physical events, described under different concepts. The denial is only of type-type reduction: mental kinds (pain, belief, desire) do not map onto physical kinds by law-like psychophysical regularities. But every token of every mental kind is still a physical token. This is called non-reductive physicalism — physical at the level of particulars, not reducible at the level of kinds."
  explanation: "The distinction between reductive and non-reductive physicalism matters because it determines what follows for cognitive science: if type identity held, neuroscience could in principle replace psychology entirely (each mental type just is a brain type). On token identity, psychology describes patterns (functional roles) that have no purely physical description — the science of mind is irreducible even though the mind is fully physical."
```

## Explainer

To understand token identity theory, you first need the type/token distinction from your prerequisite. A **type** is a general kind or pattern; a **token** is a specific instance of that kind. The word "cat" appears three times in this sentence: that's three *tokens* of one *type*. Applied to mental states: pain as a *type* is the general category; this particular pain I'm feeling right now is a *token* — a specific, dated mental event.

**Type identity theory** — your prerequisite — made the bold claim that mental types are identical to physical types: pain (as a kind) = C-fiber firing (as a kind). Every pain, anywhere, in any creature, would have to be realized by C-fiber firing. You know from **multiple realizability** why this fails: an octopus feels pain with completely different neural architecture; a silicon robot might experience pain with no neurons at all. The same mental type appears in wildly different physical substrates, so type-type identity is too rigid.

**Token identity theory** retreats to a more defensible position: each individual mental event is identical to some individual physical event, but the physical realizer can vary. *My* pain at 3pm on Tuesday is identical to *some specific neural event* in my brain — perhaps this particular C-fiber activation, or this pattern of distributed cortical activity. Your pain at a different time is identical to a different neural event. An octopus's pain is identical to yet another physical event, using entirely different biological hardware. There is no single physical type that all pains share; but every pain *token* is a physical event.

This move preserves **physicalism** — nothing mental happens without something physical happening — while respecting multiple realizability. It's a form of **non-reductive physicalism**: mental types don't reduce to physical types (no psychophysical type-type laws), but every mental particular is a physical particular. The mental and physical descriptions pick out the same events under different concepts. Token identity naturally underpins **functionalism**: what makes something a pain isn't its physical constitution but its functional role — what causes it, what it causes — and that role can be physically realized in multiple ways. This sets up the broader question of substrate independence: if token identity holds, could a sufficiently organized computer token the same mental events as a brain?
