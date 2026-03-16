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

## Explainer

In first-order semantics, variables get their values from a fixed assignment function—you set the value of x once, and then x refers to that value throughout. Anaphora shows that natural language works differently: the value of a pronoun depends on how the discourse has unfolded. "John walked in. He sat down." The pronoun "he" picks up its reference from the previous sentence, not from any assignment fixed in advance. This is the basic phenomenon of **anaphora**: an expression whose interpretation depends on something introduced earlier in the discourse.

The traditional approach—treating pronouns as directly referential or as bound variables—handles simple cases but breaks down at a famous class of examples called **donkey sentences**. "Every farmer who owns a donkey beats it." Here "it" can't be a bound variable (nothing in the syntax binds it in the right way) and can't be a simple referential pronoun (there's no particular donkey to refer to). Russell's theory of descriptions, which your prerequisite covered, doesn't help directly either. The pronoun seems to range over donkeys in a way that is somehow controlled by the indefinite "a donkey" inside the relative clause.

**Dynamic semantics** offers the key insight: treat discourse not as a static set of sentences but as a process of updating a context. Each sentence updates the **discourse context** by introducing new discourse referents and adding information about them. Indefinite noun phrases like "a farmer" or "a donkey" introduce new referents into the context; pronouns pick up referents that are already available in the context. Formally, this is modeled by treating sentence meanings as relations between input and output contexts rather than as static truth conditions. A sentence processes an incoming information state and produces an updated one, potentially adding new referents to the available stock.

This dynamic approach handles donkey sentences by allowing quantifiers to "reset" and re-bind referents: "a donkey" introduces a referent within the scope of the universal, and "it" picks up that referent within the same quantificational scope. It also explains **binding constraints**: why "He loves John" resists a reading where "he" refers to John (anti-coreference), while "John loves himself" requires coreference. Binding principles constrain which discourse referents are syntactically accessible to a given pronoun, and dynamic semantics provides a framework for tracking which referents are in scope at any point in the discourse. The upshot is a richer picture of meaning: understanding a sentence means updating your model of the discourse context, not just evaluating a static truth condition.
