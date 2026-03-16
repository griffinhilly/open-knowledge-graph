---
id: compositionality-principle
title: Compositionality and Semantic Values
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: frege-sense-and-reference
  type: hard
- id: russell-definite-descriptions
  type: hard
- id: first-order-logic-syntax
  type: soft
- id: first-order-semantics
  type: soft
builds-toward:
- truth-conditions-and-meaning
- semantic-underdetermination-context
tags:
- semantics
- compositionality
- meaning-construction
stage: advanced
status: draft
---

# Compositionality and Semantic Values

## Core Idea
The meaning of a complex expression is a function of the meanings of its constituent parts and the syntactic rules combining them. This principle explains how a finite lexicon and small set of syntactic rules generate infinitely many meaningful sentences.

## How It's Best Learned
Start with simple noun phrases and work toward full sentences, explicitly tracking how constituent meanings combine. Use symbolic representation to show the function-argument structure.

## Common Misconceptions
Compositionality does not require all parts to contribute equally to meaning, nor does it guarantee you can always recover part meanings from the whole. Some meanings are more than compositional sums of parts.

## Questions

```yaml
- question: "Which sentence most directly challenges the compositionality principle?"
  type: multiple-choice
  options:
    - "The cat sat on the mat."
    - "She kicked the bucket."
    - "No student passed every exam."
    - "Every unicorn has a horn."
  answer: 1
  explanation: "'She kicked the bucket' is an idiom meaning 'she died.' Its meaning cannot be computed from the meanings of 'kick,' 'the,' and 'bucket' plus grammatical rules — the whole means something entirely different from the sum of its parts. This is the canonical challenge to compositionality. The other sentences have compositional meanings (even with quantifier scope ambiguity or fictional reference)."

- question: "Compositionality means that knowing the meaning of each word in a sentence is always sufficient to understand the sentence."
  type: true-false
  answer: false
  explanation: "Syntactic structure — how words are combined — is equally essential. 'The dog bit the man' and 'The man bit the dog' use the same words but have different meanings because the grammatical roles differ. Compositionality requires both the meanings of parts AND the rules for combining them; neither alone is sufficient."

- question: "Why does compositionality matter for explaining linguistic productivity — the ability to understand infinitely many sentences?"
  type: short-answer
  answer: "Because language has a finite vocabulary and finite grammatical rules, but compositionality allows these finite resources to generate and interpret infinitely many expressions. Any new combination of known words according to known rules produces a new expression whose meaning can be computed without memorizing it separately."
  explanation: "This is sometimes called the 'productivity argument' for compositionality. If meanings were not compositional — if every sentence's meaning had to be stipulated independently — no finite mind could handle a productive language. Compositionality is the mechanism that bridges finite means and infinite expressive capacity."
```

## Explainer

Compositionality answers a puzzle about language: how do speakers of finite minds manage an effectively infinite language? Any natural language has a finite vocabulary and a finite set of grammatical rules, yet competent speakers routinely understand and produce sentences they have never heard before — including sentences that have never been uttered in the history of the language. The principle of compositionality explains this: the meaning of any complex expression is fully determined by the meanings of its constituent parts and the syntactic rules for combining them. If you know what "red," "bicycle," and the English adjective-noun combination rule mean, you can understand "red bicycle" without having memorized that phrase.

You've already studied Frege's distinction between sense and reference and Russell's theory of definite descriptions. Compositionality is what allows both accounts to scale up to full sentences. For Frege, sentences have semantic values just as terms do — a sentence's semantic value is its truth value — and that truth value is computed compositionally from the references of its parts according to their logical structure. The function-argument structure you encountered in first-order semantics (e.g., *loves(x, y)* as a two-place predicate that takes two arguments and returns a truth value) is a formal representation of compositionality: the predicate is a function, and applying it to its arguments yields the sentence's semantic value.

The formal version of compositionality states that there is a homomorphism from syntactic structure to semantic structure. Informally: the way meanings combine mirrors the way syntax combines. When you combine a subject noun phrase with a verb phrase, the semantic operation tracks the syntactic one — you apply the semantic value of the VP to the semantic value of the subject to obtain the sentence's truth conditions. This function-argument structure explains why word order matters: "The dog bit the man" and "The man bit the dog" have the same words but different syntactic structures and therefore different meanings.

The most important challenges to compositionality come from idioms and context-dependence. Idioms like "kick the bucket" appear to violate compositionality because the whole means something different from what its parts would predict. Context-dependence is subtler: indexicals like "I" and "now" contribute different references depending on who speaks and when; and many philosophers argue that even apparently straightforward sentences are semantically underdetermined without contextual input. These observations don't necessarily defeat compositionality — they motivate more sophisticated versions that treat context as a parameter in the meaning-computation — but they establish that the simple story requires refinement.

A common misconception is that compositionality means all parts contribute equally or symmetrically. They don't: the predicate is a function that takes arguments, not just a peer element in a list. Another misconception is that you can always reverse-engineer part meanings from the whole. You cannot: "Every student passed some exam" and "Some exam was passed by every student" differ in meaning (quantifier scope), but both are built from the same words. Structure, not just constituency, encodes meaning.
