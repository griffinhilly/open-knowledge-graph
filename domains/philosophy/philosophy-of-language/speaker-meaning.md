---
id: speaker-meaning
title: Speaker Meaning vs. Sentence Meaning
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: grice-conversational-implicature
  type: hard
builds-toward:
- pragmatics-semantics-boundary
- metaphor-and-figurative-language
tags:
- speaker-meaning
- intention
- pragmatics
- semantics
stage: abstract-reasoning
status: draft
---

# Speaker Meaning vs. Sentence Meaning

## Core Idea
Speaker meaning is what a speaker intends to communicate by an utterance—distinct from sentence meaning, which is determined by language conventions. When I say 'That's brilliant!' about a student's obviously wrong answer, my speaker meaning is critical disapproval, though the sentence literally expresses approval. Speaker meaning explains irony, metaphor, indirect speech acts, and how context shapes interpretation.

## How It's Best Learned
Consider cases where speaker meaning diverges sharply from sentence meaning (irony, sarcasm, indirect requests) and ask what determines what the speaker means. Then investigate whether speaker meaning should be incorporated into semantic theories or kept separate.

## Common Misconceptions
Speaker meaning is just what I happen to be thinking—Grice argued it involves complex intentions about the hearer's recognition of one's intentions. Speaker meaning determines sentence meaning—most semanticists argue the reverse.

## Questions

```yaml
- question: "Someone standing by an open window says, 'It's cold in here.' The room temperature is actually 65°F. What is the speaker meaning of the utterance?"
  type: multiple-choice
  options:
    - "A sincere report that the room temperature is below comfortable levels"
    - "An indirect request to close the window, using a statement about temperature"
    - "A false statement, since 65°F is not objectively cold"
    - "An expression of emotional discomfort unrelated to the window"
  answer: 1
  explanation: "The sentence meaning of 'It's cold in here' is a statement about the temperature. But in context — standing next to an open window — the speaker meaning is almost certainly an indirect speech act: a request to close the window. The speaker intends the hearer to recognize this and act accordingly. This illustrates why speaker meaning and sentence meaning must be tracked separately: the same sentence can serve completely different communicative functions depending on context and the speaker's intentions. Option A is what you would get if you only paid attention to sentence meaning."

- question: "When someone says 'Yeah, right' sarcastically after a friend's implausible excuse, Grice's account explains that the irony works because:"
  type: multiple-choice
  options:
    - "The words have developed a new conventional meaning in casual speech that is opposite to the literal meaning"
    - "The speaker intends to communicate the opposite of the sentence meaning, and relies on the hearer recognizing this intention"
    - "Irony is a failure of communication where the speaker's intentions are hidden from the hearer"
    - "The sentence meaning and speaker meaning happen to coincide in ironic utterances"
  answer: 1
  explanation: "On the Gricean account, irony is not a matter of new word meanings — 'Yeah, right' still has its literal meaning. Irony works through a layered structure of intentions: the speaker means the opposite of what the words say, intends the hearer to recognize this, and intends that recognition itself to produce the communicative effect (conveying disbelief or mockery). The key is that both parties are aware of the gap between sentence meaning and speaker meaning. Strip away that mutual recognition, and irony would be misunderstood as sincere agreement."

- question: "Speaker meaning can be the complete opposite of sentence meaning, as in irony."
  type: true-false
  answer: true
  explanation: "This is one of the most striking demonstrations of the sentence meaning / speaker meaning gap. When someone says 'That's just brilliant!' about an obviously terrible idea, the sentence meaning expresses genuine approval; the speaker meaning is critical disapproval. Both are real — the irony works precisely because the hearer can track both levels simultaneously. This shows that speaker meaning is not constrained to be a subset of or extension of sentence meaning; it can diverge radically, even being the logical opposite."

- question: "Speaker meaning is simply whatever the speaker is currently thinking or feeling at the moment of utterance."
  type: true-false
  answer: false
  explanation: "Grice argued that speaker meaning is not merely a psychological state — it has a specific structure. To mean something, the speaker must (1) intend to produce an effect in the hearer, (2) intend the hearer to recognize that intention, and (3) intend that recognition to play a role in producing the effect. This layered intentionality is what distinguishes genuine communication from accidental signaling. If I sneeze and you infer I am sick, my sneezing doesn't mean 'I am sick' in the speaker-meaning sense — there was no intention structured around your recognition. Speaker meaning requires communicative intent, not just any mental content."

- question: "Why, according to Grice's account, is speaker meaning not simply 'whatever the speaker has in mind'? What makes it a specifically communicative kind of meaning?"
  type: short-answer
  answer: "Speaker meaning, on Grice's account, requires a specific structure of intentions: the speaker must intend to produce an effect in the hearer by means of the hearer's recognition of that very intention. This reflexive, mutual-recognition structure is what distinguishes genuine communication from accidental information transfer. A sneeze can convey that someone is sick, but the sneezer doesn't mean 'I am sick' — there was no intention structured around the hearer's recognition. Speaker meaning is essentially social and public, not just internal."
  explanation: "The Gricean analysis matters because it explains how communication can be intentional and yet also non-deceptive even when speaker meaning diverges from sentence meaning. It also has implications for the semantics/pragmatics boundary: if speaker meaning requires this complex intentional structure, then pragmatic interpretation is a sophisticated inferential process, not just 'reading minds.' The account also explains why successful irony, metaphor, and indirect speech acts require a cooperative audience — hearers must be trying to figure out what the speaker means, not just decoding word meanings."
```

