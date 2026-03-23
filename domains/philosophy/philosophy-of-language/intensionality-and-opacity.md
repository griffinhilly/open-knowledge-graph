---
id: intensionality-and-opacity
title: Intensionality and Semantic Opacity
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: frege-sense-and-reference
  type: hard
- id: first-order-logic-syntax
  type: soft
- id: quantifier-scope-ambiguity
  type: soft
- id: modal-logic-intro
  type: soft
builds-toward:
- scope-ambiguity-and-representation
- de-re-de-dicto-readings
tags:
- semantics
- intensionality
- reference
- substitution
stage: formal-systems
status: draft
---

# Intensionality and Semantic Opacity

## Core Idea
Intensional contexts like 'believes that' and 'necessarily' violate the substitutivity of identicals—co-referential terms cannot always be freely substituted while preserving truth value. This reveals how language represents thought and how meaning depends on more than mere reference.

## How It's Best Learned
Work through Frege's Hesperus/Phosphorus case and belief contexts. Show how Superman/Clark Kent substitution preserves truth in simple contexts but fails in opaque contexts.

## Common Misconceptions
Intensionality does not mean expressions lack truth values in these contexts; rather, meaning is not purely referential. The opacity arises from dependence on sense or mode of presentation, not from meaninglessness.

## Questions

```yaml
- question: "Lois Lane believes Superman can fly. Superman is Clark Kent. What can we correctly conclude?"
  type: multiple-choice
  options:
    - "Lois Lane believes Clark Kent can fly, because Superman and Clark Kent are the same person"
    - "We cannot conclude that Lois Lane believes Clark Kent can fly, because the belief context is opaque to reference"
    - "The sentence 'Superman is Clark Kent' must be false, since it leads to a contradiction about Lois's beliefs"
    - "Lois Lane is irrational for having inconsistent beliefs about the same individual"
  answer: 1
  explanation: "The belief context 'Lois Lane believes...' is referentially opaque: substituting 'Clark Kent' for 'Superman' can change the truth value even though they refer to the same person. In extensional contexts, co-referential terms are interchangeable. But beliefs are about how one *represents* an individual, not merely which individual it is. Lois represents 'Superman' and 'Clark Kent' under different modes of presentation — which is why she can believe one thing about the superhero without believing it about the mild-mannered reporter."

- question: "Which of the following contexts is extensional — that is, allows free substitution of co-referential terms without changing truth value?"
  type: multiple-choice
  options:
    - "'It is necessarily true that the number of planets is greater than 7'"
    - "'Maria knows that the morning star is visible at dawn'"
    - "'The evening star is a planet' (given that the evening star = the morning star, which is a planet)"
    - "'John hopes that Hesperus will be bright tonight'"
  answer: 2
  explanation: "Option C is a simple extensional context: no propositional attitude verb, no modal operator. If the morning star is a planet and the morning star = the evening star, substitution preserves truth — the evening star is also a planet. Options A, B, and D are all intensional: 'necessarily' creates a modal context (what is necessarily true of 9 is not necessarily true of 'the number of planets,' a contingent fact), 'knows' and 'hopes' create propositional attitude contexts. In all three, substituting co-referential terms can fail."

- question: "Intensional contexts like 'believes that' are opaque because expressions within them lack determinate truth values."
  type: true-false
  answer: false
  explanation: "Opacity has nothing to do with truth values being undefined. 'Lois Lane believes Superman can fly' has a perfectly determinate truth value — true or false depending on Lois's mental states. What opacity means is that the truth value of the whole sentence depends on more than just the referents of the terms within it; it depends on the sense or mode of presentation under which those referents are given. Intensional semantics is required not because meaning breaks down, but because purely referential semantics is insufficient to capture what these sentences are about."

- question: "The discovery that 'Hesperus = Phosphorus' (both refer to Venus) is informationally trivial, just like 'Hesperus = Hesperus.'"
  type: true-false
  answer: false
  explanation: "This is Frege's original motivating example for the sense-reference distinction. 'Hesperus = Hesperus' is trivially true — it follows from the logical law of identity. But 'Hesperus = Phosphorus' was a genuine astronomical discovery: ancient astronomers tracking the evening star and the morning star did not initially know they were the same object. The two names have the same reference (Venus) but different senses — different modes of presentation. Informativeness is a function of sense, not reference, which is why identity statements can be both true and surprising."

- question: "Explain why an adequate semantic theory for natural language cannot be purely extensional, and what intensional semantics must add to handle belief and necessity contexts."
  type: short-answer
  answer: "A purely extensional semantics assigns meanings as referents — objects for names, truth values for sentences, sets for predicates — and predicts that co-referential expressions are always interchangeable. But belief and necessity contexts show this fails: 'Lois believes Superman can fly' and 'Lois believes Clark Kent can fly' can differ in truth value even though 'Superman' and 'Clark Kent' co-refer. Intensional semantics must assign meanings sensitive to mode of presentation — what Frege called 'sense' — or treat meanings as functions from possible worlds to extensions rather than bare extensions, allowing two co-referential names to differ in meaning."
  explanation: "The formal apparatus of intensional semantics — possible worlds, intensions as functions from worlds to extensions, senses as modes of presentation — reflects a genuine feature of natural language: we do not only describe the world as it is, but describe how agents represent the world, and what holds across possible scenarios. The failure of extensionality in belief and modal contexts is a window into the difference between reference (what a term picks out) and meaning (how a term presents what it picks out)."
```

