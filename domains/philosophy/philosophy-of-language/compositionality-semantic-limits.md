---
id: compositionality-semantic-limits
title: Compositionality and Its Limits
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: compositionality-principle
  type: hard
- id: first-order-logic-syntax
  type: soft
builds-toward:
- scalar-implicature-pragmatics
tags:
- compositionality
- semantics
- meaning
- structure
stage: formal-systems
status: validated
---

# Compositionality and Its Limits

## Core Idea
While compositionality is a guiding principle—a complex expression's meaning is determined by its parts and structure—it faces challenges from phenomena like idioms ("kick the bucket"), scope ambiguities, and context-shift cases. Understanding where and why compositionality succeeds and fails refines our conception of how meaning is constructed and transmitted.

## How It's Best Learned
Start with clear compositional cases (arithmetic expressions, simple predicates) then move to failures: "pull someone's leg" doesn't mean making leg-pulling motions. Study how the same structure can yield different meanings in different contexts ("That's a bright idea" versus "That's a bright student"). Examine whether compositionality is semantic law or pragmatic principle, and whether partial compositionality is defensible.

## Common Misconceptions
- Thinking compositionality is an all-or-nothing principle; it may hold in some domains but not others.
- Assuming idioms necessarily violate compositionality; some idiomatic meanings are compositional at metaphorical level.
- Overlooking that context-sensitivity might be handled compositionally if we include context-dependence in semantic values.

## Explainer

You've mastered the compositionality principle: the meaning of a complex expression is a function of the meanings of its parts and their mode of combination. The power of this principle is that it explains how finite minds understand an infinite number of sentences — you don't memorize meanings whole, you compute them. But the principle faces stress tests that reveal both its scope and its limits. Understanding where compositionality holds and where it strains illuminates the deeper architecture of how meaning is constructed.

The clearest case of compositional success is logical and mathematical language. "Three plus four equals seven" means what it does because "three," "four," "plus," and "equals seven" each make determinate contributions, and the syntactic structure specifies how those contributions combine. From your study of first-order logic syntax, you recognize that the same compositional story applies to natural language predicates: "the cat slept" means what it does because "the cat" picks out a referent and "slept" applies a predicate, combined by standard predication. The syntactic structure is the composition rule; the semantic values of the parts are the inputs; the output is the sentence's meaning.

**Idioms** are the canonical challenge. "Kick the bucket" does not mean what a compositional analysis would predict from the literal meanings of "kick" and "bucket." The meaning (to die) seems to be a stored, non-compositional whole. But careful analysis complicates this picture. Idioms may be compositional at a **metaphorical** level — the image of a bucket being kicked encodes a conventional metaphorical mapping that the community has fixed. Even if the idiomatic meaning cannot be computed from *literal* meanings of the parts, it may still be derived compositionally from *conventionalized metaphorical* meanings that are themselves stored. Whether this counts as "real" compositionality is a substantive question, but it shows that apparent failures often mask more subtle compositional structure.

**Context-shifting** poses a deeper challenge. Consider "I," "here," "now" — these pick out different individuals, places, and times depending on context. The standard response is that compositionality operates over **character** (a function from context to content, in Kaplan's framework) rather than content directly. The semantic value of "I" is not an individual but a rule: "in any context, pick the speaker." Composition applies to characters; context then yields content. This extension handles many apparent failures while revealing that the compositionality principle operates at a level of abstraction richer than surface form. Persistent cases that resist even this treatment — **donkey anaphora** ("Every farmer who owns a donkey beats it"), **ellipsis**, and **nominal coercion** — remain active research areas where the genuine limits of compositionality are tested. These cases are not failures of the principle so much as reminders that the syntax-semantics interface is more complex than any simple formulation of compositionality captures.

## Questions

- id: compositionality-semantic-limits-q1
  type: mc
  question: "How does Kaplan's framework handle the apparent compositionality failure of context-sensitive expressions like 'I,' 'here,' and 'now'?"
  options:
    - "It treats these expressions as idioms with stored meanings"
    - "It argues that compositionality applies to character (a function from context to content) rather than content directly"
    - "It abandons compositionality for sentences containing indexicals"
    - "It assigns each indexical a fixed referent determined by convention"
  correct: 1
  explanation: "Kaplan's framework preserves compositionality by operating over character rather than content. The semantic value of 'I' is not a specific individual but a rule ('pick the speaker in this context'). Composition applies to these rules, and context then determines the specific content."

- id: compositionality-semantic-limits-q2
  type: mc
  question: "Why might idioms like 'kick the bucket' not be a straightforward violation of compositionality?"
  options:
    - "Because idioms are not real expressions in any language"
    - "Because 'kick' and 'bucket' literally combine to produce the meaning 'to die'"
    - "Because the idiomatic meaning may be compositional at a conventionalized metaphorical level"
    - "Because compositionality only applies to sentences, not phrases"
  correct: 2
  explanation: "While idioms cannot be composed from the literal meanings of their parts, they may be compositional at a metaphorical level — the image encodes a conventional metaphorical mapping. Whether this counts as 'real' compositionality is debatable, but apparent failures often mask subtler compositional structure."

- id: compositionality-semantic-limits-q3
  type: tf
  question: "The compositionality principle explains how speakers can understand an infinite number of sentences from a finite vocabulary."
  correct: true
  explanation: "Compositionality's explanatory power lies precisely in this: because meaning is a function of parts and their mode of combination, finite minds can compute the meanings of infinitely many novel sentences by knowing base meanings and combination rules."

- id: compositionality-semantic-limits-q4
  type: tf
  question: "Donkey anaphora, ellipsis, and nominal coercion are cases that have been fully resolved within standard compositional semantics."
  correct: false
  explanation: "These cases remain active research areas where the genuine limits of compositionality are tested. They resist treatment even under Kaplan's extended framework and remind us that the syntax-semantics interface is more complex than any simple formulation captures."

- id: compositionality-semantic-limits-q5
  type: sa
  question: "What is the classic example of 'donkey anaphora' discussed in the topic?"
  correct: "Every farmer who owns a donkey beats it"
  explanation: "This sentence is a canonical example of donkey anaphora, where the pronoun 'it' refers back to 'a donkey' in a way that resists standard compositional treatment. It remains an active area of research at the limits of compositionality."

