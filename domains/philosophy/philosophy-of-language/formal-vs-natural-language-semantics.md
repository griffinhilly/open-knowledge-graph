---
id: formal-vs-natural-language-semantics
title: Formal Language and Natural Language Semantics
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: truth-conditions-and-meaning
  type: hard
- id: compositionality-principle
  type: soft
- id: first-order-semantics
  type: hard
- id: model-theory-basics
  type: soft
builds-toward:
- semantic-underdetermination-context
tags:
- formal-logic
- natural-language
- semantics
stage: formal-systems
status: draft
---

# Formal Language and Natural Language Semantics

## Core Idea
Natural language differs from formal logic in crucial ways: it is ambiguous, context-dependent, imprecise, and contains many non-truth-functional expressions. Formal semantic methods apply to natural language, but require adapting logical tools to preserve both accuracy and applicability.

## Questions

```yaml
- question: "A logician translates 'Mary believes the president is corrupt' into logic and then substitutes 'the CEO of Axiom Corp' for 'the president,' since they are the same person. The resulting sentence attributes to Mary the belief that the CEO of Axiom Corp is corrupt. What goes wrong?"
  type: multiple-choice
  options:
    - "Nothing — if the president and the CEO are identical, substitution preserves truth in all contexts"
    - "The substitution fails because 'the president' is an indexical whose reference shifts with context"
    - "Attitude reports create opaque contexts where substituting co-referring terms can change truth value — Mary may not know the two descriptions refer to the same individual"
    - "The problem is grammatical, not semantic — the substitution is syntactically ill-formed"
  answer: 2
  explanation: "Attitude reports like 'Mary believes that...' create what are called intensional (opaque) contexts. Standard first-order logic assumes that co-referring terms are intersubstitutable everywhere (the principle of extensionality). But within the scope of 'believes,' substitution can change truth value: Mary may sincerely believe the president is corrupt without knowing the president is the CEO. This failure of substitutivity is one of the central challenges that formal semantics must address when extending logical tools to natural language."

- question: "The sentence 'It's raining' cannot be assigned a definite truth value by a standard model-theoretic semantics alone. What additional machinery is required?"
  type: multiple-choice
  options:
    - "A possible-worlds framework to evaluate the sentence across all possible states of affairs"
    - "A context parameter specifying at minimum a location (and possibly a time) relative to which truth is evaluated"
    - "A probability distribution over rain events, since the sentence is inherently probabilistic"
    - "No additional machinery — standard models assign truth values to all sentences"
  answer: 1
  explanation: "'It's raining' is an indexical sentence: its truth conditions depend on where and when it is uttered. Without a context specifying location (and time), there is no determinate answer. Formal semantics handles this by adding a context parameter — a tuple including speaker, location, time, etc. — that supplements the model. Option A (possible worlds) is used for modality and counterfactuals but does not by itself resolve context-dependence. Option D is wrong because standard Tarskian model theory was designed for formal languages with no indexicals."

- question: "Indexical expressions like 'I,' 'here,' and 'now' cannot be handled adequately by standard model theory and require a separate context parameter that varies with each utterance situation."
  type: true-false
  answer: true
  explanation: "Standard model theory assigns fixed interpretations to constants and predicates relative to a model. Indexicals violate this: 'I' refers to the speaker (who changes with each utterance), 'here' refers to the location of utterance, 'now' to the time. To handle this, Kaplan and others extended the semantic framework with a context — a tuple of speaker, location, time, world — so that the interpretation of an indexical is a function from contexts to referents. This extension is necessary and not available within standard first-order model theory alone."

- question: "Applying formal logic to natural language is primarily a matter of translation — once you identify the correct logical form of an English sentence, standard first-order semantics handles the rest."
  type: true-false
  answer: false
  explanation: "This is the naive view that the topic is designed to refute. Natural language features — ambiguity (the same sentence has multiple logical forms), context-dependence (truth conditions shift with speaker/location/time), opacity in attitude reports, non-truth-functional conditionals, generics, tense, aspect, modality, and questions — cannot be handled by a simple translation into first-order logic. Formal semantics for natural language is an active, ongoing empirical and theoretical enterprise that requires substantial extensions: possible-worlds semantics, type theory, dynamic logic, context parameters, and more."

- question: "Why does the context-dependence of gradable adjectives like 'tall' pose a challenge for compositional semantics, and how does formal semantics attempt to address it?"
  type: short-answer
  answer: "Gradable adjectives like 'tall' are implicitly relative to a comparison class: 'tall for a jockey' and 'tall for a basketball player' can be simultaneously true and false of the same person. Compositional semantics builds sentence meanings from parts, but if the meaning of 'tall' shifts with context rather than being a fixed predicate, the composition machinery must be extended. Formal semantics addresses this by treating gradable adjectives as relations to a standard or as functions from contexts (including a comparison class parameter) to extensions, rather than as context-independent predicates. The key insight is that compositionality is preserved, but the semantic values of context-sensitive expressions are themselves context-dependent functions rather than fixed sets."
  explanation: "This example generalizes to many natural language expressions: evaluative terms ('expensive,' 'large'), relational expressions ('local,' 'nearby'), and pronouns all require contextual parameters. Formal semantics must track these parameters systematically throughout the compositional derivation — a significant complication over standard first-order semantics for formal languages."
```