## Explainer

From Frege's theory of sense and reference, you know the key distinction: two expressions can have the same **reference** (they pick out the same object) while having different **senses** (they present that object under different descriptions or modes of presentation). "Hesperus" and "Phosphorus" both refer to Venus, but they express different senses—the first was how ancient Greeks identified the evening star, the second how they identified the morning star. Frege introduced this distinction precisely to explain why "Hesperus = Phosphorus" is informative while "Hesperus = Hesperus" is trivial—even though both are true identities about the same object. Intensionality extends this insight from identity statements into a much wider range of linguistic contexts.

The key phenomenon is the failure of **substitutivity of identicals**. In standard extensional logic, if A = B, then any true sentence containing "A" remains true when "B" is substituted for it. This works fine in ordinary contexts: if "The morning star is a planet" is true and "the morning star = the evening star," then "The evening star is a planet" is equally true. But now consider belief contexts: "The ancient astronomers believed that the morning star was visible at dawn" can be true while "The ancient astronomers believed that the evening star was visible at dawn" is false—even though the morning star *is* the evening star. The co-referential terms cannot be freely swapped. This is **referential opacity**: the context is "opaque" to reference, meaning reference alone doesn't determine truth value; the sense, the mode of presentation, matters.

The Superman/Clark Kent case gives the same structure with vivid intuitive force. "Lois Lane believes Superman can fly" is true; "Lois Lane believes Clark Kent can fly" is false—even though Superman is Clark Kent. The belief context creates an intensional environment where what matters is not *who* the name picks out, but *how* Lois represents that individual. More generally, any context created by a propositional attitude verb—**believes**, **knows**, **desires**, **hopes**, **fears**—creates opacity, because these verbs describe relationships to propositions as ways of being presented, not merely to the extensions those propositions are about. Modal contexts behave similarly: "It is necessarily true that 9 > 7" is true, but "It is necessarily true that the number of planets > 7" is false—even though 9 = the number of planets, because the latter is a contingent astronomical fact, not a mathematical necessity.

The theoretical upshot is that an adequate semantic theory cannot be purely **extensional**—it cannot treat the meaning of expressions as just their referents (the objects, truth values, or sets of objects they pick out). **Intensional semantics** must assign meanings that are sensitive to mode of presentation or, in possible-worlds terms, to functions from possible worlds to extensions rather than bare extensions. This is not a mere technical fix; it reveals something deep about natural language: much of what we say is not just *about* the world as it is, but about how we or others *represent* the world. Belief, necessity, and knowledge all require a richer semantic vocabulary—one that tracks not just what things there are, but how they are given to thought.
