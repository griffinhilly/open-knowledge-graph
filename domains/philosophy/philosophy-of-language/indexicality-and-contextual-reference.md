---
id: indexicality-and-contextual-reference
title: Indexicality and Demonstratives
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: indexicals-context-sensitivity
  type: hard
- id: semantic-underdetermination-context
  type: soft
tags:
- indexicals
- demonstratives
- context
stage: formal-systems
status: draft
---

# Indexicality and Demonstratives

## Core Idea
Indexical expressions like 'I,' 'now,' 'here' and demonstratives like 'this' and 'that' have a character—a rule for determining reference based on context—distinct from their content in a specific context. Kaplan's theory distinguishes these dimensions to handle the semantics of directly referential expressions.

## Questions

```yaml
- question: "Two people each utter the sentence 'I am hungry.' According to Kaplan's theory, which statement correctly describes what is shared and what differs between the two utterances?"
  type: multiple-choice
  options:
    - "Both utterances express the same proposition, since the sentence is identical"
    - "The character of 'I' differs for each speaker, which is why they refer to different people"
    - "The character of 'I' is the same for both — 'the speaker of the context' — but the content (who is referred to) differs, and therefore the propositions expressed differ"
    - "'I' is not directly referential because it picks out different individuals in different contexts"
  answer: 2
  explanation: "Character is the stable rule that all competent speakers share — for 'I,' the rule is 'the speaker of the context.' This never changes. Content is what that rule yields in a specific context: when Griffin utters 'I,' the content is Griffin; when you utter 'I,' the content is you. Same character, different content. The propositions expressed are genuinely different singular propositions. And 'I' remains directly referential precisely because it contributes the person themselves — not a descriptive condition — to the proposition once context has fixed the reference."

- question: "On Kaplan's theory, what does a competent speaker know when they know the meaning of the word 'now'?"
  type: multiple-choice
  options:
    - "The specific time at which they are currently speaking"
    - "The character of 'now' — the rule 'the time of utterance' — which is the same in every context and never changes"
    - "A definite description equivalent to 'the moment I happen to be speaking'"
    - "A Fregean sense that picks out the time indirectly through a description"
  answer: 1
  explanation: "Kaplan's key insight is that linguistic competence is knowledge of character, not knowledge of content. A speaker who knows the word 'now' knows the rule for determining its referent from any context — namely, look to the time of the utterance. They do not need to know which specific time it is to understand the word. The character is constant; the content varies. This is what distinguishes indexicals from ordinary proper names (whose character just is their content) and from descriptions (which don't directly refer to individuals at all)."

- question: "Because 'I' picks out different individuals in different contexts of utterance, it is not directly referential — it expresses a descriptive condition like 'the current speaker' rather than contributing the individual directly to the proposition."
  type: true-false
  answer: false
  explanation: "This conflates character with content. 'I' is directly referential precisely because, once context fixes the referent, the expression contributes just the individual — not a description — to the proposition expressed. The proposition I express by saying 'I am hungry' is the singular proposition <Griffin, hungry>, not the general proposition <whoever is currently speaking, hungry>. The context-sensitivity of indexicals is captured at the level of character (the rule), not at the level of content (which is object-involving and directly referential once the context is fixed)."

- question: "In Kaplan's framework, the character of a pure indexical like 'here' is constant across all contexts of utterance."
  type: true-false
  answer: true
  explanation: "Character is the linguistic meaning of an expression — what a competent speaker knows when they know how to use the word. For pure indexicals, this rule is entirely stable: 'here' always means 'the place of the context of utterance,' regardless of where or when it is used. What varies is the content — the specific place picked out in each context. Character is what stays constant; content is what the character delivers in a particular context."

- question: "What is the difference between the character and the content of an indexical expression in Kaplan's theory, and why does the framework need both levels rather than just one?"
  type: short-answer
  answer: "The character of an indexical is the stable rule that determines its referent given a context — for 'I,' this is 'the speaker of the context'; for 'now,' it is 'the time of utterance.' Character is what a competent speaker knows: it is the linguistic meaning, constant across all contexts. The content is what the character yields in a specific utterance — the actual individual, time, or place referred to. Kaplan needs both levels because a single level cannot explain two things simultaneously: (1) why 'I' is semantically the same word whoever uses it (same character) and (2) why different utterances of 'I am hungry' express genuinely different propositions (different content/referent). Character explains linguistic competence; content explains propositional contribution. Without character, context-sensitivity is inexplicable; without content, we can't distinguish what different utterances assert."
```

## Explainer

From your prerequisite study of indexicals and context-sensitivity, you know that expressions like "I," "now," "here," "today," and "this" shift their reference depending on who uses them, when, and where. I utter "I am hungry" — the word "I" refers to me. You utter the same sentence — "I" refers to you. Same word, different reference. This context-dependence is the basic phenomenon. What **Kaplan's theory** does is give a systematic two-level semantic framework that explains exactly how this works.

The first level is **character**: the rule or function that, given a context of utterance, determines the content expressed. The character of "I" is something like: *the speaker of the context*. The character of "now" is: *the time of utterance*. The character of "here" is: *the place of utterance*. Characters are stable across all contexts — the character of "I" never changes, which is why you know how to use it correctly. Characters are the linguistic meaning in the fullest sense: what a competent speaker knows when they know what an expression means.

The second level is **content**: what the expression actually refers to or expresses in a *particular* context. When I say "I" in my utterance, the content is me — Griffin — and that content is constant across possible worlds. This is what makes Kaplan's indexicals **directly referential**: once the context fixes the reference, the expression contributes just the object itself to the proposition expressed, not a description. The proposition expressed by "I am hungry" (uttered by me) is the singular proposition *<Griffin, hungry>* — true at a possible world if and only if Griffin is hungry there.

**Demonstratives** like "this" and "that" complicate the picture because they seem to require a directing intention in addition to context. When I say "that statue," I'm not just pointing to a contextually salient object — I'm directing attention to something specific, and different intentions could fix different referents even holding the context fixed. Kaplan distinguished "pure indexicals" (where context alone fixes reference, like "I") from "true demonstratives" (where a directing intention is needed). This distinction matters for explaining cases where demonstratives misfire, succeed despite pointing errors, or pick out objects the speaker didn't intend. Understanding character and content as distinct dimensions is the key to navigating these cases — and to understanding why the same sentence can express different propositions in different mouths.
