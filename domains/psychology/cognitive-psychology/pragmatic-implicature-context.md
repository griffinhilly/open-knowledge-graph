---
id: pragmatic-implicature-context
title: Pragmatic Implicature and Context-Dependent Interpretation
domain: psychology
course: cognitive-psychology
prerequisites:
- id: language-comprehension
  type: hard
- id: theory-of-mind-development
  type: soft
builds-toward:
- sentence-comprehension-parsing
tags:
- language
- pragmatics
- meaning
- inference
stage: formal-systems
status: draft
---

# Pragmatic Implicature and Context-Dependent Interpretation

## Core Idea
Understanding an utterance requires inferring speaker intention beyond literal meaning. When someone asks 'Can you pass the salt?' they're not truly requesting information about your ability—they're implicitly requesting that you pass the salt. Pragmatic interpretation depends on shared context, mutual knowledge, and cooperative principles. Violations of these create comprehension problems or are deliberately used (e.g., irony) to communicate different meanings.

## How It's Best Learned
Analyze real conversations showing pragmatic inference and contrast with literal interpretations. Use examples like indirect requests, irony, sarcasm, and metaphor to show how context licenses non-literal meaning. Conduct experiments showing that listeners derive implicatures rapidly and unconsciously.

## Common Misconceptions
- Assuming meaning is purely compositional from word meanings; pragmatic inference creates meanings not determinable from words alone.
- Treating context effects as optional refinements; context is essential to determine what is actually communicated.

## Questions

```yaml
- question: "Someone asks 'How did John's job interview go?' and the reply is 'Well, he wore a nice tie.' According to Grice's cooperative principle, what does a listener most likely infer?"
  type: multiple-choice
  options:
    - "The speaker is avoiding the question because they don't know the answer"
    - "The speaker is implicating that John probably didn't do well but won't say so directly"
    - "The speaker thinks appearance was the most important factor in the interview"
    - "The reply violates the relation maxim and therefore carries no meaning"
  answer: 1
  explanation: "The reply seems to violate the maxim of relation (it doesn't directly answer the question), but a cooperative listener infers a meaning that rescues the assumption of cooperation: the speaker, by choosing this indirect reply, implicates that John's performance was poor but won't commit to saying so outright. This is a conversational implicature — meaning communicated without being semantically encoded. Option C misses the implicature by taking the content too literally; option A attributes ignorance where implicature is the better explanation."

- question: "A host says 'It's a bit cold in here' to a guest. The guest immediately gets up and closes the window. According to research on real-time language processing, which best describes how the guest understood the utterance?"
  type: multiple-choice
  options:
    - "As a literal temperature report, then — in a second stage — as an indirect request"
    - "As a direct request, bypassing literal meaning entirely"
    - "As an indirect request derived through cooperative inference, without a prior context-free literal stage"
    - "As a violation of the quality maxim, triggering ironic interpretation"
  answer: 2
  explanation: "Research shows context is applied immediately during comprehension, not as a post-hoc correction on top of a literal reading. There is no evidence for a two-stage model in which listeners first recover 'the literal meaning' and then adjust. Option A represents the intuitive but empirically unsupported view. Option B is also wrong — the guest did pass through inferential processing, just not a two-stage one. The pragmatic and literal aspects of meaning are processed in parallel, constrained from the start by the cooperative context."

- question: "Conversational implicatures are cancelable — a speaker can say 'She told some of the students' and then add '...in fact, she told all of them' without logical contradiction."
  type: true-false
  answer: true
  explanation: "Cancelability is the defining feature that distinguishes conversational implicature from semantic entailment. 'Some' implicates 'not all' in most contexts (via the quantity maxim), but this implicature can be withdrawn without contradiction. By contrast, an entailment cannot be canceled: if 'John killed Mary' entails 'Mary is dead,' adding '...but Mary isn't dead' produces a contradiction. Cancelability is the diagnostic test Grice used to show that implicatures are inferred rather than encoded."

- question: "Pragmatic context effects are best understood as optional refinements that listeners apply after they have fully computed the literal, compositional meaning of an utterance."
  type: true-false
  answer: false
  explanation: "This is the most persistent misconception about pragmatic processing. Experimental evidence — including ERP studies showing N400 effects for pragmatically anomalous utterances and eye-tracking showing early fixations on contextually predicted words — demonstrates that context shapes comprehension from the very beginning, not as a late correction. Meaning is always meaning-in-context; there is no prior context-free stage that yields a 'pure' literal interpretation to be adjusted afterward."

- question: "Why does interpreting 'Can you pass the salt?' as a request (rather than a question about motor ability) require something like theory of mind?"
  type: short-answer
  answer: "To recover the intended meaning, the listener must model the speaker's mind: 'This person is cooperative and has chosen these words in this context — what must they intend me to infer?' This requires attributing a second-order mental state: the speaker intends the listener to understand a request, and the listener must recognize that intention. Pure word-decoding cannot yield the request meaning; the listener must reason about what a rational, cooperative agent would mean by uttering this here. Theory of mind is the cognitive mechanism underlying pragmatic inference."
  explanation: "Grice's framework is fundamentally a theory about rational agency: listeners interpret utterances by modeling speakers as intentional communicators trying to convey meaning efficiently. When the literal meaning of words is systematically inappropriate to the context, the listener doesn't conclude the speaker is irrational — they infer a meaning that makes the speaker rational. This inference requires attributing goals, beliefs, and communicative intentions to the speaker. Research on autism spectrum conditions supports this link: reduced theory-of-mind capacity correlates with slower and less accurate pragmatic inference."
```

