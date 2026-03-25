---
id: proper-names-and-reference
title: 'Proper Names: Their Meaning and Reference'
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: kripke-causal-theory-naming
  type: hard
- id: descriptivism-proper-names
  type: soft
- id: intensionality-and-opacity
  type: soft
builds-toward:
- reference-determination
- twin-earth-thought-experiment
tags:
- proper-names
- reference
- Kripke
- semantics
stage: formal-systems
status: validated
---
# Proper Names: Their Meaning and Reference

## Core Idea
Proper names pose a distinctive problem for semantic theory: they seem to contribute nothing to the truth-conditions of sentences containing them beyond identifying an individual, yet they convey no descriptive content. Names appear to be purely referential, depending on facts about the world (causal history, current facts) rather than conceptual content. Different theories explain how names acquire their referents: descriptivist accounts, causal-historical accounts, and hybrid accounts.

## Questions

```yaml
- question: "Suppose Aristotle had died in infancy and never studied philosophy or written anything. A descriptivist says 'Aristotle' would then refer to whoever did teach Alexander the Great. Kripke argues instead that..."
  type: multiple-choice
  options:
    - "The descriptivist is correct — names are defined by whichever descriptions happen to be true of their bearer"
    - "'Aristotle' would still refer to the same individual who died in infancy — names track individuals across possible worlds, not which descriptions they satisfy"
    - "'Aristotle' would become an empty name with no referent in that counterfactual scenario"
    - "Both theories agree on this case — names always refer to actual individuals regardless of their properties"
  answer: 1
  explanation: "Kripke's core argument is that proper names are rigid designators: they pick out the same individual in every possible world in which that individual exists. 'Aristotle might have died in infancy' is a coherent claim — and it presupposes that 'Aristotle' refers to the same person in that scenario, not to whoever happened to teach Alexander. Descriptivism makes reference contingent on which descriptions are true, which means the name would 'drift' to a different person as descriptions change. Rigidity means it doesn't drift."

- question: "What is the key difference between a rigid designator and a definite description?"
  type: multiple-choice
  options:
    - "Rigid designators are shorter and more convenient; descriptions are longer but more informative"
    - "Rigid designators pick out the same individual in every possible world; descriptions pick out whoever satisfies the relevant property in each world"
    - "Rigid designators only work for living individuals; descriptions can refer to abstract objects"
    - "Rigid designators require physical ostension at baptism; descriptions require a mental concept"
  answer: 1
  explanation: "This is the modal distinction at the heart of Kripke's argument. 'The teacher of Alexander' is non-rigid: in a counterfactual world where Alexander had a different tutor, the description would refer to that other person. 'Aristotle' is rigid: it refers to Aristotle — the specific individual — in every possible world where he exists, regardless of what he did or didn't do. Descriptions pick out whoever plays the role; names track the individual through different roles."

- question: "On Kripke's causal-historical account, successfully referring to Aristotle by name requires knowing at least one true description of him."
  type: true-false
  answer: false
  explanation: "The causal-historical account explicitly replaces descriptive knowledge with causal chain membership. You refer to Aristotle because you stand in the right causal chain of name transmission — you learned the name from teachers and books, who got it from others, reaching back to an original naming event. You do not need to know any true descriptions of Aristotle. In fact, you might hold entirely false beliefs about him and still successfully refer to him, as long as your use of the name is connected to that causal chain."

- question: "The descriptivist account explains why we can say 'Aristotle might never have studied philosophy' without changing who the name refers to in that sentence."
  type: true-false
  answer: false
  explanation: "This is precisely where descriptivism fails. If 'Aristotle' is a disguised description like 'the student of Plato who taught Alexander,' then in a world where Aristotle never studied philosophy, the description picks out someone else — not the same individual. But our intuition is that the sentence is coherently about the very person who actually existed, describing a path his life didn't take. Kripke's rigidity thesis explains this intuition: the name refers to the same individual in all possible worlds, regardless of which descriptions he satisfies."

- question: "What does it mean to say that proper names are 'rigid designators,' and why does this pose a problem for descriptivist theories of reference?"
  type: short-answer
  answer: "A rigid designator refers to the same individual in every possible world — even counterfactual scenarios where that individual has different properties. 'Aristotle' refers to Aristotle in all possible worlds, including ones where he never studied philosophy. Descriptivism makes reference depend on which descriptions are true: if Aristotle had different properties, the name would pick out whoever satisfied the description instead. This predicts that 'Aristotle might never have studied philosophy' is incoherent or changes its subject — but that seems wrong. Rigidity is what allows us to use names to describe what might have been true of the same individual."
  explanation: "The modal argument is Kripke's sharpest tool against descriptivism. Consider: we can coherently evaluate counterfactuals like 'Einstein might have become a musician instead.' For this to make sense, 'Einstein' must refer to the same person in that counterfactual — not to whoever became the greatest physicist. Descriptions are non-rigid: 'the greatest physicist of the 20th century' picks out a different person in a world where Einstein pursued music. Names, Kripke argues, don't work this way — they rigidly track individuals through the space of possibilities."
```

## Explainer

From your study of Kripke's causal theory of naming, you already have the central modern account in hand. The question is why proper names were puzzling in the first place — and why Kripke's answer was so revolutionary. The puzzle begins with a simple observation: when you use a name like "Aristotle," what determines which person you are talking about? One natural answer is that you associate some cluster of descriptions with the name — "the pupil of Plato," "the teacher of Alexander," "the author of the Nicomachean Ethics" — and whoever uniquely fits that description is the referent.

This **descriptivist** view, held by Frege and Russell in varying forms, has an appealing explanation of meaning: names are disguised descriptions, and grasping the name means knowing the associated description. But Kripke's modal arguments exposed its failures. Suppose Aristotle had died young and written nothing. On descriptivism, "Aristotle" would no longer refer to Aristotle — it would refer to whoever actually taught Alexander, which might have been someone else entirely. This seems wrong: we can coherently say "Aristotle might have died young and never written anything," which presupposes that "Aristotle" *refers to the same individual* in that counterfactual scenario. Names are **rigid designators** — they pick out the same individual in every possible world in which that individual exists, regardless of which descriptions happen to be true of them. Definite descriptions are not rigid: "the teacher of Alexander" refers to whoever occupied that role in each scenario, not necessarily Aristotle.

Kripke's **causal-historical** account replaces descriptions with a chain of transmission. A name enters circulation through an initial **baptism** — a naming event where the name is attached to an individual, either by ostension ("I name this child 'Sophia'") or description-fixing ("We'll call whoever discovered this planet 'Neptune'"). Subsequent uses of the name get their reference from this chain: you picked up "Aristotle" from books and teachers, who got it from others, stretching back through generations of use to an initial event of naming. You don't need to know any true descriptions of Aristotle to refer to him; you just need to be a participant in the right causal chain. This explains how proper names can be *empty of descriptive content* while still having determinate reference.

The theory is not without complications. What counts as being in "the right" causal chain? If a name is misapplied (early Greeks named a constellation, but the name later migrated to a different object), does the chain still transmit the original reference? What about purely fictional names, or names for abstract objects? **Hybrid accounts** try to preserve the insight that names are rigid and not merely descriptions while acknowledging that descriptive content sometimes plays a role in fixing reference — especially in the initial baptism, where a description is often used to identify the named object. The broader lesson is that reference is not a relation between a word and a concept in your head, but a relation between a word, a community of speakers, and an object in the world — a fundamentally social and historical phenomenon.

