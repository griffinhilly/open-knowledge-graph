---
id: impliciture-and-enrichment
title: Impliciture and Content Enrichment
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: grice-conversational-implicature
  type: hard
- id: pragmatics-semantics-boundary
  type: hard
builds-toward:
- semantic-underdetermination-context
- literal-meaning-speaker-meaning
tags:
- impliciture
- pragmatics
- content
stage: advanced
status: draft
---

# Impliciture and Content Enrichment

## Core Idea
Impliciture refers to implicit but determinate content that enriches what is literally said, falling between explicit assertion and genuine implicature. This content is often required for coherence and is not cancellable like typical conversational implicatures.

## How It's Best Learned
Compare cases like 'He's in the garden' (domain restriction on 'the garden') with clear cases of implicature and with literalism, to locate impliciture in the space of meaning types.

## Questions

```yaml
- question: "Someone says 'I've had enough.' The hearer enriches this to mean 'I've had enough to eat.' This enriched content is best classified as:"
  type: multiple-choice
  options:
    - "A Gricean conversational implicature — arising from cooperative communication norms and cancellable by explicit denial"
    - "An impliciture — pragmatically supplied content required for truth-evaluation, and not cancellable"
    - "Part of the conventional semantic meaning of 'enough'"
    - "A presupposition — assumed as background for the utterance"
  answer: 1
  explanation: "This is impliciture in Kent Bach's sense. It is NOT a Gricean implicature because it cannot be cancelled — 'I've had enough, but I don't mean enough of anything' is incoherent (option A fails: Gricean implicatures ARE cancellable). It is NOT part of the semantic meaning of 'enough' (option C). It is not a presupposition (option D). It is pragmatically supplied context that is required to make the utterance truth-evaluable — the hallmark of impliciture."

- question: "Semantic minimalists and contextualists disagree about impliciture. Which statement correctly characterizes their disagreement?"
  type: multiple-choice
  options:
    - "Minimalists say enrichment affects truth conditions; contextualists say it is purely post-semantic communication"
    - "Minimalists say 'what is said' is the unenriched logical form; contextualists say the truth-evaluable proposition is always pragmatically enriched"
    - "Both accept that enrichment affects truth conditions but disagree about whether it is conscious or automatic"
    - "Minimalists deny that pragmatic processes exist; contextualists deny that semantic content is stable across utterances"
  answer: 1
  explanation: "Semantic minimalists hold that the proposition strictly 'said' is the minimal semantic content fixed by linguistic convention — enrichment happens post-semantically in communication. Contextualists hold that the proposition actually evaluated for truth is always enriched by context, making semantics irreducibly context-dependent. Impliciture sits exactly at this fault line: it is pragmatically supplied, required for truth conditions, but not encoded conventionally."

- question: "Unlike Gricean implicature, impliciture cannot be cancelled without producing incoherence."
  type: true-false
  answer: true
  explanation: "Cancellability is the defining mark of Gricean conversational implicature — you can say 'He finished the test, and I don't mean to suggest he finished on time.' But you cannot say 'John is ready, though I don't mean to imply he's ready for anything in particular' without incoherence. The enrichment is required for 'John is ready' to express a truth-evaluable proposition at all, making it non-cancellable and thus categorically distinct from implicature."

- question: "Impliciture is simply another name for what Grice called conversational implicature — both refer to pragmatically communicated meaning that goes beyond the sentence's literal content."
  type: true-false
  answer: false
  explanation: "Bach introduced 'impliciture' precisely to carve out a category Grice's framework obscures. Gricean implicature lies beyond what is said — it is additional content communicated alongside the proposition expressed. Impliciture enriches what is said — it affects the proposition itself and its truth conditions. Implicatures are cancellable; implicitures are not. They occupy different positions in the architecture of meaning: one post-semantic, one constitutive of content."

- question: "Explain why impliciture creates a problem for the standard view that semantics and pragmatics can be cleanly separated."
  type: short-answer
  answer: "The standard picture assigns semantics the job of determining truth-conditional content from linguistic form, and pragmatics the job of explaining what is communicated beyond that content. Impliciture breaks this picture: pragmatic enrichment processes operate inside the determination of what is said — they are needed to produce a truth-evaluable proposition at all. 'John is ready' has no truth-evaluable content without a contextually supplied completion, yet 'ready for X' is not part of the conventional meaning of 'ready.' Pragmatics does not merely add to a complete semantic output; it participates in generating that output. Semantics cannot deliver a complete truth-evaluable proposition without pragmatic input, collapsing the assumed sequential structure of the two levels."
  explanation: "This has downstream consequences for formal semantics: if truth conditions are always pragmatically enriched, a context-free semantics cannot correctly specify when sentences are true. The minimalism/contextualism debate is essentially a debate about how deep this entanglement goes and whether a useful notion of 'minimal semantic content' can be salvaged."
```

## Explainer

From Grice's theory of conversational implicature, you know that speakers communicate more than the literal content of their words, relying on assumptions of cooperative communication — the maxims of quality, quantity, relation, and manner — to generate **implicatures**: additional meanings that are cancellable (they can be explicitly denied without contradiction) and arise from the *manner* of saying something rather than from what is said. From the semantics-pragmatics boundary, you know the distinction between semantic content (what a sentence-type means in the language) and pragmatic content (what a speaker means on a particular occasion). **Impliciture** is a concept, associated with Kent Bach, introduced to handle a third category that doesn't fit cleanly into either box.

Consider "John is ready." Ready for *what*? The sentence is grammatically complete, but its content is truth-conditionally incomplete — you cannot evaluate it as true or false without knowing what John is supposed to be ready for. To understand what has been said, the hearer must supply a completion from context: ready for the interview, ready to eat, ready to leave. This completion is not a Gricean implicature — it cannot be cancelled. You cannot say "John is ready, but I don't mean to imply he's ready for anything in particular" without incoherence. It is also not part of the sentence's conventional meaning — the word "ready" does not encode the specific completion. The enriched content occupies a middle position: it is implicitly communicated *as part of what is said*, not alongside it.

**Semantic underdetermination** of this kind is pervasive in natural language. "Every bottle is empty" (empty of what? — there is implicit domain restriction). "She's had enough" (enough for what purpose?). "The meeting is on Friday" (which Friday? this requires temporal reference enrichment). "He took out his key and opened the door" (the word "and" encodes temporal order and causation beyond its logical meaning of conjunction). In each case, the hearer supplies content that makes the utterance truth-evaluable, and this enrichment is required for understanding *what was said*, not just what was implicated beyond it. The Gricean picture — a clean division between semantic content below and pragmatic implicature above — is complicated by impliciture: pragmatic processes operate *inside* the determination of literal content.

The debate over impliciture has significant consequences for formal semantics. **Semantic minimalists** resist the conclusion that enrichment affects what is strictly said; on their view, the unenriched logical form is what is "said" in the philosophically relevant sense, and all enrichment is post-semantic communication. **Contextualists** argue that the thing actually evaluated for truth and falsity — the proposition expressed — is always enriched, making semantics irreducibly context-dependent. Impliciture occupies the contested border between these camps: it is content that seems essential to truth conditions yet arises through pragmatic processes. Working out where it falls is one of the central unresolved problems in philosophy of language, and the answer has implications for how compositional semantics is formulated.
