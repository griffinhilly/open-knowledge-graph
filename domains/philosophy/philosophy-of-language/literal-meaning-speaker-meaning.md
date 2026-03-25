---
id: literal-meaning-speaker-meaning
title: Literal Meaning and Speaker Meaning
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: grice-cooperative-principle-maxims
  type: hard
- id: speaker-meaning
  type: hard
- id: meaning-convention-vs-intention
  type: soft
- id: conventional-implicature-meaning
  type: soft
builds-toward:
- metaphorical-meaning-and-extension
tags:
- meaning
- literal
- speaker-meaning
stage: formal-systems
status: validated
---
# Literal Meaning and Speaker Meaning

## Core Idea
The literal meaning of a sentence is determined by convention and compositional rules, while speaker meaning is what the speaker intends to communicate. These can diverge: irony, metaphor, and indirect speech acts involve cases where speaker meaning differs from literal meaning.

## Questions

```yaml
- question: "Someone says 'Oh, wonderful — another Monday morning meeting' in a tone of obvious irritation. Their colleague understands this as an expression of annoyance. What best describes what has happened?"
  type: multiple-choice
  options:
    - "The literal meaning and speaker meaning coincide — the utterance straightforwardly communicates the speaker's attitude"
    - "The speaker meaning (irritation) diverges from the literal meaning (the meeting is wonderful), and the hearer recovers speaker meaning via contextual inference"
    - "The literal meaning is indeterminate because tone of voice is not part of linguistic meaning"
    - "There is no literal meaning here because the sentence is non-literal by convention"
  answer: 1
  explanation: "This is irony: the literal meaning of 'wonderful' is positive, but the speaker means the opposite. The hearer does not decode the literal content and stop there — they use Gricean reasoning (the speaker is not lying, so something else must be intended), contextual knowledge (Monday morning meetings are often unpleasant), and tone to recover the speaker's actual communicative intention. Literal and speaker meaning diverge maximally, and the hearer bridges the gap through inference, not decoding."

- question: "A guest says to a host: 'I notice it's getting rather late.' The host understands this as a polite request to be allowed to leave. What phenomenon does this illustrate?"
  type: multiple-choice
  options:
    - "Metaphor — the speaker is using 'late' figuratively to mean something else"
    - "An indirect speech act — the speaker's literal meaning (an observation about time) diverges from their speaker meaning (a request to end the visit)"
    - "A violation of the maxim of quantity — the speaker has provided less information than required"
    - "Literal meaning and speaker meaning coincide — the observation about lateness is exactly what was intended"
  answer: 1
  explanation: "This is an indirect speech act: the sentence literally asserts a fact about the time, but its communicative function is a polite request. Recovering the speaker's meaning requires going beyond compositional semantics — the hearer must recognize that the speaker would not make this observation without a purpose, infer the purpose from context, and understand it as a request. The literal meaning is neither false nor beside the point; it provides the surface through which the actual communicative intention is conveyed. This illustrates how speaker meaning can diverge from literal meaning even in non-figurative language."

- question: "Literal meaning (sentence meaning) is context-independent — it belongs to the sentence as a type and does not vary depending on who utters it, when, or where."
  type: true-false
  answer: true
  explanation: "This is the key distinction between literal meaning and speaker meaning. 'The cat is on the mat' has the same literal meaning whoever utters it, wherever, whenever — its content is fixed by the meanings of its words and compositional rules. Speaker meaning, by contrast, is always the meaning of a token utterance: what a particular speaker intends to communicate in a particular context. The same sentence uttered ironically, metaphorically, or as an indirect speech act preserves its literal meaning while acquiring a different speaker meaning. Context-independence is what makes literal meaning systematizable and teachable."

- question: "Understanding what a speaker communicates is primarily a matter of computing the literal meaning of their sentences — grasping their communicative intention is a secondary, optional enrichment."
  type: true-false
  answer: false
  explanation: "This gets the relationship backwards. Literal meaning gives you the semantic content of the sentence type, but what the speaker actually communicates — their speaker meaning — requires modeling their communicative intention in context. In irony, metaphor, and indirect speech acts, acting on the literal meaning would systematically misunderstand the speaker. More broadly, even non-figurative communication requires inferential work beyond literal decoding: recognizing implicatures, resolving referential ambiguities, and understanding why the speaker chose to say this, here, now. Language is not a simple encoding-decoding system."

- question: "Why does the gap between literal meaning and speaker meaning show that language understanding requires modeling the speaker's mind, not just knowing linguistic conventions?"
  type: short-answer
  answer: "If language were a pure encoding-decoding system, knowing the compositional meaning of a sentence would be sufficient to understand what was communicated. But cases like irony (where speaker means the opposite of the literal), metaphor (where the literal is false but the speaker communicates something true), and indirect speech acts (where the literal is a different speech act than what's intended) all show that the literal meaning underdetermines speaker meaning. To recover what was actually communicated, you must model what the speaker intended — their goals, beliefs, context — and recognize what communicative intention the utterance was meant to trigger. Language understanding is therefore not just semantic knowledge but theory of mind."
  explanation: "Grice's analysis makes this explicit: speaker meaning is what the speaker intends the hearer to recognize as intended, in part because of recognizing that intention. This is an essentially mind-involving account — language works because speakers and hearers are mutual mind-readers, not just code-users. The philosophical implication is significant: a complete theory of linguistic communication cannot be purely syntactic and semantic; it must include pragmatics and the attribution of mental states. This is also why language acquisition requires joint attention and social cognition, not just statistical pattern-matching over linguistic input."
```

## Explainer

From your study of Grice's cooperative principle and maxims, you know that communication succeeds not just by encoding semantic content but by exploiting shared assumptions about how rational communicators behave. From your work on speaker meaning, you know Grice's account: speaker meaning is what the speaker intends the hearer to recognize as intended—it is the content of communicative intention, not the content encoded in the words. These two concepts—conventional sentence meaning and speaker communicative intention—can come apart, and understanding when and how they diverge is the core concern of this topic.

**Literal meaning** (also called **sentence meaning** or **semantic content**) is determined by two things: the meanings of the words, fixed by linguistic convention, and the compositional rules that determine how word meanings combine into sentence meanings. "The cat is on the mat" literally means whatever compositional semantics delivers from its components. This literal content belongs to the sentence as a type, not to any particular utterance—it is context-independent in the sense that it does not vary depending on who utters it or when. **Speaker meaning**, by contrast, is always the meaning of a token utterance by a particular speaker in a particular context with particular intentions.

The most illuminating cases are those where literal and speaker meaning maximally diverge. In **irony**, you say the opposite of what you mean: "Oh great, it's raining again" literally asserts that rain is good, but speaker meaning is irritation. In **metaphor**, you say something literally false but communicate something true: "She is a firework" is literally false (she is a person) but speaker meaning conveys that she is energetic and brilliant. In **indirect speech acts**, "Can you pass the salt?" is literally a question about physical ability but functions as a polite request. In all three cases, the hearer must go beyond literal meaning, using contextual knowledge and Gricean inference to recover what the speaker actually means.

The philosophical significance extends beyond cataloging figures of speech. The gap between literal and speaker meaning shows that language is not a simple encoding-decoding system. Successful communication depends on shared background knowledge, inferential capacity, and recognition of communicative intentions—none of which is stored in words. This means that understanding language requires understanding mindedness: you must model what the speaker intends. The distinction also has practical stakes in legal interpretation, contract law, and literary theory, where debates over whether to privilege literal meaning or speaker and author intent have no purely linguistic resolution.
