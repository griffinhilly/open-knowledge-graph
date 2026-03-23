---
id: principles-and-parameters-theory
title: Principles and Parameters Theory of Universal Grammar
domain: language-and-communication
course: linguistics
prerequisites:
- id: universal-grammar-hypothesis
  type: hard
- id: parameter-setting-universal-grammar
  type: hard
tags:
- universal-grammar
- parameters
- principles
- language-acquisition
stage: formal-systems
status: draft
---

# Principles and Parameters Theory of Universal Grammar

## Core Idea
Principles and parameters theory proposes that human languages share universal grammatical principles (structure dependence, subjacency, binding) with parametric variation at discrete switch points. During acquisition, children set parameters for their language—null-subject or not, pro-drop or obligatory subjects. This framework explains the surprising uniformity of deep structure across languages despite surface diversity.

## Questions

```yaml
- question: "A child acquiring Italian simultaneously acquires null subjects ('Parla bene' without an overt pronoun), free subject-verb inversion in declaratives, and the absence of expletive subjects — without being taught each property separately. Principles and Parameters theory explains this because:"
  type: multiple-choice
  options:
    - "Italian input provides explicit negative evidence (correction) whenever the child makes an error on any of these properties"
    - "Children learn by imitating adult speakers, and Italian adults consistently demonstrate all three properties in natural speech"
    - "These properties are all correlated consequences of setting the null-subject parameter to [+pro-drop], so one parameter setting acquires the whole cluster"
    - "All three properties are universal principles, so every child acquires them regardless of language"
  answer: 2
  explanation: "The clustering prediction is the framework's most powerful feature. Setting [+null subject] doesn't just allow null subjects — it implicates a correlated cluster of properties including subject-verb inversion and absence of expletives, because these are parametrically linked. A child who sets [+null subject] acquires the whole cluster at once from a small amount of evidence. This is far more efficient than learning each property through separate induction from input, and it explains cross-linguistic co-variation patterns that would otherwise be mysterious coincidences."

- question: "Which of the following is an example of a PRINCIPLE (rather than a parameter) in the Principles and Parameters framework?"
  type: multiple-choice
  options:
    - "Whether a language requires overt subjects in all finite clauses"
    - "The direction in which heads and complements are ordered (head-initial vs. head-final)"
    - "The constraint that all grammatical rules operate on hierarchical phrase structure rather than linear word order"
    - "Whether a language permits morphologically rich verbal agreement"
  answer: 2
  explanation: "Structure dependence — the constraint that grammatical rules operate on hierarchical phrase structure, never on linear sequences — is invariant across all languages. Children never make structure-independent errors even though the input cannot teach this constraint directly. This is a principle: absolute, universal, and not learnable from positive evidence. The other options are parametric: languages vary in whether they require overt subjects, how they order head and complement, and how rich their agreement morphology is. The principle/parameter distinction is not just taxonomic — it determines whether a property must be innate (principles) or can be learned from input (parameters)."

- question: "In Principles and Parameters theory, principles are the variable component of Universal Grammar that differs across languages, while parameters are the invariant universal constraints."
  type: true-false
  answer: false
  explanation: "This reverses the framework's core distinction. Principles are invariant — they hold across every natural language without exception and cannot be overridden. Parameters are the variable component: they have more than one possible setting, and children must determine from their input which value their language has selected. The classic example is the null-subject parameter: English is [-null subject] and Italian is [+null subject]. The principle of structure dependence, by contrast, holds equally in both languages and in every other language studied."

- question: "The clustering of co-varying grammatical properties around a single parameter setting is one of the framework's most theoretically productive features and represents a genuine empirical prediction about cross-linguistic variation."
  type: true-false
  answer: true
  explanation: "The clustering prediction is falsifiable: it predicts that languages should not vary randomly property-by-property but should cluster into types defined by parameter settings, with correlated properties co-varying predictably. If languages varied independently on each property, the parameter concept would have no explanatory value. The null-subject cluster (pro-drop, subject-verb inversion, absence of expletives, richer agreement morphology) is the canonical example of a predicted cluster that has been confirmed cross-linguistically. The framework also predicts that second-language learning will be harder when parameters must be reset."

- question: "Why does Principles and Parameters theory predict that second-language acquisition should be harder than first-language acquisition, specifically with respect to parameters?"
  type: short-answer
  answer: "In first-language acquisition, children set parameters from a neutral starting point within the innate design space — they simply select the value that their input specifies. In second-language acquisition, the L1 parameters have already been set, and learners must unset or reset them to match the L2. Resetting a parameter is harder than setting it initially because L1 parameter values are deeply entrenched and their implications are distributed across a cluster of correlated properties — not just one behavior. An English speaker acquiring Italian must reset [+null subject] and then update all the correlated properties simultaneously. Persistent difficulty with null subjects, expletives, and inversion by L2 learners is predicted by the need for parameter resetting."
  explanation: "This prediction is borne out by empirical evidence: L2 learners persistently produce errors in the parameter-linked cluster even after achieving fluency in other areas. The framework predicts that these difficulties should be clustered and persistent — not random or equally distributed across all grammatical properties — because they reflect the difficulty of resetting an entrenched parametric value rather than failing to learn isolated rules."
```

