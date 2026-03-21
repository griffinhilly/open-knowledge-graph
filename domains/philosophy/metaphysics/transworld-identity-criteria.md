---
id: transworld-identity-criteria
title: Transworld Identity and Identity Across Possible Worlds
domain: philosophy
course: metaphysics
prerequisites:
- id: possible-worlds-semantics
  type: hard
- id: modal-semantics-possible-worlds
  type: hard
- id: rigid-designators-modal-reference
  type: soft
builds-toward:
  - haecceity-primitive-identity
tags:
- modality
- identity
- possible-worlds
- transworld
- essentialism
stage: advanced
status: draft
---
# Transworld Identity and Identity Across Possible Worlds

## Core Idea
Transworld identity concerns what makes a particular object in one possible world the same object in another possible world. The question is which counterpart of an object in world w2 is genuinely that object versus merely similar. This requires criteria for tracking identity across modal space, involving understanding rigidity of designation and essential properties.

## Questions

```yaml
- question: "According to David Lewis's counterpart theory, what does 'Hubert Humphrey might have won the 1968 election' mean?"
  type: multiple-choice
  options:
    - "Humphrey himself exists in another possible world where he wins — the same numerically identical individual"
    - "There is a qualitatively similar but numerically distinct individual in another world — Humphrey's counterpart — who wins"
    - "The actual Humphrey has a disposition or potential to have won, realized in a non-actual scenario"
    - "The sentence is meaningless because Humphrey only exists in the actual world"
  answer: 1
  explanation: "Lewis held that individuals are world-bound — the actual Humphrey exists only in the actual world. Modal claims about Humphrey are really claims about his counterparts: qualitatively similar individuals in other worlds. This preserves ontological clarity (no individual inhabits multiple worlds) but at a cost: Kripke pressed the 'Humphrey objection' — Humphrey cares about winning as a possibility *for himself*, not for some similar but distinct person. Counterpart theory, on this objection, misidentifies what's at stake in first-person modal claims."

- question: "The main philosophical advantage of Lewis's counterpart theory over genuine transworld identity is that it:"
  type: multiple-choice
  options:
    - "Better captures the intuition that modal claims are about the individual themselves, not similar duplicates"
    - "Provides clearer criteria for which properties an individual must have in all worlds versus which it can lack"
    - "Avoids positing that one numerically identical individual literally inhabits multiple possible worlds, preserving ontological clarity"
    - "Is consistent with Kripke's doctrine that proper names rigidly designate the same individual across worlds"
  answer: 2
  explanation: "Lewis's motivation was ontological economy: genuine transworld identity requires making sense of one individual 'being in' or 'having properties across' multiple worlds simultaneously, which is metaphysically puzzling. Counterpart theory replaces this with qualitative similarity relations between distinct world-bound individuals — a cleaner picture. The cost is intuitive: option A names exactly the cost (Kripke's Humphrey objection). Option D is wrong — counterpart theory is in tension with rigid designation, not consistent with it."

- question: "On Lewis's counterpart theory, when we say 'Aristotle might have been a farmer,' we are making a claim about a distinct individual in another possible world who resembles Aristotle in the relevant respects."
  type: true-false
  answer: true
  explanation: "This is exactly counterpart theory. Aristotle exists only in the actual world; the 'Aristotle' in other worlds is a counterpart — numerically distinct but qualitatively similar in the respects that matter for the modal claim. The counterpart relation is context-sensitive: which similarities are 'relevant' depends on what's being discussed. Lewis accepted that this means modal claims about Aristotle are, strictly speaking, about someone else — and he thought the cost was worth the ontological benefits."

- question: "Kripke's doctrine of rigid designation is neutral between counterpart theory and genuine transworld identity — either framework can accommodate the claim that proper names pick out the same object across possible worlds."
  type: true-false
  answer: false
  explanation: "Rigid designation presupposes that there is a single individual — 'Aristotle' — to be designated across worlds. This tacitly commits to genuine transworld identity: the name tracks the same individual in every world where that individual exists. Counterpart theory requires reinterpreting rigid designation as shorthand for counterpart relations: 'Aristotle' in another world refers to Aristotle's counterpart, not Aristotle himself. The two frameworks are in tension, not compatible, which is why Kripke used rigid designation as a wedge against counterpart theory."

- question: "What is the 'Humphrey objection' to Lewis's counterpart theory, and what philosophical intuition does it appeal to?"
  type: short-answer
  answer: "The Humphrey objection (pressed by Kripke) is that counterpart theory makes modal claims about Humphrey into claims about a numerically distinct person who merely resembles him. When Humphrey cares that he might have won the election, he cares about this as a possibility for *himself* — not for some qualitatively similar but numerically different individual in another world. Counterpart theory seems to get the subject wrong. The objection appeals to the intuition that first-person modal concern is essentially about numerical identity: what matters is that it is *me* in the other scenario, not someone similar to me."
  explanation: "This objection motivates the alternative of genuine transworld identity: the view that the very same individual (numerically one and the same) exists in multiple worlds. The problem then shifts to specifying which properties are essential versus accidental — what Aristotle must be in every world versus what he could have lacked. Neither view is unproblematic; the choice involves a genuine philosophical tradeoff."
```

## Explainer

From your study of possible worlds semantics, you can state what it means to say "Aristotle might have been a farmer": there is a possible world in which Aristotle is a farmer. But this raises a question your semantics didn't quite answer: what makes the farmer in that world *Aristotle*, rather than just someone who resembles him? To say there's a world where Aristotle farms is to presuppose that we can track Aristotle across worlds — that there is some fact of the matter about which individual in world w₂ is the same person as the philosopher in the actual world. This is the problem of **transworld identity**, and it turns out to be deeply contested.

One major position is David Lewis's **counterpart theory**. Lewis held that individuals exist only in one possible world — the actual world contains the actual Aristotle, other worlds contain other, numerically distinct individuals. When we say "Aristotle might have been a farmer," we mean that some individual in another world who is sufficiently similar to Aristotle in the right respects — Aristotle's **counterpart** — is a farmer. Identity across worlds is replaced by counterpart relations: qualitative similarity of the right kind. The advantage is ontological clarity (no individual literally inhabits multiple worlds), but the cost is intuitive: it seems to make modal claims about Aristotle *about someone else*. Kripke pressed this with the **Humphrey objection**: if Hubert Humphrey might have won the 1968 election, he cares about that possibility as a possibility for *him*, not for some qualitatively similar but numerically distinct person. Counterpart theory, Kripke argued, misidentifies what's at stake in modal statements.

The alternative is **genuine transworld identity**: the very same individual — numerically one and the same — exists (or at least has properties) in multiple possible worlds. This view, associated with Kripke and others, raises a different problem: what determines which properties an individual must have in every world (its **essential properties**) versus which it could lack (its **accidental properties**)? Aristotle is necessarily human, plausibly; but might he have been born a day later, in a different city, to different parents? The **essentialist** tradition holds that some properties are constitutive of an individual's identity while others are incidental. But there is no consensus on where the line falls, and different principles (origin essentialism, kind essentialism, bare particular theories) draw it differently.

Your soft prerequisite — rigid designators — connects directly here. Kripke argued that proper names rigidly designate the same individual across all possible worlds. This presupposes that there is something — the individual itself — to be designated across worlds. The rigid designator framework thus tacitly commits to genuine transworld identity. Counterpart theory, by contrast, requires that apparent rigid designation is really a kind of shorthand for counterpart relations. Choosing between these frameworks isn't merely terminological; it shapes what we can coherently say about personal identity, modal claims about individuals, and the metaphysics of essence.

