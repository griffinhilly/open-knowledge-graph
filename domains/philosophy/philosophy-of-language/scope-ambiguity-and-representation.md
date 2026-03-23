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
stage: formal-systems
status: draft
---
# Scope Ambiguity and Logical Form

## Core Idea
Scope ambiguities arise when multiple operators in a sentence can take scope in different orders, yielding logically distinct readings. Logical form representation disambiguates between de re and de dicto interpretations and explains why a single sentence can express multiple propositions.

## Questions

```yaml
- question: "The sentence 'Every student read a book' is ambiguous. On the reading where one particular book was read by everyone, the logical form is:"
  type: multiple-choice
  options:
    - "∀x(Student(x) → ∃y(Book(y) ∧ Read(x, y)))"
    - "∃y(Book(y) ∧ ∀x(Student(x) → Read(x, y)))"
    - "∀x∀y(Student(x) ∧ Book(y) → Read(x, y))"
    - "∃x(Student(x) ∧ ∃y(Book(y) ∧ Read(x, y)))"
  answer: 1
  explanation: "The reading where one specific book is shared by all students requires the existential quantifier over books to take *wide scope* — it is asserted first, binding a particular book y, and then the universal quantifier over students falls within its scope. This gives ∃y(Book(y) ∧ ∀x(Student(x) → Read(x, y))): there is a book that every student read. Option A is the other reading (narrow-scope ∃): each student is guaranteed a book, but the books may differ. The surface English string is genuinely ambiguous between these two logical forms."

- question: "John does not know that Maria is the tallest spy. Yet he has been watching Maria for years, believing her to be dangerous. On the de re reading of 'John believes the tallest spy is dangerous,' which of the following is true?"
  type: multiple-choice
  options:
    - "John must know that Maria is the tallest spy for the de re reading to apply"
    - "The de re reading is false because John does not associate the description 'tallest spy' with Maria"
    - "The de re reading is true: John has a belief directly about Maria (the individual), even without knowing she is the tallest spy"
    - "De re and de dicto readings agree here since the description is uniquely satisfied"
  answer: 2
  explanation: "The de re reading attributes a belief *about a particular individual* — it says there is an individual x (namely Maria, who happens to be the tallest spy) such that John believes of x that she is dangerous. John need not know the description 'tallest spy' applies to her; the de re reading only requires that his belief is directed at that individual, however he identifies her. The de dicto reading would require John to have a belief *about the description itself* — believing that whoever satisfies 'tallest spy' is dangerous. The two readings differ precisely in whether the description scopes outside (de re) or inside (de dicto) John's belief context."

- question: "On the de re reading of a belief attribution, the believer must have the individual in mind under the relevant description."
  type: true-false
  answer: false
  explanation: "This is the key misconception about the de re/de dicto distinction. The de re reading requires only that there is a particular individual about whom the belief is held — it does not require the believer to identify that individual under any specific description. John's belief can be de re about Maria even if he knows her only as 'the woman in the blue coat' and has no idea she is the tallest spy. The description in the sentence ('the tallest spy') is used by the *attributor* to pick out the individual; it need not be how the believer represents her."

- question: "The scope ambiguity in natural language sentences like 'Everyone loves someone' can usually be resolved by careful attention to word order and syntax."
  type: true-false
  answer: false
  explanation: "This is the central lesson of scope ambiguity: natural language surface syntax radically underdetermines logical form. English word order and syntactic structure do not reliably indicate quantifier scope — both readings of 'Everyone loves someone' have identical surface syntax, yet they express logically distinct propositions with different truth conditions. This is why logical form representation is needed as a distinct level of semantic analysis: it makes explicit what natural language leaves systematically ambiguous. Context and pragmatics can sometimes resolve the ambiguity, but this is extra-linguistic information, not syntactic."

- question: "Why does it matter for belief attributions whether a description takes wide scope or narrow scope relative to the belief operator?"
  type: short-answer
  answer: "Scope determines what the belief is *about*. Under narrow scope (de dicto), the belief is about whoever satisfies the description — John believes there is a tallest spy and that person is dangerous, so his belief would be false if there is no tallest spy. Under wide scope (de re), there must be an actual individual who satisfies the description, and John's belief is directly about that individual, not about the description — even if John doesn't know the description applies. The two readings attribute different cognitive states to John, with different implications about his knowledge, the content of his belief, and what would verify or falsify it."
  explanation: "This matters practically for discussions of intentionality, opacity, and the semantics of propositional attitude verbs. Two people can have 'the same' belief sentence attributed to them but be in entirely different epistemic states, depending on how the descriptions scope. Logical form representation makes these differences precise and testable."
```

## Explainer

From your study of first-order logic syntax, you know that quantifiers like ∀ (for all) and ∃ (there exists) take **scope** over formulas: the formula within their scope is the claim they are quantifying over. From your study of quantifier scope ambiguity, you know that when two quantifiers appear in one sentence, there are two ways to order their scope, and those orderings can mean very different things. "Everyone loves someone" can be read as ∀x∃y Loves(x,y)—each person has someone they love, though the someone may differ per person—or as ∃y∀x Loves(x,y)—there is one particular person that everyone loves. These two **logical forms** express distinct propositions; the first is true in any world of mutual personal affections, while the second requires a single universal beloved. Natural language does not mark this distinction on its surface; the same string of words is genuinely ambiguous.

From your study of Russell's theory of definite descriptions, you know that surface grammar is a poor guide to logical form. "The present king of France is bald" looks like a simple subject-predicate sentence, but Russell showed it conceals three quantificational claims: there is at least one present king of France, there is at most one, and that one is bald. The logical form is complex and quantificational, not simple. Scope ambiguity arises here too: when a definite description occurs inside another operator (a modal operator like "necessarily" or a propositional attitude verb like "believes"), the description can take **wide scope** (applying outside the operator) or **narrow scope** (applying inside it), with very different results.

This is where the **de re / de dicto** distinction becomes essential. Consider "John believes the tallest spy is dangerous." On the **de dicto** reading (belief is about the description as such), John has a belief about whoever satisfies "tallest spy"—he believes: there is a tallest spy, and that person is dangerous. This is a narrow-scope reading of the description within the belief context. On the **de re** reading (belief is directly about the thing), there is a particular individual—call her Maria—who is in fact the tallest spy, and John has a belief specifically about Maria: he believes of her that she is dangerous. These differ dramatically in what they say about John's epistemic state: on the de re reading, John need not believe there is a tallest spy or even know who the tallest spy is; he just has a belief directed at that individual. The logical form representation using scope makes this difference explicit: wide-scope description gives the de re reading; narrow-scope description gives the de dicto reading.

Scope ambiguity connects to some of the most debated puzzles in philosophy of language and mind. Puzzles about **intentionality** and **opacity**—how the objects of beliefs and desires are identified—often reduce to scope questions. Kripke's "Paderewski" puzzle (someone can believe that Paderewski has musical talent and also believe that Paderewski lacks musical talent, if they don't know their two encounters were with the same person) turns on questions of how names and descriptions interact within belief contexts. Modal claims ("necessarily, the morning star is the morning star" vs "necessarily, the morning star is the evening star") differ in truth value depending on whether the scope of "necessarily" is narrow or wide relative to the description. Mastering logical form representation gives you a precise vocabulary for locating exactly where the ambiguity arises and what the two readings commit you to—a tool that is indispensable for serious work in semantics, philosophy of mind, and metaphysics.
