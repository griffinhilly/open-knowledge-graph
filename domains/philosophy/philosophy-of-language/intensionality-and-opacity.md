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
stage: advanced
status: draft
---

# Intensionality and Semantic Opacity

## Core Idea
Intensional contexts like 'believes that' and 'necessarily' violate the substitutivity of identicals—co-referential terms cannot always be freely substituted while preserving truth value. This reveals how language represents thought and how meaning depends on more than mere reference.

## How It's Best Learned
Work through Frege's Hesperus/Phosphorus case and belief contexts. Show how Superman/Clark Kent substitution preserves truth in simple contexts but fails in opaque contexts.

## Common Misconceptions
Intensionality does not mean expressions lack truth values in these contexts; rather, meaning is not purely referential. The opacity arises from dependence on sense or mode of presentation, not from meaninglessness.

## Explainer

From Frege's theory of sense and reference, you know the key distinction: two expressions can have the same **reference** (they pick out the same object) while having different **senses** (they present that object under different descriptions or modes of presentation). "Hesperus" and "Phosphorus" both refer to Venus, but they express different senses—the first was how ancient Greeks identified the evening star, the second how they identified the morning star. Frege introduced this distinction precisely to explain why "Hesperus = Phosphorus" is informative while "Hesperus = Hesperus" is trivial—even though both are true identities about the same object. Intensionality extends this insight from identity statements into a much wider range of linguistic contexts.

The key phenomenon is the failure of **substitutivity of identicals**. In standard extensional logic, if A = B, then any true sentence containing "A" remains true when "B" is substituted for it. This works fine in ordinary contexts: if "The morning star is a planet" is true and "the morning star = the evening star," then "The evening star is a planet" is equally true. But now consider belief contexts: "The ancient astronomers believed that the morning star was visible at dawn" can be true while "The ancient astronomers believed that the evening star was visible at dawn" is false—even though the morning star *is* the evening star. The co-referential terms cannot be freely swapped. This is **referential opacity**: the context is "opaque" to reference, meaning reference alone doesn't determine truth value; the sense, the mode of presentation, matters.

The Superman/Clark Kent case gives the same structure with vivid intuitive force. "Lois Lane believes Superman can fly" is true; "Lois Lane believes Clark Kent can fly" is false—even though Superman is Clark Kent. The belief context creates an intensional environment where what matters is not *who* the name picks out, but *how* Lois represents that individual. More generally, any context created by a propositional attitude verb—**believes**, **knows**, **desires**, **hopes**, **fears**—creates opacity, because these verbs describe relationships to propositions as ways of being presented, not merely to the extensions those propositions are about. Modal contexts behave similarly: "It is necessarily true that 9 > 7" is true, but "It is necessarily true that the number of planets > 7" is false—even though 9 = the number of planets, because the latter is a contingent astronomical fact, not a mathematical necessity.

The theoretical upshot is that an adequate semantic theory cannot be purely **extensional**—it cannot treat the meaning of expressions as just their referents (the objects, truth values, or sets of objects they pick out). **Intensional semantics** must assign meanings that are sensitive to mode of presentation or, in possible-worlds terms, to functions from possible worlds to extensions rather than bare extensions. This is not a mere technical fix; it reveals something deep about natural language: much of what we say is not just *about* the world as it is, but about how we or others *represent* the world. Belief, necessity, and knowledge all require a richer semantic vocabulary—one that tracks not just what things there are, but how they are given to thought.
