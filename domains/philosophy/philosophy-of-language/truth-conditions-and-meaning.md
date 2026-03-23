---
id: truth-conditions-and-meaning
title: Truth Conditions and Meaning
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: davidson-truth-conditional-semantics
  type: hard
- id: first-order-semantics
  type: hard
- id: propositional-semantics
  type: soft
- id: first-order-logic-syntax
  type: soft
builds-toward:
  - intensionality-and-opacity
tags:
- semantics
- truth-conditions
- meaning-theory
stage: formal-systems
status: draft
---
# Truth Conditions and Meaning

## Core Idea
Knowing the meaning of a declarative sentence means knowing its truth conditions—what circumstances would make it true or false. This approach treats truth conditions as constitutive of semantic content and provides a systematic way to analyze complex sentences using model-theoretic semantics.

## How It's Best Learned
Study Tarski's T-biconditionals: 'Snow is white' is true iff snow is white. Work through how truth conditions compose for complex sentences with multiple operators.

## Common Misconceptions
Truth-conditional semantics does not reduce all meaning to truth conditions; imperatives, questions, and pragmatic content fall outside this framework. Not all meaningful discourse is truth-valued.

## Questions

```yaml
- question: "A student argues: 'Since we clearly understand the command "Close the door!", it must have truth conditions — it is true when the door is closed.' How should a truth-conditional semanticist respond?"
  type: multiple-choice
  options:
    - "The student is right — imperatives are true when their commanded action is performed"
    - "The student is right — all meaningful sentences have truth conditions, since meaning just is truth conditions"
    - "The student is wrong — imperatives are not truth-apt; truth-conditional semantics does not cover all dimensions of meaning"
    - "The student is wrong — imperatives have truth conditions, but those conditions are never satisfied"
  answer: 2
  explanation: "Truth-conditional semantics succeeds for declarative sentences but does not cover imperatives, questions, or exclamations, which are meaningful but not truth-apt in the standard sense. This is not a refutation of the theory — it defines the domain within which the theory succeeds. Pragmatic content (what speakers implicate, not what sentences literally say) and non-declarative speech acts require supplementary frameworks like speech act theory."

- question: "Compositionality is central to truth-conditional semantics primarily because it explains:"
  type: multiple-choice
  options:
    - "Why some sentences are true and others are false in the actual world"
    - "How speakers can understand infinitely many novel sentences from a finite vocabulary and grammar"
    - "Why speakers sometimes mean more than their words literally say"
    - "How context determines the reference of indexicals like 'I' and 'here'"
  answer: 1
  explanation: "The productivity of language — that we understand sentences we have never heard before — is explained by compositionality: meaning is a function of the meanings of parts and the rules for combining them. We learn base cases (reference of names, extensions of predicates) and combination rules (conjunction, negation, quantification), and from these finite resources we compute truth conditions for infinitely many sentences. Without compositionality, a truth theory would require infinite stipulations."

- question: "To know what a sentence means, on the truth-conditional view, is to know whether the sentence is currently true."
  type: true-false
  answer: false
  explanation: "This is a critical distinction. Knowing the meaning = knowing the truth CONDITIONS — the circumstances that would make the sentence true or false. You can know what 'There is life on Mars' means without knowing whether it is actually true. The truth conditions pick out a set of possible situations, and the sentence is true in those situations and false otherwise. Knowing actual truth value requires empirical knowledge of the world; knowing meaning requires only knowledge of which situations would verify or falsify the sentence."

- question: "Tarski's T-biconditional schema — e.g., ''Snow is white' is true if and only if snow is white' — serves as the model for how a systematic truth theory can function as a meaning theory."
  type: true-false
  answer: true
  explanation: "Tarski's schema looks trivial, but its significance is that it can be generalized systematically: if you specify, for every sentence of a language, the conditions under which it is true, you have fully characterized the semantic content of each sentence. Davidson's insight was that this truth theory, applied recursively to a natural language, constitutes a meaning theory — knowing the right-hand side of each T-biconditional is knowing what the sentence means."

- question: "Why does truth-conditional semantics hold that knowing a sentence's truth conditions is the same as knowing its meaning, rather than merely a useful correlate of it?"
  type: short-answer
  answer: "Because truth conditions specify exactly what state of affairs the sentence represents — they pick out the very situations the sentence is about. To know those conditions is to know what the sentence says about the world, which is what it means to understand it. On this view, meaning just is the function from possible situations to truth values; there is no further layer of 'meaning' left over once truth conditions are fully specified."
  explanation: "The identification is conceptual, not merely empirical. If two sentences always have the same truth value in every possible situation, they express the same proposition (have the same meaning). The truth-conditional framework makes this precise via model-theoretic semantics, where meaning is formally represented as an intension — a function from possible worlds to truth values. The framework's limits (imperatives, pragmatics) show where this identification breaks down, but within declarative semantics it is extremely powerful."
```

## Explainer

You already know from Davidson's truth-conditional semantics that meaning and truth are deeply connected: to understand a sentence is, at minimum, to know what circumstances would make it true or false. You also know from first-order semantics how to assign truth values to complex sentences—quantified formulas, negations, conjunctions—by recursively evaluating them in models. This topic brings those two strands together and asks: can we build a full theory of meaning for a natural language by specifying truth conditions systematically?

The starting point is Tarski's **T-biconditional schema**: "'Snow is white' is true if and only if snow is white." This looks trivial, but its systematic generalization is not. If you can specify, for *every* sentence of a language, the conditions under which it is true, you have given a truth theory for that language. Davidson's insight was that a **truth theory** of this form functions as a **meaning theory**: knowing the truth conditions of a sentence just *is* knowing what the sentence means. The semantic content of a sentence, on this view, is its truth condition—the set of possible situations that would make it true.

The compositional structure is what makes this tractable. You already know from first-order semantics that atomic sentences get their truth conditions from the reference of their names and the extensions of their predicates. Complex sentences build truth conditions compositionally: "P and Q" is true iff P is true and Q is true; "Not P" is true iff P is false; "There exists an x such that Fx" is true iff some object in the domain satisfies F. This **principle of compositionality**—meaning is a function of parts and structure—explains how we understand infinitely many sentences from a finite vocabulary: we learn the base cases and the rules for combining them.

Model-theoretic semantics, which you already have, provides the formal framework. A model specifies a domain of objects and an interpretation function assigning extensions to predicates and referents to names. A sentence is true in a model iff the world described by the model satisfies the sentence's truth conditions. Meaning, on the truth-conditional approach, becomes the function from models (or possible worlds) to truth values—the **intension** of the sentence. Knowing this function is knowing what the sentence means.

The limitations are real and instructive. **Imperatives** ("Close the door!") and **questions** ("Is it raining?") are not truth-apt in the ordinary sense, yet they are clearly meaningful. **Indexicals** complicate truth-conditions since the same sentence-type has different truth conditions depending on who utters it when. **Pragmatic content**—what speakers implicate beyond what they literally say—falls outside the truth-conditional theory of sentence meaning, requiring Gricean or other pragmatic supplements. These limitations do not refute the approach; they define the domain within which it succeeds, and understanding those boundaries is as important as mastering the framework itself.
