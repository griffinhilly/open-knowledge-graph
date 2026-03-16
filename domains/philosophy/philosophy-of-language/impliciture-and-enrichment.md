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

## Explainer

From Grice's theory of conversational implicature, you know that speakers communicate more than the literal content of their words, relying on assumptions of cooperative communication — the maxims of quality, quantity, relation, and manner — to generate **implicatures**: additional meanings that are cancellable (they can be explicitly denied without contradiction) and arise from the *manner* of saying something rather than from what is said. From the semantics-pragmatics boundary, you know the distinction between semantic content (what a sentence-type means in the language) and pragmatic content (what a speaker means on a particular occasion). **Impliciture** is a concept, associated with Kent Bach, introduced to handle a third category that doesn't fit cleanly into either box.

Consider "John is ready." Ready for *what*? The sentence is grammatically complete, but its content is truth-conditionally incomplete — you cannot evaluate it as true or false without knowing what John is supposed to be ready for. To understand what has been said, the hearer must supply a completion from context: ready for the interview, ready to eat, ready to leave. This completion is not a Gricean implicature — it cannot be cancelled. You cannot say "John is ready, but I don't mean to imply he's ready for anything in particular" without incoherence. It is also not part of the sentence's conventional meaning — the word "ready" does not encode the specific completion. The enriched content occupies a middle position: it is implicitly communicated *as part of what is said*, not alongside it.

**Semantic underdetermination** of this kind is pervasive in natural language. "Every bottle is empty" (empty of what? — there is implicit domain restriction). "She's had enough" (enough for what purpose?). "The meeting is on Friday" (which Friday? this requires temporal reference enrichment). "He took out his key and opened the door" (the word "and" encodes temporal order and causation beyond its logical meaning of conjunction). In each case, the hearer supplies content that makes the utterance truth-evaluable, and this enrichment is required for understanding *what was said*, not just what was implicated beyond it. The Gricean picture — a clean division between semantic content below and pragmatic implicature above — is complicated by impliciture: pragmatic processes operate *inside* the determination of literal content.

The debate over impliciture has significant consequences for formal semantics. **Semantic minimalists** resist the conclusion that enrichment affects what is strictly said; on their view, the unenriched logical form is what is "said" in the philosophically relevant sense, and all enrichment is post-semantic communication. **Contextualists** argue that the thing actually evaluated for truth and falsity — the proposition expressed — is always enriched, making semantics irreducibly context-dependent. Impliciture occupies the contested border between these camps: it is content that seems essential to truth conditions yet arises through pragmatic processes. Working out where it falls is one of the central unresolved problems in philosophy of language, and the answer has implications for how compositional semantics is formulated.