## Explainer

You've already studied Gricean conversational implicature — the mechanism by which speakers convey more than what their words literally say by exploiting cooperative principles. Speaker meaning is the broader concept that implicature is a special case of: the full content of what a speaker *intends to communicate* by an utterance, which can diverge substantially from what the sentence conventionally means. Understanding this distinction requires recognizing that there are two separate questions about any utterance — what does the sentence mean, and what did the speaker mean by it?

**Sentence meaning** (also called semantic meaning or literal meaning) is determined by linguistic conventions — the systematic rules of the language that assign content to words and grammatical structures. "It's cold in here" has a fixed semantic content: a statement about the temperature of the room. **Speaker meaning** is what the speaker intends to communicate by producing that sentence in a particular context. If I say "It's cold in here" while standing next to a window you left open, my speaker meaning is probably a request to close the window — not a meteorological report. The sentence means one thing; I mean something else. Both are real, and understanding the utterance requires tracking both.

Grice's great contribution was to explain speaker meaning *without* making it arbitrary or mysterious. Speaker meaning, he argued, involves a layered structure of **intentions**: the speaker intends to produce a certain effect in the hearer (say, belief or action); the speaker intends the hearer to *recognize* that intention; and the speaker intends the recognition itself to play a role in producing the effect. This is why speaker meaning isn't just "whatever I'm thinking" — it's a communicative act structured around mutual recognition. When I say something ironically, I mean the opposite of what the words say, but I rely on you recognizing that I intend you to recognize the irony. Strip away that layered intentionality, and irony collapses into sincere assertion.

The speaker meaning / sentence meaning distinction is central to explaining a wide range of phenomena: **irony** (speaker means the opposite of sentence meaning), **metaphor** ("You are the sunshine of my life" has sentence meaning about solar radiation; speaker meaning about emotional warmth), **indirect speech acts** ("Can you pass the salt?" is literally a yes/no question about ability; speaker meaning is a request), and **conversational implicature** (what is communicated beyond what is said, via the cooperative maxims). A key theoretical question divides the field: should these speaker-meaning phenomena be handled *within* semantic theory (expanding what sentences conventionally express) or *outside* it, in a separate pragmatic theory? Most contemporary approaches maintain the semantic/pragmatic distinction, treating sentence meaning as input and speaker meaning as pragmatic output — but the boundary remains contested, and how you draw it has consequences for almost every area of the philosophy of language.