## Explainer

From your study of Universal Grammar, you know the central claim: humans are born with an innate linguistic endowment that constrains the shape of possible natural languages. Principles and Parameters theory, developed by Noam Chomsky and colleagues in the early 1980s, gives that hypothesis its most precise formal expression. The framework proposes that the innate endowment has exactly two components: **principles**, which are invariant across all languages, and **parameters**, which vary but only within a pre-specified set of options. Together, these two components produce the striking combination of deep uniformity and surface diversity that characterizes human languages.

**Principles** are the absolute constraints that hold without exception across every natural language. **Structure dependence** is perhaps the clearest example: all grammatical rules operate on hierarchical phrase structure, never on linear sequences of words. When English forms a yes/no question from "The man who is tall is happy," the auxiliary that moves is the one in the main clause — not the first auxiliary encountered reading left to right. Even children, who have never been taught the concept of clausal hierarchy, respect this constraint without error. They never produce "Is the man who tall is happy?" This cannot be explained by the input alone — the constraint must be part of the innate system. **Subjacency** (restricting the distance over which movement can extract constituents) and the **binding principles** (governing the reference of pronouns and anaphors) function the same way: they hold everywhere, children respect them from the start, and they cannot be learned from positive evidence alone.

**Parameters** are where languages diverge. Unlike principles, parameters have more than one value, and children must determine from their input which value their language has set. The **null-subject parameter** (also called the pro-drop parameter) is the canonical example. Italian and Spanish allow sentences without overt subjects — "Parla bene" is grammatical without "lui" — while English requires an overt subject in nearly every clause. The parameter is binary: a language either allows null subjects or requires overt ones. What makes parametric variation powerful is that it is not a collection of isolated quirks; each parameter setting **implicates a cluster of correlated properties**. Languages with [+null subject] also tend to allow stylistic subject-verb inversion in declaratives, omit expletive subjects like "it" and "there," and display richer agreement morphology. A child who sets [+null subject] acquires the whole cluster at once, not each property through separate evidence.

This clustering is the framework's most theoretically productive feature and its deepest empirical commitment. It predicts that cross-linguistic variation should not be random — languages should clump into types defined by parameter settings, and those types should co-vary in predictable ways. It also predicts that second-language acquisition should involve **parameter resetting**, which is harder than first-language acquisition precisely because parameters must be unset from their L1 value — a prediction born out by persistent difficulty English speakers have acquiring null-subject languages and vice versa.

Principles and Parameters theory has been substantially revised since its 1980s formulation — the Minimalist Program, ongoing since the 1990s, aims to derive as much as possible from general principles of computational economy rather than stipulated parameters. But the core intuition endures: the deep structure of human language is constrained by innate universal principles, surface diversity arises from a finite set of parametric choices, and the task of language acquisition is not rule-learning from scratch but parameter-setting within a pre-specified design space. That intuition reshaped linguistics and cognitive science, and it remains the starting point for any serious account of how children acquire grammar.
