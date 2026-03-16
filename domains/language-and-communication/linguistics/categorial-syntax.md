---
id: categorial-syntax
title: 'Categorial Grammar: Type-Based Syntax'
domain: language-and-communication
course: linguistics
prerequisites:
- id: semantic-types-and-composition
  type: hard
tags:
- syntax
- framework
- types
stage: formal-systems
status: draft
---

# Categorial Grammar: Type-Based Syntax

## Core Idea
Categorial grammar assigns types (e.g., (NP\S)/NP for a transitive verb) to words, where ⟨e,t⟩ represents functions and slash denotes directionality. Syntax is reduction: applying a function of type A/B to an argument of type B yields type A, directly integrating syntax and semantics.

## Explainer

From your study of semantic types and composition, you know that expressions can be assigned types like **e** (entity) and **t** (truth value), and that complex expressions are built by function application — a function takes an argument of the right type and returns a value. Categorial grammar takes this type-theoretic architecture and makes it the basis of syntax itself, not just semantics. Instead of describing syntactic structure with labeled phrase-structure trees, every word receives a **syntactic type** that encodes both what it is and what it needs to combine with.

The basic types are **S** (sentence) and **NP** (noun phrase). A transitive verb like "likes" needs an NP to its right (its object) and an NP to its left (its subject) to form a complete sentence. In categorial notation, this is written **(NP\S)/NP**: the forward slash "/" means "needs an NP to the right," and the backward slash "\" means "needs an NP to the left." When "likes" takes its object "cats," it combines by **function application**: (NP\S)/NP applied to NP yields NP\S — a verb phrase that still needs a subject. When that VP takes the subject "Mary," it applies again: NP\S applied to NP yields S — a complete, well-formed sentence.

The elegance of categorial grammar is that **syntax is just type reduction**. The only combinatory rule needed is: if you have a function of type A/B and an argument of type B, combine them to get A. Every grammatical sentence reduces to type S; any combination that fails to reduce is ungrammatical. This is why syntax and semantics are directly integrated in this framework: the syntactic types are the semantic types. A transitive verb's syntactic type (NP\S)/NP corresponds exactly to its semantic type as a relation between individuals that yields a truth value once both arguments are saturated.

The slash notation encodes **directionality** — a feature that tree-based grammars typically handle implicitly through word-order rules. The "/" slash requires its argument to the right; the "\" slash requires its argument to the left. English has left-subject, right-object order, which is why subjects appear with the "\" slash and objects with the "/" slash. Languages with different word orders assign the same functional types but with different slash orientations. Word-order variation is thus a systematic consequence of type directionality rather than a separate stipulation — a sign of the framework's underlying unity between syntactic form and semantic function.
