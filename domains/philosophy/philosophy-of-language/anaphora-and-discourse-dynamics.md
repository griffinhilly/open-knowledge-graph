---
id: anaphora-and-discourse-dynamics
title: Anaphora and Discourse Context
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: first-order-semantics
  type: hard
- id: russell-definite-descriptions
  type: soft
builds-toward:
- ellipsis-and-implicit-content
- discourse-coherence-linguistic
tags:
- discourse
- anaphora
- pronouns
- context
stage: advanced
status: draft
---

# Anaphora and Discourse Context

## Core Idea
Anaphoric pronouns refer back to previously introduced discourse referents. Dynamic semantic approaches treat discourse as building up a context of available referents, with pronouns and expressions accessing this evolving context structure.

## How It's Best Learned
Analyze multi-sentence discourses, identifying what serves as antecedent for each pronoun. Examine cases where anaphora is blocked by syntactic constraints to understand binding principles.

## Questions

```yaml
- question: "Consider the sentence: 'Every farmer who owns a donkey beats it.' Why does this sentence pose a problem for the standard treatment of pronouns as either bound variables or directly referential expressions?"
  type: multiple-choice
  options:
    - "The sentence is grammatically ill-formed, so standard semantics simply doesn't apply"
    - "'It' cannot be a bound variable (nothing in the syntax binds it within the right scope) and cannot be a directly referential expression (there is no particular donkey being referred to), leaving the co-variation inference pattern unexplained"
    - "First-order logic lacks quantifiers that can range over animals, so the sentence is undefinable"
    - "The problem is pragmatic, not semantic — context supplies the missing donkey referent"
  answer: 1
  explanation: "This is the classic 'donkey sentence.' If 'it' were a bound variable, something in the syntax would need to bind it — but 'a donkey' is inside a relative clause and cannot bind 'it' in the main clause. If 'it' were directly referential (like a name), it would pick out a specific donkey — but the sentence makes a universal claim about all farmer-donkey pairs, not about any particular donkey. The inference pattern (each farmer beats their own donkey) falls through the cracks of both standard analyses, motivating dynamic approaches."

- question: "In dynamic semantics, what is the fundamental difference in how sentence meanings are characterized compared to classical truth-conditional semantics?"
  type: multiple-choice
  options:
    - "Dynamic semantics assigns truth values to individual words rather than to whole sentences"
    - "Sentence meanings are relations between input context states and output context states — they transform the discourse context rather than having static truth conditions"
    - "Dynamic semantics abandons truth conditions entirely and replaces them with speech act types"
    - "Sentence meanings are evaluated relative to the speaker's intentions rather than to discourse context"
  answer: 1
  explanation: "In classical truth-conditional semantics, a sentence's meaning is a set of possible worlds (the worlds in which the sentence is true) — a static object. In dynamic semantics, meaning is a program or transition function: a sentence takes an input information state, processes it, and yields an updated output state. Indefinites introduce new discourse referents; subsequent sentences can access those referents via pronouns. This shift from static propositions to context-update functions is the central theoretical innovation."

- question: "In dynamic semantics, indefinite noun phrases like 'a farmer' function by picking out a specific individual that is already present in the discourse context."
  type: true-false
  answer: false
  explanation: "It is precisely the other way around: indefinite noun phrases *introduce* new discourse referents into the context. Pronouns are what *access* referents that are already available. This asymmetry is fundamental to the dynamic approach. 'A donkey entered the field' introduces a donkey referent; 'It brayed' picks up that referent. If indefinites merely picked out pre-existing referents, dynamic semantics would offer no advantage over classical approaches."

- question: "The failure of standard bound-variable and directly-referential analyses to handle donkey sentences was a key motivation for developing dynamic approaches to natural language meaning."
  type: true-false
  answer: true
  explanation: "Donkey sentences were a historically important trigger for developing dynamic semantics (particularly Discourse Representation Theory by Kamp, and Dynamic Predicate Logic by Groenendijk and Stokhof). The bound-variable analysis requires an unattested syntactic binding relationship; the directly-referential analysis requires a specific donkey referent that doesn't exist in a universally quantified statement. Dynamic semantics handles both by making quantifiers introduce referents that can be accessed within their scope — including from subsequent sentences."

- question: "How does dynamic semantics differ from static truth-conditional semantics in its account of what a sentence means, and why does this difference matter for handling pronouns?"
  type: short-answer
  answer: "In static truth-conditional semantics, a sentence's meaning is a fixed truth condition — a proposition that is true or false at possible worlds, independent of what has been said before. In dynamic semantics, a sentence's meaning is a context-update function: a relation that maps an input context (a set of available discourse referents and information about them) to an output context. This matters for pronouns because pronouns depend on what referents have been introduced in prior sentences. By making sentence meaning a context-transformation rather than a static proposition, dynamic semantics can formally represent how later sentences inherit referents introduced by earlier ones."
  explanation: "The practical payoff is that dynamic semantics can compositionally derive the reading of donkey sentences and cross-sentential anaphora within a unified framework, without stipulating special rules for each case. The shift is analogous to treating program meaning as what a subroutine *does* to memory state, rather than as a static value the subroutine *holds*."
```

## Explainer

In first-order semantics, variables get their values from a fixed assignment function—you set the value of x once, and then x refers to that value throughout. Anaphora shows that natural language works differently: the value of a pronoun depends on how the discourse has unfolded. "John walked in. He sat down." The pronoun "he" picks up its reference from the previous sentence, not from any assignment fixed in advance. This is the basic phenomenon of **anaphora**: an expression whose interpretation depends on something introduced earlier in the discourse.

The traditional approach—treating pronouns as directly referential or as bound variables—handles simple cases but breaks down at a famous class of examples called **donkey sentences**. "Every farmer who owns a donkey beats it." Here "it" can't be a bound variable (nothing in the syntax binds it in the right way) and can't be a simple referential pronoun (there's no particular donkey to refer to). Russell's theory of descriptions, which your prerequisite covered, doesn't help directly either. The pronoun seems to range over donkeys in a way that is somehow controlled by the indefinite "a donkey" inside the relative clause.

**Dynamic semantics** offers the key insight: treat discourse not as a static set of sentences but as a process of updating a context. Each sentence updates the **discourse context** by introducing new discourse referents and adding information about them. Indefinite noun phrases like "a farmer" or "a donkey" introduce new referents into the context; pronouns pick up referents that are already available in the context. Formally, this is modeled by treating sentence meanings as relations between input and output contexts rather than as static truth conditions. A sentence processes an incoming information state and produces an updated one, potentially adding new referents to the available stock.

This dynamic approach handles donkey sentences by allowing quantifiers to "reset" and re-bind referents: "a donkey" introduces a referent within the scope of the universal, and "it" picks up that referent within the same quantificational scope. It also explains **binding constraints**: why "He loves John" resists a reading where "he" refers to John (anti-coreference), while "John loves himself" requires coreference. Binding principles constrain which discourse referents are syntactically accessible to a given pronoun, and dynamic semantics provides a framework for tracking which referents are in scope at any point in the discourse. The upshot is a richer picture of meaning: understanding a sentence means updating your model of the discourse context, not just evaluating a static truth condition.
