---
id: reference-failure-empty-names
title: Reference Failure and Empty Names
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: russell-definite-descriptions
  type: hard
- id: frege-sense-and-reference
  type: soft
- id: compositionality-principle
  type: soft
tags:
- reference
- names
- truth-values
- empty-terms
stage: formal-systems
status: draft
---

# Reference Failure and Empty Names

## Core Idea
When a name lacks a referent (like "Vulcan" or "the current king of France"), how do statements containing it have truth conditions? Frege proposed a truth-value gap; Russell proposed that descriptions are logically analyzable into quantified formulas that entail existence; direct reference theorists must explain what happens when reference fails. This problem reveals deep issues about semantic content and compositionality.

## How It's Best Learned
Compare solutions: Russell's analysis of "The current king of France is wise" shows it's false rather than truth-valueless by parsing it as "There exists a unique current king of France who is wise." Study how direct reference theorists handle empty names, and consider whether fictional names ("Sherlock Holmes") require special treatment. Examine whether presupposition failure is the right model.

## Common Misconceptions
- Thinking Frege and Russell disagree about truth-values; they disagree about semantic analysis, not always about verdicts.
- Assuming empty names always fail to communicate; we successfully communicate about fictional characters and historical figures.
- Overlooking that some views (Meinongian) allow reference to non-existent objects.

## Explainer

From your work on **Russell's theory of definite descriptions** and **Frege's sense/reference distinction**, you're equipped to see why empty names create a genuine crisis for theories of meaning. Both Frege and Russell built their semantic theories around reference: expressions contribute their referents to the propositions they help express. But what happens when a name has no referent? The question is not merely abstract — it arises for names of myths ("Zeus"), fictional characters ("Sherlock Holmes"), failed scientific posits ("Vulcan," the planet once hypothesized to orbit inside Mercury), and ordinary speakers' mistaken beliefs.

Frege's response was the **truth-value gap**: a sentence like "Vulcan is larger than Mercury" is neither true nor false because "Vulcan" lacks a referent and thus the sentence fails to express a complete proposition. Frege softened this by distinguishing the literary and scientific contexts: in fiction, names have **sense** (a mode of presentation) without ordinary reference, referring instead to fictional objects or ideas. His theory can thus acknowledge that we understand and communicate successfully about fictional characters without committing to their literal existence. The cost is that compositionality becomes complicated — the semantic value of a complex expression depends on the semantic values of its parts, but what is the semantic value of a part with no referent?

Russell's strategy was more radical: **deny that proper names (in the logical sense) can fail to refer**. He distinguished between ordinary proper names ("Hamlet," "Vulcan"), which are disguised definite descriptions, and **logically proper names**, which are guaranteed to refer. "Vulcan" abbreviates something like "the planet between Mercury and the Sun." Russell's analysis of definite descriptions then handles the failure: "The planet between Mercury and the Sun is larger than Mercury" is analyzed as "There exists a unique planet between Mercury and the Sun that is larger than Mercury" — which is simply **false**, not truth-valueless, because the existential claim fails. This preserves bivalence (every proposition is either true or false) at the cost of denying that ordinary names are genuine referring expressions.

**Direct reference theorists** (Kripke, Kaplan) face the sharpest challenge. If a name's sole semantic contribution is its referent — no descriptive backing, no Fregean sense — then an empty name contributes nothing, and the sentence containing it fails to express a proposition at all. This makes it hard to explain how "Sherlock Holmes is a detective" seems to communicate something, how we can make true negative existential claims ("Vulcan does not exist"), and how fiction is intelligible. Responses include **Meinongianism** (names refer to non-existent objects that have properties), **pretense theory** (we are engaged in a game of make-believe), **abstract artifact theories** (fictional characters exist as abstract objects created by authors), and various hybrid theories. Each choice reflects deeper commitments about the metaphysics of existence, the semantics of reference, and the purpose of names in natural language.

## Questions

```yaml
- question: "Russell analyzes 'The present king of France is bald' as false rather than truth-valueless. How does his theory achieve this?"
  type: short-answer
  answer: "Russell treats 'The present king of France' not as a genuine referring expression but as a description that can be paraphrased into a quantified formula: 'There exists exactly one thing that is currently king of France, and that thing is bald.' This complex existential statement is simply false, because the existential claim (there is a present king of France) fails. By eliminating the description in favor of quantifiers, Russell avoids the assumption that a singular term must refer for the sentence to have a truth value."
  explanation: "This is the core move in Russell's theory of descriptions: definite descriptions are 'incomplete symbols' that disappear on logical analysis. The surface grammar suggests a subject-predicate form, but the logical form is existential. This preserves classical bivalence — every proposition is true or false — while explaining why sentences about non-existent things can be meaningfully evaluated."

- question: "A direct reference theorist faces a harder problem with empty names than a Fregean does. Why?"
  type: multiple-choice
  options:
    - "Because direct reference theorists deny that names have any meaning at all"
    - "Because if a name's only semantic contribution is its referent, an empty name contributes nothing, leaving no proposition expressed"
    - "Because Fregean sense is always available to fill the gap left by a missing referent"
    - "Because direct reference theorists do not allow fictional names in their semantic theory"
  answer: 1
  explanation: "Direct reference theory holds that names are 'rigid designators' that contribute their referent directly to propositional content — there is no Fregean sense or descriptive backing to serve as a fallback. When the referent is absent, there is nothing for the name to contribute, and the sentence fails to express a proposition. Fregeans have a built-in resource (sense) that can do semantic work even when reference fails, allowing the sentence to have content even if it lacks a truth value. Direct reference theorists must find another solution — pretense, Meinongianism, or abstract artifact theories — precisely because their view denies the availability of Fregean sense."
```
