---
id: discourse-representation-theory
title: Discourse Representation Theory
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: discourse-analysis
  type: hard
- id: formal-pragmatics-context
  type: soft
builds-toward:
- context-update-semantics
tags:
- pragmatics
- discourse
- formal
stage: expert
status: validated
---

# Discourse Representation Theory

## Core Idea
Discourse Representation Theory models discourse by building structured Discourse Representation Structures. Each sentence adds referents and conditions; pronouns resolve to established referents. This handles anaphora and presupposition accommodation in extended discourse: 'A woman entered. She was happy' succeeds, but 'A woman entered. She had three children' accommodates missing information.

## Questions

```yaml
- question: "In the sentence 'Every farmer who owns a donkey beats it,' why does standard first-order predicate logic struggle to handle the pronoun 'it'?"
  type: multiple-choice
  options:
    - "The sentence is semantically anomalous and cannot be represented formally at all"
    - "The existential quantifier for 'a donkey' falls inside the restrictor of 'every farmer,' outside the scope needed to bind 'it' in the matrix clause"
    - "First-order logic cannot represent sentences with more than one quantifier"
    - "The pronoun 'it' must refer to 'farmer,' not 'donkey,' since farmers are mentioned first"
  answer: 1
  explanation: "In first-order logic, 'a donkey' introduces an existential quantifier (∃y) whose scope is limited to the relative clause 'who owns a donkey.' The pronoun 'it' in 'beats it' falls *outside* that scope, so the variable y is not accessible to bind. Attempts to extend the scope of ∃y to cover the whole sentence produce a different, weaker reading. DRT resolves this by building a DRS in which indefinites introduce discourse referents accessible across the entire conditional structure — 'a donkey' in the restrictor introduces a referent y accessible to the matrix clause."

- question: "A speaker says 'My neighbor just got back from her trip.' The listener has no prior information about any trip. In DRT terms, what happens?"
  type: multiple-choice
  options:
    - "The discourse fails — the presupposition of a prior trip cannot be resolved and interpretation halts"
    - "The presupposition is accommodated — a new discourse referent for the trip is added to the DRS"
    - "The pronoun 'her' fails to find an antecedent and the sentence is uninterpretable"
    - "The listener discards the sentence as uncooperative under Gricean maxims"
  answer: 1
  explanation: "DRT distinguishes anaphora resolution (finding an existing referent) from presupposition accommodation (adding a missing referent when required). 'My neighbor got back from her trip' presupposes that a trip occurred. When this isn't established in the current DRS, the interpreter accommodates — inferring that a trip must exist and adding it as a new discourse referent with the conditions that the speaker's neighbor took it. Accommodation is licensed when the presupposition is plausible and consistent with the existing model. The DRS does not crash; it dynamically expands."

- question: "In DRT, each sentence is interpreted independently, and pronouns find their antecedents only within the sentence that contains them."
  type: true-false
  answer: false
  explanation: "This describes sentence-level semantics, not DRT. DRT's central innovation is that discourse is interpreted by building a single, cumulative Discourse Representation Structure across multiple sentences. A discourse referent introduced in one sentence (e.g., 'A woman entered' — introduces referent x) remains accessible to subsequent sentences ('She was happy' — the pronoun 'she' picks up x). Pronouns can resolve to any discourse referent currently in scope within the DRS, regardless of which sentence introduced it."

- question: "In DRT, whether a discourse referent introduced in a subordinate clause (e.g., the antecedent of a conditional) can serve as an antecedent for a subsequent pronoun depends on the accessibility conditions of the DRS."
  type: true-false
  answer: true
  explanation: "DRT defines formal accessibility conditions specifying which discourse referents a pronoun can pick up. Referents in main boxes are accessible to subsequent discourse. But referents introduced inside subordinate DRS boxes (e.g., the consequent of a conditional, or the scope of a negation) are typically *not* accessible outside those boxes. This explains why 'If a farmer owns a donkey, he beats it' allows 'he' to pick up the farmer (both are in the same conditional structure) but 'I don't own a donkey. *It is brown' fails — the referent introduced under negation is inaccessible outside it."

- question: "How does DRT handle pronoun resolution across sentence boundaries, and what formal object makes this possible?"
  type: short-answer
  answer: "DRT tracks all discourse referents — entities introduced by noun phrases and pronouns — in a Discourse Representation Structure (DRS), a box containing referents and conditions that accumulates across the entire discourse. When a pronoun appears, it resolves by searching the accessible portion of the current DRS for a compatible referent. Because the DRS is updated incrementally with each sentence rather than reset, a referent introduced in sentence 1 remains in scope for pronouns in sentences 2, 3, and beyond, provided the accessibility conditions are met."
  explanation: "This contrasts with purely sentence-level semantics, where each sentence starts fresh. The DRS functions as a formal model of the shared mental space that speaker and hearer build together during discourse. Pronouns are not self-contained — they are instructions to find a referent in this ongoing model. The formalism turns what was an informal notion ('discourse context') into a precise, compositional object whose structure can be reasoned about rigorously."
```

## Explainer

Your study of discourse analysis and formal pragmatics gave you two things: an understanding that meaning extends beyond the sentence, and some tools for thinking about how context shapes interpretation. **Discourse Representation Theory** (DRT), developed by Hans Kamp in the 1980s, provides the formal architecture that makes those intuitions precise. Its central insight is deceptively simple: to understand a discourse, you don't just interpret each sentence in isolation — you build a running mental model, and each new sentence updates that model.

The formal object DRT introduces is the **Discourse Representation Structure** (DRS), which you can think of as a box containing two things: a list of **discourse referents** (roughly, the individuals the discourse has introduced) and a list of **conditions** (propositions that are true of those referents in the model). When you hear "A farmer owns a donkey," the DRS box gets two new referents — call them *x* (the farmer) and *y* (the donkey) — plus the conditions *farmer(x)*, *donkey(y)*, and *owns(x,y)*. Nothing about this is exotic yet. The payoff comes with anaphora. When the next sentence is "He beats it," the pronouns *he* and *it* need to find antecedents. DRT says they can access the discourse referents already in scope: *he* can pick up *x* (the farmer), *it* can pick up *y* (the donkey). The conditions *beats(x,y)* get added to the same box. The discourse is now a single structured representation rather than two independent sentences.

This matters because it solves the **donkey anaphora** problem — a famous puzzle in formal semantics. "Every farmer who owns a donkey beats it" seems simple, but the pronoun *it* cannot be a simple variable bound by "a donkey" in the scope of "every farmer," because the scoping doesn't work out. DRT handles it elegantly: the indefinite "a donkey" inside the restrictor of "every farmer" introduces a referent that is accessible to the pronoun in the matrix clause, because both are inside the same conditional DRS structure. The box architecture tracks accessibility in a way that standard predicate logic does not.

**Presupposition accommodation** is the other major application. When someone says "A woman entered. She had three children," the second sentence presupposes the existence of three children — information not previously established. Rather than crashing, the discourse interpreter **accommodates** the presupposition by adding the three children as new referents to the DRS, inferring that they must exist because the sentence requires them to. DRT provides a principled account of when accommodation is possible (the presupposition is plausible and consistent with the model) and when it fails. This connects directly to the formal pragmatics you studied: accommodation is the mechanism by which context is dynamically enriched as discourse unfolds. The DRS is not a static representation of a situation; it is the record of an ongoing interpretive process in which each sentence both draws on and updates the shared context that speaker and hearer are building together.
