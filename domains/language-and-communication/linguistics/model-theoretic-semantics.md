---
id: model-theoretic-semantics
title: Model-Theoretic Semantics and Truth Conditions
domain: language-and-communication
course: linguistics
prerequisites:
- id: predicate-logic-semantics
  type: hard
- id: possible-worlds-semantics
  type: hard
builds-toward:
- syntax-semantics-interface-formal
tags:
- semantics
- model-theory
- truth-conditions
- extensions-intensions
stage: advanced
status: draft
---

# Model-Theoretic Semantics and Truth Conditions

## Core Idea
Model-theoretic semantics defines meaning as truth in a model. A model specifies a domain of individuals and assigns truth values to atomic propositions. Compositional interpretation assigns denotations to parts and recursively computes whole meanings. Extensions capture what a word refers to; intensions capture the concept or rule for picking out referents.

## Explainer

From predicate logic semantics, you know how to translate sentences into formulas using predicates, variables, quantifiers, and logical connectives. From possible-worlds semantics, you know that meaning can be analyzed in terms of truth across different possible situations — that the meaning of a sentence is (roughly) the set of worlds in which it is true. Model-theoretic semantics fuses these ideas into a rigorous formal framework: it makes precise exactly what it means for a sentence to be true by specifying how linguistic expressions are interpreted relative to a formal **model**.

A **model** M is a mathematical structure consisting of a domain D — a set of individual entities — and an interpretation function I that assigns semantic values to the non-logical vocabulary. For a predicate like "barks," the interpretation function assigns it the set of all entities in D that have the barking property. For an individual constant like "Fido," it assigns a specific element of D. Combining these: "Fido barks" is true in M if and only if the entity I assigns to "Fido" is a member of the set I assigns to "barks." This is the core of truth-conditional semantics — meaning is modeled as a relation between linguistic expressions and formal structures, and truth is the central semantic property.

The distinction between **extension** and **intension** is the bridge from a single model to possible-worlds reasoning. The extension of an expression is its semantic value in the current model — the actual set of entities the predicate picks out, or the actual individual a name refers to. The intension is the *function* from possible worlds to extensions — the rule or concept that determines what the expression refers to in each possible situation. "The morning star" and "the evening star" have the same extension (both pick out Venus), but different intensions (different modes of presentation), which is why "The morning star is the evening star" is informative in a way that "The morning star is the morning star" is not. This distinction is essential for analyzing belief contexts, necessity, and other intensional phenomena.

**Compositionality** is the principle that the semantic value of a complex expression is computed from the semantic values of its parts and their mode of combination. This is what makes model-theoretic semantics a genuine theory of meaning rather than a lookup table. You don't need to directly interpret "Every barking dog frightened some child" — you compute its meaning systematically: the universal quantifier takes a predicate and returns a generalized quantifier, which combines with the verb phrase's meaning, which was itself computed from the verb and its object. Each syntactic operation corresponds to a semantic operation (typically function application). The power of the framework is that finite means — a lexicon plus compositional rules — generate infinite interpretable expressions, mirroring the productivity of natural language itself.
