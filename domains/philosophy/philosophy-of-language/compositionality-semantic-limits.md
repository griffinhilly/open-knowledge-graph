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

## Questions

```yaml
- question: "Kaplan's framework handles context-sensitive expressions like 'I' and 'here' without abandoning compositionality. How does it achieve this?"
  type: multiple-choice
  options:
    - "Context-sensitive words are treated as idioms stored as wholes, bypassing composition"
    - "Compositionality is applied to character — a function from contexts to contents — rather than to content directly, preserving the principle at a more abstract level"
    - "Context-sensitivity proves compositionality is false, since the same sentence can express different propositions in different contexts"
    - "Compositionality only applies to logical and mathematical language, not to natural language expressions like indexicals"
  answer: 1
  explanation: "Kaplan's key move: 'I' doesn't have a fixed content (an individual); it has a character — a rule that picks out the speaker in any context. Composition operates over these characters. Context then maps character to content. This extends compositionality to handle indexicals without abandoning the principle — it just reveals that compositionality operates at a level of semantic abstraction richer than surface content. The principle is preserved, not refuted."

- question: "A student argues: 'Kick the bucket means to die, but you can't compute that meaning from what "kick" and "bucket" literally mean — therefore compositionality is false.' What is the strongest response?"
  type: multiple-choice
  options:
    - "The student is correct — idioms are decisive counterexamples to compositionality"
    - "The idiom's meaning may still be compositionally derived from the conventionalized metaphorical meanings of the parts, not their literal meanings — apparent failure masks more subtle compositional structure"
    - "Idioms are exempt from compositionality by definition, so they don't count as evidence for or against it"
    - "The idiom fails compositionality, but idioms are so rare that the principle is still approximately correct"
  answer: 1
  explanation: "The nuanced response: compositionality only requires that meanings derive from the meanings of the parts — it doesn't specify those meanings must be literal. If 'kick' carries a conventional metaphorical association with death (the image of a bucket being kicked), the idiomatic meaning might still be compositionally derived from those conventionalized metaphorical meanings. Whether this counts as 'real' compositionality is contested, but it shows that apparent failures often mask deeper compositional structure rather than outright violations."

- question: "Compositionality is compatible with context-sensitive expressions if the principle is understood to apply to character (a function from context to content) rather than to content directly."
  type: true-false
  answer: true
  explanation: "This is Kaplan's extension of compositionality. Instead of requiring that complex expressions have context-independent semantic values, we allow semantic values to be characters — rules that yield different contents in different contexts. Compositionality then holds at the level of character: the character of a complex expression is determined by the characters of its parts and their mode of combination. Context-sensitivity becomes a feature of the semantic values, not a violation of the compositional architecture."

- question: "If compositionality holds, every sentence must have a context-independent meaning, because compositionality requires meaning to be fully determined by the parts."
  type: true-false
  answer: false
  explanation: "Compositionality requires that complex meanings be determined by the meanings of parts — but those 'meanings' can themselves be context-dependent. If 'I' means 'the speaker in this context,' then 'I am hungry' compositionally combines this context-sensitive part with a predicate, yielding a sentence whose full content is fixed only relative to a context. The principle governs how parts combine, not whether those parts are context-sensitive. Context-sensitivity and compositionality are orthogonal properties."

- question: "Why do idioms not straightforwardly refute compositionality, even though their idiomatic meanings cannot be computed from the literal meanings of their parts?"
  type: short-answer
  answer: "Compositionality only requires that meanings derive from the meanings of parts — it doesn't specify those meanings must be literal. Idioms may be compositional at a metaphorical level: if the parts carry conventionalized figurative meanings (e.g., 'kick the bucket' involves a conventional mapping from the image of a kicked bucket to the concept of death), then the idiomatic meaning might still be computed compositionally from those metaphorical meanings. The apparent failure is at the level of literal interpretation; it may not extend to the level of conventional meaning. Whether this preserves 'true' compositionality is a substantive debate, but it shows that apparent violations often indicate more complex compositional structure rather than a breakdown of the principle."
  explanation: "This also illustrates the broader lesson: when compositionality appears to fail, the right response is often to ask whether we have correctly identified the relevant semantic values of the parts. Extending the principle to operate over richer semantic values (metaphorical meanings, characters, etc.) often resolves apparent counterexamples."
```

## Explainer

You've mastered the compositionality principle: the meaning of a complex expression is a function of the meanings of its parts and their mode of combination. The power of this principle is that it explains how finite minds understand an infinite number of sentences — you don't memorize meanings whole, you compute them. But the principle faces stress tests that reveal both its scope and its limits. Understanding where compositionality holds and where it strains illuminates the deeper architecture of how meaning is constructed.

The clearest case of compositional success is logical and mathematical language. "Three plus four equals seven" means what it does because "three," "four," "plus," and "equals seven" each make determinate contributions, and the syntactic structure specifies how those contributions combine. From your study of first-order logic syntax, you recognize that the same compositional story applies to natural language predicates: "the cat slept" means what it does because "the cat" picks out a referent and "slept" applies a predicate, combined by standard predication. The syntactic structure is the composition rule; the semantic values of the parts are the inputs; the output is the sentence's meaning.

**Idioms** are the canonical challenge. "Kick the bucket" does not mean what a compositional analysis would predict from the literal meanings of "kick" and "bucket." The meaning (to die) seems to be a stored, non-compositional whole. But careful analysis complicates this picture. Idioms may be compositional at a **metaphorical** level — the image of a bucket being kicked encodes a conventional metaphorical mapping that the community has fixed. Even if the idiomatic meaning cannot be computed from *literal* meanings of the parts, it may still be derived compositionally from *conventionalized metaphorical* meanings that are themselves stored. Whether this counts as "real" compositionality is a substantive question, but it shows that apparent failures often mask more subtle compositional structure.

**Context-shifting** poses a deeper challenge. Consider "I," "here," "now" — these pick out different individuals, places, and times depending on context. The standard response is that compositionality operates over **character** (a function from context to content, in Kaplan's framework) rather than content directly. The semantic value of "I" is not an individual but a rule: "in any context, pick the speaker." Composition applies to characters; context then yields content. This extension handles many apparent failures while revealing that the compositionality principle operates at a level of abstraction richer than surface form. Persistent cases that resist even this treatment — **donkey anaphora** ("Every farmer who owns a donkey beats it"), **ellipsis**, and **nominal coercion** — remain active research areas where the genuine limits of compositionality are tested. These cases are not failures of the principle so much as reminders that the syntax-semantics interface is more complex than any simple formulation of compositionality captures.