## Explainer

You have studied language comprehension — how listeners parse sentence structure and recover literal semantic content from words and syntax. But you know from everyday experience that what a speaker means routinely exceeds what their words literally say. "Nice weather we're having" said during a storm means the opposite. "Can you pass the salt?" is a request, not a question about your motor ability. The philosopher H.P. Grice proposed that this gap is bridged by the **Cooperative Principle**: speakers and listeners implicitly assume that conversations are governed by rational cooperation. This generates four **Gricean maxims** — quantity (be as informative as required, not more), quality (say what you believe to be true), relation (be relevant), and manner (be clear and orderly). These maxims are not rules people consciously follow; they are assumptions that license inference.

The key inferential mechanism is: when a speaker appears to violate a maxim, the listener doesn't conclude the speaker is irrational — they infer a meaning that rescues the assumption of cooperation. Suppose you ask "How did Sarah do on the exam?" and the reply is "She didn't miss a single lecture." The response seems irrelevant to the question (relation maxim apparently violated). But a cooperative listener infers: "This reply must be relevant in some way — perhaps it implicates that diligence led to a good result, or that the speaker won't commit to a stronger positive claim." The inference is a **conversational implicature** — a meaning communicated but not semantically encoded. Crucially, implicatures are **cancelable**: you could add "…but she still failed" without logical contradiction, which distinguishes them from semantic entailments that cannot be canceled.

Your prerequisite in theory of mind is directly relevant here. Computing implicature requires modeling the speaker's mind: "Given that this person is cooperative and has chosen *these* words in *this* context, what must they intend me to infer?" This is second-order mental state reasoning — you attribute to the speaker an intention to communicate a particular meaning, and you recover that meaning by reasoning about what a rational agent would mean by saying this here. **Irony and sarcasm** demand even higher-order reasoning: the speaker says something they know to be false (violating quality), and the listener must detect the deliberate violation, attribute ironic intent, and recover the speaker's actual attitude. Research shows that individuals with autism spectrum conditions often process implicature more slowly or less accurately — consistent with the theory-of-mind demands of pragmatic inference.

A common intuition is that context *refines* meaning after the fact — you get the literal reading first, then adjust. Research on real-time language processing shows this is wrong. Contextual constraint is applied *immediately*, in parallel with lexical and syntactic processing, not as a post-hoc correction. In a strongly constraining context ("He spread the butter with the…"), readers begin fixating on the contextually appropriate word before encountering it. When an utterance is pragmatically anomalous — when what was said is implausible for the conversational context — processing difficulty increases measurably: reading times slow, and ERP measures show **N400** effects (the neural signature of semantic processing difficulty). Context is not an optional layer added on top of semantic comprehension; it shapes the comprehension process from the first word. Meaning is always meaning-in-context, and there is no prior context-free stage that yields "the literal interpretation" to be then adjusted.
