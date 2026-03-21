---
id: selectional-restrictions
title: Selectional Restrictions and Lexical Licensing
domain: language-and-communication
course: linguistics
prerequisites:
- id: semantic-linking-to-syntax
  type: hard
- id: verb-complements-basic
  type: soft
builds-toward:
- lexical-organization-formal
tags:
- semantics
- lexicon
- subcategorization
- constraints
stage: formal-systems
status: draft
---

# Selectional Restrictions and Lexical Licensing

## Core Idea
Predicates impose selectional restrictions—constraints on the semantic types of their arguments. Verbs like "eat" require animate subjects and consumable objects; "believe" requires sentient subjects. These restrictions are lexical properties stored in a predicate's argument structure and may reduce to semantic well-formedness conditions (arguments must denote individuals with specific properties).

## Questions

```yaml
- question: "The sentence 'The rock ate sadness' is odd. What type of violation does it represent, and what distinguishes this from a sentence like 'Ate the rock sadness'?"
  type: multiple-choice
  options:
    - "Both sentences violate syntactic rules; they are equally ungrammatical"
    - "'The rock ate sadness' is syntactically well-formed but selectionally anomalous — it violates the semantic type constraints 'eat' places on its arguments; 'Ate the rock sadness' is syntactically malformed regardless of meaning"
    - "'The rock ate sadness' is selectionally anomalous and therefore also ungrammatical"
    - "Both sentences are acceptable in poetic contexts, so neither violates any linguistic rule"
  answer: 1
  explanation: "This distinction is the core of selectional restrictions. 'The rock ate sadness' follows English word order perfectly (Subject-Verb-Object) and uses a normal transitive verb construction — it is syntactically impeccable. The oddness is purely semantic: 'eat' requires an animate subject and a consumable object, and rocks and sadness satisfy neither constraint. 'Ate the rock sadness' scrambles the phrase structure in a way that violates the grammar regardless of meaning. Selectional restriction violations and syntactic violations are different phenomena at different levels of linguistic description."

- question: "A poet writes 'Time devoured the years.' How do selectional restrictions explain why this phrase is interpretable as metaphor rather than simply anomalous?"
  type: multiple-choice
  options:
    - "Metaphors are exempt from selectional restrictions entirely, so the sentence is processed literally"
    - "The selectional violation is productive: because 'devour' requires a consumable object and 'years' is abstract, the listener must construct a non-literal mapping — the violation signals that metaphorical interpretation is required"
    - "The sentence is grammatical because 'years' can be consumed metaphorically, satisfying the restriction"
    - "Selectional restrictions only apply to spoken language; written poetry is not subject to them"
  answer: 1
  explanation: "Selectional restrictions are the background against which metaphor figures. A listener who knows 'devour' selects for [+consumable] objects encounters a mismatch when the object is an abstract temporal span. This mismatch, rather than blocking interpretation, signals that a literal reading is not intended and triggers a search for an analogical mapping — perhaps that time consumes or wastes years in the way a hungry animal consumes food. Metaphor works precisely because the violation is recognized as deliberate. If the listener did not know the restriction, the metaphorical force would be lost."

- question: "Selectional restrictions are properties of individual words (predicates), stored in the lexicon, not rules of general grammar that apply uniformly to all predicates."
  type: true-false
  answer: true
  explanation: "This is the defining characteristic of selectional restrictions. 'Elapse' requires a temporal subject (time elapses, events elapse — rocks do not). 'Blond' requires a head noun denoting something that bears hair. 'Devour' requires an edible object. These are not properties derivable from a general rule like 'subjects must be animate' — each predicate carries its own set of filters, and the set differs from predicate to predicate even among closely related words (compare 'eat' vs. 'consume' vs. 'ingest'). The lexicon is where this information is stored; acquiring a verb includes acquiring its selectional requirements."

- question: "If a sentence violates a selectional restriction, it is ungrammatical in the same way as a sentence with a syntactic error."
  type: true-false
  answer: false
  explanation: "Selectional restriction violations and syntactic violations are distinguishable both descriptively and theoretically. A syntactically ungrammatical sentence like '*The ate rock' cannot be interpreted; native speakers consistently reject it and cannot assign it a meaning. A selectionally anomalous sentence like 'The rock ate sadness' is perfectly interpretable — it can function as metaphor, appear in fiction, or describe an impossible situation. Native speakers typically describe it as 'odd' or 'weird' rather than 'ungrammatical.' This contrast is part of the evidence that syntax and lexical-semantic constraints operate at different levels."

- question: "Explain why understanding selectional restrictions is necessary to give a complete account of how metaphor works."
  type: short-answer
  answer: "Metaphor works by deliberate violation of selectional restrictions: a predicate is applied to an argument that fails its semantic filters, and this mismatch signals to the listener that literal interpretation is impossible — triggering a search for an analogical or extended meaning. Without the concept of selectional restrictions (the rules being violated), there is no account of what makes a metaphor a violation rather than just an unusual word combination. The restrictions define normality; the metaphor exploits a departure from that norm. A speaker who said 'time devoured the years' to a listener who did not know 'devour' selects for consumable objects would generate no metaphorical effect — the listener would simply be confused."
  explanation: "This is why selectional restrictions are not just a constraint but a resource. They establish the semantic expectations against which figurative language operates. Grasping this turns the apparent 'limitation' of selectional restrictions into an explanation of linguistic creativity: the constraints are what make metaphor possible and interpretable. The same logic extends to personification, synesthesia, and other tropes that involve applying predicates to arguments of the wrong type — in every case, the violation is meaningful only because the restriction is known."
```

## Explainer

From your work on semantic linking to syntax, you know that verbs impose requirements on their arguments — not just structural requirements (a subject must appear, an object may appear) but semantic ones. The verb "eat" does not just require two noun phrases; it requires that the subject be animate and the object be something consumable. "The rock ate sadness" violates no syntactic rules but is semantically deviant. These semantic constraints are **selectional restrictions**: requirements that a predicate places on the semantic types of its arguments.

Selectional restrictions are stored as part of a word's lexical entry — they are properties of individual predicates, not derived from general grammar rules. "Elapse" requires a temporal subject (time elapses, but rocks do not). "Blond" requires a head noun denoting something that can bear hair. "Devour" requires an edible object. Each predicate carries a set of **semantic filters** that its arguments must pass. If an argument fails a filter, the result is selectionally anomalous — it might be interpretable as metaphor or be felicitous in a fictional context, but in literal use it is odd in a way that purely syntactic violations are not.

The theoretical question is whether selectional restrictions are a separate constraint level or reduce to more general semantic well-formedness. On the **semantic features** approach, nouns carry bundles of features (±animate, ±human, ±concrete), and verbs specify which values their arguments must carry: "eat" requires [+animate] for its subject. On the **type-theoretic** approach, predicates impose type requirements: "elapse" selects for an argument of type *time interval*, not type *individual*. Both approaches capture the core intuition — arguments must be the right kind of thing — but they make different predictions about borderline cases and how metaphorical extensions are licensed.

Understanding selectional restrictions illuminates how metaphor works. When we say "time devoured the years" or "anxiety gnawed at her confidence," we deliberately violate selectional restrictions to generate non-literal meaning. The violation is productive precisely because the listener recognizes it as a violation: they know "devour" selects for a consumable object, and when the object is abstract, that mismatch prompts them to construct an analogy. Selectional restrictions are the background against which figurative language figures — knowing the rules is what gives a violation meaning.
