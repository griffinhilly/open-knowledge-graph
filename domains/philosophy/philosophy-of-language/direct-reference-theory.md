---
id: direct-reference-theory
title: Direct Reference Theory
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: frege-sense-and-reference
  type: hard
- id: kripke-causal-theory-naming
  type: hard
- id: russell-definite-descriptions
  type: soft
builds-toward:
- donnellan-reference-attributive
- natural-kind-terms-semantics
tags:
- reference
- names
- semantics
- directness
stage: formal-systems
status: draft
---

# Direct Reference Theory

## Core Idea
Direct reference theory holds that names refer to objects directly without descriptive content mediating the reference. Under this view, the meaning of a name just is its referent, and all information about the object is strictly external to the semantic content of the name. This approach explains why names are rigid designators and why coreferential terms like "Cicero" and "Tully" can differ in cognitive significance despite identical reference.

## How It's Best Learned
Compare Frege's puzzles about identity with how direct reference resolves them: "Cicero = Tully" is informative not because of different senses but because speakers may associate different descriptions. Work through Kripke's arguments that names don't have definite descriptions associated with them, using cases of reference-fixing versus reference-determination.

## Common Misconceptions
- Thinking the referent IS the meaning; the referent determines the truth-condition but isn't the meaning itself.
- Assuming direct reference requires no descriptive content at all; reference-fixing may be descriptive even if reference itself is direct.
- Confusing cognitive significance with semantic content; names can differ cognitively despite identical semantics.

## Explainer

From Frege, you know that two names can refer to the same object while differing in **sense** — the mode of presentation that picks out the referent. "Hesperus" and "Phosphorus" both refer to Venus, but their senses differ (evening star vs. morning star), which is why "Hesperus is Phosphorus" is informative rather than trivial. Frege's framework elegantly handles the informativeness of identity statements, but it comes with a strong commitment: names have descriptive content that mediates their reference. **Direct reference theory** challenges this commitment directly, drawing on Kripke's arguments that you've studied.

The core claim is simple but radical: the meaning of a proper name is exhausted by its referent. There is no Fregean sense that names express — just the object itself, contributed directly to the proposition expressed by sentences containing the name. When you say "Aristotle was a student of Plato," the proposition you express contains the actual man Aristotle as a constituent, not a description like "the tutor of Alexander." This is why names are **rigid designators**: in every possible world, "Aristotle" refers to Aristotle, whereas "the tutor of Alexander" might refer to different people in different possible worlds (or no one, if Alexander died young and had no tutor).

But this creates a problem: if "Cicero" and "Tully" have the same meaning (both just meaning the man Cicero), why is "Cicero is Tully" informative — something you could learn — while "Cicero is Cicero" is trivial? Direct reference theorists, especially Nathan Salmon and Scott Soames, handle this through a distinction between **semantic content** and **cognitive significance**. The semantic content — what the sentence contributes to determining truth conditions — is the same for both: a proposition containing Cicero twice in one case, once in the other. But the *cognitive significance* — what you come to know or believe when you learn the sentence — can differ because different speakers associate different ways of thinking about the object with different names. The informativeness lives in the psychology, not the semantics.

Kripke's contribution to this picture is the **causal-historical theory of reference-fixing**, which you've studied. Rather than names inheriting their reference from a cluster of descriptions speakers associate with them, reference is fixed through an initial **baptism** (an act of naming in the presence of the object, or a description used to introduce the name) and then transmitted causally through a chain of uses. Crucially, **reference-fixing** can involve descriptive content without making the name's reference *determined* by that content. We might have introduced "Aristotle" using the description "the greatest student of Plato," but the name now refers to the man himself — if it turned out Aristotle never studied under Plato, the name would still refer to him, and "Aristotle studied under Plato" would turn out to be false. The description fixes which object we're talking about; it does not become the meaning of the name.
