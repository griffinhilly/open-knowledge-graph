---
id: sortal-identity-conditions
title: Sortal Concepts and Identity Conditions
domain: philosophy
course: metaphysics
prerequisites:
- id: universals-and-particulars
  type: hard
- id: substance-and-property
  type: soft
- id: composition-and-simples
  type: soft
builds-toward: []
tags:
- sortals
- identity
- concepts
- ontology
- metaphysics
stage: formal-systems
status: draft
---
# Sortal Concepts and Identity Conditions

## Core Idea
Sortal concepts like 'horse', 'artifact', and 'person' determine identity conditions: what counts as the same horse or person across time. Different sortals impose different identity criteria—a person persists through mental continuity while matter persists through spatiotemporal continuity. Understanding sortals is essential for addressing persistence, material constitution, and the nature of kinds.

## Questions

```yaml
- question: "A ship has all its planks gradually replaced over 20 years. The original planks are then reassembled into a ship elsewhere. Which is the original ship?"
  type: multiple-choice
  options:
    - "The continuously operating ship — it maintained functional and social continuity throughout"
    - "The reassembled ship — identity follows matter, and the original matter defines the original object"
    - "The answer depends on which identity criterion the sortal 'ship' imposes — the puzzle has no sortal-neutral resolution"
    - "Neither is the original ship, because ships cannot persist through material change"
  answer: 2
  explanation: "This is the Ship of Theseus puzzle. Under an artifact sortal with functional/social continuity criteria, the operating ship is the same ship. Under a material constitution criterion, the reassembled ship has the stronger claim. The point is that 'which is the original ship?' cannot be answered without first settling what makes ships the same ship over time — that is, without specifying the identity conditions your sortal imposes. Different criteria yield different verdicts, and neither is automatically correct."

- question: "After severe brain surgery, a person has complete psychological discontinuity — no memories, radically different personality. Applying Locke's psychological continuity criterion for persons versus the biological organism sortal gives which result?"
  type: multiple-choice
  options:
    - "Both sortals agree: this is the same person, because the same body is present"
    - "Both sortals agree: this is a different person, because personality has changed"
    - "Under the 'person' sortal (psychological continuity), it may not be the same person; under 'organism,' it is the same animal"
    - "Sortal analysis is irrelevant — neuroscience settles what counts as the same person"
  answer: 2
  explanation: "The same physical entity can be assessed by different sortals with different verdicts. Under Locke's person sortal (memory and psychological connectedness as the criterion), complete discontinuity means the person may have ceased. Under the biological organism sortal, the same animal persists because bodily continuity is unbroken. This is not a contradiction — it shows that 'same X' is sortal-relative. The question 'Is this the same person?' and 'Is this the same organism?' are different questions with potentially different answers."

- question: "Two different sortals can apply to the same physical entity at the same time and yield different verdicts about whether it has persisted through a change."
  type: true-false
  answer: true
  explanation: "Yes — this is precisely the force of sortal-relative identity. A human being is simultaneously a person and an organism. If that person undergoes complete psychological discontinuity, the 'organism' sortal says continuity is preserved (same biological animal), while the 'person' sortal (on Lockean grounds) says continuity is broken. The physical facts are the same; the identity verdict differs because the sortal determines what counts as persistence."

- question: "Because identity is a logical relation (every thing is identical to itself), the question 'Is this the same X?' always has a determinate, sortal-independent answer."
  type: true-false
  answer: false
  explanation: "Logical identity (a = a) is sortal-independent, but persistence questions — 'Is this the same X across time and change?' — are not. The logical fact that a thing is self-identical doesn't settle whether a changed entity is the same instance of some kind. That question requires criteria for what counts as persistence under that kind, which is exactly what sortals provide. Without specifying the sortal, 'same X' is indeterminate — not because logic fails, but because identity-over-time is a substantive question, not a logical tautology."

- question: "What does it mean to say that identity is 'sortal-relative,' and why does this matter for puzzles like the Ship of Theseus?"
  type: short-answer
  answer: "Saying identity is sortal-relative means that 'Is this the same X?' can only be answered once you specify the kind X — because different kinds impose different criteria for what counts as persistence. For 'ship,' the criterion might be functional/social continuity (favoring the operating ship) or material constitution (favoring the reassembled ship). Neither criterion is built into reality independently of the sortal. The Ship of Theseus puzzle appears paradoxical because we implicitly assume there must be a sortal-neutral fact of the matter, but there isn't — the puzzle dissolves once you recognize that different sortals license different answers."
  explanation: "Sortal-relative identity also explains why identity puzzles in law, personal identity, and metaphysics resist simple resolution: they often involve competing sortals (legal person vs. biological organism, artifact vs. pile of material) without a principled way to adjudicate which sortal takes precedence."
```

## Explainer

When you ask "Is this the same X?" the answer depends entirely on what X is. A **sortal concept** is a concept that classifies things into a kind and, crucially, supplies the conditions under which two things at different times count as the same instance of that kind. "Horse," "club," "river," and "person" are sortals; "red" and "heavy" are not (they describe properties but don't individuate). The philosophical point is that identity is not a bare logical relation — it is always identity *as* something, governed by the sortal under which you're tracking the thing.

You've already studied universals and particulars: particular things are individual instances that exist at specific places and times. The sortal question is what makes a particular the *same* particular across time and change. Consider a ship whose planks are gradually replaced one by one. After all original planks are replaced, is it the same ship? Under the sortal **artifact**, the relevant criterion might be continuity of function and social role — so yes, it's the same ship (the Ship of Theseus). But if the original planks are reassembled elsewhere, which one is the ship? Different theories of artifact identity answer differently. The puzzle is real precisely because sortals are doing the work, and "ship" may not have a perfectly determinate answer.

The contrast between person and body demonstrates how different sortals can apply to the same physical stuff and give different verdicts. Suppose a human being undergoes complete amnesia and psychological discontinuity following brain surgery. Is this the same **person**? Under psychological continuity criteria for persons (Locke's view: personal identity follows memory and psychological connectedness), perhaps not — the person has ceased and a new one begun in the same body. But under bodily or biological criteria for organisms, it's clearly the same human animal. Neither answer is wrong in isolation: they are answers to different questions governed by different sortals. This is what Wiggins meant by saying identity is always sortal-relative.

The deeper point connects to your prerequisite material on composition and simples. A sortal doesn't just track a thing over time — it determines what counts as a thing at all. "Club" picks out an entity constituted by some members and a set of rules; if those members change completely, the club may still exist because club-identity is constituted by institutional facts, not material ones. "River" picks out a process of water flow; the water molecules at any moment are transient, but the river persists as long as the flow continues in that channel. Each sortal carries a hidden theory of what matters for identity. Making that theory explicit is what sortal analysis does — and it reveals that many identity puzzles (Is this the same organization? Is she still the same person after such profound change?) cannot be resolved without first settling what sortal you're asking about.

