---
id: pragmatics-semantics-boundary
title: The Pragmatics-Semantics Distinction
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: grice-conversational-implicature
  type: hard
- id: what-is-said-grice
  type: soft
builds-toward:
- metaphor-and-figurative-language
- vagueness-sorites-paradox
tags:
- pragmatics
- semantics
- context
- meaning
stage: abstract-reasoning
status: validated
---
# The Pragmatics-Semantics Distinction

## Core Idea
Semantics studies meaning determined by language conventions—what is literally said; pragmatics studies meaning determined by context, speaker intentions, and reasoning—what is implicated or meant. Yet the boundary is contested. Context influences truth-conditions (indexicals); pragmatic principles (relevance, informativeness) influence interpretation; figurative meaning blurs the line. Resolving the boundary matters for semantic theory: is pragmatic reasoning part of meaning-determination or separate?

## How It's Best Learned
Study cases where pragmatic and semantic contributions are hard to untangle: scalar implicatures ('Some students passed' implicates not all—semantic or pragmatic?), presupposition, and non-literal language. Use concrete examples to test where the boundary lies.

## Common Misconceptions
Pragmatics is just context—pragmatics studies how context and speaker intentions affect meaning; the mechanisms are non-trivial. The pragmatics-semantics boundary is sharp and pre-theoretic—it's a theoretical boundary that different theories place differently.

## Questions

```yaml
- question: "A speaker says 'Some students passed the exam.' A listener infers 'Not all students passed.' Which of the following best describes the current status of this inference in linguistics?"
  type: multiple-choice
  options:
    - "It is clearly a pragmatic inference derived by the Gricean maxim of quantity, not part of the sentence's semantic content"
    - "It is clearly a semantic entailment encoded by the word 'some'"
    - "It is a contested case: some theorists treat it as pragmatic implicature, others argue it is semantically encoded"
    - "It is neither semantic nor pragmatic — it is a logical deduction from the quantifier"
  answer: 2
  explanation: "Scalar implicatures sit precisely at the contested boundary between semantics and pragmatics. The Gricean view treats 'not all' as a pragmatic inference triggered by the maxim of quantity — if the speaker knew all students passed, they would have said so. But some theorists argue the inference is so systematic and automatic that it is part of the semantic content of 'some' itself. This dispute is not merely terminological; it has empirical consequences and remains actively contested with cross-linguistic evidence on both sides."

- question: "The sentence 'I am hungry' is true when a hungry person says it and false when they do not. This shows that:"
  type: multiple-choice
  options:
    - "The sentence's meaning is entirely determined by pragmatic inference from context"
    - "Context does semantic work — it is embedded in the truth conditions of the sentence itself, not merely added as implicature"
    - "The sentence has no stable semantic content and must be interpreted entirely afresh each time"
    - "This is a case of implicature, since the sentence's literal meaning does not include information about the speaker"
  answer: 1
  explanation: "Indexicals like 'I,' 'here,' and 'now' show that context can determine truth conditions — the very content of what is literally said — not merely what is implied beyond what is said. This is semantic context-dependence, not pragmatic implicature. The minimalist view that semantics provides a context-independent core is challenged precisely by indexicals, which require context as an input to produce any truth-evaluable semantic content at all."

- question: "The boundary between semantics and pragmatics is a pre-theoretical, natural distinction that most major theories of language agree upon in its basic outline."
  type: true-false
  answer: false
  explanation: "The boundary is a theoretical construct, and different theories draw it in different places. Minimalists like Cappelen and Lepore draw a sharp line: semantics handles grammatically encoded content and explicit indexicals; everything else is pragmatics. Contextualists argue that pragmatic processes routinely enter truth conditions, blurring the boundary. The disagreement is not about minor details but about the fundamental nature of meaning and what linguistic forms encode. The boundary's location is one of the central empirical disputes in philosophy of language."

- question: "Context can affect what a sentence literally says (its truth conditions), not only what it implies beyond what is said."
  type: true-false
  answer: true
  explanation: "This is the contextualist position, supported by cases like 'It's raining' (true only relative to a contextually determined location) and 'John is ready' (requires a contextually supplied complement). These are not cases of implicature added on top of a context-independent semantic content; the contextual contribution is needed to generate any truth-evaluable content at all. Whether this means pragmatics intrudes into semantics or that semantics is richer than minimalists allow is the contested question."

- question: "Explain why indexicals like 'I,' 'here,' and 'now' complicate the idea that semantics provides a context-independent core of meaning."
  type: short-answer
  answer: "Indexicals are expressions whose semantic value shifts with the context of utterance — 'I' refers to whoever is speaking, 'here' to the location of utterance, 'now' to the time. This means context must be consulted to determine the truth conditions of sentences containing these terms, not merely to add implicature on top of a fixed semantic core. Context is doing semantic work, not just pragmatic work."
  explanation: "The significance is that it defeats the clean picture where semantics is context-free and pragmatics adds context. If context must enter to produce any truth-evaluable semantic content, then the separation between 'what is said' (context-free semantics) and 'what is implied' (context-sensitive pragmatics) collapses for indexical sentences. Contextualists generalize from this to argue that contextual intrusion is widespread; minimalists try to contain it to a small class of grammatically marked cases."
```

## Explainer

You already know **Gricean implicature**: when a speaker's utterance is true but misleadingly incomplete, the listener infers additional meaning from the norms of cooperative conversation. If asked "Can you pass the salt?" and you reply "Yes," you have answered the semantic question (you are physically capable) but violated conversational norms by failing to cooperate. The **pragmatic** meaning — *pass the salt* — is derived not from the words alone but from context plus the assumption that speakers are being cooperative. Pragmatics studies this kind of derived, speaker-dependent meaning. Semantics studies the literal, context-independent meaning fixed by linguistic convention. The question is: where exactly does one end and the other begin?

The boundary looks clear in Grice's original framing: semantics gives you "what is said" (the truth-conditional content), and pragmatics adds implicature (what is communicated beyond what is said). But the boundary dissolves under pressure. Consider **indexicals** — words like "I," "here," "now," and "she." Their semantic values shift with context: "I am hungry" is true when a hungry speaker says it and false when they are not. Context is doing semantic work here, not merely adding implicature. Indexical-dependent truth conditions are not a stable semantics-fixed core with pragmatic additions — context is baked into the semantics itself, which already complicates the clean separation.

**Scalar implicatures** press the boundary even harder. If a listener knows the full scale ("some, most, all"), then "Some students passed the exam" implicates "Not all students passed." This feels pragmatic — it is derived by the Gricean maxim of quantity ("be as informative as required"). But the inference is so automatic and so systematically tied to the word "some" that some theorists argue it is part of the semantic content of "some" itself, not a late-arriving pragmatic inference. Whether scalar meanings are semantically encoded or pragmatically derived is a central empirical dispute in current semantics, with experimental and cross-linguistic evidence on both sides.

The deepest challenge comes from **contextualists**, who argue that pragmatic processes routinely affect truth conditions — not just what is implied but what is literally said. "It's raining" seems true only relative to a location, but no location is linguistically expressed. "John is ready" requires a complement (ready *for what?*) that is contextually supplied but not semantically present. **Minimalists** like Cappelen and Lepore resist this: the semantic content of a sentence is determined by its grammatical features and the values of its explicit indexicals, and the rest is pragmatics. Contextualists counter that minimalist semantic contents are often too thin to be the genuine objects of assertion and belief. The debate is not merely terminological — it concerns what grammatical structure encodes, how interpretation works, and what the proper targets of semantic theory are. The answer shapes how we understand meaning, communication, and the relationship between language and mind.
