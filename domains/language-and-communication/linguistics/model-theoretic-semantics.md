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

## Questions

```yaml
- question: "In a model M with domain D = {Fido, Rex, Luna}, the predicate 'barks' is assigned the set {Fido, Rex}. The sentence 'Luna barks' is:"
  type: multiple-choice
  options:
    - "True, because Luna is in the domain D"
    - "False, because Luna is not in the extension of 'barks' in M"
    - "Neither true nor false — model-theoretic semantics only evaluates quantified sentences"
    - "True or false depending on the possible world — a single model cannot determine truth value"
  answer: 1
  explanation: "Model-theoretic truth is a relation between expressions and models. 'Luna barks' is true in M if and only if the entity assigned to 'Luna' is a member of the set assigned to 'barks.' Since Luna ∉ {Fido, Rex}, the sentence is false in M. Being in the domain D is not sufficient — D contains all entities that exist in the model, but a predicate's extension is the specific subset that has the property. This is the core mechanism: truth is determined by checking membership in the model's interpretation, not by any external facts."

- question: "'The morning star' and 'the evening star' both pick out the planet Venus. In model-theoretic terms, these expressions have the same ___ but different ___."
  type: multiple-choice
  options:
    - "Intension; extension — they mean the same concept but refer differently in different worlds"
    - "Extension; intension — they refer to the same object now but pick it out by different rules across possible worlds"
    - "Semantic value; truth condition — they denote the same entity but describe it differently"
    - "Reference; sense — this distinction belongs to Frege's framework, not model-theoretic semantics"
  answer: 1
  explanation: "Extension is the actual referent in the current model — both expressions pick out Venus, so their extensions are identical. Intension is the function from possible worlds to extensions — the concept or mode of presentation that determines what each expression refers to in any given world. 'The morning star' picks out the brightest object in the morning sky; 'the evening star' picks out the brightest object in the evening sky. In a world where these were different objects, the expressions would have different extensions. Same extension now; different functions across all possible worlds. This is why 'The morning star is the evening star' is informative — it tells you something non-trivial about the world."

- question: "Compositionality in model-theoretic semantics means that the meaning of 'every dog barked loudly' can be systematically computed from the meanings of its parts without separately stipulating what the whole sentence means."
  type: true-false
  answer: true
  explanation: "Compositionality is the principle that complex expressions derive their semantic values from their parts and the rules for combining them. This is what makes model-theoretic semantics a genuine theory rather than a lookup table. 'Every dog barked loudly' is computed: 'loudly' modifies 'barked' via function application, the resulting predicate combines with the universal quantifier 'every,' which takes 'dog' as its domain restrictor and applies to the whole. Each syntactic operation corresponds to a semantic operation. This compositional structure is what allows finite vocabulary and rules to generate infinitely many interpretable sentences — mirroring natural language productivity."

- question: "Two expressions with the same extension must have the same intension, because they refer to the same object in the world."
  type: true-false
  answer: false
  explanation: "The morning star/evening star case directly refutes this. Both expressions have the same extension (Venus) — but different intensions, because they are defined by different criteria that could diverge across possible worlds. Intension is a function from possible worlds to extensions; if two expressions pick out the same object now but through different descriptions, they have identical extensions but distinct intensions. This distinction is essential for analyzing intensional contexts: 'Astronomers believed the morning star was the morning star' (tautology) vs. 'Astronomers believed the morning star was the evening star' (a substantive discovery) cannot be distinguished if we collapse extension and intension."

- question: "Explain the extension/intension distinction using 'the morning star' and 'the evening star' as examples, and say why it matters for analyzing natural language meaning."
  type: short-answer
  answer: "Extension is the actual referent of an expression in a given model — what it picks out in the actual world. Both 'the morning star' and 'the evening star' have the same extension: the planet Venus. Intension is the function from possible worlds to extensions — the concept or rule that determines what an expression refers to in any possible situation. 'The morning star' picks out the brightest object visible in the morning sky; 'the evening star' picks out the brightest object in the evening sky. These are different rules, which could pick out different objects in other possible worlds. The distinction matters because natural language has intensional contexts — attitude reports, modal claims, conditionals — where substituting co-extensional expressions changes truth value. 'Mary believes Venus is Venus' is trivially true; 'Mary believes the morning star is the evening star' reports a substantive empirical belief."
  explanation: "Without the extension/intension distinction, we cannot explain why coreferential terms are not always intersubstitutable, why identity statements can be informative, or how modal reasoning works. Frege noticed the problem (Sinn vs. Bedeutung); possible-worlds semantics and model-theoretic intensions provide the formal framework to handle it systematically."
```

## Explainer

From predicate logic semantics, you know how to translate sentences into formulas using predicates, variables, quantifiers, and logical connectives. From possible-worlds semantics, you know that meaning can be analyzed in terms of truth across different possible situations — that the meaning of a sentence is (roughly) the set of worlds in which it is true. Model-theoretic semantics fuses these ideas into a rigorous formal framework: it makes precise exactly what it means for a sentence to be true by specifying how linguistic expressions are interpreted relative to a formal **model**.

A **model** M is a mathematical structure consisting of a domain D — a set of individual entities — and an interpretation function I that assigns semantic values to the non-logical vocabulary. For a predicate like "barks," the interpretation function assigns it the set of all entities in D that have the barking property. For an individual constant like "Fido," it assigns a specific element of D. Combining these: "Fido barks" is true in M if and only if the entity I assigns to "Fido" is a member of the set I assigns to "barks." This is the core of truth-conditional semantics — meaning is modeled as a relation between linguistic expressions and formal structures, and truth is the central semantic property.

The distinction between **extension** and **intension** is the bridge from a single model to possible-worlds reasoning. The extension of an expression is its semantic value in the current model — the actual set of entities the predicate picks out, or the actual individual a name refers to. The intension is the *function* from possible worlds to extensions — the rule or concept that determines what the expression refers to in each possible situation. "The morning star" and "the evening star" have the same extension (both pick out Venus), but different intensions (different modes of presentation), which is why "The morning star is the evening star" is informative in a way that "The morning star is the morning star" is not. This distinction is essential for analyzing belief contexts, necessity, and other intensional phenomena.

**Compositionality** is the principle that the semantic value of a complex expression is computed from the semantic values of its parts and their mode of combination. This is what makes model-theoretic semantics a genuine theory of meaning rather than a lookup table. You don't need to directly interpret "Every barking dog frightened some child" — you compute its meaning systematically: the universal quantifier takes a predicate and returns a generalized quantifier, which combines with the verb phrase's meaning, which was itself computed from the verb and its object. Each syntactic operation corresponds to a semantic operation (typically function application). The power of the framework is that finite means — a lexicon plus compositional rules — generate infinite interpretable expressions, mirroring the productivity of natural language itself.
