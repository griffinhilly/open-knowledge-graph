---
id: formal-pragmatics-context
title: Formal Pragmatics and Context
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: linguistic-pragmatics
  type: hard
- id: montague-semantics
  type: soft
builds-toward:
- implicature-and-logical-form
- discourse-representation-theory
tags:
- pragmatics
- context
- formal
stage: advanced
status: draft
---

# Formal Pragmatics and Context

## Core Idea
Formal pragmatics extends Montague's compositional semantics by incorporating context as a formal component. Meanings depend on contextual parameters (speaker, hearer, time, location). Indexicals like 'I' and 'here' have constant character (the rule for finding their referent) but varying content (the actual referent depending on context). This formalizes how context updates affect meaning dynamically.

## Explainer

From linguistic pragmatics you know that utterance meaning goes beyond sentence meaning — what a speaker communicates depends on context, shared knowledge, and communicative intent. From Montague semantics you know how to assign meanings compositionally: each expression has a semantic value, and the meaning of a complex expression is computed from the meanings of its parts. Formal pragmatics asks: how do we keep that compositional rigor while also accounting for the fact that context changes what expressions mean? The answer is to make context itself a formal object — an element of the semantic machinery rather than just background.

The key move comes from David Kaplan's theory of **indexicals**. An indexical is an expression whose reference shifts with context: "I," "you," "here," "now," "today." On the surface, indexicals are a problem for compositional semantics — if "I" means something different in every utterance, how can we give it a stable semantic entry? Kaplan's solution is to distinguish two levels of meaning. Every indexical has a constant **character**: a rule or function that specifies how to find its referent given a context. "I" always means "the speaker of this context." This character never changes. But the **content** — the actual referent in a specific context — does change: when you say "I," the content is you; when I say "I," the content is me. Character is the meaning of the word; content is its contextual value. This two-level architecture lets formal semantics handle indexicals without abandoning compositionality.

Context is formalized as an **index** or tuple of parameters: typically at minimum a speaker, a hearer, a time, a location, and a possible world. An utterance of "I am here now" is evaluated against this index. The sentence is true at an index if and only if the speaker of that index is at the location of that index at the time of that index — which is trivially true for any coherent context of utterance, explaining the near-tautological feel of the sentence despite its apparent informativeness. Different sentences are sensitive to different parameters: tense expressions exploit the time parameter, "here" and "there" exploit location, modals like "might" and "must" exploit possible worlds. Formal pragmatics charts which expressions are sensitive to which parameters and how.

Where formal pragmatics extends beyond Kaplan is in modeling how context is not just consumed but **updated** through discourse. As a conversation unfolds, the common ground between speaker and hearer changes: each assertion (if accepted) adds to what both parties take to be known. Robert Stalnaker's framework treats context as a **context set** — the set of possible worlds still compatible with what has been established in the discourse. A felicitous assertion eliminates possibilities from the context set; a question invites the hearer to provide information that narrows it further. This dynamic view of context connects formal semantics to the study of discourse coherence and pragmatic inference. It explains why what you can appropriately say at point B in a conversation depends on what was said at point A — context is not just the world outside the conversation but the cumulative record of the conversation itself.
