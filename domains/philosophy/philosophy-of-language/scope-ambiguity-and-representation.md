---
id: scope-ambiguity-and-representation
title: Scope Ambiguity and Logical Form
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: russell-definite-descriptions
  type: hard
- id: quantifier-scope-ambiguity
  type: hard
builds-toward:
  - de-re-de-dicto-readings
tags:
- logic
- quantification
- ambiguity
- logical-form
stage: advanced
status: draft
---
# Scope Ambiguity and Logical Form

## Core Idea
Scope ambiguities arise when multiple operators in a sentence can take scope in different orders, yielding logically distinct readings. Logical form representation disambiguates between de re and de dicto interpretations and explains why a single sentence can express multiple propositions.

## Explainer

From your study of first-order logic syntax, you know that quantifiers like ∀ (for all) and ∃ (there exists) take **scope** over formulas: the formula within their scope is the claim they are quantifying over. From your study of quantifier scope ambiguity, you know that when two quantifiers appear in one sentence, there are two ways to order their scope, and those orderings can mean very different things. "Everyone loves someone" can be read as ∀x∃y Loves(x,y)—each person has someone they love, though the someone may differ per person—or as ∃y∀x Loves(x,y)—there is one particular person that everyone loves. These two **logical forms** express distinct propositions; the first is true in any world of mutual personal affections, while the second requires a single universal beloved. Natural language does not mark this distinction on its surface; the same string of words is genuinely ambiguous.

From your study of Russell's theory of definite descriptions, you know that surface grammar is a poor guide to logical form. "The present king of France is bald" looks like a simple subject-predicate sentence, but Russell showed it conceals three quantificational claims: there is at least one present king of France, there is at most one, and that one is bald. The logical form is complex and quantificational, not simple. Scope ambiguity arises here too: when a definite description occurs inside another operator (a modal operator like "necessarily" or a propositional attitude verb like "believes"), the description can take **wide scope** (applying outside the operator) or **narrow scope** (applying inside it), with very different results.

This is where the **de re / de dicto** distinction becomes essential. Consider "John believes the tallest spy is dangerous." On the **de dicto** reading (belief is about the description as such), John has a belief about whoever satisfies "tallest spy"—he believes: there is a tallest spy, and that person is dangerous. This is a narrow-scope reading of the description within the belief context. On the **de re** reading (belief is directly about the thing), there is a particular individual—call her Maria—who is in fact the tallest spy, and John has a belief specifically about Maria: he believes of her that she is dangerous. These differ dramatically in what they say about John's epistemic state: on the de re reading, John need not believe there is a tallest spy or even know who the tallest spy is; he just has a belief directed at that individual. The logical form representation using scope makes this difference explicit: wide-scope description gives the de re reading; narrow-scope description gives the de dicto reading.

Scope ambiguity connects to some of the most debated puzzles in philosophy of language and mind. Puzzles about **intentionality** and **opacity**—how the objects of beliefs and desires are identified—often reduce to scope questions. Kripke's "Paderewski" puzzle (someone can believe that Paderewski has musical talent and also believe that Paderewski lacks musical talent, if they don't know their two encounters were with the same person) turns on questions of how names and descriptions interact within belief contexts. Modal claims ("necessarily, the morning star is the morning star" vs "necessarily, the morning star is the evening star") differ in truth value depending on whether the scope of "necessarily" is narrow or wide relative to the description. Mastering logical form representation gives you a precise vocabulary for locating exactly where the ambiguity arises and what the two readings commit you to—a tool that is indispensable for serious work in semantics, philosophy of mind, and metaphysics.
