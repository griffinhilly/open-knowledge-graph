---
id: philosophy-of-language-intro
title: Introduction to Philosophy of Language
domain: philosophy
course: philosophy-of-language
prerequisites: []
builds-toward:
- meaning-and-reference-basics
- frege-sense-and-reference
- russell-definite-descriptions
tags:
- introduction
- semantics
- reference
- meaning
stage: abstract-reasoning
status: validated
---

# Introduction to Philosophy of Language

## Core Idea
Philosophy of language investigates fundamental questions about how language relates to reality: What do words refer to? How do sentences acquire meaning? How do we communicate thoughts through utterances? What is the relationship between language and truth?

## How It's Best Learned
Begin by identifying the central puzzle: why is meaning more than reference? Study the morning star / evening star case and consider what makes two names with the same referent differ in meaning.

## Common Misconceptions
Language is just a naming system where words directly stand for objects. Meaning is identical to reference. The study of language is merely about words, not about the fundamental nature of reality and thought.

## Questions

```yaml
- question: "'Hesperus' and 'Phosphorus' both refer to Venus. On a pure naming/reference theory of meaning, 'Hesperus is Phosphorus' should be equivalent in meaning to:"
  type: multiple-choice
  options:
    - "'Venus exists' — a claim about the existence of the referent"
    - "'Hesperus is Hesperus' — a trivially true logical identity"
    - "An extraordinary astronomical discovery about two distant planets"
    - "'The morning star is brighter than the evening star'"
  answer: 1
  explanation: "If meaning IS reference, then any two names with the same referent are synonymous — they mean exactly the same thing. 'Hesperus is Phosphorus' would then be as trivially true as 'Hesperus is Hesperus.' But this is clearly wrong: 'Hesperus is Phosphorus' was an astronomical discovery requiring observation, not a logical tautology. This shows that two expressions can share a referent while differing in meaning — which is exactly what motivated Frege's distinction between sense and reference."

- question: "The sentence 'Sherlock Holmes is a brilliant detective' is meaningful and widely understood. This poses a problem for a pure reference theory of meaning because:"
  type: multiple-choice
  options:
    - "Fictional detectives cannot be described in meaningful propositions"
    - "Holmes doesn't exist, so on a reference theory the sentence would be meaningless or defective — yet it clearly isn't"
    - "The word 'brilliant' cannot have a determinate reference"
    - "Literary sentences operate by different grammatical rules than ordinary language"
  answer: 1
  explanation: "On a pure reference theory, the meaning of a name is the object it names. If there is no object (Holmes doesn't exist), the name has no meaning, and any sentence containing it should be meaningless or defective. But we clearly understand, reason about, and debate such sentences. This breakdown motivates theories that separate the content a term contributes from whether it successfully picks out a real object."

- question: "On a pure reference theory of meaning, 'Hesperus' and 'Phosphorus' are exactly synonymous because they refer to the same object."
  type: true-false
  answer: true
  explanation: "This follows directly from identifying meaning with reference. The point is that this conclusion seems wrong — the two names differ in cognitive significance — which is precisely why the naming/reference theory fails. The truth of this statement is what makes it a useful step in the reductio: accept the theory, derive this consequence, notice it is implausible, conclude the theory needs revision."

- question: "The central insight of philosophy of language is that language is best understood as a naming system where words directly pick out objects in the world."
  type: true-false
  answer: false
  explanation: "This is the naive picture that philosophy of language immediately calls into question. Terms for non-existent things (Holmes), co-referring expressions with different meanings (Hesperus/Phosphorus), and general terms (red, tiger) that don't name any single individual all show that the naming picture breaks down almost immediately. The field's central task is to develop better accounts of meaning that handle these cases."

- question: "What is the 'morning star / evening star' puzzle, and what does it reveal about the relationship between meaning and reference?"
  type: short-answer
  answer: "Both 'Hesperus' (the evening star) and 'Phosphorus' (the morning star) refer to Venus, giving them the same reference. But 'Hesperus is Phosphorus' was a genuine astronomical discovery, not a trivial logical truth like 'Hesperus is Hesperus.' This shows that two expressions can share a referent while differing in meaning — their mode of presentation or cognitive significance differs. Meaning therefore cannot simply be identified with reference."
  explanation: "This puzzle is the entry point to Frege's sense/reference distinction. Sense is the mode of presentation — how an expression presents its referent — and two expressions can have the same reference but different senses. The puzzle matters because it shows that a complete theory of meaning must explain more than just what expressions point to."
```

## Explainer

The simplest possible theory of language is a naming picture: words are labels, and meaning is the thing the label is attached to. This picture works reasonably well for proper names ("London" names a city) and for pointing at objects in front of you. But it breaks down almost immediately when you examine language more carefully, and the breakdowns reveal deep questions about the relationship between language, thought, and reality.

Consider the **morning star / evening star** puzzle — your recommended starting case. "Hesperus" and "Phosphorus" are both names for Venus. On the naming picture, their meaning just *is* Venus. But then "Hesperus is Phosphorus" would mean the same as "Hesperus is Hesperus" — a trivial identity. Yet "Hesperus is Phosphorus" is an astronomical discovery, not a logical tautology. Something about the *way* these names present their referent differs, even though the referent is the same. This is the puzzle that motivated Frege to distinguish **sense** (mode of presentation, cognitive significance) from **reference** (the object denoted). Meaning cannot simply be reference, because two expressions can refer to the same thing while differing in meaning.

A second breakdown: what about terms that *don't* refer? "Sherlock Holmes is a detective" seems perfectly meaningful, but Holmes doesn't exist. If meaning were just reference, sentences about Holmes would be meaningless or defective. Yet we understand them, reason about them, and debate their truth. This motivates theories that separate the **content** a term contributes to a sentence from whether that content successfully picks out a real object. Similarly, **general terms** like "red" or "tiger" don't name a single individual — they apply to many things. What determines which things they apply to? This is the question of **extension** (the set of things a term applies to) and **intension** (the property or criterion that determines extension).

Philosophy of language is not an isolated specialty. It bears directly on metaphysics (do abstract objects like numbers and properties exist, given that we refer to them?), epistemology (how does language convey knowledge?), and the philosophy of mind (what is the relationship between linguistic meaning and mental content?). The central questions — What is reference? What is meaning? How do context and speaker intention interact with semantic content? — are foundational for everything that follows in this course.
