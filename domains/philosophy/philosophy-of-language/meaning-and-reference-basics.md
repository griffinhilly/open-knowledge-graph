---
id: meaning-and-reference-basics
title: 'Meaning and Reference: Core Distinctions'
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: philosophy-of-language-intro
  type: hard
builds-toward:
- frege-sense-and-reference
- russell-definite-descriptions
- putnam-semantic-externalism
- grice-conversational-implicature
tags:
- reference
- meaning
- semantics
- core-concepts
stage: abstract-reasoning
status: validated
---

# Meaning and Reference: Core Distinctions

## Core Idea
The core puzzle of meaning is that words seem to stand for things in the world (reference), yet the meaning of a word is not simply its referent—the word 'morning star' and 'evening star' refer to the same object but have different meanings. We must distinguish between what a word refers to and what the word means.

## Questions

```yaml
- question: "'Morning star' and 'evening star' both refer to Venus. What does Frege's puzzle about these expressions show?"
  type: multiple-choice
  options:
    - "That proper names are ambiguous and should be avoided in philosophical argument"
    - "That two expressions can refer to the same object while differing in meaning, so meaning cannot simply be reference"
    - "That astronomical terms have no precise meaning without empirical verification"
    - "That co-referring expressions are always interchangeable in any context"
  answer: 1
  explanation: "If meaning were just reference, 'morning star = evening star' would be as trivially uninformative as 'Venus = Venus.' But it was a substantive discovery that these expressions pick out the same planet. This shows that expressions can share a referent while conveying different information — meaning must involve more than reference alone."

- question: "The meaning of a proper name like 'Aristotle' is simply the individual it picks out in the world."
  type: true-false
  answer: false
  explanation: "This is the 'direct reference' view, which many philosophers reject on grounds of Frege's puzzle and related problems. If meaning were just reference, then 'Aristotle' and any other term referring to Aristotle would be semantically identical, and 'Aristotle is Aristotle' would be just as informative as 'Aristotle was a philosopher' — clearly they aren't. Frege argued we need sense (mode of presentation) in addition to reference to explain informational content."

- question: "Why does the fact that 'Lois believes Superman can fly' can be true while 'Lois believes Clark Kent can fly' is false matter for the theory of meaning?"
  type: short-answer
  answer: "If meaning were just reference, substituting co-referring terms should always preserve truth. But 'Superman' and 'Clark Kent' refer to the same person, yet substituting one for the other in belief contexts changes truth value. This shows that meaning involves more than reference — cognitive or descriptive content (how an expression presents its referent) must also be part of meaning."
  explanation: "This is the problem of substitution failure in intensional (belief, desire, knowledge) contexts. It is one of the strongest arguments that we need a notion of meaning beyond reference — something like Frege's sense or a descriptive content — to explain why co-referring terms are not always interchangeable."
```

## Explainer

Philosophy of language begins with an observation that seems obvious but turns out to be puzzling: words stand for things. "Paris" stands for a city, "red" applies to red things, "runs" is true of things that run. This relationship between language and world is called reference. But if you examine it carefully, reference alone cannot be all there is to meaning — and the morning star/evening star example makes this vivid.

"Morning star" and "evening star" both refer to the planet Venus. If meaning just *were* reference, these two phrases would mean exactly the same thing, and the statement "the morning star is the evening star" would be as trivially true as "Venus is Venus." But that's not how it seems. Ancient astronomers who discovered that the bright object visible in the pre-dawn sky and the bright object visible after sunset were the same planet were learning something — it was a real discovery, not a verbal tautology. Two expressions, one referent, different meanings. Frege's conclusion: meaning and reference are distinct.

The distinction Frege drew — between *sense* (how an expression presents its referent, its mode of presentation) and *reference* (the object picked out) — will become central when you study his Sinn und Bedeutung. For now, the key intuition is that the sense of "morning star" is something like *the celestial body visible in the morning sky*, while the sense of "evening star" is *the celestial body visible in the evening sky*. They present the same object under different descriptions. Knowing both senses and knowing that they refer to the same thing is knowing something extra.

This distinction has cascading consequences. If meaning were just reference, substituting one co-referring term for another should never change truth value. But consider: "Lois believes Superman can fly" can be true while "Lois believes Clark Kent can fly" is false, even though Superman and Clark Kent are the same person. Substituting co-referring names inside belief reports can change whether the report is true. This *substitution failure* is one of the most powerful arguments that meaning involves more than reference — some further descriptive or cognitive content that tracks how the referent is presented to the believer.

Reference works differently for different kinds of expressions, and distinguishing them is part of the foundational toolkit for philosophy of language. Singular terms (proper names, definite descriptions like "the tallest building") pick out individual objects. General terms ("human," "red") apply to or are true of many things. Predicates express properties. These all "refer" in different senses of that word, and getting clear on the distinctions is the groundwork for everything that follows — Frege's full theory, Russell's puzzles about "the present King of France," and eventually Kripke's challenge to the whole descriptivist tradition.
