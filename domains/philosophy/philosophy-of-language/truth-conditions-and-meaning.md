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
- id: presupposition-and-assertion
  type: soft
- id: linguistic-relativity-sapir-whorf
  type: soft
- id: proposition-and-semantic-content
  type: soft
builds-toward:
- intensionality-and-opacity
tags:
- semantics
- truth-conditions
- meaning-theory
stage: formal-systems
status: validated
---
# Truth Conditions and Meaning

## Core Idea
Knowing the meaning of a declarative sentence means knowing its truth conditions—what circumstances would make it true or false. This approach treats truth conditions as constitutive of semantic content and provides a systematic way to analyze complex sentences using model-theoretic semantics.

## How It's Best Learned
Study Tarski's T-biconditionals: 'Snow is white' is true iff snow is white. Work through how truth conditions compose for complex sentences with multiple operators.

## Common Misconceptions
Truth-conditional semantics does not reduce all meaning to truth conditions; imperatives, questions, and pragmatic content fall outside this framework. Not all meaningful discourse is truth-valued.

## Explainer

You already know from Davidson's truth-conditional semantics that meaning and truth are deeply connected: to understand a sentence is, at minimum, to know what circumstances would make it true or false. You also know from first-order semantics how to assign truth values to complex sentences—quantified formulas, negations, conjunctions—by recursively evaluating them in models. This topic brings those two strands together and asks: can we build a full theory of meaning for a natural language by specifying truth conditions systematically?

The starting point is Tarski's **T-biconditional schema**: "'Snow is white' is true if and only if snow is white." This looks trivial, but its systematic generalization is not. If you can specify, for *every* sentence of a language, the conditions under which it is true, you have given a truth theory for that language. Davidson's insight was that a **truth theory** of this form functions as a **meaning theory**: knowing the truth conditions of a sentence just *is* knowing what the sentence means. The semantic content of a sentence, on this view, is its truth condition—the set of possible situations that would make it true.

The compositional structure is what makes this tractable. You already know from first-order semantics that atomic sentences get their truth conditions from the reference of their names and the extensions of their predicates. Complex sentences build truth conditions compositionally: "P and Q" is true iff P is true and Q is true; "Not P" is true iff P is false; "There exists an x such that Fx" is true iff some object in the domain satisfies F. This **principle of compositionality**—meaning is a function of parts and structure—explains how we understand infinitely many sentences from a finite vocabulary: we learn the base cases and the rules for combining them.

Model-theoretic semantics, which you already have, provides the formal framework. A model specifies a domain of objects and an interpretation function assigning extensions to predicates and referents to names. A sentence is true in a model iff the world described by the model satisfies the sentence's truth conditions. Meaning, on the truth-conditional approach, becomes the function from models (or possible worlds) to truth values—the **intension** of the sentence. Knowing this function is knowing what the sentence means.

The limitations are real and instructive. **Imperatives** ("Close the door!") and **questions** ("Is it raining?") are not truth-apt in the ordinary sense, yet they are clearly meaningful. **Indexicals** complicate truth-conditions since the same sentence-type has different truth conditions depending on who utters it when. **Pragmatic content**—what speakers implicate beyond what they literally say—falls outside the truth-conditional theory of sentence meaning, requiring Gricean or other pragmatic supplements. These limitations do not refute the approach; they define the domain within which it succeeds, and understanding those boundaries is as important as mastering the framework itself.

## Questions

- id: truth-conditions-and-meaning-q1
  type: mc
  question: "According to Davidson's truth-conditional semantics, what does it mean to know the meaning of a declarative sentence?"
  options:
    - "To know the sentence's grammatical structure and vocabulary"
    - "To know the circumstances under which the sentence would be true or false"
    - "To know the speaker's intention when uttering the sentence"
    - "To know the historical origin of each word in the sentence"
  correct: 1
  explanation: "Davidson's key insight is that a truth theory functions as a meaning theory: knowing the truth conditions of a sentence — what circumstances would make it true or false — just is knowing what the sentence means."

- id: truth-conditions-and-meaning-q2
  type: mc
  question: "What is the intension of a sentence in model-theoretic semantics?"
  options:
    - "The speaker's intended meaning when uttering the sentence"
    - "The grammatical mood of the sentence (declarative, imperative, interrogative)"
    - "The function from models or possible worlds to truth values"
    - "The set of all sentences logically equivalent to it"
  correct: 2
  explanation: "In model-theoretic semantics, meaning becomes the function from models (or possible worlds) to truth values — this function is the intension of the sentence. Knowing this function is knowing what the sentence means."

- id: truth-conditions-and-meaning-q3
  type: tf
  question: "Tarski's T-biconditional schema states: 'Snow is white' is true if and only if snow is white."
  correct: true
  explanation: "This is the foundational schema of truth-conditional semantics. While it looks trivial for a single sentence, its systematic generalization across every sentence of a language yields a full truth theory that, according to Davidson, functions as a meaning theory."

- id: truth-conditions-and-meaning-q4
  type: tf
  question: "Truth-conditional semantics can fully account for the meaning of imperatives like 'Close the door!' and questions like 'Is it raining?'"
  correct: false
  explanation: "Imperatives and questions are not truth-apt in the ordinary sense — they cannot be straightforwardly assigned truth conditions — yet they are clearly meaningful. This is a recognized limitation of the truth-conditional approach."

- id: truth-conditions-and-meaning-q5
  type: sa
  question: "What type of supplementary theory is needed to account for what speakers implicate beyond what they literally say, which falls outside truth-conditional semantics?"
  correct: "pragmatic theory (Gricean pragmatics)"
  explanation: "Pragmatic content — what speakers implicate beyond literal meaning — falls outside truth-conditional semantics and requires Gricean or other pragmatic supplements to explain."
