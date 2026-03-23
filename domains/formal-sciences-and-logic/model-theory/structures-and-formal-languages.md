---
id: structures-and-formal-languages
title: Structures and Formal Languages
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: set-fundamentals
  type: soft
- id: binary-relations
  type: soft
- id: functions-and-function-properties
  type: soft
- id: functions-and-mappings-formal
  type: hard
- id: ordered-pairs-and-tuples
  type: soft
builds-toward:
- model-interpretation-and-satisfaction
- structure-homomorphisms-embeddings
tags:
- signature
- structure
- interpretation
- domain
- arity
stage: expert
status: validated
---

# Structures and Formal Languages

## Core Idea
A signature specifies the vocabulary of a formal language by listing constant symbols, function symbols with specified arities, and relation symbols with specified arities. A structure over a signature assigns concrete meaning by providing a non-empty domain and interpretations of all symbols in the language. This separation of abstract syntax from concrete semantics is foundational to model-theoretic analysis.

## Questions

```yaml
- question: "A signature for group theory contains one binary function symbol '·' and one constant symbol 'e'. Which of the following counts as a structure over this signature?"
  type: multiple-choice
  options: ["The set ℤ with '·' interpreted as addition and 'e' interpreted as 0", "The set {a, b, c} with no additional interpretation provided", "The set ℝ with '·' interpreted as addition but 'e' left undefined", "Any set equipped with a binary relation symbol '<'"]
  answer: 0
  explanation: "A structure over a signature must provide a non-empty domain and interpret *every* symbol. The integers with addition as '·' and 0 as 'e' satisfies all requirements. The second option provides no interpretation; the third leaves 'e' undefined; the fourth introduces a symbol ('<') not in the signature while ignoring the required symbols."

- question: "Two different structures over the same signature can have identical underlying domains but assign different interpretations to the function symbols."
  type: true-false
  answer: true
  explanation: "A structure is a pairing of a domain with a specific interpretation of all signature symbols. The same set can support multiple distinct structures over the same signature. For example, the natural numbers with multiplication as '·' and 1 as 'e' form a different structure than the natural numbers with addition as '·' and 0 as 'e', even though both use the same domain ℕ and the same signature."

- question: "What is the difference between a signature and a structure, and why does model theory insist on keeping them separate?"
  type: short-answer
  answer: "A signature is purely syntactic: it lists symbols and their arities, assigning no meaning. A structure assigns semantic content by pairing a domain with a concrete interpretation of each symbol. The separation matters because the same signature can be satisfied by many different structures — allowing model theory to study which sentences are true across all models of a theory."
  explanation: "By separating language from meaning, model theory can ask: what must be true in *every* structure satisfying some axioms? What models exist for a given theory? This level of generality is what gives logic its power across all of mathematics — the same first-order language can describe groups, fields, graphs, and orderings, each as a distinct structure over an appropriate signature."
```

## Explainer

Before studying model theory, you encountered first-order logic as a formal language with syntax — formulas built from variables, connectives, and quantifiers. But syntax alone does not tell you whether a sentence is true. To evaluate truth, you need a concrete mathematical setting: a domain of objects and specific interpretations of the symbols you use. Model theory makes this step precise by defining two fundamental concepts: the *signature* and the *structure*.

A *signature* (sometimes called a vocabulary or language type) specifies the building blocks of your formal language: which constant symbols, function symbols, and relation symbols are available, together with the *arity* of each function and relation symbol. Arity tells you how many arguments a symbol takes — a binary function symbol takes 2 arguments, a unary relation symbol takes 1. The signature is purely *syntactic*: it is a list of symbols and their types, saying nothing whatsoever about what those symbols mean or which domain they apply to.

A *structure* gives the signature meaning. A structure M over a signature σ consists of two things: a non-empty set |M| called the *domain* or *universe*, and an *interpretation* that assigns to each constant symbol a specific element of |M|, to each n-ary function symbol a specific function |M|ⁿ → |M|, and to each n-ary relation symbol a specific subset of |M|ⁿ. Once you have a structure, every closed formula (sentence) in the language of σ has a determinate truth value in M.

The same signature can be interpreted by many different structures, and this multiplicity is the point. The signature of ordered fields — {0, 1, +, ·, <} — is satisfied by the rationals, the reals, and no-other familiar structure (there are non-standard models too). Group theory uses a smaller signature {·, e}, satisfied by integers under addition, nonzero rationals under multiplication, symmetric groups, and countless others. Model theory studies what all these structures have in common (the consequences of the shared axioms), how they differ (distinguishing properties), and what maps between them preserve (homomorphisms, embeddings, isomorphisms).

This syntax-semantics separation — signature as vocabulary, structure as meaning — is what allows a single formal language to serve as a universal tool for mathematics. When you move to model-interpretation-and-satisfaction, you will make precise what it means for a formula to be *true in* a structure using the satisfaction relation ⊨. Everything in that account rests on the definitions introduced here.
