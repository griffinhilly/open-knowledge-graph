---
id: semantic-underdetermination-context
title: Semantic Underdetermination and Context
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: truth-conditions-and-meaning
  type: hard
- id: pragmatics-semantics-boundary
  type: hard
builds-toward:
- indexicality-and-contextual-reference
tags:
- underdetermination
- context
- pragmatics
stage: formal-systems
status: validated
---

# Semantic Underdetermination and Context

## Core Idea
Grammatical structure underdetermines semantic content; pragmatic principles and contextual factors must narrow interpretation. This explains why context sensitivity is ubiquitous in natural language and why the same sentence can express different propositions in different contexts.

## How It's Best Learned
Study cases of genuine underdetermination where syntax alone cannot determine meaning. Distinguish syntactic ambiguity from pragmatic underdetermination to appreciate the difference.

## Questions

```yaml
- question: "Someone utters 'Everyone left.' Philosophers argue that interpreting this requires contextual domain restriction. This is an example of:"
  type: multiple-choice
  options:
    - "Lexical ambiguity — 'everyone' has two distinct dictionary meanings: universal and restricted"
    - "Gricean implicature — 'everyone' literally means every person in the universe, but we pragmatically infer a smaller domain"
    - "Semantic underdetermination — the sentence leaves a domain variable unsaturated, so it does not express a determinate proposition without contextual restriction of the quantifier's domain"
    - "Pragmatic enrichment that goes beyond the literal meaning without affecting truth conditions"
  answer: 2
  explanation: "This is semantic underdetermination, not lexical ambiguity (which involves a single word having two dictionary entries) or implicature (which is communicated meaning beyond the literal). The sentence 'Everyone left' has a unique syntactic parse and no ambiguous words, yet it fails to express a complete, evaluable proposition: 'everyone in the universe left' is clearly not what's meant, and the grammar does not specify which domain of quantification is operative. Context must supply the restriction (e.g., 'everyone at the party'). This is not communicated beyond the literal — it is a gap in the literal content itself. The truth conditions of the sentence are incomplete without this contextual input."

- question: "How does semantic underdetermination differ from syntactic ambiguity?"
  type: multiple-choice
  options:
    - "Syntactic ambiguity occurs only in written language; underdetermination only in spoken language"
    - "Syntactic ambiguity involves a sentence having multiple grammatical parsings, each yielding a different meaning; semantic underdetermination involves a grammatically unambiguous sentence that still fails to express a complete proposition without contextual input"
    - "They are the same phenomenon analyzed at different levels of linguistic description"
    - "Semantic underdetermination applies only to indexical expressions like 'I' and 'here'; syntactic ambiguity applies to all sentences"
  answer: 1
  explanation: "'Flying planes can be dangerous' is syntactically ambiguous — it has two parses (flying planes = planes that fly, or flying planes = the act of flying them). Each parse yields a complete, truth-evaluable proposition. Semantic underdetermination is different: 'It is raining' is syntactically unambiguous (one parse), but the sentence underdetermines a full proposition because no location is specified. We cannot even ask whether the sentence is true or false until context fills in where. The grammar is fully specified; what's missing is a parameter the grammar requires but does not supply."

- question: "A sentence can be grammatically complete and syntactically unambiguous while still failing to express a complete, truth-evaluable proposition without contextual supplementation."
  type: true-false
  answer: true
  explanation: "This is precisely the core claim of semantic underdetermination. 'It is raining,' 'Steel is stronger than plastic,' 'I've had enough,' and 'Everyone left' are all grammatically complete and syntactically unambiguous sentences. Yet each fails to express a determinate proposition without contextual input: rain where? Stronger how and under what conditions? Enough of what? Everyone in what domain? Context must supply content that completes the logical form — and this supplementation is required for truth-conditional evaluation, not merely for pragmatic interpretation."

- question: "Semantic minimalism holds that most ordinary sentences require substantial pragmatic input from context to determine their literal, truth-conditional content."
  type: true-false
  answer: false
  explanation: "Semantic minimalism holds the opposite: sentences have minimal, context-independent truth conditions determined by grammar and lexicon alone, and pragmatic context affects only what is communicated beyond the literal meaning. It is *contextualism* that holds context shapes not just implicature but the literal truth-conditional content of ordinary sentences. The debate between minimalism and contextualism is precisely about whether phenomena like 'It is raining' show that context enters into literal meaning (contextualism) or whether the sentence already has complete (if very minimal) truth conditions that context merely enriches conversationally (minimalism)."

- question: "Why does 'It is raining' fail to express a complete proposition without context, and how is this different from mere Gricean implicature?"
  type: short-answer
  answer: "The sentence 'It is raining' has no explicit location or time argument, yet raining is always raining *somewhere*. The proposition 'it is raining somewhere at some time' is trivially true and not what the sentence communicates. To get a truth-evaluable proposition — one that could actually be true or false in a way that matters — context must supply at least a location: 'it is raining here, now.' This contextual input completes the logical form of the sentence, not just what the speaker communicates by it. Gricean implicature is different: in implicature, the sentence already has complete literal truth conditions, and pragmatic inference adds communicated meaning *beyond* those conditions. Here, the problem is prior: the sentence cannot even be evaluated for truth before context fills the gap. The context is determining literal content, not just conversational content above and beyond it."
```

## Explainer

From your study of truth conditions, you know that a sentence's meaning can be captured by specifying the conditions under which it is true. And from the semantics/pragmatics boundary, you know that what a sentence means (semantics) and what a speaker communicates by using it (pragmatics) can come apart. Semantic underdetermination brings these two insights together in a sharp way: even the literal, conventional meaning of a sentence — its semantic content — often underdetermines what proposition it expresses, and context must supply the missing content.

Consider "It is raining." This is grammatically complete and syntactically unambiguous. But what proposition does it express? Rain somewhere? Rain here, now? Rain in the location relevant to the conversation? The sentence doesn't specify a time or place — those parameters are implicit and must be filled in contextually. The **truth-conditional content** of the sentence is incomplete without context. This is not mere ambiguity (where a word has two dictionary meanings) and not mere implicature (where the literal content is enriched by conversational inference). It is a case where the **logical form itself** leaves open a variable that context must saturate.

**Semantic underdetermination** is pervasive in natural language. "I've had enough." (Enough of what?) "Everyone left." (Everyone in the universe, or everyone contextually salient?) "Steel is stronger than plastic." (Stronger how, under what conditions, in what configurations?) These sentences all require contextual supplementation before they express a determinate, evaluable proposition — before we can even ask whether they are true or false. Stanley, Sperber and Wilson, and others have mapped the various mechanisms: **free enrichment** (context adds content with no grammatical slot to receive it), **saturation of implicit arguments** (grammar posits a variable that context fills), and **loosening** (context shifts the truth-conditional boundaries of predicates).

The philosophical significance is this: the traditional picture of semantics as fully autonomous — sentences having complete truth conditions fixed by grammar and lexicon alone — turns out to be false for most ordinary utterances. The boundary between what is semantically encoded and what is pragmatically supplied is not clean. This challenges strong **semantic minimalism** (the view that sentences have minimal truth conditions independent of context) and supports **contextualism**: the view that context shapes not just what is conversationally communicated but what is literally expressed. Understanding underdetermination is prerequisite to evaluating the semantics-pragmatics debate, indexicality, and the proper scope of formal semantic theories.
