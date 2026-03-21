---
id: reductive-physicalism-theory
title: Reductive Physicalism and Mental Reduction
domain: philosophy
course: philosophy-of-mind
prerequisites:
- id: physicalism-reduction-commitment
  type: hard
builds-toward:
- type-identity-theory-details
tags:
- reduction
- type-identity
- reductionism
stage: formal-systems
status: draft
---

# Reductive Physicalism and Mental Reduction

## Core Idea
Reductive physicalism holds that mental properties can be identified with or reduced to physical properties, particularly neural properties. This view connects philosophy of mind to scientific reduction, treating the mental-physical relationship as analogous to other inter-theoretic reductions like water-H2O.

## Questions

```yaml
- question: "According to the multiple realizability argument, why does pain in humans, octopuses, and Martians pose a problem for type identity theory?"
  type: multiple-choice
  options:
    - "Because pain feels different to each creature, so 'pain' refers to multiple subjective states"
    - "Because the physical basis of pain differs across creatures, so no single physical type corresponds to the mental type 'pain'"
    - "Because Martians are hypothetical and philosophy should not use fictional examples"
    - "Because type identity theory only applies to human psychology, not animal pain"
  answer: 1
  explanation: "Type identity requires a one-to-one mapping between mental types and physical types. If 'pain' picks out one mental type but is realized by different physical states in different creatures (C-fiber firing in humans, something different in octopuses), then there is no single physical type that pain can be *identical to*. Multiple realizability breaks the mapping, which is why it pushed many physicalists away from reductive physicalism toward non-reductive alternatives."

- question: "The water-H₂O identity is the model for reductive physicalism. Which aspect of this identity does reductive physicalism aim to replicate for mental states?"
  type: multiple-choice
  options:
    - "That water and H₂O are causally related — water causes H₂O to form"
    - "That water supervenes on H₂O — every H₂O molecule is accompanied by water"
    - "That 'water' is identical to H₂O — the folk concept reduces to the chemical description, so there are not two things but one"
    - "That H₂O is more real than water, so water should be eliminated from scientific vocabulary"
  answer: 2
  explanation: "The water-H₂O case is an identity, not merely a causal or supervenience relation. We don't say water *causes* H₂O or merely *accompanies* it — we say they are the *same thing* at different levels of description. Reductive physicalism wants the same for mental states: 'pain' is not something that causes C-fiber firing or merely accompanies it — it *is* C-fiber firing, described in folk terms. Options A (causation) and B (supervenience) describe weaker relations that non-reductive physicalism accepts."

- question: "Token identity theory is a form of reductive physicalism because it claims that mental types can be reduced to physical types."
  type: true-false
  answer: false
  explanation: "Token identity theory is *weaker* than reductive physicalism — it only claims that each individual mental event (token) is identical to some physical event, not that mental *types* map onto physical types. Reductive physicalism requires type identity: pain-as-a-type must be identical to some specific neural type. Token identity allows each instance of pain to be realized differently in different creatures, so no systematic reduction of mental vocabulary to physical vocabulary is possible."

- question: "Reductive physicalism and non-reductive physicalism agree that mental properties supervene on physical properties — the disagreement is about whether mental properties are also *identical to* physical properties."
  type: true-false
  answer: true
  explanation: "Supervenience — no mental difference without a physical difference — is accepted by both views. What separates them is the stronger claim of identity: reductive physicalism says mental properties ARE physical properties (type identity), while non-reductive physicalism says they merely depend on physical properties without being identical to any single physical type. Multiple realizability is standardly taken to show that supervenience holds without type identity."

- question: "What is the multiple realizability argument against type identity theory, and why is it considered the most powerful challenge to reductive physicalism?"
  type: short-answer
  answer: "The argument observes that a single mental type (e.g., pain) can be physically realized by different structures in different organisms — C-fiber firing in humans, but perhaps different physical states in octopuses or Martians. If pain is multiply realizable, it cannot be identical to any single physical type, because identity requires a one-to-one correspondence. Type identity claims mental types = physical types; multiple realizability shows the mapping is many-to-one, so the mental vocabulary cannot be systematically reduced to the physical vocabulary."
  explanation: "The argument is powerful because it targets the logical structure of reduction itself. Even if we discovered the exact neural correlate of pain in humans, that discovery wouldn't tell us what pain is in an octopus — suggesting 'pain' picks out a functional or dispositional property that can be variously instantiated. This opened the door to functionalism, which identifies mental states by their causal roles rather than their physical substrates, and to non-reductive physicalism, which accepts supervenience without type identity."
```

## Explainer

You already know the core commitment of physicalism: that everything that exists is physical or depends entirely on the physical. **Reductive physicalism** takes this a step further. It doesn't just say that mental events depend on physical events — it says that mental properties *just are* physical properties, and that the mental vocabulary can, in principle, be reduced to the physical vocabulary in the way that chemistry reduces to physics.

The paradigm case of scientific reduction gives the model. Water, described in folk terms as a colorless liquid that fills rivers and quenches thirst, is identical to H₂O, described chemically. Once we discovered this identity, we didn't say there were two things (water and H₂O) that causally interact — we said they are the same thing described at different levels. The folk concept "water" was retained but explained: what makes something water is that it is H₂O. Reductive physicalists claim the same structure applies to the mind. The mental term "pain" picks out some neural state — perhaps C-fiber firing, or some functional-neural state — and the goal is to identify which one.

This is the program of **type identity theory**: mental *types* (pain, belief, desire) are identical to physical *types* (specific neural states or functional states). This contrasts with a weaker view, token identity theory, which only claims each individual mental event is identical to some physical event — not that the mental type as a whole maps onto a physical type. Type identity is reductive in the strong sense: it aims to show that psychological theory can be systematically subsumed under neuroscience, just as thermodynamics was subsumed under statistical mechanics.

The most powerful challenge to this program is the **multiple realizability** argument: pain in humans might involve C-fiber firing, but pain in an octopus or a Martian might be realized by completely different physical structures. If pain can be realized by many different physical types, then "pain" can't be identical to any single physical type — which means mental types resist reduction to physical types. This pushed many physicalists toward non-reductive physicalism, which accepts that mental properties supervene on physical properties without being identical to them.

Reductive physicalists respond in several ways: they can deny that multiple realizability is as widespread as critics claim, narrow the reduction to species-specific identity claims, or argue that what gets reduced is not folk-psychological types but properly scientific psychological types. The debate matters because it determines whether psychology is an autonomous science or ultimately a branch of neuroscience — whether the mental vocabulary earns its keep or will eventually be displaced by better physical descriptions.
