---
id: a-theory-b-theory-of-time
title: A-Theory and B-Theory of Time
domain: philosophy
course: metaphysics
prerequisites:
- id: philosophy-of-time
  type: hard
- id: temporal-logic
  type: soft
tags:
- A-theory
- B-theory
- presentism
- eternalism
- growing block
- temporal ontology
stage: formal-systems
status: validated
---

# A-Theory and B-Theory of Time

## Core Idea
A-theories (dynamic theories) hold that temporal distinctions of past, present, and future are fundamental and objective, and that time genuinely passes — events become present and then recede into the past. Presentism (only the present exists) and the growing block (past and present exist, future does not) are major A-theory variants. B-theories (static theories) hold that all times exist equally in a four-dimensional spacetime manifold, and the only genuine temporal relations are tenseless earlier-than/later-than; 'now' is an indexical like 'here' with no ontologically privileged status. The debate turns on arguments from special relativity, the experience of temporal passage, and the truthmakers for tensed statements.

## How It's Best Learned
Read Sider's Four-Dimensionalism Chapter 2 for the B-theory and Crisp's 'Presentism' for the A-theory. Evaluate the Einstein/relativity argument against presentism: does the relativity of simultaneity refute it, or can presenters relativize the present to a reference frame?

## Common Misconceptions
- B-theorists do not say that nothing changes; they analyze change as difference in properties between temporal stages.
- The phenomenology of temporal passage (things seeming to flow) is data for both sides — A-theorists say it's veridical, B-theorists say it requires explanation as an appearance.

## Questions

```yaml
- question: "Special relativity shows that whether two events are simultaneous depends on the observer's reference frame — there is no frame-independent 'happening now.' Which philosophical view does this most directly challenge?"
  type: multiple-choice
  options:
    - "B-theory, because it relies on fixed tenseless relations like 'earlier than'"
    - "A-theory (particularly presentism), because it requires an objective universal 'now' that relativity denies"
    - "Both equally, since relativity eliminates all temporal distinctions"
    - "Neither — relativity is a physical theory with no implications for metaphysics of time"
  answer: 1
  explanation: "A-theory — especially presentism (only the present exists) — requires an objective, universal present moment. But special relativity eliminates absolute simultaneity: two events can be simultaneous in one frame and non-simultaneous in another, with no frame being privileged. There is no observer-independent fact about 'what exists now,' which is exactly what presentism requires. B-theory is untroubled because it treats 'now' as a mere indexical and all times as equally real in a four-dimensional manifold — there is no privileged present to threaten."

- question: "On the B-theory of time, how is 'change' analyzed?"
  type: multiple-choice
  options:
    - "Change is illusory — in a static block universe, nothing genuinely changes"
    - "Change consists in an object having different properties at different times, understood as differences between its temporal stages"
    - "Change requires an objective flow of time from past to future"
    - "Change is reducible to the subjective experience of temporal passage, not a feature of the world"
  answer: 1
  explanation: "B-theorists do not deny that change occurs — they analyze it differently. Change is the fact that an object has different properties at different times: 'the leaf was green in July and is brown in October' is true just in case the leaf's temporal stage at July has the property green and its stage at October has the property brown. No temporal flow is needed — only the four-dimensional manifold with tenseless earlier-than relations. This refutes the misconception that B-theorists claim nothing changes."

- question: "B-theorists claim that hardly anything genuinely changes because they hold that most times exist equally in a static four-dimensional block."
  type: true-false
  answer: false
  explanation: "This is the most common mischaracterization of B-theory. B-theorists do analyze change: they understand it as an object having different properties at different times (or across temporal stages), without requiring an objective flow of time. The block universe view says that change is tenseless temporal variation in properties, not the passage of a privileged present. B-theorists accept all ordinary facts about change; they just don't think those facts require genuine temporal becoming."

- question: "On the B-theory, 'now' functions as an indexical — like 'here' — referring to whatever time the utterance is produced, with no special ontological priority over other times."
  type: true-false
  answer: true
  explanation: "This is a central B-theory claim. Just as 'here' refers to the speaker's spatial location without that location being metaphysically privileged, 'now' refers to the time of utterance without that time being ontologically privileged. The present is not 'more real' than past or future; it is just the temporal location of the current speaker. This contrasts with A-theory, which holds that the present is the genuinely existing, objectively distinguished moment."

- question: "What is the 'truthmaker problem' for presentism, and why does it pose a philosophical difficulty?"
  type: short-answer
  answer: "Presentism holds that only the present exists. The truthmaker problem asks: if past entities no longer exist, what makes past-tensed statements like 'Caesar was murdered' true right now? Truth requires truthmakers — entities in the world that ground the truth of propositions. But on presentism, Caesar, the senators, and all events of 44 BCE are gone. There is nothing currently existing to serve as the truthmaker for that claim. Proposed solutions include abstract ersatz past times or primitive temporal operators, but each faces objections about what these substitutes are and how they ground truth."
  explanation: "B-theorists avoid this problem entirely: for them, Caesar and the assassination exist timelessly at their temporal location in the four-dimensional manifold, serving as truthmakers for past-tensed claims just as present entities ground present-tensed ones. The truthmaker problem reveals a tension at the core of presentism between the intuitive view that only now is real and the equally intuitive truth of historical claims."
```

## Explainer

The A-theory/B-theory distinction is about what is metaphysically fundamental in our description of time. Ordinary temporal language includes two very different kinds of expression: **tense** (past, present, future) and **relational order** (earlier than, simultaneous with, later than). The debate is about which of these is more fundamental — or whether one can be reduced to the other. From your study of philosophy of time, you know that time is not obviously simple; the A/B debate sharpens that intuition into a precise philosophical question.

**B-theory** (the static, tenseless view) holds that all genuine temporal facts are relational: events are ordered by earlier-than/later-than, and this is the complete story. The word "now" is an **indexical** — it refers to whatever time the utterance is made, just as "here" refers to the speaker's location. There is nothing metaphysically special about the present moment; it is simply the time of this utterance. All times exist equally in a four-dimensional spacetime block. What we experience as "temporal passage" — the felt sense that time flows — is a feature of how we experience time, not a feature of time itself. B-theory finds natural support in special relativity: since the theory eliminates absolute simultaneity (two events can be simultaneous in one frame and non-simultaneous in another), "the present" cannot be a frame-independent objective feature of reality.

**A-theory** (the dynamic view) insists that the distinction between past, present, and future is genuine and metaphysically fundamental — not reducible to mere relational ordering. The world has a dynamic structure: events are first future, then present, then past. "Now" doesn't just pick out a time indexically; the present is the ontologically privileged moment. This intuition is hard to resist phenomenologically: the future feels genuinely open, the present feels vivid and immediate, and the past feels fixed. A-theorists argue that the phenomenology of temporal passage is **veridical** — it accurately reflects a real feature of the world. **Presentism** (only the present exists) and the **growing block** (past and present exist; future does not) are the major A-theory variants.

The debate crystallizes around concrete puzzles that connect to your temporal logic background. For the B-theorist: how do we formalize A-theoretic language without smuggling in absolute simultaneity? For the A-theorist: what are the **truthmakers** for past-tensed statements? If "Caesar was murdered" is true now, what in the world makes it true? The presentist says only present entities exist — Caesar doesn't exist — yet we make apparently true claims about him. Proposed solutions include **ersatz past times** (abstract objects representing past states) or primitive temporal operators that don't require past entities to exist. Neither is free of cost. These pressures make the A/B debate one of the most technically demanding and metaphysically consequential in contemporary philosophy.

