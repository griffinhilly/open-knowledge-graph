---
id: context-dependence-utterance
title: Context-Dependence of Utterance Content
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: indexicals-context-sensitivity
  type: hard
- id: pragmatics-semantics-boundary
  type: soft
builds-toward:
- two-dimensional-semantics
tags:
- context
- pragmatics
- modulation
- semantics
stage: abstract-reasoning
status: validated
---

# Context-Dependence of Utterance Content

## Core Idea
Beyond pronouns and indexicals, utterance content often depends on context in subtle ways. "I'm hungry" means different things depending on who speaks; "That's tall" means different things for buildings versus people. Understanding when and how context determines content distinguishes semantic meaning from pragmatic content and reveals that understanding language requires extensive contextual knowledge.

## Questions

```yaml
- question: "A physicist says 'This table is not flat' and rejects it for an experiment. A carpenter says 'This table is flat' and uses it to support a glass. Are both statements true simultaneously?"
  type: multiple-choice
  options:
    - "No — 'flat' has a fixed meaning and one of them must be wrong"
    - "No — the physicist's higher standard of precision takes priority in all contexts"
    - "Yes — each utterance is evaluated against a different contextually supplied standard of precision, so both can be true"
    - "Yes — but only because the two speakers are using 'flat' as a pragmatic implicature, not in its literal semantic sense"
  answer: 2
  explanation: "On the contextualist view, gradable adjectives like 'flat' encode a standard of precision and a comparison class that context supplies. The physicist's context (quantum tunneling experiments) supplies a much stricter standard than the carpenter's (supporting a glass). The table satisfies the carpenter's standard but not the physicist's. There is no contradiction because the two utterances express different propositions. Option D is wrong — contextualists argue this is semantic, not merely pragmatic."

- question: "The sentence 'She's ready' contains no explicit indexical like 'I' or 'here,' yet its truth conditions vary with context. Which theoretical position holds that this variability affects the proposition expressed, not just what is pragmatically implied?"
  type: multiple-choice
  options:
    - "Semantic minimalism"
    - "Contextualism"
    - "Gricean implicature theory"
    - "The description theory of reference"
  answer: 1
  explanation: "Contextualism holds that what is *said* — the proposition expressed — varies with context, not just what is implied. 'She's ready' expresses a different truth-evaluable content depending on the contextually relevant task. Semantic minimalism (option A) holds the opposite: that the linguistically encoded content is thin and context-independent, with all 'filling in' happening pragmatically and not affecting the proposition itself. Gricean implicature is what gets said when the minimal content is enriched, which is the minimalist's story, not the contextualist's."

- question: "The context-dependence of gradable adjectives like 'tall' and 'empty' is merely pragmatic — these sentences express the same proposition in all contexts, and listeners infer the appropriate threshold from the situation."
  type: true-false
  answer: false
  explanation: "This is the semantic minimalist position, but contextualists argue it gets the facts wrong. If 'the glass is empty' expresses the same proposition — say, empty of all matter — in all contexts, then it is literally false in the kitchen context (since air remains). But we don't treat it as false there; we treat it as true. Contextualists take this as evidence that the truth conditions themselves shift: 'empty' in kitchen context means empty of beer, which is a semantic difference, not just a pragmatic one."

- question: "A sentence containing no pronouns or explicit indexicals — such as 'The bank is steep' — can still express different propositions in different contexts of utterance."
  type: true-false
  answer: true
  explanation: "Context-dependence extends far beyond grammatically marked indexicals. 'Bank' is lexically ambiguous (riverbank vs. financial institution), but even beyond ambiguity, context supplies standards, comparison classes, and background assumptions that determine truth conditions. The sentence 'the bank is steep' expresses a different proposition depending on whether the relevant comparison class is riverbanks, interest rates, or wheelchair ramps. This is one of the central puzzles motivating the semantics-pragmatics boundary discussion."

- question: "What is the distinction between semantic context-dependence and pragmatic context-dependence, and why does it matter?"
  type: short-answer
  answer: "Semantic context-dependence means the proposition expressed — the truth-evaluable content — varies with context. Pragmatic context-dependence means the sentence expresses the same proposition in all contexts, but what the speaker implies or communicates beyond that proposition varies. The distinction matters because it determines whether two speakers in different contexts are disagreeing about the same thing or simply expressing different things with the same words. It also matters for legal interpretation, scientific communication, and cross-cultural understanding: if context changes the proposition, disputes about 'what was said' require careful reconstruction of context."
  explanation: "The semantic/pragmatic boundary is one of the central debates in philosophy of language. Semantic minimalists want to keep the encoded content thin and context-invariant; contextualists push much of the variability inside the semantics. The stakes are high for practical domains: legal statutes are interpreted differently depending on whether one thinks they encode thin or context-saturated content, and communication failures often stem from assuming shared context when contexts actually differ."
```

## Explainer

You already know from indexicals and context-sensitivity that some expressions—"I," "here," "now," "this"—pick out different things depending on who utters them where and when. That was the straightforward case: the context-sensitivity is explicit, grammatically marked, and the shift in reference is systematic. This topic extends the phenomenon further. It turns out that a vast range of ordinary language is context-dependent in subtler ways, and sorting out *which* context-dependencies are semantic (built into the meaning of the word) versus pragmatic (inferred from the situation) is one of the central puzzles of philosophy of language.

Consider **gradable adjectives** like "tall," "flat," "empty," "ready." "That table is flat" means something different when said by a physicist checking for quantum tunneling versus a carpenter planning to set a glass on it. The word "flat" does not encode a single threshold; it encodes a **comparison class** and a **standard of precision** that the context supplies. Similarly, "The glass is empty" means empty of beer, not of air molecules; "She's ready" means ready for whatever the contextually relevant task is. These are not mere pragmatic implicatures—the truth conditions themselves shift with context. A table that is flat enough for the carpenter but not for the physicist is not both flat and not-flat in a contradictory sense; the contexts supply different standards, and both utterances can be true.

This creates a theoretical puzzle you know from the semantics/pragmatics boundary. One view—**semantic minimalism**—holds that the linguistically encoded content of a sentence is relatively thin and context-independent; all the "filling in" is pragmatic enrichment that does not affect the proposition expressed. The opposing view—**contextualism**—holds that what is said, not just what is implicated, varies with context, so the proposition expressed by "I'm hungry" genuinely differs depending on speaker, occasion, and conversational purpose. A middle position, **indexicalism**, tries to account for variability by positing hidden indexical elements in logical form—covert variables that work like "I" and "now" but are not phonologically realized.

The practical stakes are high. Legal interpretation depends on whether statutes mean what they minimally encode or what was contextually understood. Cross-cultural communication breaks down when speakers assume different background standards. Scientific communication requires extraordinary discipline to prevent context-sensitive terms from importing background assumptions. What emerges from this topic is that language is more thoroughly context-saturated than it naively appears, and the line between "what the sentence means" and "what the speaker meant by it" requires careful and often contentious drawing.