## Explainer

You already know how formal languages work from your study of first-order logic: a **formal language** has a fixed syntax, an explicit semantics defined over models, and no ambiguity — every well-formed formula has exactly one meaning relative to an interpretation. When you learned model theory, you saw how a model assigns objects to constants, extensions to predicates, and truth conditions to sentences in a fully determined, mechanical way. Natural language — the English, French, or Swahili you grew up speaking — operates very differently, and the gap between the two is where most of the philosophical action in semantics lives.

The most immediate difference is **ambiguity**. In first-order logic, "bank" simply does not appear — you would introduce a predicate BANK and specify what it applies to. In English, "She went to the bank" is genuinely ambiguous between a financial institution and a riverside, and listeners resolve the ambiguity using context, prior discourse, and world knowledge. Formal systems eliminate ambiguity by design; natural language lives with it and relies on pragmatic inference to recover the intended meaning. This means that a naïve translation of natural language into logic — treating each English sentence as having a single logical form — would misrepresent the phenomenon.

A second gap is **context-dependence**. You know that truth conditions specify what would make a sentence true or false. But many natural language sentences cannot be assigned truth conditions without knowing the context of utterance. "I am tired" is true in some contexts and false in others — the word "I" shifts referent with each speaker. "It's raining" needs a location. "That is tall" requires a comparison class — tall for a building, a person, or a blade of grass? Formal semantics handles this through **indexicals** (expressions whose reference is fixed by context) and **context parameters** (a context providing speaker, time, location, etc.) that supplement the model. The compositional machinery you learned — how complex meanings are built from parts — must be extended to take these parameters into account.

The deeper challenge is that natural language contains constructions that resist direct translation into first-order logic. Ordinary conditionals ("If it rains, the game is canceled") seem to work differently from material conditionals. Attitude reports ("Mary believes the president is corrupt") create contexts where substituting co-referring names can change truth value — a phenomenon that violates the substitutivity you expect from standard logic. Tense, aspect, modality, generics ("Tigers are striped") and questions all require extensions of the basic first-order toolkit. The project of **formal semantics for natural language** — pursued through tools like type theory, possible-worlds semantics, and dynamic logic — is precisely to find a systematic, compositional treatment of these phenomena that preserves the precision of formal methods while respecting the actual behavior of the language. The lesson is not that formal tools fail but that applying them to natural language is an ongoing, fine-grained empirical and theoretical enterprise, not a simple translation.

